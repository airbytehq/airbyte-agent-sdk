"""
Pydantic models for outreach connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""
# ruff: noqa: E501

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class OutreachAuthConfig(BaseModel):
    """OAuth2 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """The Client ID of your Outreach developer application"""
    client_secret: str
    """The Client Secret of your Outreach developer application"""
    refresh_token: str
    """The token for obtaining the new access token"""

# Replication configuration

class OutreachReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Outreach."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """The date from which you'd like to replicate data for Outreach API, in the format YYYY-MM-DDT00:00:00Z."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class JsonApiResource(BaseModel):
    """JsonApiResource type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: int | None = Field(default=None)
    attributes: dict[str, Any] | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: dict[str, Any] | None = Field(default=None)

class PaginationLinks(BaseModel):
    """PaginationLinks type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)
    prev: str | None = Field(default=None)
    first: str | None = Field(default=None)

class ProspectAttributes(BaseModel):
    """Nested schema for Prospect.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: str | None | None = Field(default=None, alias="firstName")
    last_name: str | None | None = Field(default=None, alias="lastName")
    emails: list[str | None] | None | None = Field(default=None)
    title: str | None | None = Field(default=None)
    company: str | None | None = Field(default=None)
    tags: list[str | None] | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    account_name: str | None | None = Field(default=None, alias="accountName", description="Account name")
    """Account name"""
    added_at: str | None | None = Field(default=None, alias="addedAt", description="The date and time the prospect was added to any system.")
    """The date and time the prospect was added to any system."""
    address_city: str | None | None = Field(default=None, alias="addressCity", description="The prospect’s city (e.g. 'Seattle').")
    """The prospect’s city (e.g. 'Seattle')."""
    address_country: str | None | None = Field(default=None, alias="addressCountry", description="The prospect’s country (e.g. 'USA').")
    """The prospect’s country (e.g. 'USA')."""
    address_state: str | None | None = Field(default=None, alias="addressState", description="The prospect’s state (e.g. 'Washington').")
    """The prospect’s state (e.g. 'Washington')."""
    address_street: str | None | None = Field(default=None, alias="addressStreet", description="The prospect’s street address (e.g. '1441 N 34th St').")
    """The prospect’s street address (e.g. '1441 N 34th St')."""
    address_street2: str | None | None = Field(default=None, alias="addressStreet2", description="The prospect’s second street address, if applicable.")
    """The prospect’s second street address, if applicable."""
    address_zip: str | None | None = Field(default=None, alias="addressZip", description="The prospect’s postal code (e.g. '98103').")
    """The prospect’s postal code (e.g. '98103')."""
    angel_list_url: str | None | None = Field(default=None, alias="angelListUrl", description="The prospect’s AngelList URL.")
    """The prospect’s AngelList URL."""
    available_at: str | None | None = Field(default=None, alias="availableAt", description="The date and time the prospect is available to contact again.")
    """The date and time the prospect is available to contact again."""
    call_opted_out: bool | None | None = Field(default=None, alias="callOptedOut", description="Whether the prospect is opted out of calling, or opted out in general if granular opt-out is not enabled.")
    """Whether the prospect is opted out of calling, or opted out in general if granular opt-out is not enabled."""
    calls_opt_status: str | None | None = Field(default=None, alias="callsOptStatus", description="A string ('opted_in', 'opted_out', 'null') that represents whether a prospect has opted into or out of calls.")
    """A string ('opted_in', 'opted_out', 'null') that represents whether a prospect has opted into or out of calls."""
    calls_opted_at: str | None | None = Field(default=None, alias="callsOptedAt", description="The date and time the prospect opted in/out of calls.")
    """The date and time the prospect opted in/out of calls."""
    campaign_name: str | None | None = Field(default=None, alias="campaignName", description="The name of the campaign the prospect is associated with.")
    """The name of the campaign the prospect is associated with."""
    click_count: int | None | None = Field(default=None, alias="clickCount", description="The number of clicks the prospect has made since the last touch point.")
    """The number of clicks the prospect has made since the last touch point."""
    company_industry: str | None | None = Field(default=None, alias="companyIndustry", description="Company industry")
    """Company industry"""
    company_natural: str | None | None = Field(default=None, alias="companyNatural", description="Company natural")
    """Company natural"""
    company_size: int | None | None = Field(default=None, alias="companySize", description="Company size")
    """Company size"""
    company_type: str | None | None = Field(default=None, alias="companyType", description="Company type")
    """Company type"""
    contact_histogram: list[Any] | None | None = Field(default=None, alias="contactHistogram", description="The last 12 months of email contact history with the prospect, with the current month being the last element. The format for each month is '[inboundCount, outboundCount]'. Note: Retrieving this field will slow down the queries. Unless this field is required, it is best to filter it out. See Specify Sparse Fieldsets for examples")
    """The last 12 months of email contact history with the prospect, with the current month being the last element. The format for each month is '[inboundCount, outboundCount]'. Note: Retrieving this field will slow down the queries. Unless this field is required, it is best to filter it out. See Specify Sparse Fieldsets for examples"""
    custom1: str | None | None = Field(default=None, description="The value of the prospect’s first custom field.")
    """The value of the prospect’s first custom field."""
    custom10: str | None | None = Field(default=None, description="The value of the prospect’s 10th custom field.")
    """The value of the prospect’s 10th custom field."""
    custom100: str | None | None = Field(default=None, description="The value of the prospect’s 100th custom field.")
    """The value of the prospect’s 100th custom field."""
    custom101: str | None | None = Field(default=None, description="The value of the prospect’s 101st custom field.")
    """The value of the prospect’s 101st custom field."""
    custom102: str | None | None = Field(default=None, description="The value of the prospect’s 102nd custom field.")
    """The value of the prospect’s 102nd custom field."""
    custom103: str | None | None = Field(default=None, description="The value of the prospect’s 103rd custom field.")
    """The value of the prospect’s 103rd custom field."""
    custom104: str | None | None = Field(default=None, description="The value of the prospect’s 104th custom field.")
    """The value of the prospect’s 104th custom field."""
    custom105: str | None | None = Field(default=None, description="The value of the prospect’s 105th custom field.")
    """The value of the prospect’s 105th custom field."""
    custom106: str | None | None = Field(default=None, description="The value of the prospect’s 106th custom field.")
    """The value of the prospect’s 106th custom field."""
    custom107: str | None | None = Field(default=None, description="The value of the prospect’s 107th custom field.")
    """The value of the prospect’s 107th custom field."""
    custom108: str | None | None = Field(default=None, description="The value of the prospect’s 108th custom field.")
    """The value of the prospect’s 108th custom field."""
    custom109: str | None | None = Field(default=None, description="The value of the prospect’s 109th custom field.")
    """The value of the prospect’s 109th custom field."""
    custom11: str | None | None = Field(default=None, description="The value of the prospect’s 11th custom field.")
    """The value of the prospect’s 11th custom field."""
    custom110: str | None | None = Field(default=None, description="The value of the prospect’s 110th custom field.")
    """The value of the prospect’s 110th custom field."""
    custom111: str | None | None = Field(default=None, description="The value of the prospect’s 111th custom field.")
    """The value of the prospect’s 111th custom field."""
    custom112: str | None | None = Field(default=None, description="The value of the prospect’s 112th custom field.")
    """The value of the prospect’s 112th custom field."""
    custom113: str | None | None = Field(default=None, description="The value of the prospect’s 113th custom field.")
    """The value of the prospect’s 113th custom field."""
    custom114: str | None | None = Field(default=None, description="The value of the prospect’s 114th custom field.")
    """The value of the prospect’s 114th custom field."""
    custom115: str | None | None = Field(default=None, description="The value of the prospect’s 115th custom field.")
    """The value of the prospect’s 115th custom field."""
    custom116: str | None | None = Field(default=None, description="The value of the prospect’s 116th custom field.")
    """The value of the prospect’s 116th custom field."""
    custom117: str | None | None = Field(default=None, description="The value of the prospect’s 117th custom field.")
    """The value of the prospect’s 117th custom field."""
    custom118: str | None | None = Field(default=None, description="The value of the prospect’s 118th custom field.")
    """The value of the prospect’s 118th custom field."""
    custom119: str | None | None = Field(default=None, description="The value of the prospect’s 119th custom field.")
    """The value of the prospect’s 119th custom field."""
    custom12: str | None | None = Field(default=None, description="The value of the prospect’s 12th custom field.")
    """The value of the prospect’s 12th custom field."""
    custom120: str | None | None = Field(default=None, description="The value of the prospect’s 120th custom field.")
    """The value of the prospect’s 120th custom field."""
    custom121: str | None | None = Field(default=None, description="The value of the prospect’s 121st custom field.")
    """The value of the prospect’s 121st custom field."""
    custom122: str | None | None = Field(default=None, description="The value of the prospect’s 122nd custom field.")
    """The value of the prospect’s 122nd custom field."""
    custom123: str | None | None = Field(default=None, description="The value of the prospect’s 123rd custom field.")
    """The value of the prospect’s 123rd custom field."""
    custom124: str | None | None = Field(default=None, description="The value of the prospect’s 124th custom field.")
    """The value of the prospect’s 124th custom field."""
    custom125: str | None | None = Field(default=None, description="The value of the prospect’s 125th custom field.")
    """The value of the prospect’s 125th custom field."""
    custom126: str | None | None = Field(default=None, description="The value of the prospect’s 126th custom field.")
    """The value of the prospect’s 126th custom field."""
    custom127: str | None | None = Field(default=None, description="The value of the prospect’s 127th custom field.")
    """The value of the prospect’s 127th custom field."""
    custom128: str | None | None = Field(default=None, description="The value of the prospect’s 128th custom field.")
    """The value of the prospect’s 128th custom field."""
    custom129: str | None | None = Field(default=None, description="The value of the prospect’s 129th custom field.")
    """The value of the prospect’s 129th custom field."""
    custom13: str | None | None = Field(default=None, description="The value of the prospect’s 13th custom field.")
    """The value of the prospect’s 13th custom field."""
    custom130: str | None | None = Field(default=None, description="The value of the prospect’s 130th custom field.")
    """The value of the prospect’s 130th custom field."""
    custom131: str | None | None = Field(default=None, description="The value of the prospect’s 131st custom field.")
    """The value of the prospect’s 131st custom field."""
    custom132: str | None | None = Field(default=None, description="The value of the prospect’s 132nd custom field.")
    """The value of the prospect’s 132nd custom field."""
    custom133: str | None | None = Field(default=None, description="The value of the prospect’s 133rd custom field.")
    """The value of the prospect’s 133rd custom field."""
    custom134: str | None | None = Field(default=None, description="The value of the prospect’s 134th custom field.")
    """The value of the prospect’s 134th custom field."""
    custom135: str | None | None = Field(default=None, description="The value of the prospect’s 135th custom field.")
    """The value of the prospect’s 135th custom field."""
    custom136: str | None | None = Field(default=None, description="The value of the prospect’s 136th custom field.")
    """The value of the prospect’s 136th custom field."""
    custom137: str | None | None = Field(default=None, description="The value of the prospect’s 137th custom field.")
    """The value of the prospect’s 137th custom field."""
    custom138: str | None | None = Field(default=None, description="The value of the prospect’s 138th custom field.")
    """The value of the prospect’s 138th custom field."""
    custom139: str | None | None = Field(default=None, description="The value of the prospect’s 139th custom field.")
    """The value of the prospect’s 139th custom field."""
    custom14: str | None | None = Field(default=None, description="The value of the prospect’s 14th custom field.")
    """The value of the prospect’s 14th custom field."""
    custom140: str | None | None = Field(default=None, description="The value of the prospect’s 140th custom field.")
    """The value of the prospect’s 140th custom field."""
    custom141: str | None | None = Field(default=None, description="The value of the prospect’s 141st custom field.")
    """The value of the prospect’s 141st custom field."""
    custom142: str | None | None = Field(default=None, description="The value of the prospect’s 142nd custom field.")
    """The value of the prospect’s 142nd custom field."""
    custom143: str | None | None = Field(default=None, description="The value of the prospect’s 143rd custom field.")
    """The value of the prospect’s 143rd custom field."""
    custom144: str | None | None = Field(default=None, description="The value of the prospect’s 144th custom field.")
    """The value of the prospect’s 144th custom field."""
    custom145: str | None | None = Field(default=None, description="The value of the prospect’s 145th custom field.")
    """The value of the prospect’s 145th custom field."""
    custom146: str | None | None = Field(default=None, description="The value of the prospect’s 146th custom field.")
    """The value of the prospect’s 146th custom field."""
    custom147: str | None | None = Field(default=None, description="The value of the prospect’s 147th custom field.")
    """The value of the prospect’s 147th custom field."""
    custom148: str | None | None = Field(default=None, description="The value of the prospect’s 148th custom field.")
    """The value of the prospect’s 148th custom field."""
    custom149: str | None | None = Field(default=None, description="The value of the prospect’s 149th custom field.")
    """The value of the prospect’s 149th custom field."""
    custom15: str | None | None = Field(default=None, description="The value of the prospect’s 15th custom field.")
    """The value of the prospect’s 15th custom field."""
    custom150: str | None | None = Field(default=None, description="The value of the prospect’s 150th custom field.")
    """The value of the prospect’s 150th custom field."""
    custom16: str | None | None = Field(default=None, description="The value of the prospect’s 16th custom field.")
    """The value of the prospect’s 16th custom field."""
    custom17: str | None | None = Field(default=None, description="The value of the prospect’s 17th custom field.")
    """The value of the prospect’s 17th custom field."""
    custom18: str | None | None = Field(default=None, description="The value of the prospect’s 18th custom field.")
    """The value of the prospect’s 18th custom field."""
    custom19: str | None | None = Field(default=None, description="The value of the prospect’s 19th custom field.")
    """The value of the prospect’s 19th custom field."""
    custom2: str | None | None = Field(default=None, description="The value of the prospect’s second custom field.")
    """The value of the prospect’s second custom field."""
    custom20: str | None | None = Field(default=None, description="The value of the prospect’s 20th custom field.")
    """The value of the prospect’s 20th custom field."""
    custom21: str | None | None = Field(default=None, description="The value of the prospect’s 21st custom field.")
    """The value of the prospect’s 21st custom field."""
    custom22: str | None | None = Field(default=None, description="The value of the prospect’s 22nd custom field.")
    """The value of the prospect’s 22nd custom field."""
    custom23: str | None | None = Field(default=None, description="The value of the prospect’s 23rd custom field.")
    """The value of the prospect’s 23rd custom field."""
    custom24: str | None | None = Field(default=None, description="The value of the prospect’s 24th custom field.")
    """The value of the prospect’s 24th custom field."""
    custom25: str | None | None = Field(default=None, description="The value of the prospect’s 25th custom field.")
    """The value of the prospect’s 25th custom field."""
    custom26: str | None | None = Field(default=None, description="The value of the prospect’s 26th custom field.")
    """The value of the prospect’s 26th custom field."""
    custom27: str | None | None = Field(default=None, description="The value of the prospect’s 27th custom field.")
    """The value of the prospect’s 27th custom field."""
    custom28: str | None | None = Field(default=None, description="The value of the prospect’s 28th custom field.")
    """The value of the prospect’s 28th custom field."""
    custom29: str | None | None = Field(default=None, description="The value of the prospect’s 29th custom field.")
    """The value of the prospect’s 29th custom field."""
    custom3: str | None | None = Field(default=None, description="The value of the prospect’s third custom field.")
    """The value of the prospect’s third custom field."""
    custom30: str | None | None = Field(default=None, description="The value of the prospect’s 30th custom field.")
    """The value of the prospect’s 30th custom field."""
    custom31: str | None | None = Field(default=None, description="The value of the prospect’s 31st custom field.")
    """The value of the prospect’s 31st custom field."""
    custom32: str | None | None = Field(default=None, description="The value of the prospect’s 32nd custom field.")
    """The value of the prospect’s 32nd custom field."""
    custom33: str | None | None = Field(default=None, description="The value of the prospect’s 33rd custom field.")
    """The value of the prospect’s 33rd custom field."""
    custom34: str | None | None = Field(default=None, description="The value of the prospect’s 34th custom field.")
    """The value of the prospect’s 34th custom field."""
    custom35: str | None | None = Field(default=None, description="The value of the prospect’s 35th custom field.")
    """The value of the prospect’s 35th custom field."""
    custom36: str | None | None = Field(default=None, description="The value of the prospect’s 36th custom field.")
    """The value of the prospect’s 36th custom field."""
    custom37: str | None | None = Field(default=None, description="The value of the prospect’s 37th custom field.")
    """The value of the prospect’s 37th custom field."""
    custom38: str | None | None = Field(default=None, description="The value of the prospect’s 38th custom field.")
    """The value of the prospect’s 38th custom field."""
    custom39: str | None | None = Field(default=None, description="The value of the prospect’s 39th custom field.")
    """The value of the prospect’s 39th custom field."""
    custom4: str | None | None = Field(default=None, description="The value of the prospect’s fourth custom field.")
    """The value of the prospect’s fourth custom field."""
    custom40: str | None | None = Field(default=None, description="The value of the prospect’s 40th custom field.")
    """The value of the prospect’s 40th custom field."""
    custom41: str | None | None = Field(default=None, description="The value of the prospect’s 41st custom field.")
    """The value of the prospect’s 41st custom field."""
    custom42: str | None | None = Field(default=None, description="The value of the prospect’s 42nd custom field.")
    """The value of the prospect’s 42nd custom field."""
    custom43: str | None | None = Field(default=None, description="The value of the prospect’s 43rd custom field.")
    """The value of the prospect’s 43rd custom field."""
    custom44: str | None | None = Field(default=None, description="The value of the prospect’s 44th custom field.")
    """The value of the prospect’s 44th custom field."""
    custom45: str | None | None = Field(default=None, description="The value of the prospect’s 45th custom field.")
    """The value of the prospect’s 45th custom field."""
    custom46: str | None | None = Field(default=None, description="The value of the prospect’s 46th custom field.")
    """The value of the prospect’s 46th custom field."""
    custom47: str | None | None = Field(default=None, description="The value of the prospect’s 47th custom field.")
    """The value of the prospect’s 47th custom field."""
    custom48: str | None | None = Field(default=None, description="The value of the prospect’s 48th custom field.")
    """The value of the prospect’s 48th custom field."""
    custom49: str | None | None = Field(default=None, description="The value of the prospect’s 49th custom field.")
    """The value of the prospect’s 49th custom field."""
    custom5: str | None | None = Field(default=None, description="The value of the prospect’s fifth custom field.")
    """The value of the prospect’s fifth custom field."""
    custom50: str | None | None = Field(default=None, description="The value of the prospect’s 50th custom field.")
    """The value of the prospect’s 50th custom field."""
    custom51: str | None | None = Field(default=None, description="The value of the prospect’s 51st custom field.")
    """The value of the prospect’s 51st custom field."""
    custom52: str | None | None = Field(default=None, description="The value of the prospect’s 52nd custom field.")
    """The value of the prospect’s 52nd custom field."""
    custom53: str | None | None = Field(default=None, description="The value of the prospect’s 53rd custom field.")
    """The value of the prospect’s 53rd custom field."""
    custom54: str | None | None = Field(default=None, description="The value of the prospect’s 54th custom field.")
    """The value of the prospect’s 54th custom field."""
    custom55: str | None | None = Field(default=None, description="The value of the prospect’s 55th custom field.")
    """The value of the prospect’s 55th custom field."""
    custom56: str | None | None = Field(default=None, description="The value of the prospect’s 56th custom field.")
    """The value of the prospect’s 56th custom field."""
    custom57: str | None | None = Field(default=None, description="The value of the prospect’s 57th custom field.")
    """The value of the prospect’s 57th custom field."""
    custom58: str | None | None = Field(default=None, description="The value of the prospect’s 58th custom field.")
    """The value of the prospect’s 58th custom field."""
    custom59: str | None | None = Field(default=None, description="The value of the prospect’s 59th custom field.")
    """The value of the prospect’s 59th custom field."""
    custom6: str | None | None = Field(default=None, description="The value of the prospect’s sixth custom field.")
    """The value of the prospect’s sixth custom field."""
    custom60: str | None | None = Field(default=None, description="The value of the prospect’s 60th custom field.")
    """The value of the prospect’s 60th custom field."""
    custom61: str | None | None = Field(default=None, description="The value of the prospect’s 61st custom field.")
    """The value of the prospect’s 61st custom field."""
    custom62: str | None | None = Field(default=None, description="The value of the prospect’s 62nd custom field.")
    """The value of the prospect’s 62nd custom field."""
    custom63: str | None | None = Field(default=None, description="The value of the prospect’s 63rd custom field.")
    """The value of the prospect’s 63rd custom field."""
    custom64: str | None | None = Field(default=None, description="The value of the prospect’s 64th custom field.")
    """The value of the prospect’s 64th custom field."""
    custom65: str | None | None = Field(default=None, description="The value of the prospect’s 65th custom field.")
    """The value of the prospect’s 65th custom field."""
    custom66: str | None | None = Field(default=None, description="The value of the prospect’s 66th custom field.")
    """The value of the prospect’s 66th custom field."""
    custom67: str | None | None = Field(default=None, description="The value of the prospect’s 67th custom field.")
    """The value of the prospect’s 67th custom field."""
    custom68: str | None | None = Field(default=None, description="The value of the prospect’s 68th custom field.")
    """The value of the prospect’s 68th custom field."""
    custom69: str | None | None = Field(default=None, description="The value of the prospect’s 69th custom field.")
    """The value of the prospect’s 69th custom field."""
    custom7: str | None | None = Field(default=None, description="The value of the prospect’s seventh custom field.")
    """The value of the prospect’s seventh custom field."""
    custom70: str | None | None = Field(default=None, description="The value of the prospect’s 70th custom field.")
    """The value of the prospect’s 70th custom field."""
    custom71: str | None | None = Field(default=None, description="The value of the prospect’s 71st custom field.")
    """The value of the prospect’s 71st custom field."""
    custom72: str | None | None = Field(default=None, description="The value of the prospect’s 72nd custom field.")
    """The value of the prospect’s 72nd custom field."""
    custom73: str | None | None = Field(default=None, description="The value of the prospect’s 73rd custom field.")
    """The value of the prospect’s 73rd custom field."""
    custom74: str | None | None = Field(default=None, description="The value of the prospect’s 74th custom field.")
    """The value of the prospect’s 74th custom field."""
    custom75: str | None | None = Field(default=None, description="The value of the prospect’s 75th custom field.")
    """The value of the prospect’s 75th custom field."""
    custom76: str | None | None = Field(default=None, description="The value of the prospect’s 76th custom field.")
    """The value of the prospect’s 76th custom field."""
    custom77: str | None | None = Field(default=None, description="The value of the prospect’s 77th custom field.")
    """The value of the prospect’s 77th custom field."""
    custom78: str | None | None = Field(default=None, description="The value of the prospect’s 78th custom field.")
    """The value of the prospect’s 78th custom field."""
    custom79: str | None | None = Field(default=None, description="The value of the prospect’s 79th custom field.")
    """The value of the prospect’s 79th custom field."""
    custom8: str | None | None = Field(default=None, description="The value of the prospect’s eight custom field.")
    """The value of the prospect’s eight custom field."""
    custom80: str | None | None = Field(default=None, description="The value of the prospect’s 80th custom field.")
    """The value of the prospect’s 80th custom field."""
    custom81: str | None | None = Field(default=None, description="The value of the prospect’s 81st custom field.")
    """The value of the prospect’s 81st custom field."""
    custom82: str | None | None = Field(default=None, description="The value of the prospect’s 82nd custom field.")
    """The value of the prospect’s 82nd custom field."""
    custom83: str | None | None = Field(default=None, description="The value of the prospect’s 83rd custom field.")
    """The value of the prospect’s 83rd custom field."""
    custom84: str | None | None = Field(default=None, description="The value of the prospect’s 84th custom field.")
    """The value of the prospect’s 84th custom field."""
    custom85: str | None | None = Field(default=None, description="The value of the prospect’s 85th custom field.")
    """The value of the prospect’s 85th custom field."""
    custom86: str | None | None = Field(default=None, description="The value of the prospect’s 86th custom field.")
    """The value of the prospect’s 86th custom field."""
    custom87: str | None | None = Field(default=None, description="The value of the prospect’s 87th custom field.")
    """The value of the prospect’s 87th custom field."""
    custom88: str | None | None = Field(default=None, description="The value of the prospect’s 88th custom field.")
    """The value of the prospect’s 88th custom field."""
    custom89: str | None | None = Field(default=None, description="The value of the prospect’s 89th custom field.")
    """The value of the prospect’s 89th custom field."""
    custom9: str | None | None = Field(default=None, description="The value of the prospect’s ninth custom field.")
    """The value of the prospect’s ninth custom field."""
    custom90: str | None | None = Field(default=None, description="The value of the prospect’s 90th custom field.")
    """The value of the prospect’s 90th custom field."""
    custom91: str | None | None = Field(default=None, description="The value of the prospect’s 91st custom field.")
    """The value of the prospect’s 91st custom field."""
    custom92: str | None | None = Field(default=None, description="The value of the prospect’s 92nd custom field.")
    """The value of the prospect’s 92nd custom field."""
    custom93: str | None | None = Field(default=None, description="The value of the prospect’s 93rd custom field.")
    """The value of the prospect’s 93rd custom field."""
    custom94: str | None | None = Field(default=None, description="The value of the prospect’s 94th custom field.")
    """The value of the prospect’s 94th custom field."""
    custom95: str | None | None = Field(default=None, description="The value of the prospect’s 95th custom field.")
    """The value of the prospect’s 95th custom field."""
    custom96: str | None | None = Field(default=None, description="The value of the prospect’s 96th custom field.")
    """The value of the prospect’s 96th custom field."""
    custom97: str | None | None = Field(default=None, description="The value of the prospect’s 97th custom field.")
    """The value of the prospect’s 97th custom field."""
    custom98: str | None | None = Field(default=None, description="The value of the prospect’s 98th custom field.")
    """The value of the prospect’s 98th custom field."""
    custom99: str | None | None = Field(default=None, description="The value of the prospect’s 99th custom field.")
    """The value of the prospect’s 99th custom field."""
    date_of_birth: str | None | None = Field(default=None, alias="dateOfBirth", description="The date the prospect was born.")
    """The date the prospect was born."""
    degree: str | None | None = Field(default=None, description="The degree(s) the prospect has received.")
    """The degree(s) the prospect has received."""
    email_contacts: list[Any] | None | None = Field(default=None, alias="emailContacts", description="Email contacts")
    """Email contacts"""
    email_opted_out: bool | None | None = Field(default=None, alias="emailOptedOut", description="Whether the prospect is opted out of email, or opted out in general if granular opt-out is not enabled.")
    """Whether the prospect is opted out of email, or opted out in general if granular opt-out is not enabled."""
    emails_opt_status: str | None | None = Field(default=None, alias="emailsOptStatus", description="A string ('opted_in', 'opted_out', 'null') that represents whether a prospect has opted into or out of emails.")
    """A string ('opted_in', 'opted_out', 'null') that represents whether a prospect has opted into or out of emails."""
    emails_opted_at: str | None | None = Field(default=None, alias="emailsOptedAt", description="The date and time the prospect opted in/out of emails.")
    """The date and time the prospect opted in/out of emails."""
    engaged_at: str | None | None = Field(default=None, alias="engagedAt", description="The date and time the prospect last engaged.")
    """The date and time the prospect last engaged."""
    engaged_score: float | None | None = Field(default=None, alias="engagedScore", description="A number representing the quality of the lead, based on the number of the prospect’s opens, clicks and mailing replies.")
    """A number representing the quality of the lead, based on the number of the prospect’s opens, clicks and mailing replies."""
    enrichable: bool | None | None = Field(default=None, description="Enrichable")
    """Enrichable"""
    event_name: str | None | None = Field(default=None, alias="eventName", description="The name of the event the prospect was met at.")
    """The name of the event the prospect was met at."""
    external_id: str | None | None = Field(default=None, alias="externalId", description="A custom ID for the prospect, often referencing an ID in an external system.")
    """A custom ID for the prospect, often referencing an ID in an external system."""
    external_owner: str | None | None = Field(default=None, alias="externalOwner", description="A custom owner for the prospect, often referencing an ownering in an external system.")
    """A custom owner for the prospect, often referencing an ownering in an external system."""
    external_source: str | None | None = Field(default=None, alias="externalSource", description="The source of the resource’s creation (e.g. 'outreach-api').")
    """The source of the resource’s creation (e.g. 'outreach-api')."""
    facebook_url: str | None | None = Field(default=None, alias="facebookUrl", description="The prospect’s Facebook URL.")
    """The prospect’s Facebook URL."""
    gender: str | None | None = Field(default=None, description="The gender of the prospect.")
    """The gender of the prospect."""
    github_url: str | None | None = Field(default=None, alias="githubUrl", description="The prospect’s GitHub URL.")
    """The prospect’s GitHub URL."""
    github_username: str | None | None = Field(default=None, alias="githubUsername", description="The prospect’s GitHub username.")
    """The prospect’s GitHub username."""
    google_plus_url: str | None | None = Field(default=None, alias="googlePlusUrl", description="The prospect’s Google+ URL.")
    """The prospect’s Google+ URL."""
    graduation_date: str | None | None = Field(default=None, alias="graduationDate", description="The graduation date of the prospect.")
    """The graduation date of the prospect."""
    home_phones: list[str] | None | None = Field(default=None, alias="homePhones", description="A list of home phone numbers associated with the prospect.")
    """A list of home phone numbers associated with the prospect."""
    job_start_date: str | None | None = Field(default=None, alias="jobStartDate", description="The starting date of the prospect’s current job.")
    """The starting date of the prospect’s current job."""
    linked_in_connections: int | None | None = Field(default=None, alias="linkedInConnections", description="The number of connections on the prospect’s LinkedIn profile.")
    """The number of connections on the prospect’s LinkedIn profile."""
    linked_in_id: str | None | None = Field(default=None, alias="linkedInId", description="The prospect’s LinkedIn ID.")
    """The prospect’s LinkedIn ID."""
    linked_in_slug: str | None | None = Field(default=None, alias="linkedInSlug", description="The prospect’s LinkedIn slug.")
    """The prospect’s LinkedIn slug."""
    linked_in_url: str | None | None = Field(default=None, alias="linkedInUrl", description="The prospect’s LinkedIn URL.")
    """The prospect’s LinkedIn URL."""
    middle_name: str | None | None = Field(default=None, alias="middleName", description="The middle name of the prospect.")
    """The middle name of the prospect."""
    mobile_phones: list[str] | None | None = Field(default=None, alias="mobilePhones", description="A list of mobile phone numbers associated with the prospect.")
    """A list of mobile phone numbers associated with the prospect."""
    name: str | None | None = Field(default=None, description="The full name of the prospect.")
    """The full name of the prospect."""
    nickname: str | None | None = Field(default=None, description="The nickname of the prospect.")
    """The nickname of the prospect."""
    occupation: str | None | None = Field(default=None, description="The occupation of the prospect (e.g. 'Purchasing Manager').")
    """The occupation of the prospect (e.g. 'Purchasing Manager')."""
    open_count: int | None | None = Field(default=None, alias="openCount", description="The number of opens the prospect has made since the last touch point.")
    """The number of opens the prospect has made since the last touch point."""
    opted_out: bool | None | None = Field(default=None, alias="optedOut", description="A boolean value representing whether this prospect is currently opted out of all mailings. Set this value to true to opt out the prospect; the 'opted_out' timestamp will be updated to the time of the request. Set this value to false to revert the opt at and clear the opted out timestamp.")
    """A boolean value representing whether this prospect is currently opted out of all mailings. Set this value to true to opt out the prospect; the 'opted_out' timestamp will be updated to the time of the request. Set this value to false to revert the opt at and clear the opted out timestamp."""
    opted_out_at: str | None | None = Field(default=None, alias="optedOutAt", description="The date and time the prospect opted out of emails.")
    """The date and time the prospect opted out of emails."""
    other_phones: list[str] | None | None = Field(default=None, alias="otherPhones", description="A list of other phone numbers associated with the prospect.")
    """A list of other phone numbers associated with the prospect."""
    personal_note1: str | None | None = Field(default=None, alias="personalNote1", description="A custom note field related to the prospect.")
    """A custom note field related to the prospect."""
    personal_note2: str | None | None = Field(default=None, alias="personalNote2", description="A second note field related to the prospect.")
    """A second note field related to the prospect."""
    preferred_contact: str | None | None = Field(default=None, alias="preferredContact", description="The preferred contact method for the prospect.")
    """The preferred contact method for the prospect."""
    quora_url: str | None | None = Field(default=None, alias="quoraUrl", description="The prospect’s Quora URL.")
    """The prospect’s Quora URL."""
    real_creator_id: int | None | None = Field(default=None, alias="realCreatorId", description="Real creator ID")
    """Real creator ID"""
    real_creator_type: str | None | None = Field(default=None, alias="realCreatorType", description="Real creator type")
    """Real creator type"""
    region: str | None | None = Field(default=None, description="The primary geographic region of the prospect.")
    """The primary geographic region of the prospect."""
    reply_count: int | None | None = Field(default=None, alias="replyCount", description="The number of replies the prospect has made since the last touch point.")
    """The number of replies the prospect has made since the last touch point."""
    school: str | None | None = Field(default=None, description="The school(s) the prospect has attended.")
    """The school(s) the prospect has attended."""
    score: float | None | None = Field(default=None, description="A custom score given to measure the quality of the lead.")
    """A custom score given to measure the quality of the lead."""
    sharing_team_id: str | None | None = Field(default=None, alias="sharingTeamId", description="The ID of the sharing team associated with this object. Access is currently in beta.")
    """The ID of the sharing team associated with this object. Access is currently in beta."""
    sms_opted_out: bool | None | None = Field(default=None, alias="smsOptedOut", description="Sms opted out")
    """Sms opted out"""
    source: str | None | None = Field(default=None, description="A custom source representing where the lead was first acquired.")
    """A custom source representing where the lead was first acquired."""
    specialties: str | None | None = Field(default=None, description="A description of the prospect’s specialties.")
    """A description of the prospect’s specialties."""
    stack_overflow_id: str | None | None = Field(default=None, alias="stackOverflowId", description="The prospect’s StackOverflow ID.")
    """The prospect’s StackOverflow ID."""
    stack_overflow_url: str | None | None = Field(default=None, alias="stackOverflowUrl", description="The prospect’s StackOverflow URL.")
    """The prospect’s StackOverflow URL."""
    stage_name: str | None | None = Field(default=None, alias="stageName", description="Stage name")
    """Stage name"""
    time_zone: str | None | None = Field(default=None, alias="timeZone", description="The prospect’s current timezone, preferably in the IANA format (e.g. 'America/LosAngeles').")
    """The prospect’s current timezone, preferably in the IANA format (e.g. 'America/LosAngeles')."""
    time_zone_iana: str | None | None = Field(default=None, alias="timeZoneIana", description="The prospect’s current IANA timezone, if available.")
    """The prospect’s current IANA timezone, if available."""
    time_zone_inferred: str | None | None = Field(default=None, alias="timeZoneInferred", description="The prospect’s current inferred IANA timezone, if available.")
    """The prospect’s current inferred IANA timezone, if available."""
    touched_at: str | None | None = Field(default=None, alias="touchedAt", description="The date and time the prospect was last touched.")
    """The date and time the prospect was last touched."""
    trashed_at: str | None | None = Field(default=None, alias="trashedAt", description="The date a prospect was soft deleted.")
    """The date a prospect was soft deleted."""
    twitter_url: str | None | None = Field(default=None, alias="twitterUrl", description="The prospect’s Twitter URL.")
    """The prospect’s Twitter URL."""
    twitter_username: str | None | None = Field(default=None, alias="twitterUsername", description="The prospect’s Twitter username.")
    """The prospect’s Twitter username."""
    updater_id: int | None | None = Field(default=None, alias="updaterId", description="Updater ID")
    """Updater ID"""
    updater_type: str | None | None = Field(default=None, alias="updaterType", description="Updater type")
    """Updater type"""
    voip_phones: list[str] | None | None = Field(default=None, alias="voipPhones", description="A list of voip phone numbers associated with the prospect.")
    """A list of voip phone numbers associated with the prospect."""
    website_url1: str | None | None = Field(default=None, alias="websiteUrl1", description="The URL of the prospect’s website.")
    """The URL of the prospect’s website."""
    website_url2: str | None | None = Field(default=None, alias="websiteUrl2", description="The value of the prospect’s second website URL field.")
    """The value of the prospect’s second website URL field."""
    website_url3: str | None | None = Field(default=None, alias="websiteUrl3", description="The value of the prospect’s third website URL field.")
    """The value of the prospect’s third website URL field."""
    work_phones: list[str] | None | None = Field(default=None, alias="workPhones", description="A list of work phone numbers associated with the prospect.")
    """A list of work phone numbers associated with the prospect."""

class ProspectLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class Prospect(BaseModel):
    """Outreach prospect (contact) object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: ProspectAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: ProspectLinks | None = Field(default=None)

class ProspectsList(BaseModel):
    """ProspectsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Prospect] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class ProspectResponse(BaseModel):
    """ProspectResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Prospect | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class AccountLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class AccountAttributes(BaseModel):
    """Nested schema for Account.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    domain: str | None | None = Field(default=None)
    industry: str | None | None = Field(default=None)
    number_of_employees: int | None | None = Field(default=None, alias="numberOfEmployees")
    company_type: str | None | None = Field(default=None, alias="companyType")
    locality: str | None | None = Field(default=None)
    website_url: str | None | None = Field(default=None, alias="websiteUrl")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    annual_revenue_range: str | None | None = Field(default=None, alias="annualRevenueRange", description="Define the annual revenue range")
    """Define the annual revenue range"""
    buyer_intent_score: float | None | None = Field(default=None, alias="buyerIntentScore", description="A custom score given to measure the quality of the account.")
    """A custom score given to measure the quality of the account."""
    custom1: str | None | None = Field(default=None, description="The value of the account’s first custom field.")
    """The value of the account’s first custom field."""
    custom10: str | None | None = Field(default=None, description="The value of the account’s 10th custom field.")
    """The value of the account’s 10th custom field."""
    custom100: str | None | None = Field(default=None, description="The value of the account’s 100th custom field.")
    """The value of the account’s 100th custom field."""
    custom101: str | None | None = Field(default=None, description="The value of the account’s 101st custom field.")
    """The value of the account’s 101st custom field."""
    custom102: str | None | None = Field(default=None, description="The value of the account’s 102nd custom field.")
    """The value of the account’s 102nd custom field."""
    custom103: str | None | None = Field(default=None, description="The value of the account’s 103rd custom field.")
    """The value of the account’s 103rd custom field."""
    custom104: str | None | None = Field(default=None, description="The value of the account’s 104th custom field.")
    """The value of the account’s 104th custom field."""
    custom105: str | None | None = Field(default=None, description="The value of the account’s 105th custom field.")
    """The value of the account’s 105th custom field."""
    custom106: str | None | None = Field(default=None, description="The value of the account’s 106th custom field.")
    """The value of the account’s 106th custom field."""
    custom107: str | None | None = Field(default=None, description="The value of the account’s 107th custom field.")
    """The value of the account’s 107th custom field."""
    custom108: str | None | None = Field(default=None, description="The value of the account’s 108th custom field.")
    """The value of the account’s 108th custom field."""
    custom109: str | None | None = Field(default=None, description="The value of the account’s 109th custom field.")
    """The value of the account’s 109th custom field."""
    custom11: str | None | None = Field(default=None, description="The value of the account’s 11th custom field.")
    """The value of the account’s 11th custom field."""
    custom110: str | None | None = Field(default=None, description="The value of the account’s 110th custom field.")
    """The value of the account’s 110th custom field."""
    custom111: str | None | None = Field(default=None, description="The value of the account’s 111th custom field.")
    """The value of the account’s 111th custom field."""
    custom112: str | None | None = Field(default=None, description="The value of the account’s 112th custom field.")
    """The value of the account’s 112th custom field."""
    custom113: str | None | None = Field(default=None, description="The value of the account’s 113th custom field.")
    """The value of the account’s 113th custom field."""
    custom114: str | None | None = Field(default=None, description="The value of the account’s 114th custom field.")
    """The value of the account’s 114th custom field."""
    custom115: str | None | None = Field(default=None, description="The value of the account’s 115th custom field.")
    """The value of the account’s 115th custom field."""
    custom116: str | None | None = Field(default=None, description="The value of the account’s 116th custom field.")
    """The value of the account’s 116th custom field."""
    custom117: str | None | None = Field(default=None, description="The value of the account’s 117th custom field.")
    """The value of the account’s 117th custom field."""
    custom118: str | None | None = Field(default=None, description="The value of the account’s 118th custom field.")
    """The value of the account’s 118th custom field."""
    custom119: str | None | None = Field(default=None, description="The value of the account’s 119th custom field.")
    """The value of the account’s 119th custom field."""
    custom12: str | None | None = Field(default=None, description="The value of the account’s 12th custom field.")
    """The value of the account’s 12th custom field."""
    custom120: str | None | None = Field(default=None, description="The value of the account’s 120th custom field.")
    """The value of the account’s 120th custom field."""
    custom121: str | None | None = Field(default=None, description="The value of the account’s 121st custom field.")
    """The value of the account’s 121st custom field."""
    custom122: str | None | None = Field(default=None, description="The value of the account’s 122nd custom field.")
    """The value of the account’s 122nd custom field."""
    custom123: str | None | None = Field(default=None, description="The value of the account’s 123rd custom field.")
    """The value of the account’s 123rd custom field."""
    custom124: str | None | None = Field(default=None, description="The value of the account’s 124th custom field.")
    """The value of the account’s 124th custom field."""
    custom125: str | None | None = Field(default=None, description="The value of the account’s 125th custom field.")
    """The value of the account’s 125th custom field."""
    custom126: str | None | None = Field(default=None, description="The value of the account’s 126th custom field.")
    """The value of the account’s 126th custom field."""
    custom127: str | None | None = Field(default=None, description="The value of the account’s 127th custom field.")
    """The value of the account’s 127th custom field."""
    custom128: str | None | None = Field(default=None, description="The value of the account’s 128th custom field.")
    """The value of the account’s 128th custom field."""
    custom129: str | None | None = Field(default=None, description="The value of the account’s 129th custom field.")
    """The value of the account’s 129th custom field."""
    custom13: str | None | None = Field(default=None, description="The value of the account’s 13th custom field.")
    """The value of the account’s 13th custom field."""
    custom130: str | None | None = Field(default=None, description="The value of the account’s 130th custom field.")
    """The value of the account’s 130th custom field."""
    custom131: str | None | None = Field(default=None, description="The value of the account’s 131st custom field.")
    """The value of the account’s 131st custom field."""
    custom132: str | None | None = Field(default=None, description="The value of the account’s 132nd custom field.")
    """The value of the account’s 132nd custom field."""
    custom133: str | None | None = Field(default=None, description="The value of the account’s 133rd custom field.")
    """The value of the account’s 133rd custom field."""
    custom134: str | None | None = Field(default=None, description="The value of the account’s 134th custom field.")
    """The value of the account’s 134th custom field."""
    custom135: str | None | None = Field(default=None, description="The value of the account’s 135th custom field.")
    """The value of the account’s 135th custom field."""
    custom136: str | None | None = Field(default=None, description="The value of the account’s 136th custom field.")
    """The value of the account’s 136th custom field."""
    custom137: str | None | None = Field(default=None, description="The value of the account’s 137th custom field.")
    """The value of the account’s 137th custom field."""
    custom138: str | None | None = Field(default=None, description="The value of the account’s 138th custom field.")
    """The value of the account’s 138th custom field."""
    custom139: str | None | None = Field(default=None, description="The value of the account’s 139th custom field.")
    """The value of the account’s 139th custom field."""
    custom14: str | None | None = Field(default=None, description="The value of the account’s 14th custom field.")
    """The value of the account’s 14th custom field."""
    custom140: str | None | None = Field(default=None, description="The value of the account’s 140th custom field.")
    """The value of the account’s 140th custom field."""
    custom141: str | None | None = Field(default=None, description="The value of the account’s 141st custom field.")
    """The value of the account’s 141st custom field."""
    custom142: str | None | None = Field(default=None, description="The value of the account’s 142nd custom field.")
    """The value of the account’s 142nd custom field."""
    custom143: str | None | None = Field(default=None, description="The value of the account’s 143rd custom field.")
    """The value of the account’s 143rd custom field."""
    custom144: str | None | None = Field(default=None, description="The value of the account’s 144th custom field.")
    """The value of the account’s 144th custom field."""
    custom145: str | None | None = Field(default=None, description="The value of the account’s 145th custom field.")
    """The value of the account’s 145th custom field."""
    custom146: str | None | None = Field(default=None, description="The value of the account’s 146th custom field.")
    """The value of the account’s 146th custom field."""
    custom147: str | None | None = Field(default=None, description="The value of the account’s 147th custom field.")
    """The value of the account’s 147th custom field."""
    custom148: str | None | None = Field(default=None, description="The value of the account’s 148th custom field.")
    """The value of the account’s 148th custom field."""
    custom149: str | None | None = Field(default=None, description="The value of the account’s 149th custom field.")
    """The value of the account’s 149th custom field."""
    custom15: str | None | None = Field(default=None, description="The value of the account’s 15th custom field.")
    """The value of the account’s 15th custom field."""
    custom150: str | None | None = Field(default=None, description="The value of the account’s 150th custom field.")
    """The value of the account’s 150th custom field."""
    custom16: str | None | None = Field(default=None, description="The value of the account’s 16th custom field.")
    """The value of the account’s 16th custom field."""
    custom17: str | None | None = Field(default=None, description="The value of the account’s 17th custom field.")
    """The value of the account’s 17th custom field."""
    custom18: str | None | None = Field(default=None, description="The value of the account’s 18th custom field.")
    """The value of the account’s 18th custom field."""
    custom19: str | None | None = Field(default=None, description="The value of the account’s 19th custom field.")
    """The value of the account’s 19th custom field."""
    custom2: str | None | None = Field(default=None, description="The value of the account’s second custom field.")
    """The value of the account’s second custom field."""
    custom20: str | None | None = Field(default=None, description="The value of the account’s 20th custom field.")
    """The value of the account’s 20th custom field."""
    custom21: str | None | None = Field(default=None, description="The value of the account’s 21st custom field.")
    """The value of the account’s 21st custom field."""
    custom22: str | None | None = Field(default=None, description="The value of the account’s 22nd custom field.")
    """The value of the account’s 22nd custom field."""
    custom23: str | None | None = Field(default=None, description="The value of the account’s 23rd custom field.")
    """The value of the account’s 23rd custom field."""
    custom24: str | None | None = Field(default=None, description="The value of the account’s 24th custom field.")
    """The value of the account’s 24th custom field."""
    custom25: str | None | None = Field(default=None, description="The value of the account’s 25th custom field.")
    """The value of the account’s 25th custom field."""
    custom26: str | None | None = Field(default=None, description="The value of the account’s 26th custom field.")
    """The value of the account’s 26th custom field."""
    custom27: str | None | None = Field(default=None, description="The value of the account’s 27th custom field.")
    """The value of the account’s 27th custom field."""
    custom28: str | None | None = Field(default=None, description="The value of the account’s 28th custom field.")
    """The value of the account’s 28th custom field."""
    custom29: str | None | None = Field(default=None, description="The value of the account’s 29th custom field.")
    """The value of the account’s 29th custom field."""
    custom3: str | None | None = Field(default=None, description="The value of the account’s third custom field.")
    """The value of the account’s third custom field."""
    custom30: str | None | None = Field(default=None, description="The value of the account’s 30th custom field.")
    """The value of the account’s 30th custom field."""
    custom31: str | None | None = Field(default=None, description="The value of the account’s 31st custom field.")
    """The value of the account’s 31st custom field."""
    custom32: str | None | None = Field(default=None, description="The value of the account’s 32nd custom field.")
    """The value of the account’s 32nd custom field."""
    custom33: str | None | None = Field(default=None, description="The value of the account’s 33rd custom field.")
    """The value of the account’s 33rd custom field."""
    custom34: str | None | None = Field(default=None, description="The value of the account’s 34th custom field.")
    """The value of the account’s 34th custom field."""
    custom35: str | None | None = Field(default=None, description="The value of the account’s 35th custom field.")
    """The value of the account’s 35th custom field."""
    custom36: str | None | None = Field(default=None, description="The value of the account's 36th custom field.")
    """The value of the account's 36th custom field."""
    custom37: str | None | None = Field(default=None, description="The value of the account's 37th custom field.")
    """The value of the account's 37th custom field."""
    custom38: str | None | None = Field(default=None, description="The value of the account's 38th custom field.")
    """The value of the account's 38th custom field."""
    custom39: str | None | None = Field(default=None, description="The value of the account's 39th custom field.")
    """The value of the account's 39th custom field."""
    custom4: str | None | None = Field(default=None, description="The value of the account’s fourth custom field.")
    """The value of the account’s fourth custom field."""
    custom40: str | None | None = Field(default=None, description="The value of the account's 40th custom field.")
    """The value of the account's 40th custom field."""
    custom41: str | None | None = Field(default=None, description="The value of the account's 41st custom field.")
    """The value of the account's 41st custom field."""
    custom42: str | None | None = Field(default=None, description="The value of the account's 42nd custom field.")
    """The value of the account's 42nd custom field."""
    custom43: str | None | None = Field(default=None, description="The value of the account's 43rd custom field.")
    """The value of the account's 43rd custom field."""
    custom44: str | None | None = Field(default=None, description="The value of the account's 44th custom field.")
    """The value of the account's 44th custom field."""
    custom45: str | None | None = Field(default=None, description="The value of the account's 45th custom field.")
    """The value of the account's 45th custom field."""
    custom46: str | None | None = Field(default=None, description="The value of the account's 46th custom field.")
    """The value of the account's 46th custom field."""
    custom47: str | None | None = Field(default=None, description="The value of the account's 47th custom field.")
    """The value of the account's 47th custom field."""
    custom48: str | None | None = Field(default=None, description="The value of the account's 48th custom field.")
    """The value of the account's 48th custom field."""
    custom49: str | None | None = Field(default=None, description="The value of the account's 49th custom field.")
    """The value of the account's 49th custom field."""
    custom5: str | None | None = Field(default=None, description="The value of the account’s fifth custom field.")
    """The value of the account’s fifth custom field."""
    custom50: str | None | None = Field(default=None, description="The value of the account's 50th custom field.")
    """The value of the account's 50th custom field."""
    custom51: str | None | None = Field(default=None, description="The value of the account's 51st custom field.")
    """The value of the account's 51st custom field."""
    custom52: str | None | None = Field(default=None, description="The value of the account's 52nd custom field.")
    """The value of the account's 52nd custom field."""
    custom53: str | None | None = Field(default=None, description="The value of the account's 53rd custom field.")
    """The value of the account's 53rd custom field."""
    custom54: str | None | None = Field(default=None, description="The value of the account's 54th custom field.")
    """The value of the account's 54th custom field."""
    custom55: str | None | None = Field(default=None, description="The value of the account's 55th custom field.")
    """The value of the account's 55th custom field."""
    custom56: str | None | None = Field(default=None, description="The value of the account's 56th custom field.")
    """The value of the account's 56th custom field."""
    custom57: str | None | None = Field(default=None, description="The value of the account's 57th custom field.")
    """The value of the account's 57th custom field."""
    custom58: str | None | None = Field(default=None, description="The value of the account's 58th custom field.")
    """The value of the account's 58th custom field."""
    custom59: str | None | None = Field(default=None, description="The value of the account's 59th custom field.")
    """The value of the account's 59th custom field."""
    custom6: str | None | None = Field(default=None, description="The value of the account’s sixth custom field.")
    """The value of the account’s sixth custom field."""
    custom60: str | None | None = Field(default=None, description="The value of the account's 60th custom field.")
    """The value of the account's 60th custom field."""
    custom61: str | None | None = Field(default=None, description="The value of the account's 61st custom field.")
    """The value of the account's 61st custom field."""
    custom62: str | None | None = Field(default=None, description="The value of the account's 62nd custom field.")
    """The value of the account's 62nd custom field."""
    custom63: str | None | None = Field(default=None, description="The value of the account's 63rd custom field.")
    """The value of the account's 63rd custom field."""
    custom64: str | None | None = Field(default=None, description="The value of the account's 64th custom field.")
    """The value of the account's 64th custom field."""
    custom65: str | None | None = Field(default=None, description="The value of the account's 65th custom field.")
    """The value of the account's 65th custom field."""
    custom66: str | None | None = Field(default=None, description="The value of the account's 66th custom field.")
    """The value of the account's 66th custom field."""
    custom67: str | None | None = Field(default=None, description="The value of the account's 67th custom field.")
    """The value of the account's 67th custom field."""
    custom68: str | None | None = Field(default=None, description="The value of the account's 68th custom field.")
    """The value of the account's 68th custom field."""
    custom69: str | None | None = Field(default=None, description="The value of the account's 69th custom field.")
    """The value of the account's 69th custom field."""
    custom7: str | None | None = Field(default=None, description="The value of the account’s seventh custom field.")
    """The value of the account’s seventh custom field."""
    custom70: str | None | None = Field(default=None, description="The value of the account's 70th custom field.")
    """The value of the account's 70th custom field."""
    custom71: str | None | None = Field(default=None, description="The value of the account's 71st custom field.")
    """The value of the account's 71st custom field."""
    custom72: str | None | None = Field(default=None, description="The value of the account's 72nd custom field.")
    """The value of the account's 72nd custom field."""
    custom73: str | None | None = Field(default=None, description="The value of the account's 73rd custom field.")
    """The value of the account's 73rd custom field."""
    custom74: str | None | None = Field(default=None, description="The value of the account's 74th custom field.")
    """The value of the account's 74th custom field."""
    custom75: str | None | None = Field(default=None, description="The value of the account's 75th custom field.")
    """The value of the account's 75th custom field."""
    custom76: str | None | None = Field(default=None, description="The value of the account's 76th custom field.")
    """The value of the account's 76th custom field."""
    custom77: str | None | None = Field(default=None, description="The value of the account's 77th custom field.")
    """The value of the account's 77th custom field."""
    custom78: str | None | None = Field(default=None, description="The value of the account's 78th custom field.")
    """The value of the account's 78th custom field."""
    custom79: str | None | None = Field(default=None, description="The value of the account's 79th custom field.")
    """The value of the account's 79th custom field."""
    custom8: str | None | None = Field(default=None, description="The value of the account’s eight custom field.")
    """The value of the account’s eight custom field."""
    custom80: str | None | None = Field(default=None, description="The value of the account's 80th custom field.")
    """The value of the account's 80th custom field."""
    custom81: str | None | None = Field(default=None, description="The value of the account's 81st custom field.")
    """The value of the account's 81st custom field."""
    custom82: str | None | None = Field(default=None, description="The value of the account's 82nd custom field.")
    """The value of the account's 82nd custom field."""
    custom83: str | None | None = Field(default=None, description="The value of the account's 83rd custom field.")
    """The value of the account's 83rd custom field."""
    custom84: str | None | None = Field(default=None, description="The value of the account's 84th custom field.")
    """The value of the account's 84th custom field."""
    custom85: str | None | None = Field(default=None, description="The value of the account's 85th custom field.")
    """The value of the account's 85th custom field."""
    custom86: str | None | None = Field(default=None, description="The value of the account's 86th custom field.")
    """The value of the account's 86th custom field."""
    custom87: str | None | None = Field(default=None, description="The value of the account's 87th custom field.")
    """The value of the account's 87th custom field."""
    custom88: str | None | None = Field(default=None, description="The value of the account's 88th custom field.")
    """The value of the account's 88th custom field."""
    custom89: str | None | None = Field(default=None, description="The value of the account's 89th custom field.")
    """The value of the account's 89th custom field."""
    custom9: str | None | None = Field(default=None, description="The value of the account’s ninth custom field.")
    """The value of the account’s ninth custom field."""
    custom90: str | None | None = Field(default=None, description="The value of the account's 90th custom field.")
    """The value of the account's 90th custom field."""
    custom91: str | None | None = Field(default=None, description="The value of the account's 91st custom field.")
    """The value of the account's 91st custom field."""
    custom92: str | None | None = Field(default=None, description="The value of the account's 92nd custom field.")
    """The value of the account's 92nd custom field."""
    custom93: str | None | None = Field(default=None, description="The value of the account's 93rd custom field.")
    """The value of the account's 93rd custom field."""
    custom94: str | None | None = Field(default=None, description="The value of the account's 94th custom field.")
    """The value of the account's 94th custom field."""
    custom95: str | None | None = Field(default=None, description="The value of the account's 95th custom field.")
    """The value of the account's 95th custom field."""
    custom96: str | None | None = Field(default=None, description="The value of the account's 96th custom field.")
    """The value of the account's 96th custom field."""
    custom97: str | None | None = Field(default=None, description="The value of the account's 97th custom field.")
    """The value of the account's 97th custom field."""
    custom98: str | None | None = Field(default=None, description="The value of the account's 98th custom field.")
    """The value of the account's 98th custom field."""
    custom99: str | None | None = Field(default=None, description="The value of the account's 99th custom field.")
    """The value of the account's 99th custom field."""
    custom_id: str | None | None = Field(default=None, alias="customId", description="A custom ID for the account, often referencing an ID in an external system.")
    """A custom ID for the account, often referencing an ID in an external system."""
    description: str | None | None = Field(default=None, description="A custom description of the account.")
    """A custom description of the account."""
    enrichable: bool | None | None = Field(default=None, description="Enrichable")
    """Enrichable"""
    external_source: str | None | None = Field(default=None, alias="externalSource", description="The source of the resource’s creation (e.g. 'outreach-api').")
    """The source of the resource’s creation (e.g. 'outreach-api')."""
    followers: int | None | None = Field(default=None, description="The number of followers the company has listed on social media.")
    """The number of followers the company has listed on social media."""
    founded_at: str | None | None = Field(default=None, alias="foundedAt", description="The founding date of the company.")
    """The founding date of the company."""
    linked_in_employees: int | None | None = Field(default=None, alias="linkedInEmployees", description="The number of employees listed on the company’s LinkedIn URL.")
    """The number of employees listed on the company’s LinkedIn URL."""
    linked_in_url: str | None | None = Field(default=None, alias="linkedInUrl", description="The company’s LinkedIn URL.")
    """The company’s LinkedIn URL."""
    naics_codes: list[str] | None | None = Field(default=None, alias="naicsCodes", description="Define codes used to classify businesses by industry")
    """Define codes used to classify businesses by industry"""
    named: bool | None | None = Field(default=None, description="A boolean value determining whether this is a 'named' account or not. Only named accounts will show up on the collection index.")
    """A boolean value determining whether this is a 'named' account or not. Only named accounts will show up on the collection index."""
    natural_name: str | None | None = Field(default=None, alias="naturalName", description="The natural name of the company (e.g. 'Acme').")
    """The natural name of the company (e.g. 'Acme')."""
    sharing_team_id: str | None | None = Field(default=None, alias="sharingTeamId", description="The ID of the sharing team associated with this object. Access is currently in beta.")
    """The ID of the sharing team associated with this object. Access is currently in beta."""
    sic_codes: list[str] | None | None = Field(default=None, alias="sicCodes", description="Define codes that categorize business activities")
    """Define codes that categorize business activities"""
    tags: list[str] | None | None = Field(default=None, description="A list of tag values associated with the account (e.g. ['Enterprise', 'Tier 1']).")
    """A list of tag values associated with the account (e.g. ['Enterprise', 'Tier 1'])."""
    ticker_symbol: str | None | None = Field(default=None, alias="tickerSymbol", description="Define the ticker symbol")
    """Define the ticker symbol"""
    touched_at: str | None | None = Field(default=None, alias="touchedAt", description="The date and time the account was last touched.")
    """The date and time the account was last touched."""

class Account(BaseModel):
    """Outreach account object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: AccountAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: AccountLinks | None = Field(default=None)

class AccountsList(BaseModel):
    """AccountsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Account] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class AccountResponse(BaseModel):
    """AccountResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Account | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class SequenceAttributes(BaseModel):
    """Nested schema for Sequence.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    description: str | None | None = Field(default=None)
    sequence_type: str | None | None = Field(default=None, alias="sequenceType")
    enabled: bool | None | None = Field(default=None)
    tags: list[str | None] | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    ai_template_powered: bool | None | None = Field(default=None, alias="aiTemplatePowered", description="AI template powered")
    """AI template powered"""
    automation_percentage: float | None | None = Field(default=None, alias="automationPercentage", description="The percentage of 'auto_email' sequence steps in this sequence.")
    """The percentage of 'auto_email' sequence steps in this sequence."""
    bounce_count: int | None | None = Field(default=None, alias="bounceCount", description="The total count of bounced mailings during this sequence.")
    """The total count of bounced mailings during this sequence."""
    click_count: int | None | None = Field(default=None, alias="clickCount", description="The total count of clicked mailings from this sequence.")
    """The total count of clicked mailings from this sequence."""
    deliver_count: int | None | None = Field(default=None, alias="deliverCount", description="The total count of delivered mailings from this sequence.")
    """The total count of delivered mailings from this sequence."""
    duration_in_days: int | None | None = Field(default=None, alias="durationInDays", description="The total number of days it takes to get through this sequence.")
    """The total number of days it takes to get through this sequence."""
    enabled_at: str | None | None = Field(default=None, alias="enabledAt", description="The date and time the sequence was enabled, or null if currently disabled.")
    """The date and time the sequence was enabled, or null if currently disabled."""
    failure_count: int | None | None = Field(default=None, alias="failureCount", description="The total count of failed mailings from this sequence.")
    """The total count of failed mailings from this sequence."""
    finish_on_reply: bool | None | None = Field(default=None, alias="finishOnReply", description="Deprecated. This boolean value exists only to maintain backward compatibility and primaryReplyAction should be used instead. True if primaryReplyAction is 'finish', false otherwise.")
    """Deprecated. This boolean value exists only to maintain backward compatibility and primaryReplyAction should be used instead. True if primaryReplyAction is 'finish', false otherwise."""
    last_used_at: str | None | None = Field(default=None, alias="lastUsedAt", description="The date and time the sequence was last used.")
    """The date and time the sequence was last used."""
    locked: bool | None | None = Field(default=None, description="A boolean value determining whether the sequence is locked or not.")
    """A boolean value determining whether the sequence is locked or not."""
    locked_at: str | None | None = Field(default=None, alias="lockedAt", description="The date and time the sequence was locked, or null if currently unlocked.")
    """The date and time the sequence was locked, or null if currently unlocked."""
    max_activations: int | None | None = Field(default=None, alias="maxActivations", description="The maximum number of prospects that can be associated with the sequence. Only applies if the sequence type is 'date'.")
    """The maximum number of prospects that can be associated with the sequence. Only applies if the sequence type is 'date'."""
    negative_reply_count: int | None | None = Field(default=None, alias="negativeReplyCount", description="The total count of negative reply mailings from this sequence.")
    """The total count of negative reply mailings from this sequence."""
    neutral_reply_count: int | None | None = Field(default=None, alias="neutralReplyCount", description="The total count of neutral reply mailings from this sequence.")
    """The total count of neutral reply mailings from this sequence."""
    num_contacted_prospects: int | None | None = Field(default=None, alias="numContactedProspects", description="The total count of prospects who have been either called or emailed.")
    """The total count of prospects who have been either called or emailed."""
    num_replied_prospects: int | None | None = Field(default=None, alias="numRepliedProspects", description="The total count of prospects who have been marked as replied.")
    """The total count of prospects who have been marked as replied."""
    open_count: int | None | None = Field(default=None, alias="openCount", description="The total count of opened mailings from this sequence.")
    """The total count of opened mailings from this sequence."""
    opt_out_count: int | None | None = Field(default=None, alias="optOutCount", description="The total count of opted out mailings from this sequence.")
    """The total count of opted out mailings from this sequence."""
    positive_reply_count: int | None | None = Field(default=None, alias="positiveReplyCount", description="The total count of positive reply mailings from this sequence.")
    """The total count of positive reply mailings from this sequence."""
    primary_reply_action: str | None | None = Field(default=None, alias="primaryReplyAction", description="The action to take when the primary prospect replies. Must be one of 'finish', 'continue', or 'pause'.")
    """The action to take when the primary prospect replies. Must be one of 'finish', 'continue', or 'pause'."""
    primary_reply_pause_duration: int | None | None = Field(default=None, alias="primaryReplyPauseDuration", description="The duration in seconds to pause for (before automatically finishing) after a reply from the primary prospect if the primaryReplyAction is 'pause'.")
    """The duration in seconds to pause for (before automatically finishing) after a reply from the primary prospect if the primaryReplyAction is 'pause'."""
    prospect_click_count: int | None | None = Field(default=None, alias="prospectClickCount", description="Prospect click count")
    """Prospect click count"""
    prospect_contacted_count: int | None | None = Field(default=None, alias="prospectContactedCount", description="Prospect contacted count")
    """Prospect contacted count"""
    prospect_deliver_count: int | None | None = Field(default=None, alias="prospectDeliverCount", description="Prospect deliver count")
    """Prospect deliver count"""
    prospect_open_count: int | None | None = Field(default=None, alias="prospectOpenCount", description="Prospect open count")
    """Prospect open count"""
    prospect_reply_count: int | None | None = Field(default=None, alias="prospectReplyCount", description="Prospect reply count")
    """Prospect reply count"""
    reply_count: int | None | None = Field(default=None, alias="replyCount", description="The total count of replied mailings from this sequence.")
    """The total count of replied mailings from this sequence."""
    sales_motion: str | None | None = Field(default=None, alias="salesMotion", description="The sales engagement type of the sequence.")
    """The sales engagement type of the sequence."""
    schedule_count: int | None | None = Field(default=None, alias="scheduleCount", description="The total count of scheduled mailings from this sequence.")
    """The total count of scheduled mailings from this sequence."""
    schedule_interval_type: str | None | None = Field(default=None, alias="scheduleIntervalType", description="The schedule interval type must be either 'calendar' or 'schedule'")
    """The schedule interval type must be either 'calendar' or 'schedule'"""
    secondary_reply_action: str | None | None = Field(default=None, alias="secondaryReplyAction", description="The action to take when someone other than the primary prospect replies. Must be one of 'finish', 'continue', or 'pause'.")
    """The action to take when someone other than the primary prospect replies. Must be one of 'finish', 'continue', or 'pause'."""
    secondary_reply_pause_duration: int | None | None = Field(default=None, alias="secondaryReplyPauseDuration", description="The duration in seconds to pause for (before automatically finishing) after a reply from anyone other than the primary prospect if the secondaryReplyAction is 'pause'.")
    """The duration in seconds to pause for (before automatically finishing) after a reply from anyone other than the primary prospect if the secondaryReplyAction is 'pause'."""
    sequence_step_count: int | None | None = Field(default=None, alias="sequenceStepCount", description="The total number of sequence steps in this sequence.")
    """The total number of sequence steps in this sequence."""
    share_type: str | None | None = Field(default=None, alias="shareType", description="The sequence share type must be either 'private', 'read_only' or 'shared'.")
    """The sequence share type must be either 'private', 'read_only' or 'shared'."""
    throttle_capacity: int | None | None = Field(default=None, alias="throttleCapacity", description="The maximum number of associated sequence states per user that can be active at a one time.")
    """The maximum number of associated sequence states per user that can be active at a one time."""
    throttle_max_adds_per_day: int | None | None = Field(default=None, alias="throttleMaxAddsPerDay", description="The maximum number of associated sequence states per user that can be added to the sequence each day.")
    """The maximum number of associated sequence states per user that can be added to the sequence each day."""
    throttle_paused: bool | None | None = Field(default=None, alias="throttlePaused", description="A boolean value determining whether the throttling of sequence states is paused or not.")
    """A boolean value determining whether the throttling of sequence states is paused or not."""
    throttle_paused_at: str | None | None = Field(default=None, alias="throttlePausedAt", description="The date and time the sequence state throttling was paused, or null if not currently paused.")
    """The date and time the sequence state throttling was paused, or null if not currently paused."""
    transactional: bool | None | None = Field(default=None, description="A boolean value determining whether prospect opt out preferences are respected. Intended only for non-marketing sequences.")
    """A boolean value determining whether prospect opt out preferences are respected. Intended only for non-marketing sequences."""

class SequenceLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class Sequence(BaseModel):
    """Outreach sequence object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: SequenceAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: SequenceLinks | None = Field(default=None)

class SequencesList(BaseModel):
    """SequencesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Sequence] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class SequenceResponse(BaseModel):
    """SequenceResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Sequence | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class SequenceStateAttributes(BaseModel):
    """Nested schema for SequenceState.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    state: str | None | None = Field(default=None)
    state_changed_at: str | None | None = Field(default=None, alias="stateChangedAt")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")

class SequenceState(BaseModel):
    """Outreach sequence state object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: SequenceStateAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)

class SequenceStatesList(BaseModel):
    """SequenceStatesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[SequenceState] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class SequenceStateResponse(BaseModel):
    """SequenceStateResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: SequenceState | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class SequenceStepAttributes(BaseModel):
    """Nested schema for SequenceStep.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    step_type: str | None | None = Field(default=None, alias="stepType")
    interval: int | None | None = Field(default=None)
    order: int | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    bounce_count: int | None | None = Field(default=None, alias="bounceCount", description="The total count of bounced mailings during this sequence step.")
    """The total count of bounced mailings during this sequence step."""
    call_completed_count: int | None | None = Field(default=None, alias="callCompletedCount", description="Call completed count")
    """Call completed count"""
    call_no_answer_count: int | None | None = Field(default=None, alias="callNoAnswerCount", description="Call no answer count")
    """Call no answer count"""
    click_count: int | None | None = Field(default=None, alias="clickCount", description="The total count of clicked mailings from this sequence step.")
    """The total count of clicked mailings from this sequence step."""
    date: str | None | None = Field(default=None, description="The date this step will activate; only applicable to date-based sequences.")
    """The date this step will activate; only applicable to date-based sequences."""
    deliver_count: int | None | None = Field(default=None, alias="deliverCount", description="The total count of delivered mailings from this sequence step.")
    """The total count of delivered mailings from this sequence step."""
    display_name: str | None | None = Field(default=None, alias="displayName", description="A human-readable display name that captures the step’s type and order.")
    """A human-readable display name that captures the step’s type and order."""
    failure_count: int | None | None = Field(default=None, alias="failureCount", description="The total count of failed mailings from this sequence step.")
    """The total count of failed mailings from this sequence step."""
    negative_reply_count: int | None | None = Field(default=None, alias="negativeReplyCount", description="The total count of negative reply mailings from this sequence step.")
    """The total count of negative reply mailings from this sequence step."""
    neutral_reply_count: int | None | None = Field(default=None, alias="neutralReplyCount", description="The total count of neutral reply mailings from this sequence step.")
    """The total count of neutral reply mailings from this sequence step."""
    open_count: int | None | None = Field(default=None, alias="openCount", description="The total count of opened mailings from this sequence step.")
    """The total count of opened mailings from this sequence step."""
    opt_out_count: int | None | None = Field(default=None, alias="optOutCount", description="The total count of opted out mailings from this sequence step.")
    """The total count of opted out mailings from this sequence step."""
    positive_reply_count: int | None | None = Field(default=None, alias="positiveReplyCount", description="The total count of positive reply mailings from this sequence step.")
    """The total count of positive reply mailings from this sequence step."""
    reply_count: int | None | None = Field(default=None, alias="replyCount", description="The total count of replied mailings from this sequence step.")
    """The total count of replied mailings from this sequence step."""
    schedule_count: int | None | None = Field(default=None, alias="scheduleCount", description="The total count of scheduled mailings from this sequence step.")
    """The total count of scheduled mailings from this sequence step."""
    task_autoskip_delay: int | None | None = Field(default=None, alias="taskAutoskipDelay", description="The optional interval (in seconds) from when tasks created by this sequence step are overdue until they are automatically skipped.")
    """The optional interval (in seconds) from when tasks created by this sequence step are overdue until they are automatically skipped."""
    task_note: str | None | None = Field(default=None, alias="taskNote", description="An optional note to associate with created tasks.")
    """An optional note to associate with created tasks."""

class SequenceStepLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class SequenceStep(BaseModel):
    """Outreach sequence step object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: SequenceStepAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: SequenceStepLinks | None = Field(default=None)

class SequenceStepsList(BaseModel):
    """SequenceStepsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[SequenceStep] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class SequenceStepResponse(BaseModel):
    """SequenceStepResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: SequenceStep | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class OpportunityLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class OpportunityAttributes(BaseModel):
    """Nested schema for Opportunity.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    amount: float | None | None = Field(default=None)
    probability: int | None | None = Field(default=None)
    close_date: str | None | None = Field(default=None, alias="closeDate")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    amount_precise: str | None | None = Field(default=None, alias="amountPrecise", description="The precise amount that the opportunity is worth.")
    """The precise amount that the opportunity is worth."""
    currency_type: str | None | None = Field(default=None, alias="currencyType", description="The ISO code of the currency this opportunity is in.")
    """The ISO code of the currency this opportunity is in."""
    custom1: str | None | None = Field(default=None, description="The value of the opportunity's first custom field.")
    """The value of the opportunity's first custom field."""
    custom10: str | None | None = Field(default=None, description="The value of the opportunity's 10th custom field.")
    """The value of the opportunity's 10th custom field."""
    custom100: str | None | None = Field(default=None, description="The value of the opportunity's 100th custom field.")
    """The value of the opportunity's 100th custom field."""
    custom101: str | None | None = Field(default=None, description="The value of the opportunity’s 101st custom field.")
    """The value of the opportunity’s 101st custom field."""
    custom102: str | None | None = Field(default=None, description="The value of the opportunity’s 102nd custom field.")
    """The value of the opportunity’s 102nd custom field."""
    custom103: str | None | None = Field(default=None, description="The value of the opportunity’s 103rd custom field.")
    """The value of the opportunity’s 103rd custom field."""
    custom104: str | None | None = Field(default=None, description="The value of the opportunity’s 104th custom field.")
    """The value of the opportunity’s 104th custom field."""
    custom105: str | None | None = Field(default=None, description="The value of the opportunity’s 105th custom field.")
    """The value of the opportunity’s 105th custom field."""
    custom106: str | None | None = Field(default=None, description="The value of the opportunity’s 106th custom field.")
    """The value of the opportunity’s 106th custom field."""
    custom107: str | None | None = Field(default=None, description="The value of the opportunity’s 107th custom field.")
    """The value of the opportunity’s 107th custom field."""
    custom108: str | None | None = Field(default=None, description="The value of the opportunity’s 108th custom field.")
    """The value of the opportunity’s 108th custom field."""
    custom109: str | None | None = Field(default=None, description="The value of the opportunity’s 109th custom field.")
    """The value of the opportunity’s 109th custom field."""
    custom11: str | None | None = Field(default=None, description="The value of the opportunity's 11th custom field.")
    """The value of the opportunity's 11th custom field."""
    custom110: str | None | None = Field(default=None, description="The value of the opportunity’s 110th custom field.")
    """The value of the opportunity’s 110th custom field."""
    custom111: str | None | None = Field(default=None, description="The value of the opportunity’s 111th custom field.")
    """The value of the opportunity’s 111th custom field."""
    custom112: str | None | None = Field(default=None, description="The value of the opportunity’s 112th custom field.")
    """The value of the opportunity’s 112th custom field."""
    custom113: str | None | None = Field(default=None, description="The value of the opportunity’s 113th custom field.")
    """The value of the opportunity’s 113th custom field."""
    custom114: str | None | None = Field(default=None, description="The value of the opportunity’s 114th custom field.")
    """The value of the opportunity’s 114th custom field."""
    custom115: str | None | None = Field(default=None, description="The value of the opportunity’s 115th custom field.")
    """The value of the opportunity’s 115th custom field."""
    custom116: str | None | None = Field(default=None, description="The value of the opportunity’s 116th custom field.")
    """The value of the opportunity’s 116th custom field."""
    custom117: str | None | None = Field(default=None, description="The value of the opportunity’s 117th custom field.")
    """The value of the opportunity’s 117th custom field."""
    custom118: str | None | None = Field(default=None, description="The value of the opportunity’s 118th custom field.")
    """The value of the opportunity’s 118th custom field."""
    custom119: str | None | None = Field(default=None, description="The value of the opportunity’s 119th custom field.")
    """The value of the opportunity’s 119th custom field."""
    custom12: str | None | None = Field(default=None, description="The value of the opportunity's 12th custom field.")
    """The value of the opportunity's 12th custom field."""
    custom120: str | None | None = Field(default=None, description="The value of the opportunity’s 120th custom field.")
    """The value of the opportunity’s 120th custom field."""
    custom121: str | None | None = Field(default=None, description="The value of the opportunity’s 121st custom field.")
    """The value of the opportunity’s 121st custom field."""
    custom122: str | None | None = Field(default=None, description="The value of the opportunity’s 122nd custom field.")
    """The value of the opportunity’s 122nd custom field."""
    custom123: str | None | None = Field(default=None, description="The value of the opportunity’s 123rd custom field.")
    """The value of the opportunity’s 123rd custom field."""
    custom124: str | None | None = Field(default=None, description="The value of the opportunity’s 124th custom field.")
    """The value of the opportunity’s 124th custom field."""
    custom125: str | None | None = Field(default=None, description="The value of the opportunity’s 125th custom field.")
    """The value of the opportunity’s 125th custom field."""
    custom126: str | None | None = Field(default=None, description="The value of the opportunity’s 126th custom field.")
    """The value of the opportunity’s 126th custom field."""
    custom127: str | None | None = Field(default=None, description="The value of the opportunity’s 127th custom field.")
    """The value of the opportunity’s 127th custom field."""
    custom128: str | None | None = Field(default=None, description="The value of the opportunity’s 128th custom field.")
    """The value of the opportunity’s 128th custom field."""
    custom129: str | None | None = Field(default=None, description="The value of the opportunity’s 129th custom field.")
    """The value of the opportunity’s 129th custom field."""
    custom13: str | None | None = Field(default=None, description="The value of the opportunity's 13th custom field.")
    """The value of the opportunity's 13th custom field."""
    custom130: str | None | None = Field(default=None, description="The value of the opportunity’s 130th custom field.")
    """The value of the opportunity’s 130th custom field."""
    custom131: str | None | None = Field(default=None, description="The value of the opportunity’s 131st custom field.")
    """The value of the opportunity’s 131st custom field."""
    custom132: str | None | None = Field(default=None, description="The value of the opportunity’s 132nd custom field.")
    """The value of the opportunity’s 132nd custom field."""
    custom133: str | None | None = Field(default=None, description="The value of the opportunity’s 133rd custom field.")
    """The value of the opportunity’s 133rd custom field."""
    custom134: str | None | None = Field(default=None, description="The value of the opportunity’s 134th custom field.")
    """The value of the opportunity’s 134th custom field."""
    custom135: str | None | None = Field(default=None, description="The value of the opportunity’s 135th custom field.")
    """The value of the opportunity’s 135th custom field."""
    custom136: str | None | None = Field(default=None, description="The value of the opportunity’s 136th custom field.")
    """The value of the opportunity’s 136th custom field."""
    custom137: str | None | None = Field(default=None, description="The value of the opportunity’s 137th custom field.")
    """The value of the opportunity’s 137th custom field."""
    custom138: str | None | None = Field(default=None, description="The value of the opportunity’s 138th custom field.")
    """The value of the opportunity’s 138th custom field."""
    custom139: str | None | None = Field(default=None, description="The value of the opportunity’s 139th custom field.")
    """The value of the opportunity’s 139th custom field."""
    custom14: str | None | None = Field(default=None, description="The value of the opportunity's 14th custom field.")
    """The value of the opportunity's 14th custom field."""
    custom140: str | None | None = Field(default=None, description="The value of the opportunity’s 140th custom field.")
    """The value of the opportunity’s 140th custom field."""
    custom141: str | None | None = Field(default=None, description="The value of the opportunity’s 141st custom field.")
    """The value of the opportunity’s 141st custom field."""
    custom142: str | None | None = Field(default=None, description="The value of the opportunity’s 142nd custom field.")
    """The value of the opportunity’s 142nd custom field."""
    custom143: str | None | None = Field(default=None, description="The value of the opportunity’s 143rd custom field.")
    """The value of the opportunity’s 143rd custom field."""
    custom144: str | None | None = Field(default=None, description="The value of the opportunity’s 144th custom field.")
    """The value of the opportunity’s 144th custom field."""
    custom145: str | None | None = Field(default=None, description="The value of the opportunity’s 145th custom field.")
    """The value of the opportunity’s 145th custom field."""
    custom146: str | None | None = Field(default=None, description="The value of the opportunity’s 146th custom field.")
    """The value of the opportunity’s 146th custom field."""
    custom147: str | None | None = Field(default=None, description="The value of the opportunity’s 147th custom field.")
    """The value of the opportunity’s 147th custom field."""
    custom148: str | None | None = Field(default=None, description="The value of the opportunity’s 148th custom field.")
    """The value of the opportunity’s 148th custom field."""
    custom149: str | None | None = Field(default=None, description="The value of the opportunity’s 149th custom field.")
    """The value of the opportunity’s 149th custom field."""
    custom15: str | None | None = Field(default=None, description="The value of the opportunity's 15th custom field.")
    """The value of the opportunity's 15th custom field."""
    custom150: str | None | None = Field(default=None, description="The value of the opportunity’s 150th custom field.")
    """The value of the opportunity’s 150th custom field."""
    custom16: str | None | None = Field(default=None, description="The value of the opportunity's 16th custom field.")
    """The value of the opportunity's 16th custom field."""
    custom17: str | None | None = Field(default=None, description="The value of the opportunity's 17th custom field.")
    """The value of the opportunity's 17th custom field."""
    custom18: str | None | None = Field(default=None, description="The value of the opportunity's 18th custom field.")
    """The value of the opportunity's 18th custom field."""
    custom19: str | None | None = Field(default=None, description="The value of the opportunity's 19th custom field.")
    """The value of the opportunity's 19th custom field."""
    custom2: str | None | None = Field(default=None, description="The value of the opportunity's second custom field.")
    """The value of the opportunity's second custom field."""
    custom20: str | None | None = Field(default=None, description="The value of the opportunity's 20th custom field.")
    """The value of the opportunity's 20th custom field."""
    custom21: str | None | None = Field(default=None, description="The value of the opportunity's 21st custom field.")
    """The value of the opportunity's 21st custom field."""
    custom22: str | None | None = Field(default=None, description="The value of the opportunity's 22nd custom field.")
    """The value of the opportunity's 22nd custom field."""
    custom23: str | None | None = Field(default=None, description="The value of the opportunity's 23rd custom field.")
    """The value of the opportunity's 23rd custom field."""
    custom24: str | None | None = Field(default=None, description="The value of the opportunity's 24th custom field.")
    """The value of the opportunity's 24th custom field."""
    custom25: str | None | None = Field(default=None, description="The value of the opportunity's 25th custom field.")
    """The value of the opportunity's 25th custom field."""
    custom26: str | None | None = Field(default=None, description="The value of the opportunity's 26th custom field.")
    """The value of the opportunity's 26th custom field."""
    custom27: str | None | None = Field(default=None, description="The value of the opportunity's 27th custom field.")
    """The value of the opportunity's 27th custom field."""
    custom28: str | None | None = Field(default=None, description="The value of the opportunity's 28th custom field.")
    """The value of the opportunity's 28th custom field."""
    custom29: str | None | None = Field(default=None, description="The value of the opportunity's 29th custom field.")
    """The value of the opportunity's 29th custom field."""
    custom3: str | None | None = Field(default=None, description="The value of the opportunity's third custom field.")
    """The value of the opportunity's third custom field."""
    custom30: str | None | None = Field(default=None, description="The value of the opportunity's 30th custom field.")
    """The value of the opportunity's 30th custom field."""
    custom31: str | None | None = Field(default=None, description="The value of the opportunity's 31st custom field.")
    """The value of the opportunity's 31st custom field."""
    custom32: str | None | None = Field(default=None, description="The value of the opportunity's 32nd custom field.")
    """The value of the opportunity's 32nd custom field."""
    custom33: str | None | None = Field(default=None, description="The value of the opportunity's 33rd custom field.")
    """The value of the opportunity's 33rd custom field."""
    custom34: str | None | None = Field(default=None, description="The value of the opportunity's 34th custom field.")
    """The value of the opportunity's 34th custom field."""
    custom35: str | None | None = Field(default=None, description="The value of the opportunity's 35th custom field.")
    """The value of the opportunity's 35th custom field."""
    custom36: str | None | None = Field(default=None, description="The value of the opportunity's 36th custom field.")
    """The value of the opportunity's 36th custom field."""
    custom37: str | None | None = Field(default=None, description="The value of the opportunity's 37th custom field.")
    """The value of the opportunity's 37th custom field."""
    custom38: str | None | None = Field(default=None, description="The value of the opportunity's 38th custom field.")
    """The value of the opportunity's 38th custom field."""
    custom39: str | None | None = Field(default=None, description="The value of the opportunity's 39th custom field.")
    """The value of the opportunity's 39th custom field."""
    custom4: str | None | None = Field(default=None, description="The value of the opportunity's fourth custom field.")
    """The value of the opportunity's fourth custom field."""
    custom40: str | None | None = Field(default=None, description="The value of the opportunity's 40th custom field.")
    """The value of the opportunity's 40th custom field."""
    custom41: str | None | None = Field(default=None, description="The value of the opportunity's 41st custom field.")
    """The value of the opportunity's 41st custom field."""
    custom42: str | None | None = Field(default=None, description="The value of the opportunity's 42nd custom field.")
    """The value of the opportunity's 42nd custom field."""
    custom43: str | None | None = Field(default=None, description="The value of the opportunity's 43rd custom field.")
    """The value of the opportunity's 43rd custom field."""
    custom44: str | None | None = Field(default=None, description="The value of the opportunity's 44th custom field.")
    """The value of the opportunity's 44th custom field."""
    custom45: str | None | None = Field(default=None, description="The value of the opportunity's 45th custom field.")
    """The value of the opportunity's 45th custom field."""
    custom46: str | None | None = Field(default=None, description="The value of the opportunity's 46th custom field.")
    """The value of the opportunity's 46th custom field."""
    custom47: str | None | None = Field(default=None, description="The value of the opportunity's 47th custom field.")
    """The value of the opportunity's 47th custom field."""
    custom48: str | None | None = Field(default=None, description="The value of the opportunity's 48th custom field.")
    """The value of the opportunity's 48th custom field."""
    custom49: str | None | None = Field(default=None, description="The value of the opportunity's 49th custom field.")
    """The value of the opportunity's 49th custom field."""
    custom5: str | None | None = Field(default=None, description="The value of the opportunity's fifth custom field.")
    """The value of the opportunity's fifth custom field."""
    custom50: str | None | None = Field(default=None, description="The value of the opportunity's 50th custom field.")
    """The value of the opportunity's 50th custom field."""
    custom51: str | None | None = Field(default=None, description="The value of the opportunity's 51st custom field.")
    """The value of the opportunity's 51st custom field."""
    custom52: str | None | None = Field(default=None, description="The value of the opportunity's 52nd custom field.")
    """The value of the opportunity's 52nd custom field."""
    custom53: str | None | None = Field(default=None, description="The value of the opportunity's 53rd custom field.")
    """The value of the opportunity's 53rd custom field."""
    custom54: str | None | None = Field(default=None, description="The value of the opportunity's 54th custom field.")
    """The value of the opportunity's 54th custom field."""
    custom55: str | None | None = Field(default=None, description="The value of the opportunity's 55th custom field.")
    """The value of the opportunity's 55th custom field."""
    custom56: str | None | None = Field(default=None, description="The value of the opportunity's 56th custom field.")
    """The value of the opportunity's 56th custom field."""
    custom57: str | None | None = Field(default=None, description="The value of the opportunity's 57th custom field.")
    """The value of the opportunity's 57th custom field."""
    custom58: str | None | None = Field(default=None, description="The value of the opportunity's 58th custom field.")
    """The value of the opportunity's 58th custom field."""
    custom59: str | None | None = Field(default=None, description="The value of the opportunity's 59th custom field.")
    """The value of the opportunity's 59th custom field."""
    custom6: str | None | None = Field(default=None, description="The value of the opportunity's sixth custom field.")
    """The value of the opportunity's sixth custom field."""
    custom60: str | None | None = Field(default=None, description="The value of the opportunity's 60th custom field.")
    """The value of the opportunity's 60th custom field."""
    custom61: str | None | None = Field(default=None, description="The value of the opportunity's 61st custom field.")
    """The value of the opportunity's 61st custom field."""
    custom62: str | None | None = Field(default=None, description="The value of the opportunity's 62nd custom field.")
    """The value of the opportunity's 62nd custom field."""
    custom63: str | None | None = Field(default=None, description="The value of the opportunity's 63rd custom field.")
    """The value of the opportunity's 63rd custom field."""
    custom64: str | None | None = Field(default=None, description="The value of the opportunity's 64th custom field.")
    """The value of the opportunity's 64th custom field."""
    custom65: str | None | None = Field(default=None, description="The value of the opportunity's 65th custom field.")
    """The value of the opportunity's 65th custom field."""
    custom66: str | None | None = Field(default=None, description="The value of the opportunity's 66th custom field.")
    """The value of the opportunity's 66th custom field."""
    custom67: str | None | None = Field(default=None, description="The value of the opportunity's 67th custom field.")
    """The value of the opportunity's 67th custom field."""
    custom68: str | None | None = Field(default=None, description="The value of the opportunity's 68th custom field.")
    """The value of the opportunity's 68th custom field."""
    custom69: str | None | None = Field(default=None, description="The value of the opportunity's 69th custom field.")
    """The value of the opportunity's 69th custom field."""
    custom7: str | None | None = Field(default=None, description="The value of the opportunity's seventh custom field.")
    """The value of the opportunity's seventh custom field."""
    custom70: str | None | None = Field(default=None, description="The value of the opportunity's 70th custom field.")
    """The value of the opportunity's 70th custom field."""
    custom71: str | None | None = Field(default=None, description="The value of the opportunity's 71st custom field.")
    """The value of the opportunity's 71st custom field."""
    custom72: str | None | None = Field(default=None, description="The value of the opportunity's 72nd custom field.")
    """The value of the opportunity's 72nd custom field."""
    custom73: str | None | None = Field(default=None, description="The value of the opportunity's 73rd custom field.")
    """The value of the opportunity's 73rd custom field."""
    custom74: str | None | None = Field(default=None, description="The value of the opportunity's 74th custom field.")
    """The value of the opportunity's 74th custom field."""
    custom75: str | None | None = Field(default=None, description="The value of the opportunity's 75th custom field.")
    """The value of the opportunity's 75th custom field."""
    custom76: str | None | None = Field(default=None, description="The value of the opportunity's 76th custom field.")
    """The value of the opportunity's 76th custom field."""
    custom77: str | None | None = Field(default=None, description="The value of the opportunity's 77th custom field.")
    """The value of the opportunity's 77th custom field."""
    custom78: str | None | None = Field(default=None, description="The value of the opportunity's 78th custom field.")
    """The value of the opportunity's 78th custom field."""
    custom79: str | None | None = Field(default=None, description="The value of the opportunity's 79th custom field.")
    """The value of the opportunity's 79th custom field."""
    custom8: str | None | None = Field(default=None, description="The value of the opportunity's eighth custom field.")
    """The value of the opportunity's eighth custom field."""
    custom80: str | None | None = Field(default=None, description="The value of the opportunity's 80th custom field.")
    """The value of the opportunity's 80th custom field."""
    custom81: str | None | None = Field(default=None, description="The value of the opportunity's 81st custom field.")
    """The value of the opportunity's 81st custom field."""
    custom82: str | None | None = Field(default=None, description="The value of the opportunity's 82nd custom field.")
    """The value of the opportunity's 82nd custom field."""
    custom83: str | None | None = Field(default=None, description="The value of the opportunity's 83rd custom field.")
    """The value of the opportunity's 83rd custom field."""
    custom84: str | None | None = Field(default=None, description="The value of the opportunity's 84th custom field.")
    """The value of the opportunity's 84th custom field."""
    custom85: str | None | None = Field(default=None, description="The value of the opportunity's 85th custom field.")
    """The value of the opportunity's 85th custom field."""
    custom86: str | None | None = Field(default=None, description="The value of the opportunity's 86th custom field.")
    """The value of the opportunity's 86th custom field."""
    custom87: str | None | None = Field(default=None, description="The value of the opportunity's 87th custom field.")
    """The value of the opportunity's 87th custom field."""
    custom88: str | None | None = Field(default=None, description="The value of the opportunity's 88th custom field.")
    """The value of the opportunity's 88th custom field."""
    custom89: str | None | None = Field(default=None, description="The value of the opportunity's 89th custom field.")
    """The value of the opportunity's 89th custom field."""
    custom9: str | None | None = Field(default=None, description="The value of the opportunity's ninth custom field.")
    """The value of the opportunity's ninth custom field."""
    custom90: str | None | None = Field(default=None, description="The value of the opportunity's 90th custom field.")
    """The value of the opportunity's 90th custom field."""
    custom91: str | None | None = Field(default=None, description="The value of the opportunity's 91st custom field.")
    """The value of the opportunity's 91st custom field."""
    custom92: str | None | None = Field(default=None, description="The value of the opportunity's 92nd custom field.")
    """The value of the opportunity's 92nd custom field."""
    custom93: str | None | None = Field(default=None, description="The value of the opportunity's 93rd custom field.")
    """The value of the opportunity's 93rd custom field."""
    custom94: str | None | None = Field(default=None, description="The value of the opportunity's 94th custom field.")
    """The value of the opportunity's 94th custom field."""
    custom95: str | None | None = Field(default=None, description="The value of the opportunity's 95th custom field.")
    """The value of the opportunity's 95th custom field."""
    custom96: str | None | None = Field(default=None, description="The value of the opportunity's 96th custom field.")
    """The value of the opportunity's 96th custom field."""
    custom97: str | None | None = Field(default=None, description="The value of the opportunity's 97th custom field.")
    """The value of the opportunity's 97th custom field."""
    custom98: str | None | None = Field(default=None, description="The value of the opportunity's 98th custom field.")
    """The value of the opportunity's 98th custom field."""
    custom99: str | None | None = Field(default=None, description="The value of the opportunity's 99th custom field.")
    """The value of the opportunity's 99th custom field."""
    custom_id: str | None | None = Field(default=None, alias="customId", description="A custom ID for the opportunity, often referencing an ID in an external system.")
    """A custom ID for the opportunity, often referencing an ID in an external system."""
    description: str | None | None = Field(default=None, description="A description of the opportunity.")
    """A description of the opportunity."""
    external_created_at: str | None | None = Field(default=None, alias="externalCreatedAt", description="The date the opportunity was created in the external system.")
    """The date the opportunity was created in the external system."""
    external_updated_at: str | None | None = Field(default=None, alias="externalUpdatedAt", description="The date the opportunity was last updated in the external system.")
    """The date the opportunity was last updated in the external system."""
    forecast_category: str | None | None = Field(default=None, alias="forecastCategory", description="The category or classification used to predict the likelihood of closing an opportunity.")
    """The category or classification used to predict the likelihood of closing an opportunity."""
    health_category: str | None | None = Field(default=None, alias="healthCategory", description="Health category")
    """Health category"""
    health_score: int | None | None = Field(default=None, alias="healthScore", description="Health score")
    """Health score"""
    lead_source: str | None | None = Field(default=None, alias="leadSource", description="Source of this opportunity, such as Advertisement or Trade Show")
    """Source of this opportunity, such as Advertisement or Trade Show"""
    lost_reason: str | None | None = Field(default=None, alias="lostReason", description="The reason why an opportunity or deal was lost.")
    """The reason why an opportunity or deal was lost."""
    map_link: str | None | None = Field(default=None, alias="mapLink", description="A link to the SamePlan MAP (Mutual Action Plan) associated with this opportunity.")
    """A link to the SamePlan MAP (Mutual Action Plan) associated with this opportunity."""
    map_next_steps: str | None | None = Field(default=None, alias="mapNextSteps", description="The next event in the timeline that has yet to be completed for the SamePlan MAP (Mutual Action Plan).")
    """The next event in the timeline that has yet to be completed for the SamePlan MAP (Mutual Action Plan)."""
    map_number_of_overdue_tasks: int | None | None = Field(default=None, alias="mapNumberOfOverdueTasks", description="Map number of overdue tasks")
    """Map number of overdue tasks"""
    map_status: str | None | None = Field(default=None, alias="mapStatus", description="The status of the SamePlan MAP (Mutual Action Plan) based on how well both parties are trending towards the plan.")
    """The status of the SamePlan MAP (Mutual Action Plan) based on how well both parties are trending towards the plan."""
    next_step: str | None | None = Field(default=None, alias="nextStep", description="The next step to take for the opportunity.")
    """The next step to take for the opportunity."""
    opportunity_type: str | None | None = Field(default=None, alias="opportunityType", description="The type of opportunity.")
    """The type of opportunity."""
    prospecting_rep_id: str | None | None = Field(default=None, alias="prospectingRepId", description="The ID of the sales rep that prospects the opportunity.")
    """The ID of the sales rep that prospects the opportunity."""
    record_type: str | None | None = Field(default=None, alias="recordType", description="The type or category of the record, such as Opportunity, Lead, or Deal, used to classify and organize different stages in the sales process")
    """The type or category of the record, such as Opportunity, Lead, or Deal, used to classify and organize different stages in the sales process"""
    sharing_team_id: str | None | None = Field(default=None, alias="sharingTeamId", description="The ID of the sharing team associated with this object. Access is currently in beta.")
    """The ID of the sharing team associated with this object. Access is currently in beta."""
    state: str | None | None = Field(default=None, description="State")
    """State"""
    tags: list[str] | None | None = Field(default=None, description="Tags associated with the opportunity.")
    """Tags associated with the opportunity."""
    touched_at: str | None | None = Field(default=None, alias="touchedAt", description="The last time an event happened for an opportunity.")
    """The last time an event happened for an opportunity."""
    trashed_at: str | None | None = Field(default=None, alias="trashedAt", description="The date a prospect was soft deleted.")
    """The date a prospect was soft deleted."""

class Opportunity(BaseModel):
    """Outreach opportunity object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: OpportunityAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: OpportunityLinks | None = Field(default=None)

class OpportunitiesList(BaseModel):
    """OpportunitiesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Opportunity] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class OpportunityResponse(BaseModel):
    """OpportunityResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Opportunity | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class CallAttributes(BaseModel):
    """Nested schema for Call.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    direction: str | None | None = Field(default=None)
    outcome: str | None | None = Field(default=None)
    state: str | None | None = Field(default=None)
    note: str | None | None = Field(default=None)
    from_: str | None | None = Field(default=None, alias="from")
    to: str | None | None = Field(default=None)
    answered_at: str | None | None = Field(default=None, alias="answeredAt")
    completed_at: str | None | None = Field(default=None, alias="completedAt")
    dialed_at: str | None | None = Field(default=None, alias="dialedAt")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    external_vendor: str | None | None = Field(default=None, alias="externalVendor", description="The voice provider of the call. Can be blank.")
    """The voice provider of the call. Can be blank."""
    recording_url: str | None | None = Field(default=None, alias="recordingUrl", description="The URL of the call's audio recording. This field only accepts HTTP and HTTPS values.")
    """The URL of the call's audio recording. This field only accepts HTTP and HTTPS values."""
    returned_at: str | None | None = Field(default=None, alias="returnedAt", description="The date and time the call was returned.")
    """The date and time the call was returned."""
    sequence_action: str | None | None = Field(default=None, alias="sequenceAction", description="The action to take on the associated sequence; must be either 'Advance', 'Finish', 'Finish - No Reply', or 'Finish - Replied'.")
    """The action to take on the associated sequence; must be either 'Advance', 'Finish', 'Finish - No Reply', or 'Finish - Replied'."""
    should_record_call: bool | None | None = Field(default=None, alias="shouldRecordCall", description="Indicated whether or not the call is recorded.")
    """Indicated whether or not the call is recorded."""
    state_changed_at: str | None | None = Field(default=None, alias="stateChangedAt", description="The date and time the call’s state last changed.")
    """The date and time the call’s state last changed."""
    tags: list[str] | None | None = Field(default=None, description="A list of tag values associated with the call (e.g. ['Interested', 'Meeting Booked']).")
    """A list of tag values associated with the call (e.g. ['Interested', 'Meeting Booked'])."""
    uid: str | None | None = Field(default=None, description="The Outreach voice trace id.")
    """The Outreach voice trace id."""
    user_call_type: str | None | None = Field(default=None, alias="userCallType", description="The type of call placed within the Outreach client; must be either 'bridge' or 'voip'.")
    """The type of call placed within the Outreach client; must be either 'bridge' or 'voip'."""
    vendor_call_id: str | None | None = Field(default=None, alias="vendorCallId", description="The call-id as recorded by the voice provider. Can be blank.")
    """The call-id as recorded by the voice provider. Can be blank."""
    voicemail_recording_url: str | None | None = Field(default=None, alias="voicemailRecordingUrl", description="The URL of the call’s voicemail audio recording.")
    """The URL of the call’s voicemail audio recording."""

class CallLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class Call(BaseModel):
    """Outreach call object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: CallAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: CallLinks | None = Field(default=None)

class CallsList(BaseModel):
    """CallsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Call] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class CallResponse(BaseModel):
    """CallResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Call | None = Field(default=None)

class CallDispositionLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class CallDispositionAttributes(BaseModel):
    """Nested schema for CallDisposition.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    outcome: str | None | None = Field(default=None)
    order: int | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    default_for_outbound_voicemail: bool | None | None = Field(default=None, alias="defaultForOutboundVoicemail", description="Default for outbound voicemail")
    """Default for outbound voicemail"""

class CallDisposition(BaseModel):
    """Outreach call disposition object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: CallDispositionAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: CallDispositionLinks | None = Field(default=None)

class CallDispositionsList(BaseModel):
    """CallDispositionsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[CallDisposition] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class CallDispositionResponse(BaseModel):
    """CallDispositionResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CallDisposition | None = Field(default=None)

class CallPurposeAttributes(BaseModel):
    """Nested schema for CallPurpose.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    order: int | None | None = Field(default=None, description="The purpose’s display order within the collection.")
    """The purpose’s display order within the collection."""

class CallPurposeLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class CallPurpose(BaseModel):
    """Outreach call purpose object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: CallPurposeAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: CallPurposeLinks | None = Field(default=None)

class CallPurposesList(BaseModel):
    """CallPurposesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[CallPurpose] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class CallPurposeResponse(BaseModel):
    """CallPurposeResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CallPurpose | None = Field(default=None)

class MailingLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class MailingAttributes(BaseModel):
    """Nested schema for Mailing.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    mailing_type: str | None | None = Field(default=None, alias="mailingType")
    state: str | None | None = Field(default=None)
    subject: str | None | None = Field(default=None)
    body_html: str | None | None = Field(default=None, alias="bodyHtml")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    body_text: str | None | None = Field(default=None, alias="bodyText", description="The plain-text representation of the 'bodyHTML' field.")
    """The plain-text representation of the 'bodyHTML' field."""
    bounced_at: str | None | None = Field(default=None, alias="bouncedAt", description="The date and time the email was bounced.")
    """The date and time the email was bounced."""
    classification: list[Any] | None | None = Field(default=None, description="Classification")
    """Classification"""
    click_count: int | None | None = Field(default=None, alias="clickCount", description="The total number of times links within the email were clicked (if the message is tracking links).")
    """The total number of times links within the email were clicked (if the message is tracking links)."""
    clicked_at: str | None | None = Field(default=None, alias="clickedAt", description="The most recent date and time a link was clicked (if the message is tracking links).")
    """The most recent date and time a link was clicked (if the message is tracking links)."""
    delivered_at: str | None | None = Field(default=None, alias="deliveredAt", description="The date and time the email was delivered.")
    """The date and time the email was delivered."""
    error_backtrace: str | None | None = Field(default=None, alias="errorBacktrace", description="Technical details explaining the mailing's error.")
    """Technical details explaining the mailing's error."""
    error_reason: str | None | None = Field(default=None, alias="errorReason", description="A summary explaining the mailing's error.")
    """A summary explaining the mailing's error."""
    follow_up_task_scheduled_at: str | None | None = Field(default=None, alias="followUpTaskScheduledAt", description="The date and time of when a follow-up task should be due for this mailing.")
    """The date and time of when a follow-up task should be due for this mailing."""
    follow_up_task_type: str | None | None = Field(default=None, alias="followUpTaskType", description="The type of follow-up task to create. Possible values are 'follow_up' or 'no_reply'.")
    """The type of follow-up task to create. Possible values are 'follow_up' or 'no_reply'."""
    mailbox_address: str | None | None = Field(default=None, alias="mailboxAddress", description="The email address the mailing was sent from.")
    """The email address the mailing was sent from."""
    marked_as_spam_at: str | None | None = Field(default=None, alias="markedAsSpamAt", description="The date and time the email was marked as spam.")
    """The date and time the email was marked as spam."""
    message_id: str | None | None = Field(default=None, alias="messageId", description="The MIME content Message-ID of the delivered message.")
    """The MIME content Message-ID of the delivered message."""
    notify_thread_condition: str | None | None = Field(default=None, alias="notifyThreadCondition", description="The condition of when to bump this mailing to the top of the user's inbox. Possible values are 'always' or 'no_reply'.")
    """The condition of when to bump this mailing to the top of the user's inbox. Possible values are 'always' or 'no_reply'."""
    notify_thread_scheduled_at: str | None | None = Field(default=None, alias="notifyThreadScheduledAt", description="The date and time of when this mailing should be bumped to the top of the user's inbox.")
    """The date and time of when this mailing should be bumped to the top of the user's inbox."""
    notify_thread_status: str | None | None = Field(default=None, alias="notifyThreadStatus", description="The status of the bump. Possible values are 'pending', 'sent' or 'skipped'.")
    """The status of the bump. Possible values are 'pending', 'sent' or 'skipped'."""
    open_count: int | None | None = Field(default=None, alias="openCount", description="The total number of times the email was opened (if the message is tracking opens).")
    """The total number of times the email was opened (if the message is tracking opens)."""
    opened_at: str | None | None = Field(default=None, alias="openedAt", description="The most recent date and time the email was opened (if the message is tracking opens).")
    """The most recent date and time the email was opened (if the message is tracking opens)."""
    override_safety_settings: bool | None | None = Field(default=None, alias="overrideSafetySettings", description="A boolean value whether users can override submission if template variables have not all been replaced.")
    """A boolean value whether users can override submission if template variables have not all been replaced."""
    references: list[str] | None | None = Field(default=None, description="A list of references for the mailing taken from the email header.")
    """A list of references for the mailing taken from the email header."""
    replied_at: str | None | None = Field(default=None, alias="repliedAt", description="The date and time the email was replied to.")
    """The date and time the email was replied to."""
    retry_at: str | None | None = Field(default=None, alias="retryAt", description="The date and time the email will rety to send.")
    """The date and time the email will rety to send."""
    retry_count: int | None | None = Field(default=None, alias="retryCount", description="The number of times the email has been retried to send.")
    """The number of times the email has been retried to send."""
    retry_interval: int | None | None = Field(default=None, alias="retryInterval", description="The amount of time in seconds between retry attempts.")
    """The amount of time in seconds between retry attempts."""
    scheduled_at: str | None | None = Field(default=None, alias="scheduledAt", description="The date and time the email is scheduled to send.")
    """The date and time the email is scheduled to send."""
    state_changed_at: str | None | None = Field(default=None, alias="stateChangedAt", description="The date and time the state last changed.")
    """The date and time the state last changed."""
    track_links: bool | None | None = Field(default=None, alias="trackLinks", description="A boolean value whether the mailing is tracking link clicks.")
    """A boolean value whether the mailing is tracking link clicks."""
    track_opens: bool | None | None = Field(default=None, alias="trackOpens", description="A boolean value whether the mailing is tracking email opens.")
    """A boolean value whether the mailing is tracking email opens."""
    unsubscribed_at: str | None | None = Field(default=None, alias="unsubscribedAt", description="The date and time the recepient unsubscribed from the mailing's sequence.")
    """The date and time the recepient unsubscribed from the mailing's sequence."""

class Mailing(BaseModel):
    """Outreach mailing object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: MailingAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: MailingLinks | None = Field(default=None)

class MailingsList(BaseModel):
    """MailingsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Mailing] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class MailingResponse(BaseModel):
    """MailingResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Mailing | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class MailboxLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class MailboxAttributes(BaseModel):
    """Nested schema for Mailbox.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    auth_id: int | None | None = Field(default=None, alias="authId", description="The auth id associated with the mailbox.")
    """The auth id associated with the mailbox."""
    editable: bool | None | None = Field(default=None, description="A boolean value to indicate if the user has the permission to edit mailbox fields.")
    """A boolean value to indicate if the user has the permission to edit mailbox fields."""
    email_hash: str | None | None = Field(default=None, alias="emailHash", description="Hashed email address of the mailbox.")
    """Hashed email address of the mailbox."""
    email_provider: str | None | None = Field(default=None, alias="emailProvider", description="The mail service provider. While not a required field, it is strongly recommended to use one of 'exchange_online', 'exchange_server', 'gmail', 'gmail_api', 'google_oauth2', 'intermedia', 'office365_oauth2', 'microsoft_hma_oauth2', 'office_365', 'rackspace'. If no value is provided, send and sync will make assumptions based on the ews, imap, and smtp values provided.")
    """The mail service provider. While not a required field, it is strongly recommended to use one of 'exchange_online', 'exchange_server', 'gmail', 'gmail_api', 'google_oauth2', 'intermedia', 'office365_oauth2', 'microsoft_hma_oauth2', 'office_365', 'rackspace'. If no value is provided, send and sync will make assumptions based on the ews, imap, and smtp values provided."""
    email_signature: str | None | None = Field(default=None, alias="emailSignature", description="The default signature, in HTML, to be appended to sent email messages.")
    """The default signature, in HTML, to be appended to sent email messages."""
    ews_custom_search_folder: bool | None | None = Field(default=None, alias="ewsCustomSearchFolder", description="EWS custom search folder")
    """EWS custom search folder"""
    ews_delegate_sync: bool | None | None = Field(default=None, alias="ewsDelegateSync", description="EWS delegate sync")
    """EWS delegate sync"""
    ews_endpoint: str | None | None = Field(default=None, alias="ewsEndpoint", description="The url of the Exchange Web Service.")
    """The url of the Exchange Web Service."""
    ews_impersonation: bool | None | None = Field(default=None, alias="ewsImpersonation", description="EWS impersonation")
    """EWS impersonation"""
    ews_ssl_verify_mode: int | None | None = Field(default=None, alias="ewsSslVerifyMode", description="The SSL verify mode, represented as an integer, the EWS connection will used. (verify none=0, verify peer=1, verify client once=4, verify fail if no peer cert=2)")
    """The SSL verify mode, represented as an integer, the EWS connection will used. (verify none=0, verify peer=1, verify client once=4, verify fail if no peer cert=2)"""
    exchange_version: str | None | None = Field(default=None, alias="exchangeVersion", description="The version of Exchange. Must be one of 'Exchange2007', 'Exchange2007_SP1', 'Exchange2010', 'Exchange2010_SP1', 'Exchange2010_SP2', 'Exchange2013', 'Exchange2013_SP1'.")
    """The version of Exchange. Must be one of 'Exchange2007', 'Exchange2007_SP1', 'Exchange2010', 'Exchange2010_SP1', 'Exchange2010_SP2', 'Exchange2013', 'Exchange2013_SP1'."""
    imap_host: str | None | None = Field(default=None, alias="imapHost", description="The address of the IMAP host, used for syncing (e.g. 'imap.gmail.com').")
    """The address of the IMAP host, used for syncing (e.g. 'imap.gmail.com')."""
    imap_port: int | None | None = Field(default=None, alias="imapPort", description="The port number the IMAP server is using (e.g. '993').")
    """The port number the IMAP server is using (e.g. '993')."""
    imap_ssl: bool | None | None = Field(default=None, alias="imapSsl", description="A boolean value whether the IMAP connection will use SSL.")
    """A boolean value whether the IMAP connection will use SSL."""
    max_emails_per_day: int | None | None = Field(default=None, alias="maxEmailsPerDay", description="The maximum number of in/out emails per day.")
    """The maximum number of in/out emails per day."""
    max_mailings_per_day: int | None | None = Field(default=None, alias="maxMailingsPerDay", description="The maximum number of emails the application can send in a day from this mailbox. Recommended value is 500.")
    """The maximum number of emails the application can send in a day from this mailbox. Recommended value is 500."""
    max_mailings_per_week: int | None | None = Field(default=None, alias="maxMailingsPerWeek", description="The maximum number of emails the application can send within a week from this mailbox. Recommended value is 5000.")
    """The maximum number of emails the application can send within a week from this mailbox. Recommended value is 5000."""
    opt_out_message: str | None | None = Field(default=None, alias="optOutMessage", description="The message displayed on the unsubscribe confirmation page, seen after clicking the unsubscribe link in the email (e.g. 'To unsubscribe, click the button below.').")
    """The message displayed on the unsubscribe confirmation page, seen after clicking the unsubscribe link in the email (e.g. 'To unsubscribe, click the button below.')."""
    opt_out_signature: str | None | None = Field(default=None, alias="optOutSignature", description="The message below the signature, in HTML, when the sequence requires an unsubscribe link (e.g. 'If you'd like me to stop sending you emails, please ` click here `').")
    """The message below the signature, in HTML, when the sequence requires an unsubscribe link (e.g. 'If you'd like me to stop sending you emails, please ` click here `')."""
    prospect_email_exclusions: str | None | None = Field(default=None, alias="prospectEmailExclusions", description="A list (provided as a string, newline-delimited) of email address patterns to be excluded from syncing (e.g. '`*@outreach.io daniel@example.com`').")
    """A list (provided as a string, newline-delimited) of email address patterns to be excluded from syncing (e.g. '`*@outreach.io daniel@example.com`')."""
    provider_id: int | None | None = Field(default=None, alias="providerId", description="The id of the provider associated with this calendar.")
    """The id of the provider associated with this calendar."""
    provider_type: str | None | None = Field(default=None, alias="providerType", description="Email provider type.")
    """Email provider type."""
    send_disabled: bool | None | None = Field(default=None, alias="sendDisabled", description="A boolean value whether sending is disabled from this mailbox.")
    """A boolean value whether sending is disabled from this mailbox."""
    send_errored_at: str | None | None = Field(default=None, alias="sendErroredAt", description="The date and time the most recent send error occurred.")
    """The date and time the most recent send error occurred."""
    send_max_retries: int | None | None = Field(default=None, alias="sendMaxRetries", description="The maximum number of times to auto-retry a delivery when it fails.")
    """The maximum number of times to auto-retry a delivery when it fails."""
    send_method: str | None | None = Field(default=None, alias="sendMethod", description="The method used for sending email. Must be either 'ews', 'sendgrid', or 'smtp'.")
    """The method used for sending email. Must be either 'ews', 'sendgrid', or 'smtp'."""
    send_period: int | None | None = Field(default=None, alias="sendPeriod", description="The amount of time in seconds that the number of sendThreshold emails can be sent. Recommended value is two deliveries per minute (sendPeriod is 60).")
    """The amount of time in seconds that the number of sendThreshold emails can be sent. Recommended value is two deliveries per minute (sendPeriod is 60)."""
    send_permanent_error_at: str | None | None = Field(default=None, alias="sendPermanentErrorAt", description="Send permanent error at")
    """Send permanent error at"""
    send_requires_sync: bool | None | None = Field(default=None, alias="sendRequiresSync", description="A boolean value whether the mailbox is required to be recently synced before sending.")
    """A boolean value whether the mailbox is required to be recently synced before sending."""
    send_state: str | None | None = Field(default=None, alias="sendState", description="Send state")
    """Send state"""
    send_success_at: str | None | None = Field(default=None, alias="sendSuccessAt", description="The date and time the most recent successful email send occurred.")
    """The date and time the most recent successful email send occurred."""
    send_threshold: int | None | None = Field(default=None, alias="sendThreshold", description="The maximum number of email sends per the sendPeriod amount of time. Recommended value is two deliveries per minute (sendThreshold is 2).")
    """The maximum number of email sends per the sendPeriod amount of time. Recommended value is two deliveries per minute (sendThreshold is 2)."""
    sendgrid_webhook_url: str | None | None = Field(default=None, alias="sendgridWebhookUrl", description="The endpoint required within the SendGrid account settings to support bounce and spam-report tracking.")
    """The endpoint required within the SendGrid account settings to support bounce and spam-report tracking."""
    smtp_host: str | None | None = Field(default=None, alias="smtpHost", description="The address of the SMTP host, used for sending (e.g. 'smtp.gmail.com').")
    """The address of the SMTP host, used for sending (e.g. 'smtp.gmail.com')."""
    smtp_port: int | None | None = Field(default=None, alias="smtpPort", description="The port number the SMTP server is using (e.g. '587').")
    """The port number the SMTP server is using (e.g. '587')."""
    smtp_ssl: bool | None | None = Field(default=None, alias="smtpSsl", description="A boolean value whether the SMTP connection will use SSL.")
    """A boolean value whether the SMTP connection will use SSL."""
    smtp_username: str | None | None = Field(default=None, alias="smtpUsername", description="The username for the SMTP account. This value should be left blank unless a separate SMTP account is being used for sending (i.e. not the mailbox's main username/password).")
    """The username for the SMTP account. This value should be left blank unless a separate SMTP account is being used for sending (i.e. not the mailbox's main username/password)."""
    sync_active_frequency: int | None | None = Field(default=None, alias="syncActiveFrequency", description="The amount of time in seconds between syncing when the user is actively using the application.")
    """The amount of time in seconds between syncing when the user is actively using the application."""
    sync_disabled: bool | None | None = Field(default=None, alias="syncDisabled", description="A boolean value whether syncing is disabled from this mailbox.")
    """A boolean value whether syncing is disabled from this mailbox."""
    sync_errored_at: str | None | None = Field(default=None, alias="syncErroredAt", description="The date and time the most recent sync error occurred.")
    """The date and time the most recent sync error occurred."""
    sync_finished_at: str | None | None = Field(default=None, alias="syncFinishedAt", description="The date and time the most recent sync finished.")
    """The date and time the most recent sync finished."""
    sync_method: str | None | None = Field(default=None, alias="syncMethod", description="The method used for syncing email. Must be either 'ews', 'gmail_api', or 'imap'.")
    """The method used for syncing email. Must be either 'ews', 'gmail_api', or 'imap'."""
    sync_outreach_folder: bool | None | None = Field(default=None, alias="syncOutreachFolder", description="A boolean value whether the folder for syncing is named 'Outreach' instead of 'Inbox'. Only available for Exchange version 'Exchange2007_SP1'.")
    """A boolean value whether the folder for syncing is named 'Outreach' instead of 'Inbox'. Only available for Exchange version 'Exchange2007_SP1'."""
    sync_passive_frequency: int | None | None = Field(default=None, alias="syncPassiveFrequency", description="The amount of time in seconds between syncing when the user is not actively using the application.")
    """The amount of time in seconds between syncing when the user is not actively using the application."""
    sync_state: str | None | None = Field(default=None, alias="syncState", description="Sync state")
    """Sync state"""
    sync_success_at: str | None | None = Field(default=None, alias="syncSuccessAt", description="The date and time the most recent successful email sync occurred.")
    """The date and time the most recent successful email sync occurred."""
    user_id: int | None | None = Field(default=None, alias="userId", description="The id of the user associated with this mailbox.")
    """The id of the user associated with this mailbox."""
    username: str | None | None = Field(default=None, description="The username of the email account. While not a required field, a username is necessary for most email providers outside of OAuth. This value is normally the same as the email address.")
    """The username of the email account. While not a required field, a username is necessary for most email providers outside of OAuth. This value is normally the same as the email address."""

class Mailbox(BaseModel):
    """Outreach mailbox object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: MailboxAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: MailboxLinks | None = Field(default=None)

class MailboxesList(BaseModel):
    """MailboxesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Mailbox] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class MailboxResponse(BaseModel):
    """MailboxResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Mailbox | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class TaskAttributes(BaseModel):
    """Nested schema for Task.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: str | None | None = Field(default=None)
    state: str | None | None = Field(default=None)
    note: str | None | None = Field(default=None)
    due_at: str | None | None = Field(default=None, alias="dueAt")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    autoskip_at: str | None | None = Field(default=None, alias="autoskipAt", description="The optional date and time when the task will automatically be skipped. Tasks with an empty autoskip_at will never be autoskipped.")
    """The optional date and time when the task will automatically be skipped. Tasks with an empty autoskip_at will never be autoskipped."""
    compiled_sequence_template_html: str | None | None = Field(default=None, alias="compiledSequenceTemplateHtml", description="The compiled template HTML of incomplete SMS or LinkedIn tasks associated with a sequence.")
    """The compiled template HTML of incomplete SMS or LinkedIn tasks associated with a sequence."""
    completed: bool | None | None = Field(default=None, description="A boolean value whether the task has been completed.")
    """A boolean value whether the task has been completed."""
    completed_at: str | None | None = Field(default=None, alias="completedAt", description="The date and time the task was completed.")
    """The date and time the task was completed."""
    opportunity_association: str | None | None = Field(default=None, alias="opportunityAssociation", description="The optional opportunity rule associated with the task. Can be 'recent_created', 'recent_updated', 'noop'.")
    """The optional opportunity rule associated with the task. Can be 'recent_created', 'recent_updated', 'noop'."""
    scheduled_at: str | None | None = Field(default=None, alias="scheduledAt", description="The date and time the pending task is scheduled for.")
    """The date and time the pending task is scheduled for."""
    state_changed_at: str | None | None = Field(default=None, alias="stateChangedAt", description="The date and time the state last changed.")
    """The date and time the state last changed."""
    task_type: str | None | None = Field(default=None, alias="taskType", description="The type of task. Can be 'follow_up', 'manual', 'no_reply', 'sequence_open', 'sequence_click', 'sequence_step_call', 'sequence_step_email', 'sequence_step_linkedin_interact_with_post', 'sequence_step_linkedin_other', 'sequence_step_linkedin_send_connection_request', 'sequence_step_linkedin_send_message', 'sequence_step_linkedin_view_profile', 'sequence_step_sms', 'sequence_step_task', or 'touch'. Tasks created through the API will automatically be 'manual' tasks.")
    """The type of task. Can be 'follow_up', 'manual', 'no_reply', 'sequence_open', 'sequence_click', 'sequence_step_call', 'sequence_step_email', 'sequence_step_linkedin_interact_with_post', 'sequence_step_linkedin_other', 'sequence_step_linkedin_send_connection_request', 'sequence_step_linkedin_send_message', 'sequence_step_linkedin_view_profile', 'sequence_step_sms', 'sequence_step_task', or 'touch'. Tasks created through the API will automatically be 'manual' tasks."""

class TaskLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class Task(BaseModel):
    """Outreach task object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: TaskAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: TaskLinks | None = Field(default=None)

class TasksList(BaseModel):
    """TasksList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Task] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class TaskResponse(BaseModel):
    """TaskResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Task | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class UserAttributes(BaseModel):
    """Nested schema for User.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: str | None | None = Field(default=None, alias="firstName")
    last_name: str | None | None = Field(default=None, alias="lastName")
    email: str | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    accounts_view_id: int | None | None = Field(default=None, alias="accountsViewId", description="The default smart view to load on the account index view.")
    """The default smart view to load on the account index view."""
    active_prospects_count: int | None | None = Field(default=None, alias="activeProspectsCount", description="Active prospects count")
    """Active prospects count"""
    activity_notifications_disabled: bool | None | None = Field(default=None, alias="activityNotificationsDisabled", description="A boolean value whether the user's activity notifications are disabled.")
    """A boolean value whether the user's activity notifications are disabled."""
    bounce_warning_email_enabled: bool | None | None = Field(default=None, alias="bounceWarningEmailEnabled", description="A boolean value whether the user's bounce warning emails are enabled.")
    """A boolean value whether the user's bounce warning emails are enabled."""
    bridge_phone: str | None | None = Field(default=None, alias="bridgePhone", description="The telephone number of the user's outbound bridge phone.")
    """The telephone number of the user's outbound bridge phone."""
    bridge_phone_extension: str | None | None = Field(default=None, alias="bridgePhoneExtension", description="The extension number of the user's outbound bridge phone.")
    """The extension number of the user's outbound bridge phone."""
    calls_view_id: int | None | None = Field(default=None, alias="callsViewId", description="The default smart view to load on the calls view.")
    """The default smart view to load on the calls view."""
    controlled_tab_default: str | None | None = Field(default=None, alias="controlledTabDefault", description="The user's preferred default tab to open when in task flow.")
    """The user's preferred default tab to open when in task flow."""
    current_sign_in_at: str | None | None = Field(default=None, alias="currentSignInAt", description="The date and time the user most recently signed in.")
    """The date and time the user most recently signed in."""
    custom1: str | None | None = Field(default=None, description="The value of the user's first custom field.")
    """The value of the user's first custom field."""
    custom2: str | None | None = Field(default=None, description="The value of the user's second custom field.")
    """The value of the user's second custom field."""
    custom3: str | None | None = Field(default=None, description="The value of the user's third custom field.")
    """The value of the user's third custom field."""
    custom4: str | None | None = Field(default=None, description="The value of the user's fourth custom field.")
    """The value of the user's fourth custom field."""
    custom5: str | None | None = Field(default=None, description="The value of the user's fifth custom field.")
    """The value of the user's fifth custom field."""
    daily_digest_email_enabled: bool | None | None = Field(default=None, alias="dailyDigestEmailEnabled", description="A boolean value whether the user's daily digest emails are enabled.")
    """A boolean value whether the user's daily digest emails are enabled."""
    default_ruleset_id: int | None | None = Field(default=None, alias="defaultRulesetId", description="The id of the default ruleset assigned to the user.")
    """The id of the default ruleset assigned to the user."""
    default_schedule_id: int | None | None = Field(default=None, alias="defaultScheduleId", description="Default schedule ID")
    """Default schedule ID"""
    duties: Any | None = Field(default=None, description="A collection of the user's work roles.")
    """A collection of the user's work roles."""
    duties_set_at: str | None | None = Field(default=None, alias="dutiesSetAt", description="Duties set at")
    """Duties set at"""
    enable_voice_recordings: bool | None | None = Field(default=None, alias="enableVoiceRecordings", description="A boolean value whether the user has voice recordings enabled.")
    """A boolean value whether the user has voice recordings enabled."""
    engagement_emails_enabled: bool | None | None = Field(default=None, alias="engagementEmailsEnabled", description="A boolean value whether the user has engagement emails enabled.")
    """A boolean value whether the user has engagement emails enabled."""
    global_id: str | None | None = Field(default=None, alias="globalId", description="Global ID")
    """Global ID"""
    guest: bool | None | None = Field(default=None, description="Guest")
    """Guest"""
    inbound_bridge_phone: str | None | None = Field(default=None, alias="inboundBridgePhone", description="The telephone number of the user's inbound bridge phone.")
    """The telephone number of the user's inbound bridge phone."""
    inbound_bridge_phone_extension: str | None | None = Field(default=None, alias="inboundBridgePhoneExtension", description="The extension number of the user's inbound bridge phone.")
    """The extension number of the user's inbound bridge phone."""
    inbound_call_behavior: str | None | None = Field(default=None, alias="inboundCallBehavior", description="The behavior of inbound calls. Must be either 'inbound_bridge' or 'inbound_voicemail'.")
    """The behavior of inbound calls. Must be either 'inbound_bridge' or 'inbound_voicemail'."""
    inbound_phone_type: str | None | None = Field(default=None, alias="inboundPhoneType", description="The user's type of telephone for inbound calls. Must be either 'bridge', 'voip' or 'bridge_and_voip'.")
    """The user's type of telephone for inbound calls. Must be either 'bridge', 'voip' or 'bridge_and_voip'."""
    inbound_voicemail_custom_message_text: str | None | None = Field(default=None, alias="inboundVoicemailCustomMessageText", description="The message for inbound voicemails (e.g. 'Please leave a message and I will get back to you as soon I can').")
    """The message for inbound voicemails (e.g. 'Please leave a message and I will get back to you as soon I can')."""
    inbound_voicemail_message_text_voice: str | None | None = Field(default=None, alias="inboundVoicemailMessageTextVoice", description="The gender of the voice that reads the voicemail message. Must be either 'man' or 'woman'.")
    """The gender of the voice that reads the voicemail message. Must be either 'man' or 'woman'."""
    inbound_voicemail_prompt_type: str | None | None = Field(default=None, alias="inboundVoicemailPromptType", description="The type of inbound voicemail to use. Must be either 'automated', 'recorded', or 'off'.")
    """The type of inbound voicemail to use. Must be either 'automated', 'recorded', or 'off'."""
    job_role_by_name: str | None | None = Field(default=None, alias="jobRoleByName", description="The name of the job role (e.g. 'SDR').")
    """The name of the job role (e.g. 'SDR')."""
    job_title_extraction_notification_enabled: bool | None | None = Field(default=None, alias="jobTitleExtractionNotificationEnabled", description="Job title extraction notification enabled")
    """Job title extraction notification enabled"""
    kaia_recordings_view_id: int | None | None = Field(default=None, alias="kaiaRecordingsViewId", description="The default smart view to load on the kaia recordings view.")
    """The default smart view to load on the kaia recordings view."""
    keep_bridge_phone_connected: bool | None | None = Field(default=None, alias="keepBridgePhoneConnected", description="Whether to keep the user's bridge phone connected in-between outbound calls.")
    """Whether to keep the user's bridge phone connected in-between outbound calls."""
    language_preference: str | None | None = Field(default=None, alias="languagePreference", description="Language preference")
    """Language preference"""
    last_sign_in_at: str | None | None = Field(default=None, alias="lastSignInAt", description="The date and time the user previously signed in.")
    """The date and time the user previously signed in."""
    link_to_sequence_state_in_task_flow: bool | None | None = Field(default=None, alias="linkToSequenceStateInTaskFlow", description="Link to sequence state in task flow")
    """Link to sequence state in task flow"""
    locked: bool | None | None = Field(default=None, description="A boolean value whether the user is locked out of the application.")
    """A boolean value whether the user is locked out of the application."""
    mailbox_error_email_enabled: bool | None | None = Field(default=None, alias="mailboxErrorEmailEnabled", description="A boolean value whether the user's mailbox error emails are enabled.")
    """A boolean value whether the user's mailbox error emails are enabled."""
    mailings_delivered_count: int | None | None = Field(default=None, alias="mailingsDeliveredCount", description="Mailings delivered count")
    """Mailings delivered count"""
    mailings_replied_count: int | None | None = Field(default=None, alias="mailingsRepliedCount", description="Mailings replied count")
    """Mailings replied count"""
    meeting_engagement_notification_enabled: bool | None | None = Field(default=None, alias="meetingEngagementNotificationEnabled", description="A boolean value whether the user's meeting engagement notifications are enabled.")
    """A boolean value whether the user's meeting engagement notifications are enabled."""
    name: str | None | None = Field(default=None, description="The full name of the user.")
    """The full name of the user."""
    notifications_enabled: bool | None | None = Field(default=None, alias="notificationsEnabled", description="A boolean value whether the user's notifications are enabled.")
    """A boolean value whether the user's notifications are enabled."""
    oce_click_to_dial_everywhere: bool | None | None = Field(default=None, alias="oceClickToDialEverywhere", description="A boolean value indicating if phone calls will launch a call from Outreach (Salesforce, Github, Gmail, LinkedIn, and Twitter).")
    """A boolean value indicating if phone calls will launch a call from Outreach (Salesforce, Github, Gmail, LinkedIn, and Twitter)."""
    oce_gmail_toolbar: bool | None | None = Field(default=None, alias="oceGmailToolbar", description="A boolean value indicating whether the Outreach Gmail toolbar is enabled.")
    """A boolean value indicating whether the Outreach Gmail toolbar is enabled."""
    oce_gmail_tracking_state: str | None | None = Field(default=None, alias="oceGmailTrackingState", description="The user's current email tracking settings when using Outreach Everywhere with GMail.")
    """The user's current email tracking settings when using Outreach Everywhere with GMail."""
    oce_salesforce_email_decorating: bool | None | None = Field(default=None, alias="oceSalesforceEmailDecorating", description="A boolean value indicating if emails are enabled in Outreach Everywhere with Salesforce.")
    """A boolean value indicating if emails are enabled in Outreach Everywhere with Salesforce."""
    oce_salesforce_phone_decorating: bool | None | None = Field(default=None, alias="oceSalesforcePhoneDecorating", description="A boolean value indicating if phone calls are enabled in Outreach Everywhere with Salesforce.")
    """A boolean value indicating if phone calls are enabled in Outreach Everywhere with Salesforce."""
    oce_universal_task_flow: bool | None | None = Field(default=None, alias="oceUniversalTaskFlow", description="A boolean value indicating whether Outreach Everywhere universal task flow is enabled.")
    """A boolean value indicating whether Outreach Everywhere universal task flow is enabled."""
    oce_window_mode: bool | None | None = Field(default=None, alias="oceWindowMode", description="A boolean value indicating whether Outreach Everywhere window mode is enabled.")
    """A boolean value indicating whether Outreach Everywhere window mode is enabled."""
    onboarded_at: str | None | None = Field(default=None, alias="onboardedAt", description="Onboarded at")
    """Onboarded at"""
    opportunities_view_id: int | None | None = Field(default=None, alias="opportunitiesViewId", description="The default smart view to load on the opportunity index view.")
    """The default smart view to load on the opportunity index view."""
    orca_standalone_enabled: bool | None | None = Field(default=None, alias="orcaStandaloneEnabled", description="ORCA standalone enabled")
    """ORCA standalone enabled"""
    password_expires_at: str | None | None = Field(default=None, alias="passwordExpiresAt", description="The date and time the current password expires.")
    """The date and time the current password expires."""
    phone_country_code: str | None | None = Field(default=None, alias="phoneCountryCode", description="The country code of the user's phone.")
    """The country code of the user's phone."""
    phone_number: str | None | None = Field(default=None, alias="phoneNumber", description="The telephone number of the user's phone.")
    """The telephone number of the user's phone."""
    phone_type: str | None | None = Field(default=None, alias="phoneType", description="The user's type of telephone for outbound calls. Must be either 'bridge' or 'voip'.")
    """The user's type of telephone for outbound calls. Must be either 'bridge' or 'voip'."""
    plugin_alert_notification_enabled: bool | None | None = Field(default=None, alias="pluginAlertNotificationEnabled", description="A boolean value whether the user's plugin related error notifications are enabled.")
    """A boolean value whether the user's plugin related error notifications are enabled."""
    preferred_voice_region: str | None | None = Field(default=None, alias="preferredVoiceRegion", description="A string that represents Twilio data center used to connect to Twilio.")
    """A string that represents Twilio data center used to connect to Twilio."""
    prefers_local_presence: bool | None | None = Field(default=None, alias="prefersLocalPresence", description="A boolean value whether the user prefers that a voice call comes from a local phone number.")
    """A boolean value whether the user prefers that a voice call comes from a local phone number."""
    prospect_detail_default: str | None | None = Field(default=None, alias="prospectDetailDefault", description="Prospect detail default")
    """Prospect detail default"""
    prospects_view_id: int | None | None = Field(default=None, alias="prospectsViewId", description="The default smart view to load on the prospect index view.")
    """The default smart view to load on the prospect index view."""
    reports_team_perf_view_id: int | None | None = Field(default=None, alias="reportsTeamPerfViewId", description="The default smart view to load on the team performance reports view.")
    """The default smart view to load on the team performance reports view."""
    reports_view_id: int | None | None = Field(default=None, alias="reportsViewId", description="The default smart view to load on the reports view.")
    """The default smart view to load on the reports view."""
    scim_external_id: str | None | None = Field(default=None, alias="scimExternalId", description="The ID from the SCIM provisioning service used to create the user.")
    """The ID from the SCIM provisioning service used to create the user."""
    scim_source: str | None | None = Field(default=None, alias="scimSource", description="The name of the SCIM provisioning source used to create the user.")
    """The name of the SCIM provisioning source used to create the user."""
    sender_notifications_excluded: bool | None | None = Field(default=None, alias="senderNotificationsExcluded", description="A boolean value whether the user's sender notifications are excluded.")
    """A boolean value whether the user's sender notifications are excluded."""
    tasks_due_count: int | None | None = Field(default=None, alias="tasksDueCount", description="Tasks due count")
    """Tasks due count"""
    tasks_view_id: int | None | None = Field(default=None, alias="tasksViewId", description="The default smart view to load on the tasks index view.")
    """The default smart view to load on the tasks index view."""
    teams_view_id: int | None | None = Field(default=None, alias="teamsViewId", description="The default smart view to load on the teams index view.")
    """The default smart view to load on the teams index view."""
    texting_email_notifications: bool | None | None = Field(default=None, alias="textingEmailNotifications", description="A boolean value whether to send the user email notifications when a text message is missed.")
    """A boolean value whether to send the user email notifications when a text message is missed."""
    title: str | None | None = Field(default=None, description="The user's job title (e.g. 'Staff Accountant').")
    """The user's job title (e.g. 'Staff Accountant')."""
    unknown_reply_email_enabled: bool | None | None = Field(default=None, alias="unknownReplyEmailEnabled", description="A boolean value whether the user's unknown reply emails are enabled.")
    """A boolean value whether the user's unknown reply emails are enabled."""
    use_sales_navigator_for_linked_in_tasks: bool | None | None = Field(default=None, alias="useSalesNavigatorForLinkedInTasks", description="Use sales navigator for linked in tasks")
    """Use sales navigator for linked in tasks"""
    user_guid: str | None | None = Field(default=None, alias="userGuid", description="The globally unique ID (GUID) assigned to the user.")
    """The globally unique ID (GUID) assigned to the user."""
    username: str | None | None = Field(default=None, description="A reader friendly unique identifier of the user.")
    """A reader friendly unique identifier of the user."""
    users_view_id: int | None | None = Field(default=None, alias="usersViewId", description="The default smart view to load on the users index view.")
    """The default smart view to load on the users index view."""
    voicemail_notification_enabled: bool | None | None = Field(default=None, alias="voicemailNotificationEnabled", description="A boolean value whether the user's voicemail notifications are enabled.")
    """A boolean value whether the user's voicemail notifications are enabled."""
    weekly_digest_email_enabled: bool | None | None = Field(default=None, alias="weeklyDigestEmailEnabled", description="A boolean value whether the user's weekly digest email are enabled.")
    """A boolean value whether the user's weekly digest email are enabled."""

class UserLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class User(BaseModel):
    """Outreach user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: UserAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: UserLinks | None = Field(default=None)

class UsersList(BaseModel):
    """UsersList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[User] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class UserResponse(BaseModel):
    """UserResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: User | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class StageLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class StageAttributes(BaseModel):
    """Nested schema for Stage.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    order: int | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    color: str | None | None = Field(default=None, description="The color the stage label will be highlighted in the interface, specified as a hexidecimal value (e.g. '#5951ff').")
    """The color the stage label will be highlighted in the interface, specified as a hexidecimal value (e.g. '#5951ff')."""

class Stage(BaseModel):
    """Outreach stage object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: StageAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: StageLinks | None = Field(default=None)

class StagesList(BaseModel):
    """StagesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Stage] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class StageResponse(BaseModel):
    """StageResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Stage | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class PersonaLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class PersonaAttributes(BaseModel):
    """Nested schema for Persona.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    description: str | None | None = Field(default=None, description="A description of the persona.")
    """A description of the persona."""

class Persona(BaseModel):
    """Outreach persona object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: PersonaAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: PersonaLinks | None = Field(default=None)

class PersonasList(BaseModel):
    """PersonasList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Persona] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class PersonaResponse(BaseModel):
    """PersonaResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Persona | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class TemplateAttributes(BaseModel):
    """Nested schema for Template.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    subject: str | None | None = Field(default=None)
    body_html: str | None | None = Field(default=None, alias="bodyHtml")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    archived: bool | None | None = Field(default=None, description="Boolean value indicating if the template has been archived.")
    """Boolean value indicating if the template has been archived."""
    archived_at: str | None | None = Field(default=None, alias="archivedAt", description="The date and time the template was archived.")
    """The date and time the template was archived."""
    bcc_recipients: list[str] | None | None = Field(default=None, alias="bccRecipients", description="A list of default person and email address pairs to receive this template in the 'bcc' field (e.g. [Billy Bob `<billy.bob@seattle.city>`])")
    """A list of default person and email address pairs to receive this template in the 'bcc' field (e.g. [Billy Bob `<billy.bob@seattle.city>`])"""
    body_text: str | None | None = Field(default=None, alias="bodyText", description="The body text of the template.")
    """The body text of the template."""
    bounce_count: int | None | None = Field(default=None, alias="bounceCount", description="The total count of bounced mailings during this template.")
    """The total count of bounced mailings during this template."""
    cc_recipients: list[str] | None | None = Field(default=None, alias="ccRecipients", description="A list of default person and email address pairs to receive this template in the 'cc' field (e.g. [Billy Bob `<billy.bob@seattle.city>`])")
    """A list of default person and email address pairs to receive this template in the 'cc' field (e.g. [Billy Bob `<billy.bob@seattle.city>`])"""
    click_count: int | None | None = Field(default=None, alias="clickCount", description="The total count of clicked mailings from this template.")
    """The total count of clicked mailings from this template."""
    contains_custom_html: bool | None | None = Field(default=None, alias="containsCustomHtml", description="Contains custom html")
    """Contains custom html"""
    deliver_count: int | None | None = Field(default=None, alias="deliverCount", description="The total count of delivered mailings from this template.")
    """The total count of delivered mailings from this template."""
    failure_count: int | None | None = Field(default=None, alias="failureCount", description="The total count of failed mailings from this template.")
    """The total count of failed mailings from this template."""
    has_ai_content: bool | None | None = Field(default=None, alias="hasAiContent", description="Has AI content")
    """Has AI content"""
    has_ai_subject_line: bool | None | None = Field(default=None, alias="hasAiSubjectLine", description="Has AI subject line")
    """Has AI subject line"""
    last_used_at: str | None | None = Field(default=None, alias="lastUsedAt", description="The last time the template was used.")
    """The last time the template was used."""
    negative_reply_count: int | None | None = Field(default=None, alias="negativeReplyCount", description="The total count of negative reply mailings from this template.")
    """The total count of negative reply mailings from this template."""
    neutral_reply_count: int | None | None = Field(default=None, alias="neutralReplyCount", description="The total count of neutral reply mailings from this template.")
    """The total count of neutral reply mailings from this template."""
    open_count: int | None | None = Field(default=None, alias="openCount", description="The total count of opened mailings from this template.")
    """The total count of opened mailings from this template."""
    opt_out_count: int | None | None = Field(default=None, alias="optOutCount", description="The total count of opted out mailings from this template.")
    """The total count of opted out mailings from this template."""
    personalization_ids: list[Any] | None | None = Field(default=None, alias="personalizationIds", description="Personalization ids")
    """Personalization ids"""
    positive_reply_count: int | None | None = Field(default=None, alias="positiveReplyCount", description="The total count of positive reply mailings from this template.")
    """The total count of positive reply mailings from this template."""
    reply_count: int | None | None = Field(default=None, alias="replyCount", description="The total count of replied mailings from this template.")
    """The total count of replied mailings from this template."""
    schedule_count: int | None | None = Field(default=None, alias="scheduleCount", description="The total count of scheduled mailings from this template.")
    """The total count of scheduled mailings from this template."""
    share_type: str | None | None = Field(default=None, alias="shareType", description="The share type must be one of 'read_only,' 'private,' or 'shared'.")
    """The share type must be one of 'read_only,' 'private,' or 'shared'."""
    tags: list[str] | None | None = Field(default=None, description="A list of tag values associated with the template (e.g. ['Sequencing', 'Quick Response']).")
    """A list of tag values associated with the template (e.g. ['Sequencing', 'Quick Response'])."""
    to_recipients: list[str] | None | None = Field(default=None, alias="toRecipients", description="A list of default person and email address pairs to receive this template in the 'to' field (e.g. ['Billy Bob <billy.bob@seattle.city>'])")
    """A list of default person and email address pairs to receive this template in the 'to' field (e.g. ['Billy Bob <billy.bob@seattle.city>'])"""
    track_links: bool | None | None = Field(default=None, alias="trackLinks", description="Boolean value indicating if link tracking is on for the template.")
    """Boolean value indicating if link tracking is on for the template."""
    track_opens: bool | None | None = Field(default=None, alias="trackOpens", description="Boolean value indicating if open tracking is on for the template.")
    """Boolean value indicating if open tracking is on for the template."""

class TemplateLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class Template(BaseModel):
    """Outreach template object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: TemplateAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: TemplateLinks | None = Field(default=None)

class TemplatesList(BaseModel):
    """TemplatesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Template] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class TemplateResponse(BaseModel):
    """TemplateResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Template | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class SnippetAttributes(BaseModel):
    """Nested schema for Snippet.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    body_html: str | None | None = Field(default=None, alias="bodyHtml")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")
    body_text: str | None | None = Field(default=None, alias="bodyText", description="The text of the snippet.")
    """The text of the snippet."""
    contains_custom_html: bool | None | None = Field(default=None, alias="containsCustomHtml", description="Contains custom html")
    """Contains custom html"""
    share_type: str | None | None = Field(default=None, alias="shareType", description="The permissions for sharing the snippet; must be 'private' or 'shared.'")
    """The permissions for sharing the snippet; must be 'private' or 'shared.'"""
    tags: list[str] | None | None = Field(default=None, description="A list of tags associated with the snippet (e.g. ['Useful', 'Prospecting']).")
    """A list of tags associated with the snippet (e.g. ['Useful', 'Prospecting'])."""

class SnippetLinks(BaseModel):
    """Links associated with this resource"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="URL for this resource")
    """URL for this resource"""

class Snippet(BaseModel):
    """Outreach snippet object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    attributes: SnippetAttributes | None = Field(default=None)
    relationships: dict[str, Any] | None = Field(default=None)
    links: SnippetLinks | None = Field(default=None)

class SnippetsList(BaseModel):
    """SnippetsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Snippet] | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

class SnippetResponse(BaseModel):
    """SnippetResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Snippet | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ProspectsListResultMeta(BaseModel):
    """Metadata for prospects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class SequencesListResultMeta(BaseModel):
    """Metadata for sequences.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class SequenceStatesListResultMeta(BaseModel):
    """Metadata for sequence_states.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class SequenceStepsListResultMeta(BaseModel):
    """Metadata for sequence_steps.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class OpportunitiesListResultMeta(BaseModel):
    """Metadata for opportunities.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class CallsListResultMeta(BaseModel):
    """Metadata for calls.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class CallDispositionsListResultMeta(BaseModel):
    """Metadata for call_dispositions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class CallPurposesListResultMeta(BaseModel):
    """Metadata for call_purposes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class MailingsListResultMeta(BaseModel):
    """Metadata for mailings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class MailboxesListResultMeta(BaseModel):
    """Metadata for mailboxes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class StagesListResultMeta(BaseModel):
    """Metadata for stages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class PersonasListResultMeta(BaseModel):
    """Metadata for personas.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class TemplatesListResultMeta(BaseModel):
    """Metadata for templates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class SnippetsListResultMeta(BaseModel):
    """Metadata for snippets.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class OutreachCheckResult(BaseModel):
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


class OutreachExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class OutreachExecuteResultWithMeta(OutreachExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AccountsSearchData(BaseModel):
    """Search result data for accounts entity."""
    model_config = ConfigDict(extra="allow")

    assigned_teams: list[Any] | None = None
    """Assigned teams"""
    assigned_users: list[Any] | None = None
    """Assigned users"""
    batches: list[Any] | None = None
    """Batches"""
    buyer_intent_score: float | None = None
    """Buyer intent score"""
    company_type: str | None = None
    """Company type"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    custom1: str | None = None
    """Custom field 1"""
    custom10: str | None = None
    """Custom field 10"""
    custom100: str | None = None
    """Custom field 100"""
    custom101: str | None = None
    """Custom field 101"""
    custom102: str | None = None
    """Custom field 102"""
    custom103: str | None = None
    """Custom field 103"""
    custom104: str | None = None
    """Custom field 104"""
    custom105: str | None = None
    """Custom field 105"""
    custom106: str | None = None
    """Custom field 106"""
    custom107: str | None = None
    """Custom field 107"""
    custom108: str | None = None
    """Custom field 108"""
    custom109: str | None = None
    """Custom field 109"""
    custom11: str | None = None
    """Custom field 11"""
    custom110: str | None = None
    """Custom field 110"""
    custom111: str | None = None
    """Custom field 111"""
    custom112: str | None = None
    """Custom field 112"""
    custom113: str | None = None
    """Custom field 113"""
    custom114: str | None = None
    """Custom field 114"""
    custom115: str | None = None
    """Custom field 115"""
    custom116: str | None = None
    """Custom field 116"""
    custom117: str | None = None
    """Custom field 117"""
    custom118: str | None = None
    """Custom field 118"""
    custom119: str | None = None
    """Custom field 119"""
    custom12: str | None = None
    """Custom field 12"""
    custom120: str | None = None
    """Custom field 120"""
    custom121: str | None = None
    """Custom field 121"""
    custom122: str | None = None
    """Custom field 122"""
    custom123: str | None = None
    """Custom field 123"""
    custom124: str | None = None
    """Custom field 124"""
    custom125: str | None = None
    """Custom field 125"""
    custom126: str | None = None
    """Custom field 126"""
    custom127: str | None = None
    """Custom field 127"""
    custom128: str | None = None
    """Custom field 128"""
    custom129: str | None = None
    """Custom field 129"""
    custom13: str | None = None
    """Custom field 13"""
    custom130: str | None = None
    """Custom field 130"""
    custom131: str | None = None
    """Custom field 131"""
    custom132: str | None = None
    """Custom field 132"""
    custom133: str | None = None
    """Custom field 133"""
    custom134: str | None = None
    """Custom field 134"""
    custom135: str | None = None
    """Custom field 135"""
    custom136: str | None = None
    """Custom field 136"""
    custom137: str | None = None
    """Custom field 137"""
    custom138: str | None = None
    """Custom field 138"""
    custom139: str | None = None
    """Custom field 139"""
    custom14: str | None = None
    """Custom field 14"""
    custom140: str | None = None
    """Custom field 140"""
    custom141: str | None = None
    """Custom field 141"""
    custom142: str | None = None
    """Custom field 142"""
    custom143: str | None = None
    """Custom field 143"""
    custom144: str | None = None
    """Custom field 144"""
    custom145: str | None = None
    """Custom field 145"""
    custom146: str | None = None
    """Custom field 146"""
    custom147: str | None = None
    """Custom field 147"""
    custom148: str | None = None
    """Custom field 148"""
    custom149: str | None = None
    """Custom field 149"""
    custom15: str | None = None
    """Custom field 15"""
    custom150: str | None = None
    """Custom field 150"""
    custom16: str | None = None
    """Custom field 16"""
    custom17: str | None = None
    """Custom field 17"""
    custom18: str | None = None
    """Custom field 18"""
    custom19: str | None = None
    """Custom field 19"""
    custom2: str | None = None
    """Custom field 2"""
    custom20: str | None = None
    """Custom field 20"""
    custom21: str | None = None
    """Custom field 21"""
    custom22: str | None = None
    """Custom field 22"""
    custom23: str | None = None
    """Custom field 23"""
    custom24: str | None = None
    """Custom field 24"""
    custom25: str | None = None
    """Custom field 25"""
    custom26: str | None = None
    """Custom field 26"""
    custom27: str | None = None
    """Custom field 27"""
    custom28: str | None = None
    """Custom field 28"""
    custom29: str | None = None
    """Custom field 29"""
    custom3: str | None = None
    """Custom field 3"""
    custom30: str | None = None
    """Custom field 30"""
    custom31: str | None = None
    """Custom field 31"""
    custom32: str | None = None
    """Custom field 32"""
    custom33: str | None = None
    """Custom field 33"""
    custom34: str | None = None
    """Custom field 34"""
    custom35: str | None = None
    """Custom field 35"""
    custom36: str | None = None
    """Custom field 36"""
    custom37: str | None = None
    """Custom field 37"""
    custom38: str | None = None
    """Custom field 38"""
    custom39: str | None = None
    """Custom field 39"""
    custom4: str | None = None
    """Custom field 4"""
    custom40: str | None = None
    """Custom field 40"""
    custom41: str | None = None
    """Custom field 41"""
    custom42: str | None = None
    """Custom field 42"""
    custom43: str | None = None
    """Custom field 43"""
    custom44: str | None = None
    """Custom field 44"""
    custom45: str | None = None
    """Custom field 45"""
    custom46: str | None = None
    """Custom field 46"""
    custom47: str | None = None
    """Custom field 47"""
    custom48: str | None = None
    """Custom field 48"""
    custom49: str | None = None
    """Custom field 49"""
    custom5: str | None = None
    """Custom field 5"""
    custom50: str | None = None
    """Custom field 50"""
    custom51: str | None = None
    """Custom field 51"""
    custom52: str | None = None
    """Custom field 52"""
    custom53: str | None = None
    """Custom field 53"""
    custom54: str | None = None
    """Custom field 54"""
    custom55: str | None = None
    """Custom field 55"""
    custom56: str | None = None
    """Custom field 56"""
    custom57: str | None = None
    """Custom field 57"""
    custom58: str | None = None
    """Custom field 58"""
    custom59: str | None = None
    """Custom field 59"""
    custom6: str | None = None
    """Custom field 6"""
    custom60: str | None = None
    """Custom field 60"""
    custom61: str | None = None
    """Custom field 61"""
    custom62: str | None = None
    """Custom field 62"""
    custom63: str | None = None
    """Custom field 63"""
    custom64: str | None = None
    """Custom field 64"""
    custom65: str | None = None
    """Custom field 65"""
    custom66: str | None = None
    """Custom field 66"""
    custom67: str | None = None
    """Custom field 67"""
    custom68: str | None = None
    """Custom field 68"""
    custom69: str | None = None
    """Custom field 69"""
    custom7: str | None = None
    """Custom field 7"""
    custom70: str | None = None
    """Custom field 70"""
    custom71: str | None = None
    """Custom field 71"""
    custom72: str | None = None
    """Custom field 72"""
    custom73: str | None = None
    """Custom field 73"""
    custom74: str | None = None
    """Custom field 74"""
    custom75: str | None = None
    """Custom field 75"""
    custom76: str | None = None
    """Custom field 76"""
    custom77: str | None = None
    """Custom field 77"""
    custom78: str | None = None
    """Custom field 78"""
    custom79: str | None = None
    """Custom field 79"""
    custom8: str | None = None
    """Custom field 8"""
    custom80: str | None = None
    """Custom field 80"""
    custom81: str | None = None
    """Custom field 81"""
    custom82: str | None = None
    """Custom field 82"""
    custom83: str | None = None
    """Custom field 83"""
    custom84: str | None = None
    """Custom field 84"""
    custom85: str | None = None
    """Custom field 85"""
    custom86: str | None = None
    """Custom field 86"""
    custom87: str | None = None
    """Custom field 87"""
    custom88: str | None = None
    """Custom field 88"""
    custom89: str | None = None
    """Custom field 89"""
    custom9: str | None = None
    """Custom field 9"""
    custom90: str | None = None
    """Custom field 90"""
    custom91: str | None = None
    """Custom field 91"""
    custom92: str | None = None
    """Custom field 92"""
    custom93: str | None = None
    """Custom field 93"""
    custom94: str | None = None
    """Custom field 94"""
    custom95: str | None = None
    """Custom field 95"""
    custom96: str | None = None
    """Custom field 96"""
    custom97: str | None = None
    """Custom field 97"""
    custom98: str | None = None
    """Custom field 98"""
    custom99: str | None = None
    """Custom field 99"""
    custom_id: str | None = None
    """Custom id"""
    default_plugin_mapping: list[Any] | None = None
    """Default plugin mapping"""
    description: str | None = None
    """Description"""
    domain: str | None = None
    """Domain"""
    external_source: str | None = None
    """External source"""
    favorites: list[Any] | None = None
    """Favorites"""
    followers: int | None = None
    """Followers"""
    founded_at: str | None = None
    """Founded at"""
    id: int | None = None
    """Unique account identifier"""
    industry: str | None = None
    """Industry"""
    linked_in_employees: int | None = None
    """Linked in employees"""
    linked_in_url: str | None = None
    """Linked in url"""
    locality: str | None = None
    """Locality"""
    name: str | None = None
    """Name"""
    named: bool | None = None
    """Named"""
    natural_name: str | None = None
    """Natural name"""
    number_of_employees: int | None = None
    """Number of employees"""
    owner: list[Any] | None = None
    """Owner"""
    prospects: list[Any] | None = None
    """Prospects"""
    sharing_team_id: str | None = None
    """Sharing team id"""
    tags: list[Any] | None = None
    """Tags"""
    tasks: list[Any] | None = None
    """Tasks"""
    touched_at: str | None = None
    """Touched at"""
    trashed_at: str | None = None
    """Trashed at"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""
    website_url: str | None = None
    """Website url"""


class CallsSearchData(BaseModel):
    """Search result data for calls entity."""
    model_config = ConfigDict(extra="allow")

    answered_at: str | None = None
    """Answered at"""
    batches: list[Any] | None = None
    """Batches"""
    call_disposition: list[Any] | None = None
    """Call disposition"""
    call_purpose: list[Any] | None = None
    """Call purpose"""
    completed_at: str | None = None
    """Completed at"""
    created_at: str | None = None
    """Created at"""
    dialed_at: str | None = None
    """Dialed at"""
    direction: str | None = None
    """Direction"""
    external_vendor: str | None = None
    """External vendor"""
    from_: str | None = None
    """From"""
    id: int | None = None
    """Unique call identifier"""
    note: str | None = None
    """Note"""
    opportunity: list[Any] | None = None
    """Opportunity"""
    outbound_voicemail: list[Any] | None = None
    """Outbound voicemail"""
    outcome: str | None = None
    """Outcome"""
    phone: list[Any] | None = None
    """Phone"""
    phone_number: list[Any] | None = None
    """Phone number"""
    prospect: list[Any] | None = None
    """Prospect"""
    recording_deletion_reason: str | None = None
    """Recording deletion reason"""
    recording_url: str | None = None
    """Recording url"""
    returned_at: str | None = None
    """Returned at"""
    sequence: list[Any] | None = None
    """Sequence"""
    sequence_action: str | None = None
    """Sequence action"""
    sequence_state: list[Any] | None = None
    """Sequence state"""
    sequence_step: list[Any] | None = None
    """Sequence step"""
    should_record_call: bool | None = None
    """Should record call"""
    state: str | None = None
    """State"""
    state_changed_at: str | None = None
    """State changed at"""
    tags: list[Any] | None = None
    """Tags"""
    task: list[Any] | None = None
    """Task"""
    to: str | None = None
    """To"""
    uid: str | None = None
    """Uid"""
    updated_at: str | None = None
    """Updated at"""
    user: list[Any] | None = None
    """User"""
    user_call_type: str | None = None
    """User call type"""
    vendor_call_id: str | None = None
    """Vendor call id"""
    voicemail_recording_url: str | None = None
    """Voicemail recording url"""


class CallDispositionsSearchData(BaseModel):
    """Search result data for call_dispositions entity."""
    model_config = ConfigDict(extra="allow")

    calls: list[Any] | None = None
    """Calls"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    default_for_outbound_voicemail: bool | None = None
    """Default for outbound voicemail"""
    id: int | None = None
    """Unique call disposition identifier"""
    name: str | None = None
    """Name"""
    order: int | None = None
    """Order"""
    outcome: str | None = None
    """Outcome"""
    updated_at: str | None = None
    """Updated at"""


class CallPurposesSearchData(BaseModel):
    """Search result data for call_purposes entity."""
    model_config = ConfigDict(extra="allow")

    calls: list[Any] | None = None
    """Calls"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    id: int | None = None
    """Unique call purpose identifier"""
    name: str | None = None
    """Name"""
    order: int | None = None
    """Order"""
    updated_at: str | None = None
    """Updated at"""


class MailingsSearchData(BaseModel):
    """Search result data for mailings entity."""
    model_config = ConfigDict(extra="allow")

    attachments: list[Any] | None = None
    """Attachments"""
    attributable_sequence_id: int | None = None
    """Attributable sequence id"""
    attributable_sequence_name: str | None = None
    """Attributable sequence name"""
    body_html: str | None = None
    """Body html"""
    body_text: str | None = None
    """Body text"""
    bounced_at: str | None = None
    """Bounced at"""
    calendar: list[Any] | None = None
    """Calendar"""
    click_count: int | None = None
    """Click count"""
    clicked_at: str | None = None
    """Clicked at"""
    created_at: str | None = None
    """Created at"""
    delivered_at: str | None = None
    """Delivered at"""
    desired_at: str | None = None
    """Desired at"""
    error_backtrace: str | None = None
    """Error backtrace"""
    error_reason: str | None = None
    """Error reason"""
    follow_up_sequence: list[Any] | None = None
    """Follow up sequence"""
    follow_up_sequence_id: int | None = None
    """Follow up sequence id"""
    follow_up_sequence_name: str | None = None
    """Follow up sequence name"""
    follow_up_sequence_starting_date: str | None = None
    """Follow up sequence starting date"""
    follow_up_task_scheduled_at: str | None = None
    """Follow up task scheduled at"""
    follow_up_task_type: str | None = None
    """Follow up task type"""
    id: int | None = None
    """Unique mailing identifier"""
    mailbox: list[Any] | None = None
    """Mailbox"""
    mailbox_address: str | None = None
    """Mailbox address"""
    mailing_type: str | None = None
    """Mailing type"""
    marked_as_spam_at: str | None = None
    """Marked as spam at"""
    meeting_description: str | None = None
    """Meeting description"""
    meeting_duration: int | None = None
    """Meeting duration"""
    meeting_location: str | None = None
    """Meeting location"""
    meeting_title: str | None = None
    """Meeting title"""
    message_id: str | None = None
    """Message id"""
    notify_thread_condition: str | None = None
    """Notify thread condition"""
    notify_thread_scheduled_at: str | None = None
    """Notify thread scheduled at"""
    notify_thread_status: str | None = None
    """Notify thread status"""
    open_count: int | None = None
    """Open count"""
    opened_at: str | None = None
    """Opened at"""
    opportunity: list[Any] | None = None
    """Opportunity"""
    optimized_scheduled_at: str | None = None
    """Optimized scheduled at"""
    override_safety_settings: bool | None = None
    """Override safety settings"""
    prospect: list[Any] | None = None
    """Prospect"""
    recipients: list[Any] | None = None
    """Recipients"""
    references: list[Any] | None = None
    """References"""
    replied_at: str | None = None
    """Replied at"""
    reply_sentiment: str | None = None
    """Reply sentiment"""
    retry_at: str | None = None
    """Retry at"""
    retry_count: int | None = None
    """Retry count"""
    retry_interval: int | None = None
    """Retry interval"""
    schedule: list[Any] | None = None
    """Schedule"""
    schedule_id: int | None = None
    """Schedule id"""
    scheduled_at: str | None = None
    """Scheduled at"""
    sequence: list[Any] | None = None
    """Sequence"""
    sequence_state: list[Any] | None = None
    """Sequence state"""
    sequence_step: list[Any] | None = None
    """Sequence step"""
    state: str | None = None
    """State"""
    state_changed_at: str | None = None
    """State changed at"""
    subject: str | None = None
    """Subject"""
    task: list[Any] | None = None
    """Task"""
    tasks: list[Any] | None = None
    """Tasks"""
    template: list[Any] | None = None
    """Template"""
    track_links: bool | None = None
    """Track links"""
    track_opens: bool | None = None
    """Track opens"""
    unsubscribed_at: str | None = None
    """Unsubscribed at"""
    updated_at: str | None = None
    """Updated at"""
    user: list[Any] | None = None
    """User"""


class MailboxesSearchData(BaseModel):
    """Search result data for mailboxes entity."""
    model_config = ConfigDict(extra="allow")

    auth_id: int | None = None
    """Auth id"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    editable: bool | None = None
    """Editable"""
    email: str | None = None
    """Email"""
    email_hash: str | None = None
    """Email hash"""
    email_provider: str | None = None
    """Email provider"""
    email_signature: str | None = None
    """Email signature"""
    ews_custom_search_folder: bool | None = None
    """Ews custom search folder"""
    ews_delegate_sync: bool | None = None
    """Ews delegate sync"""
    ews_endpoint: str | None = None
    """Ews endpoint"""
    ews_impersonation: bool | None = None
    """Ews impersonation"""
    ews_ssl_verify_mode: int | None = None
    """Ews ssl verify mode"""
    exchange_version: str | None = None
    """Exchange version"""
    id: int | None = None
    """Unique mailbox identifier"""
    imap_host: str | None = None
    """Imap host"""
    imap_port: int | None = None
    """Imap port"""
    imap_ssl: bool | None = None
    """Imap ssl"""
    mail_aliases: list[Any] | None = None
    """Mail aliases"""
    mailings: list[Any] | None = None
    """Mailings"""
    max_emails_per_day: int | None = None
    """Max emails per day"""
    max_mailings_per_day: int | None = None
    """Max mailings per day"""
    max_mailings_per_week: int | None = None
    """Max mailings per week"""
    opt_out_message: str | None = None
    """Opt out message"""
    opt_out_signature: str | None = None
    """Opt out signature"""
    prospect_email_exclusions: list[Any] | None = None
    """Prospect email exclusions"""
    provider_id: int | None = None
    """Provider id"""
    provider_type: str | None = None
    """Provider type"""
    send_disabled: bool | None = None
    """Send disabled"""
    send_errored_at: str | None = None
    """Send errored at"""
    send_max_retries: int | None = None
    """Send max retries"""
    send_method: str | None = None
    """Send method"""
    send_period: int | None = None
    """Send period"""
    send_permanent_error_at: str | None = None
    """Send permanent error at"""
    send_requires_sync: bool | None = None
    """Send requires sync"""
    send_success_at: str | None = None
    """Send success at"""
    send_threshold: int | None = None
    """Send threshold"""
    sendgrid_webhook_url: str | None = None
    """Sendgrid webhook url"""
    smtp_host: str | None = None
    """Smtp host"""
    smtp_port: int | None = None
    """Smtp port"""
    smtp_ssl: bool | None = None
    """Smtp ssl"""
    smtp_username: str | None = None
    """Smtp username"""
    sync_active_frequency: int | None = None
    """Sync active frequency"""
    sync_disabled: bool | None = None
    """Sync disabled"""
    sync_errored_at: str | None = None
    """Sync errored at"""
    sync_finished_at: str | None = None
    """Sync finished at"""
    sync_method: str | None = None
    """Sync method"""
    sync_outreach_folder: bool | None = None
    """Sync outreach folder"""
    sync_passive_frequency: int | None = None
    """Sync passive frequency"""
    sync_permanent_error_at: str | None = None
    """Sync permanent error at"""
    sync_success_at: str | None = None
    """Sync success at"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""
    user: list[Any] | None = None
    """User"""
    user_id: int | None = None
    """User id"""
    username: str | None = None
    """Username"""


class OpportunitiesSearchData(BaseModel):
    """Search result data for opportunities entity."""
    model_config = ConfigDict(extra="allow")

    account: list[Any] | None = None
    """Account"""
    amount: int | None = None
    """Amount"""
    assigned_teams: list[Any] | None = None
    """Assigned teams"""
    assigned_users: list[Any] | None = None
    """Assigned users"""
    close_date: str | None = None
    """Close date"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    currency_type: str | None = None
    """Currency type"""
    custom1: str | None = None
    """Custom field 1"""
    custom10: str | None = None
    """Custom field 10"""
    custom100: str | None = None
    """Custom field 100"""
    custom101: str | None = None
    """Custom field 101"""
    custom102: str | None = None
    """Custom field 102"""
    custom103: str | None = None
    """Custom field 103"""
    custom104: str | None = None
    """Custom field 104"""
    custom105: str | None = None
    """Custom field 105"""
    custom106: str | None = None
    """Custom field 106"""
    custom107: str | None = None
    """Custom field 107"""
    custom108: str | None = None
    """Custom field 108"""
    custom109: str | None = None
    """Custom field 109"""
    custom11: str | None = None
    """Custom field 11"""
    custom110: str | None = None
    """Custom field 110"""
    custom111: str | None = None
    """Custom field 111"""
    custom112: str | None = None
    """Custom field 112"""
    custom113: str | None = None
    """Custom field 113"""
    custom114: str | None = None
    """Custom field 114"""
    custom115: str | None = None
    """Custom field 115"""
    custom116: str | None = None
    """Custom field 116"""
    custom117: str | None = None
    """Custom field 117"""
    custom118: str | None = None
    """Custom field 118"""
    custom119: str | None = None
    """Custom field 119"""
    custom12: str | None = None
    """Custom field 12"""
    custom120: str | None = None
    """Custom field 120"""
    custom121: str | None = None
    """Custom field 121"""
    custom122: str | None = None
    """Custom field 122"""
    custom123: str | None = None
    """Custom field 123"""
    custom124: str | None = None
    """Custom field 124"""
    custom125: str | None = None
    """Custom field 125"""
    custom126: str | None = None
    """Custom field 126"""
    custom127: str | None = None
    """Custom field 127"""
    custom128: str | None = None
    """Custom field 128"""
    custom129: str | None = None
    """Custom field 129"""
    custom13: str | None = None
    """Custom field 13"""
    custom130: str | None = None
    """Custom field 130"""
    custom131: str | None = None
    """Custom field 131"""
    custom132: str | None = None
    """Custom field 132"""
    custom133: str | None = None
    """Custom field 133"""
    custom134: str | None = None
    """Custom field 134"""
    custom135: str | None = None
    """Custom field 135"""
    custom136: str | None = None
    """Custom field 136"""
    custom137: str | None = None
    """Custom field 137"""
    custom138: str | None = None
    """Custom field 138"""
    custom139: str | None = None
    """Custom field 139"""
    custom14: str | None = None
    """Custom field 14"""
    custom140: str | None = None
    """Custom field 140"""
    custom141: str | None = None
    """Custom field 141"""
    custom142: str | None = None
    """Custom field 142"""
    custom143: str | None = None
    """Custom field 143"""
    custom144: str | None = None
    """Custom field 144"""
    custom145: str | None = None
    """Custom field 145"""
    custom146: str | None = None
    """Custom field 146"""
    custom147: str | None = None
    """Custom field 147"""
    custom148: str | None = None
    """Custom field 148"""
    custom149: str | None = None
    """Custom field 149"""
    custom15: str | None = None
    """Custom field 15"""
    custom150: str | None = None
    """Custom field 150"""
    custom16: str | None = None
    """Custom field 16"""
    custom17: str | None = None
    """Custom field 17"""
    custom18: str | None = None
    """Custom field 18"""
    custom19: str | None = None
    """Custom field 19"""
    custom2: str | None = None
    """Custom field 2"""
    custom20: str | None = None
    """Custom field 20"""
    custom21: str | None = None
    """Custom field 21"""
    custom22: str | None = None
    """Custom field 22"""
    custom23: str | None = None
    """Custom field 23"""
    custom24: str | None = None
    """Custom field 24"""
    custom25: str | None = None
    """Custom field 25"""
    custom26: str | None = None
    """Custom field 26"""
    custom27: str | None = None
    """Custom field 27"""
    custom28: str | None = None
    """Custom field 28"""
    custom29: str | None = None
    """Custom field 29"""
    custom3: str | None = None
    """Custom field 3"""
    custom30: str | None = None
    """Custom field 30"""
    custom31: str | None = None
    """Custom field 31"""
    custom32: str | None = None
    """Custom field 32"""
    custom33: str | None = None
    """Custom field 33"""
    custom34: str | None = None
    """Custom field 34"""
    custom35: str | None = None
    """Custom field 35"""
    custom36: str | None = None
    """Custom field 36"""
    custom37: str | None = None
    """Custom field 37"""
    custom38: str | None = None
    """Custom field 38"""
    custom39: str | None = None
    """Custom field 39"""
    custom4: str | None = None
    """Custom field 4"""
    custom40: str | None = None
    """Custom field 40"""
    custom41: str | None = None
    """Custom field 41"""
    custom42: str | None = None
    """Custom field 42"""
    custom43: str | None = None
    """Custom field 43"""
    custom44: str | None = None
    """Custom field 44"""
    custom45: str | None = None
    """Custom field 45"""
    custom46: str | None = None
    """Custom field 46"""
    custom47: str | None = None
    """Custom field 47"""
    custom48: str | None = None
    """Custom field 48"""
    custom49: str | None = None
    """Custom field 49"""
    custom5: str | None = None
    """Custom field 5"""
    custom50: str | None = None
    """Custom field 50"""
    custom51: str | None = None
    """Custom field 51"""
    custom52: str | None = None
    """Custom field 52"""
    custom53: str | None = None
    """Custom field 53"""
    custom54: str | None = None
    """Custom field 54"""
    custom55: str | None = None
    """Custom field 55"""
    custom56: str | None = None
    """Custom field 56"""
    custom57: str | None = None
    """Custom field 57"""
    custom58: str | None = None
    """Custom field 58"""
    custom59: str | None = None
    """Custom field 59"""
    custom6: str | None = None
    """Custom field 6"""
    custom60: str | None = None
    """Custom field 60"""
    custom61: str | None = None
    """Custom field 61"""
    custom62: str | None = None
    """Custom field 62"""
    custom63: str | None = None
    """Custom field 63"""
    custom64: str | None = None
    """Custom field 64"""
    custom65: str | None = None
    """Custom field 65"""
    custom66: str | None = None
    """Custom field 66"""
    custom67: str | None = None
    """Custom field 67"""
    custom68: str | None = None
    """Custom field 68"""
    custom69: str | None = None
    """Custom field 69"""
    custom7: str | None = None
    """Custom field 7"""
    custom70: str | None = None
    """Custom field 70"""
    custom71: str | None = None
    """Custom field 71"""
    custom72: str | None = None
    """Custom field 72"""
    custom73: str | None = None
    """Custom field 73"""
    custom74: str | None = None
    """Custom field 74"""
    custom75: str | None = None
    """Custom field 75"""
    custom76: str | None = None
    """Custom field 76"""
    custom77: str | None = None
    """Custom field 77"""
    custom78: str | None = None
    """Custom field 78"""
    custom79: str | None = None
    """Custom field 79"""
    custom8: str | None = None
    """Custom field 8"""
    custom80: str | None = None
    """Custom field 80"""
    custom81: str | None = None
    """Custom field 81"""
    custom82: str | None = None
    """Custom field 82"""
    custom83: str | None = None
    """Custom field 83"""
    custom84: str | None = None
    """Custom field 84"""
    custom85: str | None = None
    """Custom field 85"""
    custom86: str | None = None
    """Custom field 86"""
    custom87: str | None = None
    """Custom field 87"""
    custom88: str | None = None
    """Custom field 88"""
    custom89: str | None = None
    """Custom field 89"""
    custom9: str | None = None
    """Custom field 9"""
    custom90: str | None = None
    """Custom field 90"""
    custom91: str | None = None
    """Custom field 91"""
    custom92: str | None = None
    """Custom field 92"""
    custom93: str | None = None
    """Custom field 93"""
    custom94: str | None = None
    """Custom field 94"""
    custom95: str | None = None
    """Custom field 95"""
    custom96: str | None = None
    """Custom field 96"""
    custom97: str | None = None
    """Custom field 97"""
    custom98: str | None = None
    """Custom field 98"""
    custom99: str | None = None
    """Custom field 99"""
    default_plugin_mapping: list[Any] | None = None
    """Default plugin mapping"""
    description: str | None = None
    """Description"""
    external_created_at: str | None = None
    """External created at"""
    external_creator: list[Any] | None = None
    """External creator"""
    favorites: list[Any] | None = None
    """Favorites"""
    health_category: str | None = None
    """Health category"""
    health_score: int | None = None
    """Health score"""
    id: int | None = None
    """Unique opportunity identifier"""
    map_link: str | None = None
    """Map link"""
    map_next_steps: str | None = None
    """Map next steps"""
    map_number_of_overdue_tasks: int | None = None
    """Map number of overdue tasks"""
    map_status: str | None = None
    """Map status"""
    name: str | None = None
    """Name"""
    next_step: str | None = None
    """Next step"""
    opportunity_health_factors: list[Any] | None = None
    """Opportunity health factors"""
    opportunity_stage: list[Any] | None = None
    """Opportunity stage"""
    opportunity_type: str | None = None
    """Opportunity type"""
    owner: list[Any] | None = None
    """Owner"""
    primary_prospect: list[Any] | None = None
    """Primary prospect"""
    probability: int | None = None
    """Probability"""
    prospecting_rep_id: str | None = None
    """Prospecting rep id"""
    prospects: list[Any] | None = None
    """Prospects"""
    sharing_team_id: str | None = None
    """Sharing team id"""
    stage: list[Any] | None = None
    """Stage"""
    tags: list[Any] | None = None
    """Tags"""
    touched_at: str | None = None
    """Touched at"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""


class PersonasSearchData(BaseModel):
    """Search result data for personas entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """Created at"""
    description: str | None = None
    """Description"""
    id: int | None = None
    """Unique persona identifier"""
    name: str | None = None
    """Name"""
    prospects: list[Any] | None = None
    """Prospects"""
    updated_at: str | None = None
    """Updated at"""


class ProspectsSearchData(BaseModel):
    """Search result data for prospects entity."""
    model_config = ConfigDict(extra="allow")

    account: list[Any] | None = None
    """Account"""
    account_name: str | None = None
    """Account name"""
    active_sequence_states: list[Any] | None = None
    """Active sequence states"""
    added_at: str | None = None
    """Added at"""
    address_city: str | None = None
    """Address city"""
    address_country: str | None = None
    """Address country"""
    address_state: str | None = None
    """Address state"""
    address_street: str | None = None
    """Address street"""
    address_street2: str | None = None
    """Address street2"""
    address_zip: str | None = None
    """Address zip"""
    angel_list_url: str | None = None
    """Angel list url"""
    assigned_teams: list[Any] | None = None
    """Assigned teams"""
    assigned_users: list[Any] | None = None
    """Assigned users"""
    available_at: str | None = None
    """Available at"""
    batches: list[Any] | None = None
    """Batches"""
    call_opted_out: bool | None = None
    """Call opted out"""
    calls: list[Any] | None = None
    """Calls"""
    calls_opt_status: str | None = None
    """Calls opt status"""
    calls_opted_at: str | None = None
    """Calls opted at"""
    campaign_name: str | None = None
    """Campaign name"""
    click_count: int | None = None
    """Click count"""
    company: str | None = None
    """Company"""
    company_followers: int | None = None
    """Company followers"""
    company_founded_at: str | None = None
    """Company founded at"""
    company_industry: str | None = None
    """Company industry"""
    company_linked_in: str | None = None
    """Company linked in"""
    company_linked_in_employees: str | None = None
    """Company linked in employees"""
    company_locality: str | None = None
    """Company locality"""
    company_natural: str | None = None
    """Company natural"""
    company_size: int | None = None
    """Company size"""
    company_start_date: str | None = None
    """Company start date"""
    company_type: str | None = None
    """Company type"""
    contact_histogram: list[Any] | None = None
    """Contact histogram"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    custom1: str | None = None
    """Custom field 1"""
    custom10: str | None = None
    """Custom field 10"""
    custom100: str | None = None
    """Custom field 100"""
    custom101: str | None = None
    """Custom field 101"""
    custom102: str | None = None
    """Custom field 102"""
    custom103: str | None = None
    """Custom field 103"""
    custom104: str | None = None
    """Custom field 104"""
    custom105: str | None = None
    """Custom field 105"""
    custom106: str | None = None
    """Custom field 106"""
    custom107: str | None = None
    """Custom field 107"""
    custom108: str | None = None
    """Custom field 108"""
    custom109: str | None = None
    """Custom field 109"""
    custom11: str | None = None
    """Custom field 11"""
    custom110: str | None = None
    """Custom field 110"""
    custom111: str | None = None
    """Custom field 111"""
    custom112: str | None = None
    """Custom field 112"""
    custom113: str | None = None
    """Custom field 113"""
    custom114: str | None = None
    """Custom field 114"""
    custom115: str | None = None
    """Custom field 115"""
    custom116: str | None = None
    """Custom field 116"""
    custom117: str | None = None
    """Custom field 117"""
    custom118: str | None = None
    """Custom field 118"""
    custom119: str | None = None
    """Custom field 119"""
    custom12: str | None = None
    """Custom field 12"""
    custom120: str | None = None
    """Custom field 120"""
    custom121: str | None = None
    """Custom field 121"""
    custom122: str | None = None
    """Custom field 122"""
    custom123: str | None = None
    """Custom field 123"""
    custom124: str | None = None
    """Custom field 124"""
    custom125: str | None = None
    """Custom field 125"""
    custom126: str | None = None
    """Custom field 126"""
    custom127: str | None = None
    """Custom field 127"""
    custom128: str | None = None
    """Custom field 128"""
    custom129: str | None = None
    """Custom field 129"""
    custom13: str | None = None
    """Custom field 13"""
    custom130: str | None = None
    """Custom field 130"""
    custom131: str | None = None
    """Custom field 131"""
    custom132: str | None = None
    """Custom field 132"""
    custom133: str | None = None
    """Custom field 133"""
    custom134: str | None = None
    """Custom field 134"""
    custom135: str | None = None
    """Custom field 135"""
    custom136: str | None = None
    """Custom field 136"""
    custom137: str | None = None
    """Custom field 137"""
    custom138: str | None = None
    """Custom field 138"""
    custom139: str | None = None
    """Custom field 139"""
    custom14: str | None = None
    """Custom field 14"""
    custom140: str | None = None
    """Custom field 140"""
    custom141: str | None = None
    """Custom field 141"""
    custom142: str | None = None
    """Custom field 142"""
    custom143: str | None = None
    """Custom field 143"""
    custom144: str | None = None
    """Custom field 144"""
    custom145: str | None = None
    """Custom field 145"""
    custom146: str | None = None
    """Custom field 146"""
    custom147: str | None = None
    """Custom field 147"""
    custom148: str | None = None
    """Custom field 148"""
    custom149: str | None = None
    """Custom field 149"""
    custom15: str | None = None
    """Custom field 15"""
    custom150: str | None = None
    """Custom field 150"""
    custom16: str | None = None
    """Custom field 16"""
    custom17: str | None = None
    """Custom field 17"""
    custom18: str | None = None
    """Custom field 18"""
    custom19: str | None = None
    """Custom field 19"""
    custom2: str | None = None
    """Custom field 2"""
    custom20: str | None = None
    """Custom field 20"""
    custom21: str | None = None
    """Custom field 21"""
    custom22: str | None = None
    """Custom field 22"""
    custom23: str | None = None
    """Custom field 23"""
    custom24: str | None = None
    """Custom field 24"""
    custom25: str | None = None
    """Custom field 25"""
    custom26: str | None = None
    """Custom field 26"""
    custom27: str | None = None
    """Custom field 27"""
    custom28: str | None = None
    """Custom field 28"""
    custom29: str | None = None
    """Custom field 29"""
    custom3: str | None = None
    """Custom field 3"""
    custom30: str | None = None
    """Custom field 30"""
    custom31: str | None = None
    """Custom field 31"""
    custom32: str | None = None
    """Custom field 32"""
    custom33: str | None = None
    """Custom field 33"""
    custom34: str | None = None
    """Custom field 34"""
    custom35: str | None = None
    """Custom field 35"""
    custom36: str | None = None
    """Custom field 36"""
    custom37: str | None = None
    """Custom field 37"""
    custom38: str | None = None
    """Custom field 38"""
    custom39: str | None = None
    """Custom field 39"""
    custom4: str | None = None
    """Custom field 4"""
    custom40: str | None = None
    """Custom field 40"""
    custom41: str | None = None
    """Custom field 41"""
    custom42: str | None = None
    """Custom field 42"""
    custom43: str | None = None
    """Custom field 43"""
    custom44: str | None = None
    """Custom field 44"""
    custom45: str | None = None
    """Custom field 45"""
    custom46: str | None = None
    """Custom field 46"""
    custom47: str | None = None
    """Custom field 47"""
    custom48: str | None = None
    """Custom field 48"""
    custom49: str | None = None
    """Custom field 49"""
    custom5: str | None = None
    """Custom field 5"""
    custom50: str | None = None
    """Custom field 50"""
    custom51: str | None = None
    """Custom field 51"""
    custom52: str | None = None
    """Custom field 52"""
    custom53: str | None = None
    """Custom field 53"""
    custom54: str | None = None
    """Custom field 54"""
    custom55: str | None = None
    """Custom field 55"""
    custom56: str | None = None
    """Custom field 56"""
    custom57: str | None = None
    """Custom field 57"""
    custom58: str | None = None
    """Custom field 58"""
    custom59: str | None = None
    """Custom field 59"""
    custom6: str | None = None
    """Custom field 6"""
    custom60: str | None = None
    """Custom field 60"""
    custom61: str | None = None
    """Custom field 61"""
    custom62: str | None = None
    """Custom field 62"""
    custom63: str | None = None
    """Custom field 63"""
    custom64: str | None = None
    """Custom field 64"""
    custom65: str | None = None
    """Custom field 65"""
    custom66: str | None = None
    """Custom field 66"""
    custom67: str | None = None
    """Custom field 67"""
    custom68: str | None = None
    """Custom field 68"""
    custom69: str | None = None
    """Custom field 69"""
    custom7: str | None = None
    """Custom field 7"""
    custom70: str | None = None
    """Custom field 70"""
    custom71: str | None = None
    """Custom field 71"""
    custom72: str | None = None
    """Custom field 72"""
    custom73: str | None = None
    """Custom field 73"""
    custom74: str | None = None
    """Custom field 74"""
    custom75: str | None = None
    """Custom field 75"""
    custom76: str | None = None
    """Custom field 76"""
    custom77: str | None = None
    """Custom field 77"""
    custom78: str | None = None
    """Custom field 78"""
    custom79: str | None = None
    """Custom field 79"""
    custom8: str | None = None
    """Custom field 8"""
    custom80: str | None = None
    """Custom field 80"""
    custom81: str | None = None
    """Custom field 81"""
    custom82: str | None = None
    """Custom field 82"""
    custom83: str | None = None
    """Custom field 83"""
    custom84: str | None = None
    """Custom field 84"""
    custom85: str | None = None
    """Custom field 85"""
    custom86: str | None = None
    """Custom field 86"""
    custom87: str | None = None
    """Custom field 87"""
    custom88: str | None = None
    """Custom field 88"""
    custom89: str | None = None
    """Custom field 89"""
    custom9: str | None = None
    """Custom field 9"""
    custom90: str | None = None
    """Custom field 90"""
    custom91: str | None = None
    """Custom field 91"""
    custom92: str | None = None
    """Custom field 92"""
    custom93: str | None = None
    """Custom field 93"""
    custom94: str | None = None
    """Custom field 94"""
    custom95: str | None = None
    """Custom field 95"""
    custom96: str | None = None
    """Custom field 96"""
    custom97: str | None = None
    """Custom field 97"""
    custom98: str | None = None
    """Custom field 98"""
    custom99: str | None = None
    """Custom field 99"""
    date_of_birth: str | None = None
    """Date of birth"""
    default_plugin_mapping: list[Any] | None = None
    """Default plugin mapping"""
    degree: str | None = None
    """Degree"""
    email_addresses: list[Any] | None = None
    """Email addresses"""
    email_contacts: list[Any] | None = None
    """Email contacts"""
    email_opted_out: bool | None = None
    """Email opted out"""
    emails: list[Any] | None = None
    """Emails"""
    emails_opt_status: str | None = None
    """Emails opt status"""
    emails_opted_at: str | None = None
    """Emails opted at"""
    engaged_at: str | None = None
    """Engaged at"""
    engaged_score: float | None = None
    """Engaged score"""
    event_name: str | None = None
    """Event name"""
    external_id: str | None = None
    """External id"""
    external_owner: str | None = None
    """External owner"""
    external_source: str | None = None
    """External source"""
    facebook_url: str | None = None
    """Facebook url"""
    favorites: list[Any] | None = None
    """Favorites"""
    first_name: str | None = None
    """First name"""
    gender: str | None = None
    """Gender"""
    github_url: str | None = None
    """Github url"""
    github_username: str | None = None
    """Github username"""
    google_plus_url: str | None = None
    """Google plus url"""
    graduation_date: str | None = None
    """Graduation date"""
    home_phones: list[Any] | None = None
    """Home phones"""
    id: int | None = None
    """Unique prospect identifier"""
    job_start_date: str | None = None
    """Job start date"""
    last_name: str | None = None
    """Last name"""
    linked_in_connections: int | None = None
    """Linked in connections"""
    linked_in_id: str | None = None
    """Linked in id"""
    linked_in_slug: str | None = None
    """Linked in slug"""
    linked_in_url: str | None = None
    """Linked in url"""
    mailings: list[Any] | None = None
    """Mailings"""
    middle_name: str | None = None
    """Middle name"""
    mobile_phones: list[Any] | None = None
    """Mobile phones"""
    name: str | None = None
    """Name"""
    nickname: str | None = None
    """Nickname"""
    occupation: str | None = None
    """Occupation"""
    open_count: int | None = None
    """Open count"""
    opportunities: list[Any] | None = None
    """Opportunities"""
    opportunity_prospect_roles: list[Any] | None = None
    """Opportunity prospect roles"""
    opted_out: bool | None = None
    """Opted out"""
    opted_out_at: str | None = None
    """Opted out at"""
    other_phones: list[Any] | None = None
    """Other phones"""
    owner: list[Any] | None = None
    """Owner"""
    persona: list[Any] | None = None
    """Persona"""
    persona_name: str | None = None
    """Persona name"""
    personal_note1: str | None = None
    """Personal note1"""
    personal_note2: str | None = None
    """Personal note2"""
    phone_numbers: list[Any] | None = None
    """Phone numbers"""
    preferred_contact: str | None = None
    """Preferred contact"""
    quora_url: str | None = None
    """Quora url"""
    region: str | None = None
    """Region"""
    reply_count: int | None = None
    """Reply count"""
    school: str | None = None
    """School"""
    score: float | None = None
    """Score"""
    sequence_states: list[Any] | None = None
    """Sequence states"""
    sharing_team_id: str | None = None
    """Sharing team id"""
    sms_opt_status: str | None = None
    """Sms opt status"""
    sms_opted_at: str | None = None
    """Sms opted at"""
    sms_opted_out: bool | None = None
    """Sms opted out"""
    source: str | None = None
    """Source"""
    specialties: str | None = None
    """Specialties"""
    stack_overflow_id: str | None = None
    """Stack overflow id"""
    stack_overflow_url: str | None = None
    """Stack overflow url"""
    stage: list[Any] | None = None
    """Stage"""
    stage_name: str | None = None
    """Stage name"""
    tags: list[Any] | None = None
    """Tags"""
    tasks: list[Any] | None = None
    """Tasks"""
    time_zone: str | None = None
    """Time zone"""
    time_zone_iana: str | None = None
    """Time zone iana"""
    time_zone_inferred: str | None = None
    """Time zone inferred"""
    title: str | None = None
    """Title"""
    touched_at: str | None = None
    """Touched at"""
    trashed_at: str | None = None
    """Trashed at"""
    trashed_by_account: list[Any] | None = None
    """Trashed by account"""
    twitter_url: str | None = None
    """Twitter url"""
    twitter_username: str | None = None
    """Twitter username"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""
    updater_id: int | None = None
    """Updater id"""
    updater_type: str | None = None
    """Updater type"""
    voip_phones: list[Any] | None = None
    """Voip phones"""
    website_url1: str | None = None
    """Website url1"""
    website_url2: str | None = None
    """Website url2"""
    website_url3: str | None = None
    """Website url3"""
    work_phones: list[Any] | None = None
    """Work phones"""


class SequencesSearchData(BaseModel):
    """Search result data for sequences entity."""
    model_config = ConfigDict(extra="allow")

    automation_percentage: float | None = None
    """Automation percentage"""
    bounce_count: int | None = None
    """Bounce count"""
    calls: list[Any] | None = None
    """Calls"""
    click_count: int | None = None
    """Click count"""
    content_category_memberships: list[Any] | None = None
    """Content category memberships"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    deliver_count: int | None = None
    """Deliver count"""
    description: str | None = None
    """Description"""
    duration_in_days: int | None = None
    """Duration in days"""
    enabled: bool | None = None
    """Enabled"""
    enabled_at: str | None = None
    """Enabled at"""
    failure_count: int | None = None
    """Failure count"""
    finish_on_reply: bool | None = None
    """Finish on reply"""
    id: int | None = None
    """Unique sequence identifier"""
    last_used_at: str | None = None
    """Last used at"""
    locked: bool | None = None
    """Locked"""
    locked_at: str | None = None
    """Locked at"""
    mailings: list[Any] | None = None
    """Mailings"""
    max_activations: int | None = None
    """Max activations"""
    name: str | None = None
    """Name"""
    negative_reply_count: int | None = None
    """Negative reply count"""
    neutral_reply_count: int | None = None
    """Neutral reply count"""
    num_contacted_prospects: int | None = None
    """Num contacted prospects"""
    num_replied_prospects: int | None = None
    """Num replied prospects"""
    open_count: int | None = None
    """Open count"""
    opt_out_count: int | None = None
    """Opt out count"""
    owner: list[Any] | None = None
    """Owner"""
    positive_reply_count: int | None = None
    """Positive reply count"""
    primary_reply_action: str | None = None
    """Primary reply action"""
    primary_reply_pause_duration: int | None = None
    """Primary reply pause duration"""
    reply_count: int | None = None
    """Reply count"""
    ruleset: list[Any] | None = None
    """Ruleset"""
    schedule: list[Any] | None = None
    """Schedule"""
    schedule_count: int | None = None
    """Schedule count"""
    schedule_interval_type: str | None = None
    """Schedule interval type"""
    secondary_reply_action: str | None = None
    """Secondary reply action"""
    secondary_reply_pause_duration: int | None = None
    """Secondary reply pause duration"""
    sequence_states: list[Any] | None = None
    """Sequence states"""
    sequence_step_count: int | None = None
    """Sequence step count"""
    sequence_steps: list[Any] | None = None
    """Sequence steps"""
    sequence_type: str | None = None
    """Sequence type"""
    share_type: str | None = None
    """Share type"""
    tags: list[Any] | None = None
    """Tags"""
    tasks: list[Any] | None = None
    """Tasks"""
    throttle_capacity: int | None = None
    """Throttle capacity"""
    throttle_max_adds_per_day: int | None = None
    """Throttle max adds per day"""
    throttle_paused: bool | None = None
    """Throttle paused"""
    throttle_paused_at: str | None = None
    """Throttle paused at"""
    transactional: bool | None = None
    """Transactional"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""


class SequenceStatesSearchData(BaseModel):
    """Search result data for sequence_states entity."""
    model_config = ConfigDict(extra="allow")

    account: list[Any] | None = None
    """Account"""
    active_at: str | None = None
    """Active at"""
    active_step_mailings: list[Any] | None = None
    """Active step mailings"""
    active_step_tasks: list[Any] | None = None
    """Active step tasks"""
    bounce_count: int | None = None
    """Bounce count"""
    call_completed_at: str | None = None
    """Call completed at"""
    calls: list[Any] | None = None
    """Calls"""
    click_count: int | None = None
    """Click count"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    deliver_count: int | None = None
    """Deliver count"""
    error_reason: str | None = None
    """Error reason"""
    failure_count: int | None = None
    """Failure count"""
    id: int | None = None
    """Unique sequence state identifier"""
    mailbox: list[Any] | None = None
    """Mailbox"""
    mailings: list[Any] | None = None
    """Mailings"""
    negative_reply_count: int | None = None
    """Negative reply count"""
    neutral_reply_count: int | None = None
    """Neutral reply count"""
    open_count: int | None = None
    """Open count"""
    opportunity: list[Any] | None = None
    """Opportunity"""
    opt_out_count: int | None = None
    """Opt out count"""
    pause_reason: str | None = None
    """Pause reason"""
    positive_reply_count: int | None = None
    """Positive reply count"""
    prospect: list[Any] | None = None
    """Prospect"""
    replied_at: str | None = None
    """Replied at"""
    reply_count: int | None = None
    """Reply count"""
    schedule_count: int | None = None
    """Schedule count"""
    sequence: list[Any] | None = None
    """Sequence"""
    sequence_step: list[Any] | None = None
    """Sequence step"""
    state: str | None = None
    """State"""
    state_changed_at: str | None = None
    """State changed at"""
    tasks: list[Any] | None = None
    """Tasks"""
    updated_at: str | None = None
    """Updated at"""


class SequenceStepsSearchData(BaseModel):
    """Search result data for sequence_steps entity."""
    model_config = ConfigDict(extra="allow")

    bounce_count: int | None = None
    """Bounce count"""
    call_purpose: list[Any] | None = None
    """Call purpose"""
    calls: list[Any] | None = None
    """Calls"""
    click_count: int | None = None
    """Click count"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    date: str | None = None
    """Date"""
    deliver_count: int | None = None
    """Deliver count"""
    display_name: str | None = None
    """Display name"""
    failure_count: int | None = None
    """Failure count"""
    id: int | None = None
    """Unique sequence step identifier"""
    interval: int | None = None
    """Interval"""
    mailings: list[Any] | None = None
    """Mailings"""
    negative_reply_count: int | None = None
    """Negative reply count"""
    neutral_reply_count: int | None = None
    """Neutral reply count"""
    open_count: int | None = None
    """Open count"""
    opt_out_count: int | None = None
    """Opt out count"""
    order: int | None = None
    """Order"""
    positive_reply_count: int | None = None
    """Positive reply count"""
    reply_count: int | None = None
    """Reply count"""
    schedule_count: int | None = None
    """Schedule count"""
    sequence: list[Any] | None = None
    """Sequence"""
    sequence_templates: list[Any] | None = None
    """Sequence templates"""
    step_type: str | None = None
    """Step type"""
    task_auto_display: str | None = None
    """Task auto display"""
    task_priority: list[Any] | None = None
    """Task priority"""
    tasks: list[Any] | None = None
    """Tasks"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""


class SnippetsSearchData(BaseModel):
    """Search result data for snippets entity."""
    model_config = ConfigDict(extra="allow")

    body_html: str | None = None
    """Body html"""
    body_text: str | None = None
    """Body text"""
    content_category_memberships: list[Any] | None = None
    """Content category memberships"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    id: int | None = None
    """Unique snippet identifier"""
    name: str | None = None
    """Name"""
    owner: list[Any] | None = None
    """Owner"""
    share_type: str | None = None
    """Share type"""
    tags: str | None = None
    """Tags"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""


class StagesSearchData(BaseModel):
    """Search result data for stages entity."""
    model_config = ConfigDict(extra="allow")

    color: str | None = None
    """Color"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    id: int | None = None
    """Unique stage identifier"""
    name: str | None = None
    """Name"""
    order: int | None = None
    """Order"""
    prospects: list[Any] | None = None
    """Prospects"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""


class TasksSearchData(BaseModel):
    """Search result data for tasks entity."""
    model_config = ConfigDict(extra="allow")

    account: list[Any] | None = None
    """Account"""
    action: str | None = None
    """Action"""
    autoskip_at: str | None = None
    """Autoskip at"""
    call: list[Any] | None = None
    """Call"""
    calls: list[Any] | None = None
    """Calls"""
    compiled_sequence_template_html: str | None = None
    """Compiled sequence template html"""
    completed: bool | None = None
    """Completed"""
    completed_at: str | None = None
    """Completed at"""
    completer: list[Any] | None = None
    """Completer"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    default_plugin_mapping: list[Any] | None = None
    """Default plugin mapping"""
    due_at: str | None = None
    """Due at"""
    id: int | None = None
    """Unique task identifier"""
    mailing: list[Any] | None = None
    """Mailing"""
    mailings: list[Any] | None = None
    """Mailings"""
    note: str | None = None
    """Note"""
    opportunity: list[Any] | None = None
    """Opportunity"""
    opportunity_association: str | None = None
    """Opportunity association"""
    owner: list[Any] | None = None
    """Owner"""
    prospect: list[Any] | None = None
    """Prospect"""
    prospect_account: list[Any] | None = None
    """Prospect account"""
    prospect_contacts: list[Any] | None = None
    """Prospect contacts"""
    prospect_owner: list[Any] | None = None
    """Prospect owner"""
    prospect_phone_numbers: list[Any] | None = None
    """Prospect phone numbers"""
    prospect_stage: list[Any] | None = None
    """Prospect stage"""
    scheduled_at: str | None = None
    """Scheduled at"""
    sequence: list[Any] | None = None
    """Sequence"""
    sequence_sequence_steps: list[Any] | None = None
    """Sequence sequence steps"""
    sequence_state: list[Any] | None = None
    """Sequence state"""
    sequence_state_sequence_step: list[Any] | None = None
    """Sequence state sequence step"""
    sequence_state_sequence_step_overrides: list[Any] | None = None
    """Sequence state sequence step overrides"""
    sequence_state_starting_template: list[Any] | None = None
    """Sequence state starting template"""
    sequence_step: list[Any] | None = None
    """Sequence step"""
    sequence_step_override_templates: list[Any] | None = None
    """Sequence step override templates"""
    sequence_template: list[Any] | None = None
    """Sequence template"""
    sequence_template_template: list[Any] | None = None
    """Sequence template template"""
    state: str | None = None
    """State"""
    state_changed_at: str | None = None
    """State changed at"""
    subject: list[Any] | None = None
    """Subject"""
    task_priority: list[Any] | None = None
    """Task priority"""
    task_theme: list[Any] | None = None
    """Task theme"""
    task_type: str | None = None
    """Task type"""
    template: list[Any] | None = None
    """Template"""
    updated_at: str | None = None
    """Updated at"""


class TemplatesSearchData(BaseModel):
    """Search result data for templates entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Archived"""
    archived_at: str | None = None
    """Archived at"""
    bcc_recipients: str | None = None
    """Bcc recipients"""
    body_html: str | None = None
    """Body html"""
    body_text: str | None = None
    """Body text"""
    bounce_count: int | None = None
    """Bounce count"""
    cc_recipients: str | None = None
    """Cc recipients"""
    click_count: int | None = None
    """Click count"""
    content_category_memberships: list[Any] | None = None
    """Content category memberships"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    deliver_count: int | None = None
    """Deliver count"""
    failure_count: int | None = None
    """Failure count"""
    id: int | None = None
    """Unique template identifier"""
    last_used_at: str | None = None
    """Last used at"""
    name: str | None = None
    """Name"""
    negative_reply_count: int | None = None
    """Negative reply count"""
    neutral_reply_count: int | None = None
    """Neutral reply count"""
    open_count: int | None = None
    """Open count"""
    opt_out_count: int | None = None
    """Opt out count"""
    owner: list[Any] | None = None
    """Owner"""
    positive_reply_count: int | None = None
    """Positive reply count"""
    recipients: list[Any] | None = None
    """Recipients"""
    reply_count: int | None = None
    """Reply count"""
    schedule_count: int | None = None
    """Schedule count"""
    sequence_templates: list[Any] | None = None
    """Sequence templates"""
    share_type: str | None = None
    """Share type"""
    subject: str | None = None
    """Subject"""
    tags: str | None = None
    """Tags"""
    to_recipients: str | None = None
    """To recipients"""
    track_links: bool | None = None
    """Track links"""
    track_opens: bool | None = None
    """Track opens"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    accounts_view_id: int | None = None
    """Accounts view id"""
    active_prospects_count: int | None = None
    """Active prospects count"""
    activity_notifications_disabled: bool | None = None
    """Activity notifications disabled"""
    batches: list[Any] | None = None
    """Batches"""
    batches_view_id: int | None = None
    """Batches view id"""
    bounce_warning_email_enabled: bool | None = None
    """Bounce warning email enabled"""
    bridge_phone: str | None = None
    """Bridge phone"""
    bridge_phone_extension: str | None = None
    """Bridge phone extension"""
    buyer_language_preference: str | None = None
    """Buyer language preference"""
    calendar: list[Any] | None = None
    """Calendar"""
    calendar_events_view_id: int | None = None
    """Calendar events view id"""
    calls_view_id: int | None = None
    """Calls view id"""
    content_categories: list[Any] | None = None
    """Content categories"""
    content_category_ownerships: list[Any] | None = None
    """Content category ownerships"""
    controlled_tab_default: str | None = None
    """Controlled tab default"""
    created_at: str | None = None
    """Created at"""
    creator: list[Any] | None = None
    """Creator"""
    current_sign_in_at: str | None = None
    """Current sign in at"""
    custom1: str | None = None
    """Custom field 1"""
    custom2: str | None = None
    """Custom field 2"""
    custom3: str | None = None
    """Custom field 3"""
    custom4: str | None = None
    """Custom field 4"""
    custom5: str | None = None
    """Custom field 5"""
    daily_digest_email_enabled: bool | None = None
    """Daily digest email enabled"""
    default_ruleset_id: int | None = None
    """Default ruleset id"""
    default_schedule_id: int | None = None
    """Default schedule id"""
    duties: list[Any] | None = None
    """Duties"""
    duties_set_at: str | None = None
    """Duties set at"""
    email: str | None = None
    """Email"""
    enable_voice_recordings: bool | None = None
    """Enable voice recordings"""
    engagement_emails_enabled: bool | None = None
    """Engagement emails enabled"""
    favorites: list[Any] | None = None
    """Favorites"""
    first_name: str | None = None
    """First name"""
    global_id: str | None = None
    """Global id"""
    id: int | None = None
    """Unique user identifier"""
    imports_view_id: int | None = None
    """Imports view id"""
    inbound_bridge_phone: str | None = None
    """Inbound bridge phone"""
    inbound_bridge_phone_extension: str | None = None
    """Inbound bridge phone extension"""
    inbound_call_behavior: str | None = None
    """Inbound call behavior"""
    inbound_phone_type: str | None = None
    """Inbound phone type"""
    inbound_voicemail_custom_message_text: str | None = None
    """Inbound voicemail custom message text"""
    inbound_voicemail_message_text_voice: str | None = None
    """Inbound voicemail message text voice"""
    inbound_voicemail_prompt_type: str | None = None
    """Inbound voicemail prompt type"""
    job_role: list[Any] | None = None
    """Job role"""
    kaia_recordings_view_id: int | None = None
    """Kaia recordings view id"""
    keep_bridge_phone_connected: bool | None = None
    """Keep bridge phone connected"""
    language_preference: str | None = None
    """Language preference"""
    last_name: str | None = None
    """Last name"""
    last_sign_in_at: str | None = None
    """Last sign in at"""
    link_to_sequence_state_in_task_flow: bool | None = None
    """Link to sequence state in task flow"""
    live_listen_view_id: int | None = None
    """Live listen view id"""
    locked: bool | None = None
    """Locked"""
    mailbox: list[Any] | None = None
    """Mailbox"""
    mailbox_error_email_enabled: bool | None = None
    """Mailbox error email enabled"""
    mailboxes: list[Any] | None = None
    """Mailboxes"""
    mailings_delivered_count: int | None = None
    """Mailings delivered count"""
    mailings_replied_count: int | None = None
    """Mailings replied count"""
    mailings_view_id: int | None = None
    """Mailings view id"""
    meeting_engagement_notification_enabled: bool | None = None
    """Meeting engagement notification enabled"""
    meeting_types_view_id: int | None = None
    """Meeting types view id"""
    name: str | None = None
    """Name"""
    notifications_enabled: bool | None = None
    """Notifications enabled"""
    oce_click_to_dial_everywhere: bool | None = None
    """Oce click to dial everywhere"""
    oce_gmail_toolbar: bool | None = None
    """Oce gmail toolbar"""
    oce_gmail_tracking_state: str | None = None
    """Oce gmail tracking state"""
    oce_salesforce_email_decorating: bool | None = None
    """Oce salesforce email decorating"""
    oce_salesforce_phone_decorating: bool | None = None
    """Oce salesforce phone decorating"""
    oce_universal_task_flow: bool | None = None
    """Oce universal task flow"""
    oce_window_mode: bool | None = None
    """Oce window mode"""
    onboarded_at: str | None = None
    """Onboarded at"""
    opportunities_view_id: int | None = None
    """Opportunities view id"""
    orca_standalone_enabled: bool | None = None
    """Orca standalone enabled"""
    outbound_voicemails: list[Any] | None = None
    """Outbound voicemails"""
    password_expires_at: str | None = None
    """Password expires at"""
    phone: list[Any] | None = None
    """Phone"""
    phone_country_code: str | None = None
    """Phone country code"""
    phone_number: str | None = None
    """Phone number"""
    phone_type: str | None = None
    """Phone type"""
    phones: list[Any] | None = None
    """Phones"""
    phones_view_id: int | None = None
    """Phones view id"""
    plugin_alert_notification_enabled: bool | None = None
    """Plugin alert notification enabled"""
    preferred_voice_region: str | None = None
    """Preferred voice region"""
    prefers_local_presence: bool | None = None
    """Prefers local presence"""
    primary_timezone: str | None = None
    """Primary timezone"""
    profile: list[Any] | None = None
    """Profile"""
    prospect_detail_default: str | None = None
    """Prospect detail default"""
    prospects_view_id: int | None = None
    """Prospects view id"""
    recipients: list[Any] | None = None
    """Recipients"""
    reports_sequence_performance_view_id: int | None = None
    """Reports sequence performance view id"""
    reports_team_perf_view_id: int | None = None
    """Reports team perf view id"""
    reports_team_performance_intraday_view_id: int | None = None
    """Reports team performance intraday view id"""
    reports_team_performance_view_id: int | None = None
    """Reports team performance view id"""
    reports_view_id: int | None = None
    """Reports view id"""
    role: list[Any] | None = None
    """Role"""
    scim_external_id: str | None = None
    """Scim external id"""
    scim_source: str | None = None
    """Scim source"""
    secondary_timezone: str | None = None
    """Secondary timezone"""
    send_invite_fallback: bool | None = None
    """Send invite fallback"""
    sender_notifications_excluded: bool | None = None
    """Sender notifications excluded"""
    sequence_states_view_id: int | None = None
    """Sequence states view id"""
    sequences_view_id: int | None = None
    """Sequences view id"""
    sms_phone: list[Any] | None = None
    """Sms phone"""
    snippets_view_id: int | None = None
    """Snippets view id"""
    tasks_due_count: int | None = None
    """Tasks due count"""
    tasks_view_id: int | None = None
    """Tasks view id"""
    teams: list[Any] | None = None
    """Teams"""
    teams_view_id: int | None = None
    """Teams view id"""
    templates_view_id: int | None = None
    """Templates view id"""
    tertiary_timezone: str | None = None
    """Tertiary timezone"""
    texting_email_notifications: bool | None = None
    """Texting email notifications"""
    title: str | None = None
    """Title"""
    unknown_reply_email_enabled: bool | None = None
    """Unknown reply email enabled"""
    updated_at: str | None = None
    """Updated at"""
    updater: list[Any] | None = None
    """Updater"""
    use_sales_navigator_for_linked_in_tasks: bool | None = None
    """Use sales navigator for linked in tasks"""
    user_guid: str | None = None
    """User guid"""
    username: str | None = None
    """Username"""
    users_view_id: int | None = None
    """Users view id"""
    voicemail_notification_enabled: bool | None = None
    """Voicemail notification enabled"""
    voicemail_prompts: list[Any] | None = None
    """Voicemail prompts"""
    weekly_digest_email_enabled: bool | None = None
    """Weekly digest email enabled"""


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

AccountsSearchResult = AirbyteSearchResult[AccountsSearchData]
"""Search result type for accounts entity."""

CallsSearchResult = AirbyteSearchResult[CallsSearchData]
"""Search result type for calls entity."""

CallDispositionsSearchResult = AirbyteSearchResult[CallDispositionsSearchData]
"""Search result type for call_dispositions entity."""

CallPurposesSearchResult = AirbyteSearchResult[CallPurposesSearchData]
"""Search result type for call_purposes entity."""

MailingsSearchResult = AirbyteSearchResult[MailingsSearchData]
"""Search result type for mailings entity."""

MailboxesSearchResult = AirbyteSearchResult[MailboxesSearchData]
"""Search result type for mailboxes entity."""

OpportunitiesSearchResult = AirbyteSearchResult[OpportunitiesSearchData]
"""Search result type for opportunities entity."""

PersonasSearchResult = AirbyteSearchResult[PersonasSearchData]
"""Search result type for personas entity."""

ProspectsSearchResult = AirbyteSearchResult[ProspectsSearchData]
"""Search result type for prospects entity."""

SequencesSearchResult = AirbyteSearchResult[SequencesSearchData]
"""Search result type for sequences entity."""

SequenceStatesSearchResult = AirbyteSearchResult[SequenceStatesSearchData]
"""Search result type for sequence_states entity."""

SequenceStepsSearchResult = AirbyteSearchResult[SequenceStepsSearchData]
"""Search result type for sequence_steps entity."""

SnippetsSearchResult = AirbyteSearchResult[SnippetsSearchData]
"""Search result type for snippets entity."""

StagesSearchResult = AirbyteSearchResult[StagesSearchData]
"""Search result type for stages entity."""

TasksSearchResult = AirbyteSearchResult[TasksSearchData]
"""Search result type for tasks entity."""

TemplatesSearchResult = AirbyteSearchResult[TemplatesSearchData]
"""Search result type for templates entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ProspectsListResult = OutreachExecuteResultWithMeta[list[Prospect], ProspectsListResultMeta]
"""Result type for prospects.list operation with data and metadata."""

AccountsListResult = OutreachExecuteResultWithMeta[list[Account], AccountsListResultMeta]
"""Result type for accounts.list operation with data and metadata."""

SequencesListResult = OutreachExecuteResultWithMeta[list[Sequence], SequencesListResultMeta]
"""Result type for sequences.list operation with data and metadata."""

SequenceStatesListResult = OutreachExecuteResultWithMeta[list[SequenceState], SequenceStatesListResultMeta]
"""Result type for sequence_states.list operation with data and metadata."""

SequenceStepsListResult = OutreachExecuteResultWithMeta[list[SequenceStep], SequenceStepsListResultMeta]
"""Result type for sequence_steps.list operation with data and metadata."""

OpportunitiesListResult = OutreachExecuteResultWithMeta[list[Opportunity], OpportunitiesListResultMeta]
"""Result type for opportunities.list operation with data and metadata."""

CallsListResult = OutreachExecuteResultWithMeta[list[Call], CallsListResultMeta]
"""Result type for calls.list operation with data and metadata."""

CallDispositionsListResult = OutreachExecuteResultWithMeta[list[CallDisposition], CallDispositionsListResultMeta]
"""Result type for call_dispositions.list operation with data and metadata."""

CallPurposesListResult = OutreachExecuteResultWithMeta[list[CallPurpose], CallPurposesListResultMeta]
"""Result type for call_purposes.list operation with data and metadata."""

MailingsListResult = OutreachExecuteResultWithMeta[list[Mailing], MailingsListResultMeta]
"""Result type for mailings.list operation with data and metadata."""

MailboxesListResult = OutreachExecuteResultWithMeta[list[Mailbox], MailboxesListResultMeta]
"""Result type for mailboxes.list operation with data and metadata."""

TasksListResult = OutreachExecuteResultWithMeta[list[Task], TasksListResultMeta]
"""Result type for tasks.list operation with data and metadata."""

UsersListResult = OutreachExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

StagesListResult = OutreachExecuteResultWithMeta[list[Stage], StagesListResultMeta]
"""Result type for stages.list operation with data and metadata."""

PersonasListResult = OutreachExecuteResultWithMeta[list[Persona], PersonasListResultMeta]
"""Result type for personas.list operation with data and metadata."""

TemplatesListResult = OutreachExecuteResultWithMeta[list[Template], TemplatesListResultMeta]
"""Result type for templates.list operation with data and metadata."""

SnippetsListResult = OutreachExecuteResultWithMeta[list[Snippet], SnippetsListResultMeta]
"""Result type for snippets.list operation with data and metadata."""

