"""Canonical redaction logic for the Airbyte Agent SDK.

This module is the **single source of truth** for all secret-scrubbing
deny-lists and redaction helpers used across the SDK.  Every emission
boundary (telemetry, request logger, cassette recorder) imports from
here — no other module should define its own sensitive-key list.

Explicit exclusions (out of scope for this module):
- **OpenTelemetry span attributes** — spans are consumed by the host's
  own tracer provider; redacting them requires tracer-provider middleware,
  not call-site wrapping.
- **OAuth2 token-refresh traffic** — `OAuth2TokenRefresher` uses a
  standalone `httpx.AsyncClient` that never flows through the SDK logger.
  If refresh traffic is ever wired through `RequestLogger`, the body/
  response redaction will catch it automatically.
- **In-memory traceback scrubbing** — frame-local dict scanning is a
  separate, larger problem.  This module defends the *emission*
  boundaries, not the construction sites.
"""

import re
from collections.abc import Collection, Mapping
from typing import Any
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

# ---------------------------------------------------------------------------
# Key-name deny-lists
# ---------------------------------------------------------------------------

SENSITIVE_HEADER_PATTERNS: list[str] = [
    "authorization",
    "api-key",
    "x-api-key",
    "token",
    "bearer",
    "secret",
    "password",
    "credential",
    "cookie",
    "set-cookie",
]
"""Substring patterns matched against header names (case-insensitive).

Used by `redact_headers` and by the cassette recorder's `_filter_headers`
(which drops matching request headers entirely instead of replacing their
values).
"""

SENSITIVE_PARAM_PATTERNS: list[str] = [
    "password",
    "secret",
    "api_key",
    "apikey",
    "token",
    "credentials",
    "auth",
    "key",
]
"""Substring patterns matched against query-param names (case-insensitive)."""

RECURSIVE_KEY_NAMES: frozenset[str] = frozenset(
    {
        "authorization",
        "api_key",
        "apikey",
        "api-key",
        "x-api-key",
        "access_token",
        "refresh_token",
        "id_token",
        "bearer",
        "bearer_token",
        "password",
        "passwd",
        "secret",
        "client_secret",
        "credential",
        "credentials",
        "token",
        "session_token",
        "private_key",
        "set-cookie",
        "cookie",
    }
)
"""Exact key names (case-insensitive) for recursive dict/body redaction.

Kept deliberately narrower than the legacy substring lists used by
`redact_headers`/`redact_params`.  The broad substrings "auth" and "key"
would eat fields like "author", "keyword", or "api_key_prefix" when
applied recursively to arbitrary JSON bodies.
"""

# ---------------------------------------------------------------------------
# Value-shape patterns  (compiled once at import time)
# ---------------------------------------------------------------------------

_VALUE_PATTERN_SOURCES: list[tuple[str, str]] = [
    # Stripe / OpenAI-style prefixed keys
    # https://docs.stripe.com/keys
    (r"sk_(live|test)_[A-Za-z0-9]{16,}", "Stripe/OpenAI-style secret key"),
    # Stripe restricted keys
    (r"rk_(live|test)_[A-Za-z0-9]{16,}", "Stripe restricted key"),
    # Stripe webhook secrets
    (r"whsec_[A-Za-z0-9]{32,}", "Stripe webhook secret"),
    # GitHub PAT / OAuth / server tokens
    # https://github.blog/changelog/2021-03-31-authentication-token-format-updates/
    (r"gh[poas]_[A-Za-z0-9]{30,}", "GitHub token"),
    # GitHub fine-grained PATs
    (r"github_pat_[A-Za-z0-9_]{80,}", "GitHub fine-grained PAT"),
    # Slack bot / app / user tokens
    # https://api.slack.com/authentication/token-types
    (r"xox[baprs]-[A-Za-z0-9\-]{10,}", "Slack token"),
    # Slack app-level tokens
    (r"xapp-[A-Za-z0-9\-]{10,}", "Slack app-level token"),
    # Google API key (fixed 39-char body)
    # https://cloud.google.com/docs/authentication/api-keys
    (r"AIza[A-Za-z0-9_\-]{35}", "Google API key"),
    # AWS access key ID (always starts AKIA, 20 chars total)
    # https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html
    (r"AKIA[A-Z0-9]{16}", "AWS access key ID"),
    # JWT (three dot-separated base64url segments)
    # https://datatracker.ietf.org/doc/html/rfc7519
    (r"eyJ[A-Za-z0-9_\-]{5,}\.[A-Za-z0-9_\-]{5,}\.[A-Za-z0-9_\-]{5,}", "JWT"),
]

VALUE_PATTERNS: list[re.Pattern[str]] = [re.compile(src) for src, _doc in _VALUE_PATTERN_SOURCES]

# Generic high-entropy pattern — only used when `aggressive=True`
# (cassette recording path).  False-positive rate is too high for
# telemetry / logging.
_AGGRESSIVE_PATTERN: re.Pattern[str] = re.compile(r"[A-Za-z0-9+/_\-]{40,}={0,2}")

_MAX_DEPTH = 32
_REDACTION_MARKER = "***REDACTED***"


class DataRedactor:
    """Canonical redaction helpers for the Airbyte Agent SDK.

    All methods are ``@staticmethod`` — no instance state is needed.
    """

    # Expose constants as class-level attributes for import convenience.
    SENSITIVE_HEADER_PATTERNS = SENSITIVE_HEADER_PATTERNS
    SENSITIVE_PARAM_PATTERNS = SENSITIVE_PARAM_PATTERNS
    RECURSIVE_KEY_NAMES = RECURSIVE_KEY_NAMES
    VALUE_PATTERNS = VALUE_PATTERNS

    @staticmethod
    def redact_headers(headers: dict[str, str], *, marker: str = _REDACTION_MARKER) -> dict[str, str]:
        """Redact sensitive headers by key-name substring match."""
        redacted: dict[str, str] = {}
        for key, value in headers.items():
            if any(pattern in key.lower() for pattern in SENSITIVE_HEADER_PATTERNS):
                redacted[key] = marker
            else:
                redacted[key] = value
        return redacted

    @staticmethod
    def redact_params(params: dict[str, Any]) -> dict[str, Any]:
        """Redact sensitive parameters by key-name substring match."""
        redacted: dict[str, Any] = {}
        for key, value in params.items():
            if any(pattern in key.lower() for pattern in SENSITIVE_PARAM_PATTERNS):
                redacted[key] = _REDACTION_MARKER
            else:
                redacted[key] = value
        return redacted

    @staticmethod
    def redact_url(url: str) -> str:
        """Redact sensitive query params, userinfo, and fragment from a URL string."""
        parsed = urlparse(url)

        # Scrub userinfo (user:password@host)
        netloc = parsed.netloc
        if "@" in netloc:
            host_part = netloc.rsplit("@", 1)[1]
            netloc = f"{_REDACTION_MARKER}@{host_part}"

        # Scrub query params by key name
        new_query = parsed.query
        if parsed.query:
            params = parse_qs(parsed.query)
            redacted_params: dict[str, list[str]] = {}
            for key, values in params.items():
                if any(pattern in key.lower() for pattern in SENSITIVE_PARAM_PATTERNS):
                    redacted_params[key] = [_REDACTION_MARKER] * len(values)
                else:
                    redacted_params[key] = values
            new_query = urlencode(redacted_params, doseq=True)

        # Scrub fragment params (OAuth implicit flow)
        new_fragment = parsed.fragment
        if parsed.fragment and "=" in parsed.fragment:
            frag_params = parse_qs(parsed.fragment)
            redacted_frag: dict[str, list[str]] = {}
            for key, values in frag_params.items():
                if any(pattern in key.lower() for pattern in SENSITIVE_PARAM_PATTERNS):
                    redacted_frag[key] = [_REDACTION_MARKER] * len(values)
                else:
                    redacted_frag[key] = values
            new_fragment = urlencode(redacted_frag, doseq=True)

        return urlunparse(
            (
                parsed.scheme,
                netloc,
                parsed.path,
                parsed.params,
                new_query,
                new_fragment,
            )
        )

    # ------------------------------------------------------------------
    # New public surface — value-shape + recursive redaction
    # ------------------------------------------------------------------

    @staticmethod
    def redact_value(value: Any, *, aggressive: bool = False) -> Any:
        """Replace VALUE_PATTERNS matches in `value` with the redaction marker.

        Key-name matching is NOT performed here; callers should use
        `redact_mapping` for key-name + value-shape combined redaction.

        When `aggressive` is True the generic high-entropy pattern is
        also applied.  This is intended **only** for the cassette
        recording path where false positives redact test-only data.

        Non-string inputs are returned unchanged.
        """
        if not isinstance(value, str):
            return value
        for pattern in VALUE_PATTERNS:
            value = pattern.sub(_REDACTION_MARKER, value)
        if aggressive:
            value = _AGGRESSIVE_PATTERN.sub(_REDACTION_MARKER, value)
        return value

    @staticmethod
    def redact_string(text: Any, *, aggressive: bool = False) -> Any:
        """Apply value-shape redaction to an unstructured string.

        Suitable for log lines, exception messages, or URL path segments.
        Non-string inputs are returned unchanged.
        """
        return DataRedactor.redact_value(text, aggressive=aggressive)

    @staticmethod
    def redact_mapping(
        data: Mapping[str, Any],
        *,
        key_names: Collection[str] | None = None,
        aggressive: bool = False,
    ) -> dict[str, Any]:
        """Recursive deep-copy redactor for dicts (Segment properties, JSON bodies, request logs).

        - `key_names` defaults to `RECURSIVE_KEY_NAMES` (narrow, boundary-safe).
        - If a key (case-insensitive exact match) is in `key_names`, the
          entire value is replaced with the marker regardless of shape.
        - Otherwise, string values are passed through `redact_value`.
        - Dicts and lists are walked recursively; other scalars pass
          through unchanged.
        - Uses an `id()`-based seen-set to handle reference cycles.
        - Caps recursion depth at 32; on overflow, substitutes
          `{"__redacted__": "max_depth_exceeded"}` for the subtree.
        """
        if key_names is None:
            key_names = RECURSIVE_KEY_NAMES

        seen: set[int] = set()

        def _redact(obj: Any, depth: int) -> Any:
            if depth > _MAX_DEPTH:
                return {"__redacted__": "max_depth_exceeded"}

            obj_id = id(obj)
            if obj_id in seen:
                return _REDACTION_MARKER
            seen.add(obj_id)

            try:
                if isinstance(obj, dict):
                    result: dict[str, Any] = {}
                    for k, v in obj.items():
                        if isinstance(k, str) and k.lower() in key_names:
                            result[k] = _REDACTION_MARKER
                        else:
                            result[k] = _redact(v, depth + 1)
                    return result

                if isinstance(obj, (list, tuple)):
                    return [_redact(item, depth + 1) for item in obj]

                if isinstance(obj, str):
                    return DataRedactor.redact_value(obj, aggressive=aggressive)

                return obj
            finally:
                seen.discard(obj_id)

        return _redact(data, 0)
