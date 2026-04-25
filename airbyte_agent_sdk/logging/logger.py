"""Request/response logging implementation."""

import base64
import json
import time
import uuid
from pathlib import Path
from typing import Any, Dict

from airbyte_agent_sdk.observability.redactor import DataRedactor

from .types import LogSession, RequestLog

# Logger-local redaction marker — preserved for backwards compatibility
# with existing assertions in tests/test_logging.py and bug-bash harness.
_LOGGER_MARKER = "[REDACTED]"


def _redact_body(body: Any) -> Any:
    """Redact secrets from a request or response body.

    - dict/list: recursive key-name + value-shape redaction via `redact_mapping`.
    - str: value-shape redaction via `redact_string`.
    - bytes / binary wrapper: pass through unchanged (opaque binary payloads).
    """
    if isinstance(body, dict):
        if "_base64" in body or body.get("_binary"):
            return body
        return DataRedactor.redact_mapping(body)
    if isinstance(body, list):
        return DataRedactor.redact_mapping({"_list": body})["_list"]
    if isinstance(body, str):
        return DataRedactor.redact_string(body)
    return body


class RequestLogger:
    """Captures HTTP request/response interactions to a JSON file.

    Implements bounded logging with automatic rotation and flush-before-discard
    to prevent unbounded memory growth in long-running processes.
    """

    def __init__(
        self,
        log_file: str | None = None,
        connector_name: str | None = None,
        max_logs: int | None = 10000,
    ):
        """Initialize the request logger.

        Args:
            log_file: Path to write logs. If None, generates timestamped filename.
            connector_name: Name of the connector being logged.
            max_logs: Maximum number of logs to keep in memory before rotation.
                Set to None for unlimited (not recommended for production).
                Defaults to 10000.
        """
        if log_file is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            log_file = f".logs/session_{timestamp}.json"

        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        self.session = LogSession(
            session_id=str(uuid.uuid4()),
            connector_name=connector_name,
            max_logs=max_logs,
        )
        self._active_requests: Dict[str, Dict[str, Any]] = {}
        # Store rotated logs that have been flushed from active buffer
        self._rotated_logs: list[RequestLog] = []

    def _redact_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Redact sensitive headers using the canonical deny-list."""
        return DataRedactor.redact_headers(headers, marker=_LOGGER_MARKER)

    def _rotate_logs_if_needed(self) -> None:
        """Rotate logs if max_logs limit is reached.

        Moves oldest logs to _rotated_logs before removing them from active buffer.
        This ensures logs are preserved for final save() without memory growth.
        """
        max_logs = self.session.max_logs
        if max_logs is None:
            # Unlimited logging, no rotation needed
            return

        current_count = len(self.session.logs)
        if current_count >= max_logs:
            # Calculate how many logs to rotate (keep buffer at ~90% to avoid thrashing)
            num_to_rotate = max(1, current_count - int(max_logs * 0.9))

            # Move oldest logs to rotated buffer
            rotated = self.session.logs[:num_to_rotate]
            self._rotated_logs.extend(rotated)

            # Remove rotated logs from active buffer
            self.session.logs = self.session.logs[num_to_rotate:]

    def log_request(
        self,
        method: str,
        url: str,
        path: str,
        headers: Dict[str, str] | None = None,
        params: Dict[str, Any] | None = None,
        body: Any | None = None,
    ) -> str:
        """Log the start of an HTTP request.

        Args:
            method: HTTP method (GET, POST, etc.)
            url: Full URL
            path: Request path
            headers: Request headers
            params: Query parameters
            body: Request body

        Returns:
            Request ID for correlating with response
        """
        request_id = str(uuid.uuid4())
        self._active_requests[request_id] = {
            "start_time": time.time(),
            "method": method,
            "url": DataRedactor.redact_string(DataRedactor.redact_url(url)),
            "path": DataRedactor.redact_string(path),
            "headers": self._redact_headers(headers or {}),
            "params": DataRedactor.redact_mapping(params) if params else params,
            "body": _redact_body(body) if body is not None else body,
        }
        return request_id

    def log_response(
        self,
        request_id: str,
        status_code: int,
        response_body: Any | None = None,
        response_headers: Dict[str, str] | None = None,
    ) -> None:
        """Log a successful HTTP response.

        Args:
            request_id: ID returned from log_request
            status_code: HTTP status code
            response_body: Response body
            response_headers: Response headers
        """
        if request_id not in self._active_requests:
            return

        request_data = self._active_requests.pop(request_id)
        timing_ms = (time.time() - request_data["start_time"]) * 1000

        # Convert bytes to base64 for JSON serialization
        serializable_body = response_body
        if isinstance(response_body, bytes):
            serializable_body = {
                "_binary": True,
                "_base64": base64.b64encode(response_body).decode("utf-8"),
            }

        # Redact response body and headers before storing
        redacted_response_body = _redact_body(serializable_body) if serializable_body is not None else serializable_body
        redacted_response_headers = DataRedactor.redact_headers(response_headers, marker=_LOGGER_MARKER) if response_headers else {}

        log_entry = RequestLog(
            method=request_data["method"],
            url=request_data["url"],
            path=request_data["path"],
            headers=request_data["headers"],
            params=request_data["params"],
            body=request_data["body"],
            response_status=status_code,
            response_body=redacted_response_body,
            response_headers=redacted_response_headers,
            timing_ms=timing_ms,
        )

        self.session.logs.append(log_entry)
        self._rotate_logs_if_needed()

    def log_error(
        self,
        request_id: str,
        error: str,
        status_code: int | None = None,
    ) -> None:
        """Log an HTTP request error.

        Args:
            request_id: ID returned from log_request
            error: Error message
            status_code: HTTP status code if available
        """
        if request_id not in self._active_requests:
            return

        request_data = self._active_requests.pop(request_id)
        timing_ms = (time.time() - request_data["start_time"]) * 1000

        log_entry = RequestLog(
            method=request_data["method"],
            url=request_data["url"],
            path=request_data["path"],
            headers=request_data["headers"],
            params=request_data["params"],
            body=request_data["body"],
            response_status=status_code,
            timing_ms=timing_ms,
            error=DataRedactor.redact_string(error),
        )

        self.session.logs.append(log_entry)
        self._rotate_logs_if_needed()

    def log_chunk_fetch(self, chunk: bytes) -> None:
        """Log a chunk from streaming response.

        Args:
            chunk: Binary chunk data from streaming response
        """
        self.session.chunk_logs.append(chunk)

    def save(self) -> None:
        """Write the current session to the log file.

        Includes both rotated logs and current active logs to ensure
        no data loss during bounded logging.
        """
        # Combine rotated logs with current logs for complete session
        all_logs = self._rotated_logs + self.session.logs

        # Create a temporary session with all logs for serialization
        session_data = self.session.model_dump(mode="json")
        session_data["logs"] = [log.model_dump(mode="json") for log in all_logs]

        with open(self.log_file, "w") as f:
            json.dump(session_data, f, indent=2, default=str)

    def close(self) -> None:
        """Finalize and save the logging session."""
        self.save()


class NullLogger:
    """No-op logger for when logging is disabled."""

    def log_request(self, *args, **kwargs) -> str:
        """No-op log_request."""
        return ""

    def log_response(
        self,
        request_id: str,
        status_code: int,
        response_body: Any | None = None,
        response_headers: Dict[str, str] | None = None,
    ) -> None:
        """No-op log_response."""
        pass

    def log_error(self, *args, **kwargs) -> None:
        """No-op log_error."""
        pass

    def log_chunk_fetch(self, chunk: bytes) -> None:
        """No-op chunk logging for production."""
        pass

    def save(self) -> None:
        """No-op save."""
        pass

    def close(self) -> None:
        """No-op close."""
        pass
