"""
Reddit-Ads connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import RedditAdsConnector
from .models import (
    RedditAdsAuthConfig,
    RedditAdsReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    AdsSearchData,
    AdsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "RedditAdsConnector",
    "AirbyteAuthConfig",
    "RedditAdsAuthConfig",
    "RedditAdsReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "CampaignsSearchData",
    "CampaignsSearchResult",
    "AdsSearchData",
    "AdsSearchResult",
]