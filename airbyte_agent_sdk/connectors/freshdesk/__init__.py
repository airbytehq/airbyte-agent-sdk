"""
Freshdesk connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import FreshdeskConnector
from .models import (
    FreshdeskAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    TicketsSearchData,
    TicketsSearchResult,
    AgentsSearchData,
    AgentsSearchResult,
    GroupsSearchData,
    GroupsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "FreshdeskConnector",
    "AirbyteAuthConfig",
    "FreshdeskAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "TicketsSearchData",
    "TicketsSearchResult",
    "AgentsSearchData",
    "AgentsSearchResult",
    "GroupsSearchData",
    "GroupsSearchResult",
]