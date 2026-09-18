"""
Type definitions for reddit-ads connector.
"""
# ruff: noqa: E501
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class BusinessesListParams(TypedDict):
    """Parameters for businesses.list operation"""
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class AdAccountsListParams(TypedDict):
    """Parameters for ad_accounts.list operation"""
    business_id: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class AdAccountsGetParams(TypedDict):
    """Parameters for ad_accounts.get operation"""
    ad_account_id: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    ad_account_id: str
    id: NotRequired[list[str]]
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    campaign_id: str

class AdGroupsListParams(TypedDict):
    """Parameters for ad_groups.list operation"""
    ad_account_id: str
    campaign_id: NotRequired[str]
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class AdGroupsGetParams(TypedDict):
    """Parameters for ad_groups.get operation"""
    ad_group_id: str

class AdsListParams(TypedDict):
    """Parameters for ads.list operation"""
    ad_account_id: str
    campaign_id: NotRequired[list[str]]
    ad_group_id: NotRequired[list[str]]
    configured_status: NotRequired[list[str]]
    effective_status: NotRequired[list[str]]
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class AdsGetParams(TypedDict):
    """Parameters for ads.get operation"""
    ad_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    ad_account_id: str | None
    """The ad account this campaign belongs to"""
    app_id: str | None
    """App Store or Play Store ID"""
    configured_status: str | None
    """User-configured status (ACTIVE, ARCHIVED, DELETED, PAUSED)"""
    created_at: str | None
    """Creation timestamp in ISO 8601 format"""
    effective_status: str | None
    """Effective delivery status"""
    funding_instrument_id: str | None
    """Funding instrument ID"""
    goal_type: str | None
    """Goal type (LIFETIME_SPEND, DAILY_SPEND)"""
    goal_value: int | None
    """Goal value in microcurrency"""
    id: str | None
    """Unique campaign identifier"""
    is_campaign_budget_optimization: bool | None
    """Whether campaign budget optimization is enabled"""
    modified_at: str | None
    """Last modification timestamp"""
    name: str | None
    """Campaign name"""
    objective: str | None
    """Campaign objective"""
    spend_cap: int | None
    """Spend cap in microcurrency"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """The ad account this campaign belongs to"""
    app_id: list[str]
    """App Store or Play Store ID"""
    configured_status: list[str]
    """User-configured status (ACTIVE, ARCHIVED, DELETED, PAUSED)"""
    created_at: list[str]
    """Creation timestamp in ISO 8601 format"""
    effective_status: list[str]
    """Effective delivery status"""
    funding_instrument_id: list[str]
    """Funding instrument ID"""
    goal_type: list[str]
    """Goal type (LIFETIME_SPEND, DAILY_SPEND)"""
    goal_value: list[int]
    """Goal value in microcurrency"""
    id: list[str]
    """Unique campaign identifier"""
    is_campaign_budget_optimization: list[bool]
    """Whether campaign budget optimization is enabled"""
    modified_at: list[str]
    """Last modification timestamp"""
    name: list[str]
    """Campaign name"""
    objective: list[str]
    """Campaign objective"""
    spend_cap: list[int]
    """Spend cap in microcurrency"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """The ad account this campaign belongs to"""
    app_id: Any
    """App Store or Play Store ID"""
    configured_status: Any
    """User-configured status (ACTIVE, ARCHIVED, DELETED, PAUSED)"""
    created_at: Any
    """Creation timestamp in ISO 8601 format"""
    effective_status: Any
    """Effective delivery status"""
    funding_instrument_id: Any
    """Funding instrument ID"""
    goal_type: Any
    """Goal type (LIFETIME_SPEND, DAILY_SPEND)"""
    goal_value: Any
    """Goal value in microcurrency"""
    id: Any
    """Unique campaign identifier"""
    is_campaign_budget_optimization: Any
    """Whether campaign budget optimization is enabled"""
    modified_at: Any
    """Last modification timestamp"""
    name: Any
    """Campaign name"""
    objective: Any
    """Campaign objective"""
    spend_cap: Any
    """Spend cap in microcurrency"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    ad_account_id: str
    """The ad account this campaign belongs to"""
    app_id: str
    """App Store or Play Store ID"""
    configured_status: str
    """User-configured status (ACTIVE, ARCHIVED, DELETED, PAUSED)"""
    created_at: str
    """Creation timestamp in ISO 8601 format"""
    effective_status: str
    """Effective delivery status"""
    funding_instrument_id: str
    """Funding instrument ID"""
    goal_type: str
    """Goal type (LIFETIME_SPEND, DAILY_SPEND)"""
    goal_value: str
    """Goal value in microcurrency"""
    id: str
    """Unique campaign identifier"""
    is_campaign_budget_optimization: str
    """Whether campaign budget optimization is enabled"""
    modified_at: str
    """Last modification timestamp"""
    name: str
    """Campaign name"""
    objective: str
    """Campaign objective"""
    spend_cap: str
    """Spend cap in microcurrency"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    ad_account_id: AirbyteSortOrder
    """The ad account this campaign belongs to"""
    app_id: AirbyteSortOrder
    """App Store or Play Store ID"""
    configured_status: AirbyteSortOrder
    """User-configured status (ACTIVE, ARCHIVED, DELETED, PAUSED)"""
    created_at: AirbyteSortOrder
    """Creation timestamp in ISO 8601 format"""
    effective_status: AirbyteSortOrder
    """Effective delivery status"""
    funding_instrument_id: AirbyteSortOrder
    """Funding instrument ID"""
    goal_type: AirbyteSortOrder
    """Goal type (LIFETIME_SPEND, DAILY_SPEND)"""
    goal_value: AirbyteSortOrder
    """Goal value in microcurrency"""
    id: AirbyteSortOrder
    """Unique campaign identifier"""
    is_campaign_budget_optimization: AirbyteSortOrder
    """Whether campaign budget optimization is enabled"""
    modified_at: AirbyteSortOrder
    """Last modification timestamp"""
    name: AirbyteSortOrder
    """Campaign name"""
    objective: AirbyteSortOrder
    """Campaign objective"""
    spend_cap: AirbyteSortOrder
    """Spend cap in microcurrency"""


# Entity-specific condition types for campaigns
class CampaignsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CampaignsSearchFilter


class CampaignsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CampaignsSearchFilter


class CampaignsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CampaignsSearchFilter


class CampaignsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CampaignsSearchFilter


class CampaignsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CampaignsSearchFilter


class CampaignsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CampaignsSearchFilter


class CampaignsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CampaignsStringFilter


class CampaignsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CampaignsStringFilter


class CampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignsStringFilter


class CampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignsStringFilter


class CampaignsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: CampaignsAnyValueFilter


class CampaignsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: CampaignsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CampaignsInCondition = TypedDict("CampaignsInCondition", {"in": CampaignsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CampaignsNotCondition = TypedDict("CampaignsNotCondition", {"not": "CampaignsCondition"}, total=False)
"""Negates the nested condition."""

CampaignsAndCondition = TypedDict("CampaignsAndCondition", {"and": "list[CampaignsCondition]"}, total=False)
"""True if all nested conditions are true."""

CampaignsOrCondition = TypedDict("CampaignsOrCondition", {"or": "list[CampaignsCondition]"}, total=False)
"""True if any nested condition is true."""

CampaignsAnyCondition = TypedDict("CampaignsAnyCondition", {"any": CampaignsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all campaigns condition types
CampaignsCondition = (
    CampaignsEqCondition
    | CampaignsNeqCondition
    | CampaignsGtCondition
    | CampaignsGteCondition
    | CampaignsLtCondition
    | CampaignsLteCondition
    | CampaignsInCondition
    | CampaignsStartswithCondition
    | CampaignsEndswithCondition
    | CampaignsFuzzyCondition
    | CampaignsKeywordCondition
    | CampaignsContainsCondition
    | CampaignsArrayContainsCondition
    | CampaignsNotCondition
    | CampaignsAndCondition
    | CampaignsOrCondition
    | CampaignsAnyCondition
)


class CampaignsSearchQuery(TypedDict, total=False):
    """Search query for campaigns entity."""
    filter: CampaignsCondition
    sort: list[CampaignsSortFilter]


# ===== ADS SEARCH TYPES =====

class AdsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ads search queries."""
    ad_account_id: str | None
    """The ad account this ad belongs to"""
    ad_group_id: str | None
    """The ad group this ad belongs to"""
    campaign_id: str | None
    """The campaign this ad belongs to"""
    click_url: str | None
    """Click destination URL"""
    configured_status: str | None
    """User-configured status"""
    created_at: str | None
    """Creation timestamp"""
    effective_status: str | None
    """Effective delivery status"""
    id: str | None
    """Unique ad identifier"""
    modified_at: str | None
    """Last modification timestamp"""
    name: str | None
    """Ad name"""
    post_id: str | None
    """Reddit post ID (t3_ prefix)"""
    post_url: str | None
    """Reddit post URL"""
    preview_url: str | None
    """Ad preview URL"""
    rejection_reason: str | None
    """Reason the ad was rejected"""


class AdsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """The ad account this ad belongs to"""
    ad_group_id: list[str]
    """The ad group this ad belongs to"""
    campaign_id: list[str]
    """The campaign this ad belongs to"""
    click_url: list[str]
    """Click destination URL"""
    configured_status: list[str]
    """User-configured status"""
    created_at: list[str]
    """Creation timestamp"""
    effective_status: list[str]
    """Effective delivery status"""
    id: list[str]
    """Unique ad identifier"""
    modified_at: list[str]
    """Last modification timestamp"""
    name: list[str]
    """Ad name"""
    post_id: list[str]
    """Reddit post ID (t3_ prefix)"""
    post_url: list[str]
    """Reddit post URL"""
    preview_url: list[str]
    """Ad preview URL"""
    rejection_reason: list[str]
    """Reason the ad was rejected"""


class AdsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """The ad account this ad belongs to"""
    ad_group_id: Any
    """The ad group this ad belongs to"""
    campaign_id: Any
    """The campaign this ad belongs to"""
    click_url: Any
    """Click destination URL"""
    configured_status: Any
    """User-configured status"""
    created_at: Any
    """Creation timestamp"""
    effective_status: Any
    """Effective delivery status"""
    id: Any
    """Unique ad identifier"""
    modified_at: Any
    """Last modification timestamp"""
    name: Any
    """Ad name"""
    post_id: Any
    """Reddit post ID (t3_ prefix)"""
    post_url: Any
    """Reddit post URL"""
    preview_url: Any
    """Ad preview URL"""
    rejection_reason: Any
    """Reason the ad was rejected"""


class AdsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    ad_account_id: str
    """The ad account this ad belongs to"""
    ad_group_id: str
    """The ad group this ad belongs to"""
    campaign_id: str
    """The campaign this ad belongs to"""
    click_url: str
    """Click destination URL"""
    configured_status: str
    """User-configured status"""
    created_at: str
    """Creation timestamp"""
    effective_status: str
    """Effective delivery status"""
    id: str
    """Unique ad identifier"""
    modified_at: str
    """Last modification timestamp"""
    name: str
    """Ad name"""
    post_id: str
    """Reddit post ID (t3_ prefix)"""
    post_url: str
    """Reddit post URL"""
    preview_url: str
    """Ad preview URL"""
    rejection_reason: str
    """Reason the ad was rejected"""


class AdsSortFilter(TypedDict, total=False):
    """Available fields for sorting ads search results."""
    ad_account_id: AirbyteSortOrder
    """The ad account this ad belongs to"""
    ad_group_id: AirbyteSortOrder
    """The ad group this ad belongs to"""
    campaign_id: AirbyteSortOrder
    """The campaign this ad belongs to"""
    click_url: AirbyteSortOrder
    """Click destination URL"""
    configured_status: AirbyteSortOrder
    """User-configured status"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    effective_status: AirbyteSortOrder
    """Effective delivery status"""
    id: AirbyteSortOrder
    """Unique ad identifier"""
    modified_at: AirbyteSortOrder
    """Last modification timestamp"""
    name: AirbyteSortOrder
    """Ad name"""
    post_id: AirbyteSortOrder
    """Reddit post ID (t3_ prefix)"""
    post_url: AirbyteSortOrder
    """Reddit post URL"""
    preview_url: AirbyteSortOrder
    """Ad preview URL"""
    rejection_reason: AirbyteSortOrder
    """Reason the ad was rejected"""


# Entity-specific condition types for ads
class AdsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdsSearchFilter


class AdsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdsSearchFilter


class AdsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdsSearchFilter


class AdsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdsSearchFilter


class AdsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdsSearchFilter


class AdsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdsSearchFilter


class AdsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdsStringFilter


class AdsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdsStringFilter


class AdsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdsStringFilter


class AdsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdsStringFilter


class AdsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: AdsAnyValueFilter


class AdsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: AdsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdsInCondition = TypedDict("AdsInCondition", {"in": AdsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdsNotCondition = TypedDict("AdsNotCondition", {"not": "AdsCondition"}, total=False)
"""Negates the nested condition."""

AdsAndCondition = TypedDict("AdsAndCondition", {"and": "list[AdsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdsOrCondition = TypedDict("AdsOrCondition", {"or": "list[AdsCondition]"}, total=False)
"""True if any nested condition is true."""

AdsAnyCondition = TypedDict("AdsAnyCondition", {"any": AdsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ads condition types
AdsCondition = (
    AdsEqCondition
    | AdsNeqCondition
    | AdsGtCondition
    | AdsGteCondition
    | AdsLtCondition
    | AdsLteCondition
    | AdsInCondition
    | AdsStartswithCondition
    | AdsEndswithCondition
    | AdsFuzzyCondition
    | AdsKeywordCondition
    | AdsContainsCondition
    | AdsArrayContainsCondition
    | AdsNotCondition
    | AdsAndCondition
    | AdsOrCondition
    | AdsAnyCondition
)


class AdsSearchQuery(TypedDict, total=False):
    """Search query for ads entity."""
    filter: AdsCondition
    sort: list[AdsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
