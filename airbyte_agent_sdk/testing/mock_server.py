"""
HTTP mock server for connector testing using pytest-httpx.

Provides HTTP-layer mocking for testing connectors without hitting real APIs.

Note: This module is optional and only used for pytest-based testing.
For standalone CLI usage, the runner uses unittest.mock instead.
"""

from typing import TYPE_CHECKING, Dict, List
from urllib.parse import urlencode

# Optional import - only needed for pytest integration
try:
    from pytest_httpx import HTTPXMock

    PYTEST_HTTPX_AVAILABLE = True
except ImportError:
    PYTEST_HTTPX_AVAILABLE = False
    if TYPE_CHECKING:
        from pytest_httpx import HTTPXMock

from .models import TestSpec


class MockServer:
    """
    Manages HTTP mocking for connector tests using pytest-httpx.

    This class sets up HTTP mocks based on test specifications, allowing
    tests to run without hitting real APIs.
    """

    def __init__(self, httpx_mock: HTTPXMock, base_url: str):
        """
        Initialize the mock server.

        Args:
            httpx_mock: pytest-httpx mock instance
            base_url: Base URL for the API (e.g., "https://api.stripe.com")
        """
        self.httpx_mock = httpx_mock
        self.base_url = base_url.rstrip("/")
        self._expectations: List[TestSpec] = []

    def add_expectation(self, spec: TestSpec) -> None:
        """
        Add a request/response expectation from a test spec.

        Args:
            spec: Test specification containing expected request and response
        """
        request = spec.captured_request
        response = spec.captured_response

        # Build full URL
        url = self._build_url(request.path, request.query_params)

        # Prepare response
        json_response = response.body if isinstance(response.body, (dict, list)) else None
        text_response = response.body if isinstance(response.body, str) else None

        # Add the mock response
        self.httpx_mock.add_response(
            method=request.method,
            url=url,
            status_code=response.status_code,
            json=json_response,
            text=text_response,
            headers=response.headers,
        )

        self._expectations.append(spec)

    def add_expectations(self, specs: List[TestSpec]) -> None:
        """
        Add multiple request/response expectations.

        Args:
            specs: List of test specifications
        """
        for spec in specs:
            self.add_expectation(spec)

    def _build_url(self, path: str, query_params: Dict[str, str] | None = None) -> str:
        """
        Build full URL from path and query parameters.

        Args:
            path: URL path
            query_params: Optional query parameters

        Returns:
            Full URL with base, path, and query string
        """
        url = f"{self.base_url}{path}"

        if query_params:
            # Sort for consistent URL matching
            sorted_params = sorted(query_params.items())
            query_string = urlencode(sorted_params)
            url = f"{url}?{query_string}"

        return url

    @property
    def expectation_count(self) -> int:
        """Number of expectations registered."""
        return len(self._expectations)

    def reset(self) -> None:
        """Reset all expectations (calls httpx_mock.reset())."""
        self.httpx_mock.reset(assert_all_responses_were_requested=False)
        self._expectations.clear()


def create_mock_server(base_url: str) -> HTTPXMock:  # noqa: ARG001
    """
    Create a new HTTPXMock instance for testing.

    This is a convenience function for creating mocks outside of pytest fixtures.

    Args:
        base_url: Base URL for the API

    Returns:
        Configured HTTPXMock instance
    """
    return HTTPXMock()


def setup_mock_for_spec(httpx_mock: HTTPXMock, base_url: str, spec: TestSpec) -> None:
    """
    Convenience function to set up a single test spec mock.

    Args:
        httpx_mock: pytest-httpx mock instance
        base_url: Base URL for the API
        spec: Test specification to mock
    """
    server = MockServer(httpx_mock, base_url)
    server.add_expectation(spec)


def setup_mocks_for_specs(httpx_mock: HTTPXMock, base_url: str, specs: List[TestSpec]) -> MockServer:
    """
    Convenience function to set up multiple test spec mocks.

    Args:
        httpx_mock: pytest-httpx mock instance
        base_url: Base URL for the API
        specs: List of test specifications to mock

    Returns:
        Configured MockServer instance
    """
    server = MockServer(httpx_mock, base_url)
    server.add_expectations(specs)
    return server
