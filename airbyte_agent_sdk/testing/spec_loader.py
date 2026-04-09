"""
Test specification loader for YAML-based test files.

Loads and parses test specifications from YAML files into Pydantic models.
"""

import os
from pathlib import Path
from typing import Any, Dict, List

import yaml
from pydantic import ValidationError

from airbyte_agent_sdk.secrets import (
    SecretStr,
    convert_to_secret_dict,
    resolve_env_var_references,
)

from .models import TestSpec


def resolve_secret_references(
    data: Dict[str, Any],
    secrets: Dict[str, SecretStr] | None = None,
    env_vars: Dict[str, str] | None = None,
) -> Dict[str, SecretStr]:
    """
    Resolve secret references in the format ${ENV_VAR_NAME}.

    Args:
        data: Dictionary potentially containing secret references
        secrets: Optional dict of secret values to use. If not provided, will read from env vars.
        env_vars: Optional dict of environment variables to use for resolving ${VAR} references.
                 If not provided, uses os.environ.

    Returns:
        Dictionary with secret references resolved and wrapped in SecretStr

    Example:
        Input: {"STRIPE_API_KEY": "${STRIPE_TEST_ACCOUNT_1}"}
        Output: {"STRIPE_API_KEY": SecretStr("sk_test_actual_value")}
    """
    if secrets is None:
        secrets = {}

    # Build environment dict for resolution
    # Priority: secrets dict first, then env_vars/os.environ
    env_dict: Dict[str, str] = {}

    # Add env_vars or os.environ as base
    if env_vars is not None:
        env_dict.update(env_vars)
    else:
        env_dict.update(os.environ)

    # Add provided secrets (these take priority)
    for key, secret_str in secrets.items():
        env_dict[key] = secret_str.get_secret_value()

    # Use resolve_env_var_references to handle ${VAR} substitution
    resolved_dict = resolve_env_var_references(data, env_vars=env_dict, strict=False)

    # Convert to SecretStr dict
    return convert_to_secret_dict(resolved_dict)


def load_test_spec(
    file_path: Path,
    auth_config: Dict[str, SecretStr] | None = None,
) -> TestSpec:
    """
    Load a single test specification from a YAML file.

    Args:
        file_path: Path to the YAML test specification file
        auth_config: Optional dict of auth config values for resolving ${ENV_VAR} references

    Returns:
        Parsed TestSpec object

    Raises:
        FileNotFoundError: If the file doesn't exist
        yaml.YAMLError: If the YAML is malformed
        ValidationError: If the YAML doesn't match TestSpec schema
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Test spec file not found: {file_path}")

    with open(file_path) as f:
        raw_data = yaml.safe_load(f)

    if not raw_data:
        raise ValueError(f"Empty test spec file: {file_path}")

    # Resolve secret references in the auth_config dict
    if "auth_config" in raw_data:
        raw_data["auth_config"] = resolve_secret_references(raw_data["auth_config"], secrets=auth_config)

    try:
        return TestSpec(**raw_data)
    except ValidationError as e:
        raise ValueError(f"Invalid test spec in {file_path}: {e}") from e


def load_test_specs(
    directory: Path,
    auth_config: Dict[str, SecretStr] | None = None,
    pattern: str = "*.yaml",
) -> List[TestSpec]:
    """
    Load all test specifications from a directory.

    Args:
        directory: Path to directory containing YAML test specs
        auth_config: Optional dict of auth config values for resolving ${ENV_VAR} references
        pattern: Glob pattern for matching test files (default: "*.yaml")

    Returns:
        List of parsed TestSpec objects

    Raises:
        FileNotFoundError: If the directory doesn't exist
        ValidationError: If any YAML file doesn't match TestSpec schema
    """
    if not directory.exists():
        raise FileNotFoundError(f"Test spec directory not found: {directory}")

    if not directory.is_dir():
        raise ValueError(f"Not a directory: {directory}")

    specs: List[TestSpec] = []
    test_files = sorted(directory.glob(pattern))

    if not test_files:
        raise ValueError(f"No test spec files found in {directory} matching pattern '{pattern}'")

    for file_path in test_files:
        try:
            spec = load_test_spec(file_path, auth_config=auth_config)
            specs.append(spec)
        except Exception as e:
            # Re-raise with more context
            raise ValueError(f"Failed to load test spec from {file_path}: {e}") from e

    return specs


def validate_test_spec_file(file_path: Path) -> tuple[bool, str | None]:
    """
    Validate a test specification file without loading auth config.

    Args:
        file_path: Path to the YAML test specification file

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if the spec is valid, False otherwise
        - error_message: None if valid, error description if invalid
    """
    try:
        load_test_spec(file_path, auth_config={})
        return True, None
    except FileNotFoundError as e:
        return False, str(e)
    except yaml.YAMLError as e:
        return False, f"YAML parsing error: {e}"
    except ValidationError as e:
        return False, f"Validation error: {e}"
    except Exception as e:
        return False, f"Unexpected error: {e}"
