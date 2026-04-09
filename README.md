# Airbyte SDK

Type-safe connector execution framework with blessed connectors and full IDE autocomplete.

## Overview

The Airbyte SDK executes connector operations through the Airbyte platform. The platform manages third-party API credentials, handles rate limiting, and provides a unified execution layer.

## Installation

```bash
uv pip install airbyte-agent-sdk
```

## Credentials

You need Airbyte platform credentials to use the SDK:

- **`AIRBYTE_CLIENT_ID`** / **`AIRBYTE_CLIENT_SECRET`** — from your Airbyte Cloud organization settings
- **`connector_id`** — the source UUID for an existing connector (from the Airbyte dashboard or `create()`)

## Quick Start: Connect to an Existing Source

```python
from airbyte_agent_sdk.connectors.stripe import StripeConnector
from airbyte_agent_sdk.types import AirbyteAuthConfig

connector = StripeConnector(auth_config=AirbyteAuthConfig(
    airbyte_client_id="your_client_id",
    airbyte_client_secret="your_client_secret",
    connector_id="your_source_uuid",
))

# List customers — returns typed Pydantic envelope
customers = await connector.customers.list(limit=10)
for c in customers.data:
    print(f"{c.id}: {c.email}")
print(f"More pages? {customers.meta.has_more}")

# Get a single customer
customer = await connector.customers.get(id="cus_123")
print(customer["email"])

# Health check
check = await connector.check()
print(check.status)  # "healthy"
```

## Getting Started: Create a New Source

Use `StripeConnector.create()` to provision a source on Airbyte Cloud:

```python
from airbyte_agent_sdk.connectors.stripe import StripeConnector
from airbyte_agent_sdk.connectors.stripe.models import StripeAuthConfig
from airbyte_agent_sdk.types import AirbyteAuthConfig

connector = await StripeConnector.create(
    airbyte_config=AirbyteAuthConfig(
        airbyte_client_id="your_client_id",
        airbyte_client_secret="your_client_secret",
        workspace_name="my-workspace",
    ),
    auth_config=StripeAuthConfig(api_key="sk_test_..."),
)

# Save the connector_id for future use
print(f"Source created: {connector.connector_id}")

# Now use it
customers = await connector.customers.list(limit=5)
```

## Generic Factory: connect()

Use `connect()` for any connector by name. It auto-reads `AIRBYTE_CLIENT_ID` and `AIRBYTE_CLIENT_SECRET` from the environment:

```python
from airbyte_agent_sdk import connect, list_connectors

# Discover available connectors (bundled connector slugs)
print(list_connectors())  # ['airtable', 'github', 'stripe', ...]

# Connect (reads AIRBYTE_CLIENT_ID/SECRET from env automatically)
stripe = connect("stripe", connector_id="your_source_uuid")

# Execute operations — shorthand form
result = await stripe.execute("customers", "list", params={"limit": 10})
print(result.success)        # True
print(result.data[0]["id"])  # "cus_..."
print(result.meta)           # {"has_more": False}

# ExecutionConfig form also works:
# from airbyte_agent_sdk import ExecutionConfig
# result = await stripe.execute(
#     ExecutionConfig(entity="customers", action="list", params={"limit": 10})
# )

await stripe.close()
```

## Workspace: Full Workspace Access

Use `Workspace` for workspace-level operations: natural language queries, listing connectors, creating and deleting connectors.

```python
from airbyte_agent_sdk import Workspace

async with Workspace(workspace_name="my-workspace") as ws:
    # Ask a question across all connectors
    result = await ws.ask("list my recent Stripe customers")
    print(result.answer)

    # List live connector instances from the API
    # (contrast with list_connectors() which returns bundled connector slugs)
    for c in await ws.list_connectors():
        print(f"{c.name} ({c.id})")

    # Get a connector by name (must be exactly one instance in workspace)
    stripe = await ws.get_connector(name="stripe")
    try:
        result = await stripe.execute("customers", "list", params={"limit": 5})
    finally:
        await stripe.close()
```

### Quick ask() — No Setup Needed

```python
from airbyte_agent_sdk import ask

# Reads AIRBYTE_CLIENT_ID/SECRET from env
result = await ask("who are my top customers?", workspace_name="my-workspace")
print(result.answer)
```

Sync version for scripts and notebooks:

```python
from airbyte_agent_sdk import ask_sync

# Sync version — works in scripts and notebooks
result = ask_sync("who are my top customers?", workspace_name="my-workspace")
print(result.answer)
```

## Available Connectors

Connectors are included in the `airbyte-agent-sdk` package:

```bash
uv pip install airbyte-agent-sdk
```

Currently supported typed connectors: **Stripe** (more coming soon!)

51 connectors available via `connect()` — run `list_connectors()` to see all.

## Advanced: Local Mode (Direct API Calls)

For development and testing, you can bypass the platform and call APIs directly with raw credentials:

```python
from airbyte_agent_sdk.connectors.stripe import StripeConnector
from airbyte_agent_sdk.connectors.stripe.models import StripeAuthConfig

# Local mode — direct HTTP calls to Stripe API
connector = StripeConnector(auth_config=StripeAuthConfig(api_key="sk_test_..."))
customers = await connector.customers.list(limit=5)
```

## Connector YAML Format

Connectors are defined in `connector.yaml` files:

```yaml
connector:
  name: stripe
  version: 1.0.0
  base_url: https://api.stripe.com

auth:
  type: api_key
  config:
    header: Authorization
    prefix: Bearer

entities:
  - name: Customer
    actions: [get, create, update, delete, list]
    endpoints:
      get:
        method: GET
        path: /v1/customers/{id}
      create:
        method: POST
        path: /v1/customers
        body_fields: [email, name, description]
      list:
        method: GET
        path: /v1/customers
        query_params: [limit, starting_after]
    schema:
      type: object
      properties:
        id: {type: string}
        email: {type: string}
        name: {type: string}
```

## Supported Actions

- `get` - Fetch a single entity by ID
- `create` - Create a new entity
- `update` - Update an existing entity
- `delete` - Delete an entity
- `list` - List all entities (paginated)
- `search` - Search with flexible criteria
- `download` - Download binary content
- `authorize` - Verify permissions

## Working with Downloads

The `download` action returns an `AsyncIterator[bytes]` for streaming file content. You can handle this in two ways:

### Option 1: Using the save_download Helper (Recommended)

The SDK provides a convenient helper to save downloads to disk:

```python
from airbyte_agent_sdk import save_download
from airbyte_agent_sdk.connectors.zendesk_support import ZendeskSupportConnector

# Create connector instance
zendesk = ZendeskSupportConnector(
    auth_config={"api_token": "your_token"},
    subdomain="your_subdomain"
)

# Download an article attachment
download_iterator = await zendesk.download_article_attachment(
    article_id="123",
    attachment_id="456"
)

# Save to file
file_path = await save_download(download_iterator, "./downloads/attachment.pdf")
print(f"Downloaded to {file_path}")

# Overwrite existing files
file_path = await save_download(
    download_iterator,
    "./downloads/attachment.pdf",
    overwrite=True
)
```

**Features:**
- ✅ Creates parent directories automatically
- ✅ Returns absolute path to saved file
- ✅ Handles large files efficiently (streams chunks)
- ✅ Cleans up partial files on error
- ✅ Optional overwrite protection
- ✅ Expands `~` for home directory

### Option 2: Manual Handling

You can also manually consume the iterator for custom processing:

```python
# Download and process chunks manually
download_iterator = await zendesk.download_article_attachment(
    article_id="123",
    attachment_id="456"
)

# Save manually
with open("./downloads/attachment.pdf", "wb") as f:
    async for chunk in download_iterator:
        f.write(chunk)
```

## Authentication Types

- `api_key` - API key authentication (most common)
- `bearer_token` - Bearer token in Authorization header
- `basic` - HTTP Basic authentication

## Secret Management

The SDK provides secure handling of sensitive credentials like API keys, tokens, and passwords through the `SecretStr` type and environment variable resolution.

### Environment Variable References

Use the `${ENV_VAR_NAME}` syntax to reference environment variables in your secrets. This is the recommended approach for security:

```python
from airbyte_agent_sdk.executor import LocalExecutor

# Use LocalExecutor directly for local API access
executor = LocalExecutor(
    config_path="path/to/connector.yaml",
    auth_config={"api_key": "${STRIPE_API_KEY}"},
)
```

### CLI Secret Management

The SDK's CLI commands handle secrets differently for security reasons:

#### `cassette record` Command (Explicit Secrets)

The `record` command requires explicit secret mapping via `--secrets` to prevent accidentally recording all environment variables in cassettes:

```bash
# Set your API key
export MY_API_KEY="sk_test_123..."

# Reference it explicitly
uv run airbyte-agent-sdk cassette record ./stripe/ \
  --entity customers \
  --action list \
  --secrets '{"token": "${MY_API_KEY}"}'
```

**Features:**
- ✅ Supports `${ENV_VAR_NAME}` syntax for environment variables
- ✅ Supports literal values: `'{"token": "literal_value"}'`
- ✅ Supports multiple variables: `'{"token": "${PREFIX}_${SUFFIX}"}'`
- ✅ Validates that referenced environment variables exist
- ✅ Prevents accidentally recording secrets in cassette files

**Examples:**

```bash
# Single environment variable
--secrets '{"token": "${STRIPE_API_KEY}"}'

# Multiple environment variables in one value
--secrets '{"token": "${API_PREFIX}_${API_SUFFIX}"}'

# Mix of environment variables and literal values
--secrets '{"token": "${API_KEY}", "client_id": "my_client_123"}'

# Literal value (not recommended for production)
--secrets '{"token": "sk_test_hardcoded"}'
```

#### `test run` Command (Automatic Environment Loading)

The `run` command automatically loads **all environment variables** as potential secrets for backward compatibility:

```bash
# Set your secrets as environment variables
export STRIPE_API_KEY="sk_test_..."
export GITHUB_TOKEN="ghp_..."

# No --secrets needed; test specs reference specific vars
uv run airbyte-agent-sdk test run ./stripe/
```

**Why the difference?**
- `record`: Explicit mapping prevents accidentally capturing all env vars in cassette files
- `run`: Automatic loading maintains backward compatibility and convenience for running tests

### SecretStr Type

All secrets are wrapped in Pydantic's `SecretStr` type for automatic obfuscation in logs and error messages:

```python
from airbyte_agent_sdk.secrets import SecretStr

api_key = SecretStr("sk_test_123")
print(api_key)  # Output: **********
print(repr(api_key))  # Output: SecretStr('**********')
api_key.get_secret_value()  # Returns: 'sk_test_123'
```

**Security benefits:**
- Secrets are automatically hidden in logs
- Error messages don't leak secret values
- String representations are obfuscated
- IDE debuggers show `**********` instead of actual values

### Best Practices

1. **Never hardcode secrets** - Always use environment variables
2. **Use `.env` files locally** - Load with `python-dotenv` or similar
3. **Use `${ENV_VAR}` syntax in cassettes** - Keeps secrets out of version control
4. **Validate env vars exist** - The SDK will error if referenced variables are missing
5. **Use different secrets for dev/prod** - Never use production credentials in tests

Example `.env` file:

```bash
# Development secrets (never commit to git!)
STRIPE_API_KEY=sk_test_...
GITHUB_TOKEN=ghp_...
```

## Architecture

The SDK has a layered architecture:

### Core Components

1. **Config Loader** - Parses OpenAPI 3.1 and legacy YAML formats
2. **HTTP Client** - Makes authenticated HTTP requests
3. **Executor** - Interprets YAML and executes operations
4. **Types** - Pydantic models for validation

### Typed Connector System

1. **Protocol** - Defines interface for all typed connectors
2. **Type Stubs** - TypedDict definitions for full type safety
3. **Wrapper Classes** - Convenient, typed methods for each connector

```
┌─────────────────────────────────────────┐
│     Typed Connectors                    │
│  StripeConnector, GitHubConnector, ...  │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│    connect() / HostedExecutor            │
│   (YAML-driven, works with any API)      │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│          HTTP Client + Auth             │
│      (Bearer, API Key, Basic)           │
└─────────────────────────────────────────┘
```

All connector logic is driven by OpenAPI 3.1 specifications!

## Testing Connectors

The SDK includes a powerful testing framework based on "cassettes" - YAML-based test specifications that capture real API interactions. This allows you to:

- Test connectors without making live API calls
- Validate request/response behavior
- Ensure backward compatibility
- Run tests quickly in CI/CD

### What Are Cassettes?

Cassettes are YAML files that capture:
- The exact HTTP request (method, path, params, headers, body)
- The actual API response (status code, headers, body)
- Input parameters for the operation
- Secret references (using environment variables)

They're stored in `tests/cassettes/` and used for fast, reliable mock testing.

### Generating Cassettes

Use the `cassette record` command to capture real API interactions:

```bash
# Set your API key
export STRIPE_API_KEY="sk_test_..."

# Generate a cassette for listing customers
uv run airbyte-agent-sdk cassette record integrations/stripe/ \
  --entity customers \
  --action list \
  --params '{"limit": 10}' \
  --secrets '{"STRIPE_API_KEY": "${STRIPE_API_KEY}"}' \
  --output integrations/stripe/tests/cassettes

# Generate a cassette for retrieving a customer
uv run airbyte-agent-sdk cassette record integrations/stripe/ \
  --entity customers \
  --action get \
  --params '{"id": "cus_xxx"}' \
  --secrets '{"STRIPE_API_KEY": "${STRIPE_API_KEY}"}' \
  --output integrations/stripe/tests/cassettes
```

**What happens:**
1. The command executes the real operation against the API
2. HTTP requests/responses are logged
3. A YAML cassette file is automatically generated
4. Sensitive data is automatically redacted

**Command options:**
- `--entity` - Entity name (e.g., "customers")
- `--action` - Operation action (e.g., "list", "get", "create")
- `--params` - JSON string of operation parameters
- `--secrets` - JSON mapping of secret names to environment variable references
- `--output` - Directory to save cassette files (default: "tests/cassettes")

### Validating Cassettes

Validate cassette files to ensure they're well-formed:

```bash
uv run airbyte-agent-sdk test validate integrations/stripe/tests/cassettes/customers_list.yaml
```

**Output:**
```
Validating test spec: integrations/stripe/tests/cassettes/customers_list.yaml...
✓ Test specification is valid
```

### Running Tests

Run tests using your cassettes in mock mode (no API calls):

```bash
# Set environment variables for secret resolution
export STRIPE_API_KEY="sk_test_..."

# Run all tests in a directory
uv run airbyte-agent-sdk test run integrations/stripe/ \
  --test-dir integrations/stripe/tests/cassettes \
  --verbose
```

**Output:**
```
Running tests for integrations/stripe/connector.yaml...
Test directory: integrations/stripe/tests/cassettes
Mode: mock

  ✓ customers_list (0.4ms)
  ✓ customers_get (0.2ms)

============================================================
Test Report: integrations/stripe/connector.yaml
Mode: mock
============================================================

Summary:
------------------------------------------------------------
  Total:        2
  Passed:       2 ✓
  Failed:       0 ✗
  Errors:       0 ⚠
  Success Rate: 100.0%
  Duration:     19.8ms
============================================================
✅ ALL TESTS PASSED
============================================================
```

**Test modes:**
- `mock` (default) - Uses cassettes, no real API calls
- More modes coming soon (live, record)

**Output formats:**
- `console` (default) - Human-readable output
- `json` - Machine-readable JSON report
- `html` - HTML report file

```bash
# Generate JSON report
uv run airbyte-agent-sdk test run integrations/stripe/ \
  --test-dir integrations/stripe/tests/cassettes \
  --format json \
  --output results.json

# Generate HTML report
uv run airbyte-agent-sdk test run integrations/stripe/ \
  --test-dir integrations/stripe/tests/cassettes \
  --format html \
  --output report.html
```

### Cassette File Format

Cassettes are YAML files with this structure:

```yaml
test_name: "customers_list"
description: "Captured from real API call"
entity: "customers"
action: "list"

# Secret references (resolved from environment variables)
secrets:
  STRIPE_API_KEY: "${STRIPE_API_KEY}"

# Input parameters for the operation
inputs:
  params:
    limit: 10

# Expected HTTP request (captured from real API)
captured_request:
  method: "GET"
  path: "/v1/customers"
  query_params:
    limit: "10"
  headers: {}
  body: null

# Captured HTTP response (from real API)
captured_response:
  status_code: 200
  headers: {}
  body:
    object: "list"
    data: [...]
```

**Key features:**
- Authentication headers are NOT included - they're auto-injected from `connector.yaml`
- Secrets use environment variable references like `${STRIPE_API_KEY}`
- Response body contains actual data from your test API account

## Anonymous Telemetry

The Airbyte SDK includes optional anonymous telemetry to help us understand how connectors are being used in the wild. This helps us prioritize features and improvements.

### What's Tracked

**What's Tracked (Basic Mode - Default):**
- Connector name and version
- API operations used (entity/action, e.g., "customers/list")
- Success/failure rates
- Performance metrics (timing)
- Error types (not error messages or parameters)
- Execution context (MCP server, direct SDK, etc.)
- System info (Python version, OS)
- Public IP address (for usage analytics and regional insights)
- Anonymous user ID (stored in config to correlate sessions)

**What's NOT Tracked:**
- Your API keys or credentials
- Customer data or PII
- Actual API responses
- Error messages or parameters

### Opt-out

Telemetry is enabled by default. To disable it:

```bash
export AIRBYTE_TELEMETRY_MODE=disabled
```

### Configuration

The SDK stores configuration in `~/.airbyte/connector-sdk/config.yaml`:

```yaml
# Generated user ID for anonymous telemetry
user_id: "550e8400-e29b-41d4-a716-446655440000"

# Set to true for internal Airbyte users
is_internal_user: false
```

The anonymous user ID allows us to understand usage patterns across multiple sessions from the same user. The ID is a random UUID and contains no personally identifiable information. You can delete the config file at any time to generate a new ID.

**For Airbyte employees**: Run the setup script to mark yourself as an internal user:

```bash
./scripts/setup_internal_user.sh
```

Or set the environment variable (takes precedence over config file):

```bash
export AIRBYTE_INTERNAL_USER=true
```

For more details, see our [Privacy Policy](../../PRIVACY.md).

## Development

```bash
# Install dev dependencies
uv pip install -e ".[dev]"

# Run tests
pytest
```

## License

MIT
