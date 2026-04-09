"""
Amazon-Seller-Partner connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import AmazonSellerPartnerConnector
from .models import (
    AmazonSellerPartnerAuthConfig,
    AmazonSellerPartnerReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    OrdersSearchData,
    OrdersSearchResult,
    OrderItemsSearchData,
    OrderItemsSearchResult,
    ListFinancialEventGroupsSearchData,
    ListFinancialEventGroupsSearchResult,
    ListFinancialEventsSearchData,
    ListFinancialEventsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "AmazonSellerPartnerConnector",
    "AirbyteAuthConfig",
    "AmazonSellerPartnerAuthConfig",
    "AmazonSellerPartnerReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "OrdersSearchData",
    "OrdersSearchResult",
    "OrderItemsSearchData",
    "OrderItemsSearchResult",
    "ListFinancialEventGroupsSearchData",
    "ListFinancialEventGroupsSearchResult",
    "ListFinancialEventsSearchData",
    "ListFinancialEventsSearchResult",
]