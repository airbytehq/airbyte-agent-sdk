"""
Connector model for reddit-ads.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""
# ruff: noqa: E501

from __future__ import annotations

from airbyte_agent_sdk.types import (
    Action,
    AuthConfig,
    AuthType,
    ConnectorModel,
    EndpointDefinition,
    EntityDefinition,
)
from airbyte_agent_sdk.schema.security import (
    AuthConfigFieldSpec,
    AuthConfigSpec,
)
from airbyte_agent_sdk.schema.extensions import (
    CacheConfig,
    CacheEntityConfig,
    CacheFieldConfig,
    EntityRelationshipConfig,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

RedditAdsConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('c876992b-877e-4bb3-946b-4678c82bb7ac'),
    name='reddit-ads',
    base_url='https://ads-api.reddit.com/api/v3',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://www.reddit.com/api/v1/access_token',
            'auth_style': 'basic',
            'body_format': 'form',
        },
        user_config_spec=AuthConfigSpec(
            title='Reddit OAuth2 Authentication',
            type='object',
            required=['client_id', 'client_secret', 'refresh_token'],
            properties={
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='The OAuth2 client ID from your Reddit developer application.',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='The OAuth2 client secret from your Reddit developer application.',
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='The OAuth2 refresh token obtained through the authorization code flow.\n',
                ),
            },
            auth_mapping={
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
                'refresh_token': '${refresh_token}',
            },
            replication_auth_key_mapping={
                'client_id': 'client_id',
                'client_secret': 'client_secret',
                'refresh_token': 'refresh_token',
            },
        ),
    ),
    entities=[
        EntityDefinition(
            name='businesses',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/me/businesses',
                    action=Action.LIST,
                    description='Retrieve all businesses associated with the authenticated user.',
                    query_params=['page.size', 'page.token'],
                    query_params_schema={
                        'page.size': {
                            'type': 'integer',
                            'required': False,
                            'maximum': 1000,
                        },
                        'page.token': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Reddit advertising business entity.',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique business identifier (UUID)'},
                                        'name': {'type': 'string', 'description': 'Business name'},
                                        'country': {'type': 'string', 'description': 'Business country code'},
                                        'primary_contact_id': {'type': 'string', 'description': 'Primary contact member ID'},
                                        'creator_id': {'type': 'string', 'description': 'ID of the user who created the business'},
                                        'industry': {'type': 'string', 'description': 'Business industry'},
                                        'website_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Business website URL',
                                        },
                                        'phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Business phone number',
                                        },
                                        'agency_affiliated': {'type': 'boolean', 'description': 'Whether the business is affiliated with an agency'},
                                        'two_fa_enforcement': {'type': 'string', 'description': 'Two-factor authentication enforcement setting'},
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Business creation timestamp',
                                        },
                                        'modified_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'businesses',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Reddit advertising businesses that own ad accounts',
                                        'when_to_use': 'Questions about business entities, business settings, or finding which businesses the user has access to',
                                        'trigger_phrases': [
                                            'business',
                                            'my businesses',
                                            'business account',
                                            'organization',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What businesses do I have access to?', 'Show me my business details'],
                                        'search_strategy': 'Search by business name',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'description': 'Pagination metadata for list responses',
                                'properties': {
                                    'next_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for next page. Null if this is the last page.',
                                    },
                                    'previous_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for previous page. Null if this is the first page.',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_link': '$.pagination.next_url'},
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Reddit advertising business entity.',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique business identifier (UUID)'},
                    'name': {'type': 'string', 'description': 'Business name'},
                    'country': {'type': 'string', 'description': 'Business country code'},
                    'primary_contact_id': {'type': 'string', 'description': 'Primary contact member ID'},
                    'creator_id': {'type': 'string', 'description': 'ID of the user who created the business'},
                    'industry': {'type': 'string', 'description': 'Business industry'},
                    'website_url': {
                        'type': ['null', 'string'],
                        'description': 'Business website URL',
                    },
                    'phone': {
                        'type': ['null', 'string'],
                        'description': 'Business phone number',
                    },
                    'agency_affiliated': {'type': 'boolean', 'description': 'Whether the business is affiliated with an agency'},
                    'two_fa_enforcement': {'type': 'string', 'description': 'Two-factor authentication enforcement setting'},
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Business creation timestamp',
                    },
                    'modified_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                },
                'x-airbyte-entity-name': 'businesses',
                'x-airbyte-ai-hints': {
                    'summary': 'Reddit advertising businesses that own ad accounts',
                    'when_to_use': 'Questions about business entities, business settings, or finding which businesses the user has access to',
                    'trigger_phrases': [
                        'business',
                        'my businesses',
                        'business account',
                        'organization',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What businesses do I have access to?', 'Show me my business details'],
                    'search_strategy': 'Search by business name',
                },
            },
            ai_hints={
                'summary': 'Reddit advertising businesses that own ad accounts',
                'when_to_use': 'Questions about business entities, business settings, or finding which businesses the user has access to',
                'trigger_phrases': [
                    'business',
                    'my businesses',
                    'business account',
                    'organization',
                ],
                'freshness': 'live',
                'example_questions': ['What businesses do I have access to?', 'Show me my business details'],
                'search_strategy': 'Search by business name',
            },
        ),
        EntityDefinition(
            name='ad_accounts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/businesses/{business_id}/ad_accounts',
                    action=Action.LIST,
                    description='Retrieve the ad accounts in a business.',
                    query_params=['page.size', 'page.token'],
                    query_params_schema={
                        'page.size': {
                            'type': 'integer',
                            'required': False,
                            'maximum': 1000,
                        },
                        'page.token': {'type': 'string', 'required': False},
                    },
                    path_params=['business_id'],
                    path_params_schema={
                        'business_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Reddit ad account with billing, attribution, and configuration settings.',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique ad account identifier (t2_ or a2_ prefix)'},
                                        'name': {'type': 'string', 'description': 'Ad account name'},
                                        'business_id': {'type': 'string', 'description': 'The business this account belongs to'},
                                        'type': {
                                            'type': 'string',
                                            'enum': ['MANAGED', 'SELF_SERVE'],
                                            'description': 'Account type',
                                        },
                                        'currency': {'type': 'string', 'description': 'Account currency code'},
                                        'time_zone_id': {'type': 'string', 'description': 'Account time zone'},
                                        'admin_approval': {
                                            'type': 'string',
                                            'enum': [
                                                'ADMIN',
                                                'BANNED',
                                                'NEEDS_ID_VERIFICATION',
                                                'PENDING',
                                                'SUSPENDED',
                                                'SUSPICIOUS',
                                                'TRUSTED',
                                                'VALID',
                                            ],
                                            'description': 'Admin approval status',
                                        },
                                        'attribution_type': {'type': 'string', 'description': 'Attribution type for web conversions'},
                                        'click_attribution_window': {
                                            'type': 'string',
                                            'enum': ['DAY', 'MONTH', 'WEEK'],
                                            'description': 'Click attribution window',
                                        },
                                        'view_attribution_window': {
                                            'type': 'string',
                                            'enum': ['DAY', 'MONTH', 'WEEK'],
                                            'description': 'View attribution window',
                                        },
                                        'app_attribution_type': {'type': 'string', 'description': 'Attribution type for app events'},
                                        'app_click_attribution_window': {'type': 'string', 'description': 'App click attribution window'},
                                        'app_view_attribution_window': {'type': 'string', 'description': 'App view attribution window'},
                                        'primary_contact_member_id': {'type': 'string', 'description': 'Primary contact member ID'},
                                        'suspension_reason': {
                                            'type': ['null', 'string'],
                                            'description': 'Reason for account suspension, if applicable',
                                        },
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Account creation timestamp',
                                        },
                                        'modified_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'excluded_communities': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'List of excluded community IDs',
                                        },
                                        'excluded_keywords': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'List of excluded keywords',
                                        },
                                        'pixel_partner_preferences': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'Pixel partner preferences',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ad_accounts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Reddit advertising accounts with billing, attribution, and configuration settings',
                                        'when_to_use': 'Questions about ad account setup, billing status, attribution windows, or account-level settings',
                                        'trigger_phrases': [
                                            'ad account',
                                            'billing info',
                                            'account status',
                                            'attribution window',
                                            'Reddit ads account',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What ad accounts do I have?', 'What is the attribution window for my ad account?', 'Is my ad account in good standing?'],
                                        'search_strategy': 'Search by account name or ID',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'description': 'Pagination metadata for list responses',
                                'properties': {
                                    'next_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for next page. Null if this is the last page.',
                                    },
                                    'previous_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for previous page. Null if this is the first page.',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_link': '$.pagination.next_url'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}',
                    action=Action.GET,
                    description='Retrieve ad account by ID.',
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Reddit ad account with billing, attribution, and configuration settings.',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique ad account identifier (t2_ or a2_ prefix)'},
                                    'name': {'type': 'string', 'description': 'Ad account name'},
                                    'business_id': {'type': 'string', 'description': 'The business this account belongs to'},
                                    'type': {
                                        'type': 'string',
                                        'enum': ['MANAGED', 'SELF_SERVE'],
                                        'description': 'Account type',
                                    },
                                    'currency': {'type': 'string', 'description': 'Account currency code'},
                                    'time_zone_id': {'type': 'string', 'description': 'Account time zone'},
                                    'admin_approval': {
                                        'type': 'string',
                                        'enum': [
                                            'ADMIN',
                                            'BANNED',
                                            'NEEDS_ID_VERIFICATION',
                                            'PENDING',
                                            'SUSPENDED',
                                            'SUSPICIOUS',
                                            'TRUSTED',
                                            'VALID',
                                        ],
                                        'description': 'Admin approval status',
                                    },
                                    'attribution_type': {'type': 'string', 'description': 'Attribution type for web conversions'},
                                    'click_attribution_window': {
                                        'type': 'string',
                                        'enum': ['DAY', 'MONTH', 'WEEK'],
                                        'description': 'Click attribution window',
                                    },
                                    'view_attribution_window': {
                                        'type': 'string',
                                        'enum': ['DAY', 'MONTH', 'WEEK'],
                                        'description': 'View attribution window',
                                    },
                                    'app_attribution_type': {'type': 'string', 'description': 'Attribution type for app events'},
                                    'app_click_attribution_window': {'type': 'string', 'description': 'App click attribution window'},
                                    'app_view_attribution_window': {'type': 'string', 'description': 'App view attribution window'},
                                    'primary_contact_member_id': {'type': 'string', 'description': 'Primary contact member ID'},
                                    'suspension_reason': {
                                        'type': ['null', 'string'],
                                        'description': 'Reason for account suspension, if applicable',
                                    },
                                    'created_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Account creation timestamp',
                                    },
                                    'modified_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Last modification timestamp',
                                    },
                                    'excluded_communities': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of excluded community IDs',
                                    },
                                    'excluded_keywords': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of excluded keywords',
                                    },
                                    'pixel_partner_preferences': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'Pixel partner preferences',
                                    },
                                },
                                'x-airbyte-entity-name': 'ad_accounts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Reddit advertising accounts with billing, attribution, and configuration settings',
                                    'when_to_use': 'Questions about ad account setup, billing status, attribution windows, or account-level settings',
                                    'trigger_phrases': [
                                        'ad account',
                                        'billing info',
                                        'account status',
                                        'attribution window',
                                        'Reddit ads account',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What ad accounts do I have?', 'What is the attribution window for my ad account?', 'Is my ad account in good standing?'],
                                    'search_strategy': 'Search by account name or ID',
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Reddit ad account with billing, attribution, and configuration settings.',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique ad account identifier (t2_ or a2_ prefix)'},
                    'name': {'type': 'string', 'description': 'Ad account name'},
                    'business_id': {'type': 'string', 'description': 'The business this account belongs to'},
                    'type': {
                        'type': 'string',
                        'enum': ['MANAGED', 'SELF_SERVE'],
                        'description': 'Account type',
                    },
                    'currency': {'type': 'string', 'description': 'Account currency code'},
                    'time_zone_id': {'type': 'string', 'description': 'Account time zone'},
                    'admin_approval': {
                        'type': 'string',
                        'enum': [
                            'ADMIN',
                            'BANNED',
                            'NEEDS_ID_VERIFICATION',
                            'PENDING',
                            'SUSPENDED',
                            'SUSPICIOUS',
                            'TRUSTED',
                            'VALID',
                        ],
                        'description': 'Admin approval status',
                    },
                    'attribution_type': {'type': 'string', 'description': 'Attribution type for web conversions'},
                    'click_attribution_window': {
                        'type': 'string',
                        'enum': ['DAY', 'MONTH', 'WEEK'],
                        'description': 'Click attribution window',
                    },
                    'view_attribution_window': {
                        'type': 'string',
                        'enum': ['DAY', 'MONTH', 'WEEK'],
                        'description': 'View attribution window',
                    },
                    'app_attribution_type': {'type': 'string', 'description': 'Attribution type for app events'},
                    'app_click_attribution_window': {'type': 'string', 'description': 'App click attribution window'},
                    'app_view_attribution_window': {'type': 'string', 'description': 'App view attribution window'},
                    'primary_contact_member_id': {'type': 'string', 'description': 'Primary contact member ID'},
                    'suspension_reason': {
                        'type': ['null', 'string'],
                        'description': 'Reason for account suspension, if applicable',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Account creation timestamp',
                    },
                    'modified_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'excluded_communities': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'List of excluded community IDs',
                    },
                    'excluded_keywords': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'List of excluded keywords',
                    },
                    'pixel_partner_preferences': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Pixel partner preferences',
                    },
                },
                'x-airbyte-entity-name': 'ad_accounts',
                'x-airbyte-ai-hints': {
                    'summary': 'Reddit advertising accounts with billing, attribution, and configuration settings',
                    'when_to_use': 'Questions about ad account setup, billing status, attribution windows, or account-level settings',
                    'trigger_phrases': [
                        'ad account',
                        'billing info',
                        'account status',
                        'attribution window',
                        'Reddit ads account',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What ad accounts do I have?', 'What is the attribution window for my ad account?', 'Is my ad account in good standing?'],
                    'search_strategy': 'Search by account name or ID',
                },
            },
            ai_hints={
                'summary': 'Reddit advertising accounts with billing, attribution, and configuration settings',
                'when_to_use': 'Questions about ad account setup, billing status, attribution windows, or account-level settings',
                'trigger_phrases': [
                    'ad account',
                    'billing info',
                    'account status',
                    'attribution window',
                    'Reddit ads account',
                ],
                'freshness': 'live',
                'example_questions': ['What ad accounts do I have?', 'What is the attribution window for my ad account?', 'Is my ad account in good standing?'],
                'search_strategy': 'Search by account name or ID',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='ad_accounts',
                    target_entity='businesses',
                    foreign_key='business_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='campaigns',
            stream_name='campaign',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}/campaigns',
                    action=Action.LIST,
                    description='Retrieve campaigns by ad account.',
                    query_params=['id', 'page.size', 'page.token'],
                    query_params_schema={
                        'id': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'string'},
                            'style': 'form',
                            'explode': False,
                        },
                        'page.size': {
                            'type': 'integer',
                            'required': False,
                            'maximum': 1000,
                        },
                        'page.token': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Reddit advertising campaign with objective, budget, and scheduling settings.',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                                        'name': {'type': 'string', 'description': 'Campaign name'},
                                        'ad_account_id': {'type': 'string', 'description': 'The ad account this campaign belongs to'},
                                        'objective': {
                                            'type': 'string',
                                            'enum': [
                                                'APP_INSTALLS',
                                                'CATALOG_SALES',
                                                'CLICKS',
                                                'CONVERSIONS',
                                                'IMPRESSIONS',
                                                'LEAD_GENERATION',
                                                'VIDEO_VIEWABLE_IMPRESSIONS',
                                            ],
                                            'description': 'Campaign objective',
                                        },
                                        'configured_status': {
                                            'type': 'string',
                                            'enum': [
                                                'ACTIVE',
                                                'ARCHIVED',
                                                'DELETED',
                                                'PAUSED',
                                            ],
                                            'description': 'User-configured status',
                                        },
                                        'effective_status': {
                                            'type': 'string',
                                            'enum': [
                                                'ACTIVE',
                                                'AD_GROUP_PAUSED',
                                                'ARCHIVED',
                                                'CAMPAIGN_PAUSED',
                                                'COMPLETED',
                                                'DELETED',
                                                'PAUSED',
                                                'PENDING_APPROVAL',
                                                'PENDING_BILLING_INFO',
                                                'PENDING_ID_VERIFICATION',
                                                'REJECTED',
                                                'PROCESSING',
                                            ],
                                            'description': 'Effective delivery status',
                                        },
                                        'delivery_status': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'Delivery status details',
                                        },
                                        'funding_instrument_id': {'type': 'string', 'description': 'Funding instrument ID'},
                                        'goal_type': {
                                            'type': 'string',
                                            'enum': ['LIFETIME_SPEND', 'DAILY_SPEND'],
                                            'description': 'Budget goal type',
                                        },
                                        'goal_value': {'type': 'integer', 'description': 'Budget goal value in microcurrency'},
                                        'is_campaign_budget_optimization': {'type': 'boolean', 'description': 'Whether campaign budget optimization is enabled'},
                                        'spend_cap': {
                                            'type': ['null', 'integer'],
                                            'description': 'Spend cap in microcurrency',
                                        },
                                        'start_time': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign start time in ISO 8601 format',
                                        },
                                        'end_time': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign end time in ISO 8601 format',
                                        },
                                        'optimization_goal': {
                                            'type': ['null', 'string'],
                                            'description': 'Optimization goal for the campaign',
                                        },
                                        'bid_strategy': {
                                            'type': ['null', 'string'],
                                            'description': 'Bid strategy',
                                        },
                                        'bid_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Bid type',
                                        },
                                        'bid_value': {
                                            'type': ['null', 'integer'],
                                            'description': 'Bid value in microcurrency',
                                        },
                                        'app_id': {
                                            'type': ['null', 'string'],
                                            'description': 'App Store or Play Store app ID',
                                        },
                                        'view_through_conversion_type': {
                                            'type': ['null', 'string'],
                                            'description': 'View-through conversion attribution type',
                                        },
                                        'special_ad_categories': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'Special ad categories',
                                        },
                                        'schedule': {'type': 'array', 'description': 'Weekly delivery schedule'},
                                        'skadnetwork_metadata': {
                                            'type': ['null', 'object'],
                                            'description': 'SKAdNetwork metadata for iOS attribution',
                                        },
                                        'age_restriction': {
                                            'type': ['null', 'string'],
                                            'description': 'Age restriction setting',
                                        },
                                        'invoice_label': {
                                            'type': ['null', 'string'],
                                            'description': 'Invoice label',
                                        },
                                        'conversion_pixel_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Conversion pixel ID',
                                        },
                                        'is_max': {'type': 'boolean', 'description': 'Whether this is a Max campaign'},
                                        'use_catalog': {'type': 'boolean', 'description': 'Whether this campaign uses a product catalog'},
                                        'type': {'type': 'string', 'description': 'Campaign type (MANUAL, AUTOMATED)'},
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Campaign creation timestamp',
                                        },
                                        'modified_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'campaign',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Reddit advertising campaigns with budget, objective, and scheduling configuration',
                                        'when_to_use': 'Questions about campaign setup, budgets, objectives, status, or performance settings',
                                        'trigger_phrases': [
                                            'campaign',
                                            'ad campaign',
                                            'campaign budget',
                                            'campaign objective',
                                            'campaign status',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What campaigns are currently active?', 'Which campaigns have the highest budget?', 'Show me campaigns with a conversions objective'],
                                        'search_strategy': 'Search by campaign name or filter by status and objective',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'description': 'Pagination metadata for list responses',
                                'properties': {
                                    'next_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for next page. Null if this is the last page.',
                                    },
                                    'previous_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for previous page. Null if this is the first page.',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_link': '$.pagination.next_url'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/campaigns/{campaign_id}',
                    action=Action.GET,
                    description='Retrieve a campaign by ID.',
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Reddit advertising campaign with objective, budget, and scheduling settings.',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                                    'name': {'type': 'string', 'description': 'Campaign name'},
                                    'ad_account_id': {'type': 'string', 'description': 'The ad account this campaign belongs to'},
                                    'objective': {
                                        'type': 'string',
                                        'enum': [
                                            'APP_INSTALLS',
                                            'CATALOG_SALES',
                                            'CLICKS',
                                            'CONVERSIONS',
                                            'IMPRESSIONS',
                                            'LEAD_GENERATION',
                                            'VIDEO_VIEWABLE_IMPRESSIONS',
                                        ],
                                        'description': 'Campaign objective',
                                    },
                                    'configured_status': {
                                        'type': 'string',
                                        'enum': [
                                            'ACTIVE',
                                            'ARCHIVED',
                                            'DELETED',
                                            'PAUSED',
                                        ],
                                        'description': 'User-configured status',
                                    },
                                    'effective_status': {
                                        'type': 'string',
                                        'enum': [
                                            'ACTIVE',
                                            'AD_GROUP_PAUSED',
                                            'ARCHIVED',
                                            'CAMPAIGN_PAUSED',
                                            'COMPLETED',
                                            'DELETED',
                                            'PAUSED',
                                            'PENDING_APPROVAL',
                                            'PENDING_BILLING_INFO',
                                            'PENDING_ID_VERIFICATION',
                                            'REJECTED',
                                            'PROCESSING',
                                        ],
                                        'description': 'Effective delivery status',
                                    },
                                    'delivery_status': {
                                        'type': ['null', 'array'],
                                        'items': {'type': 'string'},
                                        'description': 'Delivery status details',
                                    },
                                    'funding_instrument_id': {'type': 'string', 'description': 'Funding instrument ID'},
                                    'goal_type': {
                                        'type': 'string',
                                        'enum': ['LIFETIME_SPEND', 'DAILY_SPEND'],
                                        'description': 'Budget goal type',
                                    },
                                    'goal_value': {'type': 'integer', 'description': 'Budget goal value in microcurrency'},
                                    'is_campaign_budget_optimization': {'type': 'boolean', 'description': 'Whether campaign budget optimization is enabled'},
                                    'spend_cap': {
                                        'type': ['null', 'integer'],
                                        'description': 'Spend cap in microcurrency',
                                    },
                                    'start_time': {
                                        'type': ['null', 'string'],
                                        'description': 'Campaign start time in ISO 8601 format',
                                    },
                                    'end_time': {
                                        'type': ['null', 'string'],
                                        'description': 'Campaign end time in ISO 8601 format',
                                    },
                                    'optimization_goal': {
                                        'type': ['null', 'string'],
                                        'description': 'Optimization goal for the campaign',
                                    },
                                    'bid_strategy': {
                                        'type': ['null', 'string'],
                                        'description': 'Bid strategy',
                                    },
                                    'bid_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Bid type',
                                    },
                                    'bid_value': {
                                        'type': ['null', 'integer'],
                                        'description': 'Bid value in microcurrency',
                                    },
                                    'app_id': {
                                        'type': ['null', 'string'],
                                        'description': 'App Store or Play Store app ID',
                                    },
                                    'view_through_conversion_type': {
                                        'type': ['null', 'string'],
                                        'description': 'View-through conversion attribution type',
                                    },
                                    'special_ad_categories': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'Special ad categories',
                                    },
                                    'schedule': {'type': 'array', 'description': 'Weekly delivery schedule'},
                                    'skadnetwork_metadata': {
                                        'type': ['null', 'object'],
                                        'description': 'SKAdNetwork metadata for iOS attribution',
                                    },
                                    'age_restriction': {
                                        'type': ['null', 'string'],
                                        'description': 'Age restriction setting',
                                    },
                                    'invoice_label': {
                                        'type': ['null', 'string'],
                                        'description': 'Invoice label',
                                    },
                                    'conversion_pixel_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Conversion pixel ID',
                                    },
                                    'is_max': {'type': 'boolean', 'description': 'Whether this is a Max campaign'},
                                    'use_catalog': {'type': 'boolean', 'description': 'Whether this campaign uses a product catalog'},
                                    'type': {'type': 'string', 'description': 'Campaign type (MANUAL, AUTOMATED)'},
                                    'created_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Campaign creation timestamp',
                                    },
                                    'modified_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Last modification timestamp',
                                    },
                                },
                                'x-airbyte-entity-name': 'campaigns',
                                'x-airbyte-stream-name': 'campaign',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Reddit advertising campaigns with budget, objective, and scheduling configuration',
                                    'when_to_use': 'Questions about campaign setup, budgets, objectives, status, or performance settings',
                                    'trigger_phrases': [
                                        'campaign',
                                        'ad campaign',
                                        'campaign budget',
                                        'campaign objective',
                                        'campaign status',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What campaigns are currently active?', 'Which campaigns have the highest budget?', 'Show me campaigns with a conversions objective'],
                                    'search_strategy': 'Search by campaign name or filter by status and objective',
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Reddit advertising campaign with objective, budget, and scheduling settings.',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                    'name': {'type': 'string', 'description': 'Campaign name'},
                    'ad_account_id': {'type': 'string', 'description': 'The ad account this campaign belongs to'},
                    'objective': {
                        'type': 'string',
                        'enum': [
                            'APP_INSTALLS',
                            'CATALOG_SALES',
                            'CLICKS',
                            'CONVERSIONS',
                            'IMPRESSIONS',
                            'LEAD_GENERATION',
                            'VIDEO_VIEWABLE_IMPRESSIONS',
                        ],
                        'description': 'Campaign objective',
                    },
                    'configured_status': {
                        'type': 'string',
                        'enum': [
                            'ACTIVE',
                            'ARCHIVED',
                            'DELETED',
                            'PAUSED',
                        ],
                        'description': 'User-configured status',
                    },
                    'effective_status': {
                        'type': 'string',
                        'enum': [
                            'ACTIVE',
                            'AD_GROUP_PAUSED',
                            'ARCHIVED',
                            'CAMPAIGN_PAUSED',
                            'COMPLETED',
                            'DELETED',
                            'PAUSED',
                            'PENDING_APPROVAL',
                            'PENDING_BILLING_INFO',
                            'PENDING_ID_VERIFICATION',
                            'REJECTED',
                            'PROCESSING',
                        ],
                        'description': 'Effective delivery status',
                    },
                    'delivery_status': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'Delivery status details',
                    },
                    'funding_instrument_id': {'type': 'string', 'description': 'Funding instrument ID'},
                    'goal_type': {
                        'type': 'string',
                        'enum': ['LIFETIME_SPEND', 'DAILY_SPEND'],
                        'description': 'Budget goal type',
                    },
                    'goal_value': {'type': 'integer', 'description': 'Budget goal value in microcurrency'},
                    'is_campaign_budget_optimization': {'type': 'boolean', 'description': 'Whether campaign budget optimization is enabled'},
                    'spend_cap': {
                        'type': ['null', 'integer'],
                        'description': 'Spend cap in microcurrency',
                    },
                    'start_time': {
                        'type': ['null', 'string'],
                        'description': 'Campaign start time in ISO 8601 format',
                    },
                    'end_time': {
                        'type': ['null', 'string'],
                        'description': 'Campaign end time in ISO 8601 format',
                    },
                    'optimization_goal': {
                        'type': ['null', 'string'],
                        'description': 'Optimization goal for the campaign',
                    },
                    'bid_strategy': {
                        'type': ['null', 'string'],
                        'description': 'Bid strategy',
                    },
                    'bid_type': {
                        'type': ['null', 'string'],
                        'description': 'Bid type',
                    },
                    'bid_value': {
                        'type': ['null', 'integer'],
                        'description': 'Bid value in microcurrency',
                    },
                    'app_id': {
                        'type': ['null', 'string'],
                        'description': 'App Store or Play Store app ID',
                    },
                    'view_through_conversion_type': {
                        'type': ['null', 'string'],
                        'description': 'View-through conversion attribution type',
                    },
                    'special_ad_categories': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Special ad categories',
                    },
                    'schedule': {'type': 'array', 'description': 'Weekly delivery schedule'},
                    'skadnetwork_metadata': {
                        'type': ['null', 'object'],
                        'description': 'SKAdNetwork metadata for iOS attribution',
                    },
                    'age_restriction': {
                        'type': ['null', 'string'],
                        'description': 'Age restriction setting',
                    },
                    'invoice_label': {
                        'type': ['null', 'string'],
                        'description': 'Invoice label',
                    },
                    'conversion_pixel_id': {
                        'type': ['null', 'string'],
                        'description': 'Conversion pixel ID',
                    },
                    'is_max': {'type': 'boolean', 'description': 'Whether this is a Max campaign'},
                    'use_catalog': {'type': 'boolean', 'description': 'Whether this campaign uses a product catalog'},
                    'type': {'type': 'string', 'description': 'Campaign type (MANUAL, AUTOMATED)'},
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Campaign creation timestamp',
                    },
                    'modified_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                },
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'campaign',
                'x-airbyte-ai-hints': {
                    'summary': 'Reddit advertising campaigns with budget, objective, and scheduling configuration',
                    'when_to_use': 'Questions about campaign setup, budgets, objectives, status, or performance settings',
                    'trigger_phrases': [
                        'campaign',
                        'ad campaign',
                        'campaign budget',
                        'campaign objective',
                        'campaign status',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What campaigns are currently active?', 'Which campaigns have the highest budget?', 'Show me campaigns with a conversions objective'],
                    'search_strategy': 'Search by campaign name or filter by status and objective',
                },
            },
            ai_hints={
                'summary': 'Reddit advertising campaigns with budget, objective, and scheduling configuration',
                'when_to_use': 'Questions about campaign setup, budgets, objectives, status, or performance settings',
                'trigger_phrases': [
                    'campaign',
                    'ad campaign',
                    'campaign budget',
                    'campaign objective',
                    'campaign status',
                ],
                'freshness': 'live',
                'example_questions': ['What campaigns are currently active?', 'Which campaigns have the highest budget?', 'Show me campaigns with a conversions objective'],
                'search_strategy': 'Search by campaign name or filter by status and objective',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='campaigns',
                    target_entity='ad_accounts',
                    foreign_key='ad_account_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='ad_groups',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}/ad_groups',
                    action=Action.LIST,
                    description='Retrieve ad groups by ad account.',
                    query_params=['campaign_id', 'page.size', 'page.token'],
                    query_params_schema={
                        'campaign_id': {'type': 'string', 'required': False},
                        'page.size': {
                            'type': 'integer',
                            'required': False,
                            'maximum': 1000,
                        },
                        'page.token': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Reddit ad group with targeting, bidding, and scheduling settings.',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique ad group identifier'},
                                        'name': {'type': 'string', 'description': 'Ad group name'},
                                        'type': {
                                            'type': 'string',
                                            'enum': ['MANUAL', 'AUTOMATED'],
                                            'description': 'Ad group type',
                                        },
                                        'ad_account_id': {'type': 'string', 'description': 'The ad account this ad group belongs to'},
                                        'campaign_id': {'type': 'string', 'description': 'The campaign this ad group belongs to'},
                                        'configured_status': {
                                            'type': 'string',
                                            'enum': [
                                                'ACTIVE',
                                                'ARCHIVED',
                                                'DELETED',
                                                'PAUSED',
                                            ],
                                            'description': 'User-configured status',
                                        },
                                        'effective_status': {
                                            'type': 'string',
                                            'enum': [
                                                'ACTIVE',
                                                'AD_GROUP_PAUSED',
                                                'ARCHIVED',
                                                'CAMPAIGN_PAUSED',
                                                'COMPLETED',
                                                'DELETED',
                                                'PAUSED',
                                                'PENDING_APPROVAL',
                                                'PENDING_BILLING_INFO',
                                                'PENDING_ID_VERIFICATION',
                                                'REJECTED',
                                                'PROCESSING',
                                            ],
                                            'description': 'Effective delivery status',
                                        },
                                        'delivery_status': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'Delivery status details',
                                        },
                                        'bid_strategy': {
                                            'type': ['null', 'string'],
                                            'description': 'Bid strategy',
                                        },
                                        'bid_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Bid type',
                                        },
                                        'bid_value': {
                                            'type': ['null', 'integer'],
                                            'description': 'Bid value in microcurrency',
                                        },
                                        'optimization_goal': {
                                            'type': ['null', 'string'],
                                            'description': 'Optimization goal',
                                        },
                                        'campaign_objective_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign objective type inherited from parent campaign',
                                        },
                                        'goal_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Goal type',
                                        },
                                        'goal_value': {
                                            'type': ['null', 'integer'],
                                            'description': 'Goal value in microcurrency',
                                        },
                                        'is_campaign_budget_optimization': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether campaign budget optimization is enabled',
                                        },
                                        'start_time': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad group start time in ISO 8601 format',
                                        },
                                        'end_time': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad group end time in ISO 8601 format',
                                        },
                                        'targeting': {
                                            'type': 'object',
                                            'additionalProperties': True,
                                            'description': 'Targeting configuration',
                                            'properties': {
                                                'communities': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Targeted community subreddit names',
                                                },
                                                'custom_audience_ids': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Custom audience IDs to target',
                                                },
                                                'excluded_communities': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Excluded community subreddit names',
                                                },
                                                'excluded_custom_audience_ids': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Excluded custom audience IDs',
                                                },
                                                'excluded_geolocations': {
                                                    'type': 'array',
                                                    'items': {'type': 'object'},
                                                    'description': 'Excluded geographic locations',
                                                },
                                                'excluded_keywords': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Excluded keywords for targeting',
                                                },
                                                'expand_targeting': {'type': 'boolean', 'description': 'Whether to expand targeting beyond specified criteria'},
                                                'geolocations': {
                                                    'type': 'array',
                                                    'items': {'type': 'object'},
                                                    'description': 'Targeted geographic locations',
                                                },
                                                'interests': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Interest category IDs for targeting',
                                                },
                                                'devices': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'description': 'Device type (DESKTOP, MOBILE)'},
                                                            'os': {
                                                                'type': ['null', 'string'],
                                                                'description': 'Device OS (ANDROID, IOS)',
                                                            },
                                                            'min_version': {
                                                                'type': ['null', 'string'],
                                                                'description': 'Minimum major OS version',
                                                            },
                                                            'max_version': {
                                                                'type': ['null', 'string'],
                                                                'description': 'Maximum major OS version',
                                                            },
                                                            'label_map': {
                                                                'type': ['null', 'object'],
                                                                'additionalProperties': True,
                                                                'description': 'Device models to target, keyed by make',
                                                            },
                                                        },
                                                    },
                                                    'description': 'Targeted devices (type/OS/version constraints)',
                                                },
                                                'locations': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Ad placement locations (e.g. FEED, COMMENTS_PAGE)',
                                                },
                                                'platforms': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Targeted platforms (e.g. ALL, IOS, ANDROID)',
                                                },
                                                'view_modes': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'View mode targeting (e.g. ALL)',
                                                },
                                                'suppression_event_types': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Event types to suppress for retargeting',
                                                },
                                                'gender': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Gender targeting filter',
                                                },
                                                'carriers': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Mobile carrier targeting',
                                                },
                                                'keywords': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                    'description': 'Keyword targeting terms',
                                                },
                                                'age_targeting': {
                                                    'type': 'object',
                                                    'additionalProperties': True,
                                                    'description': 'Age range targeting configuration',
                                                },
                                                'languages': {
                                                    'type': ['null', 'array'],
                                                    'items': {'type': 'string'},
                                                    'description': 'Language targeting codes',
                                                },
                                            },
                                        },
                                        'view_through_conversion_type': {
                                            'type': ['null', 'string'],
                                            'description': 'View-through conversion attribution type',
                                        },
                                        'conversion_pixel_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Conversion pixel ID',
                                        },
                                        'app_id': {
                                            'type': ['null', 'string'],
                                            'description': 'App ID for app install campaigns',
                                        },
                                        'optimization_strategy_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Optimization strategy type',
                                        },
                                        'product_set_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Product set ID for catalog sales',
                                        },
                                        'saved_audience_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Saved audience ID',
                                        },
                                        'schedule': {'type': 'array', 'description': 'Weekly delivery schedule'},
                                        'skadnetwork_metadata': {
                                            'type': ['null', 'object'],
                                            'description': 'SKAdNetwork metadata for iOS attribution',
                                        },
                                        'shopping_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Shopping type for catalog campaigns',
                                        },
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Ad group creation timestamp',
                                        },
                                        'modified_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ad_groups',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Reddit ad groups with targeting, bidding, and scheduling settings within campaigns',
                                        'when_to_use': 'Questions about ad group targeting, bid settings, optimization, or scheduling',
                                        'trigger_phrases': [
                                            'ad group',
                                            'targeting',
                                            'bid settings',
                                            'ad set',
                                            'audience targeting',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What ad groups are in my campaign?', 'Show me ad groups with CPC bidding', 'Which ad groups are paused?'],
                                        'search_strategy': 'Search by ad group name, filter by campaign or status',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'description': 'Pagination metadata for list responses',
                                'properties': {
                                    'next_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for next page. Null if this is the last page.',
                                    },
                                    'previous_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for previous page. Null if this is the first page.',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_link': '$.pagination.next_url'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/ad_groups/{ad_group_id}',
                    action=Action.GET,
                    description='Retrieve an ad group by ID.',
                    path_params=['ad_group_id'],
                    path_params_schema={
                        'ad_group_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Reddit ad group with targeting, bidding, and scheduling settings.',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique ad group identifier'},
                                    'name': {'type': 'string', 'description': 'Ad group name'},
                                    'type': {
                                        'type': 'string',
                                        'enum': ['MANUAL', 'AUTOMATED'],
                                        'description': 'Ad group type',
                                    },
                                    'ad_account_id': {'type': 'string', 'description': 'The ad account this ad group belongs to'},
                                    'campaign_id': {'type': 'string', 'description': 'The campaign this ad group belongs to'},
                                    'configured_status': {
                                        'type': 'string',
                                        'enum': [
                                            'ACTIVE',
                                            'ARCHIVED',
                                            'DELETED',
                                            'PAUSED',
                                        ],
                                        'description': 'User-configured status',
                                    },
                                    'effective_status': {
                                        'type': 'string',
                                        'enum': [
                                            'ACTIVE',
                                            'AD_GROUP_PAUSED',
                                            'ARCHIVED',
                                            'CAMPAIGN_PAUSED',
                                            'COMPLETED',
                                            'DELETED',
                                            'PAUSED',
                                            'PENDING_APPROVAL',
                                            'PENDING_BILLING_INFO',
                                            'PENDING_ID_VERIFICATION',
                                            'REJECTED',
                                            'PROCESSING',
                                        ],
                                        'description': 'Effective delivery status',
                                    },
                                    'delivery_status': {
                                        'type': ['null', 'array'],
                                        'items': {'type': 'string'},
                                        'description': 'Delivery status details',
                                    },
                                    'bid_strategy': {
                                        'type': ['null', 'string'],
                                        'description': 'Bid strategy',
                                    },
                                    'bid_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Bid type',
                                    },
                                    'bid_value': {
                                        'type': ['null', 'integer'],
                                        'description': 'Bid value in microcurrency',
                                    },
                                    'optimization_goal': {
                                        'type': ['null', 'string'],
                                        'description': 'Optimization goal',
                                    },
                                    'campaign_objective_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Campaign objective type inherited from parent campaign',
                                    },
                                    'goal_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Goal type',
                                    },
                                    'goal_value': {
                                        'type': ['null', 'integer'],
                                        'description': 'Goal value in microcurrency',
                                    },
                                    'is_campaign_budget_optimization': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether campaign budget optimization is enabled',
                                    },
                                    'start_time': {
                                        'type': ['null', 'string'],
                                        'description': 'Ad group start time in ISO 8601 format',
                                    },
                                    'end_time': {
                                        'type': ['null', 'string'],
                                        'description': 'Ad group end time in ISO 8601 format',
                                    },
                                    'targeting': {
                                        'type': 'object',
                                        'additionalProperties': True,
                                        'description': 'Targeting configuration',
                                        'properties': {
                                            'communities': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Targeted community subreddit names',
                                            },
                                            'custom_audience_ids': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Custom audience IDs to target',
                                            },
                                            'excluded_communities': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Excluded community subreddit names',
                                            },
                                            'excluded_custom_audience_ids': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Excluded custom audience IDs',
                                            },
                                            'excluded_geolocations': {
                                                'type': 'array',
                                                'items': {'type': 'object'},
                                                'description': 'Excluded geographic locations',
                                            },
                                            'excluded_keywords': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Excluded keywords for targeting',
                                            },
                                            'expand_targeting': {'type': 'boolean', 'description': 'Whether to expand targeting beyond specified criteria'},
                                            'geolocations': {
                                                'type': 'array',
                                                'items': {'type': 'object'},
                                                'description': 'Targeted geographic locations',
                                            },
                                            'interests': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Interest category IDs for targeting',
                                            },
                                            'devices': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'type': {'type': 'string', 'description': 'Device type (DESKTOP, MOBILE)'},
                                                        'os': {
                                                            'type': ['null', 'string'],
                                                            'description': 'Device OS (ANDROID, IOS)',
                                                        },
                                                        'min_version': {
                                                            'type': ['null', 'string'],
                                                            'description': 'Minimum major OS version',
                                                        },
                                                        'max_version': {
                                                            'type': ['null', 'string'],
                                                            'description': 'Maximum major OS version',
                                                        },
                                                        'label_map': {
                                                            'type': ['null', 'object'],
                                                            'additionalProperties': True,
                                                            'description': 'Device models to target, keyed by make',
                                                        },
                                                    },
                                                },
                                                'description': 'Targeted devices (type/OS/version constraints)',
                                            },
                                            'locations': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Ad placement locations (e.g. FEED, COMMENTS_PAGE)',
                                            },
                                            'platforms': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Targeted platforms (e.g. ALL, IOS, ANDROID)',
                                            },
                                            'view_modes': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'View mode targeting (e.g. ALL)',
                                            },
                                            'suppression_event_types': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Event types to suppress for retargeting',
                                            },
                                            'gender': {
                                                'type': ['null', 'string'],
                                                'description': 'Gender targeting filter',
                                            },
                                            'carriers': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Mobile carrier targeting',
                                            },
                                            'keywords': {
                                                'type': 'array',
                                                'items': {'type': 'string'},
                                                'description': 'Keyword targeting terms',
                                            },
                                            'age_targeting': {
                                                'type': 'object',
                                                'additionalProperties': True,
                                                'description': 'Age range targeting configuration',
                                            },
                                            'languages': {
                                                'type': ['null', 'array'],
                                                'items': {'type': 'string'},
                                                'description': 'Language targeting codes',
                                            },
                                        },
                                    },
                                    'view_through_conversion_type': {
                                        'type': ['null', 'string'],
                                        'description': 'View-through conversion attribution type',
                                    },
                                    'conversion_pixel_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Conversion pixel ID',
                                    },
                                    'app_id': {
                                        'type': ['null', 'string'],
                                        'description': 'App ID for app install campaigns',
                                    },
                                    'optimization_strategy_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Optimization strategy type',
                                    },
                                    'product_set_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Product set ID for catalog sales',
                                    },
                                    'saved_audience_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Saved audience ID',
                                    },
                                    'schedule': {'type': 'array', 'description': 'Weekly delivery schedule'},
                                    'skadnetwork_metadata': {
                                        'type': ['null', 'object'],
                                        'description': 'SKAdNetwork metadata for iOS attribution',
                                    },
                                    'shopping_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Shopping type for catalog campaigns',
                                    },
                                    'created_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Ad group creation timestamp',
                                    },
                                    'modified_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Last modification timestamp',
                                    },
                                },
                                'x-airbyte-entity-name': 'ad_groups',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Reddit ad groups with targeting, bidding, and scheduling settings within campaigns',
                                    'when_to_use': 'Questions about ad group targeting, bid settings, optimization, or scheduling',
                                    'trigger_phrases': [
                                        'ad group',
                                        'targeting',
                                        'bid settings',
                                        'ad set',
                                        'audience targeting',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What ad groups are in my campaign?', 'Show me ad groups with CPC bidding', 'Which ad groups are paused?'],
                                    'search_strategy': 'Search by ad group name, filter by campaign or status',
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Reddit ad group with targeting, bidding, and scheduling settings.',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique ad group identifier'},
                    'name': {'type': 'string', 'description': 'Ad group name'},
                    'type': {
                        'type': 'string',
                        'enum': ['MANUAL', 'AUTOMATED'],
                        'description': 'Ad group type',
                    },
                    'ad_account_id': {'type': 'string', 'description': 'The ad account this ad group belongs to'},
                    'campaign_id': {'type': 'string', 'description': 'The campaign this ad group belongs to'},
                    'configured_status': {
                        'type': 'string',
                        'enum': [
                            'ACTIVE',
                            'ARCHIVED',
                            'DELETED',
                            'PAUSED',
                        ],
                        'description': 'User-configured status',
                    },
                    'effective_status': {
                        'type': 'string',
                        'enum': [
                            'ACTIVE',
                            'AD_GROUP_PAUSED',
                            'ARCHIVED',
                            'CAMPAIGN_PAUSED',
                            'COMPLETED',
                            'DELETED',
                            'PAUSED',
                            'PENDING_APPROVAL',
                            'PENDING_BILLING_INFO',
                            'PENDING_ID_VERIFICATION',
                            'REJECTED',
                            'PROCESSING',
                        ],
                        'description': 'Effective delivery status',
                    },
                    'delivery_status': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'Delivery status details',
                    },
                    'bid_strategy': {
                        'type': ['null', 'string'],
                        'description': 'Bid strategy',
                    },
                    'bid_type': {
                        'type': ['null', 'string'],
                        'description': 'Bid type',
                    },
                    'bid_value': {
                        'type': ['null', 'integer'],
                        'description': 'Bid value in microcurrency',
                    },
                    'optimization_goal': {
                        'type': ['null', 'string'],
                        'description': 'Optimization goal',
                    },
                    'campaign_objective_type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign objective type inherited from parent campaign',
                    },
                    'goal_type': {
                        'type': ['null', 'string'],
                        'description': 'Goal type',
                    },
                    'goal_value': {
                        'type': ['null', 'integer'],
                        'description': 'Goal value in microcurrency',
                    },
                    'is_campaign_budget_optimization': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether campaign budget optimization is enabled',
                    },
                    'start_time': {
                        'type': ['null', 'string'],
                        'description': 'Ad group start time in ISO 8601 format',
                    },
                    'end_time': {
                        'type': ['null', 'string'],
                        'description': 'Ad group end time in ISO 8601 format',
                    },
                    'targeting': {
                        'type': 'object',
                        'additionalProperties': True,
                        'description': 'Targeting configuration',
                        'properties': {
                            'communities': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Targeted community subreddit names',
                            },
                            'custom_audience_ids': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Custom audience IDs to target',
                            },
                            'excluded_communities': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Excluded community subreddit names',
                            },
                            'excluded_custom_audience_ids': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Excluded custom audience IDs',
                            },
                            'excluded_geolocations': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Excluded geographic locations',
                            },
                            'excluded_keywords': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Excluded keywords for targeting',
                            },
                            'expand_targeting': {'type': 'boolean', 'description': 'Whether to expand targeting beyond specified criteria'},
                            'geolocations': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Targeted geographic locations',
                            },
                            'interests': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Interest category IDs for targeting',
                            },
                            'devices': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'type': {'type': 'string', 'description': 'Device type (DESKTOP, MOBILE)'},
                                        'os': {
                                            'type': ['null', 'string'],
                                            'description': 'Device OS (ANDROID, IOS)',
                                        },
                                        'min_version': {
                                            'type': ['null', 'string'],
                                            'description': 'Minimum major OS version',
                                        },
                                        'max_version': {
                                            'type': ['null', 'string'],
                                            'description': 'Maximum major OS version',
                                        },
                                        'label_map': {
                                            'type': ['null', 'object'],
                                            'additionalProperties': True,
                                            'description': 'Device models to target, keyed by make',
                                        },
                                    },
                                },
                                'description': 'Targeted devices (type/OS/version constraints)',
                            },
                            'locations': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Ad placement locations (e.g. FEED, COMMENTS_PAGE)',
                            },
                            'platforms': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Targeted platforms (e.g. ALL, IOS, ANDROID)',
                            },
                            'view_modes': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'View mode targeting (e.g. ALL)',
                            },
                            'suppression_event_types': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Event types to suppress for retargeting',
                            },
                            'gender': {
                                'type': ['null', 'string'],
                                'description': 'Gender targeting filter',
                            },
                            'carriers': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Mobile carrier targeting',
                            },
                            'keywords': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Keyword targeting terms',
                            },
                            'age_targeting': {
                                'type': 'object',
                                'additionalProperties': True,
                                'description': 'Age range targeting configuration',
                            },
                            'languages': {
                                'type': ['null', 'array'],
                                'items': {'type': 'string'},
                                'description': 'Language targeting codes',
                            },
                        },
                    },
                    'view_through_conversion_type': {
                        'type': ['null', 'string'],
                        'description': 'View-through conversion attribution type',
                    },
                    'conversion_pixel_id': {
                        'type': ['null', 'string'],
                        'description': 'Conversion pixel ID',
                    },
                    'app_id': {
                        'type': ['null', 'string'],
                        'description': 'App ID for app install campaigns',
                    },
                    'optimization_strategy_type': {
                        'type': ['null', 'string'],
                        'description': 'Optimization strategy type',
                    },
                    'product_set_id': {
                        'type': ['null', 'string'],
                        'description': 'Product set ID for catalog sales',
                    },
                    'saved_audience_id': {
                        'type': ['null', 'string'],
                        'description': 'Saved audience ID',
                    },
                    'schedule': {'type': 'array', 'description': 'Weekly delivery schedule'},
                    'skadnetwork_metadata': {
                        'type': ['null', 'object'],
                        'description': 'SKAdNetwork metadata for iOS attribution',
                    },
                    'shopping_type': {
                        'type': ['null', 'string'],
                        'description': 'Shopping type for catalog campaigns',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Ad group creation timestamp',
                    },
                    'modified_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                },
                'x-airbyte-entity-name': 'ad_groups',
                'x-airbyte-ai-hints': {
                    'summary': 'Reddit ad groups with targeting, bidding, and scheduling settings within campaigns',
                    'when_to_use': 'Questions about ad group targeting, bid settings, optimization, or scheduling',
                    'trigger_phrases': [
                        'ad group',
                        'targeting',
                        'bid settings',
                        'ad set',
                        'audience targeting',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What ad groups are in my campaign?', 'Show me ad groups with CPC bidding', 'Which ad groups are paused?'],
                    'search_strategy': 'Search by ad group name, filter by campaign or status',
                },
            },
            ai_hints={
                'summary': 'Reddit ad groups with targeting, bidding, and scheduling settings within campaigns',
                'when_to_use': 'Questions about ad group targeting, bid settings, optimization, or scheduling',
                'trigger_phrases': [
                    'ad group',
                    'targeting',
                    'bid settings',
                    'ad set',
                    'audience targeting',
                ],
                'freshness': 'live',
                'example_questions': ['What ad groups are in my campaign?', 'Show me ad groups with CPC bidding', 'Which ad groups are paused?'],
                'search_strategy': 'Search by ad group name, filter by campaign or status',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='ad_groups',
                    target_entity='ad_accounts',
                    foreign_key='ad_account_id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='ad_groups',
                    target_entity='campaigns',
                    foreign_key='campaign_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='ads',
            stream_name='ad',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ad_accounts/{ad_account_id}/ads',
                    action=Action.LIST,
                    description='Retrieve ads by ad account. Filters combine with logical AND across different query parameters.\n',
                    query_params=[
                        'campaign_id',
                        'ad_group_id',
                        'configured_status',
                        'effective_status',
                        'page.size',
                        'page.token',
                    ],
                    query_params_schema={
                        'campaign_id': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'string'},
                            'style': 'form',
                            'explode': False,
                        },
                        'ad_group_id': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'string'},
                            'style': 'form',
                            'explode': False,
                        },
                        'configured_status': {
                            'type': 'array',
                            'required': False,
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'ACTIVE',
                                    'ARCHIVED',
                                    'DELETED',
                                    'PAUSED',
                                ],
                            },
                            'style': 'form',
                            'explode': False,
                        },
                        'effective_status': {
                            'type': 'array',
                            'required': False,
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'ACTIVE',
                                    'AD_GROUP_PAUSED',
                                    'ARCHIVED',
                                    'CAMPAIGN_PAUSED',
                                    'COMPLETED',
                                    'DELETED',
                                    'MISSING_PERMISSIONS',
                                    'PAUSED',
                                    'PENDING_APPROVAL',
                                    'PENDING_BILLING_INFO',
                                    'PENDING_ID_VERIFICATION',
                                    'PROCESSING',
                                    'REJECTED',
                                ],
                            },
                            'style': 'form',
                            'explode': False,
                        },
                        'page.size': {
                            'type': 'integer',
                            'required': False,
                            'maximum': 1000,
                        },
                        'page.token': {'type': 'string', 'required': False},
                    },
                    path_params=['ad_account_id'],
                    path_params_schema={
                        'ad_account_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Reddit ad with creative configuration, status, and tracking settings.',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique ad identifier'},
                                        'name': {'type': 'string', 'description': 'Ad name'},
                                        'type': {
                                            'type': 'string',
                                            'enum': ['UNSPECIFIED', 'DYNAMIC_CREATIVE_AD_TEMPLATE'],
                                            'description': 'Ad type',
                                        },
                                        'ad_account_id': {'type': 'string', 'description': 'The ad account this ad belongs to'},
                                        'ad_group_id': {'type': 'string', 'description': 'The ad group this ad belongs to'},
                                        'campaign_id': {'type': 'string', 'description': 'The campaign this ad belongs to'},
                                        'campaign_objective_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign objective type',
                                        },
                                        'click_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Click destination URL',
                                        },
                                        'click_url_query_parameters': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'value': {'type': 'string'},
                                                },
                                            },
                                            'description': 'Query parameters appended to click URL',
                                        },
                                        'configured_status': {
                                            'type': 'string',
                                            'enum': [
                                                'ACTIVE',
                                                'ARCHIVED',
                                                'DELETED',
                                                'PAUSED',
                                            ],
                                            'description': 'User-configured status',
                                        },
                                        'effective_status': {
                                            'type': 'string',
                                            'enum': [
                                                'ACTIVE',
                                                'AD_GROUP_PAUSED',
                                                'ARCHIVED',
                                                'CAMPAIGN_PAUSED',
                                                'COMPLETED',
                                                'DELETED',
                                                'MISSING_PERMISSIONS',
                                                'PAUSED',
                                                'PENDING_APPROVAL',
                                                'PENDING_BILLING_INFO',
                                                'PENDING_ID_VERIFICATION',
                                                'PROCESSING',
                                                'REJECTED',
                                            ],
                                            'description': 'Effective delivery status',
                                        },
                                        'delivery_status': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'Delivery status details',
                                        },
                                        'event_trackers': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'type': {
                                                        'type': 'string',
                                                        'enum': ['CLICK', 'VIEW'],
                                                    },
                                                    'url': {'type': 'string'},
                                                },
                                            },
                                            'description': 'Click and impression tracking URLs',
                                        },
                                        'post_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Reddit post ID (t3_ prefix)',
                                        },
                                        'post_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Reddit post URL',
                                        },
                                        'preview_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Ad preview URL',
                                        },
                                        'preview_expiry': {
                                            'type': ['null', 'string'],
                                            'description': 'Preview URL expiration timestamp',
                                        },
                                        'rejection_reason': {
                                            'type': ['null', 'string'],
                                            'description': 'Reason the ad was rejected',
                                        },
                                        'profile_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Reddit profile ID used for the ad',
                                        },
                                        'products': {
                                            'type': ['null', 'array'],
                                            'description': 'Product items for catalog ads',
                                        },
                                        'shopping_creative': {
                                            'type': ['null', 'object'],
                                            'description': 'Shopping creative configuration',
                                        },
                                        'skadnetwork_metadata': {
                                            'type': ['null', 'object'],
                                            'description': 'SKAdNetwork metadata for iOS app install attribution',
                                        },
                                        'extensions': {
                                            'type': ['null', 'object'],
                                            'description': 'Ad extensions',
                                        },
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Ad creation timestamp',
                                        },
                                        'modified_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ads',
                                    'x-airbyte-stream-name': 'ad',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Reddit ads with creative configuration, click URLs, event trackers, and approval status',
                                        'when_to_use': 'Questions about individual ads, creatives, ad approval status, or click destinations',
                                        'trigger_phrases': [
                                            'ad',
                                            'creative',
                                            'ad status',
                                            'ad approval',
                                            'promoted post',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show me all active ads', 'Which ads were rejected and why?', 'What ads are in my campaign?'],
                                        'search_strategy': 'Search by ad name, filter by status, campaign, or ad group',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'description': 'Pagination metadata for list responses',
                                'properties': {
                                    'next_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for next page. Null if this is the last page.',
                                    },
                                    'previous_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Full URL for previous page. Null if this is the first page.',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_link': '$.pagination.next_url'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/ads/{ad_id}',
                    action=Action.GET,
                    description='Retrieve an ad by ID.',
                    path_params=['ad_id'],
                    path_params_schema={
                        'ad_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A Reddit ad with creative configuration, status, and tracking settings.',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique ad identifier'},
                                    'name': {'type': 'string', 'description': 'Ad name'},
                                    'type': {
                                        'type': 'string',
                                        'enum': ['UNSPECIFIED', 'DYNAMIC_CREATIVE_AD_TEMPLATE'],
                                        'description': 'Ad type',
                                    },
                                    'ad_account_id': {'type': 'string', 'description': 'The ad account this ad belongs to'},
                                    'ad_group_id': {'type': 'string', 'description': 'The ad group this ad belongs to'},
                                    'campaign_id': {'type': 'string', 'description': 'The campaign this ad belongs to'},
                                    'campaign_objective_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Campaign objective type',
                                    },
                                    'click_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Click destination URL',
                                    },
                                    'click_url_query_parameters': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'name': {'type': 'string'},
                                                'value': {'type': 'string'},
                                            },
                                        },
                                        'description': 'Query parameters appended to click URL',
                                    },
                                    'configured_status': {
                                        'type': 'string',
                                        'enum': [
                                            'ACTIVE',
                                            'ARCHIVED',
                                            'DELETED',
                                            'PAUSED',
                                        ],
                                        'description': 'User-configured status',
                                    },
                                    'effective_status': {
                                        'type': 'string',
                                        'enum': [
                                            'ACTIVE',
                                            'AD_GROUP_PAUSED',
                                            'ARCHIVED',
                                            'CAMPAIGN_PAUSED',
                                            'COMPLETED',
                                            'DELETED',
                                            'MISSING_PERMISSIONS',
                                            'PAUSED',
                                            'PENDING_APPROVAL',
                                            'PENDING_BILLING_INFO',
                                            'PENDING_ID_VERIFICATION',
                                            'PROCESSING',
                                            'REJECTED',
                                        ],
                                        'description': 'Effective delivery status',
                                    },
                                    'delivery_status': {
                                        'type': ['null', 'array'],
                                        'items': {'type': 'string'},
                                        'description': 'Delivery status details',
                                    },
                                    'event_trackers': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {
                                                    'type': 'string',
                                                    'enum': ['CLICK', 'VIEW'],
                                                },
                                                'url': {'type': 'string'},
                                            },
                                        },
                                        'description': 'Click and impression tracking URLs',
                                    },
                                    'post_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Reddit post ID (t3_ prefix)',
                                    },
                                    'post_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Reddit post URL',
                                    },
                                    'preview_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Ad preview URL',
                                    },
                                    'preview_expiry': {
                                        'type': ['null', 'string'],
                                        'description': 'Preview URL expiration timestamp',
                                    },
                                    'rejection_reason': {
                                        'type': ['null', 'string'],
                                        'description': 'Reason the ad was rejected',
                                    },
                                    'profile_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Reddit profile ID used for the ad',
                                    },
                                    'products': {
                                        'type': ['null', 'array'],
                                        'description': 'Product items for catalog ads',
                                    },
                                    'shopping_creative': {
                                        'type': ['null', 'object'],
                                        'description': 'Shopping creative configuration',
                                    },
                                    'skadnetwork_metadata': {
                                        'type': ['null', 'object'],
                                        'description': 'SKAdNetwork metadata for iOS app install attribution',
                                    },
                                    'extensions': {
                                        'type': ['null', 'object'],
                                        'description': 'Ad extensions',
                                    },
                                    'created_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Ad creation timestamp',
                                    },
                                    'modified_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Last modification timestamp',
                                    },
                                },
                                'x-airbyte-entity-name': 'ads',
                                'x-airbyte-stream-name': 'ad',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Reddit ads with creative configuration, click URLs, event trackers, and approval status',
                                    'when_to_use': 'Questions about individual ads, creatives, ad approval status, or click destinations',
                                    'trigger_phrases': [
                                        'ad',
                                        'creative',
                                        'ad status',
                                        'ad approval',
                                        'promoted post',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Show me all active ads', 'Which ads were rejected and why?', 'What ads are in my campaign?'],
                                    'search_strategy': 'Search by ad name, filter by status, campaign, or ad group',
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Reddit ad with creative configuration, status, and tracking settings.',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique ad identifier'},
                    'name': {'type': 'string', 'description': 'Ad name'},
                    'type': {
                        'type': 'string',
                        'enum': ['UNSPECIFIED', 'DYNAMIC_CREATIVE_AD_TEMPLATE'],
                        'description': 'Ad type',
                    },
                    'ad_account_id': {'type': 'string', 'description': 'The ad account this ad belongs to'},
                    'ad_group_id': {'type': 'string', 'description': 'The ad group this ad belongs to'},
                    'campaign_id': {'type': 'string', 'description': 'The campaign this ad belongs to'},
                    'campaign_objective_type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign objective type',
                    },
                    'click_url': {
                        'type': ['null', 'string'],
                        'description': 'Click destination URL',
                    },
                    'click_url_query_parameters': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'name': {'type': 'string'},
                                'value': {'type': 'string'},
                            },
                        },
                        'description': 'Query parameters appended to click URL',
                    },
                    'configured_status': {
                        'type': 'string',
                        'enum': [
                            'ACTIVE',
                            'ARCHIVED',
                            'DELETED',
                            'PAUSED',
                        ],
                        'description': 'User-configured status',
                    },
                    'effective_status': {
                        'type': 'string',
                        'enum': [
                            'ACTIVE',
                            'AD_GROUP_PAUSED',
                            'ARCHIVED',
                            'CAMPAIGN_PAUSED',
                            'COMPLETED',
                            'DELETED',
                            'MISSING_PERMISSIONS',
                            'PAUSED',
                            'PENDING_APPROVAL',
                            'PENDING_BILLING_INFO',
                            'PENDING_ID_VERIFICATION',
                            'PROCESSING',
                            'REJECTED',
                        ],
                        'description': 'Effective delivery status',
                    },
                    'delivery_status': {
                        'type': ['null', 'array'],
                        'items': {'type': 'string'},
                        'description': 'Delivery status details',
                    },
                    'event_trackers': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'type': {
                                    'type': 'string',
                                    'enum': ['CLICK', 'VIEW'],
                                },
                                'url': {'type': 'string'},
                            },
                        },
                        'description': 'Click and impression tracking URLs',
                    },
                    'post_id': {
                        'type': ['null', 'string'],
                        'description': 'Reddit post ID (t3_ prefix)',
                    },
                    'post_url': {
                        'type': ['null', 'string'],
                        'description': 'Reddit post URL',
                    },
                    'preview_url': {
                        'type': ['null', 'string'],
                        'description': 'Ad preview URL',
                    },
                    'preview_expiry': {
                        'type': ['null', 'string'],
                        'description': 'Preview URL expiration timestamp',
                    },
                    'rejection_reason': {
                        'type': ['null', 'string'],
                        'description': 'Reason the ad was rejected',
                    },
                    'profile_id': {
                        'type': ['null', 'string'],
                        'description': 'Reddit profile ID used for the ad',
                    },
                    'products': {
                        'type': ['null', 'array'],
                        'description': 'Product items for catalog ads',
                    },
                    'shopping_creative': {
                        'type': ['null', 'object'],
                        'description': 'Shopping creative configuration',
                    },
                    'skadnetwork_metadata': {
                        'type': ['null', 'object'],
                        'description': 'SKAdNetwork metadata for iOS app install attribution',
                    },
                    'extensions': {
                        'type': ['null', 'object'],
                        'description': 'Ad extensions',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Ad creation timestamp',
                    },
                    'modified_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                },
                'x-airbyte-entity-name': 'ads',
                'x-airbyte-stream-name': 'ad',
                'x-airbyte-ai-hints': {
                    'summary': 'Reddit ads with creative configuration, click URLs, event trackers, and approval status',
                    'when_to_use': 'Questions about individual ads, creatives, ad approval status, or click destinations',
                    'trigger_phrases': [
                        'ad',
                        'creative',
                        'ad status',
                        'ad approval',
                        'promoted post',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show me all active ads', 'Which ads were rejected and why?', 'What ads are in my campaign?'],
                    'search_strategy': 'Search by ad name, filter by status, campaign, or ad group',
                },
            },
            ai_hints={
                'summary': 'Reddit ads with creative configuration, click URLs, event trackers, and approval status',
                'when_to_use': 'Questions about individual ads, creatives, ad approval status, or click destinations',
                'trigger_phrases': [
                    'ad',
                    'creative',
                    'ad status',
                    'ad approval',
                    'promoted post',
                ],
                'freshness': 'live',
                'example_questions': ['Show me all active ads', 'Which ads were rejected and why?', 'What ads are in my campaign?'],
                'search_strategy': 'Search by ad name, filter by status, campaign, or ad group',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='ads',
                    target_entity='ad_accounts',
                    foreign_key='ad_account_id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='ads',
                    target_entity='ad_groups',
                    foreign_key='ad_group_id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='ads',
                    target_entity='campaigns',
                    foreign_key='campaign_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='campaigns',
                suggested=True,
                x_airbyte_name='campaign',
                fields=[
                    CacheFieldConfig(
                        name='ad_account_id',
                        type=['null', 'string'],
                        description='The ad account this campaign belongs to',
                    ),
                    CacheFieldConfig(
                        name='app_id',
                        type=['null', 'string'],
                        description='App Store or Play Store ID',
                    ),
                    CacheFieldConfig(
                        name='configured_status',
                        type=['null', 'string'],
                        description='User-configured status (ACTIVE, ARCHIVED, DELETED, PAUSED)',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Creation timestamp in ISO 8601 format',
                    ),
                    CacheFieldConfig(
                        name='effective_status',
                        type=['null', 'string'],
                        description='Effective delivery status',
                    ),
                    CacheFieldConfig(
                        name='funding_instrument_id',
                        type=['null', 'string'],
                        description='Funding instrument ID',
                    ),
                    CacheFieldConfig(
                        name='goal_type',
                        type=['null', 'string'],
                        description='Goal type (LIFETIME_SPEND, DAILY_SPEND)',
                    ),
                    CacheFieldConfig(
                        name='goal_value',
                        type=['null', 'integer'],
                        description='Goal value in microcurrency',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique campaign identifier',
                    ),
                    CacheFieldConfig(
                        name='is_campaign_budget_optimization',
                        type=['null', 'boolean'],
                        description='Whether campaign budget optimization is enabled',
                    ),
                    CacheFieldConfig(
                        name='modified_at',
                        type=['null', 'string'],
                        description='Last modification timestamp',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Campaign name',
                    ),
                    CacheFieldConfig(
                        name='objective',
                        type=['null', 'string'],
                        description='Campaign objective',
                    ),
                    CacheFieldConfig(
                        name='spend_cap',
                        type=['null', 'integer'],
                        description='Spend cap in microcurrency',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='ads',
                suggested=True,
                x_airbyte_name='ad',
                fields=[
                    CacheFieldConfig(
                        name='ad_account_id',
                        type=['null', 'string'],
                        description='The ad account this ad belongs to',
                    ),
                    CacheFieldConfig(
                        name='ad_group_id',
                        type=['null', 'string'],
                        description='The ad group this ad belongs to',
                    ),
                    CacheFieldConfig(
                        name='campaign_id',
                        type=['null', 'string'],
                        description='The campaign this ad belongs to',
                    ),
                    CacheFieldConfig(
                        name='click_url',
                        type=['null', 'string'],
                        description='Click destination URL',
                    ),
                    CacheFieldConfig(
                        name='configured_status',
                        type=['null', 'string'],
                        description='User-configured status',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Creation timestamp',
                    ),
                    CacheFieldConfig(
                        name='effective_status',
                        type=['null', 'string'],
                        description='Effective delivery status',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique ad identifier',
                    ),
                    CacheFieldConfig(
                        name='modified_at',
                        type=['null', 'string'],
                        description='Last modification timestamp',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Ad name',
                    ),
                    CacheFieldConfig(
                        name='post_id',
                        type=['null', 'string'],
                        description='Reddit post ID (t3_ prefix)',
                    ),
                    CacheFieldConfig(
                        name='post_url',
                        type=['null', 'string'],
                        description='Reddit post URL',
                    ),
                    CacheFieldConfig(
                        name='preview_url',
                        type=['null', 'string'],
                        description='Ad preview URL',
                    ),
                    CacheFieldConfig(
                        name='rejection_reason',
                        type=['null', 'string'],
                        description='Reason the ad was rejected',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'campaigns': [
            'ad_account_id',
            'app_id',
            'configured_status',
            'created_at',
            'effective_status',
            'funding_instrument_id',
            'goal_type',
            'goal_value',
            'id',
            'is_campaign_budget_optimization',
            'modified_at',
            'name',
            'objective',
            'spend_cap',
        ],
        'ads': [
            'ad_account_id',
            'ad_group_id',
            'campaign_id',
            'click_url',
            'configured_status',
            'created_at',
            'effective_status',
            'id',
            'modified_at',
            'name',
            'post_id',
            'post_url',
            'preview_url',
            'rejection_reason',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all campaigns in my ad account',
            'Show me my ad groups',
            'Get details for a specific ad',
            'List all ad accounts in my business',
        ],
        context_store_search=[
            'Which campaigns are paused and what are their objectives?',
            'List ads in campaign X grouped by effective status',
            'Which campaigns have a lifetime spend cap above $1000?',
            'Find paused ad groups',
        ],
        search=[
            'Which campaigns are paused and what are their objectives?',
            'List ads in campaign X grouped by effective status',
            'Which campaigns have a lifetime spend cap above $1000?',
            'Find paused ad groups',
        ],
        unsupported=[
            'Create a new campaign',
            'Update ad group targeting',
            'Delete an ad',
            'Upload creative assets',
        ],
    ),
)