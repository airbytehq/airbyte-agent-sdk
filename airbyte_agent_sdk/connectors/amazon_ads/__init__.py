"""
Amazon-Ads connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import AmazonAdsConnector
from .models import (
    AmazonAdsAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    ProfilesSearchData,
    ProfilesSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "AmazonAdsConnector",
    "AirbyteAuthConfig",
    "AmazonAdsAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "ProfilesSearchData",
    "ProfilesSearchResult",
]