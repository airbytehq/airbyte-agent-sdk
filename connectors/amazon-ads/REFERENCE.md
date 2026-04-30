# Amazon-Ads full reference

This is the full reference documentation for the Amazon-Ads agent connector.

## Supported entities and actions

The Amazon-Ads connector supports the following entities and actions.

| Entity | Actions |
|--------|---------|
| Profiles | [List](#profiles-list), [Get](#profiles-get), [Context Store Search](#profiles-context-store-search) |
| Portfolios | [List](#portfolios-list), [Get](#portfolios-get), [Context Store Search](#portfolios-context-store-search) |
| Sponsored Product Campaigns | [List](#sponsored-product-campaigns-list), [Get](#sponsored-product-campaigns-get), [Context Store Search](#sponsored-product-campaigns-context-store-search) |
| Sponsored Product Ad Groups | [List](#sponsored-product-ad-groups-list), [Context Store Search](#sponsored-product-ad-groups-context-store-search) |
| Sponsored Product Keywords | [List](#sponsored-product-keywords-list), [Context Store Search](#sponsored-product-keywords-context-store-search) |
| Sponsored Product Product Ads | [List](#sponsored-product-product-ads-list), [Context Store Search](#sponsored-product-product-ads-context-store-search) |
| Sponsored Product Targets | [List](#sponsored-product-targets-list), [Context Store Search](#sponsored-product-targets-context-store-search) |
| Sponsored Product Negative Keywords | [List](#sponsored-product-negative-keywords-list), [Context Store Search](#sponsored-product-negative-keywords-context-store-search) |
| Sponsored Product Negative Targets | [List](#sponsored-product-negative-targets-list) |
| Sponsored Brands Campaigns | [List](#sponsored-brands-campaigns-list), [Context Store Search](#sponsored-brands-campaigns-context-store-search) |
| Sponsored Brands Ad Groups | [List](#sponsored-brands-ad-groups-list), [Context Store Search](#sponsored-brands-ad-groups-context-store-search) |

## Profiles

### Profiles List

Returns a list of advertising profiles associated with the authenticated user.
Profiles represent an advertiser's account in a specific marketplace. Advertisers
may have a single profile if they advertise in only one marketplace, or a separate
profile for each marketplace if they advertise regionally or globally.


#### Python SDK

```python
await amazon_ads.profiles.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "profiles",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `profileTypeFilter` | `string` | No | Filter profiles by type. Comma-separated list of profile types.
Valid values: seller, vendor, agency
 |


<details>
<summary><b>Response Schema</b></summary>

#### Records

| Field Name | Type | Description |
|------------|------|-------------|
| `profileId` | `integer` |  |
| `countryCode` | `string \| null` |  |
| `currencyCode` | `string \| null` |  |
| `dailyBudget` | `number \| null` |  |
| `timezone` | `string \| null` |  |
| `accountInfo` | `object \| any` |  |


</details>

### Profiles Get

Retrieves a single advertising profile by its ID. The profile contains
information about the advertiser's account in a specific marketplace.


#### Python SDK

```python
await amazon_ads.profiles.get(
    profile_id=0
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "profiles",
    "action": "get",
    "params": {
        "profileId": 0
    }
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `profileId` | `integer` | Yes | The unique identifier of the profile |


<details>
<summary><b>Response Schema</b></summary>

#### Records

| Field Name | Type | Description |
|------------|------|-------------|
| `profileId` | `integer` |  |
| `countryCode` | `string \| null` |  |
| `currencyCode` | `string \| null` |  |
| `dailyBudget` | `number \| null` |  |
| `timezone` | `string \| null` |  |
| `accountInfo` | `object \| any` |  |


</details>

### Profiles Context Store Search

Search and filter profiles records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.profiles.context_store_search(
    query={"filter": {"eq": {"accountInfo": {}}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "profiles",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"accountInfo": {}}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `accountInfo` | `object` |  |
| `countryCode` | `string` |  |
| `currencyCode` | `string` |  |
| `dailyBudget` | `number` |  |
| `profileId` | `integer` |  |
| `timezone` | `string` |  |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].accountInfo` | `object` |  |
| `data[].countryCode` | `string` |  |
| `data[].currencyCode` | `string` |  |
| `data[].dailyBudget` | `number` |  |
| `data[].profileId` | `integer` |  |
| `data[].timezone` | `string` |  |

</details>

## Portfolios

### Portfolios List

Returns a list of portfolios for the specified profile. Portfolios are used to
group campaigns together for organizational and budget management purposes.


#### Python SDK

```python
await amazon_ads.portfolios.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "portfolios",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `includeExtendedDataFields` | `string` | No | Whether to include extended data fields in the response |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Portfolios Get

Retrieves a single portfolio by its ID using the v2 API.


#### Python SDK

```python
await amazon_ads.portfolios.get(
    portfolio_id=0
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "portfolios",
    "action": "get",
    "params": {
        "portfolioId": 0
    }
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `portfolioId` | `integer` | Yes | The unique identifier of the portfolio |


<details>
<summary><b>Response Schema</b></summary>

#### Records

| Field Name | Type | Description |
|------------|------|-------------|
| `portfolioId` | `string \| integer` |  |
| `name` | `string \| null` |  |
| `budget` | `object \| any` |  |
| `inBudget` | `boolean \| null` |  |
| `state` | `string \| null` |  |
| `creationDate` | `integer \| null` |  |
| `lastUpdatedDate` | `integer \| null` |  |
| `servingStatus` | `string \| null` |  |


</details>

### Portfolios Context Store Search

Search and filter portfolios records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.portfolios.context_store_search(
    query={"filter": {"eq": {"portfolioId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "portfolios",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"portfolioId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `portfolioId` | `string` | The unique identifier of the portfolio |
| `name` | `string` | The name of the portfolio |
| `budget` | `object` | Budget configuration for the portfolio |
| `inBudget` | `boolean` | Whether the portfolio is within its budget |
| `state` | `string` | The state of the portfolio (enabled, paused, archived) |
| `creationDate` | `integer` | The creation date of the portfolio (epoch milliseconds) |
| `lastUpdatedDate` | `integer` | The last updated date of the portfolio (epoch milliseconds) |
| `servingStatus` | `string` | The serving status of the portfolio |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].portfolioId` | `string` | The unique identifier of the portfolio |
| `data[].name` | `string` | The name of the portfolio |
| `data[].budget` | `object` | Budget configuration for the portfolio |
| `data[].inBudget` | `boolean` | Whether the portfolio is within its budget |
| `data[].state` | `string` | The state of the portfolio (enabled, paused, archived) |
| `data[].creationDate` | `integer` | The creation date of the portfolio (epoch milliseconds) |
| `data[].lastUpdatedDate` | `integer` | The last updated date of the portfolio (epoch milliseconds) |
| `data[].servingStatus` | `string` | The serving status of the portfolio |

</details>

## Sponsored Product Campaigns

### Sponsored Product Campaigns List

Returns a list of sponsored product campaigns for the specified profile.
Sponsored Products campaigns promote individual product listings on Amazon.


#### Python SDK

```python
await amazon_ads.sponsored_product_campaigns.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_campaigns",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Sponsored Product Campaigns Get

Retrieves a single sponsored product campaign by its ID using the v2 API.


#### Python SDK

```python
await amazon_ads.sponsored_product_campaigns.get(
    campaign_id=0
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_campaigns",
    "action": "get",
    "params": {
        "campaignId": 0
    }
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `campaignId` | `integer` | Yes | The unique identifier of the campaign |


<details>
<summary><b>Response Schema</b></summary>

#### Records

| Field Name | Type | Description |
|------------|------|-------------|
| `campaignId` | `string \| integer` |  |
| `portfolioId` | `string \| integer \| any` |  |
| `name` | `string \| null` |  |
| `campaignType` | `string \| null` |  |
| `tags` | `object \| null` |  |
| `targetingType` | `string \| null` |  |
| `premiumBidAdjustment` | `boolean \| null` |  |
| `state` | `string \| null` |  |
| `dynamicBidding` | `object \| any` |  |
| `bidding` | `object \| any` |  |
| `startDate` | `string \| null` |  |
| `endDate` | `string \| null` |  |
| `dailyBudget` | `number \| null` |  |
| `budget` | `object \| any` |  |
| `extendedData` | `object \| null` |  |
| `marketplaceBudgetAllocation` | `string \| null` |  |
| `offAmazonSettings` | `object \| null` |  |


</details>

### Sponsored Product Campaigns Context Store Search

Search and filter sponsored product campaigns records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.sponsored_product_campaigns.context_store_search(
    query={"filter": {"eq": {"campaignId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_campaigns",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"campaignId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `campaignId` | `string` | The unique identifier of the campaign |
| `portfolioId` | `string` | The portfolio ID this campaign belongs to |
| `name` | `string` | The name of the campaign |
| `targetingType` | `string` | The targeting type (manual, auto) |
| `state` | `string` | The state of the campaign (enabled, paused, archived) |
| `budget` | `object` | Budget configuration for the campaign |
| `startDate` | `string` | The start date of the campaign (YYYYMMDD format) |
| `endDate` | `string` | The end date of the campaign (YYYYMMDD format) |
| `dynamicBidding` | `object` | Dynamic bidding settings for the campaign |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].campaignId` | `string` | The unique identifier of the campaign |
| `data[].portfolioId` | `string` | The portfolio ID this campaign belongs to |
| `data[].name` | `string` | The name of the campaign |
| `data[].targetingType` | `string` | The targeting type (manual, auto) |
| `data[].state` | `string` | The state of the campaign (enabled, paused, archived) |
| `data[].budget` | `object` | Budget configuration for the campaign |
| `data[].startDate` | `string` | The start date of the campaign (YYYYMMDD format) |
| `data[].endDate` | `string` | The end date of the campaign (YYYYMMDD format) |
| `data[].dynamicBidding` | `object` | Dynamic bidding settings for the campaign |

</details>

## Sponsored Product Ad Groups

### Sponsored Product Ad Groups List

Returns a list of sponsored product ad groups for the specified profile.
Ad groups are used to organize ads and targeting within a campaign.


#### Python SDK

```python
await amazon_ads.sponsored_product_ad_groups.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_ad_groups",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Sponsored Product Ad Groups Context Store Search

Search and filter sponsored product ad groups records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.sponsored_product_ad_groups.context_store_search(
    query={"filter": {"eq": {"adGroupId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_ad_groups",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"adGroupId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `adGroupId` | `string` | The unique identifier of the ad group |
| `campaignId` | `string` | The campaign ID this ad group belongs to |
| `name` | `string` | The name of the ad group |
| `state` | `string` | The state of the ad group (enabled, paused, archived) |
| `defaultBid` | `number` | The default bid amount for the ad group |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].adGroupId` | `string` | The unique identifier of the ad group |
| `data[].campaignId` | `string` | The campaign ID this ad group belongs to |
| `data[].name` | `string` | The name of the ad group |
| `data[].state` | `string` | The state of the ad group (enabled, paused, archived) |
| `data[].defaultBid` | `number` | The default bid amount for the ad group |

</details>

## Sponsored Product Keywords

### Sponsored Product Keywords List

Returns a list of sponsored product keywords for the specified profile.
Keywords are used in manual targeting campaigns to match shopper search queries.


#### Python SDK

```python
await amazon_ads.sponsored_product_keywords.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_keywords",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Sponsored Product Keywords Context Store Search

Search and filter sponsored product keywords records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.sponsored_product_keywords.context_store_search(
    query={"filter": {"eq": {"keywordId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_keywords",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"keywordId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `keywordId` | `string` | The unique identifier of the keyword |
| `campaignId` | `string` | The campaign ID this keyword belongs to |
| `adGroupId` | `string` | The ad group ID this keyword belongs to |
| `keywordText` | `string` | The keyword text |
| `state` | `string` | The state of the keyword (enabled, paused, archived) |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].keywordId` | `string` | The unique identifier of the keyword |
| `data[].campaignId` | `string` | The campaign ID this keyword belongs to |
| `data[].adGroupId` | `string` | The ad group ID this keyword belongs to |
| `data[].keywordText` | `string` | The keyword text |
| `data[].state` | `string` | The state of the keyword (enabled, paused, archived) |

</details>

## Sponsored Product Product Ads

### Sponsored Product Product Ads List

Returns a list of sponsored product ads for the specified profile.
Product ads associate an advertised product with an ad group.


#### Python SDK

```python
await amazon_ads.sponsored_product_product_ads.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_product_ads",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Sponsored Product Product Ads Context Store Search

Search and filter sponsored product product ads records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.sponsored_product_product_ads.context_store_search(
    query={"filter": {"eq": {"adId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_product_ads",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"adId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `adId` | `string` | The unique identifier of the product ad |
| `campaignId` | `string` | The campaign ID this product ad belongs to |
| `adGroupId` | `string` | The ad group ID this product ad belongs to |
| `asin` | `string` | The ASIN of the advertised product |
| `sku` | `string` | The SKU of the advertised product (seller accounts only) |
| `state` | `string` | The state of the product ad (enabled, paused, archived) |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].adId` | `string` | The unique identifier of the product ad |
| `data[].campaignId` | `string` | The campaign ID this product ad belongs to |
| `data[].adGroupId` | `string` | The ad group ID this product ad belongs to |
| `data[].asin` | `string` | The ASIN of the advertised product |
| `data[].sku` | `string` | The SKU of the advertised product (seller accounts only) |
| `data[].state` | `string` | The state of the product ad (enabled, paused, archived) |

</details>

## Sponsored Product Targets

### Sponsored Product Targets List

Returns a list of sponsored product targeting clauses for the specified profile.
Targeting clauses define product or category targeting for ad groups.


#### Python SDK

```python
await amazon_ads.sponsored_product_targets.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_targets",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Sponsored Product Targets Context Store Search

Search and filter sponsored product targets records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.sponsored_product_targets.context_store_search(
    query={"filter": {"eq": {"targetId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_targets",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"targetId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `targetId` | `string` | The unique identifier of the targeting clause |
| `campaignId` | `string` | The campaign ID this target belongs to |
| `adGroupId` | `string` | The ad group ID this target belongs to |
| `expressionType` | `string` | The type of targeting expression (manual, auto) |
| `state` | `string` | The state of the targeting clause (enabled, paused, archived) |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].targetId` | `string` | The unique identifier of the targeting clause |
| `data[].campaignId` | `string` | The campaign ID this target belongs to |
| `data[].adGroupId` | `string` | The ad group ID this target belongs to |
| `data[].expressionType` | `string` | The type of targeting expression (manual, auto) |
| `data[].state` | `string` | The state of the targeting clause (enabled, paused, archived) |

</details>

## Sponsored Product Negative Keywords

### Sponsored Product Negative Keywords List

Returns a list of sponsored product negative keywords for the specified profile.
Negative keywords prevent ads from showing for specific search terms.


#### Python SDK

```python
await amazon_ads.sponsored_product_negative_keywords.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_negative_keywords",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Sponsored Product Negative Keywords Context Store Search

Search and filter sponsored product negative keywords records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.sponsored_product_negative_keywords.context_store_search(
    query={"filter": {"eq": {"keywordId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_negative_keywords",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"keywordId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `keywordId` | `string` | The unique identifier of the negative keyword |
| `campaignId` | `string` | The campaign ID this negative keyword belongs to |
| `adGroupId` | `string` | The ad group ID this negative keyword belongs to |
| `keywordText` | `string` | The negative keyword text |
| `state` | `string` | The state of the negative keyword (enabled, paused, archived) |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].keywordId` | `string` | The unique identifier of the negative keyword |
| `data[].campaignId` | `string` | The campaign ID this negative keyword belongs to |
| `data[].adGroupId` | `string` | The ad group ID this negative keyword belongs to |
| `data[].keywordText` | `string` | The negative keyword text |
| `data[].state` | `string` | The state of the negative keyword (enabled, paused, archived) |

</details>

## Sponsored Product Negative Targets

### Sponsored Product Negative Targets List

Returns a list of sponsored product negative targeting clauses for the specified profile.
Negative targeting clauses exclude specific products or categories from targeting.


#### Python SDK

```python
await amazon_ads.sponsored_product_negative_targets.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_product_negative_targets",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

## Sponsored Brands Campaigns

### Sponsored Brands Campaigns List

Returns a list of sponsored brands campaigns for the specified profile.
Sponsored Brands campaigns help drive discovery and sales with creative ad experiences.


#### Python SDK

```python
await amazon_ads.sponsored_brands_campaigns.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_brands_campaigns",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Sponsored Brands Campaigns Context Store Search

Search and filter sponsored brands campaigns records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.sponsored_brands_campaigns.context_store_search(
    query={"filter": {"eq": {"campaignId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_brands_campaigns",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"campaignId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `campaignId` | `string` | The unique identifier of the campaign |
| `name` | `string` | The name of the campaign |
| `state` | `string` | The state of the campaign (enabled, paused, archived) |
| `budget` | `number` | The budget amount for the campaign |
| `budgetType` | `string` | The budget type (DAILY, LIFETIME) |
| `startDate` | `string` | The start date of the campaign (YYYYMMDD format) |
| `endDate` | `string` | The end date of the campaign (YYYYMMDD format) |
| `portfolioId` | `string` | The portfolio ID this campaign belongs to |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].campaignId` | `string` | The unique identifier of the campaign |
| `data[].name` | `string` | The name of the campaign |
| `data[].state` | `string` | The state of the campaign (enabled, paused, archived) |
| `data[].budget` | `number` | The budget amount for the campaign |
| `data[].budgetType` | `string` | The budget type (DAILY, LIFETIME) |
| `data[].startDate` | `string` | The start date of the campaign (YYYYMMDD format) |
| `data[].endDate` | `string` | The end date of the campaign (YYYYMMDD format) |
| `data[].portfolioId` | `string` | The portfolio ID this campaign belongs to |

</details>

## Sponsored Brands Ad Groups

### Sponsored Brands Ad Groups List

Returns a list of sponsored brands ad groups for the specified profile.
Ad groups organize ads and targeting within a Sponsored Brands campaign.


#### Python SDK

```python
await amazon_ads.sponsored_brands_ad_groups.list()
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_brands_ad_groups",
    "action": "list"
}'
```


#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stateFilter` | `object` | No |  |
| `stateFilter.include` | `string` | No | Comma-separated list of states to include (enabled, paused, archived) |
| `maxResults` | `integer` | No | Maximum number of results to return |
| `nextToken` | `string` | No | Token for pagination |


<details>
<summary><b>Response Schema</b></summary>



#### Meta

| Field Name | Type | Description |
|------------|------|-------------|
| `next_token` | `string \| null` |  |

</details>

### Sponsored Brands Ad Groups Context Store Search

Search and filter sponsored brands ad groups records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK

```python
await amazon_ads.sponsored_brands_ad_groups.context_store_search(
    query={"filter": {"eq": {"adGroupId": "<str>"}}}
)
```

#### API

```bash
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "sponsored_brands_ad_groups",
    "action": "context_store_search",
    "params": {
        "query": {"filter": {"eq": {"adGroupId": "<str>"}}}
    }
}'
```

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `query` | `object` | Yes | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object` | No | Filter conditions |
| `query.sort` | `array` | No | Sort conditions |
| `limit` | `integer` | No | Maximum results to return (default 1000) |
| `cursor` | `string` | No | Pagination cursor from previous response's `meta.cursor` |
| `fields` | `array` | No | Field paths to include in results |

#### Searchable Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `adGroupId` | `string` | The unique identifier of the ad group |
| `campaignId` | `string` | The campaign ID this ad group belongs to |
| `name` | `string` | The name of the ad group |
| `state` | `string` | The state of the ad group (enabled, paused, archived) |

<details>
<summary><b>Response Schema</b></summary>

| Field Name | Type | Description |
|------------|------|-------------|
| `data` | `array` | List of matching records |
| `meta` | `object` | Pagination metadata |
| `meta.has_more` | `boolean` | Whether additional pages are available |
| `meta.cursor` | `string \| null` | Cursor for next page of results |
| `meta.took_ms` | `number \| null` | Query execution time in milliseconds |
| `data[].adGroupId` | `string` | The unique identifier of the ad group |
| `data[].campaignId` | `string` | The campaign ID this ad group belongs to |
| `data[].name` | `string` | The name of the ad group |
| `data[].state` | `string` | The state of the ad group (enabled, paused, archived) |

</details>

