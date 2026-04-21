"""
Gmail connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import GmailConnector
from .models import (
    GmailAuthConfig,
    GmailReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    ProfileSearchData,
    ProfileSearchResult,
    MessagesSearchData,
    MessagesSearchResult,
    LabelsSearchData,
    LabelsSearchResult,
    DraftsSearchData,
    DraftsSearchResult,
    ThreadsSearchData,
    ThreadsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "GmailConnector",
    "AirbyteAuthConfig",
    "GmailAuthConfig",
    "GmailReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "ProfileSearchData",
    "ProfileSearchResult",
    "MessagesSearchData",
    "MessagesSearchResult",
    "LabelsSearchData",
    "LabelsSearchResult",
    "DraftsSearchData",
    "DraftsSearchResult",
    "ThreadsSearchData",
    "ThreadsSearchResult",
]