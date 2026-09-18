"""
Reddit-Ads connector.
"""
# ruff: noqa: E501

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import RedditAdsConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.tools import UNSET, AgentToolRole, SkillDocsAccessor, Unset, build_agent_tool_decorator
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    AdAccountsGetParams,
    AdAccountsListParams,
    AdGroupsGetParams,
    AdGroupsListParams,
    AdsGetParams,
    AdsListParams,
    BusinessesListParams,
    CampaignsGetParams,
    CampaignsListParams,
    AirbyteSearchParams,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    AdsSearchFilter,
    AdsSearchQuery,
)
from .models import RedditAdsAuthConfig
if TYPE_CHECKING:
    from .models import RedditAdsReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    RedditAdsCheckResult,
    RedditAdsExecuteResult,
    RedditAdsExecuteResultWithMeta,
    BusinessesListResult,
    AdAccountsListResult,
    CampaignsListResult,
    AdGroupsListResult,
    AdsListResult,
    Ad,
    AdAccount,
    AdGroup,
    Business,
    Campaign,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    AdsSearchData,
    AdsSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class RedditAdsConnector:
    """
    Type-safe Reddit-Ads API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "reddit-ads"
    connector_version = "1.0.0"
    sdk_version = "0.1.345"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("businesses", "list"): True,
        ("ad_accounts", "list"): True,
        ("ad_accounts", "get"): None,
        ("campaigns", "list"): True,
        ("campaigns", "get"): None,
        ("ad_groups", "list"): True,
        ("ad_groups", "get"): None,
        ("ads", "list"): True,
        ("ads", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('businesses', 'list'): {'page_size': 'page.size', 'page_token': 'page.token'},
        ('ad_accounts', 'list'): {'business_id': 'business_id', 'page_size': 'page.size', 'page_token': 'page.token'},
        ('ad_accounts', 'get'): {'ad_account_id': 'ad_account_id'},
        ('campaigns', 'list'): {'ad_account_id': 'ad_account_id', 'id': 'id', 'page_size': 'page.size', 'page_token': 'page.token'},
        ('campaigns', 'get'): {'campaign_id': 'campaign_id'},
        ('ad_groups', 'list'): {'ad_account_id': 'ad_account_id', 'campaign_id': 'campaign_id', 'page_size': 'page.size', 'page_token': 'page.token'},
        ('ad_groups', 'get'): {'ad_group_id': 'ad_group_id'},
        ('ads', 'list'): {'ad_account_id': 'ad_account_id', 'campaign_id': 'campaign_id', 'ad_group_id': 'ad_group_id', 'configured_status': 'configured_status', 'effective_status': 'effective_status', 'page_size': 'page.size', 'page_token': 'page.token'},
        ('ads', 'get'): {'ad_id': 'ad_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (RedditAdsAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: RedditAdsAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new reddit-ads connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., RedditAdsAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = RedditAdsConnector(auth_config=RedditAdsAuthConfig(client_id="...", client_secret="...", refresh_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = RedditAdsConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = RedditAdsConnector(
                auth_config=AirbyteAuthConfig(
                    workspace_name="user-123",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789"
                )
            )
        """
        # Accept AirbyteAuthConfig from any vendored SDK version
        if (
            auth_config is not None
            and not isinstance(auth_config, AirbyteAuthConfig)
            and type(auth_config).__name__ == AirbyteAuthConfig.__name__
        ):
            auth_config = AirbyteAuthConfig(**auth_config.model_dump())

        # Validate auth_config type
        if auth_config is not None and not isinstance(auth_config, self._ACCEPTED_AUTH_TYPES):
            raise TypeError(
                f"Unsupported auth_config type: {type(auth_config).__name__}. "
                f"Expected one of: {', '.join(t.__name__ for t in self._ACCEPTED_AUTH_TYPES)}"
            )

        # Hosted mode: auth_config is AirbyteAuthConfig
        is_hosted = isinstance(auth_config, AirbyteAuthConfig)

        if is_hosted:
            from airbyte_agent_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                workspace_name=auth_config.workspace_name or "default",
                organization_id=auth_config.organization_id,
                connector_definition_id=str(RedditAdsConnectorModel.id),
                model=RedditAdsConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or RedditAdsAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=RedditAdsConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.businesses = BusinessesQuery(self)
        self.ad_accounts = AdAccountsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.ad_groups = AdGroupsQuery(self)
        self.ads = AdsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["businesses"],
        action: Literal["list"],
        params: "BusinessesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BusinessesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_accounts"],
        action: Literal["list"],
        params: "AdAccountsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdAccountsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_accounts"],
        action: Literal["get"],
        params: "AdAccountsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdAccount": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Campaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_groups"],
        action: Literal["list"],
        params: "AdGroupsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_groups"],
        action: Literal["get"],
        params: "AdGroupsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdGroup": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads"],
        action: Literal["list"],
        params: "AdsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AdsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ads"],
        action: Literal["get"],
        params: "AdsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Ad": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "context_store_search", "context_store_sql_query"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> RedditAdsExecuteResult[Any] | RedditAdsExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "context_store_search", "context_store_sql_query"],
        params: Mapping[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True
    ) -> Any:
        """
        Execute an entity operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for entity/action/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "create", "get", "list")
            params: Operation parameters (typed based on entity+action)
            select_fields: Optional allowlist of dot-notation fields to include
            exclude_fields: Optional blocklist of dot-notation fields to remove
            skip_truncation: Disable long-text truncation for collection actions

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from airbyte_agent_sdk.executor import ExecutionConfig

        # Remap parameter names from snake_case (TypedDict keys) to API parameter names
        resolved_params = dict(params) if params is not None else None
        if resolved_params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                resolved_params = {param_map.get(k, k): v for k, v in resolved_params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=resolved_params,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return RedditAdsExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return RedditAdsExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> RedditAdsCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            RedditAdsCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return RedditAdsCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return RedditAdsCheckResult(
                status="unhealthy",
                error=result.error or "Unknown error during health check",
            )

    # ===== INTROSPECTION METHODS =====

    @classmethod
    def tool_utils(
        cls,
        func: _F | None = None,
        *,
        update_docstring: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
        framework: FrameworkName | None = None,
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> _F | Callable[[_F], _F]:
        """
        Deprecated. Add connector-specific documentation and runtime safeguards to one tool.

        Kept for backwards compatibility with existing single-tool
        integrations; it is not removed and does not warn at runtime, but new
        code should use `build_connector_tools` or `agent_tool` below.

        For new agents, prefer `build_connector_tools`. It returns progressive
        `inspect_connector`, `read_skill_docs`, and `execute` tools so the agent
        can load only the connector guidance it needs:

        ```python
        from airbyte_agent_sdk import build_connector_tools
        from pydantic_ai import Agent

        tools = build_connector_tools(connector, framework="pydantic_ai")
        agent = Agent("openai:gpt-4o", tools=tools.as_list())
        ```

        When a new integration needs custom tool bodies or a framework
        without native support, use `agent_tool` instead.

        ### Legacy: one generated-description tool

        Existing integrations can keep using `tool_utils` for one broad
        `execute` tool with the connector's full generated catalog in its
        description:

        ```python
        from fastmcp import FastMCP

        connector = RedditAdsConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @RedditAdsConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @RedditAdsConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @RedditAdsConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        This decorator composes `translate_exceptions` for runtime wrapping,
        output-size checks, framework signal translation, and optional internal
        retries, then adds connector-specific docstring augmentation.

        Args:
            update_docstring: When True, append connector capabilities to `__doc__`.
            max_output_chars: Max serialized output size before raising. Use `None` to disable.
            framework: One of `"pydantic_ai" | "langchain" | "openai_agents" | "mcp" | "none"`.
                Defaults to `None`, which auto-detects each framework's canonical
                import in order and falls back to `"none"` with a warning when no
                supported framework is installed. Explicit always wins, and an
                explicit framework whose package is missing raises `RuntimeError`.
            internal_retries: How many transient runtime failures (429/5xx, network,
                timeout) to retry silently before surfacing. Default 0. Forwarded to
                `airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate `(error, args, kwargs) -> bool`
                further restricting which retryable errors are safe for this specific
                tool. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback
                `(error, args, kwargs) -> str | None`. Invoked after internal retries
                are exhausted or were skipped because `should_internal_retry` returned
                `False`. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    RedditAdsConnectorModel,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            wrapped = translate_exceptions(
                inner,
                framework=framework,
                max_output_chars=max_output_chars,
                internal_retries=internal_retries,
                should_internal_retry=should_internal_retry,
                exhausted_runtime_failure_message=exhausted_runtime_failure_message,
            )

            if update_docstring:
                wrapped.__doc__ = full_doc
            return wrapped  # type: ignore[return-value]

        if func is not None:
            return decorate(func)
        return decorate

    @classmethod
    def agent_tool(
        cls,
        role: AgentToolRole | None = None,
        *,
        inspect_tool: str | None = None,
        docs_tool: str | None = None,
        max_output_chars: int | None | Unset = UNSET,
        framework: FrameworkName = "none",
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> Callable[[_F], _F]:
        """
        Decorator for new user-written connector tool functions.

        Use this when a tool needs a custom body or the framework lacks a
        native strategy. Instead of baking the full entity/action reference
        into the docstring, it instructs the agent to call this connector's
        inspect and docs tools before executing. Tool failures raise
        :class:`airbyte_agent_sdk.AirbyteToolError` by default
        (``framework="none"``, no auto-detection) — pass ``framework=...`` to
        translate to a supported framework's signal instead.

        Decorate three functions per connector — execute, inspect and docs.
        The role is inferred from each function's signature (extra parameters
        are allowed); a signature matching more than one role, a generic
        ``(*args, **kwargs)`` wrapper, or a callable whose signature cannot
        be read must pass the role explicitly:

        - ``(entity, action, ...)`` -> ``"execute"``
        - ``(section, ...)``        -> ``"read_skill_docs"``
        - ``()``                    -> ``"inspect_connector"``

        Usage:
            connector = RedditAdsConnector(...)

            @RedditAdsConnector.agent_tool()
            async def execute(entity: str, action: str, params: dict | None = None):
                return await connector.execute(entity=entity, action=action, params=params or {})

            @RedditAdsConnector.agent_tool()
            async def inspect_connector():
                return await connector.inspect_connector()

            @RedditAdsConnector.agent_tool()
            async def read_skill_docs(section: str | None = None):
                return await connector.read_skill_docs(section)

        Args:
            role: ``"execute" | "inspect_connector" | "read_skill_docs"``.
                None (default) infers the role from the decorated function's
                signature; an explicit role validates the canonical
                parameters are present (functions accepting ``**kwargs``, or
                callables whose signature cannot be read, pass validation).
            inspect_tool: Exact registered name of the sibling inspect tool,
                woven into the execute docstring for tighter steering.
                Defaults to generic phrasing.
            docs_tool: Exact registered name of the sibling docs tool (see
                inspect_tool).
            max_output_chars: Max serialized output size before failing.
                Defaults per role: execute -> DEFAULT_MAX_OUTPUT_CHARS, docs
                tools -> None.
            framework: Translation target for tool failures. Defaults to
                ``"none"`` (raise AirbyteToolError); never auto-detects.
            internal_retries: How many transient runtime failures (429/5xx,
                network, timeout) to retry silently before surfacing.
                Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate ``(error, args, kwargs)
                -> bool`` further restricting which retryable errors are safe
                for this specific tool. Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback ``(error,
                args, kwargs) -> str | None`` invoked after internal retries
                are exhausted or skipped. Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
        """
        return build_agent_tool_decorator(  # type: ignore[return-value]
            RedditAdsConnectorModel,
            role=role,
            inspect_tool=inspect_tool,
            docs_tool=docs_tool,
            max_output_chars=max_output_chars,
            framework=framework,
            internal_retries=internal_retries,
            should_internal_retry=should_internal_retry,
            exhausted_runtime_failure_message=exhausted_runtime_failure_message,
        )

    def _skill_docs(self) -> SkillDocsAccessor:
        accessor: SkillDocsAccessor | None = getattr(self, "_skill_docs_accessor", None)
        if accessor is None:
            accessor = SkillDocsAccessor(self)
            self._skill_docs_accessor = accessor
        return accessor

    async def inspect_connector(self) -> dict[str, Any]:
        """
        Inspect this connector's hosted metadata/readiness and resolve its docs skill id.

        Call this before read_skill_docs in the normal hosted flow. For
        local/offline connectors this returns a local-mode payload with a
        warning instead of a hosted inspection.

        Example:
            info = await connector.inspect_connector()
            print(info["docs_skill_id"])
        """
        return await self._skill_docs().inspect()

    async def read_skill_docs(self, section: str | None = None) -> str:
        """
        Read this connector's usage docs, rendered to text.

        Omit section for the outline and general guidance; pass an exact
        section id from the outline for full details. For local/offline
        connectors the full generated docs are returned and section is
        ignored.

        Example:
            outline = await connector.read_skill_docs()
            details = await connector.read_skill_docs(section="entity:contacts")
        """
        return await self._skill_docs().read(section)

    def list_entities(self) -> list[dict[str, Any]]:
        """
        Get structured data about available entities, actions, and parameters.

        Returns a list of entity descriptions with:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts

        Example:
            entities = connector.list_entities()
            for entity in entities:
                print(f"{entity['entity_name']}: {entity['available_actions']}")
        """
        return describe_entities(RedditAdsConnectorModel)

    def entity_schema(self, entity: str) -> dict[str, Any] | None:
        """
        Get the JSON schema for an entity.

        Args:
            entity: Entity name (e.g., "contacts", "companies")

        Returns:
            JSON schema dict describing the entity structure, or None if not found.

        Example:
            schema = connector.entity_schema("contacts")
            if schema:
                print(f"Contact properties: {list(schema.get('properties', {}).keys())}")
        """
        entity_def = next(
            (e for e in RedditAdsConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in RedditAdsConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== RESOURCE MANAGEMENT =====

    async def close(self):
        """Close the connector and release resources."""
        await self._executor.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()



class BusinessesQuery:
    """
    Query class for Businesses entity operations.
    """

    def __init__(self, connector: RedditAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> BusinessesListResult:
        """
        Retrieve all businesses associated with the authenticated user.

        Args:
            page_size: Number of items per page (max 1000)
            page_token: Pagination token for next page
            **kwargs: Additional parameters

        Returns:
            BusinessesListResult
        """
        params = {k: v for k, v in {
            "page.size": page_size,
            "page.token": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("businesses", "list", params)
        # Cast generic envelope to concrete typed result
        return BusinessesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class AdAccountsQuery:
    """
    Query class for AdAccounts entity operations.
    """

    def __init__(self, connector: RedditAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        business_id: str,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> AdAccountsListResult:
        """
        Retrieve the ad accounts in a business.

        Args:
            business_id: The business ID
            page_size: Number of items per page (max 1000)
            page_token: Pagination token for next page
            **kwargs: Additional parameters

        Returns:
            AdAccountsListResult
        """
        params = {k: v for k, v in {
            "business_id": business_id,
            "page.size": page_size,
            "page.token": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_accounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AdAccountsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        ad_account_id: str,
        **kwargs
    ) -> AdAccount:
        """
        Retrieve ad account by ID.

        Args:
            ad_account_id: The ad account ID
            **kwargs: Additional parameters

        Returns:
            AdAccount
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_accounts", "get", params)
        return result



class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: RedditAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        id: list[str] | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Retrieve campaigns by ad account.

        Args:
            ad_account_id: The ad account ID
            id: Filter by campaign IDs (comma-separated)
            page_size: Number of items per page (max 1000)
            page_token: Pagination token for next page
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "id": id,
            "page.size": page_size,
            "page.token": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        campaign_id: str,
        **kwargs
    ) -> Campaign:
        """
        Retrieve a campaign by ID.

        Args:
            campaign_id: The campaign ID
            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



    async def context_store_search(
        self,
        query: CampaignsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignsSearchResult:
        """
        Search campaigns records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignsSearchFilter):
        - ad_account_id: The ad account this campaign belongs to
        - app_id: App Store or Play Store ID
        - configured_status: User-configured status (ACTIVE, ARCHIVED, DELETED, PAUSED)
        - created_at: Creation timestamp in ISO 8601 format
        - effective_status: Effective delivery status
        - funding_instrument_id: Funding instrument ID
        - goal_type: Goal type (LIFETIME_SPEND, DAILY_SPEND)
        - goal_value: Goal value in microcurrency
        - id: Unique campaign identifier
        - is_campaign_budget_optimization: Whether campaign budget optimization is enabled
        - modified_at: Last modification timestamp
        - name: Campaign name
        - objective: Campaign objective
        - spend_cap: Spend cap in microcurrency

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("campaigns", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignsSearchResult(
            data=[
                CampaignsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against campaigns records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("campaigns", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdGroupsQuery:
    """
    Query class for AdGroups entity operations.
    """

    def __init__(self, connector: RedditAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        campaign_id: str | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> AdGroupsListResult:
        """
        Retrieve ad groups by ad account.

        Args:
            ad_account_id: The ad account ID
            campaign_id: Filter by campaign ID
            page_size: Number of items per page (max 1000)
            page_token: Pagination token for next page
            **kwargs: Additional parameters

        Returns:
            AdGroupsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "campaign_id": campaign_id,
            "page.size": page_size,
            "page.token": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return AdGroupsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        ad_group_id: str,
        **kwargs
    ) -> AdGroup:
        """
        Retrieve an ad group by ID.

        Args:
            ad_group_id: The ad group ID
            **kwargs: Additional parameters

        Returns:
            AdGroup
        """
        params = {k: v for k, v in {
            "ad_group_id": ad_group_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_groups", "get", params)
        return result



class AdsQuery:
    """
    Query class for Ads entity operations.
    """

    def __init__(self, connector: RedditAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        campaign_id: list[str] | None = None,
        ad_group_id: list[str] | None = None,
        configured_status: list[str] | None = None,
        effective_status: list[str] | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> AdsListResult:
        """
        Retrieve ads by ad account. Filters combine with logical AND across different query parameters.


        Args:
            ad_account_id: The ad account ID
            campaign_id: Filter by campaign IDs (comma-separated)
            ad_group_id: Filter by ad group IDs (comma-separated)
            configured_status: Filter by configured status
            effective_status: Filter by effective status
            page_size: Number of items per page (max 1000)
            page_token: Pagination token for next page
            **kwargs: Additional parameters

        Returns:
            AdsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "campaign_id": campaign_id,
            "ad_group_id": ad_group_id,
            "configured_status": configured_status,
            "effective_status": effective_status,
            "page.size": page_size,
            "page.token": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        ad_id: str,
        **kwargs
    ) -> Ad:
        """
        Retrieve an ad by ID.

        Args:
            ad_id: The ad ID
            **kwargs: Additional parameters

        Returns:
            Ad
        """
        params = {k: v for k, v in {
            "ad_id": ad_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads", "get", params)
        return result



    async def context_store_search(
        self,
        query: AdsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdsSearchResult:
        """
        Search ads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdsSearchFilter):
        - ad_account_id: The ad account this ad belongs to
        - ad_group_id: The ad group this ad belongs to
        - campaign_id: The campaign this ad belongs to
        - click_url: Click destination URL
        - configured_status: User-configured status
        - created_at: Creation timestamp
        - effective_status: Effective delivery status
        - id: Unique ad identifier
        - modified_at: Last modification timestamp
        - name: Ad name
        - post_id: Reddit post ID (t3_ prefix)
        - post_url: Reddit post URL
        - preview_url: Ad preview URL
        - rejection_reason: Reason the ad was rejected

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("ads", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdsSearchResult(
            data=[
                AdsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against ads records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("ads", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
