"""Deprecated action-name aliases kept for a migration window.

Scrub plan (target: after 2026-10-01): delete this module, remove its call sites
(grep `deprecated_action_aliases`), and delete `tests/test_deprecated_action_aliases.py`.
Orb metering intentionally keeps reporting `api_search` (see `_ORB_TOOL_CALLS_ACTION_ALIASES`
in `backend/app/core/orb_outbox.py`); leave that mapping in place unless billing agrees to rename.
"""

import logging
import warnings
from datetime import UTC, datetime
from typing import Final

logger = logging.getLogger(__name__)

DEPRECATED_ACTION_ALIASES: Final[dict[str, str]] = {"api_search": "search"}

# Before this date, event-history rows with action "search" recorded a Context Store search
# (the raw API search was "api_search"; Context Store search was renamed "context_store_search"
# in April 2026). Rows on/after it with action "search" are raw API searches.
LEGACY_CONTEXT_STORE_SEARCH_CUTOFF: Final[datetime] = datetime(2026, 9, 1, tzinfo=UTC)


def resolve_action_alias(action: str) -> str:
    canonical = DEPRECATED_ACTION_ALIASES.get(action)
    if canonical is None:
        return action
    warnings.warn(f"Action '{action}' is deprecated; use '{canonical}'.", DeprecationWarning, stacklevel=2)
    logger.info("Deprecated action alias used", extra={"action": action, "canonical": canonical})
    return canonical
