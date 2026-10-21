# Airbyte Agent SDK

Typed connector tools for working with third-party APIs, with full IDE autocomplete.

## Overview

The Airbyte Agent SDK provides 50+ connectors with typed tools for third-party APIs. Run connectors locally with your own credentials in connector-specific auth configs; the SDK makes direct calls to each third-party API.

## How to install

```bash
uv pip install airbyte-agent-sdk
```

## Tool integration

The SDK ships a tool builder and two connector-tool decorators for turning connector calls into LLM tools with retry-aware exception translation, output-size guards, and framework-specific error signalling, plus `translate_exceptions` for callables that are not connector tools. Pick from these in this order:

- **`build_connector_tools(connector, framework="...")`** — the simplest, preferred default on supported frameworks (PydanticAI, LangChain, OpenAI Agents, FastMCP) when you do not need custom tool bodies. Returns `inspect_connector`, `read_skill_docs`, and `execute` callables bound to one connector; the tool names are fixed, so register one connector's tool set per agent. With a local connector, `inspect_connector` returns a `mode: "local"` payload with a warning, and `read_skill_docs` returns the full generated connector docs; a section request returns a notice followed by the same docs. Pass `use_progressive_docs=False` to make `tools.as_list()` expose only `execute` with the legacy rich description.
- **`@<Connector>.agent_tool(...)`** — use when you need custom tool bodies, a framework the SDK does not natively support, or a multi-connector agent. Decorate three functions (execute, inspect, docs) and the execute docstring steers the agent through the inspect → docs → execute flow instead of embedding the full entity/action reference. On supported frameworks pass `framework="pydantic_ai"`, `"langchain"`, `"openai_agents"`, or `"mcp"` to target that framework's failure signal; on unsupported frameworks omit it and failures raise `AirbyteToolError` (`framework="none"`; no auto-detection).
- **`@<Connector>.tool_utils`** — deprecated; retained only for backwards compatibility with existing integrations that use one broad, generated-description tool. Do not use it for new tools. It auto-detects supported frameworks and remains available so existing integrations can migrate independently.
- **`@translate_exceptions`** — same translation behaviour for any callable that is not a generated `Connector` (custom helpers, eval harnesses, ad-hoc tools).

The builder and decorators preserve async callables, `__name__`, and `__doc__`. Transient runtime failures (429/5xx, network, timeout) can be retried silently via `internal_retries=N`. Output exceeding `max_output_chars` (default 100 KB) is converted to the framework's retry signal so the LLM can narrow the query.

> **Pick one SDK decorator per tool.** `agent_tool` and legacy `tool_utils` already include exception translation. Stacking `@translate_exceptions` with either decorator is detected and short-circuited.

### Prebuilt connector tools (default)

```python
import os

from pydantic_ai import Agent
from airbyte_agent_sdk import build_connector_tools
from airbyte_agent_sdk.connectors.stripe import StripeConnector, StripeAuthConfig

stripe = StripeConnector(
    auth_config=StripeAuthConfig(api_key=os.environ["STRIPE_API_KEY"])
)
tools = build_connector_tools(stripe, framework="pydantic_ai")

agent = Agent("openai:gpt-4o", tools=tools.as_list())
```

The model-facing docs flow is `inspect_connector()` -> `read_skill_docs()` -> `read_skill_docs(section="...")` -> `execute(...)`. Locally, `inspect_connector()` returns a `mode: "local"` payload with a warning, and `read_skill_docs()` returns the full generated connector docs; a section request adds a notice that section-specific docs are unavailable, then returns the same full docs.

The builder covers one connector per agent — the tool names are fixed (`inspect_connector`, `read_skill_docs`, `execute`), so the tool sets for multiple connectors collide when registered on the same agent. Renaming the callables at registration avoids the collision, but the generated `execute` guidance still tells the model to call `inspect_connector` and `read_skill_docs`, so it points at the wrong tools. Multi-connector agents use `agent_tool` with connector-specific function names, which weaves those names into the guidance via `inspect_tool=` and `docs_tool=`.

Locally, the inspect/docs round trip returns the full generated docs that the `execute` description would carry. To opt out of that flow:

```python
tools = build_connector_tools(stripe, framework="pydantic_ai", use_progressive_docs=False)
agent = Agent("openai:gpt-4o", tools=tools.as_list())  # exposes execute only
```

### Custom tool bodies and unsupported frameworks — `agent_tool`

When you need custom tool bodies, or when your framework is not one the SDK
natively supports, write the three functions yourself and decorate each with
`agent_tool`. The role is inferred from the signature — `(entity, action, ...)`
is execute, `(section, ...)` is docs, `()` is inspect — or pass it explicitly
(`agent_tool("execute")`). Extra parameters are allowed.

```python
import os

from airbyte_agent_sdk.connectors.stripe import StripeAuthConfig, StripeConnector
from pydantic_ai import Agent

stripe = StripeConnector(auth_config=StripeAuthConfig(api_key=os.environ["STRIPE_API_KEY"]))
agent = Agent("openai:gpt-4o")

@agent.tool_plain
@StripeConnector.agent_tool(
    framework="pydantic_ai",
    inspect_tool="stripe_inspect",
    docs_tool="stripe_read_docs",
)
async def stripe_execute(entity: str, action: str, params: dict | None = None):
    result = await stripe.execute(entity, action, params or {})
    return result.data if hasattr(result, "data") else result

@agent.tool_plain
@StripeConnector.agent_tool(framework="pydantic_ai")
async def stripe_inspect():
    return await stripe.inspect_connector()

@agent.tool_plain
@StripeConnector.agent_tool(framework="pydantic_ai")
async def stripe_read_docs(section: str | None = None):
    return await stripe.read_skill_docs(section)
```

The optional `inspect_tool=`/`docs_tool=` kwargs weave the exact registered
sibling-tool names into the execute docstring for tighter steering; omitting
them uses generic phrasing. Register the same three-function pattern with any
other framework and set `framework=` to match it.

`framework=` decides what a tool failure looks like to the agent. This applies
equally to `build_connector_tools`, `agent_tool`, and `translate_exceptions`:

| `framework=` | Tool failures surface as | Framework-side wiring |
|--------------|--------------------------|-----------------------|
| `"pydantic_ai"` | raises `pydantic_ai.ModelRetry` | none — the agent retries |
| `"langchain"` | raises `langchain_core.tools.ToolException` | pass `handle_tool_error=True` to the tool so the message goes back to the model instead of aborting the run |
| `"openai_agents"` | returns the failure message as the tool result | register with `function_tool(..., strict_mode=False)` for `params: dict` |
| `"mcp"` | raises `fastmcp.exceptions.ToolError` | FastMCP serializes it as an errored tool result |
| `"none"` | raises `airbyte_agent_sdk.AirbyteToolError` | catch it in your dispatch loop and hand the message to the model |

An explicit `framework=` whose package is not installed raises `RuntimeError` at
call time. `agent_tool` defaults to `"none"` and never auto-detects;
`build_connector_tools`, `tool_utils`, and `translate_exceptions` auto-detect
when `framework` is omitted and fall back to `"none"` with a warning if no
supported framework is installed.

On a framework the SDK does not support natively, omit `framework=` and handle
the failure yourself:

```python
from airbyte_agent_sdk import AirbyteToolError

# `handlers` maps each registered tool name to its decorated function;
# `tool_name`/`tool_args` come from the model's tool call.
handlers = {fn.__name__: fn for fn in (stripe_inspect, stripe_read_docs, stripe_execute)}

try:
    content = await handlers[tool_name](**tool_args)
except AirbyteToolError as err:
    content = str(err)  # return to the model as an errored tool result
```

### Legacy: `tool_utils`

Existing integrations can keep `tool_utils` without changing behavior:

```python
legacy_agent = Agent("openai:gpt-4o")

@legacy_agent.tool_plain
@StripeConnector.tool_utils
async def legacy_stripe_execute(entity: str, action: str, params: dict | None = None):
    result = await stripe.execute(entity, action, params or {})
    return result.data if hasattr(result, "data") else result
```

`tool_utils` embeds the full generated connector catalog in one tool description
and auto-detects the installed supported framework. It is deprecated and kept
only so existing integrations can migrate independently; new code uses
`build_connector_tools` or `agent_tool(framework="...")`.

The advanced kwargs `internal_retries`, `should_internal_retry`, and `exhausted_runtime_failure_message` are documented in the function docstrings.

## Search and Airbyte Cloud

Fast search across your data and context-layer queries aren't part of this SDK. They're available in Airbyte Cloud through the Airbyte MCP at `https://mcp.airbyte.com/mcp`; [sign up for Airbyte Cloud](https://cloud.airbyte.com/signup). Some connectors list `context_store_search` and `context_store_sql_query` actions, but the local executor rejects either with `NotImplementedError` before making an API call.

## How to install the skills

The repo ships skills that walk agents through setting up and using the connectors. Three install paths:

**skills.sh** (works for Claude Code, Codex, Cursor, OpenCode, and 40+ other agents):

```bash
npx skills add airbytehq/airbyte-agent-sdk
```

**Claude Code** (native plugin):

```
/plugin marketplace add airbytehq/airbyte-agent-sdk
/plugin install airbyte-agent-sdk@airbyte-agent-sdk
```

**Codex** (clone + symlink):

```bash
git clone https://github.com/airbytehq/airbyte-agent-sdk ~/.codex/skills/airbyte-agent-sdk-src
ln -s ~/.codex/skills/airbyte-agent-sdk-src/connector-sdk/.claude/skills/* ~/.codex/skills/
```
