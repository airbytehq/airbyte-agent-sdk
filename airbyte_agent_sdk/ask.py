"""ask() — one-call natural language query across all workspace connectors."""

from __future__ import annotations

import asyncio
import concurrent.futures

from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient
from airbyte_agent_sdk.config import resolve_credentials
from airbyte_agent_sdk.executor.models import AskResult

_UNSET = object()


async def ask(
    prompt: str,
    *,
    client_id: str | None = None,
    client_secret: str | None = None,
    workspace_name: str | object = _UNSET,
    organization_id: str | None = None,
) -> AskResult:
    """Ask a natural-language question across all connectors in a workspace.

    Simplest entry point — no Workspace or connect() needed.
    Reads AIRBYTE_CLIENT_ID/SECRET from env if not provided.
    """
    resolved_id, resolved_secret, resolved_org_id, resolved_ws = resolve_credentials(
        client_id=client_id,
        client_secret=client_secret,
        organization_id=organization_id,
        workspace_name=workspace_name if workspace_name is not _UNSET else None,
    )
    client = AirbyteCloudClient(client_id=resolved_id, client_secret=resolved_secret, organization_id=resolved_org_id)
    try:
        response = await client.ask_workspace(resolved_ws, prompt)
        return AskResult.from_response(response)
    finally:
        await client.close()


def ask_sync(
    prompt: str,
    *,
    client_id: str | None = None,
    client_secret: str | None = None,
    workspace_name: str | object = _UNSET,
    organization_id: str | None = None,
) -> AskResult:
    """Synchronous version of :func:`ask`. Works in scripts and notebooks.

    In a plain script (no running event loop) this uses ``asyncio.run()``.
    Inside a Jupyter notebook or other environment that already has a running
    loop, it dispatches the coroutine to a background thread so it does not
    block the existing loop.
    """
    coro = ask(
        prompt,
        client_id=client_id,
        client_secret=client_secret,
        workspace_name=workspace_name,
        organization_id=organization_id,
    )
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        return pool.submit(asyncio.run, coro).result()
