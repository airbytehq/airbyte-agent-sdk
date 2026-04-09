"""
Monday connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import MondayConnector
from .models import (
    MondayAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    ActivityLogsSearchData,
    ActivityLogsSearchResult,
    BoardsSearchData,
    BoardsSearchResult,
    ItemsSearchData,
    ItemsSearchResult,
    TagsSearchData,
    TagsSearchResult,
    TeamsSearchData,
    TeamsSearchResult,
    UpdatesSearchData,
    UpdatesSearchResult,
    UsersSearchData,
    UsersSearchResult,
    WorkspacesSearchData,
    WorkspacesSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "MondayConnector",
    "AirbyteAuthConfig",
    "MondayAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "ActivityLogsSearchData",
    "ActivityLogsSearchResult",
    "BoardsSearchData",
    "BoardsSearchResult",
    "ItemsSearchData",
    "ItemsSearchResult",
    "TagsSearchData",
    "TagsSearchResult",
    "TeamsSearchData",
    "TeamsSearchResult",
    "UpdatesSearchData",
    "UpdatesSearchResult",
    "UsersSearchData",
    "UsersSearchResult",
    "WorkspacesSearchData",
    "WorkspacesSearchResult",
]