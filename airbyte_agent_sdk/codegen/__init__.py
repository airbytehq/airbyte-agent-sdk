"""
Code generation tools for typed connectors.

Generates type-safe connector packages from OpenAPI 3.0 specifications.
"""

from .generator import ConnectorGenerator

__all__ = ["ConnectorGenerator"]
