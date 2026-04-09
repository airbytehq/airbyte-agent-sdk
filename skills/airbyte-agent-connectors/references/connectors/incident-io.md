<!-- AUTO-GENERATED from connectors/incident-io/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-04-09 -->

# incident.io

The Incident-Io agent connector is a Python package that equips AI agents to interact with Incident-Io through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-incident-io` v0.1.20
- **Auth:** Token
- **Docs:** [Official API docs](https://api-docs.incident.io/)
- **Status:** complete

## Example Prompts

- List all incidents
- Show all open incidents
- List all alerts
- Show all users
- List all escalations
- Show all on-call schedules
- List all severities
- Show all incident statuses
- List all custom fields
- Which incidents were created this week?
- What are the most recent high-severity incidents?
- Who is currently on-call?
- How many incidents are in triage status?
- What incidents were updated today?

## Unsupported

- Create a new incident
- Update an incident's severity
- Delete an alert
- Assign someone to an incident role

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-incident-io
```

### OSS Mode

```python
from airbyte_agent_incident_io import IncidentIoConnector
from airbyte_agent_incident_io.models import IncidentIoAuthConfig

connector = IncidentIoConnector(
    auth_config=IncidentIoAuthConfig(
        api_key="<Your incident.io API key. Create one at https://app.incident.io/settings/api-keys>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@IncidentIoConnector.tool_utils
async def incident_io_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_incident_io import IncidentIoConnector, AirbyteAuthConfig

connector = IncidentIoConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@IncidentIoConnector.tool_utils
async def incident_io_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Incidents | List, Get, Context Store Search |
| Alerts | List, Get, Context Store Search |
| Escalations | List, Get, Context Store Search |
| Users | List, Get, Context Store Search |
| Incident Updates | List, Context Store Search |
| Incident Roles | List, Get, Context Store Search |
| Incident Statuses | List, Get, Context Store Search |
| Incident Timestamps | List, Get, Context Store Search |
| Severities | List, Get, Context Store Search |
| Custom Fields | List, Get, Context Store Search |
| Catalog Types | List, Get, Context Store Search |
| Schedules | List, Get, Context Store Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/incident-io/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/incident-io/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/incident-io)*
