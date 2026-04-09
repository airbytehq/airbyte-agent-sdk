"""
Shopify connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import ShopifyConnector
from .models import (
    ShopifyAuthConfig,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "ShopifyConnector",
    "AirbyteAuthConfig",
    "ShopifyAuthConfig",
]