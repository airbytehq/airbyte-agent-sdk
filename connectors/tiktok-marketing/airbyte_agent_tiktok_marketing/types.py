"""
Type definitions for tiktok-marketing connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class AdvertisersListParams(TypedDict):
    """Parameters for advertisers.list operation"""
    advertiser_ids: str
    page: NotRequired[int]
    page_size: NotRequired[int]

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    advertiser_id: str
    page: NotRequired[int]
    page_size: NotRequired[int]

class AdGroupsListParams(TypedDict):
    """Parameters for ad_groups.list operation"""
    advertiser_id: str
    page: NotRequired[int]
    page_size: NotRequired[int]

class AdsListParams(TypedDict):
    """Parameters for ads.list operation"""
    advertiser_id: str
    page: NotRequired[int]
    page_size: NotRequired[int]

class AudiencesListParams(TypedDict):
    """Parameters for audiences.list operation"""
    advertiser_id: str
    page: NotRequired[int]
    page_size: NotRequired[int]

class CreativeAssetsImagesListParams(TypedDict):
    """Parameters for creative_assets_images.list operation"""
    advertiser_id: str
    page: NotRequired[int]
    page_size: NotRequired[int]

class CreativeAssetsVideosListParams(TypedDict):
    """Parameters for creative_assets_videos.list operation"""
    advertiser_id: str
    page: NotRequired[int]
    page_size: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ADVERTISERS SEARCH TYPES =====

class AdvertisersSearchFilter(TypedDict, total=False):
    """Available fields for filtering advertisers search queries."""
    address: str | None
    """The physical address of the advertiser."""
    advertiser_account_type: str | None
    """The type of advertiser's account (e.g., individual, business)."""
    advertiser_id: int | None
    """Unique identifier for the advertiser."""
    balance: float | None
    """The current balance in the advertiser's account."""
    brand: str | None
    """The brand name associated with the advertiser."""
    cellphone_number: str | None
    """The cellphone number of the advertiser."""
    company: str | None
    """The name of the company associated with the advertiser."""
    contacter: str | None
    """The contact person for the advertiser."""
    country: str | None
    """The country where the advertiser is located."""
    create_time: int | None
    """The timestamp when the advertiser account was created."""
    currency: str | None
    """The currency used for transactions in the account."""
    description: str | None
    """A brief description or bio of the advertiser or company."""
    display_timezone: str | None
    """The timezone for display purposes."""
    email: str | None
    """The email address associated with the advertiser."""
    industry: str | None
    """The industry or sector the advertiser operates in."""
    language: str | None
    """The preferred language of communication for the advertiser."""
    license_city: str | None
    """The city where the advertiser's license is registered."""
    license_no: str | None
    """The license number of the advertiser."""
    license_province: str | None
    """The province or state where the advertiser's license is registered."""
    license_url: str | None
    """The URL link to the advertiser's license documentation."""
    name: str | None
    """The name of the advertiser or company."""
    promotion_area: str | None
    """The specific area or region where the advertiser focuses promotion."""
    promotion_center_city: str | None
    """The city at the center of the advertiser's promotion activities."""
    promotion_center_province: str | None
    """The province or state at the center of the advertiser's promotion activities."""
    rejection_reason: str | None
    """Reason for any advertisement rejection by the platform."""
    role: str | None
    """The role or position of the advertiser within the company."""
    status: str | None
    """The current status of the advertiser's account."""
    telephone_number: str | None
    """The telephone number of the advertiser."""
    timezone: str | None
    """The timezone setting for the advertiser's activities."""


class AdvertisersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    address: list[str]
    """The physical address of the advertiser."""
    advertiser_account_type: list[str]
    """The type of advertiser's account (e.g., individual, business)."""
    advertiser_id: list[int]
    """Unique identifier for the advertiser."""
    balance: list[float]
    """The current balance in the advertiser's account."""
    brand: list[str]
    """The brand name associated with the advertiser."""
    cellphone_number: list[str]
    """The cellphone number of the advertiser."""
    company: list[str]
    """The name of the company associated with the advertiser."""
    contacter: list[str]
    """The contact person for the advertiser."""
    country: list[str]
    """The country where the advertiser is located."""
    create_time: list[int]
    """The timestamp when the advertiser account was created."""
    currency: list[str]
    """The currency used for transactions in the account."""
    description: list[str]
    """A brief description or bio of the advertiser or company."""
    display_timezone: list[str]
    """The timezone for display purposes."""
    email: list[str]
    """The email address associated with the advertiser."""
    industry: list[str]
    """The industry or sector the advertiser operates in."""
    language: list[str]
    """The preferred language of communication for the advertiser."""
    license_city: list[str]
    """The city where the advertiser's license is registered."""
    license_no: list[str]
    """The license number of the advertiser."""
    license_province: list[str]
    """The province or state where the advertiser's license is registered."""
    license_url: list[str]
    """The URL link to the advertiser's license documentation."""
    name: list[str]
    """The name of the advertiser or company."""
    promotion_area: list[str]
    """The specific area or region where the advertiser focuses promotion."""
    promotion_center_city: list[str]
    """The city at the center of the advertiser's promotion activities."""
    promotion_center_province: list[str]
    """The province or state at the center of the advertiser's promotion activities."""
    rejection_reason: list[str]
    """Reason for any advertisement rejection by the platform."""
    role: list[str]
    """The role or position of the advertiser within the company."""
    status: list[str]
    """The current status of the advertiser's account."""
    telephone_number: list[str]
    """The telephone number of the advertiser."""
    timezone: list[str]
    """The timezone setting for the advertiser's activities."""


class AdvertisersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    address: Any
    """The physical address of the advertiser."""
    advertiser_account_type: Any
    """The type of advertiser's account (e.g., individual, business)."""
    advertiser_id: Any
    """Unique identifier for the advertiser."""
    balance: Any
    """The current balance in the advertiser's account."""
    brand: Any
    """The brand name associated with the advertiser."""
    cellphone_number: Any
    """The cellphone number of the advertiser."""
    company: Any
    """The name of the company associated with the advertiser."""
    contacter: Any
    """The contact person for the advertiser."""
    country: Any
    """The country where the advertiser is located."""
    create_time: Any
    """The timestamp when the advertiser account was created."""
    currency: Any
    """The currency used for transactions in the account."""
    description: Any
    """A brief description or bio of the advertiser or company."""
    display_timezone: Any
    """The timezone for display purposes."""
    email: Any
    """The email address associated with the advertiser."""
    industry: Any
    """The industry or sector the advertiser operates in."""
    language: Any
    """The preferred language of communication for the advertiser."""
    license_city: Any
    """The city where the advertiser's license is registered."""
    license_no: Any
    """The license number of the advertiser."""
    license_province: Any
    """The province or state where the advertiser's license is registered."""
    license_url: Any
    """The URL link to the advertiser's license documentation."""
    name: Any
    """The name of the advertiser or company."""
    promotion_area: Any
    """The specific area or region where the advertiser focuses promotion."""
    promotion_center_city: Any
    """The city at the center of the advertiser's promotion activities."""
    promotion_center_province: Any
    """The province or state at the center of the advertiser's promotion activities."""
    rejection_reason: Any
    """Reason for any advertisement rejection by the platform."""
    role: Any
    """The role or position of the advertiser within the company."""
    status: Any
    """The current status of the advertiser's account."""
    telephone_number: Any
    """The telephone number of the advertiser."""
    timezone: Any
    """The timezone setting for the advertiser's activities."""


class AdvertisersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    address: str
    """The physical address of the advertiser."""
    advertiser_account_type: str
    """The type of advertiser's account (e.g., individual, business)."""
    advertiser_id: str
    """Unique identifier for the advertiser."""
    balance: str
    """The current balance in the advertiser's account."""
    brand: str
    """The brand name associated with the advertiser."""
    cellphone_number: str
    """The cellphone number of the advertiser."""
    company: str
    """The name of the company associated with the advertiser."""
    contacter: str
    """The contact person for the advertiser."""
    country: str
    """The country where the advertiser is located."""
    create_time: str
    """The timestamp when the advertiser account was created."""
    currency: str
    """The currency used for transactions in the account."""
    description: str
    """A brief description or bio of the advertiser or company."""
    display_timezone: str
    """The timezone for display purposes."""
    email: str
    """The email address associated with the advertiser."""
    industry: str
    """The industry or sector the advertiser operates in."""
    language: str
    """The preferred language of communication for the advertiser."""
    license_city: str
    """The city where the advertiser's license is registered."""
    license_no: str
    """The license number of the advertiser."""
    license_province: str
    """The province or state where the advertiser's license is registered."""
    license_url: str
    """The URL link to the advertiser's license documentation."""
    name: str
    """The name of the advertiser or company."""
    promotion_area: str
    """The specific area or region where the advertiser focuses promotion."""
    promotion_center_city: str
    """The city at the center of the advertiser's promotion activities."""
    promotion_center_province: str
    """The province or state at the center of the advertiser's promotion activities."""
    rejection_reason: str
    """Reason for any advertisement rejection by the platform."""
    role: str
    """The role or position of the advertiser within the company."""
    status: str
    """The current status of the advertiser's account."""
    telephone_number: str
    """The telephone number of the advertiser."""
    timezone: str
    """The timezone setting for the advertiser's activities."""


class AdvertisersSortFilter(TypedDict, total=False):
    """Available fields for sorting advertisers search results."""
    address: AirbyteSortOrder
    """The physical address of the advertiser."""
    advertiser_account_type: AirbyteSortOrder
    """The type of advertiser's account (e.g., individual, business)."""
    advertiser_id: AirbyteSortOrder
    """Unique identifier for the advertiser."""
    balance: AirbyteSortOrder
    """The current balance in the advertiser's account."""
    brand: AirbyteSortOrder
    """The brand name associated with the advertiser."""
    cellphone_number: AirbyteSortOrder
    """The cellphone number of the advertiser."""
    company: AirbyteSortOrder
    """The name of the company associated with the advertiser."""
    contacter: AirbyteSortOrder
    """The contact person for the advertiser."""
    country: AirbyteSortOrder
    """The country where the advertiser is located."""
    create_time: AirbyteSortOrder
    """The timestamp when the advertiser account was created."""
    currency: AirbyteSortOrder
    """The currency used for transactions in the account."""
    description: AirbyteSortOrder
    """A brief description or bio of the advertiser or company."""
    display_timezone: AirbyteSortOrder
    """The timezone for display purposes."""
    email: AirbyteSortOrder
    """The email address associated with the advertiser."""
    industry: AirbyteSortOrder
    """The industry or sector the advertiser operates in."""
    language: AirbyteSortOrder
    """The preferred language of communication for the advertiser."""
    license_city: AirbyteSortOrder
    """The city where the advertiser's license is registered."""
    license_no: AirbyteSortOrder
    """The license number of the advertiser."""
    license_province: AirbyteSortOrder
    """The province or state where the advertiser's license is registered."""
    license_url: AirbyteSortOrder
    """The URL link to the advertiser's license documentation."""
    name: AirbyteSortOrder
    """The name of the advertiser or company."""
    promotion_area: AirbyteSortOrder
    """The specific area or region where the advertiser focuses promotion."""
    promotion_center_city: AirbyteSortOrder
    """The city at the center of the advertiser's promotion activities."""
    promotion_center_province: AirbyteSortOrder
    """The province or state at the center of the advertiser's promotion activities."""
    rejection_reason: AirbyteSortOrder
    """Reason for any advertisement rejection by the platform."""
    role: AirbyteSortOrder
    """The role or position of the advertiser within the company."""
    status: AirbyteSortOrder
    """The current status of the advertiser's account."""
    telephone_number: AirbyteSortOrder
    """The telephone number of the advertiser."""
    timezone: AirbyteSortOrder
    """The timezone setting for the advertiser's activities."""


# Entity-specific condition types for advertisers
class AdvertisersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdvertisersSearchFilter


class AdvertisersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdvertisersSearchFilter


class AdvertisersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdvertisersSearchFilter


class AdvertisersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdvertisersSearchFilter


class AdvertisersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdvertisersSearchFilter


class AdvertisersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdvertisersSearchFilter


class AdvertisersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdvertisersStringFilter


class AdvertisersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdvertisersStringFilter


class AdvertisersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdvertisersStringFilter


class AdvertisersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdvertisersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdvertisersInCondition = TypedDict("AdvertisersInCondition", {"in": AdvertisersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdvertisersNotCondition = TypedDict("AdvertisersNotCondition", {"not": "AdvertisersCondition"}, total=False)
"""Negates the nested condition."""

AdvertisersAndCondition = TypedDict("AdvertisersAndCondition", {"and": "list[AdvertisersCondition]"}, total=False)
"""True if all nested conditions are true."""

AdvertisersOrCondition = TypedDict("AdvertisersOrCondition", {"or": "list[AdvertisersCondition]"}, total=False)
"""True if any nested condition is true."""

AdvertisersAnyCondition = TypedDict("AdvertisersAnyCondition", {"any": AdvertisersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all advertisers condition types
AdvertisersCondition = (
    AdvertisersEqCondition
    | AdvertisersNeqCondition
    | AdvertisersGtCondition
    | AdvertisersGteCondition
    | AdvertisersLtCondition
    | AdvertisersLteCondition
    | AdvertisersInCondition
    | AdvertisersLikeCondition
    | AdvertisersFuzzyCondition
    | AdvertisersKeywordCondition
    | AdvertisersContainsCondition
    | AdvertisersNotCondition
    | AdvertisersAndCondition
    | AdvertisersOrCondition
    | AdvertisersAnyCondition
)


class AdvertisersSearchQuery(TypedDict, total=False):
    """Search query for advertisers entity."""
    filter: AdvertisersCondition
    sort: list[AdvertisersSortFilter]


# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    advertiser_id: int | None
    """The unique identifier of the advertiser associated with the campaign"""
    app_promotion_type: str | None
    """Type of app promotion being used in the campaign"""
    bid_type: str | None
    """Type of bid strategy being used in the campaign"""
    budget: float | None
    """Total budget allocated for the campaign"""
    budget_mode: str | None
    """Mode in which the budget is being managed (e.g., daily, lifetime)"""
    budget_optimize_on: bool | None
    """The metric or event that the budget optimization is based on"""
    campaign_id: int | None
    """The unique identifier of the campaign"""
    campaign_name: str | None
    """Name of the campaign for easy identification"""
    campaign_type: str | None
    """Type of campaign (e.g., awareness, conversion)"""
    create_time: str | None
    """Timestamp when the campaign was created"""
    deep_bid_type: str | None
    """Advanced bid type used for campaign optimization"""
    is_new_structure: bool | None
    """Flag indicating if the campaign utilizes a new campaign structure"""
    is_search_campaign: bool | None
    """Flag indicating if the campaign is a search campaign"""
    is_smart_performance_campaign: bool | None
    """Flag indicating if the campaign uses smart performance optimization"""
    modify_time: str | None
    """Timestamp when the campaign was last modified"""
    objective: str | None
    """The objective or goal of the campaign"""
    objective_type: str | None
    """Type of objective selected for the campaign"""
    operation_status: str | None
    """Current operational status of the campaign"""
    optimization_goal: str | None
    """Specific goal to be optimized for in the campaign"""
    rf_campaign_type: str | None
    """Type of RF (reach and frequency) campaign being run"""
    roas_bid: float | None
    """Return on ad spend goal set for the campaign"""
    secondary_status: str | None
    """Additional status information of the campaign"""
    split_test_variable: str | None
    """Variable being tested in a split test campaign"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    advertiser_id: list[int]
    """The unique identifier of the advertiser associated with the campaign"""
    app_promotion_type: list[str]
    """Type of app promotion being used in the campaign"""
    bid_type: list[str]
    """Type of bid strategy being used in the campaign"""
    budget: list[float]
    """Total budget allocated for the campaign"""
    budget_mode: list[str]
    """Mode in which the budget is being managed (e.g., daily, lifetime)"""
    budget_optimize_on: list[bool]
    """The metric or event that the budget optimization is based on"""
    campaign_id: list[int]
    """The unique identifier of the campaign"""
    campaign_name: list[str]
    """Name of the campaign for easy identification"""
    campaign_type: list[str]
    """Type of campaign (e.g., awareness, conversion)"""
    create_time: list[str]
    """Timestamp when the campaign was created"""
    deep_bid_type: list[str]
    """Advanced bid type used for campaign optimization"""
    is_new_structure: list[bool]
    """Flag indicating if the campaign utilizes a new campaign structure"""
    is_search_campaign: list[bool]
    """Flag indicating if the campaign is a search campaign"""
    is_smart_performance_campaign: list[bool]
    """Flag indicating if the campaign uses smart performance optimization"""
    modify_time: list[str]
    """Timestamp when the campaign was last modified"""
    objective: list[str]
    """The objective or goal of the campaign"""
    objective_type: list[str]
    """Type of objective selected for the campaign"""
    operation_status: list[str]
    """Current operational status of the campaign"""
    optimization_goal: list[str]
    """Specific goal to be optimized for in the campaign"""
    rf_campaign_type: list[str]
    """Type of RF (reach and frequency) campaign being run"""
    roas_bid: list[float]
    """Return on ad spend goal set for the campaign"""
    secondary_status: list[str]
    """Additional status information of the campaign"""
    split_test_variable: list[str]
    """Variable being tested in a split test campaign"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    advertiser_id: Any
    """The unique identifier of the advertiser associated with the campaign"""
    app_promotion_type: Any
    """Type of app promotion being used in the campaign"""
    bid_type: Any
    """Type of bid strategy being used in the campaign"""
    budget: Any
    """Total budget allocated for the campaign"""
    budget_mode: Any
    """Mode in which the budget is being managed (e.g., daily, lifetime)"""
    budget_optimize_on: Any
    """The metric or event that the budget optimization is based on"""
    campaign_id: Any
    """The unique identifier of the campaign"""
    campaign_name: Any
    """Name of the campaign for easy identification"""
    campaign_type: Any
    """Type of campaign (e.g., awareness, conversion)"""
    create_time: Any
    """Timestamp when the campaign was created"""
    deep_bid_type: Any
    """Advanced bid type used for campaign optimization"""
    is_new_structure: Any
    """Flag indicating if the campaign utilizes a new campaign structure"""
    is_search_campaign: Any
    """Flag indicating if the campaign is a search campaign"""
    is_smart_performance_campaign: Any
    """Flag indicating if the campaign uses smart performance optimization"""
    modify_time: Any
    """Timestamp when the campaign was last modified"""
    objective: Any
    """The objective or goal of the campaign"""
    objective_type: Any
    """Type of objective selected for the campaign"""
    operation_status: Any
    """Current operational status of the campaign"""
    optimization_goal: Any
    """Specific goal to be optimized for in the campaign"""
    rf_campaign_type: Any
    """Type of RF (reach and frequency) campaign being run"""
    roas_bid: Any
    """Return on ad spend goal set for the campaign"""
    secondary_status: Any
    """Additional status information of the campaign"""
    split_test_variable: Any
    """Variable being tested in a split test campaign"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    advertiser_id: str
    """The unique identifier of the advertiser associated with the campaign"""
    app_promotion_type: str
    """Type of app promotion being used in the campaign"""
    bid_type: str
    """Type of bid strategy being used in the campaign"""
    budget: str
    """Total budget allocated for the campaign"""
    budget_mode: str
    """Mode in which the budget is being managed (e.g., daily, lifetime)"""
    budget_optimize_on: str
    """The metric or event that the budget optimization is based on"""
    campaign_id: str
    """The unique identifier of the campaign"""
    campaign_name: str
    """Name of the campaign for easy identification"""
    campaign_type: str
    """Type of campaign (e.g., awareness, conversion)"""
    create_time: str
    """Timestamp when the campaign was created"""
    deep_bid_type: str
    """Advanced bid type used for campaign optimization"""
    is_new_structure: str
    """Flag indicating if the campaign utilizes a new campaign structure"""
    is_search_campaign: str
    """Flag indicating if the campaign is a search campaign"""
    is_smart_performance_campaign: str
    """Flag indicating if the campaign uses smart performance optimization"""
    modify_time: str
    """Timestamp when the campaign was last modified"""
    objective: str
    """The objective or goal of the campaign"""
    objective_type: str
    """Type of objective selected for the campaign"""
    operation_status: str
    """Current operational status of the campaign"""
    optimization_goal: str
    """Specific goal to be optimized for in the campaign"""
    rf_campaign_type: str
    """Type of RF (reach and frequency) campaign being run"""
    roas_bid: str
    """Return on ad spend goal set for the campaign"""
    secondary_status: str
    """Additional status information of the campaign"""
    split_test_variable: str
    """Variable being tested in a split test campaign"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    advertiser_id: AirbyteSortOrder
    """The unique identifier of the advertiser associated with the campaign"""
    app_promotion_type: AirbyteSortOrder
    """Type of app promotion being used in the campaign"""
    bid_type: AirbyteSortOrder
    """Type of bid strategy being used in the campaign"""
    budget: AirbyteSortOrder
    """Total budget allocated for the campaign"""
    budget_mode: AirbyteSortOrder
    """Mode in which the budget is being managed (e.g., daily, lifetime)"""
    budget_optimize_on: AirbyteSortOrder
    """The metric or event that the budget optimization is based on"""
    campaign_id: AirbyteSortOrder
    """The unique identifier of the campaign"""
    campaign_name: AirbyteSortOrder
    """Name of the campaign for easy identification"""
    campaign_type: AirbyteSortOrder
    """Type of campaign (e.g., awareness, conversion)"""
    create_time: AirbyteSortOrder
    """Timestamp when the campaign was created"""
    deep_bid_type: AirbyteSortOrder
    """Advanced bid type used for campaign optimization"""
    is_new_structure: AirbyteSortOrder
    """Flag indicating if the campaign utilizes a new campaign structure"""
    is_search_campaign: AirbyteSortOrder
    """Flag indicating if the campaign is a search campaign"""
    is_smart_performance_campaign: AirbyteSortOrder
    """Flag indicating if the campaign uses smart performance optimization"""
    modify_time: AirbyteSortOrder
    """Timestamp when the campaign was last modified"""
    objective: AirbyteSortOrder
    """The objective or goal of the campaign"""
    objective_type: AirbyteSortOrder
    """Type of objective selected for the campaign"""
    operation_status: AirbyteSortOrder
    """Current operational status of the campaign"""
    optimization_goal: AirbyteSortOrder
    """Specific goal to be optimized for in the campaign"""
    rf_campaign_type: AirbyteSortOrder
    """Type of RF (reach and frequency) campaign being run"""
    roas_bid: AirbyteSortOrder
    """Return on ad spend goal set for the campaign"""
    secondary_status: AirbyteSortOrder
    """Additional status information of the campaign"""
    split_test_variable: AirbyteSortOrder
    """Variable being tested in a split test campaign"""


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


class CampaignsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CampaignsStringFilter


class CampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignsStringFilter


class CampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignsStringFilter


class CampaignsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CampaignsAnyValueFilter


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
    | CampaignsLikeCondition
    | CampaignsFuzzyCondition
    | CampaignsKeywordCondition
    | CampaignsContainsCondition
    | CampaignsNotCondition
    | CampaignsAndCondition
    | CampaignsOrCondition
    | CampaignsAnyCondition
)


class CampaignsSearchQuery(TypedDict, total=False):
    """Search query for campaigns entity."""
    filter: CampaignsCondition
    sort: list[CampaignsSortFilter]


# ===== AD_GROUPS SEARCH TYPES =====

class AdGroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_groups search queries."""
    adgroup_id: int | None
    """The unique identifier of the ad group"""
    adgroup_name: str | None
    """The name of the ad group"""
    advertiser_id: int | None
    """The unique identifier of the advertiser"""
    budget: float | None
    """The allocated budget for the ad group"""
    budget_mode: str | None
    """The mode for managing the budget"""
    campaign_id: int | None
    """The unique identifier of the campaign"""
    create_time: str | None
    """The timestamp for when the ad group was created"""
    modify_time: str | None
    """The timestamp for when the ad group was last modified"""
    operation_status: str | None
    """The status of the operation"""
    optimization_goal: str | None
    """The goal set for optimization"""
    placement_type: str | None
    """The type of ad placement"""
    promotion_type: str | None
    """The type of promotion"""
    secondary_status: str | None
    """The secondary status of the ad group"""


class AdGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    adgroup_id: list[int]
    """The unique identifier of the ad group"""
    adgroup_name: list[str]
    """The name of the ad group"""
    advertiser_id: list[int]
    """The unique identifier of the advertiser"""
    budget: list[float]
    """The allocated budget for the ad group"""
    budget_mode: list[str]
    """The mode for managing the budget"""
    campaign_id: list[int]
    """The unique identifier of the campaign"""
    create_time: list[str]
    """The timestamp for when the ad group was created"""
    modify_time: list[str]
    """The timestamp for when the ad group was last modified"""
    operation_status: list[str]
    """The status of the operation"""
    optimization_goal: list[str]
    """The goal set for optimization"""
    placement_type: list[str]
    """The type of ad placement"""
    promotion_type: list[str]
    """The type of promotion"""
    secondary_status: list[str]
    """The secondary status of the ad group"""


class AdGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    adgroup_id: Any
    """The unique identifier of the ad group"""
    adgroup_name: Any
    """The name of the ad group"""
    advertiser_id: Any
    """The unique identifier of the advertiser"""
    budget: Any
    """The allocated budget for the ad group"""
    budget_mode: Any
    """The mode for managing the budget"""
    campaign_id: Any
    """The unique identifier of the campaign"""
    create_time: Any
    """The timestamp for when the ad group was created"""
    modify_time: Any
    """The timestamp for when the ad group was last modified"""
    operation_status: Any
    """The status of the operation"""
    optimization_goal: Any
    """The goal set for optimization"""
    placement_type: Any
    """The type of ad placement"""
    promotion_type: Any
    """The type of promotion"""
    secondary_status: Any
    """The secondary status of the ad group"""


class AdGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    adgroup_id: str
    """The unique identifier of the ad group"""
    adgroup_name: str
    """The name of the ad group"""
    advertiser_id: str
    """The unique identifier of the advertiser"""
    budget: str
    """The allocated budget for the ad group"""
    budget_mode: str
    """The mode for managing the budget"""
    campaign_id: str
    """The unique identifier of the campaign"""
    create_time: str
    """The timestamp for when the ad group was created"""
    modify_time: str
    """The timestamp for when the ad group was last modified"""
    operation_status: str
    """The status of the operation"""
    optimization_goal: str
    """The goal set for optimization"""
    placement_type: str
    """The type of ad placement"""
    promotion_type: str
    """The type of promotion"""
    secondary_status: str
    """The secondary status of the ad group"""


class AdGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_groups search results."""
    adgroup_id: AirbyteSortOrder
    """The unique identifier of the ad group"""
    adgroup_name: AirbyteSortOrder
    """The name of the ad group"""
    advertiser_id: AirbyteSortOrder
    """The unique identifier of the advertiser"""
    budget: AirbyteSortOrder
    """The allocated budget for the ad group"""
    budget_mode: AirbyteSortOrder
    """The mode for managing the budget"""
    campaign_id: AirbyteSortOrder
    """The unique identifier of the campaign"""
    create_time: AirbyteSortOrder
    """The timestamp for when the ad group was created"""
    modify_time: AirbyteSortOrder
    """The timestamp for when the ad group was last modified"""
    operation_status: AirbyteSortOrder
    """The status of the operation"""
    optimization_goal: AirbyteSortOrder
    """The goal set for optimization"""
    placement_type: AirbyteSortOrder
    """The type of ad placement"""
    promotion_type: AirbyteSortOrder
    """The type of promotion"""
    secondary_status: AirbyteSortOrder
    """The secondary status of the ad group"""


# Entity-specific condition types for ad_groups
class AdGroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdGroupsSearchFilter


class AdGroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdGroupsSearchFilter


class AdGroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdGroupsSearchFilter


class AdGroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdGroupsSearchFilter


class AdGroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdGroupsSearchFilter


class AdGroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdGroupsSearchFilter


class AdGroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdGroupsStringFilter


class AdGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdGroupsStringFilter


class AdGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdGroupsStringFilter


class AdGroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdGroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdGroupsInCondition = TypedDict("AdGroupsInCondition", {"in": AdGroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdGroupsNotCondition = TypedDict("AdGroupsNotCondition", {"not": "AdGroupsCondition"}, total=False)
"""Negates the nested condition."""

AdGroupsAndCondition = TypedDict("AdGroupsAndCondition", {"and": "list[AdGroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdGroupsOrCondition = TypedDict("AdGroupsOrCondition", {"or": "list[AdGroupsCondition]"}, total=False)
"""True if any nested condition is true."""

AdGroupsAnyCondition = TypedDict("AdGroupsAnyCondition", {"any": AdGroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_groups condition types
AdGroupsCondition = (
    AdGroupsEqCondition
    | AdGroupsNeqCondition
    | AdGroupsGtCondition
    | AdGroupsGteCondition
    | AdGroupsLtCondition
    | AdGroupsLteCondition
    | AdGroupsInCondition
    | AdGroupsLikeCondition
    | AdGroupsFuzzyCondition
    | AdGroupsKeywordCondition
    | AdGroupsContainsCondition
    | AdGroupsNotCondition
    | AdGroupsAndCondition
    | AdGroupsOrCondition
    | AdGroupsAnyCondition
)


class AdGroupsSearchQuery(TypedDict, total=False):
    """Search query for ad_groups entity."""
    filter: AdGroupsCondition
    sort: list[AdGroupsSortFilter]


# ===== ADS SEARCH TYPES =====

class AdsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ads search queries."""
    ad_format: str | None
    """The format of the ad"""
    ad_id: int | None
    """The unique identifier of the ad"""
    ad_name: str | None
    """The name of the ad"""
    ad_text: str | None
    """The text content of the ad"""
    adgroup_id: int | None
    """The unique identifier of the ad group"""
    adgroup_name: str | None
    """The name of the ad group"""
    advertiser_id: int | None
    """The unique identifier of the advertiser"""
    campaign_id: int | None
    """The unique identifier of the campaign"""
    campaign_name: str | None
    """The name of the campaign"""
    create_time: str | None
    """The timestamp when the ad was created"""
    landing_page_url: str | None
    """The URL of the landing page for the ad"""
    modify_time: str | None
    """The timestamp when the ad was last modified"""
    operation_status: str | None
    """The operational status of the ad"""
    secondary_status: str | None
    """The secondary status of the ad"""
    video_id: str | None
    """The unique identifier of the video"""


class AdsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_format: list[str]
    """The format of the ad"""
    ad_id: list[int]
    """The unique identifier of the ad"""
    ad_name: list[str]
    """The name of the ad"""
    ad_text: list[str]
    """The text content of the ad"""
    adgroup_id: list[int]
    """The unique identifier of the ad group"""
    adgroup_name: list[str]
    """The name of the ad group"""
    advertiser_id: list[int]
    """The unique identifier of the advertiser"""
    campaign_id: list[int]
    """The unique identifier of the campaign"""
    campaign_name: list[str]
    """The name of the campaign"""
    create_time: list[str]
    """The timestamp when the ad was created"""
    landing_page_url: list[str]
    """The URL of the landing page for the ad"""
    modify_time: list[str]
    """The timestamp when the ad was last modified"""
    operation_status: list[str]
    """The operational status of the ad"""
    secondary_status: list[str]
    """The secondary status of the ad"""
    video_id: list[str]
    """The unique identifier of the video"""


class AdsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_format: Any
    """The format of the ad"""
    ad_id: Any
    """The unique identifier of the ad"""
    ad_name: Any
    """The name of the ad"""
    ad_text: Any
    """The text content of the ad"""
    adgroup_id: Any
    """The unique identifier of the ad group"""
    adgroup_name: Any
    """The name of the ad group"""
    advertiser_id: Any
    """The unique identifier of the advertiser"""
    campaign_id: Any
    """The unique identifier of the campaign"""
    campaign_name: Any
    """The name of the campaign"""
    create_time: Any
    """The timestamp when the ad was created"""
    landing_page_url: Any
    """The URL of the landing page for the ad"""
    modify_time: Any
    """The timestamp when the ad was last modified"""
    operation_status: Any
    """The operational status of the ad"""
    secondary_status: Any
    """The secondary status of the ad"""
    video_id: Any
    """The unique identifier of the video"""


class AdsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_format: str
    """The format of the ad"""
    ad_id: str
    """The unique identifier of the ad"""
    ad_name: str
    """The name of the ad"""
    ad_text: str
    """The text content of the ad"""
    adgroup_id: str
    """The unique identifier of the ad group"""
    adgroup_name: str
    """The name of the ad group"""
    advertiser_id: str
    """The unique identifier of the advertiser"""
    campaign_id: str
    """The unique identifier of the campaign"""
    campaign_name: str
    """The name of the campaign"""
    create_time: str
    """The timestamp when the ad was created"""
    landing_page_url: str
    """The URL of the landing page for the ad"""
    modify_time: str
    """The timestamp when the ad was last modified"""
    operation_status: str
    """The operational status of the ad"""
    secondary_status: str
    """The secondary status of the ad"""
    video_id: str
    """The unique identifier of the video"""


class AdsSortFilter(TypedDict, total=False):
    """Available fields for sorting ads search results."""
    ad_format: AirbyteSortOrder
    """The format of the ad"""
    ad_id: AirbyteSortOrder
    """The unique identifier of the ad"""
    ad_name: AirbyteSortOrder
    """The name of the ad"""
    ad_text: AirbyteSortOrder
    """The text content of the ad"""
    adgroup_id: AirbyteSortOrder
    """The unique identifier of the ad group"""
    adgroup_name: AirbyteSortOrder
    """The name of the ad group"""
    advertiser_id: AirbyteSortOrder
    """The unique identifier of the advertiser"""
    campaign_id: AirbyteSortOrder
    """The unique identifier of the campaign"""
    campaign_name: AirbyteSortOrder
    """The name of the campaign"""
    create_time: AirbyteSortOrder
    """The timestamp when the ad was created"""
    landing_page_url: AirbyteSortOrder
    """The URL of the landing page for the ad"""
    modify_time: AirbyteSortOrder
    """The timestamp when the ad was last modified"""
    operation_status: AirbyteSortOrder
    """The operational status of the ad"""
    secondary_status: AirbyteSortOrder
    """The secondary status of the ad"""
    video_id: AirbyteSortOrder
    """The unique identifier of the video"""


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


class AdsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdsStringFilter


class AdsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdsStringFilter


class AdsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdsStringFilter


class AdsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdsAnyValueFilter


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
    | AdsLikeCondition
    | AdsFuzzyCondition
    | AdsKeywordCondition
    | AdsContainsCondition
    | AdsNotCondition
    | AdsAndCondition
    | AdsOrCondition
    | AdsAnyCondition
)


class AdsSearchQuery(TypedDict, total=False):
    """Search query for ads entity."""
    filter: AdsCondition
    sort: list[AdsSortFilter]


# ===== AUDIENCES SEARCH TYPES =====

class AudiencesSearchFilter(TypedDict, total=False):
    """Available fields for filtering audiences search queries."""
    audience_id: str | None
    """Unique identifier for the audience"""
    audience_type: str | None
    """Type of audience"""
    cover_num: int | None
    """Number of audience members covered"""
    create_time: str | None
    """Timestamp indicating when the audience was created"""
    is_valid: bool | None
    """Flag indicating if the audience data is valid"""
    name: str | None
    """Name of the audience"""
    shared: bool | None
    """Flag indicating if the audience is shared"""


class AudiencesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    audience_id: list[str]
    """Unique identifier for the audience"""
    audience_type: list[str]
    """Type of audience"""
    cover_num: list[int]
    """Number of audience members covered"""
    create_time: list[str]
    """Timestamp indicating when the audience was created"""
    is_valid: list[bool]
    """Flag indicating if the audience data is valid"""
    name: list[str]
    """Name of the audience"""
    shared: list[bool]
    """Flag indicating if the audience is shared"""


class AudiencesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    audience_id: Any
    """Unique identifier for the audience"""
    audience_type: Any
    """Type of audience"""
    cover_num: Any
    """Number of audience members covered"""
    create_time: Any
    """Timestamp indicating when the audience was created"""
    is_valid: Any
    """Flag indicating if the audience data is valid"""
    name: Any
    """Name of the audience"""
    shared: Any
    """Flag indicating if the audience is shared"""


class AudiencesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    audience_id: str
    """Unique identifier for the audience"""
    audience_type: str
    """Type of audience"""
    cover_num: str
    """Number of audience members covered"""
    create_time: str
    """Timestamp indicating when the audience was created"""
    is_valid: str
    """Flag indicating if the audience data is valid"""
    name: str
    """Name of the audience"""
    shared: str
    """Flag indicating if the audience is shared"""


class AudiencesSortFilter(TypedDict, total=False):
    """Available fields for sorting audiences search results."""
    audience_id: AirbyteSortOrder
    """Unique identifier for the audience"""
    audience_type: AirbyteSortOrder
    """Type of audience"""
    cover_num: AirbyteSortOrder
    """Number of audience members covered"""
    create_time: AirbyteSortOrder
    """Timestamp indicating when the audience was created"""
    is_valid: AirbyteSortOrder
    """Flag indicating if the audience data is valid"""
    name: AirbyteSortOrder
    """Name of the audience"""
    shared: AirbyteSortOrder
    """Flag indicating if the audience is shared"""


# Entity-specific condition types for audiences
class AudiencesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AudiencesSearchFilter


class AudiencesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AudiencesSearchFilter


class AudiencesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AudiencesSearchFilter


class AudiencesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AudiencesSearchFilter


class AudiencesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AudiencesSearchFilter


class AudiencesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AudiencesSearchFilter


class AudiencesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AudiencesStringFilter


class AudiencesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AudiencesStringFilter


class AudiencesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AudiencesStringFilter


class AudiencesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AudiencesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AudiencesInCondition = TypedDict("AudiencesInCondition", {"in": AudiencesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AudiencesNotCondition = TypedDict("AudiencesNotCondition", {"not": "AudiencesCondition"}, total=False)
"""Negates the nested condition."""

AudiencesAndCondition = TypedDict("AudiencesAndCondition", {"and": "list[AudiencesCondition]"}, total=False)
"""True if all nested conditions are true."""

AudiencesOrCondition = TypedDict("AudiencesOrCondition", {"or": "list[AudiencesCondition]"}, total=False)
"""True if any nested condition is true."""

AudiencesAnyCondition = TypedDict("AudiencesAnyCondition", {"any": AudiencesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all audiences condition types
AudiencesCondition = (
    AudiencesEqCondition
    | AudiencesNeqCondition
    | AudiencesGtCondition
    | AudiencesGteCondition
    | AudiencesLtCondition
    | AudiencesLteCondition
    | AudiencesInCondition
    | AudiencesLikeCondition
    | AudiencesFuzzyCondition
    | AudiencesKeywordCondition
    | AudiencesContainsCondition
    | AudiencesNotCondition
    | AudiencesAndCondition
    | AudiencesOrCondition
    | AudiencesAnyCondition
)


class AudiencesSearchQuery(TypedDict, total=False):
    """Search query for audiences entity."""
    filter: AudiencesCondition
    sort: list[AudiencesSortFilter]


# ===== CREATIVE_ASSETS_IMAGES SEARCH TYPES =====

class CreativeAssetsImagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering creative_assets_images search queries."""
    create_time: str | None
    """The timestamp when the image was created."""
    file_name: str | None
    """The name of the image file."""
    format: str | None
    """The format type of the image file."""
    height: int | None
    """The height dimension of the image."""
    image_id: str | None
    """The unique identifier for the image."""
    image_url: str | None
    """The URL to access the image."""
    modify_time: str | None
    """The timestamp when the image was last modified."""
    size: int | None
    """The size of the image file."""
    width: int | None
    """The width dimension of the image."""


class CreativeAssetsImagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    create_time: list[str]
    """The timestamp when the image was created."""
    file_name: list[str]
    """The name of the image file."""
    format: list[str]
    """The format type of the image file."""
    height: list[int]
    """The height dimension of the image."""
    image_id: list[str]
    """The unique identifier for the image."""
    image_url: list[str]
    """The URL to access the image."""
    modify_time: list[str]
    """The timestamp when the image was last modified."""
    size: list[int]
    """The size of the image file."""
    width: list[int]
    """The width dimension of the image."""


class CreativeAssetsImagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    create_time: Any
    """The timestamp when the image was created."""
    file_name: Any
    """The name of the image file."""
    format: Any
    """The format type of the image file."""
    height: Any
    """The height dimension of the image."""
    image_id: Any
    """The unique identifier for the image."""
    image_url: Any
    """The URL to access the image."""
    modify_time: Any
    """The timestamp when the image was last modified."""
    size: Any
    """The size of the image file."""
    width: Any
    """The width dimension of the image."""


class CreativeAssetsImagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    create_time: str
    """The timestamp when the image was created."""
    file_name: str
    """The name of the image file."""
    format: str
    """The format type of the image file."""
    height: str
    """The height dimension of the image."""
    image_id: str
    """The unique identifier for the image."""
    image_url: str
    """The URL to access the image."""
    modify_time: str
    """The timestamp when the image was last modified."""
    size: str
    """The size of the image file."""
    width: str
    """The width dimension of the image."""


class CreativeAssetsImagesSortFilter(TypedDict, total=False):
    """Available fields for sorting creative_assets_images search results."""
    create_time: AirbyteSortOrder
    """The timestamp when the image was created."""
    file_name: AirbyteSortOrder
    """The name of the image file."""
    format: AirbyteSortOrder
    """The format type of the image file."""
    height: AirbyteSortOrder
    """The height dimension of the image."""
    image_id: AirbyteSortOrder
    """The unique identifier for the image."""
    image_url: AirbyteSortOrder
    """The URL to access the image."""
    modify_time: AirbyteSortOrder
    """The timestamp when the image was last modified."""
    size: AirbyteSortOrder
    """The size of the image file."""
    width: AirbyteSortOrder
    """The width dimension of the image."""


# Entity-specific condition types for creative_assets_images
class CreativeAssetsImagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CreativeAssetsImagesSearchFilter


class CreativeAssetsImagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CreativeAssetsImagesSearchFilter


class CreativeAssetsImagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CreativeAssetsImagesSearchFilter


class CreativeAssetsImagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CreativeAssetsImagesSearchFilter


class CreativeAssetsImagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CreativeAssetsImagesSearchFilter


class CreativeAssetsImagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CreativeAssetsImagesSearchFilter


class CreativeAssetsImagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CreativeAssetsImagesStringFilter


class CreativeAssetsImagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CreativeAssetsImagesStringFilter


class CreativeAssetsImagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CreativeAssetsImagesStringFilter


class CreativeAssetsImagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CreativeAssetsImagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CreativeAssetsImagesInCondition = TypedDict("CreativeAssetsImagesInCondition", {"in": CreativeAssetsImagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CreativeAssetsImagesNotCondition = TypedDict("CreativeAssetsImagesNotCondition", {"not": "CreativeAssetsImagesCondition"}, total=False)
"""Negates the nested condition."""

CreativeAssetsImagesAndCondition = TypedDict("CreativeAssetsImagesAndCondition", {"and": "list[CreativeAssetsImagesCondition]"}, total=False)
"""True if all nested conditions are true."""

CreativeAssetsImagesOrCondition = TypedDict("CreativeAssetsImagesOrCondition", {"or": "list[CreativeAssetsImagesCondition]"}, total=False)
"""True if any nested condition is true."""

CreativeAssetsImagesAnyCondition = TypedDict("CreativeAssetsImagesAnyCondition", {"any": CreativeAssetsImagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all creative_assets_images condition types
CreativeAssetsImagesCondition = (
    CreativeAssetsImagesEqCondition
    | CreativeAssetsImagesNeqCondition
    | CreativeAssetsImagesGtCondition
    | CreativeAssetsImagesGteCondition
    | CreativeAssetsImagesLtCondition
    | CreativeAssetsImagesLteCondition
    | CreativeAssetsImagesInCondition
    | CreativeAssetsImagesLikeCondition
    | CreativeAssetsImagesFuzzyCondition
    | CreativeAssetsImagesKeywordCondition
    | CreativeAssetsImagesContainsCondition
    | CreativeAssetsImagesNotCondition
    | CreativeAssetsImagesAndCondition
    | CreativeAssetsImagesOrCondition
    | CreativeAssetsImagesAnyCondition
)


class CreativeAssetsImagesSearchQuery(TypedDict, total=False):
    """Search query for creative_assets_images entity."""
    filter: CreativeAssetsImagesCondition
    sort: list[CreativeAssetsImagesSortFilter]


# ===== CREATIVE_ASSETS_VIDEOS SEARCH TYPES =====

class CreativeAssetsVideosSearchFilter(TypedDict, total=False):
    """Available fields for filtering creative_assets_videos search queries."""
    create_time: str | None
    """Timestamp when the video was created."""
    duration: float | None
    """Duration of the video in seconds."""
    file_name: str | None
    """Name of the video file."""
    format: str | None
    """Format of the video file."""
    height: int | None
    """Height of the video in pixels."""
    modify_time: str | None
    """Timestamp when the video was last modified."""
    size: int | None
    """Size of the video file in bytes."""
    video_cover_url: str | None
    """URL for the cover image of the video."""
    video_id: str | None
    """ID of the video."""
    width: int | None
    """Width of the video in pixels."""


class CreativeAssetsVideosInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    create_time: list[str]
    """Timestamp when the video was created."""
    duration: list[float]
    """Duration of the video in seconds."""
    file_name: list[str]
    """Name of the video file."""
    format: list[str]
    """Format of the video file."""
    height: list[int]
    """Height of the video in pixels."""
    modify_time: list[str]
    """Timestamp when the video was last modified."""
    size: list[int]
    """Size of the video file in bytes."""
    video_cover_url: list[str]
    """URL for the cover image of the video."""
    video_id: list[str]
    """ID of the video."""
    width: list[int]
    """Width of the video in pixels."""


class CreativeAssetsVideosAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    create_time: Any
    """Timestamp when the video was created."""
    duration: Any
    """Duration of the video in seconds."""
    file_name: Any
    """Name of the video file."""
    format: Any
    """Format of the video file."""
    height: Any
    """Height of the video in pixels."""
    modify_time: Any
    """Timestamp when the video was last modified."""
    size: Any
    """Size of the video file in bytes."""
    video_cover_url: Any
    """URL for the cover image of the video."""
    video_id: Any
    """ID of the video."""
    width: Any
    """Width of the video in pixels."""


class CreativeAssetsVideosStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    create_time: str
    """Timestamp when the video was created."""
    duration: str
    """Duration of the video in seconds."""
    file_name: str
    """Name of the video file."""
    format: str
    """Format of the video file."""
    height: str
    """Height of the video in pixels."""
    modify_time: str
    """Timestamp when the video was last modified."""
    size: str
    """Size of the video file in bytes."""
    video_cover_url: str
    """URL for the cover image of the video."""
    video_id: str
    """ID of the video."""
    width: str
    """Width of the video in pixels."""


class CreativeAssetsVideosSortFilter(TypedDict, total=False):
    """Available fields for sorting creative_assets_videos search results."""
    create_time: AirbyteSortOrder
    """Timestamp when the video was created."""
    duration: AirbyteSortOrder
    """Duration of the video in seconds."""
    file_name: AirbyteSortOrder
    """Name of the video file."""
    format: AirbyteSortOrder
    """Format of the video file."""
    height: AirbyteSortOrder
    """Height of the video in pixels."""
    modify_time: AirbyteSortOrder
    """Timestamp when the video was last modified."""
    size: AirbyteSortOrder
    """Size of the video file in bytes."""
    video_cover_url: AirbyteSortOrder
    """URL for the cover image of the video."""
    video_id: AirbyteSortOrder
    """ID of the video."""
    width: AirbyteSortOrder
    """Width of the video in pixels."""


# Entity-specific condition types for creative_assets_videos
class CreativeAssetsVideosEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CreativeAssetsVideosSearchFilter


class CreativeAssetsVideosNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CreativeAssetsVideosSearchFilter


class CreativeAssetsVideosGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CreativeAssetsVideosSearchFilter


class CreativeAssetsVideosGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CreativeAssetsVideosSearchFilter


class CreativeAssetsVideosLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CreativeAssetsVideosSearchFilter


class CreativeAssetsVideosLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CreativeAssetsVideosSearchFilter


class CreativeAssetsVideosLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CreativeAssetsVideosStringFilter


class CreativeAssetsVideosFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CreativeAssetsVideosStringFilter


class CreativeAssetsVideosKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CreativeAssetsVideosStringFilter


class CreativeAssetsVideosContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CreativeAssetsVideosAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CreativeAssetsVideosInCondition = TypedDict("CreativeAssetsVideosInCondition", {"in": CreativeAssetsVideosInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CreativeAssetsVideosNotCondition = TypedDict("CreativeAssetsVideosNotCondition", {"not": "CreativeAssetsVideosCondition"}, total=False)
"""Negates the nested condition."""

CreativeAssetsVideosAndCondition = TypedDict("CreativeAssetsVideosAndCondition", {"and": "list[CreativeAssetsVideosCondition]"}, total=False)
"""True if all nested conditions are true."""

CreativeAssetsVideosOrCondition = TypedDict("CreativeAssetsVideosOrCondition", {"or": "list[CreativeAssetsVideosCondition]"}, total=False)
"""True if any nested condition is true."""

CreativeAssetsVideosAnyCondition = TypedDict("CreativeAssetsVideosAnyCondition", {"any": CreativeAssetsVideosAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all creative_assets_videos condition types
CreativeAssetsVideosCondition = (
    CreativeAssetsVideosEqCondition
    | CreativeAssetsVideosNeqCondition
    | CreativeAssetsVideosGtCondition
    | CreativeAssetsVideosGteCondition
    | CreativeAssetsVideosLtCondition
    | CreativeAssetsVideosLteCondition
    | CreativeAssetsVideosInCondition
    | CreativeAssetsVideosLikeCondition
    | CreativeAssetsVideosFuzzyCondition
    | CreativeAssetsVideosKeywordCondition
    | CreativeAssetsVideosContainsCondition
    | CreativeAssetsVideosNotCondition
    | CreativeAssetsVideosAndCondition
    | CreativeAssetsVideosOrCondition
    | CreativeAssetsVideosAnyCondition
)


class CreativeAssetsVideosSearchQuery(TypedDict, total=False):
    """Search query for creative_assets_videos entity."""
    filter: CreativeAssetsVideosCondition
    sort: list[CreativeAssetsVideosSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
