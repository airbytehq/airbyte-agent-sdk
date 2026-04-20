# Airbyte Agent SDK

Type-safe connector execution framework with blessed connectors and full IDE autocomplete.

## Overview

The Airbyte Agent SDK gives AI agents access to 50+ third-party APIs through strongly typed, well-documented tools. Connectors can run through the Airbyte platform (which manages credentials, rate limiting, and execution) or locally in OSS mode.

## How to install

```bash
uv pip install airbyte-agent-sdk
```

## Documentation

Full documentation is available at [docs.airbyte.com/ai-agents/about/](https://docs.airbyte.com/ai-agents/about/).

## How to install the skills

The repo ships a Claude Code skill with agent instructions for setting up and using the connectors. Install it with:

```bash
npx skills add airbytehq/airbyte-agent-sdk
```

Or in Claude Code:

```
/install airbytehq/airbyte-agent-sdk
```

See [`.claude/skills/`](./.claude/skills/) for the skill source.
