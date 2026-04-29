"""Workspace — top-level entry point for hosted-mode workspace operations."""

from __future__ import annotations

import asyncio
from typing import Any

from airbyte_agent_sdk import registry
from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient
from airbyte_agent_sdk.config import resolve_credentials
from airbyte_agent_sdk.connector_model_loader import load_connector_model
from airbyte_agent_sdk.executor.hosted_executor import HostedExecutor
from airbyte_agent_sdk.executor.models import AutomationInfo, ConnectorInfo, WorkflowInfo

_AUTOMATION_FANOUT_CONCURRENCY = 10


def _automation_info_from_dict(data: dict[str, Any]) -> AutomationInfo:
    return AutomationInfo(
        id=str(data["id"]),
        workflow_id=str(data["workflow_id"]),
        workspace_id=str(data["workspace_id"]),
        enabled=data["enabled"],
        trigger_type=data["trigger_type"],
        cron_expression=data.get("cron_expression"),
        timezone=data.get("timezone", "UTC"),
        completion_webhook_url=data.get("completion_webhook_url"),
        trigger_webhook_url=data.get("trigger_webhook_url"),
        created_at=data.get("created_at"),
        updated_at=data.get("updated_at"),
    )


class Workspace:
    """Top-level entry point for Airbyte hosted-mode workspace operations.

    Provides workspace-level methods: list/create/delete connectors, get a
    connector executor, and workflow/automation CRUD. Use `Workspace` when
    you want to operate against a whole workspace (many connectors,
    workflows, automations); use [`connect()`](#connect) when you already
    know which connector you want to execute.

    Example:
        ```python
        import asyncio
        from airbyte_agent_sdk import Workspace

        async def main():
            async with Workspace(
                client_id="your_client_id",
                client_secret="your_client_secret",
                workspace_name="my-workspace",
            ) as ws:
                connectors = await ws.list_connectors()
                print(len(connectors))

        asyncio.run(main())
        ```

    Args:
        client_id: Airbyte OAuth client ID (or set `AIRBYTE_CLIENT_ID`).
        client_secret: Airbyte OAuth client secret (or set
            `AIRBYTE_CLIENT_SECRET`).
        workspace_name: Workspace name for scoping operations. Defaults to
            `"default"`.
        organization_id: Optional org ID for multi-org routing.

    Raises:
        ValueError: If `client_id`/`client_secret` are not supplied and no
            `AIRBYTE_CLIENT_ID`/`AIRBYTE_CLIENT_SECRET` env vars are set.
    """

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        workspace_name: str | None = None,
        organization_id: str | None = None,
    ):
        resolved_id, resolved_secret, resolved_org, resolved_ws = resolve_credentials(
            client_id=client_id,
            client_secret=client_secret,
            organization_id=organization_id,
            workspace_name=workspace_name,
        )
        self._workspace_name = resolved_ws
        self._organization_id = resolved_org
        self._client_id = resolved_id
        self._client_secret = resolved_secret
        self._workspace_id: str | None = None
        self._cloud_client = AirbyteCloudClient(
            client_id=resolved_id,
            client_secret=resolved_secret,
            organization_id=self._organization_id,
        )

    async def list_connectors(self) -> list[ConnectorInfo]:
        """List connector instances in this workspace."""
        data = await self._cloud_client.list_workspace_connectors(self._workspace_name)
        return [
            ConnectorInfo(
                id=str(c["id"]),
                name=c["name"],
                connector_type=(c.get("summarized_source_template") or {}).get("name"),
                created_at=c.get("created_at"),
                updated_at=c.get("updated_at"),
            )
            for c in data
        ]

    async def get_connector(
        self,
        *,
        connector_id: str | None = None,
        name: str | None = None,
    ) -> HostedExecutor:
        """Get a HostedExecutor for a specific connector.

        Provide exactly one of connector_id or name:
        - connector_id: Direct lookup, no API call needed.
        - name: Resolves connector slug (e.g. "stripe") to the single instance
          of that type in this workspace. Raises ValueError if 0 or >1 found.

        Creates an independent HostedExecutor with its own AirbyteCloudClient.
        The caller is responsible for closing the executor when done.

        Example:
            stripe = await ws.get_connector(name="stripe")
            try:
                result = await stripe.execute(...)
            finally:
                await stripe.close()
        """
        if connector_id and name:
            raise ValueError("Provide either connector_id or name, not both")
        if not connector_id and not name:
            raise ValueError("Provide either connector_id or name")

        if name:
            spec_path = registry.get_spec_path(name)
            model = load_connector_model(str(spec_path))
            definition_id = str(model.id)

            connector_id = await self._cloud_client.get_connector_id(
                workspace_name=self._workspace_name,
                connector_definition_id=definition_id,
            )

        return HostedExecutor(
            airbyte_client_id=self._client_id,
            airbyte_client_secret=self._client_secret,
            connector_id=connector_id,
            organization_id=self._organization_id,
        )

    async def create_connector(
        self,
        *,
        definition_id: str,
        credentials: dict[str, Any] | None = None,
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """Create a new connector, returns the connector ID."""
        source_name = name or f"connector-{self._workspace_name}"
        return await self._cloud_client.create_source(
            name=source_name,
            connector_definition_id=definition_id,
            workspace_name=self._workspace_name,
            credentials=credentials,
            replication_config=replication_config,
            source_template_id=source_template_id,
        )

    async def delete_connector(self, connector_id: str) -> None:
        """Delete a connector."""
        await self._cloud_client.delete_connector(connector_id)

    # ---- Workspace ID resolution (internal) ----------------------------------

    async def _resolve_workspace_id(self) -> str:
        """Resolve and cache the workspace UUID from the workspace name.

        Only caches on success — a failed resolution leaves the cache empty so
        subsequent calls will retry.
        """
        if self._workspace_id is not None:
            return self._workspace_id
        workspace_id = await self._cloud_client.resolve_workspace_id(self._workspace_name)
        self._workspace_id = workspace_id
        return workspace_id

    # ---- Workflow CRUD -------------------------------------------------------

    async def list_workflows(self) -> list[WorkflowInfo]:
        """List workflows in this workspace."""
        workspace_id = await self._resolve_workspace_id()
        data = await self._cloud_client.list_workflows(workspace_id)
        return [
            WorkflowInfo(
                id=str(w["id"]),
                name=w["name"],
                workspace_id=str(w["workspace_id"]),
                created_at=w.get("created_at"),
                updated_at=w.get("updated_at"),
            )
            for w in data
        ]

    async def create_workflow(
        self,
        name: str,
        *,
        tasks: list[dict[str, Any]] | None = None,
    ) -> WorkflowInfo:
        """Create a workflow in this workspace."""
        workspace_id = await self._resolve_workspace_id()
        data = await self._cloud_client.create_workflow(workspace_id, name, tasks=tasks)
        return WorkflowInfo(
            id=str(data["id"]),
            name=data["name"],
            workspace_id=str(data["workspace_id"]),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )

    async def get_workflow(self, workflow_id: str) -> WorkflowInfo:
        """Get a single workflow by ID."""
        workspace_id = await self._resolve_workspace_id()
        data = await self._cloud_client.get_workflow(workflow_id, workspace_id)
        return WorkflowInfo(
            id=str(data["id"]),
            name=data["name"],
            workspace_id=str(data["workspace_id"]),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )

    async def update_workflow(
        self,
        workflow_id: str,
        *,
        name: str | None = None,
    ) -> WorkflowInfo:
        """Update a workflow."""
        workspace_id = await self._resolve_workspace_id()
        data = await self._cloud_client.update_workflow(workflow_id, workspace_id, name=name)
        return WorkflowInfo(
            id=str(data["id"]),
            name=data["name"],
            workspace_id=str(data["workspace_id"]),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )

    async def delete_workflow(self, workflow_id: str) -> None:
        """Delete a workflow."""
        workspace_id = await self._resolve_workspace_id()
        await self._cloud_client.delete_workflow(workflow_id, workspace_id)

    # ---- Automation CRUD -----------------------------------------------------

    async def list_automations(
        self,
        workflow_id: str | None = None,
    ) -> list[AutomationInfo]:
        """List automations.

        When `workflow_id` is a non-`None` string, returns automations for that
        single workflow (workflow-scoped path, unchanged behavior).

        When `workflow_id` is omitted or passed explicitly as `None`, returns all
        automations across every workflow in the workspace via a bounded-concurrency
        fan-out over `list_workflows()`. Omission and explicit `None` are treated
        identically.

        Concurrent per-workflow HTTP requests are bounded by
        `_AUTOMATION_FANOUT_CONCURRENCY`. The first per-workflow error propagates
        to the caller immediately; sibling in-flight requests continue to
        completion in the background (their results are discarded). Workflows
        deleted mid-flight surface as an error rather than being silently
        filtered.

        Result ordering: automations are grouped per workflow in the order
        returned by `list_workflows()`; ordering within a workflow matches the
        backend response.
        """
        workspace_id = await self._resolve_workspace_id()

        if workflow_id is not None:
            data = await self._cloud_client.list_automations(workflow_id, workspace_id)
            return [_automation_info_from_dict(a) for a in data]

        workflows = await self._cloud_client.list_workflows(workspace_id)
        if not workflows:
            return []

        semaphore = asyncio.Semaphore(_AUTOMATION_FANOUT_CONCURRENCY)

        async def _fetch(wf_id: str) -> list[dict[str, Any]]:
            async with semaphore:
                return await self._cloud_client.list_automations(wf_id, workspace_id)

        results = await asyncio.gather(
            *(_fetch(str(w["id"])) for w in workflows),
        )
        return [_automation_info_from_dict(a) for group in results for a in group]

    async def create_automation(
        self,
        workflow_id: str,
        *,
        trigger_type: str = "schedule",
        enabled: bool = True,
        cron_expression: str | None = None,
        timezone: str | None = None,
        completion_webhook_url: str | None = None,
    ) -> AutomationInfo:
        """Create an automation on a workflow."""
        workspace_id = await self._resolve_workspace_id()
        data = await self._cloud_client.create_automation(
            workflow_id,
            workspace_id,
            trigger_type=trigger_type,
            enabled=enabled,
            cron_expression=cron_expression,
            timezone=timezone,
            completion_webhook_url=completion_webhook_url,
        )
        return AutomationInfo(
            id=str(data["id"]),
            workflow_id=str(data["workflow_id"]),
            workspace_id=str(data["workspace_id"]),
            enabled=data["enabled"],
            trigger_type=data["trigger_type"],
            cron_expression=data.get("cron_expression"),
            timezone=data.get("timezone", "UTC"),
            completion_webhook_url=data.get("completion_webhook_url"),
            trigger_webhook_url=data.get("trigger_webhook_url"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )

    async def get_automation(self, workflow_id: str, automation_id: str) -> AutomationInfo:
        """Get a single automation."""
        workspace_id = await self._resolve_workspace_id()
        data = await self._cloud_client.get_automation(workflow_id, automation_id, workspace_id)
        return AutomationInfo(
            id=str(data["id"]),
            workflow_id=str(data["workflow_id"]),
            workspace_id=str(data["workspace_id"]),
            enabled=data["enabled"],
            trigger_type=data["trigger_type"],
            cron_expression=data.get("cron_expression"),
            timezone=data.get("timezone", "UTC"),
            completion_webhook_url=data.get("completion_webhook_url"),
            trigger_webhook_url=data.get("trigger_webhook_url"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )

    async def update_automation(
        self,
        workflow_id: str,
        automation_id: str,
        *,
        enabled: bool | None = None,
        trigger_type: str | None = None,
        cron_expression: str | None = None,
        timezone: str | None = None,
        completion_webhook_url: str | None = None,
    ) -> AutomationInfo:
        """Update an automation."""
        workspace_id = await self._resolve_workspace_id()
        data = await self._cloud_client.update_automation(
            workflow_id,
            automation_id,
            workspace_id,
            enabled=enabled,
            trigger_type=trigger_type,
            cron_expression=cron_expression,
            timezone=timezone,
            completion_webhook_url=completion_webhook_url,
        )
        return AutomationInfo(
            id=str(data["id"]),
            workflow_id=str(data["workflow_id"]),
            workspace_id=str(data["workspace_id"]),
            enabled=data["enabled"],
            trigger_type=data["trigger_type"],
            cron_expression=data.get("cron_expression"),
            timezone=data.get("timezone", "UTC"),
            completion_webhook_url=data.get("completion_webhook_url"),
            trigger_webhook_url=data.get("trigger_webhook_url"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )

    async def delete_automation(self, workflow_id: str, automation_id: str) -> None:
        """Delete an automation."""
        workspace_id = await self._resolve_workspace_id()
        await self._cloud_client.delete_automation(workflow_id, automation_id, workspace_id)

    async def close(self):
        """Close the cloud client."""
        await self._cloud_client.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
