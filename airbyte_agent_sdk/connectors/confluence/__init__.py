"""
Confluence connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import ConfluenceConnector
from .models import (
    ConfluenceAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AuditSearchData,
    AuditSearchResult,
    BlogPostsSearchData,
    BlogPostsSearchResult,
    GroupsSearchData,
    GroupsSearchResult,
    PagesSearchData,
    PagesSearchResult,
    SpacesSearchData,
    SpacesSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "ConfluenceConnector",
    "AirbyteAuthConfig",
    "ConfluenceAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "AuditSearchData",
    "AuditSearchResult",
    "BlogPostsSearchData",
    "BlogPostsSearchResult",
    "GroupsSearchData",
    "GroupsSearchResult",
    "PagesSearchData",
    "PagesSearchResult",
    "SpacesSearchData",
    "SpacesSearchResult",
]