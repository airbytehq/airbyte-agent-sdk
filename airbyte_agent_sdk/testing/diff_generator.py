"""
Diff generation for test validation failures.

This module provides utilities for generating human-readable diffs between
expected and actual values in test results.
"""

import json
from difflib import unified_diff
from typing import Any, Dict, List


class DiffGenerator:
    """Generates human-readable diffs between expected and actual values."""

    def generate_diff(self, expected: Any, actual: Any, field_name: str = "value") -> str:
        """
        Generate a human-readable diff between expected and actual values.

        Args:
            expected: Expected value
            actual: Actual value
            field_name: Name of the field being compared (for context)

        Returns:
            Formatted diff string
        """
        # Handle None cases
        if expected is None and actual is None:
            return "Both values are None (no difference)"
        if expected is None:
            return f"Expected: None\nActual: {self._format_value(actual)}"
        if actual is None:
            return f"Expected: {self._format_value(expected)}\nActual: None"

        # For simple types, show side-by-side
        if not isinstance(expected, (dict, list)):
            return self._format_simple_diff(expected, actual)

        # For complex types (dict/list), use JSON diff
        return self.generate_json_diff(expected, actual, field_name)

    def generate_json_diff(self, expected: Any, actual: Any, field_name: str = "value") -> str:
        """
        Generate a unified diff for JSON-serializable objects.

        Args:
            expected: Expected value
            actual: Actual value
            field_name: Name of the field (for labels)

        Returns:
            Unified diff string
        """
        # Convert to formatted JSON strings
        expected_str = json.dumps(expected, indent=2, sort_keys=True)
        actual_str = json.dumps(actual, indent=2, sort_keys=True)

        # Split into lines for diff
        expected_lines = expected_str.splitlines(keepends=True)
        actual_lines = actual_str.splitlines(keepends=True)

        # Generate unified diff
        diff_lines = list(
            unified_diff(
                expected_lines,
                actual_lines,
                fromfile=f"expected {field_name}",
                tofile=f"actual {field_name}",
                lineterm="",
            )
        )

        if not diff_lines:
            return "No differences found"

        return "".join(diff_lines)

    def generate_dict_diff(self, expected: Dict[str, Any], actual: Dict[str, Any]) -> str:
        """
        Generate a detailed diff for dictionaries.

        Shows added, removed, and changed keys.

        Args:
            expected: Expected dictionary
            actual: Actual dictionary

        Returns:
            Formatted diff description
        """
        expected_keys = set(expected.keys())
        actual_keys = set(actual.keys())

        added_keys = actual_keys - expected_keys
        removed_keys = expected_keys - actual_keys
        common_keys = expected_keys & actual_keys

        diff_parts = []

        if removed_keys:
            diff_parts.append(f"Missing keys: {', '.join(sorted(removed_keys))}")

        if added_keys:
            diff_parts.append(f"Extra keys: {', '.join(sorted(added_keys))}")

        changed_keys = []
        for key in sorted(common_keys):
            if expected[key] != actual[key]:
                changed_keys.append(key)

        if changed_keys:
            diff_parts.append("Changed values:")
            for key in changed_keys:
                diff_parts.append(f"  {key}:\n    Expected: {self._format_value(expected[key])}\n    Actual:   {self._format_value(actual[key])}")

        if not diff_parts:
            return "Dictionaries are identical"

        return "\n".join(diff_parts)

    def generate_list_diff(self, expected: List[Any], actual: List[Any]) -> str:
        """
        Generate a detailed diff for lists.

        Args:
            expected: Expected list
            actual: Actual list

        Returns:
            Formatted diff description
        """
        diff_parts = []

        if len(expected) != len(actual):
            diff_parts.append(f"Length mismatch: expected {len(expected)}, actual {len(actual)}")

        # Compare elements up to the shorter length
        min_len = min(len(expected), len(actual))
        for i in range(min_len):
            if expected[i] != actual[i]:
                diff_parts.append(f"Element {i}:\n  Expected: {self._format_value(expected[i])}\n  Actual:   {self._format_value(actual[i])}")

        # Show extra elements if lists have different lengths
        if len(expected) > min_len:
            diff_parts.append(
                f"Missing elements (indices {min_len}-{len(expected) - 1}):\n"
                + "\n".join(f"  [{i}]: {self._format_value(expected[i])}" for i in range(min_len, len(expected)))
            )

        if len(actual) > min_len:
            diff_parts.append(
                f"Extra elements (indices {min_len}-{len(actual) - 1}):\n"
                + "\n".join(f"  [{i}]: {self._format_value(actual[i])}" for i in range(min_len, len(actual)))
            )

        if not diff_parts:
            return "Lists are identical"

        return "\n".join(diff_parts)

    def _format_simple_diff(self, expected: Any, actual: Any) -> str:
        """Format a simple diff for non-complex types."""
        return f"Expected: {self._format_value(expected)}\nActual:   {self._format_value(actual)}"

    def _format_value(self, value: Any) -> str:
        """Format a value for display in diffs."""
        if isinstance(value, str):
            # Show strings with quotes
            return f'"{value}"'
        if isinstance(value, (dict, list)):
            # Show JSON representation for complex types
            try:
                return json.dumps(value, sort_keys=True)
            except (TypeError, ValueError):
                return str(value)
        return str(value)
