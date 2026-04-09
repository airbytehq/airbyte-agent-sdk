"""Exceptions for the Airbyte SDK.

DEPRECATED: HTTP exceptions have been moved to airbyte_agent_sdk.http.exceptions.
This module re-exports them for backward compatibility.
"""

from airbyte_agent_sdk.http.exceptions import (
    AuthenticationError,
    HTTPClientError,
    HTTPStatusError,
    NetworkError,
    RateLimitError,
    TimeoutError,
)

__all__ = [
    "HTTPClientError",
    "HTTPStatusError",
    "AuthenticationError",
    "RateLimitError",
    "NetworkError",
    "TimeoutError",
]
