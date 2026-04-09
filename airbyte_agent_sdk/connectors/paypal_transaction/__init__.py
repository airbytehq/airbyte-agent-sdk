"""
Paypal-Transaction connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import PaypalTransactionConnector
from .models import (
    PaypalTransactionAuthConfig,
    PaypalTransactionReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    TransactionsSearchData,
    TransactionsSearchResult,
    BalancesSearchData,
    BalancesSearchResult,
    ListProductsSearchData,
    ListProductsSearchResult,
    ShowProductDetailsSearchData,
    ShowProductDetailsSearchResult,
    ListDisputesSearchData,
    ListDisputesSearchResult,
    SearchInvoicesSearchData,
    SearchInvoicesSearchResult,
    ListPaymentsSearchData,
    ListPaymentsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "PaypalTransactionConnector",
    "AirbyteAuthConfig",
    "PaypalTransactionAuthConfig",
    "PaypalTransactionReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "TransactionsSearchData",
    "TransactionsSearchResult",
    "BalancesSearchData",
    "BalancesSearchResult",
    "ListProductsSearchData",
    "ListProductsSearchResult",
    "ShowProductDetailsSearchData",
    "ShowProductDetailsSearchResult",
    "ListDisputesSearchData",
    "ListDisputesSearchResult",
    "SearchInvoicesSearchData",
    "SearchInvoicesSearchResult",
    "ListPaymentsSearchData",
    "ListPaymentsSearchResult",
]