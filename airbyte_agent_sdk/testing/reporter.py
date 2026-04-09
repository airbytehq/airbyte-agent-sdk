"""
Test result reporter for formatting and displaying test results.

Supports console output and JSON export.
"""

import json
import sys
from typing import TextIO

from .diff_generator import DiffGenerator
from .html_reporter import HTMLReporter
from .models import TestReport, TestResult


class TestReporter:
    """Formats and displays test results."""

    def __init__(self, verbose: bool = False, show_diffs: bool = False):
        """
        Initialize reporter.

        Args:
            verbose: Enable verbose output with individual test details
            show_diffs: Show detailed diffs for mismatches in console output
        """
        self.verbose = verbose
        self.show_diffs = show_diffs
        self.html_reporter = HTMLReporter()
        self.diff_generator = DiffGenerator()

    def report_console(self, report: TestReport, output: TextIO | None = None) -> None:
        """
        Print test report to console.

        Args:
            report: TestReport to display
            output: Output stream (default: sys.stdout)
        """
        if output is None:
            output = sys.stdout

        # Header
        output.write(f"\n{'=' * 60}\n")
        output.write(f"Test Report: {report.connector_path}\n")
        output.write(f"Mode: {report.mode}\n")
        output.write(f"Timestamp: {report.timestamp.isoformat()}\n")
        output.write(f"{'=' * 60}\n\n")

        # Individual results (if verbose)
        if self.verbose:
            output.write("Test Results:\n")
            output.write("-" * 60 + "\n")
            for result in report.results:
                self._print_result(result, output)
            output.write("\n")

        # Summary
        output.write("Summary:\n")
        output.write("-" * 60 + "\n")
        output.write(f"  Total:        {report.total}\n")
        output.write(f"  Passed:       {report.passed} {self._status_symbol('passed')}\n")
        output.write(f"  Failed:       {report.failed} {self._status_symbol('failed')}\n")
        output.write(f"  Errors:       {report.errors} {self._status_symbol('error')}\n")
        output.write(f"  Success Rate: {report.success_rate:.1f}%\n")
        output.write(f"  Duration:     {report.total_duration_ms:.1f}ms ({report.total_duration_ms / report.total:.1f}ms avg)\n")
        output.write("\n")

        # Overall status
        if report.failed > 0 or report.errors > 0:
            output.write(f"{'=' * 60}\n")
            output.write("❌ TESTS FAILED\n")
            output.write(f"{'=' * 60}\n")
        else:
            output.write(f"{'=' * 60}\n")
            output.write("✅ ALL TESTS PASSED\n")
            output.write(f"{'=' * 60}\n")

    def _print_result(self, result: TestResult, output: TextIO) -> None:
        """Print a single test result."""
        symbol = self._status_symbol(result.status)
        output.write(f"  {symbol} {result.test_name} ({result.duration_ms:.1f}ms)\n")

        if result.status != "passed" and result.error_message:
            output.write(f"      Error: {result.error_message}\n")

        # Phase 2: Show mismatches if present
        if result.mismatches:
            output.write(f"      Mismatches: {len(result.mismatches)}\n")
            if self.show_diffs:
                for mismatch in result.mismatches:
                    output.write(f"        - {mismatch.field}: {mismatch.description}\n")
                    if self.show_diffs:
                        diff = self.diff_generator.generate_diff(mismatch.expected, mismatch.actual, mismatch.field)
                        # Indent diff output
                        for line in diff.split("\n"):
                            output.write(f"          {line}\n")

    def _status_symbol(self, status: str) -> str:
        """Get visual symbol for status."""
        symbols = {"passed": "✓", "failed": "✗", "error": "⚠"}
        return symbols.get(status, "?")

    def report_json(self, report: TestReport, output: TextIO | None = None, pretty: bool = True) -> None:
        """
        Print test report as JSON.

        Args:
            report: TestReport to display
            output: Output stream (default: sys.stdout)
            pretty: Pretty-print JSON with indentation
        """
        if output is None:
            output = sys.stdout

        data = {
            "connector_path": report.connector_path,
            "mode": report.mode,
            "timestamp": report.timestamp.isoformat(),
            "total_duration_ms": report.total_duration_ms,
            "summary": report.summary_dict(),
            "results": [
                {
                    "test_name": r.test_name,
                    "entity": r.entity,
                    "action": r.action,
                    "status": r.status,
                    "duration_ms": r.duration_ms,
                    "error_message": r.error_message,
                    "mismatches": [
                        {
                            "field": m.field,
                            "expected": m.expected,
                            "actual": m.actual,
                            "description": m.description,
                        }
                        for m in r.mismatches
                    ]
                    if r.mismatches
                    else [],
                    "timestamp": r.timestamp.isoformat(),
                }
                for r in report.results
            ],
        }

        if pretty:
            json.dump(data, output, indent=2)
        else:
            json.dump(data, output)

        output.write("\n")

    def report_json_file(self, report: TestReport, file_path: str, pretty: bool = True) -> None:
        """
        Write test report to JSON file.

        Args:
            report: TestReport to save
            file_path: Path to output file
            pretty: Pretty-print JSON with indentation
        """
        with open(file_path, "w") as f:
            self.report_json(report, output=f, pretty=pretty)

    def report_html(self, report: TestReport, output: TextIO | None = None) -> None:
        """
        Print test report as HTML.

        Args:
            report: TestReport to display
            output: Output stream (default: sys.stdout)
        """
        if output is None:
            output = sys.stdout

        html = self.html_reporter.generate_html_report(report)
        output.write(html)

    def report_html_file(self, report: TestReport, file_path: str) -> None:
        """
        Write test report to HTML file.

        Args:
            report: TestReport to save
            file_path: Path to output file
        """
        with open(file_path, "w") as f:
            self.report_html(report, output=f)


def print_quick_summary(report: TestReport) -> None:
    """
    Print a quick one-line summary of test results.

    Args:
        report: TestReport to summarize
    """
    symbol = "✅" if report.failed == 0 and report.errors == 0 else "❌"
    print(f"{symbol} {report.passed}/{report.total} passed ({report.success_rate:.1f}%) in {report.total_duration_ms:.1f}ms")
