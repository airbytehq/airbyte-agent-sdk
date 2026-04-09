"""
Github connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import GithubConnector
from .models import (
    GithubAuthConfig,
    GithubReplicationConfig,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "GithubConnector",
    "AirbyteAuthConfig",
    "GithubAuthConfig",
    "GithubReplicationConfig",
]