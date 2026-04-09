"""
Pydantic models for connector test specifications.

These models define the schema for YAML-based test specifications,
test results, and test reports.
"""

from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel, Field

from airbyte_agent_sdk.secrets import SecretStr


class TestInputs(BaseModel):
    """Input parameters for a test operation."""

    params: Dict[str, Any] = Field(default_factory=dict, description="Parameters to pass to the operation")


class ValidationConfig(BaseModel):
    """Configuration for request validation strictness."""

    query_params_strict: bool = Field(
        default=True,
        description="If True, query params must match exactly. If False, actual can be a superset.",
    )
    headers_strict: bool = Field(
        default=False,
        description="If True, headers must match exactly. If False, actual can be a superset.",
    )
    body_strict: bool = Field(
        default=True,
        description="If True, body must match exactly. If False, actual can be a superset.",
    )
    ignore_headers: List[str] = Field(
        default_factory=lambda: ["User-Agent", "Accept-Encoding", "Date"],
        description="Headers to ignore during validation (case-insensitive)",
    )


class CapturedRequest(BaseModel):
    """
    HTTP request captured from a real API call.

    Note: Auth headers are NOT included - they are inherited from connector.yaml
    """

    method: str = Field(description="HTTP method (GET, POST, PUT, DELETE, etc.)")
    path: str = Field(description="URL path (without base URL)")
    query_params: Dict[str, str] | None = Field(default=None, description="Query parameters as key-value pairs")
    headers: Dict[str, str] = Field(
        default_factory=dict,
        description="HTTP headers (excluding Authorization header)",
    )
    body: Any | None = Field(default=None, description="Request body (if any)")
    validation: ValidationConfig = Field(
        default_factory=ValidationConfig,
        description="Validation configuration for this request",
    )


class CapturedResponse(BaseModel):
    """HTTP response captured from a real API call."""

    status_code: int = Field(description="HTTP status code")
    headers: Dict[str, str] = Field(default_factory=dict, description="Response headers")
    body: Any = Field(description="Response body (JSON object, array, or string)")


class TestSpec(BaseModel):
    """
    Complete test specification for a connector operation.

    This represents a verified test captured from a real API call.
    """

    test_name: str = Field(description="Descriptive name for this test")
    description: str | None = Field(default=None, description="Optional description of what this test verifies")
    entity: str = Field(description="Entity name (e.g., 'customers')")
    action: str = Field(description="Operation action (e.g., 'list', 'create', 'get')")
    auth_config: Dict[str, SecretStr] | None = Field(
        default=None,
        description="User-facing auth configuration (e.g., {'api_key': '${STRIPE_API_KEY}'}). Follows x-airbyte-auth-config spec.",
    )
    auth_scheme: str | None = Field(
        default=None,
        description="Authentication scheme name for multi-auth connectors (e.g., 'githubOAuth', 'githubPAT')",
    )
    inputs: TestInputs = Field(description="Input parameters for the operation")
    captured_request: CapturedRequest = Field(description="Expected HTTP request (captured from real API)")
    captured_response: CapturedResponse = Field(description="Mock HTTP response (captured from real API)")

    # Optional fields for download operations (two-step: metadata + file download)
    captured_file_request: CapturedRequest | None = Field(
        default=None,
        description="Expected HTTP request for file download (for download action only)",
    )
    captured_file_response: CapturedResponse | None = Field(
        default=None,
        description="Mock HTTP response for file download (for download action only)",
    )

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "test_name": "List customers with limit",
                "description": "Captured from real API call on 2025-01-15",
                "entity": "customers",
                "action": "list",
                "auth_config": {"api_key": "${STRIPE_API_KEY}"},
                "inputs": {"params": {"limit": 10}},
                "captured_request": {
                    "method": "GET",
                    "path": "/v1/customers",
                    "query_params": {"limit": "10"},
                    "headers": {"Content-Type": "application/x-www-form-urlencoded"},
                    "body": None,
                },
                "captured_response": {
                    "status_code": 200,
                    "headers": {"Content-Type": "application/json"},
                    "body": {
                        "object": "list",
                        "data": [
                            {
                                "id": "cus_test123",
                                "object": "customer",
                                "email": "test@example.com",
                            }
                        ],
                        "has_more": False,
                    },
                },
            }
        }


class RequestMismatch(BaseModel):
    """Represents a validation failure between expected and actual requests."""

    field: str = Field(description="Field that didn't match (e.g., 'method', 'path', 'query_params', 'headers', 'body')")
    expected: Any = Field(description="Expected value")
    actual: Any = Field(description="Actual value")
    description: str = Field(description="Human-readable description of the mismatch")


class TestResult(BaseModel):
    """Result of running a single test."""

    test_name: str = Field(description="Name of the test")
    entity: str = Field(description="Entity being tested")
    action: str = Field(description="Operation action")
    status: str = Field(description="Test status: 'passed', 'failed', or 'error'")
    duration_ms: float = Field(description="Test execution time in milliseconds")
    error_message: str | None = Field(default=None, description="Error message if test failed")
    mismatches: List[RequestMismatch] = Field(
        default_factory=list,
        description="Request validation failures (Phase 2)",
    )
    timestamp: datetime = Field(default_factory=datetime.now, description="When the test was run")


class TestReport(BaseModel):
    """Collection of test results with summary statistics."""

    connector_path: str = Field(description="Path to connector.yaml being tested")
    mode: str = Field(description="Test mode: 'mock' or 'live'")
    timestamp: datetime = Field(default_factory=datetime.now, description="When tests were run")
    total_duration_ms: float = Field(description="Total execution time for all tests in milliseconds")
    results: List[TestResult] = Field(default_factory=list, description="Individual test results")

    @property
    def total(self) -> int:
        """Total number of tests."""
        return len(self.results)

    @property
    def passed(self) -> int:
        """Number of passed tests."""
        return sum(1 for r in self.results if r.status == "passed")

    @property
    def failed(self) -> int:
        """Number of failed tests."""
        return sum(1 for r in self.results if r.status == "failed")

    @property
    def errors(self) -> int:
        """Number of tests with errors."""
        return sum(1 for r in self.results if r.status == "error")

    @property
    def success_rate(self) -> float:
        """Percentage of tests that passed."""
        return (self.passed / self.total * 100) if self.total > 0 else 0.0

    def summary_dict(self) -> Dict[str, Any]:
        """Get summary statistics as a dictionary."""
        return {
            "total": self.total,
            "passed": self.passed,
            "failed": self.failed,
            "errors": self.errors,
            "success_rate": f"{self.success_rate:.1f}%",
            "total_duration_ms": self.total_duration_ms,
        }
