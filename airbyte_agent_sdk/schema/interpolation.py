"""Date-macro interpolation for replication_config_constants.

Provides a sandboxed Jinja2 environment with date macros compatible with
the airbyte-python-cdk (`now_utc`, `today_utc`, `day_delta`).

String values containing `{{` are treated as Jinja2 templates and rendered
at resolve time.  Non-string values and plain strings pass through unchanged.

Example YAML usage::

    replication_config_constants:
      start_date: "{{ day_delta(-730, '%Y-%m-%dT%H:%M:%SZ') }}"
"""

from collections.abc import Mapping
from datetime import UTC, datetime, timedelta
from typing import Any

from jinja2.sandbox import SandboxedEnvironment


def _now_utc() -> datetime:
    """Current UTC datetime (matches CDK `now_utc()`)."""
    return datetime.now(UTC)


def _today_utc() -> datetime:
    """Midnight of the current UTC date (matches CDK `today_utc()`)."""
    return datetime.now(UTC).replace(hour=0, minute=0, second=0, microsecond=0)


def _day_delta(num_days: int, format: str = "%Y-%m-%dT%H:%M:%SZ") -> str:
    """Return `now_utc() + num_days` formatted as a string (matches CDK `day_delta()`)."""
    return (datetime.now(UTC) + timedelta(days=num_days)).strftime(format)


_JINJA_ENV = SandboxedEnvironment()
_JINJA_ENV.globals.update(
    {
        "now_utc": _now_utc,
        "today_utc": _today_utc,
        "day_delta": _day_delta,
    }
)


def resolve_interpolated_constants(constants: Mapping[str, Any]) -> dict[str, Any]:
    """Evaluate Jinja2 date expressions inside constant values.

    Only string values containing `{{` are rendered as templates.
    All other types are returned as-is.
    """
    resolved: dict[str, Any] = {}
    for key, value in constants.items():
        if isinstance(value, str) and "{{" in value:
            resolved[key] = _JINJA_ENV.from_string(value).render()
        else:
            resolved[key] = value
    return resolved
