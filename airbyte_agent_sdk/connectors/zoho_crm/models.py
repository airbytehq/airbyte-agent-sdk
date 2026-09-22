"""
Pydantic models for zoho-crm connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""
# ruff: noqa: E501

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class ZohoCrmAuthConfig(BaseModel):
    """Zoho CRM OAuth 2.0"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """OAuth 2.0 Client ID from Zoho Developer Console"""
    client_secret: str
    """OAuth 2.0 Client Secret from Zoho Developer Console"""
    refresh_token: str
    """OAuth 2.0 Refresh Token (does not expire)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Owner(BaseModel):
    """Record owner reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    id: str | None = Field(default=None)
    email: str | None = Field(default=None)

class CreatedBy(BaseModel):
    """User who created the record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    id: str | None = Field(default=None)
    email: str | None = Field(default=None)

class ModifiedBy(BaseModel):
    """User who last modified the record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    id: str | None = Field(default=None)
    email: str | None = Field(default=None)

class LookupRef(BaseModel):
    """Lookup reference to another record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    id: str | None = Field(default=None)

class PaginationInfo(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    per_page: int | None = Field(default=None)
    count: int | None = Field(default=None)
    page: int | None = Field(default=None)
    more_records: bool | None = Field(default=None)
    sort_by: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)

class Lead(BaseModel):
    """Zoho CRM lead object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    company: str | None = Field(default=None, alias="Company")
    first_name: str | None = Field(default=None, alias="First_Name")
    last_name: str | None = Field(default=None, alias="Last_Name")
    full_name: str | None = Field(default=None, alias="Full_Name")
    email: str | None = Field(default=None, alias="Email")
    phone: str | None = Field(default=None, alias="Phone")
    mobile: str | None = Field(default=None, alias="Mobile")
    fax: str | None = Field(default=None, alias="Fax")
    designation: str | None = Field(default=None, alias="Designation")
    lead_source: str | None = Field(default=None, alias="Lead_Source")
    industry: str | None = Field(default=None, alias="Industry")
    annual_revenue: float | None = Field(default=None, alias="Annual_Revenue")
    no_of_employees: int | None = Field(default=None, alias="No_of_Employees")
    rating: str | None = Field(default=None, alias="Rating")
    lead_status: str | None = Field(default=None, alias="Lead_Status")
    website: str | None = Field(default=None, alias="Website")
    street: str | None = Field(default=None, alias="Street")
    city: str | None = Field(default=None, alias="City")
    state: str | None = Field(default=None, alias="State")
    zip_code: str | None = Field(default=None, alias="Zip_Code")
    country: str | None = Field(default=None, alias="Country")
    description: str | None = Field(default=None, alias="Description")
    converted_detail: dict[str, Any] | None = Field(default=None, alias="Converted_Detail")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    converted: bool | None = Field(default=None, alias="$converted")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    layout_id: dict[str, Any] | None = Field(default=None, alias="$layout_id")
    locked_for_me: bool | None = Field(default=None, alias="$locked_for_me")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    zia_owner_assignment: str | None = Field(default=None, alias="$zia_owner_assignment")
    email_opt_out: bool | None = Field(default=None, alias="Email_Opt_Out")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    locked_s: bool | None = Field(default=None, alias="Locked__s")
    record_image: str | None = Field(default=None, alias="Record_Image")
    salutation: str | None = Field(default=None, alias="Salutation")
    secondary_email: str | None = Field(default=None, alias="Secondary_Email")
    skype_id: str | None = Field(default=None, alias="Skype_ID")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")
    twitter: str | None = Field(default=None, alias="Twitter")
    unsubscribed_mode: str | None = Field(default=None, alias="Unsubscribed_Mode")
    unsubscribed_time: str | None = Field(default=None, alias="Unsubscribed_Time")

class LeadsList(BaseModel):
    """Paginated list of leads"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Lead] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Contact(BaseModel):
    """Zoho CRM contact object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    first_name: str | None = Field(default=None, alias="First_Name")
    last_name: str | None = Field(default=None, alias="Last_Name")
    full_name: str | None = Field(default=None, alias="Full_Name")
    email: str | None = Field(default=None, alias="Email")
    phone: str | None = Field(default=None, alias="Phone")
    mobile: str | None = Field(default=None, alias="Mobile")
    fax: str | None = Field(default=None, alias="Fax")
    title: str | None = Field(default=None, alias="Title")
    department: str | None = Field(default=None, alias="Department")
    account_name: Any | None = Field(default=None, alias="Account_Name")
    lead_source: str | None = Field(default=None, alias="Lead_Source")
    date_of_birth: str | None = Field(default=None, alias="Date_of_Birth")
    mailing_street: str | None = Field(default=None, alias="Mailing_Street")
    mailing_city: str | None = Field(default=None, alias="Mailing_City")
    mailing_state: str | None = Field(default=None, alias="Mailing_State")
    mailing_zip: str | None = Field(default=None, alias="Mailing_Zip")
    mailing_country: str | None = Field(default=None, alias="Mailing_Country")
    other_street: str | None = Field(default=None, alias="Other_Street")
    other_city: str | None = Field(default=None, alias="Other_City")
    other_state: str | None = Field(default=None, alias="Other_State")
    other_zip: str | None = Field(default=None, alias="Other_Zip")
    other_country: str | None = Field(default=None, alias="Other_Country")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    is_duplicate: bool | None = Field(default=None, alias="$is_duplicate")
    layout_id: dict[str, Any] | None = Field(default=None, alias="$layout_id")
    locked_for_me: bool | None = Field(default=None, alias="$locked_for_me")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    state: str | None = Field(default=None, alias="$state")
    zia_owner_assignment: str | None = Field(default=None, alias="$zia_owner_assignment")
    assistant: str | None = Field(default=None, alias="Assistant")
    asst_phone: str | None = Field(default=None, alias="Asst_Phone")
    contact_auto_number: str | None = Field(default=None, alias="Contact_Auto_Number")
    email_opt_out: bool | None = Field(default=None, alias="Email_Opt_Out")
    home_phone: str | None = Field(default=None, alias="Home_Phone")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    locked_s: bool | None = Field(default=None, alias="Locked__s")
    other_phone: str | None = Field(default=None, alias="Other_Phone")
    record_image: str | None = Field(default=None, alias="Record_Image")
    reporting_to: Any | None = Field(default=None, alias="Reporting_To")
    salutation: str | None = Field(default=None, alias="Salutation")
    secondary_email: str | None = Field(default=None, alias="Secondary_Email")
    skype_id: str | None = Field(default=None, alias="Skype_ID")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")
    twitter: str | None = Field(default=None, alias="Twitter")
    unsubscribed_mode: str | None = Field(default=None, alias="Unsubscribed_Mode")
    unsubscribed_time: str | None = Field(default=None, alias="Unsubscribed_Time")
    vendor_name: Any | None = Field(default=None, alias="Vendor_Name")

class ContactsList(BaseModel):
    """Paginated list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Contact] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Account(BaseModel):
    """Zoho CRM account (company) object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    account_name: str | None = Field(default=None, alias="Account_Name")
    account_number: str | None = Field(default=None, alias="Account_Number")
    account_type: str | None = Field(default=None, alias="Account_Type")
    industry: str | None = Field(default=None, alias="Industry")
    annual_revenue: float | None = Field(default=None, alias="Annual_Revenue")
    employees: int | None = Field(default=None, alias="Employees")
    phone: str | None = Field(default=None, alias="Phone")
    fax: str | None = Field(default=None, alias="Fax")
    website: str | None = Field(default=None, alias="Website")
    ownership: str | None = Field(default=None, alias="Ownership")
    rating: str | None = Field(default=None, alias="Rating")
    sic_code: int | None = Field(default=None, alias="SIC_Code")
    ticker_symbol: str | None = Field(default=None, alias="Ticker_Symbol")
    parent_account: Any | None = Field(default=None, alias="Parent_Account")
    billing_street: str | None = Field(default=None, alias="Billing_Street")
    billing_city: str | None = Field(default=None, alias="Billing_City")
    billing_state: str | None = Field(default=None, alias="Billing_State")
    billing_code: str | None = Field(default=None, alias="Billing_Code")
    billing_country: str | None = Field(default=None, alias="Billing_Country")
    shipping_street: str | None = Field(default=None, alias="Shipping_Street")
    shipping_city: str | None = Field(default=None, alias="Shipping_City")
    shipping_state: str | None = Field(default=None, alias="Shipping_State")
    shipping_code: str | None = Field(default=None, alias="Shipping_Code")
    shipping_country: str | None = Field(default=None, alias="Shipping_Country")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    is_duplicate: bool | None = Field(default=None, alias="$is_duplicate")
    layout_id: dict[str, Any] | None = Field(default=None, alias="$layout_id")
    locked_for_me: bool | None = Field(default=None, alias="$locked_for_me")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    state: str | None = Field(default=None, alias="$state")
    zia_owner_assignment: str | None = Field(default=None, alias="$zia_owner_assignment")
    account_site: str | None = Field(default=None, alias="Account_Site")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    locked_s: bool | None = Field(default=None, alias="Locked__s")
    record_image: str | None = Field(default=None, alias="Record_Image")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")

class AccountsList(BaseModel):
    """Paginated list of accounts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Account] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class DealPipeline(BaseModel):
    """Sales pipeline reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    id: str | None = Field(default=None)

class Deal(BaseModel):
    """Zoho CRM deal (opportunity) object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    deal_name: str | None = Field(default=None, alias="Deal_Name")
    amount: float | None = Field(default=None, alias="Amount")
    stage: str | None = Field(default=None, alias="Stage")
    probability: int | None = Field(default=None, alias="Probability")
    closing_date: str | None = Field(default=None, alias="Closing_Date")
    type_: str | None = Field(default=None, alias="Type")
    next_step: str | None = Field(default=None, alias="Next_Step")
    lead_source: str | None = Field(default=None, alias="Lead_Source")
    contact_name: Any | None = Field(default=None, alias="Contact_Name")
    account_name: Any | None = Field(default=None, alias="Account_Name")
    campaign_source: Any | None = Field(default=None, alias="Campaign_Source")
    pipeline: DealPipeline | None = Field(default=None, alias="Pipeline")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    followed: bool | None = Field(default=None, alias="$followed")
    followers: list[Any] | None = Field(default=None, alias="$followers")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    layout_id: dict[str, Any] | None = Field(default=None, alias="$layout_id")
    locked_for_me: bool | None = Field(default=None, alias="$locked_for_me")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    state: str | None = Field(default=None, alias="$state")
    zia_owner_assignment: str | None = Field(default=None, alias="$zia_owner_assignment")
    expected_revenue: float | None = Field(default=None, alias="Expected_Revenue")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    lead_conversion_time: int | None = Field(default=None, alias="Lead_Conversion_Time")
    locked_s: bool | None = Field(default=None, alias="Locked__s")
    overall_sales_duration: int | None = Field(default=None, alias="Overall_Sales_Duration")
    sales_cycle_duration: int | None = Field(default=None, alias="Sales_Cycle_Duration")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")

class DealsList(BaseModel):
    """Paginated list of deals"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Deal] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Campaign(BaseModel):
    """Zoho CRM campaign object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    campaign_name: str | None = Field(default=None, alias="Campaign_Name")
    type_: str | None = Field(default=None, alias="Type")
    status: str | None = Field(default=None, alias="Status")
    start_date: str | None = Field(default=None, alias="Start_Date")
    end_date: str | None = Field(default=None, alias="End_Date")
    expected_revenue: float | None = Field(default=None, alias="Expected_Revenue")
    budgeted_cost: float | None = Field(default=None, alias="Budgeted_Cost")
    actual_cost: float | None = Field(default=None, alias="Actual_Cost")
    num_sent: str | None = Field(default=None, alias="Num_sent")
    expected_response: int | None = Field(default=None, alias="Expected_Response")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    layout_id: dict[str, Any] | None = Field(default=None, alias="$layout_id")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    state: str | None = Field(default=None, alias="$state")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    parent_campaign: Any | None = Field(default=None, alias="Parent_Campaign")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")

class CampaignsList(BaseModel):
    """Paginated list of campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Campaign] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Task(BaseModel):
    """Zoho CRM task object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    subject: str | None = Field(default=None, alias="Subject")
    due_date: str | None = Field(default=None, alias="Due_Date")
    status: str | None = Field(default=None, alias="Status")
    priority: str | None = Field(default=None, alias="Priority")
    send_notification_email: bool | None = Field(default=None, alias="Send_Notification_Email")
    remind_at: dict[str, Any] | None = Field(default=None, alias="Remind_At")
    who_id: Any | None = Field(default=None, alias="Who_Id")
    what_id: Any | None = Field(default=None, alias="What_Id")
    recurring_activity: dict[str, Any] | None = Field(default=None, alias="Recurring_Activity")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    closed_time: str | None = Field(default=None, alias="Closed_Time")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    locked_for_me: bool | None = Field(default=None, alias="$locked_for_me")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    se_module: str | None = Field(default=None, alias="$se_module")
    state: str | None = Field(default=None, alias="$state")
    u_id: str | None = Field(default=None, alias="$u_id")
    zia_owner_assignment: str | None = Field(default=None, alias="$zia_owner_assignment")
    best_time: list[Any] | None = Field(default=None, alias="BEST_TIME")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    locked_s: bool | None = Field(default=None, alias="Locked__s")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")

class TasksList(BaseModel):
    """Paginated list of tasks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Task] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class EventParticipantsItem(BaseModel):
    """Nested schema for Event.Participants_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    email: str | None = Field(default=None, alias="Email")
    invited: bool | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    participant: str | None = Field(default=None)
    status: str | None = Field(default=None)

class Event(BaseModel):
    """Zoho CRM event (meeting/calendar) object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    event_title: str | None = Field(default=None, alias="Event_Title")
    start_date_time: str | None = Field(default=None, alias="Start_DateTime")
    end_date_time: str | None = Field(default=None, alias="End_DateTime")
    all_day: bool | None = Field(default=None, alias="All_day")
    venue: str | None = Field(default=None, alias="Venue")
    participants: list[EventParticipantsItem] | None = Field(default=None, alias="Participants")
    who_id: Any | None = Field(default=None, alias="Who_Id")
    what_id: Any | None = Field(default=None, alias="What_Id")
    remind_at: dict[str, Any] | None = Field(default=None, alias="Remind_At")
    recurring_activity: dict[str, Any] | None = Field(default=None, alias="Recurring_Activity")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    calendar_booking_event: bool | None = Field(default=None, alias="$calendar_booking_event")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    meeting_details: dict[str, Any] | None = Field(default=None, alias="$meeting_details")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    recurrence_id: str | None = Field(default=None, alias="$recurrence_id")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    se_module: str | None = Field(default=None, alias="$se_module")
    send_notification: bool | None = Field(default=None, alias="$send_notification")
    state: str | None = Field(default=None, alias="$state")
    u_id: str | None = Field(default=None, alias="$u_id")
    check_in_address: str | None = Field(default=None, alias="Check_In_Address")
    check_in_by: dict[str, Any] | None = Field(default=None, alias="Check_In_By")
    check_in_city: str | None = Field(default=None, alias="Check_In_City")
    check_in_comment: str | None = Field(default=None, alias="Check_In_Comment")
    check_in_country: str | None = Field(default=None, alias="Check_In_Country")
    check_in_state: str | None = Field(default=None, alias="Check_In_State")
    check_in_status: str | None = Field(default=None, alias="Check_In_Status")
    check_in_sub_locality: str | None = Field(default=None, alias="Check_In_Sub_Locality")
    check_in_time: str | None = Field(default=None, alias="Check_In_Time")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    latitude: float | None = Field(default=None, alias="Latitude")
    longitude: float | None = Field(default=None, alias="Longitude")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")
    zip_code: str | None = Field(default=None, alias="ZIP_Code")

class EventsList(BaseModel):
    """Paginated list of events"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Event] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Call(BaseModel):
    """Zoho CRM call object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    subject: str | None = Field(default=None, alias="Subject")
    call_type: str | None = Field(default=None, alias="Call_Type")
    call_start_time: str | None = Field(default=None, alias="Call_Start_Time")
    call_duration: str | None = Field(default=None, alias="Call_Duration")
    call_duration_in_seconds: float | None = Field(default=None, alias="Call_Duration_in_seconds")
    call_purpose: str | None = Field(default=None, alias="Call_Purpose")
    call_result: str | None = Field(default=None, alias="Call_Result")
    who_id: Any | None = Field(default=None, alias="Who_Id")
    what_id: Any | None = Field(default=None, alias="What_Id")
    description: str | None = Field(default=None, alias="Description")
    caller_id: str | None = Field(default=None, alias="Caller_ID")
    call_status: str | None = Field(default=None, alias="Call_Status")
    call_agenda: str | None = Field(default=None, alias="Call_Agenda")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    calendar_booking_call: bool | None = Field(default=None, alias="$calendar_booking_call")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    se_module: str | None = Field(default=None, alias="$se_module")
    state: str | None = Field(default=None, alias="$state")
    dialled_number: str | None = Field(default=None, alias="Dialled_Number")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    reminder: str | None = Field(default=None, alias="Reminder")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")

class CallsList(BaseModel):
    """Paginated list of calls"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Call] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Product(BaseModel):
    """Zoho CRM product object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    product_name: str | None = Field(default=None, alias="Product_Name")
    product_code: str | None = Field(default=None, alias="Product_Code")
    product_category: str | None = Field(default=None, alias="Product_Category")
    product_active: bool | None = Field(default=None, alias="Product_Active")
    unit_price: float | None = Field(default=None, alias="Unit_Price")
    commission_rate: float | None = Field(default=None, alias="Commission_Rate")
    manufacturer: str | None = Field(default=None, alias="Manufacturer")
    sales_start_date: str | None = Field(default=None, alias="Sales_Start_Date")
    sales_end_date: str | None = Field(default=None, alias="Sales_End_Date")
    support_start_date: str | None = Field(default=None, alias="Support_Start_Date")
    support_expiry_date: str | None = Field(default=None, alias="Support_Expiry_Date")
    qty_in_stock: float | None = Field(default=None, alias="Qty_in_Stock")
    qty_in_demand: float | None = Field(default=None, alias="Qty_in_Demand")
    qty_ordered: float | None = Field(default=None, alias="Qty_Ordered")
    reorder_level: float | None = Field(default=None, alias="Reorder_Level")
    handler: Any | None = Field(default=None, alias="Handler")
    tax: list[str] | None = Field(default=None, alias="Tax")
    vendor_name: Any | None = Field(default=None, alias="Vendor_Name")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    layout_id: dict[str, Any] | None = Field(default=None, alias="$layout_id")
    locked_for_me: bool | None = Field(default=None, alias="$locked_for_me")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    state: str | None = Field(default=None, alias="$state")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    locked_s: bool | None = Field(default=None, alias="Locked__s")
    record_image: str | None = Field(default=None, alias="Record_Image")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")
    taxable: bool | None = Field(default=None, alias="Taxable")
    usage_unit: str | None = Field(default=None, alias="Usage_Unit")

class ProductsList(BaseModel):
    """Paginated list of products"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Product] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Quote(BaseModel):
    """Zoho CRM quote object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    subject: str | None = Field(default=None, alias="Subject")
    quote_stage: str | None = Field(default=None, alias="Quote_Stage")
    valid_till: str | None = Field(default=None, alias="Valid_Till")
    deal_name: Any | None = Field(default=None, alias="Deal_Name")
    contact_name: Any | None = Field(default=None, alias="Contact_Name")
    account_name: Any | None = Field(default=None, alias="Account_Name")
    carrier: str | None = Field(default=None, alias="Carrier")
    shipping_street: str | None = Field(default=None, alias="Shipping_Street")
    shipping_city: str | None = Field(default=None, alias="Shipping_City")
    shipping_state: str | None = Field(default=None, alias="Shipping_State")
    shipping_code: str | None = Field(default=None, alias="Shipping_Code")
    shipping_country: str | None = Field(default=None, alias="Shipping_Country")
    billing_street: str | None = Field(default=None, alias="Billing_Street")
    billing_city: str | None = Field(default=None, alias="Billing_City")
    billing_state: str | None = Field(default=None, alias="Billing_State")
    billing_code: str | None = Field(default=None, alias="Billing_Code")
    billing_country: str | None = Field(default=None, alias="Billing_Country")
    sub_total: float | None = Field(default=None, alias="Sub_Total")
    tax: float | None = Field(default=None, alias="Tax")
    adjustment: float | None = Field(default=None, alias="Adjustment")
    grand_total: float | None = Field(default=None, alias="Grand_Total")
    discount: float | None = Field(default=None, alias="Discount")
    terms_and_conditions: str | None = Field(default=None, alias="Terms_and_Conditions")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    converted: bool | None = Field(default=None, alias="$converted")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    layout_id: dict[str, Any] | None = Field(default=None, alias="$layout_id")
    line_tax: list[Any] | None = Field(default=None, alias="$line_tax")
    locked_for_me: bool | None = Field(default=None, alias="$locked_for_me")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    state: str | None = Field(default=None, alias="$state")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    locked_s: bool | None = Field(default=None, alias="Locked__s")
    product_details: list[dict[str, Any]] | None = Field(default=None, alias="Product_Details")
    quote_number: str | None = Field(default=None, alias="Quote_Number")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")
    team: str | None = Field(default=None, alias="Team")

class QuotesList(BaseModel):
    """Paginated list of quotes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Quote] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Invoice(BaseModel):
    """Zoho CRM invoice object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    subject: str | None = Field(default=None, alias="Subject")
    invoice_number: str | None = Field(default=None, alias="Invoice_Number")
    invoice_date: str | None = Field(default=None, alias="Invoice_Date")
    due_date: str | None = Field(default=None, alias="Due_Date")
    status: str | None = Field(default=None, alias="Status")
    sales_order: Any | None = Field(default=None, alias="Sales_Order")
    contact_name: Any | None = Field(default=None, alias="Contact_Name")
    account_name: Any | None = Field(default=None, alias="Account_Name")
    deal_name: Any | None = Field(default=None, alias="Deal_Name")
    purchase_order: str | None = Field(default=None, alias="Purchase_Order")
    excise_duty: float | None = Field(default=None, alias="Excise_Duty")
    billing_street: str | None = Field(default=None, alias="Billing_Street")
    billing_city: str | None = Field(default=None, alias="Billing_City")
    billing_state: str | None = Field(default=None, alias="Billing_State")
    billing_code: str | None = Field(default=None, alias="Billing_Code")
    billing_country: str | None = Field(default=None, alias="Billing_Country")
    shipping_street: str | None = Field(default=None, alias="Shipping_Street")
    shipping_city: str | None = Field(default=None, alias="Shipping_City")
    shipping_state: str | None = Field(default=None, alias="Shipping_State")
    shipping_code: str | None = Field(default=None, alias="Shipping_Code")
    shipping_country: str | None = Field(default=None, alias="Shipping_Country")
    sub_total: float | None = Field(default=None, alias="Sub_Total")
    tax: float | None = Field(default=None, alias="Tax")
    adjustment: float | None = Field(default=None, alias="Adjustment")
    grand_total: float | None = Field(default=None, alias="Grand_Total")
    discount: float | None = Field(default=None, alias="Discount")
    terms_and_conditions: str | None = Field(default=None, alias="Terms_and_Conditions")
    description: str | None = Field(default=None, alias="Description")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")
    record_status_s: str | None = Field(default=None, alias="Record_Status__s")
    approval: dict[str, Any] | None = Field(default=None, alias="$approval")
    approval_state: str | None = Field(default=None, alias="$approval_state")
    approved: bool | None = Field(default=None, alias="$approved")
    currency_symbol: str | None = Field(default=None, alias="$currency_symbol")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    in_merge: bool | None = Field(default=None, alias="$in_merge")
    layout_id: dict[str, Any] | None = Field(default=None, alias="$layout_id")
    line_tax: list[Any] | None = Field(default=None, alias="$line_tax")
    locked_for_me: bool | None = Field(default=None, alias="$locked_for_me")
    orchestration: bool | None = Field(default=None, alias="$orchestration")
    process_flow: bool | None = Field(default=None, alias="$process_flow")
    review: dict[str, Any] | None = Field(default=None, alias="$review")
    review_process: dict[str, Any] | None = Field(default=None, alias="$review_process")
    state: str | None = Field(default=None, alias="$state")
    last_activity_time: str | None = Field(default=None, alias="Last_Activity_Time")
    locked_s: bool | None = Field(default=None, alias="Locked__s")
    product_details: list[dict[str, Any]] | None = Field(default=None, alias="Product_Details")
    sales_commission: float | None = Field(default=None, alias="Sales_Commission")
    tag: list[dict[str, Any]] | None = Field(default=None, alias="Tag")

class InvoicesList(BaseModel):
    """Paginated list of invoices"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Invoice] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

class Note(BaseModel):
    """Zoho CRM note object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    owner: Any | None = Field(default=None, alias="Owner")
    note_title: str | None = Field(default=None, alias="Note_Title")
    note_content: str | None = Field(default=None, alias="Note_Content")
    parent_id: Any | None = Field(default=None, alias="Parent_Id")
    created_time: str | None = Field(default=None, alias="Created_Time")
    modified_time: str | None = Field(default=None, alias="Modified_Time")
    attachments: list[Any] | None = Field(default=None, alias="$attachments")
    editable: bool | None = Field(default=None, alias="$editable")
    field_states: dict[str, Any] | None = Field(default=None, alias="$field_states")
    is_shared_to_client: bool | None = Field(default=None, alias="$is_shared_to_client")
    se_module: str | None = Field(default=None, alias="$se_module")
    size: int | None = Field(default=None, alias="$size")
    state: str | None = Field(default=None, alias="$state")
    voice_note: bool | None = Field(default=None, alias="$voice_note")
    created_by: Any | None = Field(default=None, alias="Created_By")
    modified_by: Any | None = Field(default=None, alias="Modified_By")

class NotesList(BaseModel):
    """Paginated list of notes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Note] | None = Field(default=None)
    info: PaginationInfo | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class LeadsListResultMeta(BaseModel):
    """Metadata for leads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class DealsListResultMeta(BaseModel):
    """Metadata for deals.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class EventsListResultMeta(BaseModel):
    """Metadata for events.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class CallsListResultMeta(BaseModel):
    """Metadata for calls.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class ProductsListResultMeta(BaseModel):
    """Metadata for products.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class QuotesListResultMeta(BaseModel):
    """Metadata for quotes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class InvoicesListResultMeta(BaseModel):
    """Metadata for invoices.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

class NotesListResultMeta(BaseModel):
    """Metadata for notes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    more_records: bool | None = Field(default=None)
    page: int | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class ZohoCrmCheckResult(BaseModel):
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


class ZohoCrmExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ZohoCrmExecuteResultWithMeta(ZohoCrmExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class LeadsSearchData(BaseModel):
    """Search result data for leads entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    first_name: str | None = None
    """Lead's first name"""
    last_name: str | None = None
    """Lead's last name"""
    full_name: str | None = None
    """Lead's full name"""
    email: str | None = None
    """Lead's email address"""
    phone: str | None = None
    """Lead's phone number"""
    mobile: str | None = None
    """Lead's mobile number"""
    company: str | None = None
    """Company the lead is associated with"""
    designation: str | None = None
    """Lead's job title. Zoho names this `Designation` on Leads and `Title` on Contacts; there is no `Title` field on the Leads module.
"""
    lead_source: str | None = None
    """Source from which the lead was generated"""
    industry: str | None = None
    """Industry the lead belongs to"""
    annual_revenue: float | None = None
    """Annual revenue of the lead's company"""
    no_of_employees: int | None = None
    """Number of employees in the lead's company"""
    rating: str | None = None
    """Lead rating"""
    lead_status: str | None = None
    """Current status of the lead"""
    website: str | None = None
    """Lead's website URL"""
    city: str | None = None
    """Lead's city"""
    state: str | None = None
    """Lead's state or province"""
    country: str | None = None
    """Lead's country"""
    description: str | None = None
    """Description or notes about the lead"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class ContactsSearchData(BaseModel):
    """Search result data for contacts entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    first_name: str | None = None
    """Contact's first name"""
    last_name: str | None = None
    """Contact's last name"""
    full_name: str | None = None
    """Contact's full name"""
    email: str | None = None
    """Contact's email address"""
    phone: str | None = None
    """Contact's phone number"""
    mobile: str | None = None
    """Contact's mobile number"""
    title: str | None = None
    """Contact's job title"""
    department: str | None = None
    """Department the contact belongs to"""
    account_name: dict[str, Any] | None = None
    """Account the contact belongs to, as a lookup object with `name` and `id`"""
    lead_source: str | None = None
    """Source from which the contact was generated"""
    date_of_birth: str | None = None
    """Contact's date of birth"""
    mailing_city: str | None = None
    """Mailing address city"""
    mailing_state: str | None = None
    """Mailing address state or province"""
    mailing_country: str | None = None
    """Mailing address country"""
    description: str | None = None
    """Description or notes about the contact"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class AccountsSearchData(BaseModel):
    """Search result data for accounts entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    account_name: str | None = None
    """Name of the account or company"""
    account_number: str | None = None
    """Account number"""
    account_type: str | None = None
    """Type of account (e.g., Analyst, Competitor, Customer)"""
    industry: str | None = None
    """Industry the account belongs to"""
    annual_revenue: float | None = None
    """Annual revenue of the account"""
    employees: int | None = None
    """Number of employees"""
    phone: str | None = None
    """Account phone number"""
    website: str | None = None
    """Account website URL"""
    ownership: str | None = None
    """Ownership type (e.g., Public, Private)"""
    rating: str | None = None
    """Account rating"""
    billing_city: str | None = None
    """Billing address city"""
    billing_state: str | None = None
    """Billing address state or province"""
    billing_country: str | None = None
    """Billing address country"""
    description: str | None = None
    """Description or notes about the account"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class DealsSearchData(BaseModel):
    """Search result data for deals entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    deal_name: str | None = None
    """Name of the deal"""
    account_name: dict[str, Any] | None = None
    """Account the deal belongs to, as a lookup object with `name` and `id`"""
    amount: float | None = None
    """Monetary value of the deal"""
    stage: str | None = None
    """Current stage of the deal in the pipeline"""
    probability: int | None = None
    """Probability of closing the deal (percentage)"""
    closing_date: str | None = None
    """Expected closing date"""
    type_: str | None = None
    """Type of deal (e.g., New Business, Existing Business)"""
    next_step: str | None = None
    """Next step in the deal process"""
    lead_source: str | None = None
    """Source from which the deal originated"""
    description: str | None = None
    """Description or notes about the deal"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    campaign_name: str | None = None
    """Name of the campaign"""
    type_: str | None = None
    """Type of campaign (e.g., Email, Webinar, Conference)"""
    status: str | None = None
    """Current status of the campaign"""
    start_date: str | None = None
    """Campaign start date"""
    end_date: str | None = None
    """Campaign end date"""
    expected_revenue: float | None = None
    """Expected revenue from the campaign"""
    budgeted_cost: float | None = None
    """Budget allocated for the campaign"""
    actual_cost: float | None = None
    """Actual cost incurred"""
    num_sent: str | None = None
    """Number of campaign messages sent"""
    expected_response: int | None = None
    """Expected response count"""
    description: str | None = None
    """Description or notes about the campaign"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class TasksSearchData(BaseModel):
    """Search result data for tasks entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    subject: str | None = None
    """Subject or title of the task"""
    who_id: dict[str, Any] | None = None
    """Contact or lead the task is with, as a lookup object with `name` and `id`"""
    what_id: dict[str, Any] | None = None
    """Account, deal, or other record the task is linked to, as a lookup object with `name` and `id`"""
    due_date: str | None = None
    """Due date for the task"""
    status: str | None = None
    """Current status (e.g., Not Started, In Progress, Completed)"""
    priority: str | None = None
    """Priority level (e.g., High, Highest, Low, Lowest, Normal)"""
    send_notification_email: bool | None = None
    """Whether to send a notification email"""
    description: str | None = None
    """Description or notes about the task"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""
    closed_time: str | None = None
    """Time the task was closed"""


class EventsSearchData(BaseModel):
    """Search result data for events entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    event_title: str | None = None
    """Title of the event"""
    who_id: dict[str, Any] | None = None
    """Contact or lead invited to the event, as a lookup object with `name` and `id`"""
    what_id: dict[str, Any] | None = None
    """Account, deal, or other record the event is linked to, as a lookup object with `name` and `id`"""
    start_date_time: str | None = None
    """Event start date and time"""
    end_date_time: str | None = None
    """Event end date and time"""
    all_day: bool | None = None
    """Whether this is an all-day event"""
    venue: str | None = None
    """Event location. Zoho names this field `Venue`; there is no `Location` field on the Events module.
"""
    description: str | None = None
    """Description or notes about the event"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class CallsSearchData(BaseModel):
    """Search result data for calls entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    subject: str | None = None
    """Subject of the call"""
    who_id: dict[str, Any] | None = None
    """Contact or lead on the call, as a lookup object with `name` and `id`"""
    what_id: dict[str, Any] | None = None
    """Account, deal, or other record the call is linked to, as a lookup object with `name` and `id`"""
    call_type: str | None = None
    """Type of call (Inbound or Outbound)"""
    call_start_time: str | None = None
    """Start time of the call"""
    call_duration: str | None = None
    """Duration of the call as a formatted string"""
    call_duration_in_seconds: float | None = None
    """Duration of the call in seconds"""
    call_purpose: str | None = None
    """Purpose of the call"""
    call_result: str | None = None
    """Result or outcome of the call"""
    caller_id: str | None = None
    """Caller ID number"""
    call_status: str | None = None
    """Disposition of the call (Missed, Received, Overdue, Scheduled). Zoho names this field `Call_Status`; there is no `Outgoing_Call_Status` field on the Calls module.
"""
    call_agenda: str | None = None
    """Free-text agenda written before the call"""
    description: str | None = None
    """Description or notes about the call"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class ProductsSearchData(BaseModel):
    """Search result data for products entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    product_name: str | None = None
    """Name of the product"""
    product_code: str | None = None
    """Product code or SKU"""
    product_category: str | None = None
    """Category of the product"""
    product_active: bool | None = None
    """Whether the product is active"""
    unit_price: float | None = None
    """Unit price of the product"""
    commission_rate: float | None = None
    """Commission rate for the product"""
    manufacturer: str | None = None
    """Product manufacturer"""
    sales_start_date: str | None = None
    """Date when sales begin"""
    sales_end_date: str | None = None
    """Date when sales end"""
    qty_in_stock: float | None = None
    """Quantity currently in stock"""
    qty_in_demand: float | None = None
    """Quantity in demand"""
    qty_ordered: float | None = None
    """Quantity on order"""
    description: str | None = None
    """Description of the product"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class QuotesSearchData(BaseModel):
    """Search result data for quotes entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    subject: str | None = None
    """Subject or title of the quote"""
    quote_stage: str | None = None
    """Current stage of the quote"""
    valid_till: str | None = None
    """Date until which the quote is valid"""
    carrier: str | None = None
    """Shipping carrier"""
    sub_total: float | None = None
    """Subtotal before tax and adjustments"""
    tax: float | None = None
    """Tax amount"""
    adjustment: float | None = None
    """Adjustment amount"""
    grand_total: float | None = None
    """Total amount including tax and adjustments"""
    discount: float | None = None
    """Discount amount"""
    terms_and_conditions: str | None = None
    """Terms and conditions text"""
    description: str | None = None
    """Description or notes about the quote"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class InvoicesSearchData(BaseModel):
    """Search result data for invoices entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    subject: str | None = None
    """Subject or title of the invoice"""
    invoice_number: str | None = None
    """Invoice number"""
    invoice_date: str | None = None
    """Date the invoice was issued"""
    due_date: str | None = None
    """Payment due date"""
    status: str | None = None
    """Current status of the invoice"""
    purchase_order: str | None = None
    """Associated purchase order number"""
    sub_total: float | None = None
    """Subtotal before tax and adjustments"""
    tax: float | None = None
    """Tax amount"""
    adjustment: float | None = None
    """Adjustment amount"""
    grand_total: float | None = None
    """Total amount including tax and adjustments"""
    discount: float | None = None
    """Discount amount"""
    excise_duty: float | None = None
    """Excise duty amount"""
    terms_and_conditions: str | None = None
    """Terms and conditions text"""
    description: str | None = None
    """Description or notes about the invoice"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


class NotesSearchData(BaseModel):
    """Search result data for notes entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique record identifier"""
    note_content: str | None = None
    """Body of the note. This is where rep-authored free text actually accumulates in Zoho CRM -- notes attach to any module record and, unlike the per-record `Description` textarea, are mandatory content by construction.
"""
    note_title: str | None = None
    """Optional short title for the note"""
    parent_id: dict[str, Any] | None = None
    """Record the note is attached to, as a lookup object with `name` and `id`"""
    created_time: str | None = None
    """Time the record was created"""
    modified_time: str | None = None
    """Time the record was last modified"""


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

LeadsSearchResult = AirbyteSearchResult[LeadsSearchData]
"""Search result type for leads entity."""

ContactsSearchResult = AirbyteSearchResult[ContactsSearchData]
"""Search result type for contacts entity."""

AccountsSearchResult = AirbyteSearchResult[AccountsSearchData]
"""Search result type for accounts entity."""

DealsSearchResult = AirbyteSearchResult[DealsSearchData]
"""Search result type for deals entity."""

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

TasksSearchResult = AirbyteSearchResult[TasksSearchData]
"""Search result type for tasks entity."""

EventsSearchResult = AirbyteSearchResult[EventsSearchData]
"""Search result type for events entity."""

CallsSearchResult = AirbyteSearchResult[CallsSearchData]
"""Search result type for calls entity."""

ProductsSearchResult = AirbyteSearchResult[ProductsSearchData]
"""Search result type for products entity."""

QuotesSearchResult = AirbyteSearchResult[QuotesSearchData]
"""Search result type for quotes entity."""

InvoicesSearchResult = AirbyteSearchResult[InvoicesSearchData]
"""Search result type for invoices entity."""

NotesSearchResult = AirbyteSearchResult[NotesSearchData]
"""Search result type for notes entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

LeadsListResult = ZohoCrmExecuteResultWithMeta[list[Lead], LeadsListResultMeta]
"""Result type for leads.list operation with data and metadata."""

ContactsListResult = ZohoCrmExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

AccountsListResult = ZohoCrmExecuteResultWithMeta[list[Account], AccountsListResultMeta]
"""Result type for accounts.list operation with data and metadata."""

DealsListResult = ZohoCrmExecuteResultWithMeta[list[Deal], DealsListResultMeta]
"""Result type for deals.list operation with data and metadata."""

CampaignsListResult = ZohoCrmExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

TasksListResult = ZohoCrmExecuteResultWithMeta[list[Task], TasksListResultMeta]
"""Result type for tasks.list operation with data and metadata."""

EventsListResult = ZohoCrmExecuteResultWithMeta[list[Event], EventsListResultMeta]
"""Result type for events.list operation with data and metadata."""

CallsListResult = ZohoCrmExecuteResultWithMeta[list[Call], CallsListResultMeta]
"""Result type for calls.list operation with data and metadata."""

ProductsListResult = ZohoCrmExecuteResultWithMeta[list[Product], ProductsListResultMeta]
"""Result type for products.list operation with data and metadata."""

QuotesListResult = ZohoCrmExecuteResultWithMeta[list[Quote], QuotesListResultMeta]
"""Result type for quotes.list operation with data and metadata."""

InvoicesListResult = ZohoCrmExecuteResultWithMeta[list[Invoice], InvoicesListResultMeta]
"""Result type for invoices.list operation with data and metadata."""

NotesListResult = ZohoCrmExecuteResultWithMeta[list[Note], NotesListResultMeta]
"""Result type for notes.list operation with data and metadata."""

