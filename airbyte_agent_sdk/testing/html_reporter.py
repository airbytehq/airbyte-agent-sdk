"""
HTML report generation for test results.

This module provides HTML-formatted test reports with visual diffs
and expandable test details.
"""

from .diff_generator import DiffGenerator
from .models import RequestMismatch, TestReport, TestResult


class HTMLReporter:
    """Generates HTML reports for test results."""

    def __init__(self):
        """Initialize HTML reporter."""
        self.diff_generator = DiffGenerator()

    def generate_html_report(self, report: TestReport) -> str:
        """
        Generate a complete HTML report.

        Args:
            report: TestReport to format as HTML

        Returns:
            Complete HTML document as string
        """
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connector Test Report - {report.connector_path}</title>
    {self._get_styles()}
</head>
<body>
    <div class="container">
        {self._render_header(report)}
        {self._render_summary(report)}
        {self._render_results(report)}
    </div>
    {self._get_scripts()}
</body>
</html>"""

    def _render_header(self, report: TestReport) -> str:
        """Render the report header."""
        return f"""
        <header>
            <h1>Connector Test Report</h1>
            <div class="metadata">
                <div><strong>Connector:</strong> {report.connector_path}</div>
                <div><strong>Mode:</strong> {report.mode}</div>
                <div><strong>Time:</strong> {report.timestamp.strftime("%Y-%m-%d %H:%M:%S")}</div>
                <div><strong>Duration:</strong> {report.total_duration_ms:.2f}ms</div>
            </div>
        </header>
        """

    def _render_summary(self, report: TestReport) -> str:
        """Render the summary statistics."""
        success_rate = report.success_rate
        status_class = "success" if success_rate == 100 else "warning" if success_rate >= 80 else "danger"

        return f"""
        <section class="summary">
            <h2>Summary</h2>
            <div class="stats">
                <div class="stat-box">
                    <div class="stat-number">{report.total}</div>
                    <div class="stat-label">Total Tests</div>
                </div>
                <div class="stat-box success">
                    <div class="stat-number">{report.passed}</div>
                    <div class="stat-label">Passed</div>
                </div>
                <div class="stat-box danger">
                    <div class="stat-number">{report.failed}</div>
                    <div class="stat-label">Failed</div>
                </div>
                <div class="stat-box warning">
                    <div class="stat-number">{report.errors}</div>
                    <div class="stat-label">Errors</div>
                </div>
                <div class="stat-box {status_class}">
                    <div class="stat-number">{success_rate:.1f}%</div>
                    <div class="stat-label">Success Rate</div>
                </div>
            </div>
        </section>
        """

    def _render_results(self, report: TestReport) -> str:
        """Render individual test results."""
        results_html = '<section class="results"><h2>Test Results</h2>'

        for result in report.results:
            results_html += self._render_single_result(result)

        results_html += "</section>"
        return results_html

    def _render_single_result(self, result: TestResult) -> str:
        """Render a single test result."""
        status_class = result.status
        status_icon = "✓" if result.status == "passed" else "✗" if result.status == "failed" else "⚠"

        details_html = ""
        if result.error_message or result.mismatches:
            details_id = f"details-{id(result)}"
            details_html = f"""
            <div class="test-details" id="{details_id}">
                {self._render_error_message(result)}
                {self._render_mismatches(result)}
            </div>
            """

        toggle_button = ""
        if details_html:
            details_id = f"details-{id(result)}"
            toggle_button = f'<button class="toggle-btn" onclick="toggleDetails(\'{details_id}\')">Show Details</button>'

        return f"""
        <div class="test-result {status_class}">
            <div class="test-header">
                <span class="status-icon">{status_icon}</span>
                <div class="test-info">
                    <div class="test-name">{result.test_name}</div>
                    <div class="test-meta">
                        {result.entity}.{result.action} • {result.duration_ms:.2f}ms
                    </div>
                </div>
                {toggle_button}
            </div>
            {details_html}
        </div>
        """

    def _render_error_message(self, result: TestResult) -> str:
        """Render error message if present."""
        if not result.error_message:
            return ""

        return f"""
        <div class="error-section">
            <h4>Error</h4>
            <pre class="error-message">{self._escape_html(result.error_message)}</pre>
        </div>
        """

    def _render_mismatches(self, result: TestResult) -> str:
        """Render request validation mismatches."""
        if not result.mismatches:
            return ""

        mismatches_html = '<div class="mismatches-section"><h4>Request Validation Failures</h4>'

        for mismatch in result.mismatches:
            mismatches_html += self._render_single_mismatch(mismatch)

        mismatches_html += "</div>"
        return mismatches_html

    def _render_single_mismatch(self, mismatch: RequestMismatch) -> str:
        """Render a single request mismatch."""
        # Generate diff
        diff = self.diff_generator.generate_diff(mismatch.expected, mismatch.actual, mismatch.field)

        return f"""
        <div class="mismatch">
            <div class="mismatch-header">
                <strong>Field:</strong> {mismatch.field}
            </div>
            <div class="mismatch-description">{self._escape_html(mismatch.description)}</div>
            <div class="mismatch-diff">
                <pre>{self._escape_html(diff)}</pre>
            </div>
        </div>
        """

    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters."""
        if text is None:
            return ""
        return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;")

    def _get_styles(self) -> str:
        """Get CSS styles for the report."""
        return """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 15px;
        }

        h2 {
            color: #34495e;
            margin-bottom: 15px;
        }

        h4 {
            color: #555;
            margin-bottom: 10px;
        }

        .metadata {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            color: #666;
        }

        .summary {
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .stat-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 6px;
            text-align: center;
            border-left: 4px solid #999;
        }

        .stat-box.success {
            border-left-color: #28a745;
        }

        .stat-box.danger {
            border-left-color: #dc3545;
        }

        .stat-box.warning {
            border-left-color: #ffc107;
        }

        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #2c3e50;
        }

        .stat-label {
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
        }

        .results {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .test-result {
            background: #f8f9fa;
            margin-bottom: 15px;
            border-radius: 6px;
            border-left: 4px solid #999;
            overflow: hidden;
        }

        .test-result.passed {
            border-left-color: #28a745;
        }

        .test-result.failed {
            border-left-color: #dc3545;
        }

        .test-result.error {
            border-left-color: #ffc107;
        }

        .test-header {
            display: flex;
            align-items: center;
            padding: 15px;
            gap: 15px;
        }

        .status-icon {
            font-size: 1.5em;
            min-width: 30px;
        }

        .test-result.passed .status-icon {
            color: #28a745;
        }

        .test-result.failed .status-icon {
            color: #dc3545;
        }

        .test-result.error .status-icon {
            color: #ffc107;
        }

        .test-info {
            flex: 1;
        }

        .test-name {
            font-weight: bold;
            color: #2c3e50;
        }

        .test-meta {
            color: #666;
            font-size: 0.9em;
        }

        .toggle-btn {
            background: #007bff;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9em;
        }

        .toggle-btn:hover {
            background: #0056b3;
        }

        .test-details {
            padding: 15px;
            border-top: 1px solid #ddd;
            background: white;
            display: none;
        }

        .test-details.show {
            display: block;
        }

        .error-section,
        .mismatches-section {
            margin-bottom: 15px;
        }

        .error-message,
        .mismatch-diff pre {
            background: #f4f4f4;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }

        .mismatch {
            background: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 4px;
            padding: 15px;
            margin-bottom: 10px;
        }

        .mismatch-header {
            margin-bottom: 8px;
            color: #856404;
        }

        .mismatch-description {
            margin-bottom: 10px;
            color: #666;
        }

        .mismatch-diff {
            margin-top: 10px;
        }
    </style>
        """

    def _get_scripts(self) -> str:
        """Get JavaScript for interactive features."""
        return """
    <script>
        function toggleDetails(id) {
            const element = document.getElementById(id);
            const button = event.target;

            if (element.classList.contains('show')) {
                element.classList.remove('show');
                button.textContent = 'Show Details';
            } else {
                element.classList.add('show');
                button.textContent = 'Hide Details';
            }
        }
    </script>
        """
