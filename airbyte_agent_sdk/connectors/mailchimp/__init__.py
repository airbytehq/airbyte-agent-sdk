"""
Mailchimp connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import MailchimpConnector
from .models import (
    MailchimpAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    EmailActivitySearchData,
    EmailActivitySearchResult,
    ListsSearchData,
    ListsSearchResult,
    ReportsSearchData,
    ReportsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "MailchimpConnector",
    "AirbyteAuthConfig",
    "MailchimpAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "CampaignsSearchData",
    "CampaignsSearchResult",
    "EmailActivitySearchData",
    "EmailActivitySearchResult",
    "ListsSearchData",
    "ListsSearchResult",
    "ReportsSearchData",
    "ReportsSearchResult",
]