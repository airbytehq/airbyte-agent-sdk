"""
Pydantic models for reddit-ads connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""
# ruff: noqa: E501

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration

class RedditAdsAuthConfig(BaseModel):
    """Reddit OAuth2 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """The OAuth2 client ID from your Reddit developer application."""
    client_secret: str
    """The OAuth2 client secret from your Reddit developer application."""
    refresh_token: str
    """The OAuth2 refresh token obtained through the authorization code flow.
"""

# Replication configuration

class RedditAdsReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Reddit Ads."""

    model_config = ConfigDict(extra="forbid")

    ad_account_id: str
    """The Reddit Ads account ID to replicate data from."""
    start_time: Optional[str] = None
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ. Data will be replicated starting from this date. Defaults to 24 months ago.
"""
    user_agent: Optional[str] = None
    """A unique user agent string identifying the client. Recommended format: platform:app_id:version (by /u/username).
"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Pagination(BaseModel):
    """Pagination metadata for list responses"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_url: str | None = Field(default=None)
    previous_url: str | None = Field(default=None)

class Business(BaseModel):
    """A Reddit advertising business entity."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    country: str | None = Field(default=None)
    primary_contact_id: str | None = Field(default=None)
    creator_id: str | None = Field(default=None)
    industry: str | None = Field(default=None)
    website_url: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    agency_affiliated: bool | None = Field(default=None)
    two_fa_enforcement: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    modified_at: str | None = Field(default=None)

class AdAccount(BaseModel):
    """A Reddit ad account with billing, attribution, and configuration settings."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    business_id: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    currency: str | None = Field(default=None)
    time_zone_id: str | None = Field(default=None)
    admin_approval: str | None = Field(default=None)
    attribution_type: str | None = Field(default=None)
    click_attribution_window: str | None = Field(default=None)
    view_attribution_window: str | None = Field(default=None)
    app_attribution_type: str | None = Field(default=None)
    app_click_attribution_window: str | None = Field(default=None)
    app_view_attribution_window: str | None = Field(default=None)
    primary_contact_member_id: str | None = Field(default=None)
    suspension_reason: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    modified_at: str | None = Field(default=None)
    excluded_communities: list[str] | None = Field(default=None)
    excluded_keywords: list[str] | None = Field(default=None)
    pixel_partner_preferences: list[str] | None = Field(default=None)

class Campaign(BaseModel):
    """A Reddit advertising campaign with objective, budget, and scheduling settings."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    ad_account_id: str | None = Field(default=None)
    objective: str | None = Field(default=None)
    configured_status: str | None = Field(default=None)
    effective_status: str | None = Field(default=None)
    delivery_status: list[str] | None = Field(default=None)
    funding_instrument_id: str | None = Field(default=None)
    goal_type: str | None = Field(default=None)
    goal_value: int | None = Field(default=None)
    is_campaign_budget_optimization: bool | None = Field(default=None)
    spend_cap: int | None = Field(default=None)
    start_time: str | None = Field(default=None)
    end_time: str | None = Field(default=None)
    optimization_goal: str | None = Field(default=None)
    bid_strategy: str | None = Field(default=None)
    bid_type: str | None = Field(default=None)
    bid_value: int | None = Field(default=None)
    app_id: str | None = Field(default=None)
    view_through_conversion_type: str | None = Field(default=None)
    special_ad_categories: list[str] | None = Field(default=None)
    schedule: list[Any] | None = Field(default=None)
    skadnetwork_metadata: dict[str, Any] | None = Field(default=None)
    age_restriction: str | None = Field(default=None)
    invoice_label: str | None = Field(default=None)
    conversion_pixel_id: str | None = Field(default=None)
    is_max: bool | None = Field(default=None)
    use_catalog: bool | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    created_at: str | None = Field(default=None)
    modified_at: str | None = Field(default=None)

class AdGroupTargetingDevicesItem(BaseModel):
    """Nested schema for AdGroupTargeting.devices_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Device type (DESKTOP, MOBILE)")
    """Device type (DESKTOP, MOBILE)"""
    os: str | None | None = Field(default=None, description="Device OS (ANDROID, IOS)")
    """Device OS (ANDROID, IOS)"""
    min_version: str | None | None = Field(default=None, description="Minimum major OS version")
    """Minimum major OS version"""
    max_version: str | None | None = Field(default=None, description="Maximum major OS version")
    """Maximum major OS version"""
    label_map: dict[str, Any] | None | None = Field(default=None, description="Device models to target, keyed by make")
    """Device models to target, keyed by make"""

class AdGroupTargeting(BaseModel):
    """Targeting configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    communities: list[str] | None = Field(default=None, description="Targeted community subreddit names")
    """Targeted community subreddit names"""
    custom_audience_ids: list[str] | None = Field(default=None, description="Custom audience IDs to target")
    """Custom audience IDs to target"""
    excluded_communities: list[str] | None = Field(default=None, description="Excluded community subreddit names")
    """Excluded community subreddit names"""
    excluded_custom_audience_ids: list[str] | None = Field(default=None, description="Excluded custom audience IDs")
    """Excluded custom audience IDs"""
    excluded_geolocations: list[dict[str, Any]] | None = Field(default=None, description="Excluded geographic locations")
    """Excluded geographic locations"""
    excluded_keywords: list[str] | None = Field(default=None, description="Excluded keywords for targeting")
    """Excluded keywords for targeting"""
    expand_targeting: bool | None = Field(default=None, description="Whether to expand targeting beyond specified criteria")
    """Whether to expand targeting beyond specified criteria"""
    geolocations: list[dict[str, Any]] | None = Field(default=None, description="Targeted geographic locations")
    """Targeted geographic locations"""
    interests: list[str] | None = Field(default=None, description="Interest category IDs for targeting")
    """Interest category IDs for targeting"""
    devices: list[AdGroupTargetingDevicesItem] | None = Field(default=None, description="Targeted devices (type/OS/version constraints)")
    """Targeted devices (type/OS/version constraints)"""
    locations: list[str] | None = Field(default=None, description="Ad placement locations (e.g. FEED, COMMENTS_PAGE)")
    """Ad placement locations (e.g. FEED, COMMENTS_PAGE)"""
    platforms: list[str] | None = Field(default=None, description="Targeted platforms (e.g. ALL, IOS, ANDROID)")
    """Targeted platforms (e.g. ALL, IOS, ANDROID)"""
    view_modes: list[str] | None = Field(default=None, description="View mode targeting (e.g. ALL)")
    """View mode targeting (e.g. ALL)"""
    suppression_event_types: list[str] | None = Field(default=None, description="Event types to suppress for retargeting")
    """Event types to suppress for retargeting"""
    gender: str | None | None = Field(default=None, description="Gender targeting filter")
    """Gender targeting filter"""
    carriers: list[str] | None = Field(default=None, description="Mobile carrier targeting")
    """Mobile carrier targeting"""
    keywords: list[str] | None = Field(default=None, description="Keyword targeting terms")
    """Keyword targeting terms"""
    age_targeting: dict[str, Any] | None = Field(default=None, description="Age range targeting configuration")
    """Age range targeting configuration"""
    languages: list[str] | None | None = Field(default=None, description="Language targeting codes")
    """Language targeting codes"""

class AdGroup(BaseModel):
    """A Reddit ad group with targeting, bidding, and scheduling settings."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    ad_account_id: str | None = Field(default=None)
    campaign_id: str | None = Field(default=None)
    configured_status: str | None = Field(default=None)
    effective_status: str | None = Field(default=None)
    delivery_status: list[str] | None = Field(default=None)
    bid_strategy: str | None = Field(default=None)
    bid_type: str | None = Field(default=None)
    bid_value: int | None = Field(default=None)
    optimization_goal: str | None = Field(default=None)
    campaign_objective_type: str | None = Field(default=None)
    goal_type: str | None = Field(default=None)
    goal_value: int | None = Field(default=None)
    is_campaign_budget_optimization: bool | None = Field(default=None)
    start_time: str | None = Field(default=None)
    end_time: str | None = Field(default=None)
    targeting: AdGroupTargeting | None = Field(default=None)
    view_through_conversion_type: str | None = Field(default=None)
    conversion_pixel_id: str | None = Field(default=None)
    app_id: str | None = Field(default=None)
    optimization_strategy_type: str | None = Field(default=None)
    product_set_id: str | None = Field(default=None)
    saved_audience_id: str | None = Field(default=None)
    schedule: list[Any] | None = Field(default=None)
    skadnetwork_metadata: dict[str, Any] | None = Field(default=None)
    shopping_type: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    modified_at: str | None = Field(default=None)

class AdClickUrlQueryParametersItem(BaseModel):
    """Nested schema for Ad.click_url_query_parameters_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    value: str | None = Field(default=None)

class AdEventTrackersItem(BaseModel):
    """Nested schema for Ad.event_trackers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Ad(BaseModel):
    """A Reddit ad with creative configuration, status, and tracking settings."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    ad_account_id: str | None = Field(default=None)
    ad_group_id: str | None = Field(default=None)
    campaign_id: str | None = Field(default=None)
    campaign_objective_type: str | None = Field(default=None)
    click_url: str | None = Field(default=None)
    click_url_query_parameters: list[AdClickUrlQueryParametersItem] | None = Field(default=None)
    configured_status: str | None = Field(default=None)
    effective_status: str | None = Field(default=None)
    delivery_status: list[str] | None = Field(default=None)
    event_trackers: list[AdEventTrackersItem] | None = Field(default=None)
    post_id: str | None = Field(default=None)
    post_url: str | None = Field(default=None)
    preview_url: str | None = Field(default=None)
    preview_expiry: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    profile_id: str | None = Field(default=None)
    products: list[Any] | None = Field(default=None)
    shopping_creative: dict[str, Any] | None = Field(default=None)
    skadnetwork_metadata: dict[str, Any] | None = Field(default=None)
    extensions: dict[str, Any] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    modified_at: str | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class BusinessesListResultMeta(BaseModel):
    """Metadata for businesses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class AdAccountsListResultMeta(BaseModel):
    """Metadata for ad_accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class AdGroupsListResultMeta(BaseModel):
    """Metadata for ad_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class AdsListResultMeta(BaseModel):
    """Metadata for ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class RedditAdsCheckResult(BaseModel):
    """Result of a health check operation.

    Returned by the check() method to indicate connectivity and credential status.
    """
    model_config = ConfigDict(extra="forbid")

    status: str
    """Health check status: 'healthy' or 'unhealthy'."""
    error: str | None = None
    """Error message if status is 'unhealthy', None otherwise."""
    checked_entity: str | None = None
    """Entity name used for the health check."""
    checked_action: str | None = None
    """Action name used for the health check."""


# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class RedditAdsExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class RedditAdsExecuteResultWithMeta(RedditAdsExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """The ad account this campaign belongs to"""
    app_id: str | None = None
    """App Store or Play Store ID"""
    configured_status: str | None = None
    """User-configured status (ACTIVE, ARCHIVED, DELETED, PAUSED)"""
    created_at: str | None = None
    """Creation timestamp in ISO 8601 format"""
    effective_status: str | None = None
    """Effective delivery status"""
    funding_instrument_id: str | None = None
    """Funding instrument ID"""
    goal_type: str | None = None
    """Goal type (LIFETIME_SPEND, DAILY_SPEND)"""
    goal_value: int | None = None
    """Goal value in microcurrency"""
    id: str | None = None
    """Unique campaign identifier"""
    is_campaign_budget_optimization: bool | None = None
    """Whether campaign budget optimization is enabled"""
    modified_at: str | None = None
    """Last modification timestamp"""
    name: str | None = None
    """Campaign name"""
    objective: str | None = None
    """Campaign objective"""
    spend_cap: int | None = None
    """Spend cap in microcurrency"""


class AdsSearchData(BaseModel):
    """Search result data for ads entity."""
    model_config = ConfigDict(extra="allow")

    ad_account_id: str | None = None
    """The ad account this ad belongs to"""
    ad_group_id: str | None = None
    """The ad group this ad belongs to"""
    campaign_id: str | None = None
    """The campaign this ad belongs to"""
    click_url: str | None = None
    """Click destination URL"""
    configured_status: str | None = None
    """User-configured status"""
    created_at: str | None = None
    """Creation timestamp"""
    effective_status: str | None = None
    """Effective delivery status"""
    id: str | None = None
    """Unique ad identifier"""
    modified_at: str | None = None
    """Last modification timestamp"""
    name: str | None = None
    """Ad name"""
    post_id: str | None = None
    """Reddit post ID (t3_ prefix)"""
    post_url: str | None = None
    """Reddit post URL"""
    preview_url: str | None = None
    """Ad preview URL"""
    rejection_reason: str | None = None
    """Reason the ad was rejected"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchMeta(BaseModel):
    """Pagination metadata for search responses."""
    model_config = ConfigDict(extra="allow")

    has_more: bool = False
    """Whether more results are available."""
    cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed records."""
    model_config = ConfigDict(extra="allow")

    data: list[D] = Field(default_factory=list)
    """List of matching records."""
    meta: AirbyteSearchMeta = Field(default_factory=AirbyteSearchMeta)
    """Pagination metadata."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

AdsSearchResult = AirbyteSearchResult[AdsSearchData]
"""Search result type for ads entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

BusinessesListResult = RedditAdsExecuteResultWithMeta[list[Business], BusinessesListResultMeta]
"""Result type for businesses.list operation with data and metadata."""

AdAccountsListResult = RedditAdsExecuteResultWithMeta[list[AdAccount], AdAccountsListResultMeta]
"""Result type for ad_accounts.list operation with data and metadata."""

CampaignsListResult = RedditAdsExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

AdGroupsListResult = RedditAdsExecuteResultWithMeta[list[AdGroup], AdGroupsListResultMeta]
"""Result type for ad_groups.list operation with data and metadata."""

AdsListResult = RedditAdsExecuteResultWithMeta[list[Ad], AdsListResultMeta]
"""Result type for ads.list operation with data and metadata."""

