# Airbyte Agent SDK — Public API Reference

## Global Configuration

```python
import airbyte_agent_sdk

# Set global credentials (used as defaults by connect() and Workspace)
airbyte_agent_sdk.configure(
    *,
    client_id: str,           # Airbyte OAuth client ID
    client_secret: str,       # Airbyte OAuth client secret
    organization_id: str | None = None,  # Multi-org routing
    workspace_name: str = "default",
)
# Calling again overwrites. Explicit kwargs to connect() take priority.
# Credential resolution order: explicit arg → configure() → env vars
```

**Environment variables** (fallback when `configure()` not called):
- `AIRBYTE_CLIENT_ID`
- `AIRBYTE_CLIENT_SECRET`
- `AIRBYTE_ORGANIZATION_ID`

## connect() — One-Call Factory

```python
from airbyte_agent_sdk import connect

connector = connect(
    connector_name: str,      # Slug, e.g. "stripe" or "zendesk-support"
    *,
    client_id: str | None = None,
    client_secret: str | None = None,
    workspace_name: str = "default",  # Workspace for connector lookup
    connector_id: str | None = None,  # Direct source ID (skips lookup)
    organization_id: str | None = None,
    auth_config: AirbyteAuthConfig | None = None,
)
# Returns typed connector (e.g. StripeConnector) if package installed,
# otherwise HostedExecutor. Always hosted mode.
# Raises ValueError if connector_name unknown or no credentials resolvable.
```

## list_connectors()

```python
from airbyte_agent_sdk import list_connectors

names: list[str] = list_connectors()
# Returns sorted list of all available connector slugs.
```

## AirbyteAuthConfig

```python
from airbyte_agent_sdk.types import AirbyteAuthConfig

auth = AirbyteAuthConfig(
    workspace_name: str | None = None,       # Aliases: customer_name, external_user_id
    organization_id: str | None = None,
    airbyte_client_id: str | None = None,    # Required for hosted mode
    airbyte_client_secret: str | None = None, # Required for hosted mode
    connector_id: str | None = None,          # Skips workspace lookup if set
)
```

## Connector Methods

### execute()

```python
result = await connector.execute(
    entity: str,              # e.g. "customers", "issues"
    action: str,              # "list", "get", "create", "update", "delete", "search"
    params: dict | None = None,
)
# List actions return envelope: result.data (list) + result.meta (has_more, etc.)
# Get/create/update/delete return raw dict.
# Raises RuntimeError on execution failure.
```

### check()

```python
check_result = await connector.check()
# Returns CheckResult with:
#   status: "healthy" | "unhealthy"
#   error: str | None
#   checked_entity: str | None
#   checked_action: str | None
```

### list_entities()

```python
entities = connector.list_entities()
# Returns list of dicts, each with:
#   entity_name: str
#   description: str | None
#   available_actions: list[str]
#   parameters: dict[str, list[dict]]  # action -> param list
```

### entity_schema()

```python
schema = connector.entity_schema("customers")
# Returns JSON schema dict for the entity, or None if not found.
```

**Note**: `list_entities()` and `entity_schema()` are only available on typed connectors, NOT on `HostedExecutor`.

## build_connector_tools() — Default Tool Integration

`build_connector_tools` is the preferred default on supported frameworks when the agent does not need custom tool bodies. It returns execute, inspect, and docs callables already bound to the connector:

```python
from airbyte_agent_sdk import build_connector_tools
from pydantic_ai import Agent

tools = build_connector_tools(connector, framework="pydantic_ai")
agent = Agent("openai:gpt-4o", tools=tools.as_list())
```

The default progressive flow is `inspect_connector()` → `read_skill_docs()` → `read_skill_docs(section="...")` → `execute(...)`. Set `use_progressive_docs=False` only when an existing integration requires one broad execute-tool description. If you omit `framework`, the SDK auto-detects an installed supported framework, and falls back to `"none"` with a warning when it finds none; pass `framework="none"` to force framework-neutral `AirbyteToolError` failures without the warning.

The returned callables keep fixed names (`inspect_connector`, `read_skill_docs`, `execute`), so the tool sets for more than one connector collide on the same agent. Renaming the callables at registration avoids the collision, but the generated `execute` guidance still tells the model to call `inspect_connector` and `read_skill_docs`, so it points at the wrong tools. `agent_tool` is the supported fix: it weaves your own names into that guidance through `inspect_tool=` and `docs_tool=`.

**Main options:**

| Parameter | Default | Effect |
|-----------|---------|--------|
| `framework` | `None` | Auto-detect, or explicitly target `pydantic_ai`, `langchain`, `openai_agents`, `mcp`, or `none` |
| `docs_provider` | `None` | Optional docs provider for local connectors |
| `use_progressive_docs` | `True` | Expose inspect, docs, and execute rather than execute only |
| `max_output_chars` | `100_000` | Max serialized execute output; `None` disables |
| `internal_retries` | `0` | Silent transient-runtime retries before surfacing failure |

## Connector.agent_tool — Custom Tool Bodies and Unsupported Frameworks

Use `agent_tool` when a tool needs a custom body, when the framework is not natively supported, or for multi-connector agents. Every new user-written connector tool uses it, including tools for supported frameworks. It is a `@classmethod` on typed connector classes and requires parentheses. Decorate execute, inspect, and docs functions per connector:

```python
@agent.tool_plain
@StripeConnector.agent_tool(
    framework="pydantic_ai",
    inspect_tool="stripe_inspect",
    docs_tool="stripe_read_docs",
)
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})

@agent.tool_plain
@StripeConnector.agent_tool(framework="pydantic_ai")
async def stripe_inspect():
    return await connector.inspect_connector()

@agent.tool_plain
@StripeConnector.agent_tool(framework="pydantic_ai")
async def stripe_read_docs(section: str | None = None):
    return await connector.read_skill_docs(section)
```

Roles are inferred from `(entity, action, ...)`, `()`, and `(section, ...)` signatures. Pass `"execute"`, `"inspect_connector"`, or `"read_skill_docs"` explicitly when a wrapper has an ambiguous or unreadable signature. The optional `inspect_tool=` and `docs_tool=` names apply only to execute and make its generated guidance refer to the exact registered sibling tools.

Set `framework="pydantic_ai"`, `"langchain"`, `"openai_agents"`, or `"mcp"` to translate failures into that framework's signal. Omitting `framework` deliberately uses `"none"` without auto-detection and raises `AirbyteToolError`. A value outside that list raises `ValueError`; one of those frameworks whose package isn't installed in your environment raises `RuntimeError` when a failure is translated.

**Failure semantics per framework** (identical for `build_connector_tools`, `agent_tool`, and `translate_exceptions`):

| `framework=` | Tool failures surface as | Framework-side wiring |
|--------------|--------------------------|-----------------------|
| `"pydantic_ai"` | raises `pydantic_ai.ModelRetry` | none — the agent retries |
| `"langchain"` | raises `langchain_core.tools.ToolException` | pass `handle_tool_error=True` so the message returns to the model instead of aborting the run |
| `"openai_agents"` | returns the failure message as the tool result (never raises) | register with `function_tool(..., strict_mode=False)` for `params: dict` |
| `"mcp"` | raises `fastmcp.exceptions.ToolError` | FastMCP serializes it as an errored tool result |
| `"none"` | raises `airbyte_agent_sdk.AirbyteToolError` | catch it in the dispatch loop and hand the message to the model |

**Main options:**

| Parameter | Default | Effect |
|-----------|---------|--------|
| `role` | inferred | `execute`, `inspect_connector`, or `read_skill_docs` |
| `inspect_tool` / `docs_tool` | `None` | Exact sibling names included in execute guidance |
| `framework` | `"none"` | Failure translation target; never auto-detected |
| `max_output_chars` | role-dependent | `100_000` for execute and unlimited for inspect/docs |
| `internal_retries` | `0` | Silent transient-runtime retries before surfacing failure |

## Connector.tool_utils — Deprecated Legacy Integration

`tool_utils` is deprecated — a backwards-compatible `@classmethod` retained only for existing integrations that expose one broad connector tool. Do not use it for new tools; use `build_connector_tools` or `agent_tool(framework="...")` instead. It decorates a tool function to:
1. Append connector capabilities to the function's docstring (so the LLM knows what's available)
2. Guard output size and raise `pydantic_ai.ModelRetry` (or `RuntimeError`) if too large

```python
# Bare usage (all defaults):
@agent.tool_plain
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})

# Parameterized usage:
@agent.tool_plain
@StripeConnector.tool_utils(update_docstring=True, max_output_chars=50_000)
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

For existing code, stack the framework decorator on top and `tool_utils` underneath; the legacy ENTITIES/ACTIONS/PARAMETERS block is appended to `__doc__` and flows into the tool description automatically.

```python
# Anthropic async SDK:
@beta_async_tool
@StripeConnector.tool_utils
async def stripe_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute a Stripe API operation."""
    return await connector.execute(entity, action, params or {})
```

**Options:**

| Parameter | Default | Effect |
|-----------|---------|--------|
| `update_docstring` | `True` | Appends entity/action/schema descriptions to `__doc__` |
| `max_output_chars` | `100_000` | Max serialized output; `None` disables |

**Important**: `tool_utils` is NOT available on `HostedExecutor`. Always import the typed connector class.

## Package Naming

- **Install**: `uv pip install airbyte-agent-sdk` — one package ships every typed connector.
- **Recommended usage**: `from airbyte_agent_sdk import connect; stripe = connect("stripe")` returns a typed connector instance (e.g. `StripeConnector`).
- **Direct class import** (when you need the class itself, e.g. for `@Connector.agent_tool(...)`): `from airbyte_agent_sdk.connectors.{name} import {Name}Connector`
  - Slug hyphens become underscores: `zendesk-support` → `airbyte_agent_sdk.connectors.zendesk_support`
  - Class name: PascalCase + "Connector": `ZendeskSupportConnector`
- `AirbyteAuthConfig` is importable from `airbyte_agent_sdk.types`.

## Resource cleanup

The object returned by `connect()` is an async context manager. Prefer
`async with` so HTTP resources are released automatically:

```python
async with connect("stripe") as stripe:
    result = await stripe.customers.list(limit=10)
```

If you need manual control, call `close()` explicitly:

```python
connector = connect("stripe")
try:
    result = await connector.customers.list(limit=10)
finally:
    await connector.close()
```
