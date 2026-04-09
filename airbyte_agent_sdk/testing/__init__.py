"""
Connector testing framework for Airbyte SDK.

This module provides tools for testing Airbyte connectors through:
- YAML-based test specifications
- Mock mode testing (HTTP layer interception)
- Test execution and reporting
- CLI tools for running and validating tests
"""

from .cassette_generator import CassetteGenerator
from .models import (
    CapturedRequest,
    CapturedResponse,
    RequestMismatch,
    TestInputs,
    TestReport,
    TestResult,
    TestSpec,
    ValidationConfig,
)
from .reporter import TestReporter
from .runner import TestRunner
from .spec_loader import load_test_spec, load_test_specs

__all__ = [
    "TestSpec",
    "TestInputs",
    "CapturedRequest",
    "CapturedResponse",
    "ValidationConfig",
    "RequestMismatch",
    "TestResult",
    "TestReport",
    "load_test_spec",
    "load_test_specs",
    "TestRunner",
    "TestReporter",
    "CassetteGenerator",
]
