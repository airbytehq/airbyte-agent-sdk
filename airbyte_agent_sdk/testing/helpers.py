"""Shared helper functions for testing operations.

This module provides reusable utilities for both CLI and MCP tools to avoid code duplication.
"""

import os
import traceback
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from airbyte_agent_sdk.connector_model_loader import load_connector_model
from airbyte_agent_sdk.executor import ExecutionConfig, LocalExecutor
from airbyte_agent_sdk.secrets import (
    SecretStr,
    convert_to_secret_dict,
    resolve_env_var_references,
)
from airbyte_agent_sdk.testing.cassette_generator import CassetteGenerator
from airbyte_agent_sdk.testing.models import TestReport
from airbyte_agent_sdk.testing.runner import run_tests_async
from airbyte_agent_sdk.types import Action


@dataclass
class CassetteRecordingResult:
    """Result of a cassette recording operation."""

    success: bool
    operation: str
    params: Dict[str, Any]
    log_file: str
    cassette_file: str | None = None
    http_requests: List[Dict[str, Any]] | None = None
    error: str | None = None
    traceback: str | None = None


@dataclass
class TestRunResult:
    """Result of a test run operation."""

    success: bool
    connector_file: str | None = None
    test_report: TestReport | None = None
    error: str | None = None
    traceback: str | None = None


def resolve_connector_path(connector_path: Path) -> tuple[Path, Path]:
    """Resolve connector path to (connector_file, connector_dir).

    Args:
        connector_path: Path to connector.yaml or directory containing it

    Returns:
        Tuple of (connector_file, connector_dir)

    Raises:
        FileNotFoundError: If connector.yaml not found
    """
    if connector_path.is_dir():
        connector_file = connector_path / "connector.yaml"
        if not connector_file.exists():
            raise FileNotFoundError(f"connector.yaml not found in {connector_path}")
        connector_dir = connector_path
    else:
        connector_file = connector_path
        connector_dir = connector_path.parent

    return connector_file, connector_dir


def resolve_test_directory(
    connector_dir: Path,
    test_dir: Path | None,
    default_subdir: str,
) -> Path:
    """Resolve test directory path.

    Args:
        connector_dir: Directory containing the connector
        test_dir: Optional explicit test directory path
        default_subdir: Default subdirectory name (e.g., "tests/verified", "tests/cassettes")

    Returns:
        Resolved test directory path

    Raises:
        FileNotFoundError: If test directory doesn't exist
    """
    if test_dir is None:
        test_dir_path = connector_dir / default_subdir
    else:
        test_dir_path = test_dir

    if not test_dir_path.exists():
        raise FileNotFoundError(
            f"Test directory not found: {test_dir_path}. Create test specs in {test_dir_path} or use explicit test_dir parameter."
        )

    return test_dir_path


def load_secrets_from_env(
    env_vars: Dict[str, str] | None = None,
    secrets_mapping: Dict[str, str] | None = None,
    use_all_env_vars: bool = False,
) -> Dict[str, SecretStr]:
    """Load and resolve secrets from environment variables.

    Args:
        env_vars: Optional dict of environment variables to use for resolution.
                  If not provided, uses os.environ.
        secrets_mapping: Optional mapping of secret names to values or ${ENV_VAR} references
        use_all_env_vars: If True, use all environment variables as secrets (for test mode)

    Returns:
        Dictionary of resolved secrets wrapped in SecretStr

    Raises:
        ValueError: If secrets configuration is invalid
    """
    # If using all env vars (test mode), just convert and return
    if use_all_env_vars:
        return convert_to_secret_dict(dict(os.environ))

    # If no secrets mapping provided, return empty dict
    if not secrets_mapping:
        return {}

    # Use provided env_vars or fall back to os.environ
    env_dict = env_vars if env_vars is not None else dict(os.environ)

    # Resolve secrets - use provided mapping and resolve ${VAR} references from env_dict
    secrets_resolved = resolve_env_var_references(secrets_mapping, env_vars=env_dict, strict=True)

    # Convert secrets to SecretStr
    return convert_to_secret_dict(secrets_resolved)


async def record_cassette_operation(
    connector_file: Path,
    connector_dir: Path,
    entity: str,
    action: str,
    params: Dict[str, Any],
    auth_config: Dict[str, SecretStr],
    output_dir: Path = Path("tests/cassettes"),
    test_name: str | None = None,
    description: str | None = None,
    auth_config_mapping: Dict[str, str] | None = None,
    config_values: Dict[str, str] | None = None,
    auth_scheme: str | None = None,
) -> CassetteRecordingResult:
    """Execute connector operation and record cassette.

    Args:
        connector_file: Path to connector.yaml file
        connector_dir: Directory containing the connector
        entity: Entity name (e.g., "customers")
        action: Operation action (e.g., "list", "get")
        params: Parameters for the operation
        auth_config: Resolved user-facing auth config as SecretStr dict (applies mapping)
        output_dir: Directory to save cassette files (absolute or relative to connector_dir)
        test_name: Optional custom test name
        description: Optional test description
        auth_config_mapping: Original auth_config mapping with ${VAR} references (for cassette)
        config_values: Optional dict of config values for server variable substitution
            (e.g., {"subdomain": "acme"} for URLs like https://{subdomain}.api.example.com)
        auth_scheme: Optional auth scheme name for multi-auth connectors
            (e.g., "zendeskOAuth", "zendeskAPIToken")

    Returns:
        CassetteRecordingResult with operation details

    Note:
        For download operations, use range_header in params to limit download size
        (e.g., params={"range_header": "bytes=0-99"}) for cassette recording.
    """
    try:
        # Create log directory and file
        log_dir = Path(".logs")
        log_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"cassette_recording_{timestamp}.json"

        # Execute operation
        executor = LocalExecutor(
            config_path=str(connector_file),
            auth_config=auth_config,
            auth_scheme=auth_scheme,
            config_values=config_values,
            enable_logging=True,
            log_file=str(log_file),
        )

        try:
            execution_result = await executor.execute(ExecutionConfig(entity=entity, action=action, params=params))

            # (if not limited by range_header parameter could be a large download)
            if action == "download" or action == Action.DOWNLOAD:
                if execution_result.success:
                    async for _ in execution_result.data:
                        pass  # consume all chunks
        finally:
            await executor.close()

        # Generate cassette from log file
        generator = CassetteGenerator.from_log_file(str(log_file))

        # Check for logged requests
        logs_summary = generator.list_logs()
        if not logs_summary:
            return CassetteRecordingResult(
                success=False,
                operation=f"{entity}.{action}",
                params=params,
                log_file=str(log_file),
                error="No HTTP requests were logged. Operation may have failed.",
            )

        # Load connector config to get endpoint definition for path parameter extraction
        endpoint = None
        server_variable_names: set[str] = set()
        try:
            connector_config = load_connector_model(connector_file)
            for ent in connector_config.entities:
                if ent.name == entity:
                    action_enum = Action(action)
                    endpoint = ent.endpoints.get(action_enum)
                    break
            # Extract server variable names from OpenAPI spec
            if connector_config.openapi_spec and connector_config.openapi_spec.servers:
                for server in connector_config.openapi_spec.servers:
                    if server.variables:
                        server_variable_names.update(server.variables.keys())
        except Exception:
            # If we can't load the endpoint, path parameters won't be extracted
            # but we can still generate the cassette
            pass

        request_log = generator.log_session.logs[0] if len(generator.log_session.logs) > 0 else None
        file_log = generator.log_session.logs[1] if len(generator.log_session.logs) > 1 else None
        test_spec = generator.generate_test_spec(
            request_log=request_log,
            entity=entity,
            action=action,
            params=params,
            test_name=test_name,
            description=description,
            auth_config=auth_config_mapping,
            server_variable_names=server_variable_names,
            file_log=file_log,
        )

        # Save cassette
        # If output_dir is relative, make it relative to connector_dir
        output_path = output_dir if output_dir.is_absolute() else connector_dir / output_dir
        output_path.mkdir(parents=True, exist_ok=True)
        file_path = generator.save_yaml(test_spec, str(output_path))

        return CassetteRecordingResult(
            success=True,
            operation=f"{entity}.{action}",
            params=params,
            log_file=str(log_file),
            cassette_file=str(file_path),
            http_requests=logs_summary,
        )

    except Exception as e:
        error_trace = traceback.format_exc()
        return CassetteRecordingResult(
            success=False,
            operation=f"{entity}.{action}",
            params=params,
            log_file=str(log_file) if "log_file" in locals() else "N/A",
            error=str(e),
            traceback=error_trace,
        )


async def run_connector_tests_operation(
    connector_file: Path,
    test_dir: Path,
    auth_config: Dict[str, SecretStr],
    verbose: bool = False,
) -> TestRunResult:
    """Run connector tests using recorded cassettes.

    Args:
        connector_file: Path to connector.yaml file
        test_dir: Directory containing test cassettes
        auth_config: Resolved auth config as SecretStr dict
        verbose: Enable verbose output

    Returns:
        TestRunResult with test report
    """
    try:
        # Run tests
        report = await run_tests_async(
            connector_path=connector_file,
            test_dir=test_dir,
            auth_config=auth_config,
            verbose=verbose,
        )

        return TestRunResult(
            success=True,
            connector_file=str(connector_file),
            test_report=report,
        )

    except Exception as e:
        error_trace = traceback.format_exc()
        return TestRunResult(
            success=False,
            connector_file=str(connector_file),
            error=str(e),
            traceback=error_trace,
        )
