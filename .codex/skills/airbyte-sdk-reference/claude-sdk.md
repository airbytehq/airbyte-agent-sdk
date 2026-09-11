# Claude SDK (Anthropic Python) Wiring Patterns

## Single Connector

### Recommended: `agent_tool`

The Anthropic Agent SDK is not one of the SDK's natively supported frameworks, and its tools must return strings, so you always write the tool functions yourself.

In this case, use `agent_tool` to register execute, inspect, and access docs tools so Claude fetches connector documentation on demand (inspect → outline → section → execute). Roles are inferred from each function's signature. There is no native exception-translation strategy for the Agent SDK, so omit `framework=`.

```python
import asyncio
import json
import os
from anthropic import AsyncAnthropic, beta_async_tool
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.stripe import StripeConnector

client = AsyncAnthropic()

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
        airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
        workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
    )
)


@beta_async_tool
@StripeConnector.agent_tool(inspect_tool="stripe_inspect", docs_tool="stripe_read_docs")
async def stripe_execute(entity: str, action: str, params: dict | None = None) -> str:
    result = await connector.execute(entity, action, params or {})
    if hasattr(result, "data"):
        return json.dumps({"data": result.data, "meta": result.meta}, default=str)
    return json.dumps(result, default=str)


@beta_async_tool
@StripeConnector.agent_tool()
async def stripe_inspect() -> str:
    return json.dumps(await connector.inspect_connector(), default=str)


@beta_async_tool
@StripeConnector.agent_tool()
async def stripe_read_docs(section: str | None = None) -> str:
    return await connector.read_skill_docs(section)


async def main():
    runner = client.beta.messages.tool_runner(
        model="<model>",
        max_tokens=4096,
        tools=[stripe_execute, stripe_inspect, stripe_read_docs],
        messages=[{"role": "user", "content": "List my recent customers"}],
    )
    try:
        async for message in runner:
            for block in message.content:
                if block.type == "text":
                    print(block.text)
    finally:
        await connector.close()


if __name__ == "__main__":
    asyncio.run(main())
```

The Messages tool runner reports an `AirbyteToolError` as an error tool result; a manual dispatch loop should catch `AirbyteToolError` itself. The `inspect_tool=`/`docs_tool=` kwargs on the execute decorator weave the exact registered sibling-tool names into the docstring Claude sees; omit them for generic phrasing (they are only valid on the execute tool). You must pass the role explicitly for ambiguous signatures, generic `(*args, **kwargs)` wrappers, or callables whose signature can't be read: `agent_tool("execute")`.

### Alternative: wrapping the prebuilt tools

If you would rather not author tool bodies, `build_connector_tools(connector, framework="none")` returns prebuilt callables whose docstrings carry the same progressive guidance. Anthropic tools must return strings, so thin `@beta_async_tool` adapters serialize the prebuilt results — meaning you still write three small functions, which is why `agent_tool` above is usually just as simple:

```python
import asyncio
import json
import os
from anthropic import AsyncAnthropic, beta_async_tool
from airbyte_agent_sdk import AirbyteAuthConfig, build_connector_tools
from airbyte_agent_sdk.connectors.stripe import StripeConnector

client = AsyncAnthropic()

connector = StripeConnector(
    auth_config=AirbyteAuthConfig(
        airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
        airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
        workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
    )
)
tools = build_connector_tools(connector, framework="none")


@beta_async_tool(description=tools.inspect_connector.__doc__ or "")
async def inspect_connector() -> str:
    return json.dumps(await tools.inspect_connector(), default=str)


@beta_async_tool(description=tools.read_skill_docs.__doc__ or "")
async def read_skill_docs(section: str | None = None) -> str:
    return await tools.read_skill_docs(section)


@beta_async_tool(description=tools.execute.__doc__ or "")
async def execute(entity: str, action: str, params: dict | None = None) -> str:
    return json.dumps(await tools.execute(entity, action, params), default=str)


async def main():
    runner = client.beta.messages.tool_runner(
        model="<model>",
        max_tokens=4096,
        tools=[inspect_connector, read_skill_docs, execute],
        messages=[{"role": "user", "content": "List my recent customers"}],
    )
    try:
        async for message in runner:
            for block in message.content:
                if block.type == "text":
                    print(block.text)
    finally:
        await connector.close()


if __name__ == "__main__":
    asyncio.run(main())
```

`framework="none"` prevents unrelated installed frameworks from being auto-detected. The prebuilt tool names are fixed (`inspect_connector`, `read_skill_docs`, `execute`), so this variant only works for a single connector per agent.

`Connector.tool_utils` is deprecated and retained only for backwards compatibility with existing single-tool integrations.

## Multi-Connector

Mirror the single-connector `agent_tool` pattern for each connector, sharing a single `AirbyteAuthConfig` and an `AsyncAnthropic` client with `tool_runner`. Give every execute, inspect, and docs function a connector-specific name; the prebuilt builder's fixed tool names collide across connectors, so multi-connector agents always use `agent_tool`.

```python
import asyncio
import json
import os
from anthropic import AsyncAnthropic, beta_async_tool
from airbyte_agent_sdk import AirbyteAuthConfig
from airbyte_agent_sdk.connectors.jira import JiraConnector
from airbyte_agent_sdk.connectors.slack import SlackConnector

client = AsyncAnthropic()

auth = AirbyteAuthConfig(
    airbyte_client_id=os.getenv("AIRBYTE_CLIENT_ID"),
    airbyte_client_secret=os.getenv("AIRBYTE_CLIENT_SECRET"),
    workspace_name=os.getenv("AIRBYTE_WORKSPACE_NAME", "default"),
)

jira = JiraConnector(auth_config=auth)
slack = SlackConnector(auth_config=auth)


@beta_async_tool
@JiraConnector.agent_tool(inspect_tool="jira_inspect", docs_tool="jira_read_docs")
async def jira_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute a Jira operation (issues, projects, comments, etc.).

    Args:
        entity: Entity name (e.g. "issues", "projects")
        action: Action to perform (e.g. "list", "get", "create")
        params: Optional parameters for the operation

    Returns:
        JSON string with the operation result
    """
    result = await jira.execute(entity, action, params or {})
    if hasattr(result, "data"):
        return json.dumps({"data": result.data, "meta": result.meta}, default=str)
    return json.dumps(result, default=str)


@beta_async_tool
@JiraConnector.agent_tool()
async def jira_inspect() -> str:
    return json.dumps(await jira.inspect_connector(), default=str)


@beta_async_tool
@JiraConnector.agent_tool()
async def jira_read_docs(section: str | None = None) -> str:
    return await jira.read_skill_docs(section)


@beta_async_tool
@SlackConnector.agent_tool(inspect_tool="slack_inspect", docs_tool="slack_read_docs")
async def slack_execute(entity: str, action: str, params: dict | None = None) -> str:
    """Execute a Slack operation (channels, messages, users, etc.).

    Args:
        entity: Entity name (e.g. "channels", "messages")
        action: Action to perform (e.g. "list", "get", "create")
        params: Optional parameters for the operation

    Returns:
        JSON string with the operation result
    """
    result = await slack.execute(entity, action, params or {})
    if hasattr(result, "data"):
        return json.dumps({"data": result.data, "meta": result.meta}, default=str)
    return json.dumps(result, default=str)


@beta_async_tool
@SlackConnector.agent_tool()
async def slack_inspect() -> str:
    return json.dumps(await slack.inspect_connector(), default=str)


@beta_async_tool
@SlackConnector.agent_tool()
async def slack_read_docs(section: str | None = None) -> str:
    return await slack.read_skill_docs(section)


async def main():
    runner = client.beta.messages.tool_runner(
        model="<model>",
        max_tokens=4096,
        tools=[
            jira_execute,
            jira_inspect,
            jira_read_docs,
            slack_execute,
            slack_inspect,
            slack_read_docs,
        ],
        messages=[{"role": "user", "content": "Find open bugs in Jira and post a summary to #engineering"}],
    )
    try:
        async for message in runner:
            for block in message.content:
                if block.type == "text":
                    print(block.text)
    finally:
        await jira.close()
        await slack.close()


if __name__ == "__main__":
    asyncio.run(main())
```
