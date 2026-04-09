"""
Google-Analytics-Data-Api connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import GoogleAnalyticsDataApiConnector
from .models import (
    GoogleAnalyticsDataApiAuthConfig,
    GoogleAnalyticsDataApiReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    WebsiteOverviewSearchData,
    WebsiteOverviewSearchResult,
    DailyActiveUsersSearchData,
    DailyActiveUsersSearchResult,
    WeeklyActiveUsersSearchData,
    WeeklyActiveUsersSearchResult,
    FourWeeklyActiveUsersSearchData,
    FourWeeklyActiveUsersSearchResult,
    TrafficSourcesSearchData,
    TrafficSourcesSearchResult,
    PagesSearchData,
    PagesSearchResult,
    DevicesSearchData,
    DevicesSearchResult,
    LocationsSearchData,
    LocationsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "GoogleAnalyticsDataApiConnector",
    "AirbyteAuthConfig",
    "GoogleAnalyticsDataApiAuthConfig",
    "GoogleAnalyticsDataApiReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "WebsiteOverviewSearchData",
    "WebsiteOverviewSearchResult",
    "DailyActiveUsersSearchData",
    "DailyActiveUsersSearchResult",
    "WeeklyActiveUsersSearchData",
    "WeeklyActiveUsersSearchResult",
    "FourWeeklyActiveUsersSearchData",
    "FourWeeklyActiveUsersSearchResult",
    "TrafficSourcesSearchData",
    "TrafficSourcesSearchResult",
    "PagesSearchData",
    "PagesSearchResult",
    "DevicesSearchData",
    "DevicesSearchResult",
    "LocationsSearchData",
    "LocationsSearchResult",
]