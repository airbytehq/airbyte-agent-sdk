"""
Type definitions for amazon-ads connector.
"""
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

class SponsoredProductCampaignsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredProductCampaignsListParams.stateFilter"""
    include: NotRequired[str]

class SponsoredProductAdGroupsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredProductAdGroupsListParams.stateFilter"""
    include: NotRequired[str]

class SponsoredProductKeywordsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredProductKeywordsListParams.stateFilter"""
    include: NotRequired[str]

class SponsoredProductProductAdsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredProductProductAdsListParams.stateFilter"""
    include: NotRequired[str]

class SponsoredProductTargetsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredProductTargetsListParams.stateFilter"""
    include: NotRequired[str]

class SponsoredProductNegativeKeywordsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredProductNegativeKeywordsListParams.stateFilter"""
    include: NotRequired[str]

class SponsoredProductNegativeTargetsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredProductNegativeTargetsListParams.stateFilter"""
    include: NotRequired[str]

class SponsoredBrandsCampaignsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredBrandsCampaignsListParams.stateFilter"""
    include: NotRequired[str]

class SponsoredBrandsAdGroupsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredBrandsAdGroupsListParams.stateFilter"""
    include: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ProfilesListParams(TypedDict):
    """Parameters for profiles.list operation"""
    profile_type_filter: NotRequired[str]

class ProfilesGetParams(TypedDict):
    """Parameters for profiles.get operation"""
    profile_id: str

class PortfoliosListParams(TypedDict):
    """Parameters for portfolios.list operation"""
    include_extended_data_fields: NotRequired[str]

class PortfoliosGetParams(TypedDict):
    """Parameters for portfolios.get operation"""
    portfolio_id: str

class SponsoredProductCampaignsListParams(TypedDict):
    """Parameters for sponsored_product_campaigns.list operation"""
    state_filter: NotRequired[SponsoredProductCampaignsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredProductCampaignsGetParams(TypedDict):
    """Parameters for sponsored_product_campaigns.get operation"""
    campaign_id: str

class SponsoredProductAdGroupsListParams(TypedDict):
    """Parameters for sponsored_product_ad_groups.list operation"""
    state_filter: NotRequired[SponsoredProductAdGroupsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredProductKeywordsListParams(TypedDict):
    """Parameters for sponsored_product_keywords.list operation"""
    state_filter: NotRequired[SponsoredProductKeywordsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredProductProductAdsListParams(TypedDict):
    """Parameters for sponsored_product_product_ads.list operation"""
    state_filter: NotRequired[SponsoredProductProductAdsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredProductTargetsListParams(TypedDict):
    """Parameters for sponsored_product_targets.list operation"""
    state_filter: NotRequired[SponsoredProductTargetsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredProductNegativeKeywordsListParams(TypedDict):
    """Parameters for sponsored_product_negative_keywords.list operation"""
    state_filter: NotRequired[SponsoredProductNegativeKeywordsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredProductNegativeTargetsListParams(TypedDict):
    """Parameters for sponsored_product_negative_targets.list operation"""
    state_filter: NotRequired[SponsoredProductNegativeTargetsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredBrandsCampaignsListParams(TypedDict):
    """Parameters for sponsored_brands_campaigns.list operation"""
    state_filter: NotRequired[SponsoredBrandsCampaignsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredBrandsAdGroupsListParams(TypedDict):
    """Parameters for sponsored_brands_ad_groups.list operation"""
    state_filter: NotRequired[SponsoredBrandsAdGroupsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== PROFILES SEARCH TYPES =====

class ProfilesSearchFilter(TypedDict, total=False):
    """Available fields for filtering profiles search queries."""
    account_info: dict[str, Any] | None
    """"""
    country_code: str | None
    """"""
    currency_code: str | None
    """"""
    daily_budget: float | None
    """"""
    profile_id: int | None
    """"""
    timezone: str | None
    """"""


class ProfilesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_info: list[dict[str, Any]]
    """"""
    country_code: list[str]
    """"""
    currency_code: list[str]
    """"""
    daily_budget: list[float]
    """"""
    profile_id: list[int]
    """"""
    timezone: list[str]
    """"""


class ProfilesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_info: Any
    """"""
    country_code: Any
    """"""
    currency_code: Any
    """"""
    daily_budget: Any
    """"""
    profile_id: Any
    """"""
    timezone: Any
    """"""


class ProfilesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_info: str
    """"""
    country_code: str
    """"""
    currency_code: str
    """"""
    daily_budget: str
    """"""
    profile_id: str
    """"""
    timezone: str
    """"""


class ProfilesSortFilter(TypedDict, total=False):
    """Available fields for sorting profiles search results."""
    account_info: AirbyteSortOrder
    """"""
    country_code: AirbyteSortOrder
    """"""
    currency_code: AirbyteSortOrder
    """"""
    daily_budget: AirbyteSortOrder
    """"""
    profile_id: AirbyteSortOrder
    """"""
    timezone: AirbyteSortOrder
    """"""


# Entity-specific condition types for profiles
class ProfilesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProfilesSearchFilter


class ProfilesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProfilesSearchFilter


class ProfilesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProfilesSearchFilter


class ProfilesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProfilesSearchFilter


class ProfilesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProfilesSearchFilter


class ProfilesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProfilesSearchFilter


class ProfilesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProfilesStringFilter


class ProfilesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProfilesStringFilter


class ProfilesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProfilesStringFilter


class ProfilesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProfilesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProfilesInCondition = TypedDict("ProfilesInCondition", {"in": ProfilesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProfilesNotCondition = TypedDict("ProfilesNotCondition", {"not": "ProfilesCondition"}, total=False)
"""Negates the nested condition."""

ProfilesAndCondition = TypedDict("ProfilesAndCondition", {"and": "list[ProfilesCondition]"}, total=False)
"""True if all nested conditions are true."""

ProfilesOrCondition = TypedDict("ProfilesOrCondition", {"or": "list[ProfilesCondition]"}, total=False)
"""True if any nested condition is true."""

ProfilesAnyCondition = TypedDict("ProfilesAnyCondition", {"any": ProfilesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all profiles condition types
ProfilesCondition = (
    ProfilesEqCondition
    | ProfilesNeqCondition
    | ProfilesGtCondition
    | ProfilesGteCondition
    | ProfilesLtCondition
    | ProfilesLteCondition
    | ProfilesInCondition
    | ProfilesLikeCondition
    | ProfilesFuzzyCondition
    | ProfilesKeywordCondition
    | ProfilesContainsCondition
    | ProfilesNotCondition
    | ProfilesAndCondition
    | ProfilesOrCondition
    | ProfilesAnyCondition
)


class ProfilesSearchQuery(TypedDict, total=False):
    """Search query for profiles entity."""
    filter: ProfilesCondition
    sort: list[ProfilesSortFilter]


# ===== PORTFOLIOS SEARCH TYPES =====

class PortfoliosSearchFilter(TypedDict, total=False):
    """Available fields for filtering portfolios search queries."""
    portfolio_id: str | None
    """The unique identifier of the portfolio"""
    name: str | None
    """The name of the portfolio"""
    budget: dict[str, Any] | None
    """Budget configuration for the portfolio"""
    in_budget: bool | None
    """Whether the portfolio is within its budget"""
    state: str | None
    """The state of the portfolio (enabled, paused, archived)"""
    creation_date: int | None
    """The creation date of the portfolio (epoch milliseconds)"""
    last_updated_date: int | None
    """The last updated date of the portfolio (epoch milliseconds)"""
    serving_status: str | None
    """The serving status of the portfolio"""


class PortfoliosInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    portfolio_id: list[str]
    """The unique identifier of the portfolio"""
    name: list[str]
    """The name of the portfolio"""
    budget: list[dict[str, Any]]
    """Budget configuration for the portfolio"""
    in_budget: list[bool]
    """Whether the portfolio is within its budget"""
    state: list[str]
    """The state of the portfolio (enabled, paused, archived)"""
    creation_date: list[int]
    """The creation date of the portfolio (epoch milliseconds)"""
    last_updated_date: list[int]
    """The last updated date of the portfolio (epoch milliseconds)"""
    serving_status: list[str]
    """The serving status of the portfolio"""


class PortfoliosAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    portfolio_id: Any
    """The unique identifier of the portfolio"""
    name: Any
    """The name of the portfolio"""
    budget: Any
    """Budget configuration for the portfolio"""
    in_budget: Any
    """Whether the portfolio is within its budget"""
    state: Any
    """The state of the portfolio (enabled, paused, archived)"""
    creation_date: Any
    """The creation date of the portfolio (epoch milliseconds)"""
    last_updated_date: Any
    """The last updated date of the portfolio (epoch milliseconds)"""
    serving_status: Any
    """The serving status of the portfolio"""


class PortfoliosStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    portfolio_id: str
    """The unique identifier of the portfolio"""
    name: str
    """The name of the portfolio"""
    budget: str
    """Budget configuration for the portfolio"""
    in_budget: str
    """Whether the portfolio is within its budget"""
    state: str
    """The state of the portfolio (enabled, paused, archived)"""
    creation_date: str
    """The creation date of the portfolio (epoch milliseconds)"""
    last_updated_date: str
    """The last updated date of the portfolio (epoch milliseconds)"""
    serving_status: str
    """The serving status of the portfolio"""


class PortfoliosSortFilter(TypedDict, total=False):
    """Available fields for sorting portfolios search results."""
    portfolio_id: AirbyteSortOrder
    """The unique identifier of the portfolio"""
    name: AirbyteSortOrder
    """The name of the portfolio"""
    budget: AirbyteSortOrder
    """Budget configuration for the portfolio"""
    in_budget: AirbyteSortOrder
    """Whether the portfolio is within its budget"""
    state: AirbyteSortOrder
    """The state of the portfolio (enabled, paused, archived)"""
    creation_date: AirbyteSortOrder
    """The creation date of the portfolio (epoch milliseconds)"""
    last_updated_date: AirbyteSortOrder
    """The last updated date of the portfolio (epoch milliseconds)"""
    serving_status: AirbyteSortOrder
    """The serving status of the portfolio"""


# Entity-specific condition types for portfolios
class PortfoliosEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PortfoliosSearchFilter


class PortfoliosNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PortfoliosSearchFilter


class PortfoliosGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PortfoliosSearchFilter


class PortfoliosGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PortfoliosSearchFilter


class PortfoliosLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PortfoliosSearchFilter


class PortfoliosLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PortfoliosSearchFilter


class PortfoliosLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PortfoliosStringFilter


class PortfoliosFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PortfoliosStringFilter


class PortfoliosKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PortfoliosStringFilter


class PortfoliosContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PortfoliosAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PortfoliosInCondition = TypedDict("PortfoliosInCondition", {"in": PortfoliosInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PortfoliosNotCondition = TypedDict("PortfoliosNotCondition", {"not": "PortfoliosCondition"}, total=False)
"""Negates the nested condition."""

PortfoliosAndCondition = TypedDict("PortfoliosAndCondition", {"and": "list[PortfoliosCondition]"}, total=False)
"""True if all nested conditions are true."""

PortfoliosOrCondition = TypedDict("PortfoliosOrCondition", {"or": "list[PortfoliosCondition]"}, total=False)
"""True if any nested condition is true."""

PortfoliosAnyCondition = TypedDict("PortfoliosAnyCondition", {"any": PortfoliosAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all portfolios condition types
PortfoliosCondition = (
    PortfoliosEqCondition
    | PortfoliosNeqCondition
    | PortfoliosGtCondition
    | PortfoliosGteCondition
    | PortfoliosLtCondition
    | PortfoliosLteCondition
    | PortfoliosInCondition
    | PortfoliosLikeCondition
    | PortfoliosFuzzyCondition
    | PortfoliosKeywordCondition
    | PortfoliosContainsCondition
    | PortfoliosNotCondition
    | PortfoliosAndCondition
    | PortfoliosOrCondition
    | PortfoliosAnyCondition
)


class PortfoliosSearchQuery(TypedDict, total=False):
    """Search query for portfolios entity."""
    filter: PortfoliosCondition
    sort: list[PortfoliosSortFilter]


# ===== SPONSORED_PRODUCT_CAMPAIGNS SEARCH TYPES =====

class SponsoredProductCampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sponsored_product_campaigns search queries."""
    campaign_id: str | None
    """The unique identifier of the campaign"""
    portfolio_id: str | None
    """The portfolio ID this campaign belongs to"""
    name: str | None
    """The name of the campaign"""
    targeting_type: str | None
    """The targeting type (manual, auto)"""
    state: str | None
    """The state of the campaign (enabled, paused, archived)"""
    budget: dict[str, Any] | None
    """Budget configuration for the campaign"""
    start_date: str | None
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: str | None
    """The end date of the campaign (YYYYMMDD format)"""
    dynamic_bidding: dict[str, Any] | None
    """Dynamic bidding settings for the campaign"""


class SponsoredProductCampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    campaign_id: list[str]
    """The unique identifier of the campaign"""
    portfolio_id: list[str]
    """The portfolio ID this campaign belongs to"""
    name: list[str]
    """The name of the campaign"""
    targeting_type: list[str]
    """The targeting type (manual, auto)"""
    state: list[str]
    """The state of the campaign (enabled, paused, archived)"""
    budget: list[dict[str, Any]]
    """Budget configuration for the campaign"""
    start_date: list[str]
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: list[str]
    """The end date of the campaign (YYYYMMDD format)"""
    dynamic_bidding: list[dict[str, Any]]
    """Dynamic bidding settings for the campaign"""


class SponsoredProductCampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    campaign_id: Any
    """The unique identifier of the campaign"""
    portfolio_id: Any
    """The portfolio ID this campaign belongs to"""
    name: Any
    """The name of the campaign"""
    targeting_type: Any
    """The targeting type (manual, auto)"""
    state: Any
    """The state of the campaign (enabled, paused, archived)"""
    budget: Any
    """Budget configuration for the campaign"""
    start_date: Any
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: Any
    """The end date of the campaign (YYYYMMDD format)"""
    dynamic_bidding: Any
    """Dynamic bidding settings for the campaign"""


class SponsoredProductCampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    campaign_id: str
    """The unique identifier of the campaign"""
    portfolio_id: str
    """The portfolio ID this campaign belongs to"""
    name: str
    """The name of the campaign"""
    targeting_type: str
    """The targeting type (manual, auto)"""
    state: str
    """The state of the campaign (enabled, paused, archived)"""
    budget: str
    """Budget configuration for the campaign"""
    start_date: str
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: str
    """The end date of the campaign (YYYYMMDD format)"""
    dynamic_bidding: str
    """Dynamic bidding settings for the campaign"""


class SponsoredProductCampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting sponsored_product_campaigns search results."""
    campaign_id: AirbyteSortOrder
    """The unique identifier of the campaign"""
    portfolio_id: AirbyteSortOrder
    """The portfolio ID this campaign belongs to"""
    name: AirbyteSortOrder
    """The name of the campaign"""
    targeting_type: AirbyteSortOrder
    """The targeting type (manual, auto)"""
    state: AirbyteSortOrder
    """The state of the campaign (enabled, paused, archived)"""
    budget: AirbyteSortOrder
    """Budget configuration for the campaign"""
    start_date: AirbyteSortOrder
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: AirbyteSortOrder
    """The end date of the campaign (YYYYMMDD format)"""
    dynamic_bidding: AirbyteSortOrder
    """Dynamic bidding settings for the campaign"""


# Entity-specific condition types for sponsored_product_campaigns
class SponsoredProductCampaignsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SponsoredProductCampaignsSearchFilter


class SponsoredProductCampaignsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SponsoredProductCampaignsSearchFilter


class SponsoredProductCampaignsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SponsoredProductCampaignsSearchFilter


class SponsoredProductCampaignsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SponsoredProductCampaignsSearchFilter


class SponsoredProductCampaignsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SponsoredProductCampaignsSearchFilter


class SponsoredProductCampaignsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SponsoredProductCampaignsSearchFilter


class SponsoredProductCampaignsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SponsoredProductCampaignsStringFilter


class SponsoredProductCampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SponsoredProductCampaignsStringFilter


class SponsoredProductCampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SponsoredProductCampaignsStringFilter


class SponsoredProductCampaignsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SponsoredProductCampaignsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SponsoredProductCampaignsInCondition = TypedDict("SponsoredProductCampaignsInCondition", {"in": SponsoredProductCampaignsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SponsoredProductCampaignsNotCondition = TypedDict("SponsoredProductCampaignsNotCondition", {"not": "SponsoredProductCampaignsCondition"}, total=False)
"""Negates the nested condition."""

SponsoredProductCampaignsAndCondition = TypedDict("SponsoredProductCampaignsAndCondition", {"and": "list[SponsoredProductCampaignsCondition]"}, total=False)
"""True if all nested conditions are true."""

SponsoredProductCampaignsOrCondition = TypedDict("SponsoredProductCampaignsOrCondition", {"or": "list[SponsoredProductCampaignsCondition]"}, total=False)
"""True if any nested condition is true."""

SponsoredProductCampaignsAnyCondition = TypedDict("SponsoredProductCampaignsAnyCondition", {"any": SponsoredProductCampaignsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sponsored_product_campaigns condition types
SponsoredProductCampaignsCondition = (
    SponsoredProductCampaignsEqCondition
    | SponsoredProductCampaignsNeqCondition
    | SponsoredProductCampaignsGtCondition
    | SponsoredProductCampaignsGteCondition
    | SponsoredProductCampaignsLtCondition
    | SponsoredProductCampaignsLteCondition
    | SponsoredProductCampaignsInCondition
    | SponsoredProductCampaignsLikeCondition
    | SponsoredProductCampaignsFuzzyCondition
    | SponsoredProductCampaignsKeywordCondition
    | SponsoredProductCampaignsContainsCondition
    | SponsoredProductCampaignsNotCondition
    | SponsoredProductCampaignsAndCondition
    | SponsoredProductCampaignsOrCondition
    | SponsoredProductCampaignsAnyCondition
)


class SponsoredProductCampaignsSearchQuery(TypedDict, total=False):
    """Search query for sponsored_product_campaigns entity."""
    filter: SponsoredProductCampaignsCondition
    sort: list[SponsoredProductCampaignsSortFilter]


# ===== SPONSORED_PRODUCT_AD_GROUPS SEARCH TYPES =====

class SponsoredProductAdGroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sponsored_product_ad_groups search queries."""
    ad_group_id: str | None
    """The unique identifier of the ad group"""
    campaign_id: str | None
    """The campaign ID this ad group belongs to"""
    name: str | None
    """The name of the ad group"""
    state: str | None
    """The state of the ad group (enabled, paused, archived)"""
    default_bid: float | None
    """The default bid amount for the ad group"""


class SponsoredProductAdGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_group_id: list[str]
    """The unique identifier of the ad group"""
    campaign_id: list[str]
    """The campaign ID this ad group belongs to"""
    name: list[str]
    """The name of the ad group"""
    state: list[str]
    """The state of the ad group (enabled, paused, archived)"""
    default_bid: list[float]
    """The default bid amount for the ad group"""


class SponsoredProductAdGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_group_id: Any
    """The unique identifier of the ad group"""
    campaign_id: Any
    """The campaign ID this ad group belongs to"""
    name: Any
    """The name of the ad group"""
    state: Any
    """The state of the ad group (enabled, paused, archived)"""
    default_bid: Any
    """The default bid amount for the ad group"""


class SponsoredProductAdGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_group_id: str
    """The unique identifier of the ad group"""
    campaign_id: str
    """The campaign ID this ad group belongs to"""
    name: str
    """The name of the ad group"""
    state: str
    """The state of the ad group (enabled, paused, archived)"""
    default_bid: str
    """The default bid amount for the ad group"""


class SponsoredProductAdGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting sponsored_product_ad_groups search results."""
    ad_group_id: AirbyteSortOrder
    """The unique identifier of the ad group"""
    campaign_id: AirbyteSortOrder
    """The campaign ID this ad group belongs to"""
    name: AirbyteSortOrder
    """The name of the ad group"""
    state: AirbyteSortOrder
    """The state of the ad group (enabled, paused, archived)"""
    default_bid: AirbyteSortOrder
    """The default bid amount for the ad group"""


# Entity-specific condition types for sponsored_product_ad_groups
class SponsoredProductAdGroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SponsoredProductAdGroupsSearchFilter


class SponsoredProductAdGroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SponsoredProductAdGroupsSearchFilter


class SponsoredProductAdGroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SponsoredProductAdGroupsSearchFilter


class SponsoredProductAdGroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SponsoredProductAdGroupsSearchFilter


class SponsoredProductAdGroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SponsoredProductAdGroupsSearchFilter


class SponsoredProductAdGroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SponsoredProductAdGroupsSearchFilter


class SponsoredProductAdGroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SponsoredProductAdGroupsStringFilter


class SponsoredProductAdGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SponsoredProductAdGroupsStringFilter


class SponsoredProductAdGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SponsoredProductAdGroupsStringFilter


class SponsoredProductAdGroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SponsoredProductAdGroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SponsoredProductAdGroupsInCondition = TypedDict("SponsoredProductAdGroupsInCondition", {"in": SponsoredProductAdGroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SponsoredProductAdGroupsNotCondition = TypedDict("SponsoredProductAdGroupsNotCondition", {"not": "SponsoredProductAdGroupsCondition"}, total=False)
"""Negates the nested condition."""

SponsoredProductAdGroupsAndCondition = TypedDict("SponsoredProductAdGroupsAndCondition", {"and": "list[SponsoredProductAdGroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

SponsoredProductAdGroupsOrCondition = TypedDict("SponsoredProductAdGroupsOrCondition", {"or": "list[SponsoredProductAdGroupsCondition]"}, total=False)
"""True if any nested condition is true."""

SponsoredProductAdGroupsAnyCondition = TypedDict("SponsoredProductAdGroupsAnyCondition", {"any": SponsoredProductAdGroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sponsored_product_ad_groups condition types
SponsoredProductAdGroupsCondition = (
    SponsoredProductAdGroupsEqCondition
    | SponsoredProductAdGroupsNeqCondition
    | SponsoredProductAdGroupsGtCondition
    | SponsoredProductAdGroupsGteCondition
    | SponsoredProductAdGroupsLtCondition
    | SponsoredProductAdGroupsLteCondition
    | SponsoredProductAdGroupsInCondition
    | SponsoredProductAdGroupsLikeCondition
    | SponsoredProductAdGroupsFuzzyCondition
    | SponsoredProductAdGroupsKeywordCondition
    | SponsoredProductAdGroupsContainsCondition
    | SponsoredProductAdGroupsNotCondition
    | SponsoredProductAdGroupsAndCondition
    | SponsoredProductAdGroupsOrCondition
    | SponsoredProductAdGroupsAnyCondition
)


class SponsoredProductAdGroupsSearchQuery(TypedDict, total=False):
    """Search query for sponsored_product_ad_groups entity."""
    filter: SponsoredProductAdGroupsCondition
    sort: list[SponsoredProductAdGroupsSortFilter]


# ===== SPONSORED_PRODUCT_KEYWORDS SEARCH TYPES =====

class SponsoredProductKeywordsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sponsored_product_keywords search queries."""
    keyword_id: str | None
    """The unique identifier of the keyword"""
    campaign_id: str | None
    """The campaign ID this keyword belongs to"""
    ad_group_id: str | None
    """The ad group ID this keyword belongs to"""
    keyword_text: str | None
    """The keyword text"""
    state: str | None
    """The state of the keyword (enabled, paused, archived)"""


class SponsoredProductKeywordsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    keyword_id: list[str]
    """The unique identifier of the keyword"""
    campaign_id: list[str]
    """The campaign ID this keyword belongs to"""
    ad_group_id: list[str]
    """The ad group ID this keyword belongs to"""
    keyword_text: list[str]
    """The keyword text"""
    state: list[str]
    """The state of the keyword (enabled, paused, archived)"""


class SponsoredProductKeywordsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    keyword_id: Any
    """The unique identifier of the keyword"""
    campaign_id: Any
    """The campaign ID this keyword belongs to"""
    ad_group_id: Any
    """The ad group ID this keyword belongs to"""
    keyword_text: Any
    """The keyword text"""
    state: Any
    """The state of the keyword (enabled, paused, archived)"""


class SponsoredProductKeywordsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    keyword_id: str
    """The unique identifier of the keyword"""
    campaign_id: str
    """The campaign ID this keyword belongs to"""
    ad_group_id: str
    """The ad group ID this keyword belongs to"""
    keyword_text: str
    """The keyword text"""
    state: str
    """The state of the keyword (enabled, paused, archived)"""


class SponsoredProductKeywordsSortFilter(TypedDict, total=False):
    """Available fields for sorting sponsored_product_keywords search results."""
    keyword_id: AirbyteSortOrder
    """The unique identifier of the keyword"""
    campaign_id: AirbyteSortOrder
    """The campaign ID this keyword belongs to"""
    ad_group_id: AirbyteSortOrder
    """The ad group ID this keyword belongs to"""
    keyword_text: AirbyteSortOrder
    """The keyword text"""
    state: AirbyteSortOrder
    """The state of the keyword (enabled, paused, archived)"""


# Entity-specific condition types for sponsored_product_keywords
class SponsoredProductKeywordsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SponsoredProductKeywordsSearchFilter


class SponsoredProductKeywordsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SponsoredProductKeywordsSearchFilter


class SponsoredProductKeywordsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SponsoredProductKeywordsSearchFilter


class SponsoredProductKeywordsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SponsoredProductKeywordsSearchFilter


class SponsoredProductKeywordsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SponsoredProductKeywordsSearchFilter


class SponsoredProductKeywordsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SponsoredProductKeywordsSearchFilter


class SponsoredProductKeywordsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SponsoredProductKeywordsStringFilter


class SponsoredProductKeywordsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SponsoredProductKeywordsStringFilter


class SponsoredProductKeywordsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SponsoredProductKeywordsStringFilter


class SponsoredProductKeywordsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SponsoredProductKeywordsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SponsoredProductKeywordsInCondition = TypedDict("SponsoredProductKeywordsInCondition", {"in": SponsoredProductKeywordsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SponsoredProductKeywordsNotCondition = TypedDict("SponsoredProductKeywordsNotCondition", {"not": "SponsoredProductKeywordsCondition"}, total=False)
"""Negates the nested condition."""

SponsoredProductKeywordsAndCondition = TypedDict("SponsoredProductKeywordsAndCondition", {"and": "list[SponsoredProductKeywordsCondition]"}, total=False)
"""True if all nested conditions are true."""

SponsoredProductKeywordsOrCondition = TypedDict("SponsoredProductKeywordsOrCondition", {"or": "list[SponsoredProductKeywordsCondition]"}, total=False)
"""True if any nested condition is true."""

SponsoredProductKeywordsAnyCondition = TypedDict("SponsoredProductKeywordsAnyCondition", {"any": SponsoredProductKeywordsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sponsored_product_keywords condition types
SponsoredProductKeywordsCondition = (
    SponsoredProductKeywordsEqCondition
    | SponsoredProductKeywordsNeqCondition
    | SponsoredProductKeywordsGtCondition
    | SponsoredProductKeywordsGteCondition
    | SponsoredProductKeywordsLtCondition
    | SponsoredProductKeywordsLteCondition
    | SponsoredProductKeywordsInCondition
    | SponsoredProductKeywordsLikeCondition
    | SponsoredProductKeywordsFuzzyCondition
    | SponsoredProductKeywordsKeywordCondition
    | SponsoredProductKeywordsContainsCondition
    | SponsoredProductKeywordsNotCondition
    | SponsoredProductKeywordsAndCondition
    | SponsoredProductKeywordsOrCondition
    | SponsoredProductKeywordsAnyCondition
)


class SponsoredProductKeywordsSearchQuery(TypedDict, total=False):
    """Search query for sponsored_product_keywords entity."""
    filter: SponsoredProductKeywordsCondition
    sort: list[SponsoredProductKeywordsSortFilter]


# ===== SPONSORED_PRODUCT_PRODUCT_ADS SEARCH TYPES =====

class SponsoredProductProductAdsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sponsored_product_product_ads search queries."""
    ad_id: str | None
    """The unique identifier of the product ad"""
    campaign_id: str | None
    """The campaign ID this product ad belongs to"""
    ad_group_id: str | None
    """The ad group ID this product ad belongs to"""
    asin: str | None
    """The ASIN of the advertised product"""
    sku: str | None
    """The SKU of the advertised product (seller accounts only)"""
    state: str | None
    """The state of the product ad (enabled, paused, archived)"""


class SponsoredProductProductAdsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_id: list[str]
    """The unique identifier of the product ad"""
    campaign_id: list[str]
    """The campaign ID this product ad belongs to"""
    ad_group_id: list[str]
    """The ad group ID this product ad belongs to"""
    asin: list[str]
    """The ASIN of the advertised product"""
    sku: list[str]
    """The SKU of the advertised product (seller accounts only)"""
    state: list[str]
    """The state of the product ad (enabled, paused, archived)"""


class SponsoredProductProductAdsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_id: Any
    """The unique identifier of the product ad"""
    campaign_id: Any
    """The campaign ID this product ad belongs to"""
    ad_group_id: Any
    """The ad group ID this product ad belongs to"""
    asin: Any
    """The ASIN of the advertised product"""
    sku: Any
    """The SKU of the advertised product (seller accounts only)"""
    state: Any
    """The state of the product ad (enabled, paused, archived)"""


class SponsoredProductProductAdsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_id: str
    """The unique identifier of the product ad"""
    campaign_id: str
    """The campaign ID this product ad belongs to"""
    ad_group_id: str
    """The ad group ID this product ad belongs to"""
    asin: str
    """The ASIN of the advertised product"""
    sku: str
    """The SKU of the advertised product (seller accounts only)"""
    state: str
    """The state of the product ad (enabled, paused, archived)"""


class SponsoredProductProductAdsSortFilter(TypedDict, total=False):
    """Available fields for sorting sponsored_product_product_ads search results."""
    ad_id: AirbyteSortOrder
    """The unique identifier of the product ad"""
    campaign_id: AirbyteSortOrder
    """The campaign ID this product ad belongs to"""
    ad_group_id: AirbyteSortOrder
    """The ad group ID this product ad belongs to"""
    asin: AirbyteSortOrder
    """The ASIN of the advertised product"""
    sku: AirbyteSortOrder
    """The SKU of the advertised product (seller accounts only)"""
    state: AirbyteSortOrder
    """The state of the product ad (enabled, paused, archived)"""


# Entity-specific condition types for sponsored_product_product_ads
class SponsoredProductProductAdsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SponsoredProductProductAdsSearchFilter


class SponsoredProductProductAdsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SponsoredProductProductAdsSearchFilter


class SponsoredProductProductAdsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SponsoredProductProductAdsSearchFilter


class SponsoredProductProductAdsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SponsoredProductProductAdsSearchFilter


class SponsoredProductProductAdsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SponsoredProductProductAdsSearchFilter


class SponsoredProductProductAdsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SponsoredProductProductAdsSearchFilter


class SponsoredProductProductAdsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SponsoredProductProductAdsStringFilter


class SponsoredProductProductAdsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SponsoredProductProductAdsStringFilter


class SponsoredProductProductAdsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SponsoredProductProductAdsStringFilter


class SponsoredProductProductAdsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SponsoredProductProductAdsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SponsoredProductProductAdsInCondition = TypedDict("SponsoredProductProductAdsInCondition", {"in": SponsoredProductProductAdsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SponsoredProductProductAdsNotCondition = TypedDict("SponsoredProductProductAdsNotCondition", {"not": "SponsoredProductProductAdsCondition"}, total=False)
"""Negates the nested condition."""

SponsoredProductProductAdsAndCondition = TypedDict("SponsoredProductProductAdsAndCondition", {"and": "list[SponsoredProductProductAdsCondition]"}, total=False)
"""True if all nested conditions are true."""

SponsoredProductProductAdsOrCondition = TypedDict("SponsoredProductProductAdsOrCondition", {"or": "list[SponsoredProductProductAdsCondition]"}, total=False)
"""True if any nested condition is true."""

SponsoredProductProductAdsAnyCondition = TypedDict("SponsoredProductProductAdsAnyCondition", {"any": SponsoredProductProductAdsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sponsored_product_product_ads condition types
SponsoredProductProductAdsCondition = (
    SponsoredProductProductAdsEqCondition
    | SponsoredProductProductAdsNeqCondition
    | SponsoredProductProductAdsGtCondition
    | SponsoredProductProductAdsGteCondition
    | SponsoredProductProductAdsLtCondition
    | SponsoredProductProductAdsLteCondition
    | SponsoredProductProductAdsInCondition
    | SponsoredProductProductAdsLikeCondition
    | SponsoredProductProductAdsFuzzyCondition
    | SponsoredProductProductAdsKeywordCondition
    | SponsoredProductProductAdsContainsCondition
    | SponsoredProductProductAdsNotCondition
    | SponsoredProductProductAdsAndCondition
    | SponsoredProductProductAdsOrCondition
    | SponsoredProductProductAdsAnyCondition
)


class SponsoredProductProductAdsSearchQuery(TypedDict, total=False):
    """Search query for sponsored_product_product_ads entity."""
    filter: SponsoredProductProductAdsCondition
    sort: list[SponsoredProductProductAdsSortFilter]


# ===== SPONSORED_PRODUCT_TARGETS SEARCH TYPES =====

class SponsoredProductTargetsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sponsored_product_targets search queries."""
    target_id: str | None
    """The unique identifier of the targeting clause"""
    campaign_id: str | None
    """The campaign ID this target belongs to"""
    ad_group_id: str | None
    """The ad group ID this target belongs to"""
    expression_type: str | None
    """The type of targeting expression (manual, auto)"""
    state: str | None
    """The state of the targeting clause (enabled, paused, archived)"""


class SponsoredProductTargetsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    target_id: list[str]
    """The unique identifier of the targeting clause"""
    campaign_id: list[str]
    """The campaign ID this target belongs to"""
    ad_group_id: list[str]
    """The ad group ID this target belongs to"""
    expression_type: list[str]
    """The type of targeting expression (manual, auto)"""
    state: list[str]
    """The state of the targeting clause (enabled, paused, archived)"""


class SponsoredProductTargetsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    target_id: Any
    """The unique identifier of the targeting clause"""
    campaign_id: Any
    """The campaign ID this target belongs to"""
    ad_group_id: Any
    """The ad group ID this target belongs to"""
    expression_type: Any
    """The type of targeting expression (manual, auto)"""
    state: Any
    """The state of the targeting clause (enabled, paused, archived)"""


class SponsoredProductTargetsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    target_id: str
    """The unique identifier of the targeting clause"""
    campaign_id: str
    """The campaign ID this target belongs to"""
    ad_group_id: str
    """The ad group ID this target belongs to"""
    expression_type: str
    """The type of targeting expression (manual, auto)"""
    state: str
    """The state of the targeting clause (enabled, paused, archived)"""


class SponsoredProductTargetsSortFilter(TypedDict, total=False):
    """Available fields for sorting sponsored_product_targets search results."""
    target_id: AirbyteSortOrder
    """The unique identifier of the targeting clause"""
    campaign_id: AirbyteSortOrder
    """The campaign ID this target belongs to"""
    ad_group_id: AirbyteSortOrder
    """The ad group ID this target belongs to"""
    expression_type: AirbyteSortOrder
    """The type of targeting expression (manual, auto)"""
    state: AirbyteSortOrder
    """The state of the targeting clause (enabled, paused, archived)"""


# Entity-specific condition types for sponsored_product_targets
class SponsoredProductTargetsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SponsoredProductTargetsSearchFilter


class SponsoredProductTargetsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SponsoredProductTargetsSearchFilter


class SponsoredProductTargetsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SponsoredProductTargetsSearchFilter


class SponsoredProductTargetsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SponsoredProductTargetsSearchFilter


class SponsoredProductTargetsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SponsoredProductTargetsSearchFilter


class SponsoredProductTargetsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SponsoredProductTargetsSearchFilter


class SponsoredProductTargetsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SponsoredProductTargetsStringFilter


class SponsoredProductTargetsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SponsoredProductTargetsStringFilter


class SponsoredProductTargetsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SponsoredProductTargetsStringFilter


class SponsoredProductTargetsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SponsoredProductTargetsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SponsoredProductTargetsInCondition = TypedDict("SponsoredProductTargetsInCondition", {"in": SponsoredProductTargetsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SponsoredProductTargetsNotCondition = TypedDict("SponsoredProductTargetsNotCondition", {"not": "SponsoredProductTargetsCondition"}, total=False)
"""Negates the nested condition."""

SponsoredProductTargetsAndCondition = TypedDict("SponsoredProductTargetsAndCondition", {"and": "list[SponsoredProductTargetsCondition]"}, total=False)
"""True if all nested conditions are true."""

SponsoredProductTargetsOrCondition = TypedDict("SponsoredProductTargetsOrCondition", {"or": "list[SponsoredProductTargetsCondition]"}, total=False)
"""True if any nested condition is true."""

SponsoredProductTargetsAnyCondition = TypedDict("SponsoredProductTargetsAnyCondition", {"any": SponsoredProductTargetsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sponsored_product_targets condition types
SponsoredProductTargetsCondition = (
    SponsoredProductTargetsEqCondition
    | SponsoredProductTargetsNeqCondition
    | SponsoredProductTargetsGtCondition
    | SponsoredProductTargetsGteCondition
    | SponsoredProductTargetsLtCondition
    | SponsoredProductTargetsLteCondition
    | SponsoredProductTargetsInCondition
    | SponsoredProductTargetsLikeCondition
    | SponsoredProductTargetsFuzzyCondition
    | SponsoredProductTargetsKeywordCondition
    | SponsoredProductTargetsContainsCondition
    | SponsoredProductTargetsNotCondition
    | SponsoredProductTargetsAndCondition
    | SponsoredProductTargetsOrCondition
    | SponsoredProductTargetsAnyCondition
)


class SponsoredProductTargetsSearchQuery(TypedDict, total=False):
    """Search query for sponsored_product_targets entity."""
    filter: SponsoredProductTargetsCondition
    sort: list[SponsoredProductTargetsSortFilter]


# ===== SPONSORED_PRODUCT_NEGATIVE_KEYWORDS SEARCH TYPES =====

class SponsoredProductNegativeKeywordsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sponsored_product_negative_keywords search queries."""
    keyword_id: str | None
    """The unique identifier of the negative keyword"""
    campaign_id: str | None
    """The campaign ID this negative keyword belongs to"""
    ad_group_id: str | None
    """The ad group ID this negative keyword belongs to"""
    keyword_text: str | None
    """The negative keyword text"""
    state: str | None
    """The state of the negative keyword (enabled, paused, archived)"""


class SponsoredProductNegativeKeywordsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    keyword_id: list[str]
    """The unique identifier of the negative keyword"""
    campaign_id: list[str]
    """The campaign ID this negative keyword belongs to"""
    ad_group_id: list[str]
    """The ad group ID this negative keyword belongs to"""
    keyword_text: list[str]
    """The negative keyword text"""
    state: list[str]
    """The state of the negative keyword (enabled, paused, archived)"""


class SponsoredProductNegativeKeywordsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    keyword_id: Any
    """The unique identifier of the negative keyword"""
    campaign_id: Any
    """The campaign ID this negative keyword belongs to"""
    ad_group_id: Any
    """The ad group ID this negative keyword belongs to"""
    keyword_text: Any
    """The negative keyword text"""
    state: Any
    """The state of the negative keyword (enabled, paused, archived)"""


class SponsoredProductNegativeKeywordsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    keyword_id: str
    """The unique identifier of the negative keyword"""
    campaign_id: str
    """The campaign ID this negative keyword belongs to"""
    ad_group_id: str
    """The ad group ID this negative keyword belongs to"""
    keyword_text: str
    """The negative keyword text"""
    state: str
    """The state of the negative keyword (enabled, paused, archived)"""


class SponsoredProductNegativeKeywordsSortFilter(TypedDict, total=False):
    """Available fields for sorting sponsored_product_negative_keywords search results."""
    keyword_id: AirbyteSortOrder
    """The unique identifier of the negative keyword"""
    campaign_id: AirbyteSortOrder
    """The campaign ID this negative keyword belongs to"""
    ad_group_id: AirbyteSortOrder
    """The ad group ID this negative keyword belongs to"""
    keyword_text: AirbyteSortOrder
    """The negative keyword text"""
    state: AirbyteSortOrder
    """The state of the negative keyword (enabled, paused, archived)"""


# Entity-specific condition types for sponsored_product_negative_keywords
class SponsoredProductNegativeKeywordsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SponsoredProductNegativeKeywordsSearchFilter


class SponsoredProductNegativeKeywordsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SponsoredProductNegativeKeywordsSearchFilter


class SponsoredProductNegativeKeywordsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SponsoredProductNegativeKeywordsSearchFilter


class SponsoredProductNegativeKeywordsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SponsoredProductNegativeKeywordsSearchFilter


class SponsoredProductNegativeKeywordsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SponsoredProductNegativeKeywordsSearchFilter


class SponsoredProductNegativeKeywordsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SponsoredProductNegativeKeywordsSearchFilter


class SponsoredProductNegativeKeywordsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SponsoredProductNegativeKeywordsStringFilter


class SponsoredProductNegativeKeywordsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SponsoredProductNegativeKeywordsStringFilter


class SponsoredProductNegativeKeywordsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SponsoredProductNegativeKeywordsStringFilter


class SponsoredProductNegativeKeywordsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SponsoredProductNegativeKeywordsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SponsoredProductNegativeKeywordsInCondition = TypedDict("SponsoredProductNegativeKeywordsInCondition", {"in": SponsoredProductNegativeKeywordsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SponsoredProductNegativeKeywordsNotCondition = TypedDict("SponsoredProductNegativeKeywordsNotCondition", {"not": "SponsoredProductNegativeKeywordsCondition"}, total=False)
"""Negates the nested condition."""

SponsoredProductNegativeKeywordsAndCondition = TypedDict("SponsoredProductNegativeKeywordsAndCondition", {"and": "list[SponsoredProductNegativeKeywordsCondition]"}, total=False)
"""True if all nested conditions are true."""

SponsoredProductNegativeKeywordsOrCondition = TypedDict("SponsoredProductNegativeKeywordsOrCondition", {"or": "list[SponsoredProductNegativeKeywordsCondition]"}, total=False)
"""True if any nested condition is true."""

SponsoredProductNegativeKeywordsAnyCondition = TypedDict("SponsoredProductNegativeKeywordsAnyCondition", {"any": SponsoredProductNegativeKeywordsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sponsored_product_negative_keywords condition types
SponsoredProductNegativeKeywordsCondition = (
    SponsoredProductNegativeKeywordsEqCondition
    | SponsoredProductNegativeKeywordsNeqCondition
    | SponsoredProductNegativeKeywordsGtCondition
    | SponsoredProductNegativeKeywordsGteCondition
    | SponsoredProductNegativeKeywordsLtCondition
    | SponsoredProductNegativeKeywordsLteCondition
    | SponsoredProductNegativeKeywordsInCondition
    | SponsoredProductNegativeKeywordsLikeCondition
    | SponsoredProductNegativeKeywordsFuzzyCondition
    | SponsoredProductNegativeKeywordsKeywordCondition
    | SponsoredProductNegativeKeywordsContainsCondition
    | SponsoredProductNegativeKeywordsNotCondition
    | SponsoredProductNegativeKeywordsAndCondition
    | SponsoredProductNegativeKeywordsOrCondition
    | SponsoredProductNegativeKeywordsAnyCondition
)


class SponsoredProductNegativeKeywordsSearchQuery(TypedDict, total=False):
    """Search query for sponsored_product_negative_keywords entity."""
    filter: SponsoredProductNegativeKeywordsCondition
    sort: list[SponsoredProductNegativeKeywordsSortFilter]


# ===== SPONSORED_BRANDS_CAMPAIGNS SEARCH TYPES =====

class SponsoredBrandsCampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sponsored_brands_campaigns search queries."""
    campaign_id: str | None
    """The unique identifier of the campaign"""
    name: str | None
    """The name of the campaign"""
    state: str | None
    """The state of the campaign (enabled, paused, archived)"""
    budget: float | None
    """The budget amount for the campaign"""
    budget_type: str | None
    """The budget type (DAILY, LIFETIME)"""
    start_date: str | None
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: str | None
    """The end date of the campaign (YYYYMMDD format)"""
    portfolio_id: str | None
    """The portfolio ID this campaign belongs to"""


class SponsoredBrandsCampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    campaign_id: list[str]
    """The unique identifier of the campaign"""
    name: list[str]
    """The name of the campaign"""
    state: list[str]
    """The state of the campaign (enabled, paused, archived)"""
    budget: list[float]
    """The budget amount for the campaign"""
    budget_type: list[str]
    """The budget type (DAILY, LIFETIME)"""
    start_date: list[str]
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: list[str]
    """The end date of the campaign (YYYYMMDD format)"""
    portfolio_id: list[str]
    """The portfolio ID this campaign belongs to"""


class SponsoredBrandsCampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    campaign_id: Any
    """The unique identifier of the campaign"""
    name: Any
    """The name of the campaign"""
    state: Any
    """The state of the campaign (enabled, paused, archived)"""
    budget: Any
    """The budget amount for the campaign"""
    budget_type: Any
    """The budget type (DAILY, LIFETIME)"""
    start_date: Any
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: Any
    """The end date of the campaign (YYYYMMDD format)"""
    portfolio_id: Any
    """The portfolio ID this campaign belongs to"""


class SponsoredBrandsCampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    campaign_id: str
    """The unique identifier of the campaign"""
    name: str
    """The name of the campaign"""
    state: str
    """The state of the campaign (enabled, paused, archived)"""
    budget: str
    """The budget amount for the campaign"""
    budget_type: str
    """The budget type (DAILY, LIFETIME)"""
    start_date: str
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: str
    """The end date of the campaign (YYYYMMDD format)"""
    portfolio_id: str
    """The portfolio ID this campaign belongs to"""


class SponsoredBrandsCampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting sponsored_brands_campaigns search results."""
    campaign_id: AirbyteSortOrder
    """The unique identifier of the campaign"""
    name: AirbyteSortOrder
    """The name of the campaign"""
    state: AirbyteSortOrder
    """The state of the campaign (enabled, paused, archived)"""
    budget: AirbyteSortOrder
    """The budget amount for the campaign"""
    budget_type: AirbyteSortOrder
    """The budget type (DAILY, LIFETIME)"""
    start_date: AirbyteSortOrder
    """The start date of the campaign (YYYYMMDD format)"""
    end_date: AirbyteSortOrder
    """The end date of the campaign (YYYYMMDD format)"""
    portfolio_id: AirbyteSortOrder
    """The portfolio ID this campaign belongs to"""


# Entity-specific condition types for sponsored_brands_campaigns
class SponsoredBrandsCampaignsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SponsoredBrandsCampaignsSearchFilter


class SponsoredBrandsCampaignsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SponsoredBrandsCampaignsSearchFilter


class SponsoredBrandsCampaignsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SponsoredBrandsCampaignsSearchFilter


class SponsoredBrandsCampaignsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SponsoredBrandsCampaignsSearchFilter


class SponsoredBrandsCampaignsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SponsoredBrandsCampaignsSearchFilter


class SponsoredBrandsCampaignsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SponsoredBrandsCampaignsSearchFilter


class SponsoredBrandsCampaignsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SponsoredBrandsCampaignsStringFilter


class SponsoredBrandsCampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SponsoredBrandsCampaignsStringFilter


class SponsoredBrandsCampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SponsoredBrandsCampaignsStringFilter


class SponsoredBrandsCampaignsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SponsoredBrandsCampaignsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SponsoredBrandsCampaignsInCondition = TypedDict("SponsoredBrandsCampaignsInCondition", {"in": SponsoredBrandsCampaignsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SponsoredBrandsCampaignsNotCondition = TypedDict("SponsoredBrandsCampaignsNotCondition", {"not": "SponsoredBrandsCampaignsCondition"}, total=False)
"""Negates the nested condition."""

SponsoredBrandsCampaignsAndCondition = TypedDict("SponsoredBrandsCampaignsAndCondition", {"and": "list[SponsoredBrandsCampaignsCondition]"}, total=False)
"""True if all nested conditions are true."""

SponsoredBrandsCampaignsOrCondition = TypedDict("SponsoredBrandsCampaignsOrCondition", {"or": "list[SponsoredBrandsCampaignsCondition]"}, total=False)
"""True if any nested condition is true."""

SponsoredBrandsCampaignsAnyCondition = TypedDict("SponsoredBrandsCampaignsAnyCondition", {"any": SponsoredBrandsCampaignsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sponsored_brands_campaigns condition types
SponsoredBrandsCampaignsCondition = (
    SponsoredBrandsCampaignsEqCondition
    | SponsoredBrandsCampaignsNeqCondition
    | SponsoredBrandsCampaignsGtCondition
    | SponsoredBrandsCampaignsGteCondition
    | SponsoredBrandsCampaignsLtCondition
    | SponsoredBrandsCampaignsLteCondition
    | SponsoredBrandsCampaignsInCondition
    | SponsoredBrandsCampaignsLikeCondition
    | SponsoredBrandsCampaignsFuzzyCondition
    | SponsoredBrandsCampaignsKeywordCondition
    | SponsoredBrandsCampaignsContainsCondition
    | SponsoredBrandsCampaignsNotCondition
    | SponsoredBrandsCampaignsAndCondition
    | SponsoredBrandsCampaignsOrCondition
    | SponsoredBrandsCampaignsAnyCondition
)


class SponsoredBrandsCampaignsSearchQuery(TypedDict, total=False):
    """Search query for sponsored_brands_campaigns entity."""
    filter: SponsoredBrandsCampaignsCondition
    sort: list[SponsoredBrandsCampaignsSortFilter]


# ===== SPONSORED_BRANDS_AD_GROUPS SEARCH TYPES =====

class SponsoredBrandsAdGroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sponsored_brands_ad_groups search queries."""
    ad_group_id: str | None
    """The unique identifier of the ad group"""
    campaign_id: str | None
    """The campaign ID this ad group belongs to"""
    name: str | None
    """The name of the ad group"""
    state: str | None
    """The state of the ad group (enabled, paused, archived)"""


class SponsoredBrandsAdGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_group_id: list[str]
    """The unique identifier of the ad group"""
    campaign_id: list[str]
    """The campaign ID this ad group belongs to"""
    name: list[str]
    """The name of the ad group"""
    state: list[str]
    """The state of the ad group (enabled, paused, archived)"""


class SponsoredBrandsAdGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_group_id: Any
    """The unique identifier of the ad group"""
    campaign_id: Any
    """The campaign ID this ad group belongs to"""
    name: Any
    """The name of the ad group"""
    state: Any
    """The state of the ad group (enabled, paused, archived)"""


class SponsoredBrandsAdGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_group_id: str
    """The unique identifier of the ad group"""
    campaign_id: str
    """The campaign ID this ad group belongs to"""
    name: str
    """The name of the ad group"""
    state: str
    """The state of the ad group (enabled, paused, archived)"""


class SponsoredBrandsAdGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting sponsored_brands_ad_groups search results."""
    ad_group_id: AirbyteSortOrder
    """The unique identifier of the ad group"""
    campaign_id: AirbyteSortOrder
    """The campaign ID this ad group belongs to"""
    name: AirbyteSortOrder
    """The name of the ad group"""
    state: AirbyteSortOrder
    """The state of the ad group (enabled, paused, archived)"""


# Entity-specific condition types for sponsored_brands_ad_groups
class SponsoredBrandsAdGroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SponsoredBrandsAdGroupsSearchFilter


class SponsoredBrandsAdGroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SponsoredBrandsAdGroupsSearchFilter


class SponsoredBrandsAdGroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SponsoredBrandsAdGroupsSearchFilter


class SponsoredBrandsAdGroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SponsoredBrandsAdGroupsSearchFilter


class SponsoredBrandsAdGroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SponsoredBrandsAdGroupsSearchFilter


class SponsoredBrandsAdGroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SponsoredBrandsAdGroupsSearchFilter


class SponsoredBrandsAdGroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SponsoredBrandsAdGroupsStringFilter


class SponsoredBrandsAdGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SponsoredBrandsAdGroupsStringFilter


class SponsoredBrandsAdGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SponsoredBrandsAdGroupsStringFilter


class SponsoredBrandsAdGroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SponsoredBrandsAdGroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SponsoredBrandsAdGroupsInCondition = TypedDict("SponsoredBrandsAdGroupsInCondition", {"in": SponsoredBrandsAdGroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SponsoredBrandsAdGroupsNotCondition = TypedDict("SponsoredBrandsAdGroupsNotCondition", {"not": "SponsoredBrandsAdGroupsCondition"}, total=False)
"""Negates the nested condition."""

SponsoredBrandsAdGroupsAndCondition = TypedDict("SponsoredBrandsAdGroupsAndCondition", {"and": "list[SponsoredBrandsAdGroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

SponsoredBrandsAdGroupsOrCondition = TypedDict("SponsoredBrandsAdGroupsOrCondition", {"or": "list[SponsoredBrandsAdGroupsCondition]"}, total=False)
"""True if any nested condition is true."""

SponsoredBrandsAdGroupsAnyCondition = TypedDict("SponsoredBrandsAdGroupsAnyCondition", {"any": SponsoredBrandsAdGroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sponsored_brands_ad_groups condition types
SponsoredBrandsAdGroupsCondition = (
    SponsoredBrandsAdGroupsEqCondition
    | SponsoredBrandsAdGroupsNeqCondition
    | SponsoredBrandsAdGroupsGtCondition
    | SponsoredBrandsAdGroupsGteCondition
    | SponsoredBrandsAdGroupsLtCondition
    | SponsoredBrandsAdGroupsLteCondition
    | SponsoredBrandsAdGroupsInCondition
    | SponsoredBrandsAdGroupsLikeCondition
    | SponsoredBrandsAdGroupsFuzzyCondition
    | SponsoredBrandsAdGroupsKeywordCondition
    | SponsoredBrandsAdGroupsContainsCondition
    | SponsoredBrandsAdGroupsNotCondition
    | SponsoredBrandsAdGroupsAndCondition
    | SponsoredBrandsAdGroupsOrCondition
    | SponsoredBrandsAdGroupsAnyCondition
)


class SponsoredBrandsAdGroupsSearchQuery(TypedDict, total=False):
    """Search query for sponsored_brands_ad_groups entity."""
    filter: SponsoredBrandsAdGroupsCondition
    sort: list[SponsoredBrandsAdGroupsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
