"""
Amplitude connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import AmplitudeConnector
from .models import (
    AmplitudeAuthConfig,
    AmplitudeReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AnnotationsSearchData,
    AnnotationsSearchResult,
    CohortsSearchData,
    CohortsSearchResult,
    EventsListSearchData,
    EventsListSearchResult,
    ActiveUsersSearchData,
    ActiveUsersSearchResult,
    AverageSessionLengthSearchData,
    AverageSessionLengthSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "AmplitudeConnector",
    "AirbyteAuthConfig",
    "AmplitudeAuthConfig",
    "AmplitudeReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "AnnotationsSearchData",
    "AnnotationsSearchResult",
    "CohortsSearchData",
    "CohortsSearchResult",
    "EventsListSearchData",
    "EventsListSearchResult",
    "ActiveUsersSearchData",
    "ActiveUsersSearchResult",
    "AverageSessionLengthSearchData",
    "AverageSessionLengthSearchResult",
]