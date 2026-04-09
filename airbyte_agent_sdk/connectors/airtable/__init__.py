"""
Airtable connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import AirtableConnector
from .models import (
    AirtableAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    BasesSearchData,
    BasesSearchResult,
    TablesSearchData,
    TablesSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "AirtableConnector",
    "AirbyteAuthConfig",
    "AirtableAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "BasesSearchData",
    "BasesSearchResult",
    "TablesSearchData",
    "TablesSearchResult",
]