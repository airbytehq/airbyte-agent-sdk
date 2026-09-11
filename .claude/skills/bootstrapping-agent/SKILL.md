---
name: bootstrapping-agent
description: Wires up an Airbyte connector for use in a PydanticAI, Claude SDK, or other agent. Generates auth config, connector initialization, prebuilt connector tools, or agent_tool-decorated custom tool functions. Use when adding a connector to an agent or setting up a new agent with a connector.
---

# Bootstrapping an Agent with an Airbyte Connector

## Install the SDK

```bash
uv pip install airbyte-agent-sdk
```

The single `airbyte-agent-sdk` package ships every typed connector. Import them from `airbyte_agent_sdk.connectors.{slug}`.

## Core Pattern (PydanticAI)

Use `build_connector_tools` — the preferred default on supported frameworks — unless the agent needs custom tool bodies:

```python
import os
from pydantic_ai import Agent
from airbyte_agent_sdk import AirbyteAuthConfig, build_connector_tools
from airbyte_agent_sdk.connectors.stripe import StripeConnector

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
        airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
        workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
    )
)

tools = build_connector_tools(connector, framework="pydantic_ai")

agent = Agent(
    "<provider:model>",
    tools=tools.as_list(),
    system_prompt=(
        "You are a helpful assistant with access to Stripe. "
        "Inspect the connector, read the relevant docs, then use execute to look up data. "
        "Ask for clarification if a request is ambiguous."
    ),
)
```

**Always hosted mode**: Use `AirbyteAuthConfig` with `airbyte_client_id` and `airbyte_client_secret`. Never generate local auth code.

## Custom Tool Bodies (`agent_tool`)

When a tool needs a custom body, use `agent_tool` even when the framework is natively supported. Decorate and register execute, inspect, and docs functions so the model can discover connector capabilities progressively:

```python
manual_agent = Agent("<provider:model>")

@manual_agent.tool_plain
@StripeConnector.agent_tool(
    framework="pydantic_ai",
    inspect_tool="stripe_inspect",
    docs_tool="stripe_read_docs",
)
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})

@manual_agent.tool_plain
@StripeConnector.agent_tool(framework="pydantic_ai")
async def stripe_inspect():
    return await connector.inspect_connector()

@manual_agent.tool_plain
@StripeConnector.agent_tool(framework="pydantic_ai")
async def stripe_read_docs(section: str | None = None):
    return await connector.read_skill_docs(section)
```

The framework registration decorator goes on top and `agent_tool` goes underneath. `agent_tool` is a `@classmethod`: use `StripeConnector.agent_tool(...)`, not `connector.agent_tool(...)`. The role is inferred from each signature — `(entity, action, ...)` → execute, `(section, ...)` → docs, `()` → inspect; extra params are allowed, and ambiguous signatures must pass the role explicitly, e.g. `agent_tool("execute")`.

### Automatic Retry Translation

Both `build_connector_tools(..., framework="pydantic_ai")` and `agent_tool(framework="pydantic_ai")` translate retryable errors to PydanticAI's `ModelRetry`. Use `framework="langchain"`, `"openai_agents"`, or `"mcp"` for the corresponding supported framework. No extra translation decorator is needed.

Reference demo: `connector-sdk/examples/demo_agent.py` (mocked, no credentials needed: `--mock`).

## Unsupported Frameworks

On a framework the SDK does not natively support, use the same three-function `agent_tool` pattern and omit `framework=` (role inference works the same as above):

```python
@StripeConnector.agent_tool(inspect_tool="stripe_inspect", docs_tool="stripe_read_docs")
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})

@StripeConnector.agent_tool()
async def stripe_inspect():
    return await connector.inspect_connector()

@StripeConnector.agent_tool()
async def stripe_read_docs(section: str | None = None):
    return await connector.read_skill_docs(section)
```

Register all three with the target framework. The execute docstring steers the model through inspect → docs outline → docs section → execute instead of embedding the full entity/action reference. Failures raise `AirbyteToolError` (`from airbyte_agent_sdk import AirbyteToolError`) by default — no framework auto-detection; pass `framework="..."` to target a supported framework's retry signal instead. The optional `inspect_tool=`/`docs_tool=` kwargs put the exact registered sibling-tool names into the execute docstring; omit them for generic phrasing.

## Legacy Integrations (`tool_utils`)

`Connector.tool_utils` is deprecated; it remains available only for existing integrations that use a single broad tool description. Never generate it for new tools. When editing a legacy integration, keep the framework decorator on top and `tool_utils` underneath unless the task includes migrating it to the three-tool `agent_tool` flow.

## Verify the Setup

```python
check = await connector.check()
if check.status == "healthy":
    print(f"Connected — checked {check.checked_entity}/{check.checked_action}")
else:
    print(f"Failed: {check.error}")
```

## Framework Detection

Detect the developer's framework from their existing imports:
- `from pydantic_ai import Agent` → Use PydanticAI patterns
- `from anthropic import Anthropic` → Use Claude SDK patterns
- If unclear, ask which framework they're using

## Connector Naming Convention

All connectors ship in `airbyte-agent-sdk`. Import each one from `airbyte_agent_sdk.connectors.{slug}`:

| Connector | Import | Class |
|-----------|--------|-------|
| stripe | `airbyte_agent_sdk.connectors.stripe` | `StripeConnector` |
| zendesk-support | `airbyte_agent_sdk.connectors.zendesk_support` | `ZendeskSupportConnector` |
| hubspot | `airbyte_agent_sdk.connectors.hubspot` | `HubspotConnector` |

Hyphens in connector slugs become underscores in the submodule path.

## Environment Variables

The developer needs these in their `.env`:

```
AIRBYTE_CLIENT_ID=your_client_id
AIRBYTE_CLIENT_SECRET=your_client_secret
AIRBYTE_WORKSPACE_NAME=your_workspace_name
```

## References

- [SDK API reference](../airbyte-sdk-reference/sdk-api.md) — full API signatures and options
- [PydanticAI patterns](../airbyte-sdk-reference/pydantic-ai.md) — complete runnable examples
- [Claude SDK patterns](../airbyte-sdk-reference/claude-sdk.md) — Anthropic Python SDK examples
