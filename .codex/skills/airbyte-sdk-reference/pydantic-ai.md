# PydanticAI Wiring Patterns

## Single Connector

```python
import asyncio
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


async def main():
    result = await agent.run("List my recent customers")
    print(result.output)
    await connector.close()


if __name__ == "__main__":
    asyncio.run(main())
```

`build_connector_tools` is the preferred default when custom tool bodies are not needed. It registers the progressive inspect → docs → execute flow and applies PydanticAI exception translation. Its tool names are fixed, so it covers one connector per agent. See Multi-Connector below for the two-plus-connector pattern.

### Custom Tool Bodies (`agent_tool`)

When a tool needs a custom body, decorate execute, inspect, and docs with `agent_tool(framework="pydantic_ai")`. The PydanticAI registration decorator goes on top:

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

`agent_tool` enriches each function's docstring before PydanticAI reads it for tool registration. The execute description names its inspect and docs siblings and guides the model to fetch documentation on demand.

### Automatic Exception Translation

Both `build_connector_tools(..., framework="pydantic_ai")` and `agent_tool(framework="pydantic_ai")` translate retryable runtime errors (`ConnectorValidationError`, `RateLimitError`, `NetworkError`, `TimeoutError`, output-too-large) into `ModelRetry` so the LLM can self-correct on the next agent turn.

Recovery example:

```python
# Agent calls with a bad action → ModelRetry → agent retries with corrected args
result = await agent.run("List Stripe customers")
# Internally: first tool call raises ConnectorValidationError → the SDK translates
# to ModelRetry → pydantic-ai re-prompts with the error → agent corrects the call.
```

For non-Connector callables, use the standalone `@translate_exceptions(framework="pydantic_ai")` from `airbyte_agent_sdk`. `Connector.tool_utils` is deprecated — it remains available for backwards compatibility with existing one-tool integrations, but must not be used for new tools.

See: `examples/demo_agent.py` for a runnable end-to-end demo.

## Multi-Connector

Multi-connector agents use `agent_tool`: the builder's fixed tool names (`execute`, `inspect_connector`, `read_skill_docs`) collide when registered for more than one connector, so each connector gets its own three functions with connector-specific names. Extract `AirbyteAuthConfig(...)` into a shared `auth` variable and construct one typed connector per service.

```python
import asyncio
import os
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.jira import JiraConnector
from airbyte_agent_sdk.connectors.slack import SlackConnector
from pydantic_ai import Agent

auth = AirbyteAuthConfig(
    airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
    airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
    workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
)

jira = JiraConnector(auth_config=auth)
slack = SlackConnector(auth_config=auth)

agent = Agent(
    "<provider:model>",
    system_prompt=(
        "You are a project assistant. You can read Jira issues and post to Slack channels. "
        "Use jira_inspect and jira_read_docs before jira_execute; do the same for Slack."
    ),
)


@agent.tool_plain
@JiraConnector.agent_tool(
    framework="pydantic_ai",
    inspect_tool="jira_inspect",
    docs_tool="jira_read_docs",
)
async def jira_execute(entity: str, action: str, params: dict | None = None):
    """Execute a Jira operation."""
    return await jira.execute(entity, action, params or {})

@agent.tool_plain
@JiraConnector.agent_tool(framework="pydantic_ai")
async def jira_inspect():
    return await jira.inspect_connector()

@agent.tool_plain
@JiraConnector.agent_tool(framework="pydantic_ai")
async def jira_read_docs(section: str | None = None):
    return await jira.read_skill_docs(section)


@agent.tool_plain
@SlackConnector.agent_tool(
    framework="pydantic_ai",
    inspect_tool="slack_inspect",
    docs_tool="slack_read_docs",
)
async def slack_execute(entity: str, action: str, params: dict | None = None):
    """Execute a Slack operation."""
    return await slack.execute(entity, action, params or {})

@agent.tool_plain
@SlackConnector.agent_tool(framework="pydantic_ai")
async def slack_inspect():
    return await slack.inspect_connector()

@agent.tool_plain
@SlackConnector.agent_tool(framework="pydantic_ai")
async def slack_read_docs(section: str | None = None):
    return await slack.read_skill_docs(section)


async def main():
    result = await agent.run("Find open bugs in Jira and post a summary to #engineering")
    print(result.output)
    await jira.close()
    await slack.close()


if __name__ == "__main__":
    asyncio.run(main())
```

### Key Points

- `AirbyteAuthConfig` is exported at the `airbyte_agent_sdk` package root — import it once and share across connectors
- Each connector includes execute, inspect, and docs functions with connector-specific names
- Custom tool bodies use `agent_tool(framework="pydantic_ai")`; `tool_utils` is deprecated
- Per-connector overrides (e.g. `connector_id=` when multiple of the same type exist in the workspace) go on the typed constructor

## System Prompt Patterns

Describe what the agent can do in terms of the connectors:

```python
agent = Agent(
    "<provider:model>",
    system_prompt=(
        "You are a customer support assistant. "
        "You can look up customer details in Stripe and create tickets in Jira. "
        "Always verify customer identity before sharing billing information."
    ),
)
```

## Verifying Setup

After creating a connector, verify credentials work:

```python
check = await connector.check()
if check.status == "healthy":
    print(f"Connected — checked {check.checked_entity}/{check.checked_action}")
else:
    print(f"Connection failed: {check.error}")
```
