---
name: building-multi-connector-agent
description: Builds a complete agent with multiple Airbyte connectors using PydanticAI or Claude SDK. Scaffolds project structure, wires up connectors, composes tools, and creates a run loop. Use when building an agent with multiple connectors or scaffolding a new agent project.
---

# Building a Multi-Connector Agent

Use this when an agent needs two or more Airbyte connectors.

## Going from Single to Multi

The `bootstrapping-agent` skill shows the default single-connector pattern: `AirbyteAuthConfig` plus `build_connector_tools`. The builder's `execute`, `inspect_connector`, and `read_skill_docs` names are fixed, so the tool sets for more than one connector collide when registered on the same agent. Renaming the callables at registration avoids the collision, but the generated `execute` guidance still names `inspect_connector` and `read_skill_docs`, pointing the model at the wrong tools. Multi-connector agents write their own tool functions with `@Connector.agent_tool(...)`, which weaves the real names in through `inspect_tool=` and `docs_tool=`:

1. Build a single `AirbyteAuthConfig(...)` so credentials are shared across connectors.
2. Construct one typed connector per service (e.g. `JiraConnector(auth_config=auth)`).
3. Define execute, inspect, and docs functions for each connector, each with its own `@Connector.agent_tool(...)` decorator.

Use connector-specific function names so the framework registers six unambiguous tools for two connectors.

## Install the SDK

```bash
uv pip install airbyte-agent-sdk
```

The single `airbyte-agent-sdk` package bundles every typed connector without per-connector installs.

## Core Pattern (PydanticAI)

```python
import os
from pydantic_ai import Agent
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.jira import JiraConnector
from airbyte_agent_sdk.connectors.slack import SlackConnector

# Shared credentials — all connectors reuse the same AirbyteAuthConfig
auth = AirbyteAuthConfig(
    airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
    airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
    workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
)

jira = JiraConnector(auth_config=auth)
slack = SlackConnector(auth_config=auth)
```

If the workspace contains multiple connectors of the same type, pin one by passing `connector_id=os.getenv("JIRA_CONNECTOR_ID")` to the constructor.

## Three Progressive Tools Per Connector

Each connector gets its own execute, inspect, and docs functions. Do not combine connectors into a mega-tool; separate names give the LLM clear, independent tool descriptions and let it read only the relevant connector docs.

`agent_tool` is a `@classmethod` — decorate with `@JiraConnector.agent_tool(...)`, not `@jira.agent_tool(...)`.

```python
agent = Agent(
    "<provider:model>",
    system_prompt=(
        "You are a helpful assistant with access to Jira and Slack. "
        "Use the jira_execute tool to read Jira issues and the slack_execute tool to post messages. "
        "Ask for clarification if a request is ambiguous."
    ),
)

@agent.tool_plain
@JiraConnector.agent_tool(
    framework="pydantic_ai",
    inspect_tool="jira_inspect",
    docs_tool="jira_read_docs",
)
async def jira_execute(entity: str, action: str, params: dict | None = None):
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
    return await slack.execute(entity, action, params or {})

@agent.tool_plain
@SlackConnector.agent_tool(framework="pydantic_ai")
async def slack_inspect():
    return await slack.inspect_connector()

@agent.tool_plain
@SlackConnector.agent_tool(framework="pydantic_ai")
async def slack_read_docs(section: str | None = None):
    return await slack.read_skill_docs(section)
```

For LangChain, OpenAI Agents, or FastMCP, keep the same three-functions-per-connector structure and change `framework=` plus the outer registration decorator. Omit `framework=` for unsupported frameworks and handle `AirbyteToolError` in the dispatch loop.

`Connector.tool_utils` is deprecated and remains available only for backwards compatibility with existing one-tool integrations. Do not generate it for new multi-connector agents.

## System Prompt

Describe the agent's purpose and what each connector does:

```python
agent = Agent(
    "<provider:model>",
    system_prompt=(
        "You are a customer support assistant. "
        "Use the stripe tool to look up customer billing data. "
        "Use the jira tool to create and track support tickets. "
        "Use the slack tool to notify the support team."
    ),
)
```

## Run Loop

### PydanticAI

```python
import asyncio

async def main():
    result = await agent.run("Find open P0 bugs and post a summary to #engineering")
    print(result.output)
    await jira.close()
    await slack.close()

asyncio.run(main())
```

### Claude SDK (Anthropic Python)

See [Claude SDK patterns](../airbyte-sdk-reference/claude-sdk.md) for the full message loop with tool handling.

## Project Structure

For a new agent project:

```
my-agent/
├── pyproject.toml       # dependencies: airbyte-agent-sdk, pydantic-ai or anthropic
├── .env                 # AIRBYTE_CLIENT_ID, AIRBYTE_CLIENT_SECRET, AIRBYTE_WORKSPACE_NAME
├── agent.py             # Entry point: auth config, connectors, agent + tools, run loop
└── README.md
```

### pyproject.toml

```toml
[project]
name = "my-agent"
requires-python = ">=3.11"
dependencies = [
    "airbyte-agent-sdk",
    "pydantic-ai",
    "python-dotenv",
]
```

## Environment Variables

```
AIRBYTE_CLIENT_ID=your_client_id
AIRBYTE_CLIENT_SECRET=your_client_secret
AIRBYTE_WORKSPACE_NAME=your_workspace_name
```

## References

- [SDK API reference](../airbyte-sdk-reference/sdk-api.md) — `AirbyteAuthConfig`, `build_connector_tools`, and `agent_tool`
- [PydanticAI patterns](../airbyte-sdk-reference/pydantic-ai.md) — multi-connector example
- [Claude SDK patterns](../airbyte-sdk-reference/claude-sdk.md) — multi-connector example
- [Connector discovery](../airbyte-sdk-reference/connector-discovery.md) — finding available connectors
