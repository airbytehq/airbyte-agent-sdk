"""
Airbyte Agent SDK — type-safe connector execution framework.

Entry points:
- connect(name) — one-call factory for a hosted-mode executor
- ask(prompt) / ask_sync(prompt) — natural-language query across a workspace
- Workspace — async context manager for workspace-level operations

Also provides:
- LocalExecutor / HostedExecutor for direct connector execution
- Performance monitoring and instrumentation
"""

from __future__ import annotations

from .ask import ask, ask_sync
from .auth_strategies import AuthStrategy
from .config import configure
from .connect import connect
from .connector_model_loader import load_connector_model
from .constants import SDK_VERSION
from .exceptions import (
    AuthenticationError,
    HTTPClientError,
    NetworkError,
    RateLimitError,
    TimeoutError,
)
from .executor import (
    ActionNotSupportedError,
    EntityNotFoundError,
    ExecutionConfig,
    ExecutionResult,
    ExecutorError,
    ExecutorProtocol,
    HostedExecutor,
    InvalidParameterError,
    LocalExecutor,
    MissingParameterError,
)
from .executor.models import AskResult, AskToolCallResult, ConnectorInfo
from .http_client import HTTPClient
from .logging import LogSession, NullLogger, RequestLog, RequestLogger
from .performance import PerformanceMonitor, instrument
from .registry import list_connectors
from .types import Action, AirbyteAuthConfig, AuthType, ConnectorModel, EntityDefinition
from .utils import save_download
from .workspace import Workspace

__version__ = SDK_VERSION

__all__ = [
    # Workspace
    "Workspace",
    "ask",
    "ask_sync",
    "AskResult",
    "AskToolCallResult",
    "ConnectorInfo",
    # All Executors
    "LocalExecutor",
    "HostedExecutor",
    "ExecutorProtocol",
    "HTTPClient",
    # Execution Config and Result Types
    "ExecutionConfig",
    "ExecutionResult",
    # Types
    "AirbyteAuthConfig",
    "ConnectorModel",
    "Action",
    "AuthType",
    "EntityDefinition",
    "load_connector_model",
    # Authentication
    "AuthStrategy",
    # Executor Exceptions
    "ExecutorError",
    "EntityNotFoundError",
    "ActionNotSupportedError",
    "MissingParameterError",
    "InvalidParameterError",
    # HTTP Exceptions
    "HTTPClientError",
    "AuthenticationError",
    "RateLimitError",
    "NetworkError",
    "TimeoutError",
    # Logging
    "RequestLogger",
    "NullLogger",
    "RequestLog",
    "LogSession",
    # Performance monitoring
    "PerformanceMonitor",
    "instrument",
    # Utilities
    "save_download",
    # Global configuration
    "configure",
    # Connect factory
    "connect",
    "list_connectors",
]
