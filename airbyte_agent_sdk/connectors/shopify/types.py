"""
Type definitions for shopify connector.
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

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CustomersListParams(TypedDict):
    """Parameters for customers.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class CustomersGetParams(TypedDict):
    """Parameters for customers.get operation"""
    customer_id: str

class OrdersListParams(TypedDict):
    """Parameters for orders.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]
    status: NotRequired[str]
    financial_status: NotRequired[str]
    fulfillment_status: NotRequired[str]

class OrdersGetParams(TypedDict):
    """Parameters for orders.get operation"""
    order_id: str

class ProductsListParams(TypedDict):
    """Parameters for products.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]
    status: NotRequired[str]
    product_type: NotRequired[str]
    vendor: NotRequired[str]
    collection_id: NotRequired[int]

class ProductsGetParams(TypedDict):
    """Parameters for products.get operation"""
    product_id: str

class ProductVariantsListParams(TypedDict):
    """Parameters for product_variants.list operation"""
    product_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]

class ProductVariantsGetParams(TypedDict):
    """Parameters for product_variants.get operation"""
    variant_id: str

class ProductImagesListParams(TypedDict):
    """Parameters for product_images.list operation"""
    product_id: str
    since_id: NotRequired[int]

class ProductImagesGetParams(TypedDict):
    """Parameters for product_images.get operation"""
    product_id: str
    image_id: str

class AbandonedCheckoutsListParams(TypedDict):
    """Parameters for abandoned_checkouts.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]
    status: NotRequired[str]

class LocationsListParams(TypedDict):
    """Parameters for locations.list operation"""
    pass

class LocationsGetParams(TypedDict):
    """Parameters for locations.get operation"""
    location_id: str

class InventoryLevelsListParams(TypedDict):
    """Parameters for inventory_levels.list operation"""
    location_id: str
    limit: NotRequired[int]

class InventoryItemsListParams(TypedDict):
    """Parameters for inventory_items.list operation"""
    ids: str
    limit: NotRequired[int]

class InventoryItemsGetParams(TypedDict):
    """Parameters for inventory_items.get operation"""
    inventory_item_id: str

class ShopGetParams(TypedDict):
    """Parameters for shop.get operation"""
    pass

class PriceRulesListParams(TypedDict):
    """Parameters for price_rules.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class PriceRulesGetParams(TypedDict):
    """Parameters for price_rules.get operation"""
    price_rule_id: str

class DiscountCodesListParams(TypedDict):
    """Parameters for discount_codes.list operation"""
    price_rule_id: str
    limit: NotRequired[int]

class DiscountCodesGetParams(TypedDict):
    """Parameters for discount_codes.get operation"""
    price_rule_id: str
    discount_code_id: str

class CustomCollectionsListParams(TypedDict):
    """Parameters for custom_collections.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    title: NotRequired[str]
    product_id: NotRequired[int]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class CustomCollectionsGetParams(TypedDict):
    """Parameters for custom_collections.get operation"""
    collection_id: str

class SmartCollectionsListParams(TypedDict):
    """Parameters for smart_collections.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    title: NotRequired[str]
    product_id: NotRequired[int]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class SmartCollectionsGetParams(TypedDict):
    """Parameters for smart_collections.get operation"""
    collection_id: str

class CollectsListParams(TypedDict):
    """Parameters for collects.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    collection_id: NotRequired[int]
    product_id: NotRequired[int]

class CollectsGetParams(TypedDict):
    """Parameters for collects.get operation"""
    collect_id: str

class DraftOrdersListParams(TypedDict):
    """Parameters for draft_orders.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    status: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class DraftOrdersGetParams(TypedDict):
    """Parameters for draft_orders.get operation"""
    draft_order_id: str

class FulfillmentsListParams(TypedDict):
    """Parameters for fulfillments.list operation"""
    order_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class FulfillmentsGetParams(TypedDict):
    """Parameters for fulfillments.get operation"""
    order_id: str
    fulfillment_id: str

class OrderRefundsListParams(TypedDict):
    """Parameters for order_refunds.list operation"""
    order_id: str
    limit: NotRequired[int]

class OrderRefundsGetParams(TypedDict):
    """Parameters for order_refunds.get operation"""
    order_id: str
    refund_id: str

class TransactionsListParams(TypedDict):
    """Parameters for transactions.list operation"""
    order_id: str
    since_id: NotRequired[int]

class TransactionsGetParams(TypedDict):
    """Parameters for transactions.get operation"""
    order_id: str
    transaction_id: str

class TenderTransactionsListParams(TypedDict):
    """Parameters for tender_transactions.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    processed_at_min: NotRequired[str]
    processed_at_max: NotRequired[str]
    order: NotRequired[str]

class CountriesListParams(TypedDict):
    """Parameters for countries.list operation"""
    since_id: NotRequired[int]

class CountriesGetParams(TypedDict):
    """Parameters for countries.get operation"""
    country_id: str

class MetafieldShopsListParams(TypedDict):
    """Parameters for metafield_shops.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]
    type: NotRequired[str]

class MetafieldShopsGetParams(TypedDict):
    """Parameters for metafield_shops.get operation"""
    metafield_id: str

class MetafieldCustomersListParams(TypedDict):
    """Parameters for metafield_customers.list operation"""
    customer_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldProductsListParams(TypedDict):
    """Parameters for metafield_products.list operation"""
    product_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldOrdersListParams(TypedDict):
    """Parameters for metafield_orders.list operation"""
    order_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldDraftOrdersListParams(TypedDict):
    """Parameters for metafield_draft_orders.list operation"""
    draft_order_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldLocationsListParams(TypedDict):
    """Parameters for metafield_locations.list operation"""
    location_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldProductVariantsListParams(TypedDict):
    """Parameters for metafield_product_variants.list operation"""
    variant_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldSmartCollectionsListParams(TypedDict):
    """Parameters for metafield_smart_collections.list operation"""
    collection_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldProductImagesListParams(TypedDict):
    """Parameters for metafield_product_images.list operation"""
    product_id: str
    image_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class CustomerAddressListParams(TypedDict):
    """Parameters for customer_address.list operation"""
    customer_id: str
    limit: NotRequired[int]

class CustomerAddressGetParams(TypedDict):
    """Parameters for customer_address.get operation"""
    customer_id: str
    address_id: str

class FulfillmentOrdersListParams(TypedDict):
    """Parameters for fulfillment_orders.list operation"""
    order_id: str

class FulfillmentOrdersGetParams(TypedDict):
    """Parameters for fulfillment_orders.get operation"""
    fulfillment_order_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ABANDONED_CHECKOUTS SEARCH TYPES =====

class AbandonedCheckoutsSearchFilter(TypedDict, total=False):
    """Available fields for filtering abandoned_checkouts search queries."""


class AbandonedCheckoutsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class AbandonedCheckoutsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class AbandonedCheckoutsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class AbandonedCheckoutsSortFilter(TypedDict, total=False):
    """Available fields for sorting abandoned_checkouts search results."""


# Entity-specific condition types for abandoned_checkouts
class AbandonedCheckoutsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AbandonedCheckoutsStringFilter


class AbandonedCheckoutsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AbandonedCheckoutsStringFilter


class AbandonedCheckoutsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AbandonedCheckoutsStringFilter


class AbandonedCheckoutsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AbandonedCheckoutsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AbandonedCheckoutsInCondition = TypedDict("AbandonedCheckoutsInCondition", {"in": AbandonedCheckoutsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AbandonedCheckoutsNotCondition = TypedDict("AbandonedCheckoutsNotCondition", {"not": "AbandonedCheckoutsCondition"}, total=False)
"""Negates the nested condition."""

AbandonedCheckoutsAndCondition = TypedDict("AbandonedCheckoutsAndCondition", {"and": "list[AbandonedCheckoutsCondition]"}, total=False)
"""True if all nested conditions are true."""

AbandonedCheckoutsOrCondition = TypedDict("AbandonedCheckoutsOrCondition", {"or": "list[AbandonedCheckoutsCondition]"}, total=False)
"""True if any nested condition is true."""

AbandonedCheckoutsAnyCondition = TypedDict("AbandonedCheckoutsAnyCondition", {"any": AbandonedCheckoutsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all abandoned_checkouts condition types
AbandonedCheckoutsCondition = (
    AbandonedCheckoutsEqCondition
    | AbandonedCheckoutsNeqCondition
    | AbandonedCheckoutsGtCondition
    | AbandonedCheckoutsGteCondition
    | AbandonedCheckoutsLtCondition
    | AbandonedCheckoutsLteCondition
    | AbandonedCheckoutsInCondition
    | AbandonedCheckoutsLikeCondition
    | AbandonedCheckoutsFuzzyCondition
    | AbandonedCheckoutsKeywordCondition
    | AbandonedCheckoutsContainsCondition
    | AbandonedCheckoutsNotCondition
    | AbandonedCheckoutsAndCondition
    | AbandonedCheckoutsOrCondition
    | AbandonedCheckoutsAnyCondition
)


class AbandonedCheckoutsSearchQuery(TypedDict, total=False):
    """Search query for abandoned_checkouts entity."""
    filter: AbandonedCheckoutsCondition
    sort: list[AbandonedCheckoutsSortFilter]


# ===== COLLECTS SEARCH TYPES =====

class CollectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering collects search queries."""


class CollectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class CollectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class CollectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class CollectsSortFilter(TypedDict, total=False):
    """Available fields for sorting collects search results."""


# Entity-specific condition types for collects
class CollectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CollectsSearchFilter


class CollectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CollectsSearchFilter


class CollectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CollectsSearchFilter


class CollectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CollectsSearchFilter


class CollectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CollectsSearchFilter


class CollectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CollectsSearchFilter


class CollectsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CollectsStringFilter


class CollectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CollectsStringFilter


class CollectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CollectsStringFilter


class CollectsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CollectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CollectsInCondition = TypedDict("CollectsInCondition", {"in": CollectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CollectsNotCondition = TypedDict("CollectsNotCondition", {"not": "CollectsCondition"}, total=False)
"""Negates the nested condition."""

CollectsAndCondition = TypedDict("CollectsAndCondition", {"and": "list[CollectsCondition]"}, total=False)
"""True if all nested conditions are true."""

CollectsOrCondition = TypedDict("CollectsOrCondition", {"or": "list[CollectsCondition]"}, total=False)
"""True if any nested condition is true."""

CollectsAnyCondition = TypedDict("CollectsAnyCondition", {"any": CollectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all collects condition types
CollectsCondition = (
    CollectsEqCondition
    | CollectsNeqCondition
    | CollectsGtCondition
    | CollectsGteCondition
    | CollectsLtCondition
    | CollectsLteCondition
    | CollectsInCondition
    | CollectsLikeCondition
    | CollectsFuzzyCondition
    | CollectsKeywordCondition
    | CollectsContainsCondition
    | CollectsNotCondition
    | CollectsAndCondition
    | CollectsOrCondition
    | CollectsAnyCondition
)


class CollectsSearchQuery(TypedDict, total=False):
    """Search query for collects entity."""
    filter: CollectsCondition
    sort: list[CollectsSortFilter]


# ===== COUNTRIES SEARCH TYPES =====

class CountriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering countries search queries."""


class CountriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class CountriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class CountriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class CountriesSortFilter(TypedDict, total=False):
    """Available fields for sorting countries search results."""


# Entity-specific condition types for countries
class CountriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CountriesSearchFilter


class CountriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CountriesSearchFilter


class CountriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CountriesSearchFilter


class CountriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CountriesSearchFilter


class CountriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CountriesSearchFilter


class CountriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CountriesSearchFilter


class CountriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CountriesStringFilter


class CountriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CountriesStringFilter


class CountriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CountriesStringFilter


class CountriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CountriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CountriesInCondition = TypedDict("CountriesInCondition", {"in": CountriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CountriesNotCondition = TypedDict("CountriesNotCondition", {"not": "CountriesCondition"}, total=False)
"""Negates the nested condition."""

CountriesAndCondition = TypedDict("CountriesAndCondition", {"and": "list[CountriesCondition]"}, total=False)
"""True if all nested conditions are true."""

CountriesOrCondition = TypedDict("CountriesOrCondition", {"or": "list[CountriesCondition]"}, total=False)
"""True if any nested condition is true."""

CountriesAnyCondition = TypedDict("CountriesAnyCondition", {"any": CountriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all countries condition types
CountriesCondition = (
    CountriesEqCondition
    | CountriesNeqCondition
    | CountriesGtCondition
    | CountriesGteCondition
    | CountriesLtCondition
    | CountriesLteCondition
    | CountriesInCondition
    | CountriesLikeCondition
    | CountriesFuzzyCondition
    | CountriesKeywordCondition
    | CountriesContainsCondition
    | CountriesNotCondition
    | CountriesAndCondition
    | CountriesOrCondition
    | CountriesAnyCondition
)


class CountriesSearchQuery(TypedDict, total=False):
    """Search query for countries entity."""
    filter: CountriesCondition
    sort: list[CountriesSortFilter]


# ===== CUSTOM_COLLECTIONS SEARCH TYPES =====

class CustomCollectionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering custom_collections search queries."""


class CustomCollectionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class CustomCollectionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class CustomCollectionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class CustomCollectionsSortFilter(TypedDict, total=False):
    """Available fields for sorting custom_collections search results."""


# Entity-specific condition types for custom_collections
class CustomCollectionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomCollectionsSearchFilter


class CustomCollectionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomCollectionsSearchFilter


class CustomCollectionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomCollectionsSearchFilter


class CustomCollectionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomCollectionsSearchFilter


class CustomCollectionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomCollectionsSearchFilter


class CustomCollectionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomCollectionsSearchFilter


class CustomCollectionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomCollectionsStringFilter


class CustomCollectionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomCollectionsStringFilter


class CustomCollectionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomCollectionsStringFilter


class CustomCollectionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomCollectionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomCollectionsInCondition = TypedDict("CustomCollectionsInCondition", {"in": CustomCollectionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomCollectionsNotCondition = TypedDict("CustomCollectionsNotCondition", {"not": "CustomCollectionsCondition"}, total=False)
"""Negates the nested condition."""

CustomCollectionsAndCondition = TypedDict("CustomCollectionsAndCondition", {"and": "list[CustomCollectionsCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomCollectionsOrCondition = TypedDict("CustomCollectionsOrCondition", {"or": "list[CustomCollectionsCondition]"}, total=False)
"""True if any nested condition is true."""

CustomCollectionsAnyCondition = TypedDict("CustomCollectionsAnyCondition", {"any": CustomCollectionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all custom_collections condition types
CustomCollectionsCondition = (
    CustomCollectionsEqCondition
    | CustomCollectionsNeqCondition
    | CustomCollectionsGtCondition
    | CustomCollectionsGteCondition
    | CustomCollectionsLtCondition
    | CustomCollectionsLteCondition
    | CustomCollectionsInCondition
    | CustomCollectionsLikeCondition
    | CustomCollectionsFuzzyCondition
    | CustomCollectionsKeywordCondition
    | CustomCollectionsContainsCondition
    | CustomCollectionsNotCondition
    | CustomCollectionsAndCondition
    | CustomCollectionsOrCondition
    | CustomCollectionsAnyCondition
)


class CustomCollectionsSearchQuery(TypedDict, total=False):
    """Search query for custom_collections entity."""
    filter: CustomCollectionsCondition
    sort: list[CustomCollectionsSortFilter]


# ===== CUSTOMERS SEARCH TYPES =====

class CustomersSearchFilter(TypedDict, total=False):
    """Available fields for filtering customers search queries."""


class CustomersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class CustomersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class CustomersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class CustomersSortFilter(TypedDict, total=False):
    """Available fields for sorting customers search results."""


# Entity-specific condition types for customers
class CustomersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomersSearchFilter


class CustomersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomersSearchFilter


class CustomersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomersSearchFilter


class CustomersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomersSearchFilter


class CustomersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomersSearchFilter


class CustomersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomersSearchFilter


class CustomersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomersStringFilter


class CustomersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomersStringFilter


class CustomersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomersStringFilter


class CustomersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomersInCondition = TypedDict("CustomersInCondition", {"in": CustomersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomersNotCondition = TypedDict("CustomersNotCondition", {"not": "CustomersCondition"}, total=False)
"""Negates the nested condition."""

CustomersAndCondition = TypedDict("CustomersAndCondition", {"and": "list[CustomersCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomersOrCondition = TypedDict("CustomersOrCondition", {"or": "list[CustomersCondition]"}, total=False)
"""True if any nested condition is true."""

CustomersAnyCondition = TypedDict("CustomersAnyCondition", {"any": CustomersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all customers condition types
CustomersCondition = (
    CustomersEqCondition
    | CustomersNeqCondition
    | CustomersGtCondition
    | CustomersGteCondition
    | CustomersLtCondition
    | CustomersLteCondition
    | CustomersInCondition
    | CustomersLikeCondition
    | CustomersFuzzyCondition
    | CustomersKeywordCondition
    | CustomersContainsCondition
    | CustomersNotCondition
    | CustomersAndCondition
    | CustomersOrCondition
    | CustomersAnyCondition
)


class CustomersSearchQuery(TypedDict, total=False):
    """Search query for customers entity."""
    filter: CustomersCondition
    sort: list[CustomersSortFilter]


# ===== DISCOUNT_CODES SEARCH TYPES =====

class DiscountCodesSearchFilter(TypedDict, total=False):
    """Available fields for filtering discount_codes search queries."""


class DiscountCodesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class DiscountCodesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class DiscountCodesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class DiscountCodesSortFilter(TypedDict, total=False):
    """Available fields for sorting discount_codes search results."""


# Entity-specific condition types for discount_codes
class DiscountCodesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DiscountCodesSearchFilter


class DiscountCodesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DiscountCodesSearchFilter


class DiscountCodesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DiscountCodesSearchFilter


class DiscountCodesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DiscountCodesSearchFilter


class DiscountCodesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DiscountCodesSearchFilter


class DiscountCodesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DiscountCodesSearchFilter


class DiscountCodesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DiscountCodesStringFilter


class DiscountCodesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DiscountCodesStringFilter


class DiscountCodesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DiscountCodesStringFilter


class DiscountCodesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DiscountCodesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DiscountCodesInCondition = TypedDict("DiscountCodesInCondition", {"in": DiscountCodesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DiscountCodesNotCondition = TypedDict("DiscountCodesNotCondition", {"not": "DiscountCodesCondition"}, total=False)
"""Negates the nested condition."""

DiscountCodesAndCondition = TypedDict("DiscountCodesAndCondition", {"and": "list[DiscountCodesCondition]"}, total=False)
"""True if all nested conditions are true."""

DiscountCodesOrCondition = TypedDict("DiscountCodesOrCondition", {"or": "list[DiscountCodesCondition]"}, total=False)
"""True if any nested condition is true."""

DiscountCodesAnyCondition = TypedDict("DiscountCodesAnyCondition", {"any": DiscountCodesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all discount_codes condition types
DiscountCodesCondition = (
    DiscountCodesEqCondition
    | DiscountCodesNeqCondition
    | DiscountCodesGtCondition
    | DiscountCodesGteCondition
    | DiscountCodesLtCondition
    | DiscountCodesLteCondition
    | DiscountCodesInCondition
    | DiscountCodesLikeCondition
    | DiscountCodesFuzzyCondition
    | DiscountCodesKeywordCondition
    | DiscountCodesContainsCondition
    | DiscountCodesNotCondition
    | DiscountCodesAndCondition
    | DiscountCodesOrCondition
    | DiscountCodesAnyCondition
)


class DiscountCodesSearchQuery(TypedDict, total=False):
    """Search query for discount_codes entity."""
    filter: DiscountCodesCondition
    sort: list[DiscountCodesSortFilter]


# ===== DRAFT_ORDERS SEARCH TYPES =====

class DraftOrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering draft_orders search queries."""


class DraftOrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class DraftOrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class DraftOrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class DraftOrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting draft_orders search results."""


# Entity-specific condition types for draft_orders
class DraftOrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DraftOrdersSearchFilter


class DraftOrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DraftOrdersSearchFilter


class DraftOrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DraftOrdersSearchFilter


class DraftOrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DraftOrdersSearchFilter


class DraftOrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DraftOrdersSearchFilter


class DraftOrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DraftOrdersSearchFilter


class DraftOrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DraftOrdersStringFilter


class DraftOrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DraftOrdersStringFilter


class DraftOrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DraftOrdersStringFilter


class DraftOrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DraftOrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DraftOrdersInCondition = TypedDict("DraftOrdersInCondition", {"in": DraftOrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DraftOrdersNotCondition = TypedDict("DraftOrdersNotCondition", {"not": "DraftOrdersCondition"}, total=False)
"""Negates the nested condition."""

DraftOrdersAndCondition = TypedDict("DraftOrdersAndCondition", {"and": "list[DraftOrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

DraftOrdersOrCondition = TypedDict("DraftOrdersOrCondition", {"or": "list[DraftOrdersCondition]"}, total=False)
"""True if any nested condition is true."""

DraftOrdersAnyCondition = TypedDict("DraftOrdersAnyCondition", {"any": DraftOrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all draft_orders condition types
DraftOrdersCondition = (
    DraftOrdersEqCondition
    | DraftOrdersNeqCondition
    | DraftOrdersGtCondition
    | DraftOrdersGteCondition
    | DraftOrdersLtCondition
    | DraftOrdersLteCondition
    | DraftOrdersInCondition
    | DraftOrdersLikeCondition
    | DraftOrdersFuzzyCondition
    | DraftOrdersKeywordCondition
    | DraftOrdersContainsCondition
    | DraftOrdersNotCondition
    | DraftOrdersAndCondition
    | DraftOrdersOrCondition
    | DraftOrdersAnyCondition
)


class DraftOrdersSearchQuery(TypedDict, total=False):
    """Search query for draft_orders entity."""
    filter: DraftOrdersCondition
    sort: list[DraftOrdersSortFilter]


# ===== FULFILLMENT_ORDERS SEARCH TYPES =====

class FulfillmentOrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering fulfillment_orders search queries."""


class FulfillmentOrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class FulfillmentOrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class FulfillmentOrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class FulfillmentOrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting fulfillment_orders search results."""


# Entity-specific condition types for fulfillment_orders
class FulfillmentOrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FulfillmentOrdersSearchFilter


class FulfillmentOrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FulfillmentOrdersSearchFilter


class FulfillmentOrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FulfillmentOrdersSearchFilter


class FulfillmentOrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FulfillmentOrdersSearchFilter


class FulfillmentOrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FulfillmentOrdersSearchFilter


class FulfillmentOrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FulfillmentOrdersSearchFilter


class FulfillmentOrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FulfillmentOrdersStringFilter


class FulfillmentOrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FulfillmentOrdersStringFilter


class FulfillmentOrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FulfillmentOrdersStringFilter


class FulfillmentOrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FulfillmentOrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FulfillmentOrdersInCondition = TypedDict("FulfillmentOrdersInCondition", {"in": FulfillmentOrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FulfillmentOrdersNotCondition = TypedDict("FulfillmentOrdersNotCondition", {"not": "FulfillmentOrdersCondition"}, total=False)
"""Negates the nested condition."""

FulfillmentOrdersAndCondition = TypedDict("FulfillmentOrdersAndCondition", {"and": "list[FulfillmentOrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

FulfillmentOrdersOrCondition = TypedDict("FulfillmentOrdersOrCondition", {"or": "list[FulfillmentOrdersCondition]"}, total=False)
"""True if any nested condition is true."""

FulfillmentOrdersAnyCondition = TypedDict("FulfillmentOrdersAnyCondition", {"any": FulfillmentOrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all fulfillment_orders condition types
FulfillmentOrdersCondition = (
    FulfillmentOrdersEqCondition
    | FulfillmentOrdersNeqCondition
    | FulfillmentOrdersGtCondition
    | FulfillmentOrdersGteCondition
    | FulfillmentOrdersLtCondition
    | FulfillmentOrdersLteCondition
    | FulfillmentOrdersInCondition
    | FulfillmentOrdersLikeCondition
    | FulfillmentOrdersFuzzyCondition
    | FulfillmentOrdersKeywordCondition
    | FulfillmentOrdersContainsCondition
    | FulfillmentOrdersNotCondition
    | FulfillmentOrdersAndCondition
    | FulfillmentOrdersOrCondition
    | FulfillmentOrdersAnyCondition
)


class FulfillmentOrdersSearchQuery(TypedDict, total=False):
    """Search query for fulfillment_orders entity."""
    filter: FulfillmentOrdersCondition
    sort: list[FulfillmentOrdersSortFilter]


# ===== FULFILLMENTS SEARCH TYPES =====

class FulfillmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering fulfillments search queries."""


class FulfillmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class FulfillmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class FulfillmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class FulfillmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting fulfillments search results."""


# Entity-specific condition types for fulfillments
class FulfillmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FulfillmentsSearchFilter


class FulfillmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FulfillmentsSearchFilter


class FulfillmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FulfillmentsSearchFilter


class FulfillmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FulfillmentsSearchFilter


class FulfillmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FulfillmentsSearchFilter


class FulfillmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FulfillmentsSearchFilter


class FulfillmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FulfillmentsStringFilter


class FulfillmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FulfillmentsStringFilter


class FulfillmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FulfillmentsStringFilter


class FulfillmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FulfillmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FulfillmentsInCondition = TypedDict("FulfillmentsInCondition", {"in": FulfillmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FulfillmentsNotCondition = TypedDict("FulfillmentsNotCondition", {"not": "FulfillmentsCondition"}, total=False)
"""Negates the nested condition."""

FulfillmentsAndCondition = TypedDict("FulfillmentsAndCondition", {"and": "list[FulfillmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

FulfillmentsOrCondition = TypedDict("FulfillmentsOrCondition", {"or": "list[FulfillmentsCondition]"}, total=False)
"""True if any nested condition is true."""

FulfillmentsAnyCondition = TypedDict("FulfillmentsAnyCondition", {"any": FulfillmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all fulfillments condition types
FulfillmentsCondition = (
    FulfillmentsEqCondition
    | FulfillmentsNeqCondition
    | FulfillmentsGtCondition
    | FulfillmentsGteCondition
    | FulfillmentsLtCondition
    | FulfillmentsLteCondition
    | FulfillmentsInCondition
    | FulfillmentsLikeCondition
    | FulfillmentsFuzzyCondition
    | FulfillmentsKeywordCondition
    | FulfillmentsContainsCondition
    | FulfillmentsNotCondition
    | FulfillmentsAndCondition
    | FulfillmentsOrCondition
    | FulfillmentsAnyCondition
)


class FulfillmentsSearchQuery(TypedDict, total=False):
    """Search query for fulfillments entity."""
    filter: FulfillmentsCondition
    sort: list[FulfillmentsSortFilter]


# ===== INVENTORY_ITEMS SEARCH TYPES =====

class InventoryItemsSearchFilter(TypedDict, total=False):
    """Available fields for filtering inventory_items search queries."""


class InventoryItemsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class InventoryItemsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class InventoryItemsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class InventoryItemsSortFilter(TypedDict, total=False):
    """Available fields for sorting inventory_items search results."""


# Entity-specific condition types for inventory_items
class InventoryItemsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InventoryItemsSearchFilter


class InventoryItemsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InventoryItemsSearchFilter


class InventoryItemsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InventoryItemsSearchFilter


class InventoryItemsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InventoryItemsSearchFilter


class InventoryItemsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InventoryItemsSearchFilter


class InventoryItemsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InventoryItemsSearchFilter


class InventoryItemsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: InventoryItemsStringFilter


class InventoryItemsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InventoryItemsStringFilter


class InventoryItemsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InventoryItemsStringFilter


class InventoryItemsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: InventoryItemsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InventoryItemsInCondition = TypedDict("InventoryItemsInCondition", {"in": InventoryItemsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InventoryItemsNotCondition = TypedDict("InventoryItemsNotCondition", {"not": "InventoryItemsCondition"}, total=False)
"""Negates the nested condition."""

InventoryItemsAndCondition = TypedDict("InventoryItemsAndCondition", {"and": "list[InventoryItemsCondition]"}, total=False)
"""True if all nested conditions are true."""

InventoryItemsOrCondition = TypedDict("InventoryItemsOrCondition", {"or": "list[InventoryItemsCondition]"}, total=False)
"""True if any nested condition is true."""

InventoryItemsAnyCondition = TypedDict("InventoryItemsAnyCondition", {"any": InventoryItemsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all inventory_items condition types
InventoryItemsCondition = (
    InventoryItemsEqCondition
    | InventoryItemsNeqCondition
    | InventoryItemsGtCondition
    | InventoryItemsGteCondition
    | InventoryItemsLtCondition
    | InventoryItemsLteCondition
    | InventoryItemsInCondition
    | InventoryItemsLikeCondition
    | InventoryItemsFuzzyCondition
    | InventoryItemsKeywordCondition
    | InventoryItemsContainsCondition
    | InventoryItemsNotCondition
    | InventoryItemsAndCondition
    | InventoryItemsOrCondition
    | InventoryItemsAnyCondition
)


class InventoryItemsSearchQuery(TypedDict, total=False):
    """Search query for inventory_items entity."""
    filter: InventoryItemsCondition
    sort: list[InventoryItemsSortFilter]


# ===== INVENTORY_LEVELS SEARCH TYPES =====

class InventoryLevelsSearchFilter(TypedDict, total=False):
    """Available fields for filtering inventory_levels search queries."""


class InventoryLevelsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class InventoryLevelsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class InventoryLevelsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class InventoryLevelsSortFilter(TypedDict, total=False):
    """Available fields for sorting inventory_levels search results."""


# Entity-specific condition types for inventory_levels
class InventoryLevelsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InventoryLevelsSearchFilter


class InventoryLevelsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InventoryLevelsSearchFilter


class InventoryLevelsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InventoryLevelsSearchFilter


class InventoryLevelsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InventoryLevelsSearchFilter


class InventoryLevelsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InventoryLevelsSearchFilter


class InventoryLevelsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InventoryLevelsSearchFilter


class InventoryLevelsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: InventoryLevelsStringFilter


class InventoryLevelsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InventoryLevelsStringFilter


class InventoryLevelsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InventoryLevelsStringFilter


class InventoryLevelsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: InventoryLevelsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InventoryLevelsInCondition = TypedDict("InventoryLevelsInCondition", {"in": InventoryLevelsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InventoryLevelsNotCondition = TypedDict("InventoryLevelsNotCondition", {"not": "InventoryLevelsCondition"}, total=False)
"""Negates the nested condition."""

InventoryLevelsAndCondition = TypedDict("InventoryLevelsAndCondition", {"and": "list[InventoryLevelsCondition]"}, total=False)
"""True if all nested conditions are true."""

InventoryLevelsOrCondition = TypedDict("InventoryLevelsOrCondition", {"or": "list[InventoryLevelsCondition]"}, total=False)
"""True if any nested condition is true."""

InventoryLevelsAnyCondition = TypedDict("InventoryLevelsAnyCondition", {"any": InventoryLevelsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all inventory_levels condition types
InventoryLevelsCondition = (
    InventoryLevelsEqCondition
    | InventoryLevelsNeqCondition
    | InventoryLevelsGtCondition
    | InventoryLevelsGteCondition
    | InventoryLevelsLtCondition
    | InventoryLevelsLteCondition
    | InventoryLevelsInCondition
    | InventoryLevelsLikeCondition
    | InventoryLevelsFuzzyCondition
    | InventoryLevelsKeywordCondition
    | InventoryLevelsContainsCondition
    | InventoryLevelsNotCondition
    | InventoryLevelsAndCondition
    | InventoryLevelsOrCondition
    | InventoryLevelsAnyCondition
)


class InventoryLevelsSearchQuery(TypedDict, total=False):
    """Search query for inventory_levels entity."""
    filter: InventoryLevelsCondition
    sort: list[InventoryLevelsSortFilter]


# ===== LOCATIONS SEARCH TYPES =====

class LocationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering locations search queries."""


class LocationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class LocationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class LocationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class LocationsSortFilter(TypedDict, total=False):
    """Available fields for sorting locations search results."""


# Entity-specific condition types for locations
class LocationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LocationsSearchFilter


class LocationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LocationsSearchFilter


class LocationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LocationsSearchFilter


class LocationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LocationsSearchFilter


class LocationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LocationsSearchFilter


class LocationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LocationsSearchFilter


class LocationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: LocationsStringFilter


class LocationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LocationsStringFilter


class LocationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LocationsStringFilter


class LocationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: LocationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LocationsInCondition = TypedDict("LocationsInCondition", {"in": LocationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LocationsNotCondition = TypedDict("LocationsNotCondition", {"not": "LocationsCondition"}, total=False)
"""Negates the nested condition."""

LocationsAndCondition = TypedDict("LocationsAndCondition", {"and": "list[LocationsCondition]"}, total=False)
"""True if all nested conditions are true."""

LocationsOrCondition = TypedDict("LocationsOrCondition", {"or": "list[LocationsCondition]"}, total=False)
"""True if any nested condition is true."""

LocationsAnyCondition = TypedDict("LocationsAnyCondition", {"any": LocationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all locations condition types
LocationsCondition = (
    LocationsEqCondition
    | LocationsNeqCondition
    | LocationsGtCondition
    | LocationsGteCondition
    | LocationsLtCondition
    | LocationsLteCondition
    | LocationsInCondition
    | LocationsLikeCondition
    | LocationsFuzzyCondition
    | LocationsKeywordCondition
    | LocationsContainsCondition
    | LocationsNotCondition
    | LocationsAndCondition
    | LocationsOrCondition
    | LocationsAnyCondition
)


class LocationsSearchQuery(TypedDict, total=False):
    """Search query for locations entity."""
    filter: LocationsCondition
    sort: list[LocationsSortFilter]


# ===== METAFIELD_CUSTOMERS SEARCH TYPES =====

class MetafieldCustomersSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_customers search queries."""


class MetafieldCustomersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldCustomersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldCustomersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldCustomersSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_customers search results."""


# Entity-specific condition types for metafield_customers
class MetafieldCustomersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldCustomersSearchFilter


class MetafieldCustomersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldCustomersSearchFilter


class MetafieldCustomersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldCustomersSearchFilter


class MetafieldCustomersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldCustomersSearchFilter


class MetafieldCustomersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldCustomersSearchFilter


class MetafieldCustomersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldCustomersSearchFilter


class MetafieldCustomersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldCustomersStringFilter


class MetafieldCustomersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldCustomersStringFilter


class MetafieldCustomersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldCustomersStringFilter


class MetafieldCustomersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldCustomersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldCustomersInCondition = TypedDict("MetafieldCustomersInCondition", {"in": MetafieldCustomersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldCustomersNotCondition = TypedDict("MetafieldCustomersNotCondition", {"not": "MetafieldCustomersCondition"}, total=False)
"""Negates the nested condition."""

MetafieldCustomersAndCondition = TypedDict("MetafieldCustomersAndCondition", {"and": "list[MetafieldCustomersCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldCustomersOrCondition = TypedDict("MetafieldCustomersOrCondition", {"or": "list[MetafieldCustomersCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldCustomersAnyCondition = TypedDict("MetafieldCustomersAnyCondition", {"any": MetafieldCustomersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_customers condition types
MetafieldCustomersCondition = (
    MetafieldCustomersEqCondition
    | MetafieldCustomersNeqCondition
    | MetafieldCustomersGtCondition
    | MetafieldCustomersGteCondition
    | MetafieldCustomersLtCondition
    | MetafieldCustomersLteCondition
    | MetafieldCustomersInCondition
    | MetafieldCustomersLikeCondition
    | MetafieldCustomersFuzzyCondition
    | MetafieldCustomersKeywordCondition
    | MetafieldCustomersContainsCondition
    | MetafieldCustomersNotCondition
    | MetafieldCustomersAndCondition
    | MetafieldCustomersOrCondition
    | MetafieldCustomersAnyCondition
)


class MetafieldCustomersSearchQuery(TypedDict, total=False):
    """Search query for metafield_customers entity."""
    filter: MetafieldCustomersCondition
    sort: list[MetafieldCustomersSortFilter]


# ===== METAFIELD_DRAFT_ORDERS SEARCH TYPES =====

class MetafieldDraftOrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_draft_orders search queries."""


class MetafieldDraftOrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldDraftOrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldDraftOrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldDraftOrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_draft_orders search results."""


# Entity-specific condition types for metafield_draft_orders
class MetafieldDraftOrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldDraftOrdersStringFilter


class MetafieldDraftOrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldDraftOrdersStringFilter


class MetafieldDraftOrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldDraftOrdersStringFilter


class MetafieldDraftOrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldDraftOrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldDraftOrdersInCondition = TypedDict("MetafieldDraftOrdersInCondition", {"in": MetafieldDraftOrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldDraftOrdersNotCondition = TypedDict("MetafieldDraftOrdersNotCondition", {"not": "MetafieldDraftOrdersCondition"}, total=False)
"""Negates the nested condition."""

MetafieldDraftOrdersAndCondition = TypedDict("MetafieldDraftOrdersAndCondition", {"and": "list[MetafieldDraftOrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldDraftOrdersOrCondition = TypedDict("MetafieldDraftOrdersOrCondition", {"or": "list[MetafieldDraftOrdersCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldDraftOrdersAnyCondition = TypedDict("MetafieldDraftOrdersAnyCondition", {"any": MetafieldDraftOrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_draft_orders condition types
MetafieldDraftOrdersCondition = (
    MetafieldDraftOrdersEqCondition
    | MetafieldDraftOrdersNeqCondition
    | MetafieldDraftOrdersGtCondition
    | MetafieldDraftOrdersGteCondition
    | MetafieldDraftOrdersLtCondition
    | MetafieldDraftOrdersLteCondition
    | MetafieldDraftOrdersInCondition
    | MetafieldDraftOrdersLikeCondition
    | MetafieldDraftOrdersFuzzyCondition
    | MetafieldDraftOrdersKeywordCondition
    | MetafieldDraftOrdersContainsCondition
    | MetafieldDraftOrdersNotCondition
    | MetafieldDraftOrdersAndCondition
    | MetafieldDraftOrdersOrCondition
    | MetafieldDraftOrdersAnyCondition
)


class MetafieldDraftOrdersSearchQuery(TypedDict, total=False):
    """Search query for metafield_draft_orders entity."""
    filter: MetafieldDraftOrdersCondition
    sort: list[MetafieldDraftOrdersSortFilter]


# ===== METAFIELD_LOCATIONS SEARCH TYPES =====

class MetafieldLocationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_locations search queries."""


class MetafieldLocationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldLocationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldLocationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldLocationsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_locations search results."""


# Entity-specific condition types for metafield_locations
class MetafieldLocationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldLocationsSearchFilter


class MetafieldLocationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldLocationsSearchFilter


class MetafieldLocationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldLocationsSearchFilter


class MetafieldLocationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldLocationsSearchFilter


class MetafieldLocationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldLocationsSearchFilter


class MetafieldLocationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldLocationsSearchFilter


class MetafieldLocationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldLocationsStringFilter


class MetafieldLocationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldLocationsStringFilter


class MetafieldLocationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldLocationsStringFilter


class MetafieldLocationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldLocationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldLocationsInCondition = TypedDict("MetafieldLocationsInCondition", {"in": MetafieldLocationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldLocationsNotCondition = TypedDict("MetafieldLocationsNotCondition", {"not": "MetafieldLocationsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldLocationsAndCondition = TypedDict("MetafieldLocationsAndCondition", {"and": "list[MetafieldLocationsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldLocationsOrCondition = TypedDict("MetafieldLocationsOrCondition", {"or": "list[MetafieldLocationsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldLocationsAnyCondition = TypedDict("MetafieldLocationsAnyCondition", {"any": MetafieldLocationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_locations condition types
MetafieldLocationsCondition = (
    MetafieldLocationsEqCondition
    | MetafieldLocationsNeqCondition
    | MetafieldLocationsGtCondition
    | MetafieldLocationsGteCondition
    | MetafieldLocationsLtCondition
    | MetafieldLocationsLteCondition
    | MetafieldLocationsInCondition
    | MetafieldLocationsLikeCondition
    | MetafieldLocationsFuzzyCondition
    | MetafieldLocationsKeywordCondition
    | MetafieldLocationsContainsCondition
    | MetafieldLocationsNotCondition
    | MetafieldLocationsAndCondition
    | MetafieldLocationsOrCondition
    | MetafieldLocationsAnyCondition
)


class MetafieldLocationsSearchQuery(TypedDict, total=False):
    """Search query for metafield_locations entity."""
    filter: MetafieldLocationsCondition
    sort: list[MetafieldLocationsSortFilter]


# ===== METAFIELD_ORDERS SEARCH TYPES =====

class MetafieldOrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_orders search queries."""


class MetafieldOrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldOrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldOrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldOrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_orders search results."""


# Entity-specific condition types for metafield_orders
class MetafieldOrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldOrdersSearchFilter


class MetafieldOrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldOrdersSearchFilter


class MetafieldOrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldOrdersSearchFilter


class MetafieldOrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldOrdersSearchFilter


class MetafieldOrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldOrdersSearchFilter


class MetafieldOrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldOrdersSearchFilter


class MetafieldOrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldOrdersStringFilter


class MetafieldOrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldOrdersStringFilter


class MetafieldOrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldOrdersStringFilter


class MetafieldOrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldOrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldOrdersInCondition = TypedDict("MetafieldOrdersInCondition", {"in": MetafieldOrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldOrdersNotCondition = TypedDict("MetafieldOrdersNotCondition", {"not": "MetafieldOrdersCondition"}, total=False)
"""Negates the nested condition."""

MetafieldOrdersAndCondition = TypedDict("MetafieldOrdersAndCondition", {"and": "list[MetafieldOrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldOrdersOrCondition = TypedDict("MetafieldOrdersOrCondition", {"or": "list[MetafieldOrdersCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldOrdersAnyCondition = TypedDict("MetafieldOrdersAnyCondition", {"any": MetafieldOrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_orders condition types
MetafieldOrdersCondition = (
    MetafieldOrdersEqCondition
    | MetafieldOrdersNeqCondition
    | MetafieldOrdersGtCondition
    | MetafieldOrdersGteCondition
    | MetafieldOrdersLtCondition
    | MetafieldOrdersLteCondition
    | MetafieldOrdersInCondition
    | MetafieldOrdersLikeCondition
    | MetafieldOrdersFuzzyCondition
    | MetafieldOrdersKeywordCondition
    | MetafieldOrdersContainsCondition
    | MetafieldOrdersNotCondition
    | MetafieldOrdersAndCondition
    | MetafieldOrdersOrCondition
    | MetafieldOrdersAnyCondition
)


class MetafieldOrdersSearchQuery(TypedDict, total=False):
    """Search query for metafield_orders entity."""
    filter: MetafieldOrdersCondition
    sort: list[MetafieldOrdersSortFilter]


# ===== METAFIELD_PRODUCT_IMAGES SEARCH TYPES =====

class MetafieldProductImagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_product_images search queries."""


class MetafieldProductImagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldProductImagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldProductImagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldProductImagesSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_product_images search results."""


# Entity-specific condition types for metafield_product_images
class MetafieldProductImagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldProductImagesSearchFilter


class MetafieldProductImagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldProductImagesSearchFilter


class MetafieldProductImagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldProductImagesSearchFilter


class MetafieldProductImagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldProductImagesSearchFilter


class MetafieldProductImagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldProductImagesSearchFilter


class MetafieldProductImagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldProductImagesSearchFilter


class MetafieldProductImagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldProductImagesStringFilter


class MetafieldProductImagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldProductImagesStringFilter


class MetafieldProductImagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldProductImagesStringFilter


class MetafieldProductImagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldProductImagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldProductImagesInCondition = TypedDict("MetafieldProductImagesInCondition", {"in": MetafieldProductImagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldProductImagesNotCondition = TypedDict("MetafieldProductImagesNotCondition", {"not": "MetafieldProductImagesCondition"}, total=False)
"""Negates the nested condition."""

MetafieldProductImagesAndCondition = TypedDict("MetafieldProductImagesAndCondition", {"and": "list[MetafieldProductImagesCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldProductImagesOrCondition = TypedDict("MetafieldProductImagesOrCondition", {"or": "list[MetafieldProductImagesCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldProductImagesAnyCondition = TypedDict("MetafieldProductImagesAnyCondition", {"any": MetafieldProductImagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_product_images condition types
MetafieldProductImagesCondition = (
    MetafieldProductImagesEqCondition
    | MetafieldProductImagesNeqCondition
    | MetafieldProductImagesGtCondition
    | MetafieldProductImagesGteCondition
    | MetafieldProductImagesLtCondition
    | MetafieldProductImagesLteCondition
    | MetafieldProductImagesInCondition
    | MetafieldProductImagesLikeCondition
    | MetafieldProductImagesFuzzyCondition
    | MetafieldProductImagesKeywordCondition
    | MetafieldProductImagesContainsCondition
    | MetafieldProductImagesNotCondition
    | MetafieldProductImagesAndCondition
    | MetafieldProductImagesOrCondition
    | MetafieldProductImagesAnyCondition
)


class MetafieldProductImagesSearchQuery(TypedDict, total=False):
    """Search query for metafield_product_images entity."""
    filter: MetafieldProductImagesCondition
    sort: list[MetafieldProductImagesSortFilter]


# ===== METAFIELD_PRODUCT_VARIANTS SEARCH TYPES =====

class MetafieldProductVariantsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_product_variants search queries."""


class MetafieldProductVariantsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldProductVariantsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldProductVariantsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldProductVariantsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_product_variants search results."""


# Entity-specific condition types for metafield_product_variants
class MetafieldProductVariantsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldProductVariantsStringFilter


class MetafieldProductVariantsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldProductVariantsStringFilter


class MetafieldProductVariantsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldProductVariantsStringFilter


class MetafieldProductVariantsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldProductVariantsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldProductVariantsInCondition = TypedDict("MetafieldProductVariantsInCondition", {"in": MetafieldProductVariantsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldProductVariantsNotCondition = TypedDict("MetafieldProductVariantsNotCondition", {"not": "MetafieldProductVariantsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldProductVariantsAndCondition = TypedDict("MetafieldProductVariantsAndCondition", {"and": "list[MetafieldProductVariantsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldProductVariantsOrCondition = TypedDict("MetafieldProductVariantsOrCondition", {"or": "list[MetafieldProductVariantsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldProductVariantsAnyCondition = TypedDict("MetafieldProductVariantsAnyCondition", {"any": MetafieldProductVariantsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_product_variants condition types
MetafieldProductVariantsCondition = (
    MetafieldProductVariantsEqCondition
    | MetafieldProductVariantsNeqCondition
    | MetafieldProductVariantsGtCondition
    | MetafieldProductVariantsGteCondition
    | MetafieldProductVariantsLtCondition
    | MetafieldProductVariantsLteCondition
    | MetafieldProductVariantsInCondition
    | MetafieldProductVariantsLikeCondition
    | MetafieldProductVariantsFuzzyCondition
    | MetafieldProductVariantsKeywordCondition
    | MetafieldProductVariantsContainsCondition
    | MetafieldProductVariantsNotCondition
    | MetafieldProductVariantsAndCondition
    | MetafieldProductVariantsOrCondition
    | MetafieldProductVariantsAnyCondition
)


class MetafieldProductVariantsSearchQuery(TypedDict, total=False):
    """Search query for metafield_product_variants entity."""
    filter: MetafieldProductVariantsCondition
    sort: list[MetafieldProductVariantsSortFilter]


# ===== METAFIELD_PRODUCTS SEARCH TYPES =====

class MetafieldProductsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_products search queries."""


class MetafieldProductsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldProductsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldProductsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldProductsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_products search results."""


# Entity-specific condition types for metafield_products
class MetafieldProductsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldProductsSearchFilter


class MetafieldProductsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldProductsSearchFilter


class MetafieldProductsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldProductsSearchFilter


class MetafieldProductsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldProductsSearchFilter


class MetafieldProductsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldProductsSearchFilter


class MetafieldProductsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldProductsSearchFilter


class MetafieldProductsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldProductsStringFilter


class MetafieldProductsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldProductsStringFilter


class MetafieldProductsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldProductsStringFilter


class MetafieldProductsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldProductsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldProductsInCondition = TypedDict("MetafieldProductsInCondition", {"in": MetafieldProductsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldProductsNotCondition = TypedDict("MetafieldProductsNotCondition", {"not": "MetafieldProductsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldProductsAndCondition = TypedDict("MetafieldProductsAndCondition", {"and": "list[MetafieldProductsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldProductsOrCondition = TypedDict("MetafieldProductsOrCondition", {"or": "list[MetafieldProductsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldProductsAnyCondition = TypedDict("MetafieldProductsAnyCondition", {"any": MetafieldProductsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_products condition types
MetafieldProductsCondition = (
    MetafieldProductsEqCondition
    | MetafieldProductsNeqCondition
    | MetafieldProductsGtCondition
    | MetafieldProductsGteCondition
    | MetafieldProductsLtCondition
    | MetafieldProductsLteCondition
    | MetafieldProductsInCondition
    | MetafieldProductsLikeCondition
    | MetafieldProductsFuzzyCondition
    | MetafieldProductsKeywordCondition
    | MetafieldProductsContainsCondition
    | MetafieldProductsNotCondition
    | MetafieldProductsAndCondition
    | MetafieldProductsOrCondition
    | MetafieldProductsAnyCondition
)


class MetafieldProductsSearchQuery(TypedDict, total=False):
    """Search query for metafield_products entity."""
    filter: MetafieldProductsCondition
    sort: list[MetafieldProductsSortFilter]


# ===== METAFIELD_SHOPS SEARCH TYPES =====

class MetafieldShopsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_shops search queries."""


class MetafieldShopsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldShopsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldShopsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldShopsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_shops search results."""


# Entity-specific condition types for metafield_shops
class MetafieldShopsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldShopsSearchFilter


class MetafieldShopsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldShopsSearchFilter


class MetafieldShopsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldShopsSearchFilter


class MetafieldShopsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldShopsSearchFilter


class MetafieldShopsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldShopsSearchFilter


class MetafieldShopsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldShopsSearchFilter


class MetafieldShopsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldShopsStringFilter


class MetafieldShopsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldShopsStringFilter


class MetafieldShopsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldShopsStringFilter


class MetafieldShopsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldShopsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldShopsInCondition = TypedDict("MetafieldShopsInCondition", {"in": MetafieldShopsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldShopsNotCondition = TypedDict("MetafieldShopsNotCondition", {"not": "MetafieldShopsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldShopsAndCondition = TypedDict("MetafieldShopsAndCondition", {"and": "list[MetafieldShopsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldShopsOrCondition = TypedDict("MetafieldShopsOrCondition", {"or": "list[MetafieldShopsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldShopsAnyCondition = TypedDict("MetafieldShopsAnyCondition", {"any": MetafieldShopsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_shops condition types
MetafieldShopsCondition = (
    MetafieldShopsEqCondition
    | MetafieldShopsNeqCondition
    | MetafieldShopsGtCondition
    | MetafieldShopsGteCondition
    | MetafieldShopsLtCondition
    | MetafieldShopsLteCondition
    | MetafieldShopsInCondition
    | MetafieldShopsLikeCondition
    | MetafieldShopsFuzzyCondition
    | MetafieldShopsKeywordCondition
    | MetafieldShopsContainsCondition
    | MetafieldShopsNotCondition
    | MetafieldShopsAndCondition
    | MetafieldShopsOrCondition
    | MetafieldShopsAnyCondition
)


class MetafieldShopsSearchQuery(TypedDict, total=False):
    """Search query for metafield_shops entity."""
    filter: MetafieldShopsCondition
    sort: list[MetafieldShopsSortFilter]


# ===== METAFIELD_SMART_COLLECTIONS SEARCH TYPES =====

class MetafieldSmartCollectionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_smart_collections search queries."""


class MetafieldSmartCollectionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class MetafieldSmartCollectionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class MetafieldSmartCollectionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class MetafieldSmartCollectionsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_smart_collections search results."""


# Entity-specific condition types for metafield_smart_collections
class MetafieldSmartCollectionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldSmartCollectionsStringFilter


class MetafieldSmartCollectionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldSmartCollectionsStringFilter


class MetafieldSmartCollectionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldSmartCollectionsStringFilter


class MetafieldSmartCollectionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldSmartCollectionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldSmartCollectionsInCondition = TypedDict("MetafieldSmartCollectionsInCondition", {"in": MetafieldSmartCollectionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldSmartCollectionsNotCondition = TypedDict("MetafieldSmartCollectionsNotCondition", {"not": "MetafieldSmartCollectionsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldSmartCollectionsAndCondition = TypedDict("MetafieldSmartCollectionsAndCondition", {"and": "list[MetafieldSmartCollectionsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldSmartCollectionsOrCondition = TypedDict("MetafieldSmartCollectionsOrCondition", {"or": "list[MetafieldSmartCollectionsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldSmartCollectionsAnyCondition = TypedDict("MetafieldSmartCollectionsAnyCondition", {"any": MetafieldSmartCollectionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_smart_collections condition types
MetafieldSmartCollectionsCondition = (
    MetafieldSmartCollectionsEqCondition
    | MetafieldSmartCollectionsNeqCondition
    | MetafieldSmartCollectionsGtCondition
    | MetafieldSmartCollectionsGteCondition
    | MetafieldSmartCollectionsLtCondition
    | MetafieldSmartCollectionsLteCondition
    | MetafieldSmartCollectionsInCondition
    | MetafieldSmartCollectionsLikeCondition
    | MetafieldSmartCollectionsFuzzyCondition
    | MetafieldSmartCollectionsKeywordCondition
    | MetafieldSmartCollectionsContainsCondition
    | MetafieldSmartCollectionsNotCondition
    | MetafieldSmartCollectionsAndCondition
    | MetafieldSmartCollectionsOrCondition
    | MetafieldSmartCollectionsAnyCondition
)


class MetafieldSmartCollectionsSearchQuery(TypedDict, total=False):
    """Search query for metafield_smart_collections entity."""
    filter: MetafieldSmartCollectionsCondition
    sort: list[MetafieldSmartCollectionsSortFilter]


# ===== ORDER_REFUNDS SEARCH TYPES =====

class OrderRefundsSearchFilter(TypedDict, total=False):
    """Available fields for filtering order_refunds search queries."""


class OrderRefundsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class OrderRefundsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class OrderRefundsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class OrderRefundsSortFilter(TypedDict, total=False):
    """Available fields for sorting order_refunds search results."""


# Entity-specific condition types for order_refunds
class OrderRefundsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrderRefundsSearchFilter


class OrderRefundsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrderRefundsSearchFilter


class OrderRefundsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrderRefundsSearchFilter


class OrderRefundsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrderRefundsSearchFilter


class OrderRefundsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrderRefundsSearchFilter


class OrderRefundsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrderRefundsSearchFilter


class OrderRefundsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrderRefundsStringFilter


class OrderRefundsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrderRefundsStringFilter


class OrderRefundsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrderRefundsStringFilter


class OrderRefundsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrderRefundsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrderRefundsInCondition = TypedDict("OrderRefundsInCondition", {"in": OrderRefundsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrderRefundsNotCondition = TypedDict("OrderRefundsNotCondition", {"not": "OrderRefundsCondition"}, total=False)
"""Negates the nested condition."""

OrderRefundsAndCondition = TypedDict("OrderRefundsAndCondition", {"and": "list[OrderRefundsCondition]"}, total=False)
"""True if all nested conditions are true."""

OrderRefundsOrCondition = TypedDict("OrderRefundsOrCondition", {"or": "list[OrderRefundsCondition]"}, total=False)
"""True if any nested condition is true."""

OrderRefundsAnyCondition = TypedDict("OrderRefundsAnyCondition", {"any": OrderRefundsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all order_refunds condition types
OrderRefundsCondition = (
    OrderRefundsEqCondition
    | OrderRefundsNeqCondition
    | OrderRefundsGtCondition
    | OrderRefundsGteCondition
    | OrderRefundsLtCondition
    | OrderRefundsLteCondition
    | OrderRefundsInCondition
    | OrderRefundsLikeCondition
    | OrderRefundsFuzzyCondition
    | OrderRefundsKeywordCondition
    | OrderRefundsContainsCondition
    | OrderRefundsNotCondition
    | OrderRefundsAndCondition
    | OrderRefundsOrCondition
    | OrderRefundsAnyCondition
)


class OrderRefundsSearchQuery(TypedDict, total=False):
    """Search query for order_refunds entity."""
    filter: OrderRefundsCondition
    sort: list[OrderRefundsSortFilter]


# ===== PRICE_RULES SEARCH TYPES =====

class PriceRulesSearchFilter(TypedDict, total=False):
    """Available fields for filtering price_rules search queries."""


class PriceRulesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class PriceRulesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class PriceRulesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class PriceRulesSortFilter(TypedDict, total=False):
    """Available fields for sorting price_rules search results."""


# Entity-specific condition types for price_rules
class PriceRulesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PriceRulesSearchFilter


class PriceRulesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PriceRulesSearchFilter


class PriceRulesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PriceRulesSearchFilter


class PriceRulesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PriceRulesSearchFilter


class PriceRulesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PriceRulesSearchFilter


class PriceRulesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PriceRulesSearchFilter


class PriceRulesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PriceRulesStringFilter


class PriceRulesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PriceRulesStringFilter


class PriceRulesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PriceRulesStringFilter


class PriceRulesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PriceRulesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PriceRulesInCondition = TypedDict("PriceRulesInCondition", {"in": PriceRulesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PriceRulesNotCondition = TypedDict("PriceRulesNotCondition", {"not": "PriceRulesCondition"}, total=False)
"""Negates the nested condition."""

PriceRulesAndCondition = TypedDict("PriceRulesAndCondition", {"and": "list[PriceRulesCondition]"}, total=False)
"""True if all nested conditions are true."""

PriceRulesOrCondition = TypedDict("PriceRulesOrCondition", {"or": "list[PriceRulesCondition]"}, total=False)
"""True if any nested condition is true."""

PriceRulesAnyCondition = TypedDict("PriceRulesAnyCondition", {"any": PriceRulesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all price_rules condition types
PriceRulesCondition = (
    PriceRulesEqCondition
    | PriceRulesNeqCondition
    | PriceRulesGtCondition
    | PriceRulesGteCondition
    | PriceRulesLtCondition
    | PriceRulesLteCondition
    | PriceRulesInCondition
    | PriceRulesLikeCondition
    | PriceRulesFuzzyCondition
    | PriceRulesKeywordCondition
    | PriceRulesContainsCondition
    | PriceRulesNotCondition
    | PriceRulesAndCondition
    | PriceRulesOrCondition
    | PriceRulesAnyCondition
)


class PriceRulesSearchQuery(TypedDict, total=False):
    """Search query for price_rules entity."""
    filter: PriceRulesCondition
    sort: list[PriceRulesSortFilter]


# ===== PRODUCT_IMAGES SEARCH TYPES =====

class ProductImagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_images search queries."""


class ProductImagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class ProductImagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class ProductImagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class ProductImagesSortFilter(TypedDict, total=False):
    """Available fields for sorting product_images search results."""


# Entity-specific condition types for product_images
class ProductImagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductImagesSearchFilter


class ProductImagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductImagesSearchFilter


class ProductImagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductImagesSearchFilter


class ProductImagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductImagesSearchFilter


class ProductImagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductImagesSearchFilter


class ProductImagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductImagesSearchFilter


class ProductImagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductImagesStringFilter


class ProductImagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductImagesStringFilter


class ProductImagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductImagesStringFilter


class ProductImagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductImagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductImagesInCondition = TypedDict("ProductImagesInCondition", {"in": ProductImagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductImagesNotCondition = TypedDict("ProductImagesNotCondition", {"not": "ProductImagesCondition"}, total=False)
"""Negates the nested condition."""

ProductImagesAndCondition = TypedDict("ProductImagesAndCondition", {"and": "list[ProductImagesCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductImagesOrCondition = TypedDict("ProductImagesOrCondition", {"or": "list[ProductImagesCondition]"}, total=False)
"""True if any nested condition is true."""

ProductImagesAnyCondition = TypedDict("ProductImagesAnyCondition", {"any": ProductImagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_images condition types
ProductImagesCondition = (
    ProductImagesEqCondition
    | ProductImagesNeqCondition
    | ProductImagesGtCondition
    | ProductImagesGteCondition
    | ProductImagesLtCondition
    | ProductImagesLteCondition
    | ProductImagesInCondition
    | ProductImagesLikeCondition
    | ProductImagesFuzzyCondition
    | ProductImagesKeywordCondition
    | ProductImagesContainsCondition
    | ProductImagesNotCondition
    | ProductImagesAndCondition
    | ProductImagesOrCondition
    | ProductImagesAnyCondition
)


class ProductImagesSearchQuery(TypedDict, total=False):
    """Search query for product_images entity."""
    filter: ProductImagesCondition
    sort: list[ProductImagesSortFilter]


# ===== PRODUCT_VARIANTS SEARCH TYPES =====

class ProductVariantsSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_variants search queries."""


class ProductVariantsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class ProductVariantsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class ProductVariantsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class ProductVariantsSortFilter(TypedDict, total=False):
    """Available fields for sorting product_variants search results."""


# Entity-specific condition types for product_variants
class ProductVariantsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductVariantsSearchFilter


class ProductVariantsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductVariantsSearchFilter


class ProductVariantsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductVariantsSearchFilter


class ProductVariantsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductVariantsSearchFilter


class ProductVariantsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductVariantsSearchFilter


class ProductVariantsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductVariantsSearchFilter


class ProductVariantsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductVariantsStringFilter


class ProductVariantsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductVariantsStringFilter


class ProductVariantsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductVariantsStringFilter


class ProductVariantsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductVariantsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductVariantsInCondition = TypedDict("ProductVariantsInCondition", {"in": ProductVariantsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductVariantsNotCondition = TypedDict("ProductVariantsNotCondition", {"not": "ProductVariantsCondition"}, total=False)
"""Negates the nested condition."""

ProductVariantsAndCondition = TypedDict("ProductVariantsAndCondition", {"and": "list[ProductVariantsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductVariantsOrCondition = TypedDict("ProductVariantsOrCondition", {"or": "list[ProductVariantsCondition]"}, total=False)
"""True if any nested condition is true."""

ProductVariantsAnyCondition = TypedDict("ProductVariantsAnyCondition", {"any": ProductVariantsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_variants condition types
ProductVariantsCondition = (
    ProductVariantsEqCondition
    | ProductVariantsNeqCondition
    | ProductVariantsGtCondition
    | ProductVariantsGteCondition
    | ProductVariantsLtCondition
    | ProductVariantsLteCondition
    | ProductVariantsInCondition
    | ProductVariantsLikeCondition
    | ProductVariantsFuzzyCondition
    | ProductVariantsKeywordCondition
    | ProductVariantsContainsCondition
    | ProductVariantsNotCondition
    | ProductVariantsAndCondition
    | ProductVariantsOrCondition
    | ProductVariantsAnyCondition
)


class ProductVariantsSearchQuery(TypedDict, total=False):
    """Search query for product_variants entity."""
    filter: ProductVariantsCondition
    sort: list[ProductVariantsSortFilter]


# ===== SHOP SEARCH TYPES =====

class ShopSearchFilter(TypedDict, total=False):
    """Available fields for filtering shop search queries."""


class ShopInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class ShopAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class ShopStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class ShopSortFilter(TypedDict, total=False):
    """Available fields for sorting shop search results."""


# Entity-specific condition types for shop
class ShopEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ShopSearchFilter


class ShopNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ShopSearchFilter


class ShopGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ShopSearchFilter


class ShopGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ShopSearchFilter


class ShopLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ShopSearchFilter


class ShopLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ShopSearchFilter


class ShopLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ShopStringFilter


class ShopFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ShopStringFilter


class ShopKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ShopStringFilter


class ShopContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ShopAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ShopInCondition = TypedDict("ShopInCondition", {"in": ShopInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ShopNotCondition = TypedDict("ShopNotCondition", {"not": "ShopCondition"}, total=False)
"""Negates the nested condition."""

ShopAndCondition = TypedDict("ShopAndCondition", {"and": "list[ShopCondition]"}, total=False)
"""True if all nested conditions are true."""

ShopOrCondition = TypedDict("ShopOrCondition", {"or": "list[ShopCondition]"}, total=False)
"""True if any nested condition is true."""

ShopAnyCondition = TypedDict("ShopAnyCondition", {"any": ShopAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all shop condition types
ShopCondition = (
    ShopEqCondition
    | ShopNeqCondition
    | ShopGtCondition
    | ShopGteCondition
    | ShopLtCondition
    | ShopLteCondition
    | ShopInCondition
    | ShopLikeCondition
    | ShopFuzzyCondition
    | ShopKeywordCondition
    | ShopContainsCondition
    | ShopNotCondition
    | ShopAndCondition
    | ShopOrCondition
    | ShopAnyCondition
)


class ShopSearchQuery(TypedDict, total=False):
    """Search query for shop entity."""
    filter: ShopCondition
    sort: list[ShopSortFilter]


# ===== SMART_COLLECTIONS SEARCH TYPES =====

class SmartCollectionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering smart_collections search queries."""


class SmartCollectionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class SmartCollectionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class SmartCollectionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class SmartCollectionsSortFilter(TypedDict, total=False):
    """Available fields for sorting smart_collections search results."""


# Entity-specific condition types for smart_collections
class SmartCollectionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SmartCollectionsSearchFilter


class SmartCollectionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SmartCollectionsSearchFilter


class SmartCollectionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SmartCollectionsSearchFilter


class SmartCollectionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SmartCollectionsSearchFilter


class SmartCollectionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SmartCollectionsSearchFilter


class SmartCollectionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SmartCollectionsSearchFilter


class SmartCollectionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SmartCollectionsStringFilter


class SmartCollectionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SmartCollectionsStringFilter


class SmartCollectionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SmartCollectionsStringFilter


class SmartCollectionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SmartCollectionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SmartCollectionsInCondition = TypedDict("SmartCollectionsInCondition", {"in": SmartCollectionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SmartCollectionsNotCondition = TypedDict("SmartCollectionsNotCondition", {"not": "SmartCollectionsCondition"}, total=False)
"""Negates the nested condition."""

SmartCollectionsAndCondition = TypedDict("SmartCollectionsAndCondition", {"and": "list[SmartCollectionsCondition]"}, total=False)
"""True if all nested conditions are true."""

SmartCollectionsOrCondition = TypedDict("SmartCollectionsOrCondition", {"or": "list[SmartCollectionsCondition]"}, total=False)
"""True if any nested condition is true."""

SmartCollectionsAnyCondition = TypedDict("SmartCollectionsAnyCondition", {"any": SmartCollectionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all smart_collections condition types
SmartCollectionsCondition = (
    SmartCollectionsEqCondition
    | SmartCollectionsNeqCondition
    | SmartCollectionsGtCondition
    | SmartCollectionsGteCondition
    | SmartCollectionsLtCondition
    | SmartCollectionsLteCondition
    | SmartCollectionsInCondition
    | SmartCollectionsLikeCondition
    | SmartCollectionsFuzzyCondition
    | SmartCollectionsKeywordCondition
    | SmartCollectionsContainsCondition
    | SmartCollectionsNotCondition
    | SmartCollectionsAndCondition
    | SmartCollectionsOrCondition
    | SmartCollectionsAnyCondition
)


class SmartCollectionsSearchQuery(TypedDict, total=False):
    """Search query for smart_collections entity."""
    filter: SmartCollectionsCondition
    sort: list[SmartCollectionsSortFilter]


# ===== TENDER_TRANSACTIONS SEARCH TYPES =====

class TenderTransactionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tender_transactions search queries."""


class TenderTransactionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""


class TenderTransactionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""


class TenderTransactionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""


class TenderTransactionsSortFilter(TypedDict, total=False):
    """Available fields for sorting tender_transactions search results."""


# Entity-specific condition types for tender_transactions
class TenderTransactionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TenderTransactionsSearchFilter


class TenderTransactionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TenderTransactionsSearchFilter


class TenderTransactionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TenderTransactionsSearchFilter


class TenderTransactionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TenderTransactionsSearchFilter


class TenderTransactionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TenderTransactionsSearchFilter


class TenderTransactionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TenderTransactionsSearchFilter


class TenderTransactionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TenderTransactionsStringFilter


class TenderTransactionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TenderTransactionsStringFilter


class TenderTransactionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TenderTransactionsStringFilter


class TenderTransactionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TenderTransactionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TenderTransactionsInCondition = TypedDict("TenderTransactionsInCondition", {"in": TenderTransactionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TenderTransactionsNotCondition = TypedDict("TenderTransactionsNotCondition", {"not": "TenderTransactionsCondition"}, total=False)
"""Negates the nested condition."""

TenderTransactionsAndCondition = TypedDict("TenderTransactionsAndCondition", {"and": "list[TenderTransactionsCondition]"}, total=False)
"""True if all nested conditions are true."""

TenderTransactionsOrCondition = TypedDict("TenderTransactionsOrCondition", {"or": "list[TenderTransactionsCondition]"}, total=False)
"""True if any nested condition is true."""

TenderTransactionsAnyCondition = TypedDict("TenderTransactionsAnyCondition", {"any": TenderTransactionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tender_transactions condition types
TenderTransactionsCondition = (
    TenderTransactionsEqCondition
    | TenderTransactionsNeqCondition
    | TenderTransactionsGtCondition
    | TenderTransactionsGteCondition
    | TenderTransactionsLtCondition
    | TenderTransactionsLteCondition
    | TenderTransactionsInCondition
    | TenderTransactionsLikeCondition
    | TenderTransactionsFuzzyCondition
    | TenderTransactionsKeywordCondition
    | TenderTransactionsContainsCondition
    | TenderTransactionsNotCondition
    | TenderTransactionsAndCondition
    | TenderTransactionsOrCondition
    | TenderTransactionsAnyCondition
)


class TenderTransactionsSearchQuery(TypedDict, total=False):
    """Search query for tender_transactions entity."""
    filter: TenderTransactionsCondition
    sort: list[TenderTransactionsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
