"""
Zendesk-Chat connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import ZendeskChatConnector
from .models import (
    ZendeskChatAuthConfig,
    ZendeskChatReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AgentsSearchData,
    AgentsSearchResult,
    ChatsSearchData,
    ChatsSearchResult,
    DepartmentsSearchData,
    DepartmentsSearchResult,
    ShortcutsSearchData,
    ShortcutsSearchResult,
    TriggersSearchData,
    TriggersSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "ZendeskChatConnector",
    "AirbyteAuthConfig",
    "ZendeskChatAuthConfig",
    "ZendeskChatReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "AgentsSearchData",
    "AgentsSearchResult",
    "ChatsSearchData",
    "ChatsSearchResult",
    "DepartmentsSearchData",
    "DepartmentsSearchResult",
    "ShortcutsSearchData",
    "ShortcutsSearchResult",
    "TriggersSearchData",
    "TriggersSearchResult",
]