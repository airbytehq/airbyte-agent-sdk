"""
Freshdesk connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import FreshdeskConnector
from .models import (
    FreshdeskAuthConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    TicketsSearchData,
    TicketsSearchResult,
    AgentsSearchData,
    AgentsSearchResult,
    GroupsSearchData,
    GroupsSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    CompaniesSearchData,
    CompaniesSearchResult,
    RolesSearchData,
    RolesSearchResult,
    SatisfactionRatingsSearchData,
    SatisfactionRatingsSearchResult,
    SurveysSearchData,
    SurveysSearchResult,
    TimeEntriesSearchData,
    TimeEntriesSearchResult,
    TicketFieldsSearchData,
    TicketFieldsSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "FreshdeskConnector",
    "AirbyteAuthConfig",
    "FreshdeskAuthConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "TicketsSearchData",
    "TicketsSearchResult",
    "AgentsSearchData",
    "AgentsSearchResult",
    "GroupsSearchData",
    "GroupsSearchResult",
    "ContactsSearchData",
    "ContactsSearchResult",
    "CompaniesSearchData",
    "CompaniesSearchResult",
    "RolesSearchData",
    "RolesSearchResult",
    "SatisfactionRatingsSearchData",
    "SatisfactionRatingsSearchResult",
    "SurveysSearchData",
    "SurveysSearchResult",
    "TimeEntriesSearchData",
    "TimeEntriesSearchResult",
    "TicketFieldsSearchData",
    "TicketFieldsSearchResult",
]