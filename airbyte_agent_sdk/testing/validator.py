"""
Request validation for connector tests.

This module provides validation of actual HTTP requests against expected requests
from test specifications, with configurable strictness levels.
"""

from typing import Any, Dict, List

from .models import CapturedRequest, RequestMismatch


class RequestValidator:
    """Validates actual HTTP requests against expected requests."""

    def validate_request(self, expected: CapturedRequest, actual: CapturedRequest) -> List[RequestMismatch]:
        """
        Validate an actual request against the expected request.

        Args:
            expected: Expected request from test specification
            actual: Actual request made during test execution

        Returns:
            List of mismatches found (empty list if request matches)
        """
        mismatches: List[RequestMismatch] = []

        # Validate method (always strict)
        mismatches.extend(self._validate_method(expected, actual))

        # Validate path (always strict)
        mismatches.extend(self._validate_path(expected, actual))

        # Validate query parameters (configurable strictness)
        mismatches.extend(self._validate_query_params(expected, actual))

        # Validate headers (configurable strictness)
        mismatches.extend(self._validate_headers(expected, actual))

        # Validate body (configurable strictness)
        mismatches.extend(self._validate_body(expected, actual))

        return mismatches

    def _validate_method(self, expected: CapturedRequest, actual: CapturedRequest) -> List[RequestMismatch]:
        """Validate HTTP method (always exact match)."""
        if expected.method.upper() != actual.method.upper():
            return [
                RequestMismatch(
                    field="method",
                    expected=expected.method,
                    actual=actual.method,
                    description=f"Method mismatch: expected {expected.method}, got {actual.method}",
                )
            ]
        return []

    def _validate_path(self, expected: CapturedRequest, actual: CapturedRequest) -> List[RequestMismatch]:
        """Validate URL path (always exact match)."""
        if expected.path != actual.path:
            return [
                RequestMismatch(
                    field="path",
                    expected=expected.path,
                    actual=actual.path,
                    description=f"Path mismatch: expected {expected.path}, got {actual.path}",
                )
            ]
        return []

    def _validate_query_params(self, expected: CapturedRequest, actual: CapturedRequest) -> List[RequestMismatch]:
        """Validate query parameters with configurable strictness."""
        expected_params = expected.query_params or {}
        actual_params = actual.query_params or {}

        config = expected.validation

        if config.query_params_strict:
            # Exact match: keys and values must be identical
            if expected_params != actual_params:
                return [
                    RequestMismatch(
                        field="query_params",
                        expected=expected_params,
                        actual=actual_params,
                        description="Query parameters don't match exactly (strict mode)",
                    )
                ]
        else:
            # Partial match: expected params must be subset of actual
            for key, value in expected_params.items():
                if key not in actual_params:
                    return [
                        RequestMismatch(
                            field="query_params",
                            expected=expected_params,
                            actual=actual_params,
                            description=f"Missing expected query parameter: {key}",
                        )
                    ]
                if actual_params[key] != value:
                    return [
                        RequestMismatch(
                            field="query_params",
                            expected=expected_params,
                            actual=actual_params,
                            description=f"Query parameter {key} mismatch: expected {value}, got {actual_params[key]}",
                        )
                    ]

        return []

    def _validate_headers(self, expected: CapturedRequest, actual: CapturedRequest) -> List[RequestMismatch]:
        """Validate headers with configurable strictness and ignored headers."""
        config = expected.validation

        # Normalize header names to lowercase for comparison
        ignore_headers_lower = [h.lower() for h in config.ignore_headers]

        # Filter out ignored headers
        expected_headers = {k: v for k, v in expected.headers.items() if k.lower() not in ignore_headers_lower}
        actual_headers = {k: v for k, v in actual.headers.items() if k.lower() not in ignore_headers_lower}

        if config.headers_strict:
            # Exact match: all headers must be identical
            if expected_headers != actual_headers:
                return [
                    RequestMismatch(
                        field="headers",
                        expected=expected_headers,
                        actual=actual_headers,
                        description="Headers don't match exactly (strict mode, after filtering ignored headers)",
                    )
                ]
        else:
            # Partial match: expected headers must be subset of actual
            for key, value in expected_headers.items():
                if key not in actual_headers:
                    return [
                        RequestMismatch(
                            field="headers",
                            expected=expected_headers,
                            actual=actual_headers,
                            description=f"Missing expected header: {key}",
                        )
                    ]
                if actual_headers[key] != value:
                    return [
                        RequestMismatch(
                            field="headers",
                            expected=expected_headers,
                            actual=actual_headers,
                            description=f"Header {key} mismatch: expected {value}, got {actual_headers[key]}",
                        )
                    ]

        return []

    def _validate_body(self, expected: CapturedRequest, actual: CapturedRequest) -> List[RequestMismatch]:
        """Validate request body with configurable strictness."""
        config = expected.validation

        # Handle None/null cases
        if expected.body is None and actual.body is None:
            return []
        if expected.body is None and actual.body is not None:
            return [
                RequestMismatch(
                    field="body",
                    expected=None,
                    actual=actual.body,
                    description="Expected no body, but got body",
                )
            ]
        if expected.body is not None and actual.body is None:
            return [
                RequestMismatch(
                    field="body",
                    expected=expected.body,
                    actual=None,
                    description="Expected body, but got no body",
                )
            ]

        if config.body_strict:
            # Exact match
            if expected.body != actual.body:
                return [
                    RequestMismatch(
                        field="body",
                        expected=expected.body,
                        actual=actual.body,
                        description="Body doesn't match exactly (strict mode)",
                    )
                ]
        else:
            # Partial match: expected body fields must be subset of actual
            if isinstance(expected.body, dict) and isinstance(actual.body, dict):
                if not self._partial_dict_match(expected.body, actual.body):
                    return [
                        RequestMismatch(
                            field="body",
                            expected=expected.body,
                            actual=actual.body,
                            description="Body doesn't contain all expected fields (partial mode)",
                        )
                    ]
            else:
                # For non-dict bodies, fall back to exact match
                if expected.body != actual.body:
                    return [
                        RequestMismatch(
                            field="body",
                            expected=expected.body,
                            actual=actual.body,
                            description="Body doesn't match (non-dict body in partial mode defaults to exact match)",
                        )
                    ]

        return []

    def _partial_dict_match(self, expected: Dict[str, Any], actual: Dict[str, Any]) -> bool:
        """
        Check if actual dict contains all fields from expected dict.

        Recursively checks nested dicts. Returns True if all expected fields
        are present in actual with matching values.
        """
        for key, value in expected.items():
            if key not in actual:
                return False

            if isinstance(value, dict) and isinstance(actual[key], dict):
                # Recursively check nested dicts
                if not self._partial_dict_match(value, actual[key]):
                    return False
            elif actual[key] != value:
                return False

        return True
