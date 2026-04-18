<!-- AUTO-GENERATED from connectors/greenhouse/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-04-09 -->

# Greenhouse

The Greenhouse agent connector is a Python package that equips AI agents to interact with Greenhouse through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-greenhouse` v0.17.125
- **Auth:** Token
- **Docs:** [Official API docs](https://developers.greenhouse.io/harvest.html)
- **Status:** complete

## Example Prompts

- List all open jobs
- Show me upcoming interviews this week
- Show me recent job offers
- List recent applications
- Show me candidates from \{company\} who applied last month
- What are the top 5 sources for our job applications this quarter?
- Analyze the interview schedules for our engineering candidates this week
- Compare the number of applications across different offices
- Identify candidates who have multiple applications in our system
- Summarize the candidate pipeline for our latest job posting
- Find the most active departments in recruiting this month

## Unsupported

- Create a new job posting for the marketing team
- Schedule an interview for \{candidate\}
- Update the status of \{candidate\}'s application
- Delete a candidate profile
- Send an offer letter to \{candidate\}
- Edit the details of a job description

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-greenhouse
```

### OSS Mode

```python
from airbyte_agent_greenhouse import GreenhouseConnector
from airbyte_agent_greenhouse.models import GreenhouseAuthConfig

connector = GreenhouseConnector(
    auth_config=GreenhouseAuthConfig(
        api_key="<Your Greenhouse Harvest API Key from the Dev Center>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GreenhouseConnector.tool_utils
async def greenhouse_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_greenhouse import GreenhouseConnector, AirbyteAuthConfig

connector = GreenhouseConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@GreenhouseConnector.tool_utils
async def greenhouse_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Candidates | List, Get, Context Store Search |
| Applications | List, Get, Context Store Search |
| Jobs | List, Get, Context Store Search |
| Offers | List, Get, Context Store Search |
| Users | List, Get, Context Store Search |
| Departments | List, Get, Context Store Search |
| Offices | List, Get, Context Store Search |
| Job Posts | List, Get, Context Store Search |
| Sources | List, Context Store Search |
| Scheduled Interviews | List, Get |
| Application Attachment | Download |
| Candidate Attachment | Download |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-sdk/blob/main/connectors/greenhouse/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-sdk/blob/main/connectors/greenhouse/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-sdk/tree/main/connectors/greenhouse)*
