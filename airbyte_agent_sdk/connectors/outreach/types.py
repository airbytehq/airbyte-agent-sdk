"""
Type definitions for outreach connector.
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

class ProspectsListParams(TypedDict):
    """Parameters for prospects.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class ProspectsGetParams(TypedDict):
    """Parameters for prospects.get operation"""
    id: str

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    id: str

class SequencesListParams(TypedDict):
    """Parameters for sequences.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class SequencesGetParams(TypedDict):
    """Parameters for sequences.get operation"""
    id: str

class SequenceStatesListParams(TypedDict):
    """Parameters for sequence_states.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class SequenceStatesGetParams(TypedDict):
    """Parameters for sequence_states.get operation"""
    id: str

class SequenceStepsListParams(TypedDict):
    """Parameters for sequence_steps.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class SequenceStepsGetParams(TypedDict):
    """Parameters for sequence_steps.get operation"""
    id: str

class OpportunitiesListParams(TypedDict):
    """Parameters for opportunities.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class OpportunitiesGetParams(TypedDict):
    """Parameters for opportunities.get operation"""
    id: str

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class CallsGetParams(TypedDict):
    """Parameters for calls.get operation"""
    id: str

class CallDispositionsListParams(TypedDict):
    """Parameters for call_dispositions.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class CallDispositionsGetParams(TypedDict):
    """Parameters for call_dispositions.get operation"""
    id: str

class CallPurposesListParams(TypedDict):
    """Parameters for call_purposes.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class CallPurposesGetParams(TypedDict):
    """Parameters for call_purposes.get operation"""
    id: str

class MailingsListParams(TypedDict):
    """Parameters for mailings.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class MailingsGetParams(TypedDict):
    """Parameters for mailings.get operation"""
    id: str

class MailboxesListParams(TypedDict):
    """Parameters for mailboxes.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class MailboxesGetParams(TypedDict):
    """Parameters for mailboxes.get operation"""
    id: str

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    id: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class StagesListParams(TypedDict):
    """Parameters for stages.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class StagesGetParams(TypedDict):
    """Parameters for stages.get operation"""
    id: str

class PersonasListParams(TypedDict):
    """Parameters for personas.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class PersonasGetParams(TypedDict):
    """Parameters for personas.get operation"""
    id: str

class TemplatesListParams(TypedDict):
    """Parameters for templates.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class TemplatesGetParams(TypedDict):
    """Parameters for templates.get operation"""
    id: str

class SnippetsListParams(TypedDict):
    """Parameters for snippets.list operation"""
    page_size: NotRequired[int]
    sort: NotRequired[str]
    count: NotRequired[str]
    page_after: NotRequired[str]

class SnippetsGetParams(TypedDict):
    """Parameters for snippets.get operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ACCOUNTS SEARCH TYPES =====

class AccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering accounts search queries."""
    assigned_teams: list[Any] | None
    """Assigned teams"""
    assigned_users: list[Any] | None
    """Assigned users"""
    batches: list[Any] | None
    """Batches"""
    buyer_intent_score: float | None
    """Buyer intent score"""
    company_type: str | None
    """Company type"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    custom1: str | None
    """Custom field 1"""
    custom10: str | None
    """Custom field 10"""
    custom100: str | None
    """Custom field 100"""
    custom101: str | None
    """Custom field 101"""
    custom102: str | None
    """Custom field 102"""
    custom103: str | None
    """Custom field 103"""
    custom104: str | None
    """Custom field 104"""
    custom105: str | None
    """Custom field 105"""
    custom106: str | None
    """Custom field 106"""
    custom107: str | None
    """Custom field 107"""
    custom108: str | None
    """Custom field 108"""
    custom109: str | None
    """Custom field 109"""
    custom11: str | None
    """Custom field 11"""
    custom110: str | None
    """Custom field 110"""
    custom111: str | None
    """Custom field 111"""
    custom112: str | None
    """Custom field 112"""
    custom113: str | None
    """Custom field 113"""
    custom114: str | None
    """Custom field 114"""
    custom115: str | None
    """Custom field 115"""
    custom116: str | None
    """Custom field 116"""
    custom117: str | None
    """Custom field 117"""
    custom118: str | None
    """Custom field 118"""
    custom119: str | None
    """Custom field 119"""
    custom12: str | None
    """Custom field 12"""
    custom120: str | None
    """Custom field 120"""
    custom121: str | None
    """Custom field 121"""
    custom122: str | None
    """Custom field 122"""
    custom123: str | None
    """Custom field 123"""
    custom124: str | None
    """Custom field 124"""
    custom125: str | None
    """Custom field 125"""
    custom126: str | None
    """Custom field 126"""
    custom127: str | None
    """Custom field 127"""
    custom128: str | None
    """Custom field 128"""
    custom129: str | None
    """Custom field 129"""
    custom13: str | None
    """Custom field 13"""
    custom130: str | None
    """Custom field 130"""
    custom131: str | None
    """Custom field 131"""
    custom132: str | None
    """Custom field 132"""
    custom133: str | None
    """Custom field 133"""
    custom134: str | None
    """Custom field 134"""
    custom135: str | None
    """Custom field 135"""
    custom136: str | None
    """Custom field 136"""
    custom137: str | None
    """Custom field 137"""
    custom138: str | None
    """Custom field 138"""
    custom139: str | None
    """Custom field 139"""
    custom14: str | None
    """Custom field 14"""
    custom140: str | None
    """Custom field 140"""
    custom141: str | None
    """Custom field 141"""
    custom142: str | None
    """Custom field 142"""
    custom143: str | None
    """Custom field 143"""
    custom144: str | None
    """Custom field 144"""
    custom145: str | None
    """Custom field 145"""
    custom146: str | None
    """Custom field 146"""
    custom147: str | None
    """Custom field 147"""
    custom148: str | None
    """Custom field 148"""
    custom149: str | None
    """Custom field 149"""
    custom15: str | None
    """Custom field 15"""
    custom150: str | None
    """Custom field 150"""
    custom16: str | None
    """Custom field 16"""
    custom17: str | None
    """Custom field 17"""
    custom18: str | None
    """Custom field 18"""
    custom19: str | None
    """Custom field 19"""
    custom2: str | None
    """Custom field 2"""
    custom20: str | None
    """Custom field 20"""
    custom21: str | None
    """Custom field 21"""
    custom22: str | None
    """Custom field 22"""
    custom23: str | None
    """Custom field 23"""
    custom24: str | None
    """Custom field 24"""
    custom25: str | None
    """Custom field 25"""
    custom26: str | None
    """Custom field 26"""
    custom27: str | None
    """Custom field 27"""
    custom28: str | None
    """Custom field 28"""
    custom29: str | None
    """Custom field 29"""
    custom3: str | None
    """Custom field 3"""
    custom30: str | None
    """Custom field 30"""
    custom31: str | None
    """Custom field 31"""
    custom32: str | None
    """Custom field 32"""
    custom33: str | None
    """Custom field 33"""
    custom34: str | None
    """Custom field 34"""
    custom35: str | None
    """Custom field 35"""
    custom36: str | None
    """Custom field 36"""
    custom37: str | None
    """Custom field 37"""
    custom38: str | None
    """Custom field 38"""
    custom39: str | None
    """Custom field 39"""
    custom4: str | None
    """Custom field 4"""
    custom40: str | None
    """Custom field 40"""
    custom41: str | None
    """Custom field 41"""
    custom42: str | None
    """Custom field 42"""
    custom43: str | None
    """Custom field 43"""
    custom44: str | None
    """Custom field 44"""
    custom45: str | None
    """Custom field 45"""
    custom46: str | None
    """Custom field 46"""
    custom47: str | None
    """Custom field 47"""
    custom48: str | None
    """Custom field 48"""
    custom49: str | None
    """Custom field 49"""
    custom5: str | None
    """Custom field 5"""
    custom50: str | None
    """Custom field 50"""
    custom51: str | None
    """Custom field 51"""
    custom52: str | None
    """Custom field 52"""
    custom53: str | None
    """Custom field 53"""
    custom54: str | None
    """Custom field 54"""
    custom55: str | None
    """Custom field 55"""
    custom56: str | None
    """Custom field 56"""
    custom57: str | None
    """Custom field 57"""
    custom58: str | None
    """Custom field 58"""
    custom59: str | None
    """Custom field 59"""
    custom6: str | None
    """Custom field 6"""
    custom60: str | None
    """Custom field 60"""
    custom61: str | None
    """Custom field 61"""
    custom62: str | None
    """Custom field 62"""
    custom63: str | None
    """Custom field 63"""
    custom64: str | None
    """Custom field 64"""
    custom65: str | None
    """Custom field 65"""
    custom66: str | None
    """Custom field 66"""
    custom67: str | None
    """Custom field 67"""
    custom68: str | None
    """Custom field 68"""
    custom69: str | None
    """Custom field 69"""
    custom7: str | None
    """Custom field 7"""
    custom70: str | None
    """Custom field 70"""
    custom71: str | None
    """Custom field 71"""
    custom72: str | None
    """Custom field 72"""
    custom73: str | None
    """Custom field 73"""
    custom74: str | None
    """Custom field 74"""
    custom75: str | None
    """Custom field 75"""
    custom76: str | None
    """Custom field 76"""
    custom77: str | None
    """Custom field 77"""
    custom78: str | None
    """Custom field 78"""
    custom79: str | None
    """Custom field 79"""
    custom8: str | None
    """Custom field 8"""
    custom80: str | None
    """Custom field 80"""
    custom81: str | None
    """Custom field 81"""
    custom82: str | None
    """Custom field 82"""
    custom83: str | None
    """Custom field 83"""
    custom84: str | None
    """Custom field 84"""
    custom85: str | None
    """Custom field 85"""
    custom86: str | None
    """Custom field 86"""
    custom87: str | None
    """Custom field 87"""
    custom88: str | None
    """Custom field 88"""
    custom89: str | None
    """Custom field 89"""
    custom9: str | None
    """Custom field 9"""
    custom90: str | None
    """Custom field 90"""
    custom91: str | None
    """Custom field 91"""
    custom92: str | None
    """Custom field 92"""
    custom93: str | None
    """Custom field 93"""
    custom94: str | None
    """Custom field 94"""
    custom95: str | None
    """Custom field 95"""
    custom96: str | None
    """Custom field 96"""
    custom97: str | None
    """Custom field 97"""
    custom98: str | None
    """Custom field 98"""
    custom99: str | None
    """Custom field 99"""
    custom_id: str | None
    """Custom id"""
    default_plugin_mapping: list[Any] | None
    """Default plugin mapping"""
    description: str | None
    """Description"""
    domain: str | None
    """Domain"""
    external_source: str | None
    """External source"""
    favorites: list[Any] | None
    """Favorites"""
    followers: int | None
    """Followers"""
    founded_at: str | None
    """Founded at"""
    id: int | None
    """Unique account identifier"""
    industry: str | None
    """Industry"""
    linked_in_employees: int | None
    """Linked in employees"""
    linked_in_url: str | None
    """Linked in url"""
    locality: str | None
    """Locality"""
    name: str | None
    """Name"""
    named: bool | None
    """Named"""
    natural_name: str | None
    """Natural name"""
    number_of_employees: int | None
    """Number of employees"""
    owner: list[Any] | None
    """Owner"""
    prospects: list[Any] | None
    """Prospects"""
    sharing_team_id: str | None
    """Sharing team id"""
    tags: list[Any] | None
    """Tags"""
    tasks: list[Any] | None
    """Tasks"""
    touched_at: str | None
    """Touched at"""
    trashed_at: str | None
    """Trashed at"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""
    website_url: str | None
    """Website url"""


class AccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    assigned_teams: list[list[Any]]
    """Assigned teams"""
    assigned_users: list[list[Any]]
    """Assigned users"""
    batches: list[list[Any]]
    """Batches"""
    buyer_intent_score: list[float]
    """Buyer intent score"""
    company_type: list[str]
    """Company type"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    custom1: list[str]
    """Custom field 1"""
    custom10: list[str]
    """Custom field 10"""
    custom100: list[str]
    """Custom field 100"""
    custom101: list[str]
    """Custom field 101"""
    custom102: list[str]
    """Custom field 102"""
    custom103: list[str]
    """Custom field 103"""
    custom104: list[str]
    """Custom field 104"""
    custom105: list[str]
    """Custom field 105"""
    custom106: list[str]
    """Custom field 106"""
    custom107: list[str]
    """Custom field 107"""
    custom108: list[str]
    """Custom field 108"""
    custom109: list[str]
    """Custom field 109"""
    custom11: list[str]
    """Custom field 11"""
    custom110: list[str]
    """Custom field 110"""
    custom111: list[str]
    """Custom field 111"""
    custom112: list[str]
    """Custom field 112"""
    custom113: list[str]
    """Custom field 113"""
    custom114: list[str]
    """Custom field 114"""
    custom115: list[str]
    """Custom field 115"""
    custom116: list[str]
    """Custom field 116"""
    custom117: list[str]
    """Custom field 117"""
    custom118: list[str]
    """Custom field 118"""
    custom119: list[str]
    """Custom field 119"""
    custom12: list[str]
    """Custom field 12"""
    custom120: list[str]
    """Custom field 120"""
    custom121: list[str]
    """Custom field 121"""
    custom122: list[str]
    """Custom field 122"""
    custom123: list[str]
    """Custom field 123"""
    custom124: list[str]
    """Custom field 124"""
    custom125: list[str]
    """Custom field 125"""
    custom126: list[str]
    """Custom field 126"""
    custom127: list[str]
    """Custom field 127"""
    custom128: list[str]
    """Custom field 128"""
    custom129: list[str]
    """Custom field 129"""
    custom13: list[str]
    """Custom field 13"""
    custom130: list[str]
    """Custom field 130"""
    custom131: list[str]
    """Custom field 131"""
    custom132: list[str]
    """Custom field 132"""
    custom133: list[str]
    """Custom field 133"""
    custom134: list[str]
    """Custom field 134"""
    custom135: list[str]
    """Custom field 135"""
    custom136: list[str]
    """Custom field 136"""
    custom137: list[str]
    """Custom field 137"""
    custom138: list[str]
    """Custom field 138"""
    custom139: list[str]
    """Custom field 139"""
    custom14: list[str]
    """Custom field 14"""
    custom140: list[str]
    """Custom field 140"""
    custom141: list[str]
    """Custom field 141"""
    custom142: list[str]
    """Custom field 142"""
    custom143: list[str]
    """Custom field 143"""
    custom144: list[str]
    """Custom field 144"""
    custom145: list[str]
    """Custom field 145"""
    custom146: list[str]
    """Custom field 146"""
    custom147: list[str]
    """Custom field 147"""
    custom148: list[str]
    """Custom field 148"""
    custom149: list[str]
    """Custom field 149"""
    custom15: list[str]
    """Custom field 15"""
    custom150: list[str]
    """Custom field 150"""
    custom16: list[str]
    """Custom field 16"""
    custom17: list[str]
    """Custom field 17"""
    custom18: list[str]
    """Custom field 18"""
    custom19: list[str]
    """Custom field 19"""
    custom2: list[str]
    """Custom field 2"""
    custom20: list[str]
    """Custom field 20"""
    custom21: list[str]
    """Custom field 21"""
    custom22: list[str]
    """Custom field 22"""
    custom23: list[str]
    """Custom field 23"""
    custom24: list[str]
    """Custom field 24"""
    custom25: list[str]
    """Custom field 25"""
    custom26: list[str]
    """Custom field 26"""
    custom27: list[str]
    """Custom field 27"""
    custom28: list[str]
    """Custom field 28"""
    custom29: list[str]
    """Custom field 29"""
    custom3: list[str]
    """Custom field 3"""
    custom30: list[str]
    """Custom field 30"""
    custom31: list[str]
    """Custom field 31"""
    custom32: list[str]
    """Custom field 32"""
    custom33: list[str]
    """Custom field 33"""
    custom34: list[str]
    """Custom field 34"""
    custom35: list[str]
    """Custom field 35"""
    custom36: list[str]
    """Custom field 36"""
    custom37: list[str]
    """Custom field 37"""
    custom38: list[str]
    """Custom field 38"""
    custom39: list[str]
    """Custom field 39"""
    custom4: list[str]
    """Custom field 4"""
    custom40: list[str]
    """Custom field 40"""
    custom41: list[str]
    """Custom field 41"""
    custom42: list[str]
    """Custom field 42"""
    custom43: list[str]
    """Custom field 43"""
    custom44: list[str]
    """Custom field 44"""
    custom45: list[str]
    """Custom field 45"""
    custom46: list[str]
    """Custom field 46"""
    custom47: list[str]
    """Custom field 47"""
    custom48: list[str]
    """Custom field 48"""
    custom49: list[str]
    """Custom field 49"""
    custom5: list[str]
    """Custom field 5"""
    custom50: list[str]
    """Custom field 50"""
    custom51: list[str]
    """Custom field 51"""
    custom52: list[str]
    """Custom field 52"""
    custom53: list[str]
    """Custom field 53"""
    custom54: list[str]
    """Custom field 54"""
    custom55: list[str]
    """Custom field 55"""
    custom56: list[str]
    """Custom field 56"""
    custom57: list[str]
    """Custom field 57"""
    custom58: list[str]
    """Custom field 58"""
    custom59: list[str]
    """Custom field 59"""
    custom6: list[str]
    """Custom field 6"""
    custom60: list[str]
    """Custom field 60"""
    custom61: list[str]
    """Custom field 61"""
    custom62: list[str]
    """Custom field 62"""
    custom63: list[str]
    """Custom field 63"""
    custom64: list[str]
    """Custom field 64"""
    custom65: list[str]
    """Custom field 65"""
    custom66: list[str]
    """Custom field 66"""
    custom67: list[str]
    """Custom field 67"""
    custom68: list[str]
    """Custom field 68"""
    custom69: list[str]
    """Custom field 69"""
    custom7: list[str]
    """Custom field 7"""
    custom70: list[str]
    """Custom field 70"""
    custom71: list[str]
    """Custom field 71"""
    custom72: list[str]
    """Custom field 72"""
    custom73: list[str]
    """Custom field 73"""
    custom74: list[str]
    """Custom field 74"""
    custom75: list[str]
    """Custom field 75"""
    custom76: list[str]
    """Custom field 76"""
    custom77: list[str]
    """Custom field 77"""
    custom78: list[str]
    """Custom field 78"""
    custom79: list[str]
    """Custom field 79"""
    custom8: list[str]
    """Custom field 8"""
    custom80: list[str]
    """Custom field 80"""
    custom81: list[str]
    """Custom field 81"""
    custom82: list[str]
    """Custom field 82"""
    custom83: list[str]
    """Custom field 83"""
    custom84: list[str]
    """Custom field 84"""
    custom85: list[str]
    """Custom field 85"""
    custom86: list[str]
    """Custom field 86"""
    custom87: list[str]
    """Custom field 87"""
    custom88: list[str]
    """Custom field 88"""
    custom89: list[str]
    """Custom field 89"""
    custom9: list[str]
    """Custom field 9"""
    custom90: list[str]
    """Custom field 90"""
    custom91: list[str]
    """Custom field 91"""
    custom92: list[str]
    """Custom field 92"""
    custom93: list[str]
    """Custom field 93"""
    custom94: list[str]
    """Custom field 94"""
    custom95: list[str]
    """Custom field 95"""
    custom96: list[str]
    """Custom field 96"""
    custom97: list[str]
    """Custom field 97"""
    custom98: list[str]
    """Custom field 98"""
    custom99: list[str]
    """Custom field 99"""
    custom_id: list[str]
    """Custom id"""
    default_plugin_mapping: list[list[Any]]
    """Default plugin mapping"""
    description: list[str]
    """Description"""
    domain: list[str]
    """Domain"""
    external_source: list[str]
    """External source"""
    favorites: list[list[Any]]
    """Favorites"""
    followers: list[int]
    """Followers"""
    founded_at: list[str]
    """Founded at"""
    id: list[int]
    """Unique account identifier"""
    industry: list[str]
    """Industry"""
    linked_in_employees: list[int]
    """Linked in employees"""
    linked_in_url: list[str]
    """Linked in url"""
    locality: list[str]
    """Locality"""
    name: list[str]
    """Name"""
    named: list[bool]
    """Named"""
    natural_name: list[str]
    """Natural name"""
    number_of_employees: list[int]
    """Number of employees"""
    owner: list[list[Any]]
    """Owner"""
    prospects: list[list[Any]]
    """Prospects"""
    sharing_team_id: list[str]
    """Sharing team id"""
    tags: list[list[Any]]
    """Tags"""
    tasks: list[list[Any]]
    """Tasks"""
    touched_at: list[str]
    """Touched at"""
    trashed_at: list[str]
    """Trashed at"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""
    website_url: list[str]
    """Website url"""


class AccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    assigned_teams: Any
    """Assigned teams"""
    assigned_users: Any
    """Assigned users"""
    batches: Any
    """Batches"""
    buyer_intent_score: Any
    """Buyer intent score"""
    company_type: Any
    """Company type"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    custom1: Any
    """Custom field 1"""
    custom10: Any
    """Custom field 10"""
    custom100: Any
    """Custom field 100"""
    custom101: Any
    """Custom field 101"""
    custom102: Any
    """Custom field 102"""
    custom103: Any
    """Custom field 103"""
    custom104: Any
    """Custom field 104"""
    custom105: Any
    """Custom field 105"""
    custom106: Any
    """Custom field 106"""
    custom107: Any
    """Custom field 107"""
    custom108: Any
    """Custom field 108"""
    custom109: Any
    """Custom field 109"""
    custom11: Any
    """Custom field 11"""
    custom110: Any
    """Custom field 110"""
    custom111: Any
    """Custom field 111"""
    custom112: Any
    """Custom field 112"""
    custom113: Any
    """Custom field 113"""
    custom114: Any
    """Custom field 114"""
    custom115: Any
    """Custom field 115"""
    custom116: Any
    """Custom field 116"""
    custom117: Any
    """Custom field 117"""
    custom118: Any
    """Custom field 118"""
    custom119: Any
    """Custom field 119"""
    custom12: Any
    """Custom field 12"""
    custom120: Any
    """Custom field 120"""
    custom121: Any
    """Custom field 121"""
    custom122: Any
    """Custom field 122"""
    custom123: Any
    """Custom field 123"""
    custom124: Any
    """Custom field 124"""
    custom125: Any
    """Custom field 125"""
    custom126: Any
    """Custom field 126"""
    custom127: Any
    """Custom field 127"""
    custom128: Any
    """Custom field 128"""
    custom129: Any
    """Custom field 129"""
    custom13: Any
    """Custom field 13"""
    custom130: Any
    """Custom field 130"""
    custom131: Any
    """Custom field 131"""
    custom132: Any
    """Custom field 132"""
    custom133: Any
    """Custom field 133"""
    custom134: Any
    """Custom field 134"""
    custom135: Any
    """Custom field 135"""
    custom136: Any
    """Custom field 136"""
    custom137: Any
    """Custom field 137"""
    custom138: Any
    """Custom field 138"""
    custom139: Any
    """Custom field 139"""
    custom14: Any
    """Custom field 14"""
    custom140: Any
    """Custom field 140"""
    custom141: Any
    """Custom field 141"""
    custom142: Any
    """Custom field 142"""
    custom143: Any
    """Custom field 143"""
    custom144: Any
    """Custom field 144"""
    custom145: Any
    """Custom field 145"""
    custom146: Any
    """Custom field 146"""
    custom147: Any
    """Custom field 147"""
    custom148: Any
    """Custom field 148"""
    custom149: Any
    """Custom field 149"""
    custom15: Any
    """Custom field 15"""
    custom150: Any
    """Custom field 150"""
    custom16: Any
    """Custom field 16"""
    custom17: Any
    """Custom field 17"""
    custom18: Any
    """Custom field 18"""
    custom19: Any
    """Custom field 19"""
    custom2: Any
    """Custom field 2"""
    custom20: Any
    """Custom field 20"""
    custom21: Any
    """Custom field 21"""
    custom22: Any
    """Custom field 22"""
    custom23: Any
    """Custom field 23"""
    custom24: Any
    """Custom field 24"""
    custom25: Any
    """Custom field 25"""
    custom26: Any
    """Custom field 26"""
    custom27: Any
    """Custom field 27"""
    custom28: Any
    """Custom field 28"""
    custom29: Any
    """Custom field 29"""
    custom3: Any
    """Custom field 3"""
    custom30: Any
    """Custom field 30"""
    custom31: Any
    """Custom field 31"""
    custom32: Any
    """Custom field 32"""
    custom33: Any
    """Custom field 33"""
    custom34: Any
    """Custom field 34"""
    custom35: Any
    """Custom field 35"""
    custom36: Any
    """Custom field 36"""
    custom37: Any
    """Custom field 37"""
    custom38: Any
    """Custom field 38"""
    custom39: Any
    """Custom field 39"""
    custom4: Any
    """Custom field 4"""
    custom40: Any
    """Custom field 40"""
    custom41: Any
    """Custom field 41"""
    custom42: Any
    """Custom field 42"""
    custom43: Any
    """Custom field 43"""
    custom44: Any
    """Custom field 44"""
    custom45: Any
    """Custom field 45"""
    custom46: Any
    """Custom field 46"""
    custom47: Any
    """Custom field 47"""
    custom48: Any
    """Custom field 48"""
    custom49: Any
    """Custom field 49"""
    custom5: Any
    """Custom field 5"""
    custom50: Any
    """Custom field 50"""
    custom51: Any
    """Custom field 51"""
    custom52: Any
    """Custom field 52"""
    custom53: Any
    """Custom field 53"""
    custom54: Any
    """Custom field 54"""
    custom55: Any
    """Custom field 55"""
    custom56: Any
    """Custom field 56"""
    custom57: Any
    """Custom field 57"""
    custom58: Any
    """Custom field 58"""
    custom59: Any
    """Custom field 59"""
    custom6: Any
    """Custom field 6"""
    custom60: Any
    """Custom field 60"""
    custom61: Any
    """Custom field 61"""
    custom62: Any
    """Custom field 62"""
    custom63: Any
    """Custom field 63"""
    custom64: Any
    """Custom field 64"""
    custom65: Any
    """Custom field 65"""
    custom66: Any
    """Custom field 66"""
    custom67: Any
    """Custom field 67"""
    custom68: Any
    """Custom field 68"""
    custom69: Any
    """Custom field 69"""
    custom7: Any
    """Custom field 7"""
    custom70: Any
    """Custom field 70"""
    custom71: Any
    """Custom field 71"""
    custom72: Any
    """Custom field 72"""
    custom73: Any
    """Custom field 73"""
    custom74: Any
    """Custom field 74"""
    custom75: Any
    """Custom field 75"""
    custom76: Any
    """Custom field 76"""
    custom77: Any
    """Custom field 77"""
    custom78: Any
    """Custom field 78"""
    custom79: Any
    """Custom field 79"""
    custom8: Any
    """Custom field 8"""
    custom80: Any
    """Custom field 80"""
    custom81: Any
    """Custom field 81"""
    custom82: Any
    """Custom field 82"""
    custom83: Any
    """Custom field 83"""
    custom84: Any
    """Custom field 84"""
    custom85: Any
    """Custom field 85"""
    custom86: Any
    """Custom field 86"""
    custom87: Any
    """Custom field 87"""
    custom88: Any
    """Custom field 88"""
    custom89: Any
    """Custom field 89"""
    custom9: Any
    """Custom field 9"""
    custom90: Any
    """Custom field 90"""
    custom91: Any
    """Custom field 91"""
    custom92: Any
    """Custom field 92"""
    custom93: Any
    """Custom field 93"""
    custom94: Any
    """Custom field 94"""
    custom95: Any
    """Custom field 95"""
    custom96: Any
    """Custom field 96"""
    custom97: Any
    """Custom field 97"""
    custom98: Any
    """Custom field 98"""
    custom99: Any
    """Custom field 99"""
    custom_id: Any
    """Custom id"""
    default_plugin_mapping: Any
    """Default plugin mapping"""
    description: Any
    """Description"""
    domain: Any
    """Domain"""
    external_source: Any
    """External source"""
    favorites: Any
    """Favorites"""
    followers: Any
    """Followers"""
    founded_at: Any
    """Founded at"""
    id: Any
    """Unique account identifier"""
    industry: Any
    """Industry"""
    linked_in_employees: Any
    """Linked in employees"""
    linked_in_url: Any
    """Linked in url"""
    locality: Any
    """Locality"""
    name: Any
    """Name"""
    named: Any
    """Named"""
    natural_name: Any
    """Natural name"""
    number_of_employees: Any
    """Number of employees"""
    owner: Any
    """Owner"""
    prospects: Any
    """Prospects"""
    sharing_team_id: Any
    """Sharing team id"""
    tags: Any
    """Tags"""
    tasks: Any
    """Tasks"""
    touched_at: Any
    """Touched at"""
    trashed_at: Any
    """Trashed at"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""
    website_url: Any
    """Website url"""


class AccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    assigned_teams: str
    """Assigned teams"""
    assigned_users: str
    """Assigned users"""
    batches: str
    """Batches"""
    buyer_intent_score: str
    """Buyer intent score"""
    company_type: str
    """Company type"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    custom1: str
    """Custom field 1"""
    custom10: str
    """Custom field 10"""
    custom100: str
    """Custom field 100"""
    custom101: str
    """Custom field 101"""
    custom102: str
    """Custom field 102"""
    custom103: str
    """Custom field 103"""
    custom104: str
    """Custom field 104"""
    custom105: str
    """Custom field 105"""
    custom106: str
    """Custom field 106"""
    custom107: str
    """Custom field 107"""
    custom108: str
    """Custom field 108"""
    custom109: str
    """Custom field 109"""
    custom11: str
    """Custom field 11"""
    custom110: str
    """Custom field 110"""
    custom111: str
    """Custom field 111"""
    custom112: str
    """Custom field 112"""
    custom113: str
    """Custom field 113"""
    custom114: str
    """Custom field 114"""
    custom115: str
    """Custom field 115"""
    custom116: str
    """Custom field 116"""
    custom117: str
    """Custom field 117"""
    custom118: str
    """Custom field 118"""
    custom119: str
    """Custom field 119"""
    custom12: str
    """Custom field 12"""
    custom120: str
    """Custom field 120"""
    custom121: str
    """Custom field 121"""
    custom122: str
    """Custom field 122"""
    custom123: str
    """Custom field 123"""
    custom124: str
    """Custom field 124"""
    custom125: str
    """Custom field 125"""
    custom126: str
    """Custom field 126"""
    custom127: str
    """Custom field 127"""
    custom128: str
    """Custom field 128"""
    custom129: str
    """Custom field 129"""
    custom13: str
    """Custom field 13"""
    custom130: str
    """Custom field 130"""
    custom131: str
    """Custom field 131"""
    custom132: str
    """Custom field 132"""
    custom133: str
    """Custom field 133"""
    custom134: str
    """Custom field 134"""
    custom135: str
    """Custom field 135"""
    custom136: str
    """Custom field 136"""
    custom137: str
    """Custom field 137"""
    custom138: str
    """Custom field 138"""
    custom139: str
    """Custom field 139"""
    custom14: str
    """Custom field 14"""
    custom140: str
    """Custom field 140"""
    custom141: str
    """Custom field 141"""
    custom142: str
    """Custom field 142"""
    custom143: str
    """Custom field 143"""
    custom144: str
    """Custom field 144"""
    custom145: str
    """Custom field 145"""
    custom146: str
    """Custom field 146"""
    custom147: str
    """Custom field 147"""
    custom148: str
    """Custom field 148"""
    custom149: str
    """Custom field 149"""
    custom15: str
    """Custom field 15"""
    custom150: str
    """Custom field 150"""
    custom16: str
    """Custom field 16"""
    custom17: str
    """Custom field 17"""
    custom18: str
    """Custom field 18"""
    custom19: str
    """Custom field 19"""
    custom2: str
    """Custom field 2"""
    custom20: str
    """Custom field 20"""
    custom21: str
    """Custom field 21"""
    custom22: str
    """Custom field 22"""
    custom23: str
    """Custom field 23"""
    custom24: str
    """Custom field 24"""
    custom25: str
    """Custom field 25"""
    custom26: str
    """Custom field 26"""
    custom27: str
    """Custom field 27"""
    custom28: str
    """Custom field 28"""
    custom29: str
    """Custom field 29"""
    custom3: str
    """Custom field 3"""
    custom30: str
    """Custom field 30"""
    custom31: str
    """Custom field 31"""
    custom32: str
    """Custom field 32"""
    custom33: str
    """Custom field 33"""
    custom34: str
    """Custom field 34"""
    custom35: str
    """Custom field 35"""
    custom36: str
    """Custom field 36"""
    custom37: str
    """Custom field 37"""
    custom38: str
    """Custom field 38"""
    custom39: str
    """Custom field 39"""
    custom4: str
    """Custom field 4"""
    custom40: str
    """Custom field 40"""
    custom41: str
    """Custom field 41"""
    custom42: str
    """Custom field 42"""
    custom43: str
    """Custom field 43"""
    custom44: str
    """Custom field 44"""
    custom45: str
    """Custom field 45"""
    custom46: str
    """Custom field 46"""
    custom47: str
    """Custom field 47"""
    custom48: str
    """Custom field 48"""
    custom49: str
    """Custom field 49"""
    custom5: str
    """Custom field 5"""
    custom50: str
    """Custom field 50"""
    custom51: str
    """Custom field 51"""
    custom52: str
    """Custom field 52"""
    custom53: str
    """Custom field 53"""
    custom54: str
    """Custom field 54"""
    custom55: str
    """Custom field 55"""
    custom56: str
    """Custom field 56"""
    custom57: str
    """Custom field 57"""
    custom58: str
    """Custom field 58"""
    custom59: str
    """Custom field 59"""
    custom6: str
    """Custom field 6"""
    custom60: str
    """Custom field 60"""
    custom61: str
    """Custom field 61"""
    custom62: str
    """Custom field 62"""
    custom63: str
    """Custom field 63"""
    custom64: str
    """Custom field 64"""
    custom65: str
    """Custom field 65"""
    custom66: str
    """Custom field 66"""
    custom67: str
    """Custom field 67"""
    custom68: str
    """Custom field 68"""
    custom69: str
    """Custom field 69"""
    custom7: str
    """Custom field 7"""
    custom70: str
    """Custom field 70"""
    custom71: str
    """Custom field 71"""
    custom72: str
    """Custom field 72"""
    custom73: str
    """Custom field 73"""
    custom74: str
    """Custom field 74"""
    custom75: str
    """Custom field 75"""
    custom76: str
    """Custom field 76"""
    custom77: str
    """Custom field 77"""
    custom78: str
    """Custom field 78"""
    custom79: str
    """Custom field 79"""
    custom8: str
    """Custom field 8"""
    custom80: str
    """Custom field 80"""
    custom81: str
    """Custom field 81"""
    custom82: str
    """Custom field 82"""
    custom83: str
    """Custom field 83"""
    custom84: str
    """Custom field 84"""
    custom85: str
    """Custom field 85"""
    custom86: str
    """Custom field 86"""
    custom87: str
    """Custom field 87"""
    custom88: str
    """Custom field 88"""
    custom89: str
    """Custom field 89"""
    custom9: str
    """Custom field 9"""
    custom90: str
    """Custom field 90"""
    custom91: str
    """Custom field 91"""
    custom92: str
    """Custom field 92"""
    custom93: str
    """Custom field 93"""
    custom94: str
    """Custom field 94"""
    custom95: str
    """Custom field 95"""
    custom96: str
    """Custom field 96"""
    custom97: str
    """Custom field 97"""
    custom98: str
    """Custom field 98"""
    custom99: str
    """Custom field 99"""
    custom_id: str
    """Custom id"""
    default_plugin_mapping: str
    """Default plugin mapping"""
    description: str
    """Description"""
    domain: str
    """Domain"""
    external_source: str
    """External source"""
    favorites: str
    """Favorites"""
    followers: str
    """Followers"""
    founded_at: str
    """Founded at"""
    id: str
    """Unique account identifier"""
    industry: str
    """Industry"""
    linked_in_employees: str
    """Linked in employees"""
    linked_in_url: str
    """Linked in url"""
    locality: str
    """Locality"""
    name: str
    """Name"""
    named: str
    """Named"""
    natural_name: str
    """Natural name"""
    number_of_employees: str
    """Number of employees"""
    owner: str
    """Owner"""
    prospects: str
    """Prospects"""
    sharing_team_id: str
    """Sharing team id"""
    tags: str
    """Tags"""
    tasks: str
    """Tasks"""
    touched_at: str
    """Touched at"""
    trashed_at: str
    """Trashed at"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""
    website_url: str
    """Website url"""


class AccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting accounts search results."""
    assigned_teams: AirbyteSortOrder
    """Assigned teams"""
    assigned_users: AirbyteSortOrder
    """Assigned users"""
    batches: AirbyteSortOrder
    """Batches"""
    buyer_intent_score: AirbyteSortOrder
    """Buyer intent score"""
    company_type: AirbyteSortOrder
    """Company type"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    custom1: AirbyteSortOrder
    """Custom field 1"""
    custom10: AirbyteSortOrder
    """Custom field 10"""
    custom100: AirbyteSortOrder
    """Custom field 100"""
    custom101: AirbyteSortOrder
    """Custom field 101"""
    custom102: AirbyteSortOrder
    """Custom field 102"""
    custom103: AirbyteSortOrder
    """Custom field 103"""
    custom104: AirbyteSortOrder
    """Custom field 104"""
    custom105: AirbyteSortOrder
    """Custom field 105"""
    custom106: AirbyteSortOrder
    """Custom field 106"""
    custom107: AirbyteSortOrder
    """Custom field 107"""
    custom108: AirbyteSortOrder
    """Custom field 108"""
    custom109: AirbyteSortOrder
    """Custom field 109"""
    custom11: AirbyteSortOrder
    """Custom field 11"""
    custom110: AirbyteSortOrder
    """Custom field 110"""
    custom111: AirbyteSortOrder
    """Custom field 111"""
    custom112: AirbyteSortOrder
    """Custom field 112"""
    custom113: AirbyteSortOrder
    """Custom field 113"""
    custom114: AirbyteSortOrder
    """Custom field 114"""
    custom115: AirbyteSortOrder
    """Custom field 115"""
    custom116: AirbyteSortOrder
    """Custom field 116"""
    custom117: AirbyteSortOrder
    """Custom field 117"""
    custom118: AirbyteSortOrder
    """Custom field 118"""
    custom119: AirbyteSortOrder
    """Custom field 119"""
    custom12: AirbyteSortOrder
    """Custom field 12"""
    custom120: AirbyteSortOrder
    """Custom field 120"""
    custom121: AirbyteSortOrder
    """Custom field 121"""
    custom122: AirbyteSortOrder
    """Custom field 122"""
    custom123: AirbyteSortOrder
    """Custom field 123"""
    custom124: AirbyteSortOrder
    """Custom field 124"""
    custom125: AirbyteSortOrder
    """Custom field 125"""
    custom126: AirbyteSortOrder
    """Custom field 126"""
    custom127: AirbyteSortOrder
    """Custom field 127"""
    custom128: AirbyteSortOrder
    """Custom field 128"""
    custom129: AirbyteSortOrder
    """Custom field 129"""
    custom13: AirbyteSortOrder
    """Custom field 13"""
    custom130: AirbyteSortOrder
    """Custom field 130"""
    custom131: AirbyteSortOrder
    """Custom field 131"""
    custom132: AirbyteSortOrder
    """Custom field 132"""
    custom133: AirbyteSortOrder
    """Custom field 133"""
    custom134: AirbyteSortOrder
    """Custom field 134"""
    custom135: AirbyteSortOrder
    """Custom field 135"""
    custom136: AirbyteSortOrder
    """Custom field 136"""
    custom137: AirbyteSortOrder
    """Custom field 137"""
    custom138: AirbyteSortOrder
    """Custom field 138"""
    custom139: AirbyteSortOrder
    """Custom field 139"""
    custom14: AirbyteSortOrder
    """Custom field 14"""
    custom140: AirbyteSortOrder
    """Custom field 140"""
    custom141: AirbyteSortOrder
    """Custom field 141"""
    custom142: AirbyteSortOrder
    """Custom field 142"""
    custom143: AirbyteSortOrder
    """Custom field 143"""
    custom144: AirbyteSortOrder
    """Custom field 144"""
    custom145: AirbyteSortOrder
    """Custom field 145"""
    custom146: AirbyteSortOrder
    """Custom field 146"""
    custom147: AirbyteSortOrder
    """Custom field 147"""
    custom148: AirbyteSortOrder
    """Custom field 148"""
    custom149: AirbyteSortOrder
    """Custom field 149"""
    custom15: AirbyteSortOrder
    """Custom field 15"""
    custom150: AirbyteSortOrder
    """Custom field 150"""
    custom16: AirbyteSortOrder
    """Custom field 16"""
    custom17: AirbyteSortOrder
    """Custom field 17"""
    custom18: AirbyteSortOrder
    """Custom field 18"""
    custom19: AirbyteSortOrder
    """Custom field 19"""
    custom2: AirbyteSortOrder
    """Custom field 2"""
    custom20: AirbyteSortOrder
    """Custom field 20"""
    custom21: AirbyteSortOrder
    """Custom field 21"""
    custom22: AirbyteSortOrder
    """Custom field 22"""
    custom23: AirbyteSortOrder
    """Custom field 23"""
    custom24: AirbyteSortOrder
    """Custom field 24"""
    custom25: AirbyteSortOrder
    """Custom field 25"""
    custom26: AirbyteSortOrder
    """Custom field 26"""
    custom27: AirbyteSortOrder
    """Custom field 27"""
    custom28: AirbyteSortOrder
    """Custom field 28"""
    custom29: AirbyteSortOrder
    """Custom field 29"""
    custom3: AirbyteSortOrder
    """Custom field 3"""
    custom30: AirbyteSortOrder
    """Custom field 30"""
    custom31: AirbyteSortOrder
    """Custom field 31"""
    custom32: AirbyteSortOrder
    """Custom field 32"""
    custom33: AirbyteSortOrder
    """Custom field 33"""
    custom34: AirbyteSortOrder
    """Custom field 34"""
    custom35: AirbyteSortOrder
    """Custom field 35"""
    custom36: AirbyteSortOrder
    """Custom field 36"""
    custom37: AirbyteSortOrder
    """Custom field 37"""
    custom38: AirbyteSortOrder
    """Custom field 38"""
    custom39: AirbyteSortOrder
    """Custom field 39"""
    custom4: AirbyteSortOrder
    """Custom field 4"""
    custom40: AirbyteSortOrder
    """Custom field 40"""
    custom41: AirbyteSortOrder
    """Custom field 41"""
    custom42: AirbyteSortOrder
    """Custom field 42"""
    custom43: AirbyteSortOrder
    """Custom field 43"""
    custom44: AirbyteSortOrder
    """Custom field 44"""
    custom45: AirbyteSortOrder
    """Custom field 45"""
    custom46: AirbyteSortOrder
    """Custom field 46"""
    custom47: AirbyteSortOrder
    """Custom field 47"""
    custom48: AirbyteSortOrder
    """Custom field 48"""
    custom49: AirbyteSortOrder
    """Custom field 49"""
    custom5: AirbyteSortOrder
    """Custom field 5"""
    custom50: AirbyteSortOrder
    """Custom field 50"""
    custom51: AirbyteSortOrder
    """Custom field 51"""
    custom52: AirbyteSortOrder
    """Custom field 52"""
    custom53: AirbyteSortOrder
    """Custom field 53"""
    custom54: AirbyteSortOrder
    """Custom field 54"""
    custom55: AirbyteSortOrder
    """Custom field 55"""
    custom56: AirbyteSortOrder
    """Custom field 56"""
    custom57: AirbyteSortOrder
    """Custom field 57"""
    custom58: AirbyteSortOrder
    """Custom field 58"""
    custom59: AirbyteSortOrder
    """Custom field 59"""
    custom6: AirbyteSortOrder
    """Custom field 6"""
    custom60: AirbyteSortOrder
    """Custom field 60"""
    custom61: AirbyteSortOrder
    """Custom field 61"""
    custom62: AirbyteSortOrder
    """Custom field 62"""
    custom63: AirbyteSortOrder
    """Custom field 63"""
    custom64: AirbyteSortOrder
    """Custom field 64"""
    custom65: AirbyteSortOrder
    """Custom field 65"""
    custom66: AirbyteSortOrder
    """Custom field 66"""
    custom67: AirbyteSortOrder
    """Custom field 67"""
    custom68: AirbyteSortOrder
    """Custom field 68"""
    custom69: AirbyteSortOrder
    """Custom field 69"""
    custom7: AirbyteSortOrder
    """Custom field 7"""
    custom70: AirbyteSortOrder
    """Custom field 70"""
    custom71: AirbyteSortOrder
    """Custom field 71"""
    custom72: AirbyteSortOrder
    """Custom field 72"""
    custom73: AirbyteSortOrder
    """Custom field 73"""
    custom74: AirbyteSortOrder
    """Custom field 74"""
    custom75: AirbyteSortOrder
    """Custom field 75"""
    custom76: AirbyteSortOrder
    """Custom field 76"""
    custom77: AirbyteSortOrder
    """Custom field 77"""
    custom78: AirbyteSortOrder
    """Custom field 78"""
    custom79: AirbyteSortOrder
    """Custom field 79"""
    custom8: AirbyteSortOrder
    """Custom field 8"""
    custom80: AirbyteSortOrder
    """Custom field 80"""
    custom81: AirbyteSortOrder
    """Custom field 81"""
    custom82: AirbyteSortOrder
    """Custom field 82"""
    custom83: AirbyteSortOrder
    """Custom field 83"""
    custom84: AirbyteSortOrder
    """Custom field 84"""
    custom85: AirbyteSortOrder
    """Custom field 85"""
    custom86: AirbyteSortOrder
    """Custom field 86"""
    custom87: AirbyteSortOrder
    """Custom field 87"""
    custom88: AirbyteSortOrder
    """Custom field 88"""
    custom89: AirbyteSortOrder
    """Custom field 89"""
    custom9: AirbyteSortOrder
    """Custom field 9"""
    custom90: AirbyteSortOrder
    """Custom field 90"""
    custom91: AirbyteSortOrder
    """Custom field 91"""
    custom92: AirbyteSortOrder
    """Custom field 92"""
    custom93: AirbyteSortOrder
    """Custom field 93"""
    custom94: AirbyteSortOrder
    """Custom field 94"""
    custom95: AirbyteSortOrder
    """Custom field 95"""
    custom96: AirbyteSortOrder
    """Custom field 96"""
    custom97: AirbyteSortOrder
    """Custom field 97"""
    custom98: AirbyteSortOrder
    """Custom field 98"""
    custom99: AirbyteSortOrder
    """Custom field 99"""
    custom_id: AirbyteSortOrder
    """Custom id"""
    default_plugin_mapping: AirbyteSortOrder
    """Default plugin mapping"""
    description: AirbyteSortOrder
    """Description"""
    domain: AirbyteSortOrder
    """Domain"""
    external_source: AirbyteSortOrder
    """External source"""
    favorites: AirbyteSortOrder
    """Favorites"""
    followers: AirbyteSortOrder
    """Followers"""
    founded_at: AirbyteSortOrder
    """Founded at"""
    id: AirbyteSortOrder
    """Unique account identifier"""
    industry: AirbyteSortOrder
    """Industry"""
    linked_in_employees: AirbyteSortOrder
    """Linked in employees"""
    linked_in_url: AirbyteSortOrder
    """Linked in url"""
    locality: AirbyteSortOrder
    """Locality"""
    name: AirbyteSortOrder
    """Name"""
    named: AirbyteSortOrder
    """Named"""
    natural_name: AirbyteSortOrder
    """Natural name"""
    number_of_employees: AirbyteSortOrder
    """Number of employees"""
    owner: AirbyteSortOrder
    """Owner"""
    prospects: AirbyteSortOrder
    """Prospects"""
    sharing_team_id: AirbyteSortOrder
    """Sharing team id"""
    tags: AirbyteSortOrder
    """Tags"""
    tasks: AirbyteSortOrder
    """Tasks"""
    touched_at: AirbyteSortOrder
    """Touched at"""
    trashed_at: AirbyteSortOrder
    """Trashed at"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""
    website_url: AirbyteSortOrder
    """Website url"""


# Entity-specific condition types for accounts
class AccountsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AccountsSearchFilter


class AccountsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AccountsSearchFilter


class AccountsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AccountsSearchFilter


class AccountsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AccountsSearchFilter


class AccountsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AccountsSearchFilter


class AccountsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AccountsSearchFilter


class AccountsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AccountsStringFilter


class AccountsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AccountsStringFilter


class AccountsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountsStringFilter


class AccountsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountsStringFilter


class AccountsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: AccountsAnyValueFilter


class AccountsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: AccountsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AccountsInCondition = TypedDict("AccountsInCondition", {"in": AccountsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AccountsNotCondition = TypedDict("AccountsNotCondition", {"not": "AccountsCondition"}, total=False)
"""Negates the nested condition."""

AccountsAndCondition = TypedDict("AccountsAndCondition", {"and": "list[AccountsCondition]"}, total=False)
"""True if all nested conditions are true."""

AccountsOrCondition = TypedDict("AccountsOrCondition", {"or": "list[AccountsCondition]"}, total=False)
"""True if any nested condition is true."""

AccountsAnyCondition = TypedDict("AccountsAnyCondition", {"any": AccountsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all accounts condition types
AccountsCondition = (
    AccountsEqCondition
    | AccountsNeqCondition
    | AccountsGtCondition
    | AccountsGteCondition
    | AccountsLtCondition
    | AccountsLteCondition
    | AccountsInCondition
    | AccountsStartswithCondition
    | AccountsEndswithCondition
    | AccountsFuzzyCondition
    | AccountsKeywordCondition
    | AccountsContainsCondition
    | AccountsArrayContainsCondition
    | AccountsNotCondition
    | AccountsAndCondition
    | AccountsOrCondition
    | AccountsAnyCondition
)


class AccountsSearchQuery(TypedDict, total=False):
    """Search query for accounts entity."""
    filter: AccountsCondition
    sort: list[AccountsSortFilter]


# ===== CALLS SEARCH TYPES =====

class CallsSearchFilter(TypedDict, total=False):
    """Available fields for filtering calls search queries."""
    answered_at: str | None
    """Answered at"""
    batches: list[Any] | None
    """Batches"""
    call_disposition: list[Any] | None
    """Call disposition"""
    call_purpose: list[Any] | None
    """Call purpose"""
    completed_at: str | None
    """Completed at"""
    created_at: str | None
    """Created at"""
    dialed_at: str | None
    """Dialed at"""
    direction: str | None
    """Direction"""
    external_vendor: str | None
    """External vendor"""
    from_: str | None
    """From"""
    id: int | None
    """Unique call identifier"""
    note: str | None
    """Note"""
    opportunity: list[Any] | None
    """Opportunity"""
    outbound_voicemail: list[Any] | None
    """Outbound voicemail"""
    outcome: str | None
    """Outcome"""
    phone: list[Any] | None
    """Phone"""
    phone_number: list[Any] | None
    """Phone number"""
    prospect: list[Any] | None
    """Prospect"""
    recording_deletion_reason: str | None
    """Recording deletion reason"""
    recording_url: str | None
    """Recording url"""
    returned_at: str | None
    """Returned at"""
    sequence: list[Any] | None
    """Sequence"""
    sequence_action: str | None
    """Sequence action"""
    sequence_state: list[Any] | None
    """Sequence state"""
    sequence_step: list[Any] | None
    """Sequence step"""
    should_record_call: bool | None
    """Should record call"""
    state: str | None
    """State"""
    state_changed_at: str | None
    """State changed at"""
    tags: list[Any] | None
    """Tags"""
    task: list[Any] | None
    """Task"""
    to: str | None
    """To"""
    uid: str | None
    """Uid"""
    updated_at: str | None
    """Updated at"""
    user: list[Any] | None
    """User"""
    user_call_type: str | None
    """User call type"""
    vendor_call_id: str | None
    """Vendor call id"""
    voicemail_recording_url: str | None
    """Voicemail recording url"""


class CallsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    answered_at: list[str]
    """Answered at"""
    batches: list[list[Any]]
    """Batches"""
    call_disposition: list[list[Any]]
    """Call disposition"""
    call_purpose: list[list[Any]]
    """Call purpose"""
    completed_at: list[str]
    """Completed at"""
    created_at: list[str]
    """Created at"""
    dialed_at: list[str]
    """Dialed at"""
    direction: list[str]
    """Direction"""
    external_vendor: list[str]
    """External vendor"""
    from_: list[str]
    """From"""
    id: list[int]
    """Unique call identifier"""
    note: list[str]
    """Note"""
    opportunity: list[list[Any]]
    """Opportunity"""
    outbound_voicemail: list[list[Any]]
    """Outbound voicemail"""
    outcome: list[str]
    """Outcome"""
    phone: list[list[Any]]
    """Phone"""
    phone_number: list[list[Any]]
    """Phone number"""
    prospect: list[list[Any]]
    """Prospect"""
    recording_deletion_reason: list[str]
    """Recording deletion reason"""
    recording_url: list[str]
    """Recording url"""
    returned_at: list[str]
    """Returned at"""
    sequence: list[list[Any]]
    """Sequence"""
    sequence_action: list[str]
    """Sequence action"""
    sequence_state: list[list[Any]]
    """Sequence state"""
    sequence_step: list[list[Any]]
    """Sequence step"""
    should_record_call: list[bool]
    """Should record call"""
    state: list[str]
    """State"""
    state_changed_at: list[str]
    """State changed at"""
    tags: list[list[Any]]
    """Tags"""
    task: list[list[Any]]
    """Task"""
    to: list[str]
    """To"""
    uid: list[str]
    """Uid"""
    updated_at: list[str]
    """Updated at"""
    user: list[list[Any]]
    """User"""
    user_call_type: list[str]
    """User call type"""
    vendor_call_id: list[str]
    """Vendor call id"""
    voicemail_recording_url: list[str]
    """Voicemail recording url"""


class CallsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    answered_at: Any
    """Answered at"""
    batches: Any
    """Batches"""
    call_disposition: Any
    """Call disposition"""
    call_purpose: Any
    """Call purpose"""
    completed_at: Any
    """Completed at"""
    created_at: Any
    """Created at"""
    dialed_at: Any
    """Dialed at"""
    direction: Any
    """Direction"""
    external_vendor: Any
    """External vendor"""
    from_: Any
    """From"""
    id: Any
    """Unique call identifier"""
    note: Any
    """Note"""
    opportunity: Any
    """Opportunity"""
    outbound_voicemail: Any
    """Outbound voicemail"""
    outcome: Any
    """Outcome"""
    phone: Any
    """Phone"""
    phone_number: Any
    """Phone number"""
    prospect: Any
    """Prospect"""
    recording_deletion_reason: Any
    """Recording deletion reason"""
    recording_url: Any
    """Recording url"""
    returned_at: Any
    """Returned at"""
    sequence: Any
    """Sequence"""
    sequence_action: Any
    """Sequence action"""
    sequence_state: Any
    """Sequence state"""
    sequence_step: Any
    """Sequence step"""
    should_record_call: Any
    """Should record call"""
    state: Any
    """State"""
    state_changed_at: Any
    """State changed at"""
    tags: Any
    """Tags"""
    task: Any
    """Task"""
    to: Any
    """To"""
    uid: Any
    """Uid"""
    updated_at: Any
    """Updated at"""
    user: Any
    """User"""
    user_call_type: Any
    """User call type"""
    vendor_call_id: Any
    """Vendor call id"""
    voicemail_recording_url: Any
    """Voicemail recording url"""


class CallsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    answered_at: str
    """Answered at"""
    batches: str
    """Batches"""
    call_disposition: str
    """Call disposition"""
    call_purpose: str
    """Call purpose"""
    completed_at: str
    """Completed at"""
    created_at: str
    """Created at"""
    dialed_at: str
    """Dialed at"""
    direction: str
    """Direction"""
    external_vendor: str
    """External vendor"""
    from_: str
    """From"""
    id: str
    """Unique call identifier"""
    note: str
    """Note"""
    opportunity: str
    """Opportunity"""
    outbound_voicemail: str
    """Outbound voicemail"""
    outcome: str
    """Outcome"""
    phone: str
    """Phone"""
    phone_number: str
    """Phone number"""
    prospect: str
    """Prospect"""
    recording_deletion_reason: str
    """Recording deletion reason"""
    recording_url: str
    """Recording url"""
    returned_at: str
    """Returned at"""
    sequence: str
    """Sequence"""
    sequence_action: str
    """Sequence action"""
    sequence_state: str
    """Sequence state"""
    sequence_step: str
    """Sequence step"""
    should_record_call: str
    """Should record call"""
    state: str
    """State"""
    state_changed_at: str
    """State changed at"""
    tags: str
    """Tags"""
    task: str
    """Task"""
    to: str
    """To"""
    uid: str
    """Uid"""
    updated_at: str
    """Updated at"""
    user: str
    """User"""
    user_call_type: str
    """User call type"""
    vendor_call_id: str
    """Vendor call id"""
    voicemail_recording_url: str
    """Voicemail recording url"""


class CallsSortFilter(TypedDict, total=False):
    """Available fields for sorting calls search results."""
    answered_at: AirbyteSortOrder
    """Answered at"""
    batches: AirbyteSortOrder
    """Batches"""
    call_disposition: AirbyteSortOrder
    """Call disposition"""
    call_purpose: AirbyteSortOrder
    """Call purpose"""
    completed_at: AirbyteSortOrder
    """Completed at"""
    created_at: AirbyteSortOrder
    """Created at"""
    dialed_at: AirbyteSortOrder
    """Dialed at"""
    direction: AirbyteSortOrder
    """Direction"""
    external_vendor: AirbyteSortOrder
    """External vendor"""
    from_: AirbyteSortOrder
    """From"""
    id: AirbyteSortOrder
    """Unique call identifier"""
    note: AirbyteSortOrder
    """Note"""
    opportunity: AirbyteSortOrder
    """Opportunity"""
    outbound_voicemail: AirbyteSortOrder
    """Outbound voicemail"""
    outcome: AirbyteSortOrder
    """Outcome"""
    phone: AirbyteSortOrder
    """Phone"""
    phone_number: AirbyteSortOrder
    """Phone number"""
    prospect: AirbyteSortOrder
    """Prospect"""
    recording_deletion_reason: AirbyteSortOrder
    """Recording deletion reason"""
    recording_url: AirbyteSortOrder
    """Recording url"""
    returned_at: AirbyteSortOrder
    """Returned at"""
    sequence: AirbyteSortOrder
    """Sequence"""
    sequence_action: AirbyteSortOrder
    """Sequence action"""
    sequence_state: AirbyteSortOrder
    """Sequence state"""
    sequence_step: AirbyteSortOrder
    """Sequence step"""
    should_record_call: AirbyteSortOrder
    """Should record call"""
    state: AirbyteSortOrder
    """State"""
    state_changed_at: AirbyteSortOrder
    """State changed at"""
    tags: AirbyteSortOrder
    """Tags"""
    task: AirbyteSortOrder
    """Task"""
    to: AirbyteSortOrder
    """To"""
    uid: AirbyteSortOrder
    """Uid"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    user: AirbyteSortOrder
    """User"""
    user_call_type: AirbyteSortOrder
    """User call type"""
    vendor_call_id: AirbyteSortOrder
    """Vendor call id"""
    voicemail_recording_url: AirbyteSortOrder
    """Voicemail recording url"""


# Entity-specific condition types for calls
class CallsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallsSearchFilter


class CallsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallsSearchFilter


class CallsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallsSearchFilter


class CallsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallsSearchFilter


class CallsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallsSearchFilter


class CallsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallsSearchFilter


class CallsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CallsStringFilter


class CallsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CallsStringFilter


class CallsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallsStringFilter


class CallsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallsStringFilter


class CallsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: CallsAnyValueFilter


class CallsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: CallsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallsInCondition = TypedDict("CallsInCondition", {"in": CallsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallsNotCondition = TypedDict("CallsNotCondition", {"not": "CallsCondition"}, total=False)
"""Negates the nested condition."""

CallsAndCondition = TypedDict("CallsAndCondition", {"and": "list[CallsCondition]"}, total=False)
"""True if all nested conditions are true."""

CallsOrCondition = TypedDict("CallsOrCondition", {"or": "list[CallsCondition]"}, total=False)
"""True if any nested condition is true."""

CallsAnyCondition = TypedDict("CallsAnyCondition", {"any": CallsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all calls condition types
CallsCondition = (
    CallsEqCondition
    | CallsNeqCondition
    | CallsGtCondition
    | CallsGteCondition
    | CallsLtCondition
    | CallsLteCondition
    | CallsInCondition
    | CallsStartswithCondition
    | CallsEndswithCondition
    | CallsFuzzyCondition
    | CallsKeywordCondition
    | CallsContainsCondition
    | CallsArrayContainsCondition
    | CallsNotCondition
    | CallsAndCondition
    | CallsOrCondition
    | CallsAnyCondition
)


class CallsSearchQuery(TypedDict, total=False):
    """Search query for calls entity."""
    filter: CallsCondition
    sort: list[CallsSortFilter]


# ===== CALL_DISPOSITIONS SEARCH TYPES =====

class CallDispositionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering call_dispositions search queries."""
    calls: list[Any] | None
    """Calls"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    default_for_outbound_voicemail: bool | None
    """Default for outbound voicemail"""
    id: int | None
    """Unique call disposition identifier"""
    name: str | None
    """Name"""
    order: int | None
    """Order"""
    outcome: str | None
    """Outcome"""
    updated_at: str | None
    """Updated at"""


class CallDispositionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    calls: list[list[Any]]
    """Calls"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    default_for_outbound_voicemail: list[bool]
    """Default for outbound voicemail"""
    id: list[int]
    """Unique call disposition identifier"""
    name: list[str]
    """Name"""
    order: list[int]
    """Order"""
    outcome: list[str]
    """Outcome"""
    updated_at: list[str]
    """Updated at"""


class CallDispositionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    calls: Any
    """Calls"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    default_for_outbound_voicemail: Any
    """Default for outbound voicemail"""
    id: Any
    """Unique call disposition identifier"""
    name: Any
    """Name"""
    order: Any
    """Order"""
    outcome: Any
    """Outcome"""
    updated_at: Any
    """Updated at"""


class CallDispositionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    calls: str
    """Calls"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    default_for_outbound_voicemail: str
    """Default for outbound voicemail"""
    id: str
    """Unique call disposition identifier"""
    name: str
    """Name"""
    order: str
    """Order"""
    outcome: str
    """Outcome"""
    updated_at: str
    """Updated at"""


class CallDispositionsSortFilter(TypedDict, total=False):
    """Available fields for sorting call_dispositions search results."""
    calls: AirbyteSortOrder
    """Calls"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    default_for_outbound_voicemail: AirbyteSortOrder
    """Default for outbound voicemail"""
    id: AirbyteSortOrder
    """Unique call disposition identifier"""
    name: AirbyteSortOrder
    """Name"""
    order: AirbyteSortOrder
    """Order"""
    outcome: AirbyteSortOrder
    """Outcome"""
    updated_at: AirbyteSortOrder
    """Updated at"""


# Entity-specific condition types for call_dispositions
class CallDispositionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallDispositionsSearchFilter


class CallDispositionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallDispositionsSearchFilter


class CallDispositionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallDispositionsSearchFilter


class CallDispositionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallDispositionsSearchFilter


class CallDispositionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallDispositionsSearchFilter


class CallDispositionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallDispositionsSearchFilter


class CallDispositionsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CallDispositionsStringFilter


class CallDispositionsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CallDispositionsStringFilter


class CallDispositionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallDispositionsStringFilter


class CallDispositionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallDispositionsStringFilter


class CallDispositionsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: CallDispositionsAnyValueFilter


class CallDispositionsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: CallDispositionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallDispositionsInCondition = TypedDict("CallDispositionsInCondition", {"in": CallDispositionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallDispositionsNotCondition = TypedDict("CallDispositionsNotCondition", {"not": "CallDispositionsCondition"}, total=False)
"""Negates the nested condition."""

CallDispositionsAndCondition = TypedDict("CallDispositionsAndCondition", {"and": "list[CallDispositionsCondition]"}, total=False)
"""True if all nested conditions are true."""

CallDispositionsOrCondition = TypedDict("CallDispositionsOrCondition", {"or": "list[CallDispositionsCondition]"}, total=False)
"""True if any nested condition is true."""

CallDispositionsAnyCondition = TypedDict("CallDispositionsAnyCondition", {"any": CallDispositionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all call_dispositions condition types
CallDispositionsCondition = (
    CallDispositionsEqCondition
    | CallDispositionsNeqCondition
    | CallDispositionsGtCondition
    | CallDispositionsGteCondition
    | CallDispositionsLtCondition
    | CallDispositionsLteCondition
    | CallDispositionsInCondition
    | CallDispositionsStartswithCondition
    | CallDispositionsEndswithCondition
    | CallDispositionsFuzzyCondition
    | CallDispositionsKeywordCondition
    | CallDispositionsContainsCondition
    | CallDispositionsArrayContainsCondition
    | CallDispositionsNotCondition
    | CallDispositionsAndCondition
    | CallDispositionsOrCondition
    | CallDispositionsAnyCondition
)


class CallDispositionsSearchQuery(TypedDict, total=False):
    """Search query for call_dispositions entity."""
    filter: CallDispositionsCondition
    sort: list[CallDispositionsSortFilter]


# ===== CALL_PURPOSES SEARCH TYPES =====

class CallPurposesSearchFilter(TypedDict, total=False):
    """Available fields for filtering call_purposes search queries."""
    calls: list[Any] | None
    """Calls"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    id: int | None
    """Unique call purpose identifier"""
    name: str | None
    """Name"""
    order: int | None
    """Order"""
    updated_at: str | None
    """Updated at"""


class CallPurposesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    calls: list[list[Any]]
    """Calls"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    id: list[int]
    """Unique call purpose identifier"""
    name: list[str]
    """Name"""
    order: list[int]
    """Order"""
    updated_at: list[str]
    """Updated at"""


class CallPurposesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    calls: Any
    """Calls"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    id: Any
    """Unique call purpose identifier"""
    name: Any
    """Name"""
    order: Any
    """Order"""
    updated_at: Any
    """Updated at"""


class CallPurposesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    calls: str
    """Calls"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    id: str
    """Unique call purpose identifier"""
    name: str
    """Name"""
    order: str
    """Order"""
    updated_at: str
    """Updated at"""


class CallPurposesSortFilter(TypedDict, total=False):
    """Available fields for sorting call_purposes search results."""
    calls: AirbyteSortOrder
    """Calls"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    id: AirbyteSortOrder
    """Unique call purpose identifier"""
    name: AirbyteSortOrder
    """Name"""
    order: AirbyteSortOrder
    """Order"""
    updated_at: AirbyteSortOrder
    """Updated at"""


# Entity-specific condition types for call_purposes
class CallPurposesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallPurposesSearchFilter


class CallPurposesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallPurposesSearchFilter


class CallPurposesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallPurposesSearchFilter


class CallPurposesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallPurposesSearchFilter


class CallPurposesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallPurposesSearchFilter


class CallPurposesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallPurposesSearchFilter


class CallPurposesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CallPurposesStringFilter


class CallPurposesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CallPurposesStringFilter


class CallPurposesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallPurposesStringFilter


class CallPurposesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallPurposesStringFilter


class CallPurposesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: CallPurposesAnyValueFilter


class CallPurposesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: CallPurposesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallPurposesInCondition = TypedDict("CallPurposesInCondition", {"in": CallPurposesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallPurposesNotCondition = TypedDict("CallPurposesNotCondition", {"not": "CallPurposesCondition"}, total=False)
"""Negates the nested condition."""

CallPurposesAndCondition = TypedDict("CallPurposesAndCondition", {"and": "list[CallPurposesCondition]"}, total=False)
"""True if all nested conditions are true."""

CallPurposesOrCondition = TypedDict("CallPurposesOrCondition", {"or": "list[CallPurposesCondition]"}, total=False)
"""True if any nested condition is true."""

CallPurposesAnyCondition = TypedDict("CallPurposesAnyCondition", {"any": CallPurposesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all call_purposes condition types
CallPurposesCondition = (
    CallPurposesEqCondition
    | CallPurposesNeqCondition
    | CallPurposesGtCondition
    | CallPurposesGteCondition
    | CallPurposesLtCondition
    | CallPurposesLteCondition
    | CallPurposesInCondition
    | CallPurposesStartswithCondition
    | CallPurposesEndswithCondition
    | CallPurposesFuzzyCondition
    | CallPurposesKeywordCondition
    | CallPurposesContainsCondition
    | CallPurposesArrayContainsCondition
    | CallPurposesNotCondition
    | CallPurposesAndCondition
    | CallPurposesOrCondition
    | CallPurposesAnyCondition
)


class CallPurposesSearchQuery(TypedDict, total=False):
    """Search query for call_purposes entity."""
    filter: CallPurposesCondition
    sort: list[CallPurposesSortFilter]


# ===== MAILINGS SEARCH TYPES =====

class MailingsSearchFilter(TypedDict, total=False):
    """Available fields for filtering mailings search queries."""
    attachments: list[Any] | None
    """Attachments"""
    attributable_sequence_id: int | None
    """Attributable sequence id"""
    attributable_sequence_name: str | None
    """Attributable sequence name"""
    body_html: str | None
    """Body html"""
    body_text: str | None
    """Body text"""
    bounced_at: str | None
    """Bounced at"""
    calendar: list[Any] | None
    """Calendar"""
    click_count: int | None
    """Click count"""
    clicked_at: str | None
    """Clicked at"""
    created_at: str | None
    """Created at"""
    delivered_at: str | None
    """Delivered at"""
    desired_at: str | None
    """Desired at"""
    error_backtrace: str | None
    """Error backtrace"""
    error_reason: str | None
    """Error reason"""
    follow_up_sequence: list[Any] | None
    """Follow up sequence"""
    follow_up_sequence_id: int | None
    """Follow up sequence id"""
    follow_up_sequence_name: str | None
    """Follow up sequence name"""
    follow_up_sequence_starting_date: str | None
    """Follow up sequence starting date"""
    follow_up_task_scheduled_at: str | None
    """Follow up task scheduled at"""
    follow_up_task_type: str | None
    """Follow up task type"""
    id: int | None
    """Unique mailing identifier"""
    mailbox: list[Any] | None
    """Mailbox"""
    mailbox_address: str | None
    """Mailbox address"""
    mailing_type: str | None
    """Mailing type"""
    marked_as_spam_at: str | None
    """Marked as spam at"""
    meeting_description: str | None
    """Meeting description"""
    meeting_duration: int | None
    """Meeting duration"""
    meeting_location: str | None
    """Meeting location"""
    meeting_title: str | None
    """Meeting title"""
    message_id: str | None
    """Message id"""
    notify_thread_condition: str | None
    """Notify thread condition"""
    notify_thread_scheduled_at: str | None
    """Notify thread scheduled at"""
    notify_thread_status: str | None
    """Notify thread status"""
    open_count: int | None
    """Open count"""
    opened_at: str | None
    """Opened at"""
    opportunity: list[Any] | None
    """Opportunity"""
    optimized_scheduled_at: str | None
    """Optimized scheduled at"""
    override_safety_settings: bool | None
    """Override safety settings"""
    prospect: list[Any] | None
    """Prospect"""
    recipients: list[Any] | None
    """Recipients"""
    references: list[Any] | None
    """References"""
    replied_at: str | None
    """Replied at"""
    reply_sentiment: str | None
    """Reply sentiment"""
    retry_at: str | None
    """Retry at"""
    retry_count: int | None
    """Retry count"""
    retry_interval: int | None
    """Retry interval"""
    schedule: list[Any] | None
    """Schedule"""
    schedule_id: int | None
    """Schedule id"""
    scheduled_at: str | None
    """Scheduled at"""
    sequence: list[Any] | None
    """Sequence"""
    sequence_state: list[Any] | None
    """Sequence state"""
    sequence_step: list[Any] | None
    """Sequence step"""
    state: str | None
    """State"""
    state_changed_at: str | None
    """State changed at"""
    subject: str | None
    """Subject"""
    task: list[Any] | None
    """Task"""
    tasks: list[Any] | None
    """Tasks"""
    template: list[Any] | None
    """Template"""
    track_links: bool | None
    """Track links"""
    track_opens: bool | None
    """Track opens"""
    unsubscribed_at: str | None
    """Unsubscribed at"""
    updated_at: str | None
    """Updated at"""
    user: list[Any] | None
    """User"""


class MailingsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attachments: list[list[Any]]
    """Attachments"""
    attributable_sequence_id: list[int]
    """Attributable sequence id"""
    attributable_sequence_name: list[str]
    """Attributable sequence name"""
    body_html: list[str]
    """Body html"""
    body_text: list[str]
    """Body text"""
    bounced_at: list[str]
    """Bounced at"""
    calendar: list[list[Any]]
    """Calendar"""
    click_count: list[int]
    """Click count"""
    clicked_at: list[str]
    """Clicked at"""
    created_at: list[str]
    """Created at"""
    delivered_at: list[str]
    """Delivered at"""
    desired_at: list[str]
    """Desired at"""
    error_backtrace: list[str]
    """Error backtrace"""
    error_reason: list[str]
    """Error reason"""
    follow_up_sequence: list[list[Any]]
    """Follow up sequence"""
    follow_up_sequence_id: list[int]
    """Follow up sequence id"""
    follow_up_sequence_name: list[str]
    """Follow up sequence name"""
    follow_up_sequence_starting_date: list[str]
    """Follow up sequence starting date"""
    follow_up_task_scheduled_at: list[str]
    """Follow up task scheduled at"""
    follow_up_task_type: list[str]
    """Follow up task type"""
    id: list[int]
    """Unique mailing identifier"""
    mailbox: list[list[Any]]
    """Mailbox"""
    mailbox_address: list[str]
    """Mailbox address"""
    mailing_type: list[str]
    """Mailing type"""
    marked_as_spam_at: list[str]
    """Marked as spam at"""
    meeting_description: list[str]
    """Meeting description"""
    meeting_duration: list[int]
    """Meeting duration"""
    meeting_location: list[str]
    """Meeting location"""
    meeting_title: list[str]
    """Meeting title"""
    message_id: list[str]
    """Message id"""
    notify_thread_condition: list[str]
    """Notify thread condition"""
    notify_thread_scheduled_at: list[str]
    """Notify thread scheduled at"""
    notify_thread_status: list[str]
    """Notify thread status"""
    open_count: list[int]
    """Open count"""
    opened_at: list[str]
    """Opened at"""
    opportunity: list[list[Any]]
    """Opportunity"""
    optimized_scheduled_at: list[str]
    """Optimized scheduled at"""
    override_safety_settings: list[bool]
    """Override safety settings"""
    prospect: list[list[Any]]
    """Prospect"""
    recipients: list[list[Any]]
    """Recipients"""
    references: list[list[Any]]
    """References"""
    replied_at: list[str]
    """Replied at"""
    reply_sentiment: list[str]
    """Reply sentiment"""
    retry_at: list[str]
    """Retry at"""
    retry_count: list[int]
    """Retry count"""
    retry_interval: list[int]
    """Retry interval"""
    schedule: list[list[Any]]
    """Schedule"""
    schedule_id: list[int]
    """Schedule id"""
    scheduled_at: list[str]
    """Scheduled at"""
    sequence: list[list[Any]]
    """Sequence"""
    sequence_state: list[list[Any]]
    """Sequence state"""
    sequence_step: list[list[Any]]
    """Sequence step"""
    state: list[str]
    """State"""
    state_changed_at: list[str]
    """State changed at"""
    subject: list[str]
    """Subject"""
    task: list[list[Any]]
    """Task"""
    tasks: list[list[Any]]
    """Tasks"""
    template: list[list[Any]]
    """Template"""
    track_links: list[bool]
    """Track links"""
    track_opens: list[bool]
    """Track opens"""
    unsubscribed_at: list[str]
    """Unsubscribed at"""
    updated_at: list[str]
    """Updated at"""
    user: list[list[Any]]
    """User"""


class MailingsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attachments: Any
    """Attachments"""
    attributable_sequence_id: Any
    """Attributable sequence id"""
    attributable_sequence_name: Any
    """Attributable sequence name"""
    body_html: Any
    """Body html"""
    body_text: Any
    """Body text"""
    bounced_at: Any
    """Bounced at"""
    calendar: Any
    """Calendar"""
    click_count: Any
    """Click count"""
    clicked_at: Any
    """Clicked at"""
    created_at: Any
    """Created at"""
    delivered_at: Any
    """Delivered at"""
    desired_at: Any
    """Desired at"""
    error_backtrace: Any
    """Error backtrace"""
    error_reason: Any
    """Error reason"""
    follow_up_sequence: Any
    """Follow up sequence"""
    follow_up_sequence_id: Any
    """Follow up sequence id"""
    follow_up_sequence_name: Any
    """Follow up sequence name"""
    follow_up_sequence_starting_date: Any
    """Follow up sequence starting date"""
    follow_up_task_scheduled_at: Any
    """Follow up task scheduled at"""
    follow_up_task_type: Any
    """Follow up task type"""
    id: Any
    """Unique mailing identifier"""
    mailbox: Any
    """Mailbox"""
    mailbox_address: Any
    """Mailbox address"""
    mailing_type: Any
    """Mailing type"""
    marked_as_spam_at: Any
    """Marked as spam at"""
    meeting_description: Any
    """Meeting description"""
    meeting_duration: Any
    """Meeting duration"""
    meeting_location: Any
    """Meeting location"""
    meeting_title: Any
    """Meeting title"""
    message_id: Any
    """Message id"""
    notify_thread_condition: Any
    """Notify thread condition"""
    notify_thread_scheduled_at: Any
    """Notify thread scheduled at"""
    notify_thread_status: Any
    """Notify thread status"""
    open_count: Any
    """Open count"""
    opened_at: Any
    """Opened at"""
    opportunity: Any
    """Opportunity"""
    optimized_scheduled_at: Any
    """Optimized scheduled at"""
    override_safety_settings: Any
    """Override safety settings"""
    prospect: Any
    """Prospect"""
    recipients: Any
    """Recipients"""
    references: Any
    """References"""
    replied_at: Any
    """Replied at"""
    reply_sentiment: Any
    """Reply sentiment"""
    retry_at: Any
    """Retry at"""
    retry_count: Any
    """Retry count"""
    retry_interval: Any
    """Retry interval"""
    schedule: Any
    """Schedule"""
    schedule_id: Any
    """Schedule id"""
    scheduled_at: Any
    """Scheduled at"""
    sequence: Any
    """Sequence"""
    sequence_state: Any
    """Sequence state"""
    sequence_step: Any
    """Sequence step"""
    state: Any
    """State"""
    state_changed_at: Any
    """State changed at"""
    subject: Any
    """Subject"""
    task: Any
    """Task"""
    tasks: Any
    """Tasks"""
    template: Any
    """Template"""
    track_links: Any
    """Track links"""
    track_opens: Any
    """Track opens"""
    unsubscribed_at: Any
    """Unsubscribed at"""
    updated_at: Any
    """Updated at"""
    user: Any
    """User"""


class MailingsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    attachments: str
    """Attachments"""
    attributable_sequence_id: str
    """Attributable sequence id"""
    attributable_sequence_name: str
    """Attributable sequence name"""
    body_html: str
    """Body html"""
    body_text: str
    """Body text"""
    bounced_at: str
    """Bounced at"""
    calendar: str
    """Calendar"""
    click_count: str
    """Click count"""
    clicked_at: str
    """Clicked at"""
    created_at: str
    """Created at"""
    delivered_at: str
    """Delivered at"""
    desired_at: str
    """Desired at"""
    error_backtrace: str
    """Error backtrace"""
    error_reason: str
    """Error reason"""
    follow_up_sequence: str
    """Follow up sequence"""
    follow_up_sequence_id: str
    """Follow up sequence id"""
    follow_up_sequence_name: str
    """Follow up sequence name"""
    follow_up_sequence_starting_date: str
    """Follow up sequence starting date"""
    follow_up_task_scheduled_at: str
    """Follow up task scheduled at"""
    follow_up_task_type: str
    """Follow up task type"""
    id: str
    """Unique mailing identifier"""
    mailbox: str
    """Mailbox"""
    mailbox_address: str
    """Mailbox address"""
    mailing_type: str
    """Mailing type"""
    marked_as_spam_at: str
    """Marked as spam at"""
    meeting_description: str
    """Meeting description"""
    meeting_duration: str
    """Meeting duration"""
    meeting_location: str
    """Meeting location"""
    meeting_title: str
    """Meeting title"""
    message_id: str
    """Message id"""
    notify_thread_condition: str
    """Notify thread condition"""
    notify_thread_scheduled_at: str
    """Notify thread scheduled at"""
    notify_thread_status: str
    """Notify thread status"""
    open_count: str
    """Open count"""
    opened_at: str
    """Opened at"""
    opportunity: str
    """Opportunity"""
    optimized_scheduled_at: str
    """Optimized scheduled at"""
    override_safety_settings: str
    """Override safety settings"""
    prospect: str
    """Prospect"""
    recipients: str
    """Recipients"""
    references: str
    """References"""
    replied_at: str
    """Replied at"""
    reply_sentiment: str
    """Reply sentiment"""
    retry_at: str
    """Retry at"""
    retry_count: str
    """Retry count"""
    retry_interval: str
    """Retry interval"""
    schedule: str
    """Schedule"""
    schedule_id: str
    """Schedule id"""
    scheduled_at: str
    """Scheduled at"""
    sequence: str
    """Sequence"""
    sequence_state: str
    """Sequence state"""
    sequence_step: str
    """Sequence step"""
    state: str
    """State"""
    state_changed_at: str
    """State changed at"""
    subject: str
    """Subject"""
    task: str
    """Task"""
    tasks: str
    """Tasks"""
    template: str
    """Template"""
    track_links: str
    """Track links"""
    track_opens: str
    """Track opens"""
    unsubscribed_at: str
    """Unsubscribed at"""
    updated_at: str
    """Updated at"""
    user: str
    """User"""


class MailingsSortFilter(TypedDict, total=False):
    """Available fields for sorting mailings search results."""
    attachments: AirbyteSortOrder
    """Attachments"""
    attributable_sequence_id: AirbyteSortOrder
    """Attributable sequence id"""
    attributable_sequence_name: AirbyteSortOrder
    """Attributable sequence name"""
    body_html: AirbyteSortOrder
    """Body html"""
    body_text: AirbyteSortOrder
    """Body text"""
    bounced_at: AirbyteSortOrder
    """Bounced at"""
    calendar: AirbyteSortOrder
    """Calendar"""
    click_count: AirbyteSortOrder
    """Click count"""
    clicked_at: AirbyteSortOrder
    """Clicked at"""
    created_at: AirbyteSortOrder
    """Created at"""
    delivered_at: AirbyteSortOrder
    """Delivered at"""
    desired_at: AirbyteSortOrder
    """Desired at"""
    error_backtrace: AirbyteSortOrder
    """Error backtrace"""
    error_reason: AirbyteSortOrder
    """Error reason"""
    follow_up_sequence: AirbyteSortOrder
    """Follow up sequence"""
    follow_up_sequence_id: AirbyteSortOrder
    """Follow up sequence id"""
    follow_up_sequence_name: AirbyteSortOrder
    """Follow up sequence name"""
    follow_up_sequence_starting_date: AirbyteSortOrder
    """Follow up sequence starting date"""
    follow_up_task_scheduled_at: AirbyteSortOrder
    """Follow up task scheduled at"""
    follow_up_task_type: AirbyteSortOrder
    """Follow up task type"""
    id: AirbyteSortOrder
    """Unique mailing identifier"""
    mailbox: AirbyteSortOrder
    """Mailbox"""
    mailbox_address: AirbyteSortOrder
    """Mailbox address"""
    mailing_type: AirbyteSortOrder
    """Mailing type"""
    marked_as_spam_at: AirbyteSortOrder
    """Marked as spam at"""
    meeting_description: AirbyteSortOrder
    """Meeting description"""
    meeting_duration: AirbyteSortOrder
    """Meeting duration"""
    meeting_location: AirbyteSortOrder
    """Meeting location"""
    meeting_title: AirbyteSortOrder
    """Meeting title"""
    message_id: AirbyteSortOrder
    """Message id"""
    notify_thread_condition: AirbyteSortOrder
    """Notify thread condition"""
    notify_thread_scheduled_at: AirbyteSortOrder
    """Notify thread scheduled at"""
    notify_thread_status: AirbyteSortOrder
    """Notify thread status"""
    open_count: AirbyteSortOrder
    """Open count"""
    opened_at: AirbyteSortOrder
    """Opened at"""
    opportunity: AirbyteSortOrder
    """Opportunity"""
    optimized_scheduled_at: AirbyteSortOrder
    """Optimized scheduled at"""
    override_safety_settings: AirbyteSortOrder
    """Override safety settings"""
    prospect: AirbyteSortOrder
    """Prospect"""
    recipients: AirbyteSortOrder
    """Recipients"""
    references: AirbyteSortOrder
    """References"""
    replied_at: AirbyteSortOrder
    """Replied at"""
    reply_sentiment: AirbyteSortOrder
    """Reply sentiment"""
    retry_at: AirbyteSortOrder
    """Retry at"""
    retry_count: AirbyteSortOrder
    """Retry count"""
    retry_interval: AirbyteSortOrder
    """Retry interval"""
    schedule: AirbyteSortOrder
    """Schedule"""
    schedule_id: AirbyteSortOrder
    """Schedule id"""
    scheduled_at: AirbyteSortOrder
    """Scheduled at"""
    sequence: AirbyteSortOrder
    """Sequence"""
    sequence_state: AirbyteSortOrder
    """Sequence state"""
    sequence_step: AirbyteSortOrder
    """Sequence step"""
    state: AirbyteSortOrder
    """State"""
    state_changed_at: AirbyteSortOrder
    """State changed at"""
    subject: AirbyteSortOrder
    """Subject"""
    task: AirbyteSortOrder
    """Task"""
    tasks: AirbyteSortOrder
    """Tasks"""
    template: AirbyteSortOrder
    """Template"""
    track_links: AirbyteSortOrder
    """Track links"""
    track_opens: AirbyteSortOrder
    """Track opens"""
    unsubscribed_at: AirbyteSortOrder
    """Unsubscribed at"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    user: AirbyteSortOrder
    """User"""


# Entity-specific condition types for mailings
class MailingsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MailingsSearchFilter


class MailingsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MailingsSearchFilter


class MailingsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MailingsSearchFilter


class MailingsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MailingsSearchFilter


class MailingsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MailingsSearchFilter


class MailingsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MailingsSearchFilter


class MailingsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: MailingsStringFilter


class MailingsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: MailingsStringFilter


class MailingsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MailingsStringFilter


class MailingsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MailingsStringFilter


class MailingsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: MailingsAnyValueFilter


class MailingsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: MailingsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MailingsInCondition = TypedDict("MailingsInCondition", {"in": MailingsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MailingsNotCondition = TypedDict("MailingsNotCondition", {"not": "MailingsCondition"}, total=False)
"""Negates the nested condition."""

MailingsAndCondition = TypedDict("MailingsAndCondition", {"and": "list[MailingsCondition]"}, total=False)
"""True if all nested conditions are true."""

MailingsOrCondition = TypedDict("MailingsOrCondition", {"or": "list[MailingsCondition]"}, total=False)
"""True if any nested condition is true."""

MailingsAnyCondition = TypedDict("MailingsAnyCondition", {"any": MailingsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all mailings condition types
MailingsCondition = (
    MailingsEqCondition
    | MailingsNeqCondition
    | MailingsGtCondition
    | MailingsGteCondition
    | MailingsLtCondition
    | MailingsLteCondition
    | MailingsInCondition
    | MailingsStartswithCondition
    | MailingsEndswithCondition
    | MailingsFuzzyCondition
    | MailingsKeywordCondition
    | MailingsContainsCondition
    | MailingsArrayContainsCondition
    | MailingsNotCondition
    | MailingsAndCondition
    | MailingsOrCondition
    | MailingsAnyCondition
)


class MailingsSearchQuery(TypedDict, total=False):
    """Search query for mailings entity."""
    filter: MailingsCondition
    sort: list[MailingsSortFilter]


# ===== MAILBOXES SEARCH TYPES =====

class MailboxesSearchFilter(TypedDict, total=False):
    """Available fields for filtering mailboxes search queries."""
    auth_id: int | None
    """Auth id"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    editable: bool | None
    """Editable"""
    email: str | None
    """Email"""
    email_hash: str | None
    """Email hash"""
    email_provider: str | None
    """Email provider"""
    email_signature: str | None
    """Email signature"""
    ews_custom_search_folder: bool | None
    """Ews custom search folder"""
    ews_delegate_sync: bool | None
    """Ews delegate sync"""
    ews_endpoint: str | None
    """Ews endpoint"""
    ews_impersonation: bool | None
    """Ews impersonation"""
    ews_ssl_verify_mode: int | None
    """Ews ssl verify mode"""
    exchange_version: str | None
    """Exchange version"""
    id: int | None
    """Unique mailbox identifier"""
    imap_host: str | None
    """Imap host"""
    imap_port: int | None
    """Imap port"""
    imap_ssl: bool | None
    """Imap ssl"""
    mail_aliases: list[Any] | None
    """Mail aliases"""
    mailings: list[Any] | None
    """Mailings"""
    max_emails_per_day: int | None
    """Max emails per day"""
    max_mailings_per_day: int | None
    """Max mailings per day"""
    max_mailings_per_week: int | None
    """Max mailings per week"""
    opt_out_message: str | None
    """Opt out message"""
    opt_out_signature: str | None
    """Opt out signature"""
    prospect_email_exclusions: list[Any] | None
    """Prospect email exclusions"""
    provider_id: int | None
    """Provider id"""
    provider_type: str | None
    """Provider type"""
    send_disabled: bool | None
    """Send disabled"""
    send_errored_at: str | None
    """Send errored at"""
    send_max_retries: int | None
    """Send max retries"""
    send_method: str | None
    """Send method"""
    send_period: int | None
    """Send period"""
    send_permanent_error_at: str | None
    """Send permanent error at"""
    send_requires_sync: bool | None
    """Send requires sync"""
    send_success_at: str | None
    """Send success at"""
    send_threshold: int | None
    """Send threshold"""
    sendgrid_webhook_url: str | None
    """Sendgrid webhook url"""
    smtp_host: str | None
    """Smtp host"""
    smtp_port: int | None
    """Smtp port"""
    smtp_ssl: bool | None
    """Smtp ssl"""
    smtp_username: str | None
    """Smtp username"""
    sync_active_frequency: int | None
    """Sync active frequency"""
    sync_disabled: bool | None
    """Sync disabled"""
    sync_errored_at: str | None
    """Sync errored at"""
    sync_finished_at: str | None
    """Sync finished at"""
    sync_method: str | None
    """Sync method"""
    sync_outreach_folder: bool | None
    """Sync outreach folder"""
    sync_passive_frequency: int | None
    """Sync passive frequency"""
    sync_permanent_error_at: str | None
    """Sync permanent error at"""
    sync_success_at: str | None
    """Sync success at"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""
    user: list[Any] | None
    """User"""
    user_id: int | None
    """User id"""
    username: str | None
    """Username"""


class MailboxesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    auth_id: list[int]
    """Auth id"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    editable: list[bool]
    """Editable"""
    email: list[str]
    """Email"""
    email_hash: list[str]
    """Email hash"""
    email_provider: list[str]
    """Email provider"""
    email_signature: list[str]
    """Email signature"""
    ews_custom_search_folder: list[bool]
    """Ews custom search folder"""
    ews_delegate_sync: list[bool]
    """Ews delegate sync"""
    ews_endpoint: list[str]
    """Ews endpoint"""
    ews_impersonation: list[bool]
    """Ews impersonation"""
    ews_ssl_verify_mode: list[int]
    """Ews ssl verify mode"""
    exchange_version: list[str]
    """Exchange version"""
    id: list[int]
    """Unique mailbox identifier"""
    imap_host: list[str]
    """Imap host"""
    imap_port: list[int]
    """Imap port"""
    imap_ssl: list[bool]
    """Imap ssl"""
    mail_aliases: list[list[Any]]
    """Mail aliases"""
    mailings: list[list[Any]]
    """Mailings"""
    max_emails_per_day: list[int]
    """Max emails per day"""
    max_mailings_per_day: list[int]
    """Max mailings per day"""
    max_mailings_per_week: list[int]
    """Max mailings per week"""
    opt_out_message: list[str]
    """Opt out message"""
    opt_out_signature: list[str]
    """Opt out signature"""
    prospect_email_exclusions: list[list[Any]]
    """Prospect email exclusions"""
    provider_id: list[int]
    """Provider id"""
    provider_type: list[str]
    """Provider type"""
    send_disabled: list[bool]
    """Send disabled"""
    send_errored_at: list[str]
    """Send errored at"""
    send_max_retries: list[int]
    """Send max retries"""
    send_method: list[str]
    """Send method"""
    send_period: list[int]
    """Send period"""
    send_permanent_error_at: list[str]
    """Send permanent error at"""
    send_requires_sync: list[bool]
    """Send requires sync"""
    send_success_at: list[str]
    """Send success at"""
    send_threshold: list[int]
    """Send threshold"""
    sendgrid_webhook_url: list[str]
    """Sendgrid webhook url"""
    smtp_host: list[str]
    """Smtp host"""
    smtp_port: list[int]
    """Smtp port"""
    smtp_ssl: list[bool]
    """Smtp ssl"""
    smtp_username: list[str]
    """Smtp username"""
    sync_active_frequency: list[int]
    """Sync active frequency"""
    sync_disabled: list[bool]
    """Sync disabled"""
    sync_errored_at: list[str]
    """Sync errored at"""
    sync_finished_at: list[str]
    """Sync finished at"""
    sync_method: list[str]
    """Sync method"""
    sync_outreach_folder: list[bool]
    """Sync outreach folder"""
    sync_passive_frequency: list[int]
    """Sync passive frequency"""
    sync_permanent_error_at: list[str]
    """Sync permanent error at"""
    sync_success_at: list[str]
    """Sync success at"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""
    user: list[list[Any]]
    """User"""
    user_id: list[int]
    """User id"""
    username: list[str]
    """Username"""


class MailboxesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    auth_id: Any
    """Auth id"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    editable: Any
    """Editable"""
    email: Any
    """Email"""
    email_hash: Any
    """Email hash"""
    email_provider: Any
    """Email provider"""
    email_signature: Any
    """Email signature"""
    ews_custom_search_folder: Any
    """Ews custom search folder"""
    ews_delegate_sync: Any
    """Ews delegate sync"""
    ews_endpoint: Any
    """Ews endpoint"""
    ews_impersonation: Any
    """Ews impersonation"""
    ews_ssl_verify_mode: Any
    """Ews ssl verify mode"""
    exchange_version: Any
    """Exchange version"""
    id: Any
    """Unique mailbox identifier"""
    imap_host: Any
    """Imap host"""
    imap_port: Any
    """Imap port"""
    imap_ssl: Any
    """Imap ssl"""
    mail_aliases: Any
    """Mail aliases"""
    mailings: Any
    """Mailings"""
    max_emails_per_day: Any
    """Max emails per day"""
    max_mailings_per_day: Any
    """Max mailings per day"""
    max_mailings_per_week: Any
    """Max mailings per week"""
    opt_out_message: Any
    """Opt out message"""
    opt_out_signature: Any
    """Opt out signature"""
    prospect_email_exclusions: Any
    """Prospect email exclusions"""
    provider_id: Any
    """Provider id"""
    provider_type: Any
    """Provider type"""
    send_disabled: Any
    """Send disabled"""
    send_errored_at: Any
    """Send errored at"""
    send_max_retries: Any
    """Send max retries"""
    send_method: Any
    """Send method"""
    send_period: Any
    """Send period"""
    send_permanent_error_at: Any
    """Send permanent error at"""
    send_requires_sync: Any
    """Send requires sync"""
    send_success_at: Any
    """Send success at"""
    send_threshold: Any
    """Send threshold"""
    sendgrid_webhook_url: Any
    """Sendgrid webhook url"""
    smtp_host: Any
    """Smtp host"""
    smtp_port: Any
    """Smtp port"""
    smtp_ssl: Any
    """Smtp ssl"""
    smtp_username: Any
    """Smtp username"""
    sync_active_frequency: Any
    """Sync active frequency"""
    sync_disabled: Any
    """Sync disabled"""
    sync_errored_at: Any
    """Sync errored at"""
    sync_finished_at: Any
    """Sync finished at"""
    sync_method: Any
    """Sync method"""
    sync_outreach_folder: Any
    """Sync outreach folder"""
    sync_passive_frequency: Any
    """Sync passive frequency"""
    sync_permanent_error_at: Any
    """Sync permanent error at"""
    sync_success_at: Any
    """Sync success at"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""
    user: Any
    """User"""
    user_id: Any
    """User id"""
    username: Any
    """Username"""


class MailboxesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    auth_id: str
    """Auth id"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    editable: str
    """Editable"""
    email: str
    """Email"""
    email_hash: str
    """Email hash"""
    email_provider: str
    """Email provider"""
    email_signature: str
    """Email signature"""
    ews_custom_search_folder: str
    """Ews custom search folder"""
    ews_delegate_sync: str
    """Ews delegate sync"""
    ews_endpoint: str
    """Ews endpoint"""
    ews_impersonation: str
    """Ews impersonation"""
    ews_ssl_verify_mode: str
    """Ews ssl verify mode"""
    exchange_version: str
    """Exchange version"""
    id: str
    """Unique mailbox identifier"""
    imap_host: str
    """Imap host"""
    imap_port: str
    """Imap port"""
    imap_ssl: str
    """Imap ssl"""
    mail_aliases: str
    """Mail aliases"""
    mailings: str
    """Mailings"""
    max_emails_per_day: str
    """Max emails per day"""
    max_mailings_per_day: str
    """Max mailings per day"""
    max_mailings_per_week: str
    """Max mailings per week"""
    opt_out_message: str
    """Opt out message"""
    opt_out_signature: str
    """Opt out signature"""
    prospect_email_exclusions: str
    """Prospect email exclusions"""
    provider_id: str
    """Provider id"""
    provider_type: str
    """Provider type"""
    send_disabled: str
    """Send disabled"""
    send_errored_at: str
    """Send errored at"""
    send_max_retries: str
    """Send max retries"""
    send_method: str
    """Send method"""
    send_period: str
    """Send period"""
    send_permanent_error_at: str
    """Send permanent error at"""
    send_requires_sync: str
    """Send requires sync"""
    send_success_at: str
    """Send success at"""
    send_threshold: str
    """Send threshold"""
    sendgrid_webhook_url: str
    """Sendgrid webhook url"""
    smtp_host: str
    """Smtp host"""
    smtp_port: str
    """Smtp port"""
    smtp_ssl: str
    """Smtp ssl"""
    smtp_username: str
    """Smtp username"""
    sync_active_frequency: str
    """Sync active frequency"""
    sync_disabled: str
    """Sync disabled"""
    sync_errored_at: str
    """Sync errored at"""
    sync_finished_at: str
    """Sync finished at"""
    sync_method: str
    """Sync method"""
    sync_outreach_folder: str
    """Sync outreach folder"""
    sync_passive_frequency: str
    """Sync passive frequency"""
    sync_permanent_error_at: str
    """Sync permanent error at"""
    sync_success_at: str
    """Sync success at"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""
    user: str
    """User"""
    user_id: str
    """User id"""
    username: str
    """Username"""


class MailboxesSortFilter(TypedDict, total=False):
    """Available fields for sorting mailboxes search results."""
    auth_id: AirbyteSortOrder
    """Auth id"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    editable: AirbyteSortOrder
    """Editable"""
    email: AirbyteSortOrder
    """Email"""
    email_hash: AirbyteSortOrder
    """Email hash"""
    email_provider: AirbyteSortOrder
    """Email provider"""
    email_signature: AirbyteSortOrder
    """Email signature"""
    ews_custom_search_folder: AirbyteSortOrder
    """Ews custom search folder"""
    ews_delegate_sync: AirbyteSortOrder
    """Ews delegate sync"""
    ews_endpoint: AirbyteSortOrder
    """Ews endpoint"""
    ews_impersonation: AirbyteSortOrder
    """Ews impersonation"""
    ews_ssl_verify_mode: AirbyteSortOrder
    """Ews ssl verify mode"""
    exchange_version: AirbyteSortOrder
    """Exchange version"""
    id: AirbyteSortOrder
    """Unique mailbox identifier"""
    imap_host: AirbyteSortOrder
    """Imap host"""
    imap_port: AirbyteSortOrder
    """Imap port"""
    imap_ssl: AirbyteSortOrder
    """Imap ssl"""
    mail_aliases: AirbyteSortOrder
    """Mail aliases"""
    mailings: AirbyteSortOrder
    """Mailings"""
    max_emails_per_day: AirbyteSortOrder
    """Max emails per day"""
    max_mailings_per_day: AirbyteSortOrder
    """Max mailings per day"""
    max_mailings_per_week: AirbyteSortOrder
    """Max mailings per week"""
    opt_out_message: AirbyteSortOrder
    """Opt out message"""
    opt_out_signature: AirbyteSortOrder
    """Opt out signature"""
    prospect_email_exclusions: AirbyteSortOrder
    """Prospect email exclusions"""
    provider_id: AirbyteSortOrder
    """Provider id"""
    provider_type: AirbyteSortOrder
    """Provider type"""
    send_disabled: AirbyteSortOrder
    """Send disabled"""
    send_errored_at: AirbyteSortOrder
    """Send errored at"""
    send_max_retries: AirbyteSortOrder
    """Send max retries"""
    send_method: AirbyteSortOrder
    """Send method"""
    send_period: AirbyteSortOrder
    """Send period"""
    send_permanent_error_at: AirbyteSortOrder
    """Send permanent error at"""
    send_requires_sync: AirbyteSortOrder
    """Send requires sync"""
    send_success_at: AirbyteSortOrder
    """Send success at"""
    send_threshold: AirbyteSortOrder
    """Send threshold"""
    sendgrid_webhook_url: AirbyteSortOrder
    """Sendgrid webhook url"""
    smtp_host: AirbyteSortOrder
    """Smtp host"""
    smtp_port: AirbyteSortOrder
    """Smtp port"""
    smtp_ssl: AirbyteSortOrder
    """Smtp ssl"""
    smtp_username: AirbyteSortOrder
    """Smtp username"""
    sync_active_frequency: AirbyteSortOrder
    """Sync active frequency"""
    sync_disabled: AirbyteSortOrder
    """Sync disabled"""
    sync_errored_at: AirbyteSortOrder
    """Sync errored at"""
    sync_finished_at: AirbyteSortOrder
    """Sync finished at"""
    sync_method: AirbyteSortOrder
    """Sync method"""
    sync_outreach_folder: AirbyteSortOrder
    """Sync outreach folder"""
    sync_passive_frequency: AirbyteSortOrder
    """Sync passive frequency"""
    sync_permanent_error_at: AirbyteSortOrder
    """Sync permanent error at"""
    sync_success_at: AirbyteSortOrder
    """Sync success at"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""
    user: AirbyteSortOrder
    """User"""
    user_id: AirbyteSortOrder
    """User id"""
    username: AirbyteSortOrder
    """Username"""


# Entity-specific condition types for mailboxes
class MailboxesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MailboxesSearchFilter


class MailboxesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MailboxesSearchFilter


class MailboxesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MailboxesSearchFilter


class MailboxesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MailboxesSearchFilter


class MailboxesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MailboxesSearchFilter


class MailboxesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MailboxesSearchFilter


class MailboxesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: MailboxesStringFilter


class MailboxesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: MailboxesStringFilter


class MailboxesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MailboxesStringFilter


class MailboxesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MailboxesStringFilter


class MailboxesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: MailboxesAnyValueFilter


class MailboxesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: MailboxesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MailboxesInCondition = TypedDict("MailboxesInCondition", {"in": MailboxesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MailboxesNotCondition = TypedDict("MailboxesNotCondition", {"not": "MailboxesCondition"}, total=False)
"""Negates the nested condition."""

MailboxesAndCondition = TypedDict("MailboxesAndCondition", {"and": "list[MailboxesCondition]"}, total=False)
"""True if all nested conditions are true."""

MailboxesOrCondition = TypedDict("MailboxesOrCondition", {"or": "list[MailboxesCondition]"}, total=False)
"""True if any nested condition is true."""

MailboxesAnyCondition = TypedDict("MailboxesAnyCondition", {"any": MailboxesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all mailboxes condition types
MailboxesCondition = (
    MailboxesEqCondition
    | MailboxesNeqCondition
    | MailboxesGtCondition
    | MailboxesGteCondition
    | MailboxesLtCondition
    | MailboxesLteCondition
    | MailboxesInCondition
    | MailboxesStartswithCondition
    | MailboxesEndswithCondition
    | MailboxesFuzzyCondition
    | MailboxesKeywordCondition
    | MailboxesContainsCondition
    | MailboxesArrayContainsCondition
    | MailboxesNotCondition
    | MailboxesAndCondition
    | MailboxesOrCondition
    | MailboxesAnyCondition
)


class MailboxesSearchQuery(TypedDict, total=False):
    """Search query for mailboxes entity."""
    filter: MailboxesCondition
    sort: list[MailboxesSortFilter]


# ===== OPPORTUNITIES SEARCH TYPES =====

class OpportunitiesSearchFilter(TypedDict, total=False):
    """Available fields for filtering opportunities search queries."""
    account: list[Any] | None
    """Account"""
    amount: int | None
    """Amount"""
    assigned_teams: list[Any] | None
    """Assigned teams"""
    assigned_users: list[Any] | None
    """Assigned users"""
    close_date: str | None
    """Close date"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    currency_type: str | None
    """Currency type"""
    custom1: str | None
    """Custom field 1"""
    custom10: str | None
    """Custom field 10"""
    custom100: str | None
    """Custom field 100"""
    custom101: str | None
    """Custom field 101"""
    custom102: str | None
    """Custom field 102"""
    custom103: str | None
    """Custom field 103"""
    custom104: str | None
    """Custom field 104"""
    custom105: str | None
    """Custom field 105"""
    custom106: str | None
    """Custom field 106"""
    custom107: str | None
    """Custom field 107"""
    custom108: str | None
    """Custom field 108"""
    custom109: str | None
    """Custom field 109"""
    custom11: str | None
    """Custom field 11"""
    custom110: str | None
    """Custom field 110"""
    custom111: str | None
    """Custom field 111"""
    custom112: str | None
    """Custom field 112"""
    custom113: str | None
    """Custom field 113"""
    custom114: str | None
    """Custom field 114"""
    custom115: str | None
    """Custom field 115"""
    custom116: str | None
    """Custom field 116"""
    custom117: str | None
    """Custom field 117"""
    custom118: str | None
    """Custom field 118"""
    custom119: str | None
    """Custom field 119"""
    custom12: str | None
    """Custom field 12"""
    custom120: str | None
    """Custom field 120"""
    custom121: str | None
    """Custom field 121"""
    custom122: str | None
    """Custom field 122"""
    custom123: str | None
    """Custom field 123"""
    custom124: str | None
    """Custom field 124"""
    custom125: str | None
    """Custom field 125"""
    custom126: str | None
    """Custom field 126"""
    custom127: str | None
    """Custom field 127"""
    custom128: str | None
    """Custom field 128"""
    custom129: str | None
    """Custom field 129"""
    custom13: str | None
    """Custom field 13"""
    custom130: str | None
    """Custom field 130"""
    custom131: str | None
    """Custom field 131"""
    custom132: str | None
    """Custom field 132"""
    custom133: str | None
    """Custom field 133"""
    custom134: str | None
    """Custom field 134"""
    custom135: str | None
    """Custom field 135"""
    custom136: str | None
    """Custom field 136"""
    custom137: str | None
    """Custom field 137"""
    custom138: str | None
    """Custom field 138"""
    custom139: str | None
    """Custom field 139"""
    custom14: str | None
    """Custom field 14"""
    custom140: str | None
    """Custom field 140"""
    custom141: str | None
    """Custom field 141"""
    custom142: str | None
    """Custom field 142"""
    custom143: str | None
    """Custom field 143"""
    custom144: str | None
    """Custom field 144"""
    custom145: str | None
    """Custom field 145"""
    custom146: str | None
    """Custom field 146"""
    custom147: str | None
    """Custom field 147"""
    custom148: str | None
    """Custom field 148"""
    custom149: str | None
    """Custom field 149"""
    custom15: str | None
    """Custom field 15"""
    custom150: str | None
    """Custom field 150"""
    custom16: str | None
    """Custom field 16"""
    custom17: str | None
    """Custom field 17"""
    custom18: str | None
    """Custom field 18"""
    custom19: str | None
    """Custom field 19"""
    custom2: str | None
    """Custom field 2"""
    custom20: str | None
    """Custom field 20"""
    custom21: str | None
    """Custom field 21"""
    custom22: str | None
    """Custom field 22"""
    custom23: str | None
    """Custom field 23"""
    custom24: str | None
    """Custom field 24"""
    custom25: str | None
    """Custom field 25"""
    custom26: str | None
    """Custom field 26"""
    custom27: str | None
    """Custom field 27"""
    custom28: str | None
    """Custom field 28"""
    custom29: str | None
    """Custom field 29"""
    custom3: str | None
    """Custom field 3"""
    custom30: str | None
    """Custom field 30"""
    custom31: str | None
    """Custom field 31"""
    custom32: str | None
    """Custom field 32"""
    custom33: str | None
    """Custom field 33"""
    custom34: str | None
    """Custom field 34"""
    custom35: str | None
    """Custom field 35"""
    custom36: str | None
    """Custom field 36"""
    custom37: str | None
    """Custom field 37"""
    custom38: str | None
    """Custom field 38"""
    custom39: str | None
    """Custom field 39"""
    custom4: str | None
    """Custom field 4"""
    custom40: str | None
    """Custom field 40"""
    custom41: str | None
    """Custom field 41"""
    custom42: str | None
    """Custom field 42"""
    custom43: str | None
    """Custom field 43"""
    custom44: str | None
    """Custom field 44"""
    custom45: str | None
    """Custom field 45"""
    custom46: str | None
    """Custom field 46"""
    custom47: str | None
    """Custom field 47"""
    custom48: str | None
    """Custom field 48"""
    custom49: str | None
    """Custom field 49"""
    custom5: str | None
    """Custom field 5"""
    custom50: str | None
    """Custom field 50"""
    custom51: str | None
    """Custom field 51"""
    custom52: str | None
    """Custom field 52"""
    custom53: str | None
    """Custom field 53"""
    custom54: str | None
    """Custom field 54"""
    custom55: str | None
    """Custom field 55"""
    custom56: str | None
    """Custom field 56"""
    custom57: str | None
    """Custom field 57"""
    custom58: str | None
    """Custom field 58"""
    custom59: str | None
    """Custom field 59"""
    custom6: str | None
    """Custom field 6"""
    custom60: str | None
    """Custom field 60"""
    custom61: str | None
    """Custom field 61"""
    custom62: str | None
    """Custom field 62"""
    custom63: str | None
    """Custom field 63"""
    custom64: str | None
    """Custom field 64"""
    custom65: str | None
    """Custom field 65"""
    custom66: str | None
    """Custom field 66"""
    custom67: str | None
    """Custom field 67"""
    custom68: str | None
    """Custom field 68"""
    custom69: str | None
    """Custom field 69"""
    custom7: str | None
    """Custom field 7"""
    custom70: str | None
    """Custom field 70"""
    custom71: str | None
    """Custom field 71"""
    custom72: str | None
    """Custom field 72"""
    custom73: str | None
    """Custom field 73"""
    custom74: str | None
    """Custom field 74"""
    custom75: str | None
    """Custom field 75"""
    custom76: str | None
    """Custom field 76"""
    custom77: str | None
    """Custom field 77"""
    custom78: str | None
    """Custom field 78"""
    custom79: str | None
    """Custom field 79"""
    custom8: str | None
    """Custom field 8"""
    custom80: str | None
    """Custom field 80"""
    custom81: str | None
    """Custom field 81"""
    custom82: str | None
    """Custom field 82"""
    custom83: str | None
    """Custom field 83"""
    custom84: str | None
    """Custom field 84"""
    custom85: str | None
    """Custom field 85"""
    custom86: str | None
    """Custom field 86"""
    custom87: str | None
    """Custom field 87"""
    custom88: str | None
    """Custom field 88"""
    custom89: str | None
    """Custom field 89"""
    custom9: str | None
    """Custom field 9"""
    custom90: str | None
    """Custom field 90"""
    custom91: str | None
    """Custom field 91"""
    custom92: str | None
    """Custom field 92"""
    custom93: str | None
    """Custom field 93"""
    custom94: str | None
    """Custom field 94"""
    custom95: str | None
    """Custom field 95"""
    custom96: str | None
    """Custom field 96"""
    custom97: str | None
    """Custom field 97"""
    custom98: str | None
    """Custom field 98"""
    custom99: str | None
    """Custom field 99"""
    default_plugin_mapping: list[Any] | None
    """Default plugin mapping"""
    description: str | None
    """Description"""
    external_created_at: str | None
    """External created at"""
    external_creator: list[Any] | None
    """External creator"""
    favorites: list[Any] | None
    """Favorites"""
    health_category: str | None
    """Health category"""
    health_score: int | None
    """Health score"""
    id: int | None
    """Unique opportunity identifier"""
    map_link: str | None
    """Map link"""
    map_next_steps: str | None
    """Map next steps"""
    map_number_of_overdue_tasks: int | None
    """Map number of overdue tasks"""
    map_status: str | None
    """Map status"""
    name: str | None
    """Name"""
    next_step: str | None
    """Next step"""
    opportunity_health_factors: list[Any] | None
    """Opportunity health factors"""
    opportunity_stage: list[Any] | None
    """Opportunity stage"""
    opportunity_type: str | None
    """Opportunity type"""
    owner: list[Any] | None
    """Owner"""
    primary_prospect: list[Any] | None
    """Primary prospect"""
    probability: int | None
    """Probability"""
    prospecting_rep_id: str | None
    """Prospecting rep id"""
    prospects: list[Any] | None
    """Prospects"""
    sharing_team_id: str | None
    """Sharing team id"""
    stage: list[Any] | None
    """Stage"""
    tags: list[Any] | None
    """Tags"""
    touched_at: str | None
    """Touched at"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""


class OpportunitiesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account: list[list[Any]]
    """Account"""
    amount: list[int]
    """Amount"""
    assigned_teams: list[list[Any]]
    """Assigned teams"""
    assigned_users: list[list[Any]]
    """Assigned users"""
    close_date: list[str]
    """Close date"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    currency_type: list[str]
    """Currency type"""
    custom1: list[str]
    """Custom field 1"""
    custom10: list[str]
    """Custom field 10"""
    custom100: list[str]
    """Custom field 100"""
    custom101: list[str]
    """Custom field 101"""
    custom102: list[str]
    """Custom field 102"""
    custom103: list[str]
    """Custom field 103"""
    custom104: list[str]
    """Custom field 104"""
    custom105: list[str]
    """Custom field 105"""
    custom106: list[str]
    """Custom field 106"""
    custom107: list[str]
    """Custom field 107"""
    custom108: list[str]
    """Custom field 108"""
    custom109: list[str]
    """Custom field 109"""
    custom11: list[str]
    """Custom field 11"""
    custom110: list[str]
    """Custom field 110"""
    custom111: list[str]
    """Custom field 111"""
    custom112: list[str]
    """Custom field 112"""
    custom113: list[str]
    """Custom field 113"""
    custom114: list[str]
    """Custom field 114"""
    custom115: list[str]
    """Custom field 115"""
    custom116: list[str]
    """Custom field 116"""
    custom117: list[str]
    """Custom field 117"""
    custom118: list[str]
    """Custom field 118"""
    custom119: list[str]
    """Custom field 119"""
    custom12: list[str]
    """Custom field 12"""
    custom120: list[str]
    """Custom field 120"""
    custom121: list[str]
    """Custom field 121"""
    custom122: list[str]
    """Custom field 122"""
    custom123: list[str]
    """Custom field 123"""
    custom124: list[str]
    """Custom field 124"""
    custom125: list[str]
    """Custom field 125"""
    custom126: list[str]
    """Custom field 126"""
    custom127: list[str]
    """Custom field 127"""
    custom128: list[str]
    """Custom field 128"""
    custom129: list[str]
    """Custom field 129"""
    custom13: list[str]
    """Custom field 13"""
    custom130: list[str]
    """Custom field 130"""
    custom131: list[str]
    """Custom field 131"""
    custom132: list[str]
    """Custom field 132"""
    custom133: list[str]
    """Custom field 133"""
    custom134: list[str]
    """Custom field 134"""
    custom135: list[str]
    """Custom field 135"""
    custom136: list[str]
    """Custom field 136"""
    custom137: list[str]
    """Custom field 137"""
    custom138: list[str]
    """Custom field 138"""
    custom139: list[str]
    """Custom field 139"""
    custom14: list[str]
    """Custom field 14"""
    custom140: list[str]
    """Custom field 140"""
    custom141: list[str]
    """Custom field 141"""
    custom142: list[str]
    """Custom field 142"""
    custom143: list[str]
    """Custom field 143"""
    custom144: list[str]
    """Custom field 144"""
    custom145: list[str]
    """Custom field 145"""
    custom146: list[str]
    """Custom field 146"""
    custom147: list[str]
    """Custom field 147"""
    custom148: list[str]
    """Custom field 148"""
    custom149: list[str]
    """Custom field 149"""
    custom15: list[str]
    """Custom field 15"""
    custom150: list[str]
    """Custom field 150"""
    custom16: list[str]
    """Custom field 16"""
    custom17: list[str]
    """Custom field 17"""
    custom18: list[str]
    """Custom field 18"""
    custom19: list[str]
    """Custom field 19"""
    custom2: list[str]
    """Custom field 2"""
    custom20: list[str]
    """Custom field 20"""
    custom21: list[str]
    """Custom field 21"""
    custom22: list[str]
    """Custom field 22"""
    custom23: list[str]
    """Custom field 23"""
    custom24: list[str]
    """Custom field 24"""
    custom25: list[str]
    """Custom field 25"""
    custom26: list[str]
    """Custom field 26"""
    custom27: list[str]
    """Custom field 27"""
    custom28: list[str]
    """Custom field 28"""
    custom29: list[str]
    """Custom field 29"""
    custom3: list[str]
    """Custom field 3"""
    custom30: list[str]
    """Custom field 30"""
    custom31: list[str]
    """Custom field 31"""
    custom32: list[str]
    """Custom field 32"""
    custom33: list[str]
    """Custom field 33"""
    custom34: list[str]
    """Custom field 34"""
    custom35: list[str]
    """Custom field 35"""
    custom36: list[str]
    """Custom field 36"""
    custom37: list[str]
    """Custom field 37"""
    custom38: list[str]
    """Custom field 38"""
    custom39: list[str]
    """Custom field 39"""
    custom4: list[str]
    """Custom field 4"""
    custom40: list[str]
    """Custom field 40"""
    custom41: list[str]
    """Custom field 41"""
    custom42: list[str]
    """Custom field 42"""
    custom43: list[str]
    """Custom field 43"""
    custom44: list[str]
    """Custom field 44"""
    custom45: list[str]
    """Custom field 45"""
    custom46: list[str]
    """Custom field 46"""
    custom47: list[str]
    """Custom field 47"""
    custom48: list[str]
    """Custom field 48"""
    custom49: list[str]
    """Custom field 49"""
    custom5: list[str]
    """Custom field 5"""
    custom50: list[str]
    """Custom field 50"""
    custom51: list[str]
    """Custom field 51"""
    custom52: list[str]
    """Custom field 52"""
    custom53: list[str]
    """Custom field 53"""
    custom54: list[str]
    """Custom field 54"""
    custom55: list[str]
    """Custom field 55"""
    custom56: list[str]
    """Custom field 56"""
    custom57: list[str]
    """Custom field 57"""
    custom58: list[str]
    """Custom field 58"""
    custom59: list[str]
    """Custom field 59"""
    custom6: list[str]
    """Custom field 6"""
    custom60: list[str]
    """Custom field 60"""
    custom61: list[str]
    """Custom field 61"""
    custom62: list[str]
    """Custom field 62"""
    custom63: list[str]
    """Custom field 63"""
    custom64: list[str]
    """Custom field 64"""
    custom65: list[str]
    """Custom field 65"""
    custom66: list[str]
    """Custom field 66"""
    custom67: list[str]
    """Custom field 67"""
    custom68: list[str]
    """Custom field 68"""
    custom69: list[str]
    """Custom field 69"""
    custom7: list[str]
    """Custom field 7"""
    custom70: list[str]
    """Custom field 70"""
    custom71: list[str]
    """Custom field 71"""
    custom72: list[str]
    """Custom field 72"""
    custom73: list[str]
    """Custom field 73"""
    custom74: list[str]
    """Custom field 74"""
    custom75: list[str]
    """Custom field 75"""
    custom76: list[str]
    """Custom field 76"""
    custom77: list[str]
    """Custom field 77"""
    custom78: list[str]
    """Custom field 78"""
    custom79: list[str]
    """Custom field 79"""
    custom8: list[str]
    """Custom field 8"""
    custom80: list[str]
    """Custom field 80"""
    custom81: list[str]
    """Custom field 81"""
    custom82: list[str]
    """Custom field 82"""
    custom83: list[str]
    """Custom field 83"""
    custom84: list[str]
    """Custom field 84"""
    custom85: list[str]
    """Custom field 85"""
    custom86: list[str]
    """Custom field 86"""
    custom87: list[str]
    """Custom field 87"""
    custom88: list[str]
    """Custom field 88"""
    custom89: list[str]
    """Custom field 89"""
    custom9: list[str]
    """Custom field 9"""
    custom90: list[str]
    """Custom field 90"""
    custom91: list[str]
    """Custom field 91"""
    custom92: list[str]
    """Custom field 92"""
    custom93: list[str]
    """Custom field 93"""
    custom94: list[str]
    """Custom field 94"""
    custom95: list[str]
    """Custom field 95"""
    custom96: list[str]
    """Custom field 96"""
    custom97: list[str]
    """Custom field 97"""
    custom98: list[str]
    """Custom field 98"""
    custom99: list[str]
    """Custom field 99"""
    default_plugin_mapping: list[list[Any]]
    """Default plugin mapping"""
    description: list[str]
    """Description"""
    external_created_at: list[str]
    """External created at"""
    external_creator: list[list[Any]]
    """External creator"""
    favorites: list[list[Any]]
    """Favorites"""
    health_category: list[str]
    """Health category"""
    health_score: list[int]
    """Health score"""
    id: list[int]
    """Unique opportunity identifier"""
    map_link: list[str]
    """Map link"""
    map_next_steps: list[str]
    """Map next steps"""
    map_number_of_overdue_tasks: list[int]
    """Map number of overdue tasks"""
    map_status: list[str]
    """Map status"""
    name: list[str]
    """Name"""
    next_step: list[str]
    """Next step"""
    opportunity_health_factors: list[list[Any]]
    """Opportunity health factors"""
    opportunity_stage: list[list[Any]]
    """Opportunity stage"""
    opportunity_type: list[str]
    """Opportunity type"""
    owner: list[list[Any]]
    """Owner"""
    primary_prospect: list[list[Any]]
    """Primary prospect"""
    probability: list[int]
    """Probability"""
    prospecting_rep_id: list[str]
    """Prospecting rep id"""
    prospects: list[list[Any]]
    """Prospects"""
    sharing_team_id: list[str]
    """Sharing team id"""
    stage: list[list[Any]]
    """Stage"""
    tags: list[list[Any]]
    """Tags"""
    touched_at: list[str]
    """Touched at"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""


class OpportunitiesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account: Any
    """Account"""
    amount: Any
    """Amount"""
    assigned_teams: Any
    """Assigned teams"""
    assigned_users: Any
    """Assigned users"""
    close_date: Any
    """Close date"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    currency_type: Any
    """Currency type"""
    custom1: Any
    """Custom field 1"""
    custom10: Any
    """Custom field 10"""
    custom100: Any
    """Custom field 100"""
    custom101: Any
    """Custom field 101"""
    custom102: Any
    """Custom field 102"""
    custom103: Any
    """Custom field 103"""
    custom104: Any
    """Custom field 104"""
    custom105: Any
    """Custom field 105"""
    custom106: Any
    """Custom field 106"""
    custom107: Any
    """Custom field 107"""
    custom108: Any
    """Custom field 108"""
    custom109: Any
    """Custom field 109"""
    custom11: Any
    """Custom field 11"""
    custom110: Any
    """Custom field 110"""
    custom111: Any
    """Custom field 111"""
    custom112: Any
    """Custom field 112"""
    custom113: Any
    """Custom field 113"""
    custom114: Any
    """Custom field 114"""
    custom115: Any
    """Custom field 115"""
    custom116: Any
    """Custom field 116"""
    custom117: Any
    """Custom field 117"""
    custom118: Any
    """Custom field 118"""
    custom119: Any
    """Custom field 119"""
    custom12: Any
    """Custom field 12"""
    custom120: Any
    """Custom field 120"""
    custom121: Any
    """Custom field 121"""
    custom122: Any
    """Custom field 122"""
    custom123: Any
    """Custom field 123"""
    custom124: Any
    """Custom field 124"""
    custom125: Any
    """Custom field 125"""
    custom126: Any
    """Custom field 126"""
    custom127: Any
    """Custom field 127"""
    custom128: Any
    """Custom field 128"""
    custom129: Any
    """Custom field 129"""
    custom13: Any
    """Custom field 13"""
    custom130: Any
    """Custom field 130"""
    custom131: Any
    """Custom field 131"""
    custom132: Any
    """Custom field 132"""
    custom133: Any
    """Custom field 133"""
    custom134: Any
    """Custom field 134"""
    custom135: Any
    """Custom field 135"""
    custom136: Any
    """Custom field 136"""
    custom137: Any
    """Custom field 137"""
    custom138: Any
    """Custom field 138"""
    custom139: Any
    """Custom field 139"""
    custom14: Any
    """Custom field 14"""
    custom140: Any
    """Custom field 140"""
    custom141: Any
    """Custom field 141"""
    custom142: Any
    """Custom field 142"""
    custom143: Any
    """Custom field 143"""
    custom144: Any
    """Custom field 144"""
    custom145: Any
    """Custom field 145"""
    custom146: Any
    """Custom field 146"""
    custom147: Any
    """Custom field 147"""
    custom148: Any
    """Custom field 148"""
    custom149: Any
    """Custom field 149"""
    custom15: Any
    """Custom field 15"""
    custom150: Any
    """Custom field 150"""
    custom16: Any
    """Custom field 16"""
    custom17: Any
    """Custom field 17"""
    custom18: Any
    """Custom field 18"""
    custom19: Any
    """Custom field 19"""
    custom2: Any
    """Custom field 2"""
    custom20: Any
    """Custom field 20"""
    custom21: Any
    """Custom field 21"""
    custom22: Any
    """Custom field 22"""
    custom23: Any
    """Custom field 23"""
    custom24: Any
    """Custom field 24"""
    custom25: Any
    """Custom field 25"""
    custom26: Any
    """Custom field 26"""
    custom27: Any
    """Custom field 27"""
    custom28: Any
    """Custom field 28"""
    custom29: Any
    """Custom field 29"""
    custom3: Any
    """Custom field 3"""
    custom30: Any
    """Custom field 30"""
    custom31: Any
    """Custom field 31"""
    custom32: Any
    """Custom field 32"""
    custom33: Any
    """Custom field 33"""
    custom34: Any
    """Custom field 34"""
    custom35: Any
    """Custom field 35"""
    custom36: Any
    """Custom field 36"""
    custom37: Any
    """Custom field 37"""
    custom38: Any
    """Custom field 38"""
    custom39: Any
    """Custom field 39"""
    custom4: Any
    """Custom field 4"""
    custom40: Any
    """Custom field 40"""
    custom41: Any
    """Custom field 41"""
    custom42: Any
    """Custom field 42"""
    custom43: Any
    """Custom field 43"""
    custom44: Any
    """Custom field 44"""
    custom45: Any
    """Custom field 45"""
    custom46: Any
    """Custom field 46"""
    custom47: Any
    """Custom field 47"""
    custom48: Any
    """Custom field 48"""
    custom49: Any
    """Custom field 49"""
    custom5: Any
    """Custom field 5"""
    custom50: Any
    """Custom field 50"""
    custom51: Any
    """Custom field 51"""
    custom52: Any
    """Custom field 52"""
    custom53: Any
    """Custom field 53"""
    custom54: Any
    """Custom field 54"""
    custom55: Any
    """Custom field 55"""
    custom56: Any
    """Custom field 56"""
    custom57: Any
    """Custom field 57"""
    custom58: Any
    """Custom field 58"""
    custom59: Any
    """Custom field 59"""
    custom6: Any
    """Custom field 6"""
    custom60: Any
    """Custom field 60"""
    custom61: Any
    """Custom field 61"""
    custom62: Any
    """Custom field 62"""
    custom63: Any
    """Custom field 63"""
    custom64: Any
    """Custom field 64"""
    custom65: Any
    """Custom field 65"""
    custom66: Any
    """Custom field 66"""
    custom67: Any
    """Custom field 67"""
    custom68: Any
    """Custom field 68"""
    custom69: Any
    """Custom field 69"""
    custom7: Any
    """Custom field 7"""
    custom70: Any
    """Custom field 70"""
    custom71: Any
    """Custom field 71"""
    custom72: Any
    """Custom field 72"""
    custom73: Any
    """Custom field 73"""
    custom74: Any
    """Custom field 74"""
    custom75: Any
    """Custom field 75"""
    custom76: Any
    """Custom field 76"""
    custom77: Any
    """Custom field 77"""
    custom78: Any
    """Custom field 78"""
    custom79: Any
    """Custom field 79"""
    custom8: Any
    """Custom field 8"""
    custom80: Any
    """Custom field 80"""
    custom81: Any
    """Custom field 81"""
    custom82: Any
    """Custom field 82"""
    custom83: Any
    """Custom field 83"""
    custom84: Any
    """Custom field 84"""
    custom85: Any
    """Custom field 85"""
    custom86: Any
    """Custom field 86"""
    custom87: Any
    """Custom field 87"""
    custom88: Any
    """Custom field 88"""
    custom89: Any
    """Custom field 89"""
    custom9: Any
    """Custom field 9"""
    custom90: Any
    """Custom field 90"""
    custom91: Any
    """Custom field 91"""
    custom92: Any
    """Custom field 92"""
    custom93: Any
    """Custom field 93"""
    custom94: Any
    """Custom field 94"""
    custom95: Any
    """Custom field 95"""
    custom96: Any
    """Custom field 96"""
    custom97: Any
    """Custom field 97"""
    custom98: Any
    """Custom field 98"""
    custom99: Any
    """Custom field 99"""
    default_plugin_mapping: Any
    """Default plugin mapping"""
    description: Any
    """Description"""
    external_created_at: Any
    """External created at"""
    external_creator: Any
    """External creator"""
    favorites: Any
    """Favorites"""
    health_category: Any
    """Health category"""
    health_score: Any
    """Health score"""
    id: Any
    """Unique opportunity identifier"""
    map_link: Any
    """Map link"""
    map_next_steps: Any
    """Map next steps"""
    map_number_of_overdue_tasks: Any
    """Map number of overdue tasks"""
    map_status: Any
    """Map status"""
    name: Any
    """Name"""
    next_step: Any
    """Next step"""
    opportunity_health_factors: Any
    """Opportunity health factors"""
    opportunity_stage: Any
    """Opportunity stage"""
    opportunity_type: Any
    """Opportunity type"""
    owner: Any
    """Owner"""
    primary_prospect: Any
    """Primary prospect"""
    probability: Any
    """Probability"""
    prospecting_rep_id: Any
    """Prospecting rep id"""
    prospects: Any
    """Prospects"""
    sharing_team_id: Any
    """Sharing team id"""
    stage: Any
    """Stage"""
    tags: Any
    """Tags"""
    touched_at: Any
    """Touched at"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""


class OpportunitiesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    account: str
    """Account"""
    amount: str
    """Amount"""
    assigned_teams: str
    """Assigned teams"""
    assigned_users: str
    """Assigned users"""
    close_date: str
    """Close date"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    currency_type: str
    """Currency type"""
    custom1: str
    """Custom field 1"""
    custom10: str
    """Custom field 10"""
    custom100: str
    """Custom field 100"""
    custom101: str
    """Custom field 101"""
    custom102: str
    """Custom field 102"""
    custom103: str
    """Custom field 103"""
    custom104: str
    """Custom field 104"""
    custom105: str
    """Custom field 105"""
    custom106: str
    """Custom field 106"""
    custom107: str
    """Custom field 107"""
    custom108: str
    """Custom field 108"""
    custom109: str
    """Custom field 109"""
    custom11: str
    """Custom field 11"""
    custom110: str
    """Custom field 110"""
    custom111: str
    """Custom field 111"""
    custom112: str
    """Custom field 112"""
    custom113: str
    """Custom field 113"""
    custom114: str
    """Custom field 114"""
    custom115: str
    """Custom field 115"""
    custom116: str
    """Custom field 116"""
    custom117: str
    """Custom field 117"""
    custom118: str
    """Custom field 118"""
    custom119: str
    """Custom field 119"""
    custom12: str
    """Custom field 12"""
    custom120: str
    """Custom field 120"""
    custom121: str
    """Custom field 121"""
    custom122: str
    """Custom field 122"""
    custom123: str
    """Custom field 123"""
    custom124: str
    """Custom field 124"""
    custom125: str
    """Custom field 125"""
    custom126: str
    """Custom field 126"""
    custom127: str
    """Custom field 127"""
    custom128: str
    """Custom field 128"""
    custom129: str
    """Custom field 129"""
    custom13: str
    """Custom field 13"""
    custom130: str
    """Custom field 130"""
    custom131: str
    """Custom field 131"""
    custom132: str
    """Custom field 132"""
    custom133: str
    """Custom field 133"""
    custom134: str
    """Custom field 134"""
    custom135: str
    """Custom field 135"""
    custom136: str
    """Custom field 136"""
    custom137: str
    """Custom field 137"""
    custom138: str
    """Custom field 138"""
    custom139: str
    """Custom field 139"""
    custom14: str
    """Custom field 14"""
    custom140: str
    """Custom field 140"""
    custom141: str
    """Custom field 141"""
    custom142: str
    """Custom field 142"""
    custom143: str
    """Custom field 143"""
    custom144: str
    """Custom field 144"""
    custom145: str
    """Custom field 145"""
    custom146: str
    """Custom field 146"""
    custom147: str
    """Custom field 147"""
    custom148: str
    """Custom field 148"""
    custom149: str
    """Custom field 149"""
    custom15: str
    """Custom field 15"""
    custom150: str
    """Custom field 150"""
    custom16: str
    """Custom field 16"""
    custom17: str
    """Custom field 17"""
    custom18: str
    """Custom field 18"""
    custom19: str
    """Custom field 19"""
    custom2: str
    """Custom field 2"""
    custom20: str
    """Custom field 20"""
    custom21: str
    """Custom field 21"""
    custom22: str
    """Custom field 22"""
    custom23: str
    """Custom field 23"""
    custom24: str
    """Custom field 24"""
    custom25: str
    """Custom field 25"""
    custom26: str
    """Custom field 26"""
    custom27: str
    """Custom field 27"""
    custom28: str
    """Custom field 28"""
    custom29: str
    """Custom field 29"""
    custom3: str
    """Custom field 3"""
    custom30: str
    """Custom field 30"""
    custom31: str
    """Custom field 31"""
    custom32: str
    """Custom field 32"""
    custom33: str
    """Custom field 33"""
    custom34: str
    """Custom field 34"""
    custom35: str
    """Custom field 35"""
    custom36: str
    """Custom field 36"""
    custom37: str
    """Custom field 37"""
    custom38: str
    """Custom field 38"""
    custom39: str
    """Custom field 39"""
    custom4: str
    """Custom field 4"""
    custom40: str
    """Custom field 40"""
    custom41: str
    """Custom field 41"""
    custom42: str
    """Custom field 42"""
    custom43: str
    """Custom field 43"""
    custom44: str
    """Custom field 44"""
    custom45: str
    """Custom field 45"""
    custom46: str
    """Custom field 46"""
    custom47: str
    """Custom field 47"""
    custom48: str
    """Custom field 48"""
    custom49: str
    """Custom field 49"""
    custom5: str
    """Custom field 5"""
    custom50: str
    """Custom field 50"""
    custom51: str
    """Custom field 51"""
    custom52: str
    """Custom field 52"""
    custom53: str
    """Custom field 53"""
    custom54: str
    """Custom field 54"""
    custom55: str
    """Custom field 55"""
    custom56: str
    """Custom field 56"""
    custom57: str
    """Custom field 57"""
    custom58: str
    """Custom field 58"""
    custom59: str
    """Custom field 59"""
    custom6: str
    """Custom field 6"""
    custom60: str
    """Custom field 60"""
    custom61: str
    """Custom field 61"""
    custom62: str
    """Custom field 62"""
    custom63: str
    """Custom field 63"""
    custom64: str
    """Custom field 64"""
    custom65: str
    """Custom field 65"""
    custom66: str
    """Custom field 66"""
    custom67: str
    """Custom field 67"""
    custom68: str
    """Custom field 68"""
    custom69: str
    """Custom field 69"""
    custom7: str
    """Custom field 7"""
    custom70: str
    """Custom field 70"""
    custom71: str
    """Custom field 71"""
    custom72: str
    """Custom field 72"""
    custom73: str
    """Custom field 73"""
    custom74: str
    """Custom field 74"""
    custom75: str
    """Custom field 75"""
    custom76: str
    """Custom field 76"""
    custom77: str
    """Custom field 77"""
    custom78: str
    """Custom field 78"""
    custom79: str
    """Custom field 79"""
    custom8: str
    """Custom field 8"""
    custom80: str
    """Custom field 80"""
    custom81: str
    """Custom field 81"""
    custom82: str
    """Custom field 82"""
    custom83: str
    """Custom field 83"""
    custom84: str
    """Custom field 84"""
    custom85: str
    """Custom field 85"""
    custom86: str
    """Custom field 86"""
    custom87: str
    """Custom field 87"""
    custom88: str
    """Custom field 88"""
    custom89: str
    """Custom field 89"""
    custom9: str
    """Custom field 9"""
    custom90: str
    """Custom field 90"""
    custom91: str
    """Custom field 91"""
    custom92: str
    """Custom field 92"""
    custom93: str
    """Custom field 93"""
    custom94: str
    """Custom field 94"""
    custom95: str
    """Custom field 95"""
    custom96: str
    """Custom field 96"""
    custom97: str
    """Custom field 97"""
    custom98: str
    """Custom field 98"""
    custom99: str
    """Custom field 99"""
    default_plugin_mapping: str
    """Default plugin mapping"""
    description: str
    """Description"""
    external_created_at: str
    """External created at"""
    external_creator: str
    """External creator"""
    favorites: str
    """Favorites"""
    health_category: str
    """Health category"""
    health_score: str
    """Health score"""
    id: str
    """Unique opportunity identifier"""
    map_link: str
    """Map link"""
    map_next_steps: str
    """Map next steps"""
    map_number_of_overdue_tasks: str
    """Map number of overdue tasks"""
    map_status: str
    """Map status"""
    name: str
    """Name"""
    next_step: str
    """Next step"""
    opportunity_health_factors: str
    """Opportunity health factors"""
    opportunity_stage: str
    """Opportunity stage"""
    opportunity_type: str
    """Opportunity type"""
    owner: str
    """Owner"""
    primary_prospect: str
    """Primary prospect"""
    probability: str
    """Probability"""
    prospecting_rep_id: str
    """Prospecting rep id"""
    prospects: str
    """Prospects"""
    sharing_team_id: str
    """Sharing team id"""
    stage: str
    """Stage"""
    tags: str
    """Tags"""
    touched_at: str
    """Touched at"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""


class OpportunitiesSortFilter(TypedDict, total=False):
    """Available fields for sorting opportunities search results."""
    account: AirbyteSortOrder
    """Account"""
    amount: AirbyteSortOrder
    """Amount"""
    assigned_teams: AirbyteSortOrder
    """Assigned teams"""
    assigned_users: AirbyteSortOrder
    """Assigned users"""
    close_date: AirbyteSortOrder
    """Close date"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    currency_type: AirbyteSortOrder
    """Currency type"""
    custom1: AirbyteSortOrder
    """Custom field 1"""
    custom10: AirbyteSortOrder
    """Custom field 10"""
    custom100: AirbyteSortOrder
    """Custom field 100"""
    custom101: AirbyteSortOrder
    """Custom field 101"""
    custom102: AirbyteSortOrder
    """Custom field 102"""
    custom103: AirbyteSortOrder
    """Custom field 103"""
    custom104: AirbyteSortOrder
    """Custom field 104"""
    custom105: AirbyteSortOrder
    """Custom field 105"""
    custom106: AirbyteSortOrder
    """Custom field 106"""
    custom107: AirbyteSortOrder
    """Custom field 107"""
    custom108: AirbyteSortOrder
    """Custom field 108"""
    custom109: AirbyteSortOrder
    """Custom field 109"""
    custom11: AirbyteSortOrder
    """Custom field 11"""
    custom110: AirbyteSortOrder
    """Custom field 110"""
    custom111: AirbyteSortOrder
    """Custom field 111"""
    custom112: AirbyteSortOrder
    """Custom field 112"""
    custom113: AirbyteSortOrder
    """Custom field 113"""
    custom114: AirbyteSortOrder
    """Custom field 114"""
    custom115: AirbyteSortOrder
    """Custom field 115"""
    custom116: AirbyteSortOrder
    """Custom field 116"""
    custom117: AirbyteSortOrder
    """Custom field 117"""
    custom118: AirbyteSortOrder
    """Custom field 118"""
    custom119: AirbyteSortOrder
    """Custom field 119"""
    custom12: AirbyteSortOrder
    """Custom field 12"""
    custom120: AirbyteSortOrder
    """Custom field 120"""
    custom121: AirbyteSortOrder
    """Custom field 121"""
    custom122: AirbyteSortOrder
    """Custom field 122"""
    custom123: AirbyteSortOrder
    """Custom field 123"""
    custom124: AirbyteSortOrder
    """Custom field 124"""
    custom125: AirbyteSortOrder
    """Custom field 125"""
    custom126: AirbyteSortOrder
    """Custom field 126"""
    custom127: AirbyteSortOrder
    """Custom field 127"""
    custom128: AirbyteSortOrder
    """Custom field 128"""
    custom129: AirbyteSortOrder
    """Custom field 129"""
    custom13: AirbyteSortOrder
    """Custom field 13"""
    custom130: AirbyteSortOrder
    """Custom field 130"""
    custom131: AirbyteSortOrder
    """Custom field 131"""
    custom132: AirbyteSortOrder
    """Custom field 132"""
    custom133: AirbyteSortOrder
    """Custom field 133"""
    custom134: AirbyteSortOrder
    """Custom field 134"""
    custom135: AirbyteSortOrder
    """Custom field 135"""
    custom136: AirbyteSortOrder
    """Custom field 136"""
    custom137: AirbyteSortOrder
    """Custom field 137"""
    custom138: AirbyteSortOrder
    """Custom field 138"""
    custom139: AirbyteSortOrder
    """Custom field 139"""
    custom14: AirbyteSortOrder
    """Custom field 14"""
    custom140: AirbyteSortOrder
    """Custom field 140"""
    custom141: AirbyteSortOrder
    """Custom field 141"""
    custom142: AirbyteSortOrder
    """Custom field 142"""
    custom143: AirbyteSortOrder
    """Custom field 143"""
    custom144: AirbyteSortOrder
    """Custom field 144"""
    custom145: AirbyteSortOrder
    """Custom field 145"""
    custom146: AirbyteSortOrder
    """Custom field 146"""
    custom147: AirbyteSortOrder
    """Custom field 147"""
    custom148: AirbyteSortOrder
    """Custom field 148"""
    custom149: AirbyteSortOrder
    """Custom field 149"""
    custom15: AirbyteSortOrder
    """Custom field 15"""
    custom150: AirbyteSortOrder
    """Custom field 150"""
    custom16: AirbyteSortOrder
    """Custom field 16"""
    custom17: AirbyteSortOrder
    """Custom field 17"""
    custom18: AirbyteSortOrder
    """Custom field 18"""
    custom19: AirbyteSortOrder
    """Custom field 19"""
    custom2: AirbyteSortOrder
    """Custom field 2"""
    custom20: AirbyteSortOrder
    """Custom field 20"""
    custom21: AirbyteSortOrder
    """Custom field 21"""
    custom22: AirbyteSortOrder
    """Custom field 22"""
    custom23: AirbyteSortOrder
    """Custom field 23"""
    custom24: AirbyteSortOrder
    """Custom field 24"""
    custom25: AirbyteSortOrder
    """Custom field 25"""
    custom26: AirbyteSortOrder
    """Custom field 26"""
    custom27: AirbyteSortOrder
    """Custom field 27"""
    custom28: AirbyteSortOrder
    """Custom field 28"""
    custom29: AirbyteSortOrder
    """Custom field 29"""
    custom3: AirbyteSortOrder
    """Custom field 3"""
    custom30: AirbyteSortOrder
    """Custom field 30"""
    custom31: AirbyteSortOrder
    """Custom field 31"""
    custom32: AirbyteSortOrder
    """Custom field 32"""
    custom33: AirbyteSortOrder
    """Custom field 33"""
    custom34: AirbyteSortOrder
    """Custom field 34"""
    custom35: AirbyteSortOrder
    """Custom field 35"""
    custom36: AirbyteSortOrder
    """Custom field 36"""
    custom37: AirbyteSortOrder
    """Custom field 37"""
    custom38: AirbyteSortOrder
    """Custom field 38"""
    custom39: AirbyteSortOrder
    """Custom field 39"""
    custom4: AirbyteSortOrder
    """Custom field 4"""
    custom40: AirbyteSortOrder
    """Custom field 40"""
    custom41: AirbyteSortOrder
    """Custom field 41"""
    custom42: AirbyteSortOrder
    """Custom field 42"""
    custom43: AirbyteSortOrder
    """Custom field 43"""
    custom44: AirbyteSortOrder
    """Custom field 44"""
    custom45: AirbyteSortOrder
    """Custom field 45"""
    custom46: AirbyteSortOrder
    """Custom field 46"""
    custom47: AirbyteSortOrder
    """Custom field 47"""
    custom48: AirbyteSortOrder
    """Custom field 48"""
    custom49: AirbyteSortOrder
    """Custom field 49"""
    custom5: AirbyteSortOrder
    """Custom field 5"""
    custom50: AirbyteSortOrder
    """Custom field 50"""
    custom51: AirbyteSortOrder
    """Custom field 51"""
    custom52: AirbyteSortOrder
    """Custom field 52"""
    custom53: AirbyteSortOrder
    """Custom field 53"""
    custom54: AirbyteSortOrder
    """Custom field 54"""
    custom55: AirbyteSortOrder
    """Custom field 55"""
    custom56: AirbyteSortOrder
    """Custom field 56"""
    custom57: AirbyteSortOrder
    """Custom field 57"""
    custom58: AirbyteSortOrder
    """Custom field 58"""
    custom59: AirbyteSortOrder
    """Custom field 59"""
    custom6: AirbyteSortOrder
    """Custom field 6"""
    custom60: AirbyteSortOrder
    """Custom field 60"""
    custom61: AirbyteSortOrder
    """Custom field 61"""
    custom62: AirbyteSortOrder
    """Custom field 62"""
    custom63: AirbyteSortOrder
    """Custom field 63"""
    custom64: AirbyteSortOrder
    """Custom field 64"""
    custom65: AirbyteSortOrder
    """Custom field 65"""
    custom66: AirbyteSortOrder
    """Custom field 66"""
    custom67: AirbyteSortOrder
    """Custom field 67"""
    custom68: AirbyteSortOrder
    """Custom field 68"""
    custom69: AirbyteSortOrder
    """Custom field 69"""
    custom7: AirbyteSortOrder
    """Custom field 7"""
    custom70: AirbyteSortOrder
    """Custom field 70"""
    custom71: AirbyteSortOrder
    """Custom field 71"""
    custom72: AirbyteSortOrder
    """Custom field 72"""
    custom73: AirbyteSortOrder
    """Custom field 73"""
    custom74: AirbyteSortOrder
    """Custom field 74"""
    custom75: AirbyteSortOrder
    """Custom field 75"""
    custom76: AirbyteSortOrder
    """Custom field 76"""
    custom77: AirbyteSortOrder
    """Custom field 77"""
    custom78: AirbyteSortOrder
    """Custom field 78"""
    custom79: AirbyteSortOrder
    """Custom field 79"""
    custom8: AirbyteSortOrder
    """Custom field 8"""
    custom80: AirbyteSortOrder
    """Custom field 80"""
    custom81: AirbyteSortOrder
    """Custom field 81"""
    custom82: AirbyteSortOrder
    """Custom field 82"""
    custom83: AirbyteSortOrder
    """Custom field 83"""
    custom84: AirbyteSortOrder
    """Custom field 84"""
    custom85: AirbyteSortOrder
    """Custom field 85"""
    custom86: AirbyteSortOrder
    """Custom field 86"""
    custom87: AirbyteSortOrder
    """Custom field 87"""
    custom88: AirbyteSortOrder
    """Custom field 88"""
    custom89: AirbyteSortOrder
    """Custom field 89"""
    custom9: AirbyteSortOrder
    """Custom field 9"""
    custom90: AirbyteSortOrder
    """Custom field 90"""
    custom91: AirbyteSortOrder
    """Custom field 91"""
    custom92: AirbyteSortOrder
    """Custom field 92"""
    custom93: AirbyteSortOrder
    """Custom field 93"""
    custom94: AirbyteSortOrder
    """Custom field 94"""
    custom95: AirbyteSortOrder
    """Custom field 95"""
    custom96: AirbyteSortOrder
    """Custom field 96"""
    custom97: AirbyteSortOrder
    """Custom field 97"""
    custom98: AirbyteSortOrder
    """Custom field 98"""
    custom99: AirbyteSortOrder
    """Custom field 99"""
    default_plugin_mapping: AirbyteSortOrder
    """Default plugin mapping"""
    description: AirbyteSortOrder
    """Description"""
    external_created_at: AirbyteSortOrder
    """External created at"""
    external_creator: AirbyteSortOrder
    """External creator"""
    favorites: AirbyteSortOrder
    """Favorites"""
    health_category: AirbyteSortOrder
    """Health category"""
    health_score: AirbyteSortOrder
    """Health score"""
    id: AirbyteSortOrder
    """Unique opportunity identifier"""
    map_link: AirbyteSortOrder
    """Map link"""
    map_next_steps: AirbyteSortOrder
    """Map next steps"""
    map_number_of_overdue_tasks: AirbyteSortOrder
    """Map number of overdue tasks"""
    map_status: AirbyteSortOrder
    """Map status"""
    name: AirbyteSortOrder
    """Name"""
    next_step: AirbyteSortOrder
    """Next step"""
    opportunity_health_factors: AirbyteSortOrder
    """Opportunity health factors"""
    opportunity_stage: AirbyteSortOrder
    """Opportunity stage"""
    opportunity_type: AirbyteSortOrder
    """Opportunity type"""
    owner: AirbyteSortOrder
    """Owner"""
    primary_prospect: AirbyteSortOrder
    """Primary prospect"""
    probability: AirbyteSortOrder
    """Probability"""
    prospecting_rep_id: AirbyteSortOrder
    """Prospecting rep id"""
    prospects: AirbyteSortOrder
    """Prospects"""
    sharing_team_id: AirbyteSortOrder
    """Sharing team id"""
    stage: AirbyteSortOrder
    """Stage"""
    tags: AirbyteSortOrder
    """Tags"""
    touched_at: AirbyteSortOrder
    """Touched at"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""


# Entity-specific condition types for opportunities
class OpportunitiesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OpportunitiesSearchFilter


class OpportunitiesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OpportunitiesSearchFilter


class OpportunitiesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OpportunitiesSearchFilter


class OpportunitiesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OpportunitiesSearchFilter


class OpportunitiesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OpportunitiesSearchFilter


class OpportunitiesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OpportunitiesSearchFilter


class OpportunitiesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: OpportunitiesStringFilter


class OpportunitiesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: OpportunitiesStringFilter


class OpportunitiesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OpportunitiesStringFilter


class OpportunitiesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OpportunitiesStringFilter


class OpportunitiesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: OpportunitiesAnyValueFilter


class OpportunitiesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: OpportunitiesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OpportunitiesInCondition = TypedDict("OpportunitiesInCondition", {"in": OpportunitiesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OpportunitiesNotCondition = TypedDict("OpportunitiesNotCondition", {"not": "OpportunitiesCondition"}, total=False)
"""Negates the nested condition."""

OpportunitiesAndCondition = TypedDict("OpportunitiesAndCondition", {"and": "list[OpportunitiesCondition]"}, total=False)
"""True if all nested conditions are true."""

OpportunitiesOrCondition = TypedDict("OpportunitiesOrCondition", {"or": "list[OpportunitiesCondition]"}, total=False)
"""True if any nested condition is true."""

OpportunitiesAnyCondition = TypedDict("OpportunitiesAnyCondition", {"any": OpportunitiesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all opportunities condition types
OpportunitiesCondition = (
    OpportunitiesEqCondition
    | OpportunitiesNeqCondition
    | OpportunitiesGtCondition
    | OpportunitiesGteCondition
    | OpportunitiesLtCondition
    | OpportunitiesLteCondition
    | OpportunitiesInCondition
    | OpportunitiesStartswithCondition
    | OpportunitiesEndswithCondition
    | OpportunitiesFuzzyCondition
    | OpportunitiesKeywordCondition
    | OpportunitiesContainsCondition
    | OpportunitiesArrayContainsCondition
    | OpportunitiesNotCondition
    | OpportunitiesAndCondition
    | OpportunitiesOrCondition
    | OpportunitiesAnyCondition
)


class OpportunitiesSearchQuery(TypedDict, total=False):
    """Search query for opportunities entity."""
    filter: OpportunitiesCondition
    sort: list[OpportunitiesSortFilter]


# ===== PERSONAS SEARCH TYPES =====

class PersonasSearchFilter(TypedDict, total=False):
    """Available fields for filtering personas search queries."""
    created_at: str | None
    """Created at"""
    description: str | None
    """Description"""
    id: int | None
    """Unique persona identifier"""
    name: str | None
    """Name"""
    prospects: list[Any] | None
    """Prospects"""
    updated_at: str | None
    """Updated at"""


class PersonasInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """Created at"""
    description: list[str]
    """Description"""
    id: list[int]
    """Unique persona identifier"""
    name: list[str]
    """Name"""
    prospects: list[list[Any]]
    """Prospects"""
    updated_at: list[str]
    """Updated at"""


class PersonasAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Created at"""
    description: Any
    """Description"""
    id: Any
    """Unique persona identifier"""
    name: Any
    """Name"""
    prospects: Any
    """Prospects"""
    updated_at: Any
    """Updated at"""


class PersonasStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    created_at: str
    """Created at"""
    description: str
    """Description"""
    id: str
    """Unique persona identifier"""
    name: str
    """Name"""
    prospects: str
    """Prospects"""
    updated_at: str
    """Updated at"""


class PersonasSortFilter(TypedDict, total=False):
    """Available fields for sorting personas search results."""
    created_at: AirbyteSortOrder
    """Created at"""
    description: AirbyteSortOrder
    """Description"""
    id: AirbyteSortOrder
    """Unique persona identifier"""
    name: AirbyteSortOrder
    """Name"""
    prospects: AirbyteSortOrder
    """Prospects"""
    updated_at: AirbyteSortOrder
    """Updated at"""


# Entity-specific condition types for personas
class PersonasEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PersonasSearchFilter


class PersonasNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PersonasSearchFilter


class PersonasGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PersonasSearchFilter


class PersonasGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PersonasSearchFilter


class PersonasLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PersonasSearchFilter


class PersonasLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PersonasSearchFilter


class PersonasStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: PersonasStringFilter


class PersonasEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: PersonasStringFilter


class PersonasFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PersonasStringFilter


class PersonasKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PersonasStringFilter


class PersonasContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: PersonasAnyValueFilter


class PersonasArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: PersonasAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PersonasInCondition = TypedDict("PersonasInCondition", {"in": PersonasInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PersonasNotCondition = TypedDict("PersonasNotCondition", {"not": "PersonasCondition"}, total=False)
"""Negates the nested condition."""

PersonasAndCondition = TypedDict("PersonasAndCondition", {"and": "list[PersonasCondition]"}, total=False)
"""True if all nested conditions are true."""

PersonasOrCondition = TypedDict("PersonasOrCondition", {"or": "list[PersonasCondition]"}, total=False)
"""True if any nested condition is true."""

PersonasAnyCondition = TypedDict("PersonasAnyCondition", {"any": PersonasAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all personas condition types
PersonasCondition = (
    PersonasEqCondition
    | PersonasNeqCondition
    | PersonasGtCondition
    | PersonasGteCondition
    | PersonasLtCondition
    | PersonasLteCondition
    | PersonasInCondition
    | PersonasStartswithCondition
    | PersonasEndswithCondition
    | PersonasFuzzyCondition
    | PersonasKeywordCondition
    | PersonasContainsCondition
    | PersonasArrayContainsCondition
    | PersonasNotCondition
    | PersonasAndCondition
    | PersonasOrCondition
    | PersonasAnyCondition
)


class PersonasSearchQuery(TypedDict, total=False):
    """Search query for personas entity."""
    filter: PersonasCondition
    sort: list[PersonasSortFilter]


# ===== PROSPECTS SEARCH TYPES =====

class ProspectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering prospects search queries."""
    account: list[Any] | None
    """Account"""
    account_name: str | None
    """Account name"""
    active_sequence_states: list[Any] | None
    """Active sequence states"""
    added_at: str | None
    """Added at"""
    address_city: str | None
    """Address city"""
    address_country: str | None
    """Address country"""
    address_state: str | None
    """Address state"""
    address_street: str | None
    """Address street"""
    address_street2: str | None
    """Address street2"""
    address_zip: str | None
    """Address zip"""
    angel_list_url: str | None
    """Angel list url"""
    assigned_teams: list[Any] | None
    """Assigned teams"""
    assigned_users: list[Any] | None
    """Assigned users"""
    available_at: str | None
    """Available at"""
    batches: list[Any] | None
    """Batches"""
    call_opted_out: bool | None
    """Call opted out"""
    calls: list[Any] | None
    """Calls"""
    calls_opt_status: str | None
    """Calls opt status"""
    calls_opted_at: str | None
    """Calls opted at"""
    campaign_name: str | None
    """Campaign name"""
    click_count: int | None
    """Click count"""
    company: str | None
    """Company"""
    company_followers: int | None
    """Company followers"""
    company_founded_at: str | None
    """Company founded at"""
    company_industry: str | None
    """Company industry"""
    company_linked_in: str | None
    """Company linked in"""
    company_linked_in_employees: str | None
    """Company linked in employees"""
    company_locality: str | None
    """Company locality"""
    company_natural: str | None
    """Company natural"""
    company_size: int | None
    """Company size"""
    company_start_date: str | None
    """Company start date"""
    company_type: str | None
    """Company type"""
    contact_histogram: list[Any] | None
    """Contact histogram"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    custom1: str | None
    """Custom field 1"""
    custom10: str | None
    """Custom field 10"""
    custom100: str | None
    """Custom field 100"""
    custom101: str | None
    """Custom field 101"""
    custom102: str | None
    """Custom field 102"""
    custom103: str | None
    """Custom field 103"""
    custom104: str | None
    """Custom field 104"""
    custom105: str | None
    """Custom field 105"""
    custom106: str | None
    """Custom field 106"""
    custom107: str | None
    """Custom field 107"""
    custom108: str | None
    """Custom field 108"""
    custom109: str | None
    """Custom field 109"""
    custom11: str | None
    """Custom field 11"""
    custom110: str | None
    """Custom field 110"""
    custom111: str | None
    """Custom field 111"""
    custom112: str | None
    """Custom field 112"""
    custom113: str | None
    """Custom field 113"""
    custom114: str | None
    """Custom field 114"""
    custom115: str | None
    """Custom field 115"""
    custom116: str | None
    """Custom field 116"""
    custom117: str | None
    """Custom field 117"""
    custom118: str | None
    """Custom field 118"""
    custom119: str | None
    """Custom field 119"""
    custom12: str | None
    """Custom field 12"""
    custom120: str | None
    """Custom field 120"""
    custom121: str | None
    """Custom field 121"""
    custom122: str | None
    """Custom field 122"""
    custom123: str | None
    """Custom field 123"""
    custom124: str | None
    """Custom field 124"""
    custom125: str | None
    """Custom field 125"""
    custom126: str | None
    """Custom field 126"""
    custom127: str | None
    """Custom field 127"""
    custom128: str | None
    """Custom field 128"""
    custom129: str | None
    """Custom field 129"""
    custom13: str | None
    """Custom field 13"""
    custom130: str | None
    """Custom field 130"""
    custom131: str | None
    """Custom field 131"""
    custom132: str | None
    """Custom field 132"""
    custom133: str | None
    """Custom field 133"""
    custom134: str | None
    """Custom field 134"""
    custom135: str | None
    """Custom field 135"""
    custom136: str | None
    """Custom field 136"""
    custom137: str | None
    """Custom field 137"""
    custom138: str | None
    """Custom field 138"""
    custom139: str | None
    """Custom field 139"""
    custom14: str | None
    """Custom field 14"""
    custom140: str | None
    """Custom field 140"""
    custom141: str | None
    """Custom field 141"""
    custom142: str | None
    """Custom field 142"""
    custom143: str | None
    """Custom field 143"""
    custom144: str | None
    """Custom field 144"""
    custom145: str | None
    """Custom field 145"""
    custom146: str | None
    """Custom field 146"""
    custom147: str | None
    """Custom field 147"""
    custom148: str | None
    """Custom field 148"""
    custom149: str | None
    """Custom field 149"""
    custom15: str | None
    """Custom field 15"""
    custom150: str | None
    """Custom field 150"""
    custom16: str | None
    """Custom field 16"""
    custom17: str | None
    """Custom field 17"""
    custom18: str | None
    """Custom field 18"""
    custom19: str | None
    """Custom field 19"""
    custom2: str | None
    """Custom field 2"""
    custom20: str | None
    """Custom field 20"""
    custom21: str | None
    """Custom field 21"""
    custom22: str | None
    """Custom field 22"""
    custom23: str | None
    """Custom field 23"""
    custom24: str | None
    """Custom field 24"""
    custom25: str | None
    """Custom field 25"""
    custom26: str | None
    """Custom field 26"""
    custom27: str | None
    """Custom field 27"""
    custom28: str | None
    """Custom field 28"""
    custom29: str | None
    """Custom field 29"""
    custom3: str | None
    """Custom field 3"""
    custom30: str | None
    """Custom field 30"""
    custom31: str | None
    """Custom field 31"""
    custom32: str | None
    """Custom field 32"""
    custom33: str | None
    """Custom field 33"""
    custom34: str | None
    """Custom field 34"""
    custom35: str | None
    """Custom field 35"""
    custom36: str | None
    """Custom field 36"""
    custom37: str | None
    """Custom field 37"""
    custom38: str | None
    """Custom field 38"""
    custom39: str | None
    """Custom field 39"""
    custom4: str | None
    """Custom field 4"""
    custom40: str | None
    """Custom field 40"""
    custom41: str | None
    """Custom field 41"""
    custom42: str | None
    """Custom field 42"""
    custom43: str | None
    """Custom field 43"""
    custom44: str | None
    """Custom field 44"""
    custom45: str | None
    """Custom field 45"""
    custom46: str | None
    """Custom field 46"""
    custom47: str | None
    """Custom field 47"""
    custom48: str | None
    """Custom field 48"""
    custom49: str | None
    """Custom field 49"""
    custom5: str | None
    """Custom field 5"""
    custom50: str | None
    """Custom field 50"""
    custom51: str | None
    """Custom field 51"""
    custom52: str | None
    """Custom field 52"""
    custom53: str | None
    """Custom field 53"""
    custom54: str | None
    """Custom field 54"""
    custom55: str | None
    """Custom field 55"""
    custom56: str | None
    """Custom field 56"""
    custom57: str | None
    """Custom field 57"""
    custom58: str | None
    """Custom field 58"""
    custom59: str | None
    """Custom field 59"""
    custom6: str | None
    """Custom field 6"""
    custom60: str | None
    """Custom field 60"""
    custom61: str | None
    """Custom field 61"""
    custom62: str | None
    """Custom field 62"""
    custom63: str | None
    """Custom field 63"""
    custom64: str | None
    """Custom field 64"""
    custom65: str | None
    """Custom field 65"""
    custom66: str | None
    """Custom field 66"""
    custom67: str | None
    """Custom field 67"""
    custom68: str | None
    """Custom field 68"""
    custom69: str | None
    """Custom field 69"""
    custom7: str | None
    """Custom field 7"""
    custom70: str | None
    """Custom field 70"""
    custom71: str | None
    """Custom field 71"""
    custom72: str | None
    """Custom field 72"""
    custom73: str | None
    """Custom field 73"""
    custom74: str | None
    """Custom field 74"""
    custom75: str | None
    """Custom field 75"""
    custom76: str | None
    """Custom field 76"""
    custom77: str | None
    """Custom field 77"""
    custom78: str | None
    """Custom field 78"""
    custom79: str | None
    """Custom field 79"""
    custom8: str | None
    """Custom field 8"""
    custom80: str | None
    """Custom field 80"""
    custom81: str | None
    """Custom field 81"""
    custom82: str | None
    """Custom field 82"""
    custom83: str | None
    """Custom field 83"""
    custom84: str | None
    """Custom field 84"""
    custom85: str | None
    """Custom field 85"""
    custom86: str | None
    """Custom field 86"""
    custom87: str | None
    """Custom field 87"""
    custom88: str | None
    """Custom field 88"""
    custom89: str | None
    """Custom field 89"""
    custom9: str | None
    """Custom field 9"""
    custom90: str | None
    """Custom field 90"""
    custom91: str | None
    """Custom field 91"""
    custom92: str | None
    """Custom field 92"""
    custom93: str | None
    """Custom field 93"""
    custom94: str | None
    """Custom field 94"""
    custom95: str | None
    """Custom field 95"""
    custom96: str | None
    """Custom field 96"""
    custom97: str | None
    """Custom field 97"""
    custom98: str | None
    """Custom field 98"""
    custom99: str | None
    """Custom field 99"""
    date_of_birth: str | None
    """Date of birth"""
    default_plugin_mapping: list[Any] | None
    """Default plugin mapping"""
    degree: str | None
    """Degree"""
    email_addresses: list[Any] | None
    """Email addresses"""
    email_contacts: list[Any] | None
    """Email contacts"""
    email_opted_out: bool | None
    """Email opted out"""
    emails: list[Any] | None
    """Emails"""
    emails_opt_status: str | None
    """Emails opt status"""
    emails_opted_at: str | None
    """Emails opted at"""
    engaged_at: str | None
    """Engaged at"""
    engaged_score: float | None
    """Engaged score"""
    event_name: str | None
    """Event name"""
    external_id: str | None
    """External id"""
    external_owner: str | None
    """External owner"""
    external_source: str | None
    """External source"""
    facebook_url: str | None
    """Facebook url"""
    favorites: list[Any] | None
    """Favorites"""
    first_name: str | None
    """First name"""
    gender: str | None
    """Gender"""
    github_url: str | None
    """Github url"""
    github_username: str | None
    """Github username"""
    google_plus_url: str | None
    """Google plus url"""
    graduation_date: str | None
    """Graduation date"""
    home_phones: list[Any] | None
    """Home phones"""
    id: int | None
    """Unique prospect identifier"""
    job_start_date: str | None
    """Job start date"""
    last_name: str | None
    """Last name"""
    linked_in_connections: int | None
    """Linked in connections"""
    linked_in_id: str | None
    """Linked in id"""
    linked_in_slug: str | None
    """Linked in slug"""
    linked_in_url: str | None
    """Linked in url"""
    mailings: list[Any] | None
    """Mailings"""
    middle_name: str | None
    """Middle name"""
    mobile_phones: list[Any] | None
    """Mobile phones"""
    name: str | None
    """Name"""
    nickname: str | None
    """Nickname"""
    occupation: str | None
    """Occupation"""
    open_count: int | None
    """Open count"""
    opportunities: list[Any] | None
    """Opportunities"""
    opportunity_prospect_roles: list[Any] | None
    """Opportunity prospect roles"""
    opted_out: bool | None
    """Opted out"""
    opted_out_at: str | None
    """Opted out at"""
    other_phones: list[Any] | None
    """Other phones"""
    owner: list[Any] | None
    """Owner"""
    persona: list[Any] | None
    """Persona"""
    persona_name: str | None
    """Persona name"""
    personal_note1: str | None
    """Personal note1"""
    personal_note2: str | None
    """Personal note2"""
    phone_numbers: list[Any] | None
    """Phone numbers"""
    preferred_contact: str | None
    """Preferred contact"""
    quora_url: str | None
    """Quora url"""
    region: str | None
    """Region"""
    reply_count: int | None
    """Reply count"""
    school: str | None
    """School"""
    score: float | None
    """Score"""
    sequence_states: list[Any] | None
    """Sequence states"""
    sharing_team_id: str | None
    """Sharing team id"""
    sms_opt_status: str | None
    """Sms opt status"""
    sms_opted_at: str | None
    """Sms opted at"""
    sms_opted_out: bool | None
    """Sms opted out"""
    source: str | None
    """Source"""
    specialties: str | None
    """Specialties"""
    stack_overflow_id: str | None
    """Stack overflow id"""
    stack_overflow_url: str | None
    """Stack overflow url"""
    stage: list[Any] | None
    """Stage"""
    stage_name: str | None
    """Stage name"""
    tags: list[Any] | None
    """Tags"""
    tasks: list[Any] | None
    """Tasks"""
    time_zone: str | None
    """Time zone"""
    time_zone_iana: str | None
    """Time zone iana"""
    time_zone_inferred: str | None
    """Time zone inferred"""
    title: str | None
    """Title"""
    touched_at: str | None
    """Touched at"""
    trashed_at: str | None
    """Trashed at"""
    trashed_by_account: list[Any] | None
    """Trashed by account"""
    twitter_url: str | None
    """Twitter url"""
    twitter_username: str | None
    """Twitter username"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""
    updater_id: int | None
    """Updater id"""
    updater_type: str | None
    """Updater type"""
    voip_phones: list[Any] | None
    """Voip phones"""
    website_url1: str | None
    """Website url1"""
    website_url2: str | None
    """Website url2"""
    website_url3: str | None
    """Website url3"""
    work_phones: list[Any] | None
    """Work phones"""


class ProspectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account: list[list[Any]]
    """Account"""
    account_name: list[str]
    """Account name"""
    active_sequence_states: list[list[Any]]
    """Active sequence states"""
    added_at: list[str]
    """Added at"""
    address_city: list[str]
    """Address city"""
    address_country: list[str]
    """Address country"""
    address_state: list[str]
    """Address state"""
    address_street: list[str]
    """Address street"""
    address_street2: list[str]
    """Address street2"""
    address_zip: list[str]
    """Address zip"""
    angel_list_url: list[str]
    """Angel list url"""
    assigned_teams: list[list[Any]]
    """Assigned teams"""
    assigned_users: list[list[Any]]
    """Assigned users"""
    available_at: list[str]
    """Available at"""
    batches: list[list[Any]]
    """Batches"""
    call_opted_out: list[bool]
    """Call opted out"""
    calls: list[list[Any]]
    """Calls"""
    calls_opt_status: list[str]
    """Calls opt status"""
    calls_opted_at: list[str]
    """Calls opted at"""
    campaign_name: list[str]
    """Campaign name"""
    click_count: list[int]
    """Click count"""
    company: list[str]
    """Company"""
    company_followers: list[int]
    """Company followers"""
    company_founded_at: list[str]
    """Company founded at"""
    company_industry: list[str]
    """Company industry"""
    company_linked_in: list[str]
    """Company linked in"""
    company_linked_in_employees: list[str]
    """Company linked in employees"""
    company_locality: list[str]
    """Company locality"""
    company_natural: list[str]
    """Company natural"""
    company_size: list[int]
    """Company size"""
    company_start_date: list[str]
    """Company start date"""
    company_type: list[str]
    """Company type"""
    contact_histogram: list[list[Any]]
    """Contact histogram"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    custom1: list[str]
    """Custom field 1"""
    custom10: list[str]
    """Custom field 10"""
    custom100: list[str]
    """Custom field 100"""
    custom101: list[str]
    """Custom field 101"""
    custom102: list[str]
    """Custom field 102"""
    custom103: list[str]
    """Custom field 103"""
    custom104: list[str]
    """Custom field 104"""
    custom105: list[str]
    """Custom field 105"""
    custom106: list[str]
    """Custom field 106"""
    custom107: list[str]
    """Custom field 107"""
    custom108: list[str]
    """Custom field 108"""
    custom109: list[str]
    """Custom field 109"""
    custom11: list[str]
    """Custom field 11"""
    custom110: list[str]
    """Custom field 110"""
    custom111: list[str]
    """Custom field 111"""
    custom112: list[str]
    """Custom field 112"""
    custom113: list[str]
    """Custom field 113"""
    custom114: list[str]
    """Custom field 114"""
    custom115: list[str]
    """Custom field 115"""
    custom116: list[str]
    """Custom field 116"""
    custom117: list[str]
    """Custom field 117"""
    custom118: list[str]
    """Custom field 118"""
    custom119: list[str]
    """Custom field 119"""
    custom12: list[str]
    """Custom field 12"""
    custom120: list[str]
    """Custom field 120"""
    custom121: list[str]
    """Custom field 121"""
    custom122: list[str]
    """Custom field 122"""
    custom123: list[str]
    """Custom field 123"""
    custom124: list[str]
    """Custom field 124"""
    custom125: list[str]
    """Custom field 125"""
    custom126: list[str]
    """Custom field 126"""
    custom127: list[str]
    """Custom field 127"""
    custom128: list[str]
    """Custom field 128"""
    custom129: list[str]
    """Custom field 129"""
    custom13: list[str]
    """Custom field 13"""
    custom130: list[str]
    """Custom field 130"""
    custom131: list[str]
    """Custom field 131"""
    custom132: list[str]
    """Custom field 132"""
    custom133: list[str]
    """Custom field 133"""
    custom134: list[str]
    """Custom field 134"""
    custom135: list[str]
    """Custom field 135"""
    custom136: list[str]
    """Custom field 136"""
    custom137: list[str]
    """Custom field 137"""
    custom138: list[str]
    """Custom field 138"""
    custom139: list[str]
    """Custom field 139"""
    custom14: list[str]
    """Custom field 14"""
    custom140: list[str]
    """Custom field 140"""
    custom141: list[str]
    """Custom field 141"""
    custom142: list[str]
    """Custom field 142"""
    custom143: list[str]
    """Custom field 143"""
    custom144: list[str]
    """Custom field 144"""
    custom145: list[str]
    """Custom field 145"""
    custom146: list[str]
    """Custom field 146"""
    custom147: list[str]
    """Custom field 147"""
    custom148: list[str]
    """Custom field 148"""
    custom149: list[str]
    """Custom field 149"""
    custom15: list[str]
    """Custom field 15"""
    custom150: list[str]
    """Custom field 150"""
    custom16: list[str]
    """Custom field 16"""
    custom17: list[str]
    """Custom field 17"""
    custom18: list[str]
    """Custom field 18"""
    custom19: list[str]
    """Custom field 19"""
    custom2: list[str]
    """Custom field 2"""
    custom20: list[str]
    """Custom field 20"""
    custom21: list[str]
    """Custom field 21"""
    custom22: list[str]
    """Custom field 22"""
    custom23: list[str]
    """Custom field 23"""
    custom24: list[str]
    """Custom field 24"""
    custom25: list[str]
    """Custom field 25"""
    custom26: list[str]
    """Custom field 26"""
    custom27: list[str]
    """Custom field 27"""
    custom28: list[str]
    """Custom field 28"""
    custom29: list[str]
    """Custom field 29"""
    custom3: list[str]
    """Custom field 3"""
    custom30: list[str]
    """Custom field 30"""
    custom31: list[str]
    """Custom field 31"""
    custom32: list[str]
    """Custom field 32"""
    custom33: list[str]
    """Custom field 33"""
    custom34: list[str]
    """Custom field 34"""
    custom35: list[str]
    """Custom field 35"""
    custom36: list[str]
    """Custom field 36"""
    custom37: list[str]
    """Custom field 37"""
    custom38: list[str]
    """Custom field 38"""
    custom39: list[str]
    """Custom field 39"""
    custom4: list[str]
    """Custom field 4"""
    custom40: list[str]
    """Custom field 40"""
    custom41: list[str]
    """Custom field 41"""
    custom42: list[str]
    """Custom field 42"""
    custom43: list[str]
    """Custom field 43"""
    custom44: list[str]
    """Custom field 44"""
    custom45: list[str]
    """Custom field 45"""
    custom46: list[str]
    """Custom field 46"""
    custom47: list[str]
    """Custom field 47"""
    custom48: list[str]
    """Custom field 48"""
    custom49: list[str]
    """Custom field 49"""
    custom5: list[str]
    """Custom field 5"""
    custom50: list[str]
    """Custom field 50"""
    custom51: list[str]
    """Custom field 51"""
    custom52: list[str]
    """Custom field 52"""
    custom53: list[str]
    """Custom field 53"""
    custom54: list[str]
    """Custom field 54"""
    custom55: list[str]
    """Custom field 55"""
    custom56: list[str]
    """Custom field 56"""
    custom57: list[str]
    """Custom field 57"""
    custom58: list[str]
    """Custom field 58"""
    custom59: list[str]
    """Custom field 59"""
    custom6: list[str]
    """Custom field 6"""
    custom60: list[str]
    """Custom field 60"""
    custom61: list[str]
    """Custom field 61"""
    custom62: list[str]
    """Custom field 62"""
    custom63: list[str]
    """Custom field 63"""
    custom64: list[str]
    """Custom field 64"""
    custom65: list[str]
    """Custom field 65"""
    custom66: list[str]
    """Custom field 66"""
    custom67: list[str]
    """Custom field 67"""
    custom68: list[str]
    """Custom field 68"""
    custom69: list[str]
    """Custom field 69"""
    custom7: list[str]
    """Custom field 7"""
    custom70: list[str]
    """Custom field 70"""
    custom71: list[str]
    """Custom field 71"""
    custom72: list[str]
    """Custom field 72"""
    custom73: list[str]
    """Custom field 73"""
    custom74: list[str]
    """Custom field 74"""
    custom75: list[str]
    """Custom field 75"""
    custom76: list[str]
    """Custom field 76"""
    custom77: list[str]
    """Custom field 77"""
    custom78: list[str]
    """Custom field 78"""
    custom79: list[str]
    """Custom field 79"""
    custom8: list[str]
    """Custom field 8"""
    custom80: list[str]
    """Custom field 80"""
    custom81: list[str]
    """Custom field 81"""
    custom82: list[str]
    """Custom field 82"""
    custom83: list[str]
    """Custom field 83"""
    custom84: list[str]
    """Custom field 84"""
    custom85: list[str]
    """Custom field 85"""
    custom86: list[str]
    """Custom field 86"""
    custom87: list[str]
    """Custom field 87"""
    custom88: list[str]
    """Custom field 88"""
    custom89: list[str]
    """Custom field 89"""
    custom9: list[str]
    """Custom field 9"""
    custom90: list[str]
    """Custom field 90"""
    custom91: list[str]
    """Custom field 91"""
    custom92: list[str]
    """Custom field 92"""
    custom93: list[str]
    """Custom field 93"""
    custom94: list[str]
    """Custom field 94"""
    custom95: list[str]
    """Custom field 95"""
    custom96: list[str]
    """Custom field 96"""
    custom97: list[str]
    """Custom field 97"""
    custom98: list[str]
    """Custom field 98"""
    custom99: list[str]
    """Custom field 99"""
    date_of_birth: list[str]
    """Date of birth"""
    default_plugin_mapping: list[list[Any]]
    """Default plugin mapping"""
    degree: list[str]
    """Degree"""
    email_addresses: list[list[Any]]
    """Email addresses"""
    email_contacts: list[list[Any]]
    """Email contacts"""
    email_opted_out: list[bool]
    """Email opted out"""
    emails: list[list[Any]]
    """Emails"""
    emails_opt_status: list[str]
    """Emails opt status"""
    emails_opted_at: list[str]
    """Emails opted at"""
    engaged_at: list[str]
    """Engaged at"""
    engaged_score: list[float]
    """Engaged score"""
    event_name: list[str]
    """Event name"""
    external_id: list[str]
    """External id"""
    external_owner: list[str]
    """External owner"""
    external_source: list[str]
    """External source"""
    facebook_url: list[str]
    """Facebook url"""
    favorites: list[list[Any]]
    """Favorites"""
    first_name: list[str]
    """First name"""
    gender: list[str]
    """Gender"""
    github_url: list[str]
    """Github url"""
    github_username: list[str]
    """Github username"""
    google_plus_url: list[str]
    """Google plus url"""
    graduation_date: list[str]
    """Graduation date"""
    home_phones: list[list[Any]]
    """Home phones"""
    id: list[int]
    """Unique prospect identifier"""
    job_start_date: list[str]
    """Job start date"""
    last_name: list[str]
    """Last name"""
    linked_in_connections: list[int]
    """Linked in connections"""
    linked_in_id: list[str]
    """Linked in id"""
    linked_in_slug: list[str]
    """Linked in slug"""
    linked_in_url: list[str]
    """Linked in url"""
    mailings: list[list[Any]]
    """Mailings"""
    middle_name: list[str]
    """Middle name"""
    mobile_phones: list[list[Any]]
    """Mobile phones"""
    name: list[str]
    """Name"""
    nickname: list[str]
    """Nickname"""
    occupation: list[str]
    """Occupation"""
    open_count: list[int]
    """Open count"""
    opportunities: list[list[Any]]
    """Opportunities"""
    opportunity_prospect_roles: list[list[Any]]
    """Opportunity prospect roles"""
    opted_out: list[bool]
    """Opted out"""
    opted_out_at: list[str]
    """Opted out at"""
    other_phones: list[list[Any]]
    """Other phones"""
    owner: list[list[Any]]
    """Owner"""
    persona: list[list[Any]]
    """Persona"""
    persona_name: list[str]
    """Persona name"""
    personal_note1: list[str]
    """Personal note1"""
    personal_note2: list[str]
    """Personal note2"""
    phone_numbers: list[list[Any]]
    """Phone numbers"""
    preferred_contact: list[str]
    """Preferred contact"""
    quora_url: list[str]
    """Quora url"""
    region: list[str]
    """Region"""
    reply_count: list[int]
    """Reply count"""
    school: list[str]
    """School"""
    score: list[float]
    """Score"""
    sequence_states: list[list[Any]]
    """Sequence states"""
    sharing_team_id: list[str]
    """Sharing team id"""
    sms_opt_status: list[str]
    """Sms opt status"""
    sms_opted_at: list[str]
    """Sms opted at"""
    sms_opted_out: list[bool]
    """Sms opted out"""
    source: list[str]
    """Source"""
    specialties: list[str]
    """Specialties"""
    stack_overflow_id: list[str]
    """Stack overflow id"""
    stack_overflow_url: list[str]
    """Stack overflow url"""
    stage: list[list[Any]]
    """Stage"""
    stage_name: list[str]
    """Stage name"""
    tags: list[list[Any]]
    """Tags"""
    tasks: list[list[Any]]
    """Tasks"""
    time_zone: list[str]
    """Time zone"""
    time_zone_iana: list[str]
    """Time zone iana"""
    time_zone_inferred: list[str]
    """Time zone inferred"""
    title: list[str]
    """Title"""
    touched_at: list[str]
    """Touched at"""
    trashed_at: list[str]
    """Trashed at"""
    trashed_by_account: list[list[Any]]
    """Trashed by account"""
    twitter_url: list[str]
    """Twitter url"""
    twitter_username: list[str]
    """Twitter username"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""
    updater_id: list[int]
    """Updater id"""
    updater_type: list[str]
    """Updater type"""
    voip_phones: list[list[Any]]
    """Voip phones"""
    website_url1: list[str]
    """Website url1"""
    website_url2: list[str]
    """Website url2"""
    website_url3: list[str]
    """Website url3"""
    work_phones: list[list[Any]]
    """Work phones"""


class ProspectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account: Any
    """Account"""
    account_name: Any
    """Account name"""
    active_sequence_states: Any
    """Active sequence states"""
    added_at: Any
    """Added at"""
    address_city: Any
    """Address city"""
    address_country: Any
    """Address country"""
    address_state: Any
    """Address state"""
    address_street: Any
    """Address street"""
    address_street2: Any
    """Address street2"""
    address_zip: Any
    """Address zip"""
    angel_list_url: Any
    """Angel list url"""
    assigned_teams: Any
    """Assigned teams"""
    assigned_users: Any
    """Assigned users"""
    available_at: Any
    """Available at"""
    batches: Any
    """Batches"""
    call_opted_out: Any
    """Call opted out"""
    calls: Any
    """Calls"""
    calls_opt_status: Any
    """Calls opt status"""
    calls_opted_at: Any
    """Calls opted at"""
    campaign_name: Any
    """Campaign name"""
    click_count: Any
    """Click count"""
    company: Any
    """Company"""
    company_followers: Any
    """Company followers"""
    company_founded_at: Any
    """Company founded at"""
    company_industry: Any
    """Company industry"""
    company_linked_in: Any
    """Company linked in"""
    company_linked_in_employees: Any
    """Company linked in employees"""
    company_locality: Any
    """Company locality"""
    company_natural: Any
    """Company natural"""
    company_size: Any
    """Company size"""
    company_start_date: Any
    """Company start date"""
    company_type: Any
    """Company type"""
    contact_histogram: Any
    """Contact histogram"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    custom1: Any
    """Custom field 1"""
    custom10: Any
    """Custom field 10"""
    custom100: Any
    """Custom field 100"""
    custom101: Any
    """Custom field 101"""
    custom102: Any
    """Custom field 102"""
    custom103: Any
    """Custom field 103"""
    custom104: Any
    """Custom field 104"""
    custom105: Any
    """Custom field 105"""
    custom106: Any
    """Custom field 106"""
    custom107: Any
    """Custom field 107"""
    custom108: Any
    """Custom field 108"""
    custom109: Any
    """Custom field 109"""
    custom11: Any
    """Custom field 11"""
    custom110: Any
    """Custom field 110"""
    custom111: Any
    """Custom field 111"""
    custom112: Any
    """Custom field 112"""
    custom113: Any
    """Custom field 113"""
    custom114: Any
    """Custom field 114"""
    custom115: Any
    """Custom field 115"""
    custom116: Any
    """Custom field 116"""
    custom117: Any
    """Custom field 117"""
    custom118: Any
    """Custom field 118"""
    custom119: Any
    """Custom field 119"""
    custom12: Any
    """Custom field 12"""
    custom120: Any
    """Custom field 120"""
    custom121: Any
    """Custom field 121"""
    custom122: Any
    """Custom field 122"""
    custom123: Any
    """Custom field 123"""
    custom124: Any
    """Custom field 124"""
    custom125: Any
    """Custom field 125"""
    custom126: Any
    """Custom field 126"""
    custom127: Any
    """Custom field 127"""
    custom128: Any
    """Custom field 128"""
    custom129: Any
    """Custom field 129"""
    custom13: Any
    """Custom field 13"""
    custom130: Any
    """Custom field 130"""
    custom131: Any
    """Custom field 131"""
    custom132: Any
    """Custom field 132"""
    custom133: Any
    """Custom field 133"""
    custom134: Any
    """Custom field 134"""
    custom135: Any
    """Custom field 135"""
    custom136: Any
    """Custom field 136"""
    custom137: Any
    """Custom field 137"""
    custom138: Any
    """Custom field 138"""
    custom139: Any
    """Custom field 139"""
    custom14: Any
    """Custom field 14"""
    custom140: Any
    """Custom field 140"""
    custom141: Any
    """Custom field 141"""
    custom142: Any
    """Custom field 142"""
    custom143: Any
    """Custom field 143"""
    custom144: Any
    """Custom field 144"""
    custom145: Any
    """Custom field 145"""
    custom146: Any
    """Custom field 146"""
    custom147: Any
    """Custom field 147"""
    custom148: Any
    """Custom field 148"""
    custom149: Any
    """Custom field 149"""
    custom15: Any
    """Custom field 15"""
    custom150: Any
    """Custom field 150"""
    custom16: Any
    """Custom field 16"""
    custom17: Any
    """Custom field 17"""
    custom18: Any
    """Custom field 18"""
    custom19: Any
    """Custom field 19"""
    custom2: Any
    """Custom field 2"""
    custom20: Any
    """Custom field 20"""
    custom21: Any
    """Custom field 21"""
    custom22: Any
    """Custom field 22"""
    custom23: Any
    """Custom field 23"""
    custom24: Any
    """Custom field 24"""
    custom25: Any
    """Custom field 25"""
    custom26: Any
    """Custom field 26"""
    custom27: Any
    """Custom field 27"""
    custom28: Any
    """Custom field 28"""
    custom29: Any
    """Custom field 29"""
    custom3: Any
    """Custom field 3"""
    custom30: Any
    """Custom field 30"""
    custom31: Any
    """Custom field 31"""
    custom32: Any
    """Custom field 32"""
    custom33: Any
    """Custom field 33"""
    custom34: Any
    """Custom field 34"""
    custom35: Any
    """Custom field 35"""
    custom36: Any
    """Custom field 36"""
    custom37: Any
    """Custom field 37"""
    custom38: Any
    """Custom field 38"""
    custom39: Any
    """Custom field 39"""
    custom4: Any
    """Custom field 4"""
    custom40: Any
    """Custom field 40"""
    custom41: Any
    """Custom field 41"""
    custom42: Any
    """Custom field 42"""
    custom43: Any
    """Custom field 43"""
    custom44: Any
    """Custom field 44"""
    custom45: Any
    """Custom field 45"""
    custom46: Any
    """Custom field 46"""
    custom47: Any
    """Custom field 47"""
    custom48: Any
    """Custom field 48"""
    custom49: Any
    """Custom field 49"""
    custom5: Any
    """Custom field 5"""
    custom50: Any
    """Custom field 50"""
    custom51: Any
    """Custom field 51"""
    custom52: Any
    """Custom field 52"""
    custom53: Any
    """Custom field 53"""
    custom54: Any
    """Custom field 54"""
    custom55: Any
    """Custom field 55"""
    custom56: Any
    """Custom field 56"""
    custom57: Any
    """Custom field 57"""
    custom58: Any
    """Custom field 58"""
    custom59: Any
    """Custom field 59"""
    custom6: Any
    """Custom field 6"""
    custom60: Any
    """Custom field 60"""
    custom61: Any
    """Custom field 61"""
    custom62: Any
    """Custom field 62"""
    custom63: Any
    """Custom field 63"""
    custom64: Any
    """Custom field 64"""
    custom65: Any
    """Custom field 65"""
    custom66: Any
    """Custom field 66"""
    custom67: Any
    """Custom field 67"""
    custom68: Any
    """Custom field 68"""
    custom69: Any
    """Custom field 69"""
    custom7: Any
    """Custom field 7"""
    custom70: Any
    """Custom field 70"""
    custom71: Any
    """Custom field 71"""
    custom72: Any
    """Custom field 72"""
    custom73: Any
    """Custom field 73"""
    custom74: Any
    """Custom field 74"""
    custom75: Any
    """Custom field 75"""
    custom76: Any
    """Custom field 76"""
    custom77: Any
    """Custom field 77"""
    custom78: Any
    """Custom field 78"""
    custom79: Any
    """Custom field 79"""
    custom8: Any
    """Custom field 8"""
    custom80: Any
    """Custom field 80"""
    custom81: Any
    """Custom field 81"""
    custom82: Any
    """Custom field 82"""
    custom83: Any
    """Custom field 83"""
    custom84: Any
    """Custom field 84"""
    custom85: Any
    """Custom field 85"""
    custom86: Any
    """Custom field 86"""
    custom87: Any
    """Custom field 87"""
    custom88: Any
    """Custom field 88"""
    custom89: Any
    """Custom field 89"""
    custom9: Any
    """Custom field 9"""
    custom90: Any
    """Custom field 90"""
    custom91: Any
    """Custom field 91"""
    custom92: Any
    """Custom field 92"""
    custom93: Any
    """Custom field 93"""
    custom94: Any
    """Custom field 94"""
    custom95: Any
    """Custom field 95"""
    custom96: Any
    """Custom field 96"""
    custom97: Any
    """Custom field 97"""
    custom98: Any
    """Custom field 98"""
    custom99: Any
    """Custom field 99"""
    date_of_birth: Any
    """Date of birth"""
    default_plugin_mapping: Any
    """Default plugin mapping"""
    degree: Any
    """Degree"""
    email_addresses: Any
    """Email addresses"""
    email_contacts: Any
    """Email contacts"""
    email_opted_out: Any
    """Email opted out"""
    emails: Any
    """Emails"""
    emails_opt_status: Any
    """Emails opt status"""
    emails_opted_at: Any
    """Emails opted at"""
    engaged_at: Any
    """Engaged at"""
    engaged_score: Any
    """Engaged score"""
    event_name: Any
    """Event name"""
    external_id: Any
    """External id"""
    external_owner: Any
    """External owner"""
    external_source: Any
    """External source"""
    facebook_url: Any
    """Facebook url"""
    favorites: Any
    """Favorites"""
    first_name: Any
    """First name"""
    gender: Any
    """Gender"""
    github_url: Any
    """Github url"""
    github_username: Any
    """Github username"""
    google_plus_url: Any
    """Google plus url"""
    graduation_date: Any
    """Graduation date"""
    home_phones: Any
    """Home phones"""
    id: Any
    """Unique prospect identifier"""
    job_start_date: Any
    """Job start date"""
    last_name: Any
    """Last name"""
    linked_in_connections: Any
    """Linked in connections"""
    linked_in_id: Any
    """Linked in id"""
    linked_in_slug: Any
    """Linked in slug"""
    linked_in_url: Any
    """Linked in url"""
    mailings: Any
    """Mailings"""
    middle_name: Any
    """Middle name"""
    mobile_phones: Any
    """Mobile phones"""
    name: Any
    """Name"""
    nickname: Any
    """Nickname"""
    occupation: Any
    """Occupation"""
    open_count: Any
    """Open count"""
    opportunities: Any
    """Opportunities"""
    opportunity_prospect_roles: Any
    """Opportunity prospect roles"""
    opted_out: Any
    """Opted out"""
    opted_out_at: Any
    """Opted out at"""
    other_phones: Any
    """Other phones"""
    owner: Any
    """Owner"""
    persona: Any
    """Persona"""
    persona_name: Any
    """Persona name"""
    personal_note1: Any
    """Personal note1"""
    personal_note2: Any
    """Personal note2"""
    phone_numbers: Any
    """Phone numbers"""
    preferred_contact: Any
    """Preferred contact"""
    quora_url: Any
    """Quora url"""
    region: Any
    """Region"""
    reply_count: Any
    """Reply count"""
    school: Any
    """School"""
    score: Any
    """Score"""
    sequence_states: Any
    """Sequence states"""
    sharing_team_id: Any
    """Sharing team id"""
    sms_opt_status: Any
    """Sms opt status"""
    sms_opted_at: Any
    """Sms opted at"""
    sms_opted_out: Any
    """Sms opted out"""
    source: Any
    """Source"""
    specialties: Any
    """Specialties"""
    stack_overflow_id: Any
    """Stack overflow id"""
    stack_overflow_url: Any
    """Stack overflow url"""
    stage: Any
    """Stage"""
    stage_name: Any
    """Stage name"""
    tags: Any
    """Tags"""
    tasks: Any
    """Tasks"""
    time_zone: Any
    """Time zone"""
    time_zone_iana: Any
    """Time zone iana"""
    time_zone_inferred: Any
    """Time zone inferred"""
    title: Any
    """Title"""
    touched_at: Any
    """Touched at"""
    trashed_at: Any
    """Trashed at"""
    trashed_by_account: Any
    """Trashed by account"""
    twitter_url: Any
    """Twitter url"""
    twitter_username: Any
    """Twitter username"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""
    updater_id: Any
    """Updater id"""
    updater_type: Any
    """Updater type"""
    voip_phones: Any
    """Voip phones"""
    website_url1: Any
    """Website url1"""
    website_url2: Any
    """Website url2"""
    website_url3: Any
    """Website url3"""
    work_phones: Any
    """Work phones"""


class ProspectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    account: str
    """Account"""
    account_name: str
    """Account name"""
    active_sequence_states: str
    """Active sequence states"""
    added_at: str
    """Added at"""
    address_city: str
    """Address city"""
    address_country: str
    """Address country"""
    address_state: str
    """Address state"""
    address_street: str
    """Address street"""
    address_street2: str
    """Address street2"""
    address_zip: str
    """Address zip"""
    angel_list_url: str
    """Angel list url"""
    assigned_teams: str
    """Assigned teams"""
    assigned_users: str
    """Assigned users"""
    available_at: str
    """Available at"""
    batches: str
    """Batches"""
    call_opted_out: str
    """Call opted out"""
    calls: str
    """Calls"""
    calls_opt_status: str
    """Calls opt status"""
    calls_opted_at: str
    """Calls opted at"""
    campaign_name: str
    """Campaign name"""
    click_count: str
    """Click count"""
    company: str
    """Company"""
    company_followers: str
    """Company followers"""
    company_founded_at: str
    """Company founded at"""
    company_industry: str
    """Company industry"""
    company_linked_in: str
    """Company linked in"""
    company_linked_in_employees: str
    """Company linked in employees"""
    company_locality: str
    """Company locality"""
    company_natural: str
    """Company natural"""
    company_size: str
    """Company size"""
    company_start_date: str
    """Company start date"""
    company_type: str
    """Company type"""
    contact_histogram: str
    """Contact histogram"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    custom1: str
    """Custom field 1"""
    custom10: str
    """Custom field 10"""
    custom100: str
    """Custom field 100"""
    custom101: str
    """Custom field 101"""
    custom102: str
    """Custom field 102"""
    custom103: str
    """Custom field 103"""
    custom104: str
    """Custom field 104"""
    custom105: str
    """Custom field 105"""
    custom106: str
    """Custom field 106"""
    custom107: str
    """Custom field 107"""
    custom108: str
    """Custom field 108"""
    custom109: str
    """Custom field 109"""
    custom11: str
    """Custom field 11"""
    custom110: str
    """Custom field 110"""
    custom111: str
    """Custom field 111"""
    custom112: str
    """Custom field 112"""
    custom113: str
    """Custom field 113"""
    custom114: str
    """Custom field 114"""
    custom115: str
    """Custom field 115"""
    custom116: str
    """Custom field 116"""
    custom117: str
    """Custom field 117"""
    custom118: str
    """Custom field 118"""
    custom119: str
    """Custom field 119"""
    custom12: str
    """Custom field 12"""
    custom120: str
    """Custom field 120"""
    custom121: str
    """Custom field 121"""
    custom122: str
    """Custom field 122"""
    custom123: str
    """Custom field 123"""
    custom124: str
    """Custom field 124"""
    custom125: str
    """Custom field 125"""
    custom126: str
    """Custom field 126"""
    custom127: str
    """Custom field 127"""
    custom128: str
    """Custom field 128"""
    custom129: str
    """Custom field 129"""
    custom13: str
    """Custom field 13"""
    custom130: str
    """Custom field 130"""
    custom131: str
    """Custom field 131"""
    custom132: str
    """Custom field 132"""
    custom133: str
    """Custom field 133"""
    custom134: str
    """Custom field 134"""
    custom135: str
    """Custom field 135"""
    custom136: str
    """Custom field 136"""
    custom137: str
    """Custom field 137"""
    custom138: str
    """Custom field 138"""
    custom139: str
    """Custom field 139"""
    custom14: str
    """Custom field 14"""
    custom140: str
    """Custom field 140"""
    custom141: str
    """Custom field 141"""
    custom142: str
    """Custom field 142"""
    custom143: str
    """Custom field 143"""
    custom144: str
    """Custom field 144"""
    custom145: str
    """Custom field 145"""
    custom146: str
    """Custom field 146"""
    custom147: str
    """Custom field 147"""
    custom148: str
    """Custom field 148"""
    custom149: str
    """Custom field 149"""
    custom15: str
    """Custom field 15"""
    custom150: str
    """Custom field 150"""
    custom16: str
    """Custom field 16"""
    custom17: str
    """Custom field 17"""
    custom18: str
    """Custom field 18"""
    custom19: str
    """Custom field 19"""
    custom2: str
    """Custom field 2"""
    custom20: str
    """Custom field 20"""
    custom21: str
    """Custom field 21"""
    custom22: str
    """Custom field 22"""
    custom23: str
    """Custom field 23"""
    custom24: str
    """Custom field 24"""
    custom25: str
    """Custom field 25"""
    custom26: str
    """Custom field 26"""
    custom27: str
    """Custom field 27"""
    custom28: str
    """Custom field 28"""
    custom29: str
    """Custom field 29"""
    custom3: str
    """Custom field 3"""
    custom30: str
    """Custom field 30"""
    custom31: str
    """Custom field 31"""
    custom32: str
    """Custom field 32"""
    custom33: str
    """Custom field 33"""
    custom34: str
    """Custom field 34"""
    custom35: str
    """Custom field 35"""
    custom36: str
    """Custom field 36"""
    custom37: str
    """Custom field 37"""
    custom38: str
    """Custom field 38"""
    custom39: str
    """Custom field 39"""
    custom4: str
    """Custom field 4"""
    custom40: str
    """Custom field 40"""
    custom41: str
    """Custom field 41"""
    custom42: str
    """Custom field 42"""
    custom43: str
    """Custom field 43"""
    custom44: str
    """Custom field 44"""
    custom45: str
    """Custom field 45"""
    custom46: str
    """Custom field 46"""
    custom47: str
    """Custom field 47"""
    custom48: str
    """Custom field 48"""
    custom49: str
    """Custom field 49"""
    custom5: str
    """Custom field 5"""
    custom50: str
    """Custom field 50"""
    custom51: str
    """Custom field 51"""
    custom52: str
    """Custom field 52"""
    custom53: str
    """Custom field 53"""
    custom54: str
    """Custom field 54"""
    custom55: str
    """Custom field 55"""
    custom56: str
    """Custom field 56"""
    custom57: str
    """Custom field 57"""
    custom58: str
    """Custom field 58"""
    custom59: str
    """Custom field 59"""
    custom6: str
    """Custom field 6"""
    custom60: str
    """Custom field 60"""
    custom61: str
    """Custom field 61"""
    custom62: str
    """Custom field 62"""
    custom63: str
    """Custom field 63"""
    custom64: str
    """Custom field 64"""
    custom65: str
    """Custom field 65"""
    custom66: str
    """Custom field 66"""
    custom67: str
    """Custom field 67"""
    custom68: str
    """Custom field 68"""
    custom69: str
    """Custom field 69"""
    custom7: str
    """Custom field 7"""
    custom70: str
    """Custom field 70"""
    custom71: str
    """Custom field 71"""
    custom72: str
    """Custom field 72"""
    custom73: str
    """Custom field 73"""
    custom74: str
    """Custom field 74"""
    custom75: str
    """Custom field 75"""
    custom76: str
    """Custom field 76"""
    custom77: str
    """Custom field 77"""
    custom78: str
    """Custom field 78"""
    custom79: str
    """Custom field 79"""
    custom8: str
    """Custom field 8"""
    custom80: str
    """Custom field 80"""
    custom81: str
    """Custom field 81"""
    custom82: str
    """Custom field 82"""
    custom83: str
    """Custom field 83"""
    custom84: str
    """Custom field 84"""
    custom85: str
    """Custom field 85"""
    custom86: str
    """Custom field 86"""
    custom87: str
    """Custom field 87"""
    custom88: str
    """Custom field 88"""
    custom89: str
    """Custom field 89"""
    custom9: str
    """Custom field 9"""
    custom90: str
    """Custom field 90"""
    custom91: str
    """Custom field 91"""
    custom92: str
    """Custom field 92"""
    custom93: str
    """Custom field 93"""
    custom94: str
    """Custom field 94"""
    custom95: str
    """Custom field 95"""
    custom96: str
    """Custom field 96"""
    custom97: str
    """Custom field 97"""
    custom98: str
    """Custom field 98"""
    custom99: str
    """Custom field 99"""
    date_of_birth: str
    """Date of birth"""
    default_plugin_mapping: str
    """Default plugin mapping"""
    degree: str
    """Degree"""
    email_addresses: str
    """Email addresses"""
    email_contacts: str
    """Email contacts"""
    email_opted_out: str
    """Email opted out"""
    emails: str
    """Emails"""
    emails_opt_status: str
    """Emails opt status"""
    emails_opted_at: str
    """Emails opted at"""
    engaged_at: str
    """Engaged at"""
    engaged_score: str
    """Engaged score"""
    event_name: str
    """Event name"""
    external_id: str
    """External id"""
    external_owner: str
    """External owner"""
    external_source: str
    """External source"""
    facebook_url: str
    """Facebook url"""
    favorites: str
    """Favorites"""
    first_name: str
    """First name"""
    gender: str
    """Gender"""
    github_url: str
    """Github url"""
    github_username: str
    """Github username"""
    google_plus_url: str
    """Google plus url"""
    graduation_date: str
    """Graduation date"""
    home_phones: str
    """Home phones"""
    id: str
    """Unique prospect identifier"""
    job_start_date: str
    """Job start date"""
    last_name: str
    """Last name"""
    linked_in_connections: str
    """Linked in connections"""
    linked_in_id: str
    """Linked in id"""
    linked_in_slug: str
    """Linked in slug"""
    linked_in_url: str
    """Linked in url"""
    mailings: str
    """Mailings"""
    middle_name: str
    """Middle name"""
    mobile_phones: str
    """Mobile phones"""
    name: str
    """Name"""
    nickname: str
    """Nickname"""
    occupation: str
    """Occupation"""
    open_count: str
    """Open count"""
    opportunities: str
    """Opportunities"""
    opportunity_prospect_roles: str
    """Opportunity prospect roles"""
    opted_out: str
    """Opted out"""
    opted_out_at: str
    """Opted out at"""
    other_phones: str
    """Other phones"""
    owner: str
    """Owner"""
    persona: str
    """Persona"""
    persona_name: str
    """Persona name"""
    personal_note1: str
    """Personal note1"""
    personal_note2: str
    """Personal note2"""
    phone_numbers: str
    """Phone numbers"""
    preferred_contact: str
    """Preferred contact"""
    quora_url: str
    """Quora url"""
    region: str
    """Region"""
    reply_count: str
    """Reply count"""
    school: str
    """School"""
    score: str
    """Score"""
    sequence_states: str
    """Sequence states"""
    sharing_team_id: str
    """Sharing team id"""
    sms_opt_status: str
    """Sms opt status"""
    sms_opted_at: str
    """Sms opted at"""
    sms_opted_out: str
    """Sms opted out"""
    source: str
    """Source"""
    specialties: str
    """Specialties"""
    stack_overflow_id: str
    """Stack overflow id"""
    stack_overflow_url: str
    """Stack overflow url"""
    stage: str
    """Stage"""
    stage_name: str
    """Stage name"""
    tags: str
    """Tags"""
    tasks: str
    """Tasks"""
    time_zone: str
    """Time zone"""
    time_zone_iana: str
    """Time zone iana"""
    time_zone_inferred: str
    """Time zone inferred"""
    title: str
    """Title"""
    touched_at: str
    """Touched at"""
    trashed_at: str
    """Trashed at"""
    trashed_by_account: str
    """Trashed by account"""
    twitter_url: str
    """Twitter url"""
    twitter_username: str
    """Twitter username"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""
    updater_id: str
    """Updater id"""
    updater_type: str
    """Updater type"""
    voip_phones: str
    """Voip phones"""
    website_url1: str
    """Website url1"""
    website_url2: str
    """Website url2"""
    website_url3: str
    """Website url3"""
    work_phones: str
    """Work phones"""


class ProspectsSortFilter(TypedDict, total=False):
    """Available fields for sorting prospects search results."""
    account: AirbyteSortOrder
    """Account"""
    account_name: AirbyteSortOrder
    """Account name"""
    active_sequence_states: AirbyteSortOrder
    """Active sequence states"""
    added_at: AirbyteSortOrder
    """Added at"""
    address_city: AirbyteSortOrder
    """Address city"""
    address_country: AirbyteSortOrder
    """Address country"""
    address_state: AirbyteSortOrder
    """Address state"""
    address_street: AirbyteSortOrder
    """Address street"""
    address_street2: AirbyteSortOrder
    """Address street2"""
    address_zip: AirbyteSortOrder
    """Address zip"""
    angel_list_url: AirbyteSortOrder
    """Angel list url"""
    assigned_teams: AirbyteSortOrder
    """Assigned teams"""
    assigned_users: AirbyteSortOrder
    """Assigned users"""
    available_at: AirbyteSortOrder
    """Available at"""
    batches: AirbyteSortOrder
    """Batches"""
    call_opted_out: AirbyteSortOrder
    """Call opted out"""
    calls: AirbyteSortOrder
    """Calls"""
    calls_opt_status: AirbyteSortOrder
    """Calls opt status"""
    calls_opted_at: AirbyteSortOrder
    """Calls opted at"""
    campaign_name: AirbyteSortOrder
    """Campaign name"""
    click_count: AirbyteSortOrder
    """Click count"""
    company: AirbyteSortOrder
    """Company"""
    company_followers: AirbyteSortOrder
    """Company followers"""
    company_founded_at: AirbyteSortOrder
    """Company founded at"""
    company_industry: AirbyteSortOrder
    """Company industry"""
    company_linked_in: AirbyteSortOrder
    """Company linked in"""
    company_linked_in_employees: AirbyteSortOrder
    """Company linked in employees"""
    company_locality: AirbyteSortOrder
    """Company locality"""
    company_natural: AirbyteSortOrder
    """Company natural"""
    company_size: AirbyteSortOrder
    """Company size"""
    company_start_date: AirbyteSortOrder
    """Company start date"""
    company_type: AirbyteSortOrder
    """Company type"""
    contact_histogram: AirbyteSortOrder
    """Contact histogram"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    custom1: AirbyteSortOrder
    """Custom field 1"""
    custom10: AirbyteSortOrder
    """Custom field 10"""
    custom100: AirbyteSortOrder
    """Custom field 100"""
    custom101: AirbyteSortOrder
    """Custom field 101"""
    custom102: AirbyteSortOrder
    """Custom field 102"""
    custom103: AirbyteSortOrder
    """Custom field 103"""
    custom104: AirbyteSortOrder
    """Custom field 104"""
    custom105: AirbyteSortOrder
    """Custom field 105"""
    custom106: AirbyteSortOrder
    """Custom field 106"""
    custom107: AirbyteSortOrder
    """Custom field 107"""
    custom108: AirbyteSortOrder
    """Custom field 108"""
    custom109: AirbyteSortOrder
    """Custom field 109"""
    custom11: AirbyteSortOrder
    """Custom field 11"""
    custom110: AirbyteSortOrder
    """Custom field 110"""
    custom111: AirbyteSortOrder
    """Custom field 111"""
    custom112: AirbyteSortOrder
    """Custom field 112"""
    custom113: AirbyteSortOrder
    """Custom field 113"""
    custom114: AirbyteSortOrder
    """Custom field 114"""
    custom115: AirbyteSortOrder
    """Custom field 115"""
    custom116: AirbyteSortOrder
    """Custom field 116"""
    custom117: AirbyteSortOrder
    """Custom field 117"""
    custom118: AirbyteSortOrder
    """Custom field 118"""
    custom119: AirbyteSortOrder
    """Custom field 119"""
    custom12: AirbyteSortOrder
    """Custom field 12"""
    custom120: AirbyteSortOrder
    """Custom field 120"""
    custom121: AirbyteSortOrder
    """Custom field 121"""
    custom122: AirbyteSortOrder
    """Custom field 122"""
    custom123: AirbyteSortOrder
    """Custom field 123"""
    custom124: AirbyteSortOrder
    """Custom field 124"""
    custom125: AirbyteSortOrder
    """Custom field 125"""
    custom126: AirbyteSortOrder
    """Custom field 126"""
    custom127: AirbyteSortOrder
    """Custom field 127"""
    custom128: AirbyteSortOrder
    """Custom field 128"""
    custom129: AirbyteSortOrder
    """Custom field 129"""
    custom13: AirbyteSortOrder
    """Custom field 13"""
    custom130: AirbyteSortOrder
    """Custom field 130"""
    custom131: AirbyteSortOrder
    """Custom field 131"""
    custom132: AirbyteSortOrder
    """Custom field 132"""
    custom133: AirbyteSortOrder
    """Custom field 133"""
    custom134: AirbyteSortOrder
    """Custom field 134"""
    custom135: AirbyteSortOrder
    """Custom field 135"""
    custom136: AirbyteSortOrder
    """Custom field 136"""
    custom137: AirbyteSortOrder
    """Custom field 137"""
    custom138: AirbyteSortOrder
    """Custom field 138"""
    custom139: AirbyteSortOrder
    """Custom field 139"""
    custom14: AirbyteSortOrder
    """Custom field 14"""
    custom140: AirbyteSortOrder
    """Custom field 140"""
    custom141: AirbyteSortOrder
    """Custom field 141"""
    custom142: AirbyteSortOrder
    """Custom field 142"""
    custom143: AirbyteSortOrder
    """Custom field 143"""
    custom144: AirbyteSortOrder
    """Custom field 144"""
    custom145: AirbyteSortOrder
    """Custom field 145"""
    custom146: AirbyteSortOrder
    """Custom field 146"""
    custom147: AirbyteSortOrder
    """Custom field 147"""
    custom148: AirbyteSortOrder
    """Custom field 148"""
    custom149: AirbyteSortOrder
    """Custom field 149"""
    custom15: AirbyteSortOrder
    """Custom field 15"""
    custom150: AirbyteSortOrder
    """Custom field 150"""
    custom16: AirbyteSortOrder
    """Custom field 16"""
    custom17: AirbyteSortOrder
    """Custom field 17"""
    custom18: AirbyteSortOrder
    """Custom field 18"""
    custom19: AirbyteSortOrder
    """Custom field 19"""
    custom2: AirbyteSortOrder
    """Custom field 2"""
    custom20: AirbyteSortOrder
    """Custom field 20"""
    custom21: AirbyteSortOrder
    """Custom field 21"""
    custom22: AirbyteSortOrder
    """Custom field 22"""
    custom23: AirbyteSortOrder
    """Custom field 23"""
    custom24: AirbyteSortOrder
    """Custom field 24"""
    custom25: AirbyteSortOrder
    """Custom field 25"""
    custom26: AirbyteSortOrder
    """Custom field 26"""
    custom27: AirbyteSortOrder
    """Custom field 27"""
    custom28: AirbyteSortOrder
    """Custom field 28"""
    custom29: AirbyteSortOrder
    """Custom field 29"""
    custom3: AirbyteSortOrder
    """Custom field 3"""
    custom30: AirbyteSortOrder
    """Custom field 30"""
    custom31: AirbyteSortOrder
    """Custom field 31"""
    custom32: AirbyteSortOrder
    """Custom field 32"""
    custom33: AirbyteSortOrder
    """Custom field 33"""
    custom34: AirbyteSortOrder
    """Custom field 34"""
    custom35: AirbyteSortOrder
    """Custom field 35"""
    custom36: AirbyteSortOrder
    """Custom field 36"""
    custom37: AirbyteSortOrder
    """Custom field 37"""
    custom38: AirbyteSortOrder
    """Custom field 38"""
    custom39: AirbyteSortOrder
    """Custom field 39"""
    custom4: AirbyteSortOrder
    """Custom field 4"""
    custom40: AirbyteSortOrder
    """Custom field 40"""
    custom41: AirbyteSortOrder
    """Custom field 41"""
    custom42: AirbyteSortOrder
    """Custom field 42"""
    custom43: AirbyteSortOrder
    """Custom field 43"""
    custom44: AirbyteSortOrder
    """Custom field 44"""
    custom45: AirbyteSortOrder
    """Custom field 45"""
    custom46: AirbyteSortOrder
    """Custom field 46"""
    custom47: AirbyteSortOrder
    """Custom field 47"""
    custom48: AirbyteSortOrder
    """Custom field 48"""
    custom49: AirbyteSortOrder
    """Custom field 49"""
    custom5: AirbyteSortOrder
    """Custom field 5"""
    custom50: AirbyteSortOrder
    """Custom field 50"""
    custom51: AirbyteSortOrder
    """Custom field 51"""
    custom52: AirbyteSortOrder
    """Custom field 52"""
    custom53: AirbyteSortOrder
    """Custom field 53"""
    custom54: AirbyteSortOrder
    """Custom field 54"""
    custom55: AirbyteSortOrder
    """Custom field 55"""
    custom56: AirbyteSortOrder
    """Custom field 56"""
    custom57: AirbyteSortOrder
    """Custom field 57"""
    custom58: AirbyteSortOrder
    """Custom field 58"""
    custom59: AirbyteSortOrder
    """Custom field 59"""
    custom6: AirbyteSortOrder
    """Custom field 6"""
    custom60: AirbyteSortOrder
    """Custom field 60"""
    custom61: AirbyteSortOrder
    """Custom field 61"""
    custom62: AirbyteSortOrder
    """Custom field 62"""
    custom63: AirbyteSortOrder
    """Custom field 63"""
    custom64: AirbyteSortOrder
    """Custom field 64"""
    custom65: AirbyteSortOrder
    """Custom field 65"""
    custom66: AirbyteSortOrder
    """Custom field 66"""
    custom67: AirbyteSortOrder
    """Custom field 67"""
    custom68: AirbyteSortOrder
    """Custom field 68"""
    custom69: AirbyteSortOrder
    """Custom field 69"""
    custom7: AirbyteSortOrder
    """Custom field 7"""
    custom70: AirbyteSortOrder
    """Custom field 70"""
    custom71: AirbyteSortOrder
    """Custom field 71"""
    custom72: AirbyteSortOrder
    """Custom field 72"""
    custom73: AirbyteSortOrder
    """Custom field 73"""
    custom74: AirbyteSortOrder
    """Custom field 74"""
    custom75: AirbyteSortOrder
    """Custom field 75"""
    custom76: AirbyteSortOrder
    """Custom field 76"""
    custom77: AirbyteSortOrder
    """Custom field 77"""
    custom78: AirbyteSortOrder
    """Custom field 78"""
    custom79: AirbyteSortOrder
    """Custom field 79"""
    custom8: AirbyteSortOrder
    """Custom field 8"""
    custom80: AirbyteSortOrder
    """Custom field 80"""
    custom81: AirbyteSortOrder
    """Custom field 81"""
    custom82: AirbyteSortOrder
    """Custom field 82"""
    custom83: AirbyteSortOrder
    """Custom field 83"""
    custom84: AirbyteSortOrder
    """Custom field 84"""
    custom85: AirbyteSortOrder
    """Custom field 85"""
    custom86: AirbyteSortOrder
    """Custom field 86"""
    custom87: AirbyteSortOrder
    """Custom field 87"""
    custom88: AirbyteSortOrder
    """Custom field 88"""
    custom89: AirbyteSortOrder
    """Custom field 89"""
    custom9: AirbyteSortOrder
    """Custom field 9"""
    custom90: AirbyteSortOrder
    """Custom field 90"""
    custom91: AirbyteSortOrder
    """Custom field 91"""
    custom92: AirbyteSortOrder
    """Custom field 92"""
    custom93: AirbyteSortOrder
    """Custom field 93"""
    custom94: AirbyteSortOrder
    """Custom field 94"""
    custom95: AirbyteSortOrder
    """Custom field 95"""
    custom96: AirbyteSortOrder
    """Custom field 96"""
    custom97: AirbyteSortOrder
    """Custom field 97"""
    custom98: AirbyteSortOrder
    """Custom field 98"""
    custom99: AirbyteSortOrder
    """Custom field 99"""
    date_of_birth: AirbyteSortOrder
    """Date of birth"""
    default_plugin_mapping: AirbyteSortOrder
    """Default plugin mapping"""
    degree: AirbyteSortOrder
    """Degree"""
    email_addresses: AirbyteSortOrder
    """Email addresses"""
    email_contacts: AirbyteSortOrder
    """Email contacts"""
    email_opted_out: AirbyteSortOrder
    """Email opted out"""
    emails: AirbyteSortOrder
    """Emails"""
    emails_opt_status: AirbyteSortOrder
    """Emails opt status"""
    emails_opted_at: AirbyteSortOrder
    """Emails opted at"""
    engaged_at: AirbyteSortOrder
    """Engaged at"""
    engaged_score: AirbyteSortOrder
    """Engaged score"""
    event_name: AirbyteSortOrder
    """Event name"""
    external_id: AirbyteSortOrder
    """External id"""
    external_owner: AirbyteSortOrder
    """External owner"""
    external_source: AirbyteSortOrder
    """External source"""
    facebook_url: AirbyteSortOrder
    """Facebook url"""
    favorites: AirbyteSortOrder
    """Favorites"""
    first_name: AirbyteSortOrder
    """First name"""
    gender: AirbyteSortOrder
    """Gender"""
    github_url: AirbyteSortOrder
    """Github url"""
    github_username: AirbyteSortOrder
    """Github username"""
    google_plus_url: AirbyteSortOrder
    """Google plus url"""
    graduation_date: AirbyteSortOrder
    """Graduation date"""
    home_phones: AirbyteSortOrder
    """Home phones"""
    id: AirbyteSortOrder
    """Unique prospect identifier"""
    job_start_date: AirbyteSortOrder
    """Job start date"""
    last_name: AirbyteSortOrder
    """Last name"""
    linked_in_connections: AirbyteSortOrder
    """Linked in connections"""
    linked_in_id: AirbyteSortOrder
    """Linked in id"""
    linked_in_slug: AirbyteSortOrder
    """Linked in slug"""
    linked_in_url: AirbyteSortOrder
    """Linked in url"""
    mailings: AirbyteSortOrder
    """Mailings"""
    middle_name: AirbyteSortOrder
    """Middle name"""
    mobile_phones: AirbyteSortOrder
    """Mobile phones"""
    name: AirbyteSortOrder
    """Name"""
    nickname: AirbyteSortOrder
    """Nickname"""
    occupation: AirbyteSortOrder
    """Occupation"""
    open_count: AirbyteSortOrder
    """Open count"""
    opportunities: AirbyteSortOrder
    """Opportunities"""
    opportunity_prospect_roles: AirbyteSortOrder
    """Opportunity prospect roles"""
    opted_out: AirbyteSortOrder
    """Opted out"""
    opted_out_at: AirbyteSortOrder
    """Opted out at"""
    other_phones: AirbyteSortOrder
    """Other phones"""
    owner: AirbyteSortOrder
    """Owner"""
    persona: AirbyteSortOrder
    """Persona"""
    persona_name: AirbyteSortOrder
    """Persona name"""
    personal_note1: AirbyteSortOrder
    """Personal note1"""
    personal_note2: AirbyteSortOrder
    """Personal note2"""
    phone_numbers: AirbyteSortOrder
    """Phone numbers"""
    preferred_contact: AirbyteSortOrder
    """Preferred contact"""
    quora_url: AirbyteSortOrder
    """Quora url"""
    region: AirbyteSortOrder
    """Region"""
    reply_count: AirbyteSortOrder
    """Reply count"""
    school: AirbyteSortOrder
    """School"""
    score: AirbyteSortOrder
    """Score"""
    sequence_states: AirbyteSortOrder
    """Sequence states"""
    sharing_team_id: AirbyteSortOrder
    """Sharing team id"""
    sms_opt_status: AirbyteSortOrder
    """Sms opt status"""
    sms_opted_at: AirbyteSortOrder
    """Sms opted at"""
    sms_opted_out: AirbyteSortOrder
    """Sms opted out"""
    source: AirbyteSortOrder
    """Source"""
    specialties: AirbyteSortOrder
    """Specialties"""
    stack_overflow_id: AirbyteSortOrder
    """Stack overflow id"""
    stack_overflow_url: AirbyteSortOrder
    """Stack overflow url"""
    stage: AirbyteSortOrder
    """Stage"""
    stage_name: AirbyteSortOrder
    """Stage name"""
    tags: AirbyteSortOrder
    """Tags"""
    tasks: AirbyteSortOrder
    """Tasks"""
    time_zone: AirbyteSortOrder
    """Time zone"""
    time_zone_iana: AirbyteSortOrder
    """Time zone iana"""
    time_zone_inferred: AirbyteSortOrder
    """Time zone inferred"""
    title: AirbyteSortOrder
    """Title"""
    touched_at: AirbyteSortOrder
    """Touched at"""
    trashed_at: AirbyteSortOrder
    """Trashed at"""
    trashed_by_account: AirbyteSortOrder
    """Trashed by account"""
    twitter_url: AirbyteSortOrder
    """Twitter url"""
    twitter_username: AirbyteSortOrder
    """Twitter username"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""
    updater_id: AirbyteSortOrder
    """Updater id"""
    updater_type: AirbyteSortOrder
    """Updater type"""
    voip_phones: AirbyteSortOrder
    """Voip phones"""
    website_url1: AirbyteSortOrder
    """Website url1"""
    website_url2: AirbyteSortOrder
    """Website url2"""
    website_url3: AirbyteSortOrder
    """Website url3"""
    work_phones: AirbyteSortOrder
    """Work phones"""


# Entity-specific condition types for prospects
class ProspectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProspectsSearchFilter


class ProspectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProspectsSearchFilter


class ProspectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProspectsSearchFilter


class ProspectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProspectsSearchFilter


class ProspectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProspectsSearchFilter


class ProspectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProspectsSearchFilter


class ProspectsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ProspectsStringFilter


class ProspectsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ProspectsStringFilter


class ProspectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProspectsStringFilter


class ProspectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProspectsStringFilter


class ProspectsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: ProspectsAnyValueFilter


class ProspectsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: ProspectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProspectsInCondition = TypedDict("ProspectsInCondition", {"in": ProspectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProspectsNotCondition = TypedDict("ProspectsNotCondition", {"not": "ProspectsCondition"}, total=False)
"""Negates the nested condition."""

ProspectsAndCondition = TypedDict("ProspectsAndCondition", {"and": "list[ProspectsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProspectsOrCondition = TypedDict("ProspectsOrCondition", {"or": "list[ProspectsCondition]"}, total=False)
"""True if any nested condition is true."""

ProspectsAnyCondition = TypedDict("ProspectsAnyCondition", {"any": ProspectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all prospects condition types
ProspectsCondition = (
    ProspectsEqCondition
    | ProspectsNeqCondition
    | ProspectsGtCondition
    | ProspectsGteCondition
    | ProspectsLtCondition
    | ProspectsLteCondition
    | ProspectsInCondition
    | ProspectsStartswithCondition
    | ProspectsEndswithCondition
    | ProspectsFuzzyCondition
    | ProspectsKeywordCondition
    | ProspectsContainsCondition
    | ProspectsArrayContainsCondition
    | ProspectsNotCondition
    | ProspectsAndCondition
    | ProspectsOrCondition
    | ProspectsAnyCondition
)


class ProspectsSearchQuery(TypedDict, total=False):
    """Search query for prospects entity."""
    filter: ProspectsCondition
    sort: list[ProspectsSortFilter]


# ===== SEQUENCES SEARCH TYPES =====

class SequencesSearchFilter(TypedDict, total=False):
    """Available fields for filtering sequences search queries."""
    automation_percentage: float | None
    """Automation percentage"""
    bounce_count: int | None
    """Bounce count"""
    calls: list[Any] | None
    """Calls"""
    click_count: int | None
    """Click count"""
    content_category_memberships: list[Any] | None
    """Content category memberships"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    deliver_count: int | None
    """Deliver count"""
    description: str | None
    """Description"""
    duration_in_days: int | None
    """Duration in days"""
    enabled: bool | None
    """Enabled"""
    enabled_at: str | None
    """Enabled at"""
    failure_count: int | None
    """Failure count"""
    finish_on_reply: bool | None
    """Finish on reply"""
    id: int | None
    """Unique sequence identifier"""
    last_used_at: str | None
    """Last used at"""
    locked: bool | None
    """Locked"""
    locked_at: str | None
    """Locked at"""
    mailings: list[Any] | None
    """Mailings"""
    max_activations: int | None
    """Max activations"""
    name: str | None
    """Name"""
    negative_reply_count: int | None
    """Negative reply count"""
    neutral_reply_count: int | None
    """Neutral reply count"""
    num_contacted_prospects: int | None
    """Num contacted prospects"""
    num_replied_prospects: int | None
    """Num replied prospects"""
    open_count: int | None
    """Open count"""
    opt_out_count: int | None
    """Opt out count"""
    owner: list[Any] | None
    """Owner"""
    positive_reply_count: int | None
    """Positive reply count"""
    primary_reply_action: str | None
    """Primary reply action"""
    primary_reply_pause_duration: int | None
    """Primary reply pause duration"""
    reply_count: int | None
    """Reply count"""
    ruleset: list[Any] | None
    """Ruleset"""
    schedule: list[Any] | None
    """Schedule"""
    schedule_count: int | None
    """Schedule count"""
    schedule_interval_type: str | None
    """Schedule interval type"""
    secondary_reply_action: str | None
    """Secondary reply action"""
    secondary_reply_pause_duration: int | None
    """Secondary reply pause duration"""
    sequence_states: list[Any] | None
    """Sequence states"""
    sequence_step_count: int | None
    """Sequence step count"""
    sequence_steps: list[Any] | None
    """Sequence steps"""
    sequence_type: str | None
    """Sequence type"""
    share_type: str | None
    """Share type"""
    tags: list[Any] | None
    """Tags"""
    tasks: list[Any] | None
    """Tasks"""
    throttle_capacity: int | None
    """Throttle capacity"""
    throttle_max_adds_per_day: int | None
    """Throttle max adds per day"""
    throttle_paused: bool | None
    """Throttle paused"""
    throttle_paused_at: str | None
    """Throttle paused at"""
    transactional: bool | None
    """Transactional"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""


class SequencesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    automation_percentage: list[float]
    """Automation percentage"""
    bounce_count: list[int]
    """Bounce count"""
    calls: list[list[Any]]
    """Calls"""
    click_count: list[int]
    """Click count"""
    content_category_memberships: list[list[Any]]
    """Content category memberships"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    deliver_count: list[int]
    """Deliver count"""
    description: list[str]
    """Description"""
    duration_in_days: list[int]
    """Duration in days"""
    enabled: list[bool]
    """Enabled"""
    enabled_at: list[str]
    """Enabled at"""
    failure_count: list[int]
    """Failure count"""
    finish_on_reply: list[bool]
    """Finish on reply"""
    id: list[int]
    """Unique sequence identifier"""
    last_used_at: list[str]
    """Last used at"""
    locked: list[bool]
    """Locked"""
    locked_at: list[str]
    """Locked at"""
    mailings: list[list[Any]]
    """Mailings"""
    max_activations: list[int]
    """Max activations"""
    name: list[str]
    """Name"""
    negative_reply_count: list[int]
    """Negative reply count"""
    neutral_reply_count: list[int]
    """Neutral reply count"""
    num_contacted_prospects: list[int]
    """Num contacted prospects"""
    num_replied_prospects: list[int]
    """Num replied prospects"""
    open_count: list[int]
    """Open count"""
    opt_out_count: list[int]
    """Opt out count"""
    owner: list[list[Any]]
    """Owner"""
    positive_reply_count: list[int]
    """Positive reply count"""
    primary_reply_action: list[str]
    """Primary reply action"""
    primary_reply_pause_duration: list[int]
    """Primary reply pause duration"""
    reply_count: list[int]
    """Reply count"""
    ruleset: list[list[Any]]
    """Ruleset"""
    schedule: list[list[Any]]
    """Schedule"""
    schedule_count: list[int]
    """Schedule count"""
    schedule_interval_type: list[str]
    """Schedule interval type"""
    secondary_reply_action: list[str]
    """Secondary reply action"""
    secondary_reply_pause_duration: list[int]
    """Secondary reply pause duration"""
    sequence_states: list[list[Any]]
    """Sequence states"""
    sequence_step_count: list[int]
    """Sequence step count"""
    sequence_steps: list[list[Any]]
    """Sequence steps"""
    sequence_type: list[str]
    """Sequence type"""
    share_type: list[str]
    """Share type"""
    tags: list[list[Any]]
    """Tags"""
    tasks: list[list[Any]]
    """Tasks"""
    throttle_capacity: list[int]
    """Throttle capacity"""
    throttle_max_adds_per_day: list[int]
    """Throttle max adds per day"""
    throttle_paused: list[bool]
    """Throttle paused"""
    throttle_paused_at: list[str]
    """Throttle paused at"""
    transactional: list[bool]
    """Transactional"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""


class SequencesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    automation_percentage: Any
    """Automation percentage"""
    bounce_count: Any
    """Bounce count"""
    calls: Any
    """Calls"""
    click_count: Any
    """Click count"""
    content_category_memberships: Any
    """Content category memberships"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    deliver_count: Any
    """Deliver count"""
    description: Any
    """Description"""
    duration_in_days: Any
    """Duration in days"""
    enabled: Any
    """Enabled"""
    enabled_at: Any
    """Enabled at"""
    failure_count: Any
    """Failure count"""
    finish_on_reply: Any
    """Finish on reply"""
    id: Any
    """Unique sequence identifier"""
    last_used_at: Any
    """Last used at"""
    locked: Any
    """Locked"""
    locked_at: Any
    """Locked at"""
    mailings: Any
    """Mailings"""
    max_activations: Any
    """Max activations"""
    name: Any
    """Name"""
    negative_reply_count: Any
    """Negative reply count"""
    neutral_reply_count: Any
    """Neutral reply count"""
    num_contacted_prospects: Any
    """Num contacted prospects"""
    num_replied_prospects: Any
    """Num replied prospects"""
    open_count: Any
    """Open count"""
    opt_out_count: Any
    """Opt out count"""
    owner: Any
    """Owner"""
    positive_reply_count: Any
    """Positive reply count"""
    primary_reply_action: Any
    """Primary reply action"""
    primary_reply_pause_duration: Any
    """Primary reply pause duration"""
    reply_count: Any
    """Reply count"""
    ruleset: Any
    """Ruleset"""
    schedule: Any
    """Schedule"""
    schedule_count: Any
    """Schedule count"""
    schedule_interval_type: Any
    """Schedule interval type"""
    secondary_reply_action: Any
    """Secondary reply action"""
    secondary_reply_pause_duration: Any
    """Secondary reply pause duration"""
    sequence_states: Any
    """Sequence states"""
    sequence_step_count: Any
    """Sequence step count"""
    sequence_steps: Any
    """Sequence steps"""
    sequence_type: Any
    """Sequence type"""
    share_type: Any
    """Share type"""
    tags: Any
    """Tags"""
    tasks: Any
    """Tasks"""
    throttle_capacity: Any
    """Throttle capacity"""
    throttle_max_adds_per_day: Any
    """Throttle max adds per day"""
    throttle_paused: Any
    """Throttle paused"""
    throttle_paused_at: Any
    """Throttle paused at"""
    transactional: Any
    """Transactional"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""


class SequencesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    automation_percentage: str
    """Automation percentage"""
    bounce_count: str
    """Bounce count"""
    calls: str
    """Calls"""
    click_count: str
    """Click count"""
    content_category_memberships: str
    """Content category memberships"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    deliver_count: str
    """Deliver count"""
    description: str
    """Description"""
    duration_in_days: str
    """Duration in days"""
    enabled: str
    """Enabled"""
    enabled_at: str
    """Enabled at"""
    failure_count: str
    """Failure count"""
    finish_on_reply: str
    """Finish on reply"""
    id: str
    """Unique sequence identifier"""
    last_used_at: str
    """Last used at"""
    locked: str
    """Locked"""
    locked_at: str
    """Locked at"""
    mailings: str
    """Mailings"""
    max_activations: str
    """Max activations"""
    name: str
    """Name"""
    negative_reply_count: str
    """Negative reply count"""
    neutral_reply_count: str
    """Neutral reply count"""
    num_contacted_prospects: str
    """Num contacted prospects"""
    num_replied_prospects: str
    """Num replied prospects"""
    open_count: str
    """Open count"""
    opt_out_count: str
    """Opt out count"""
    owner: str
    """Owner"""
    positive_reply_count: str
    """Positive reply count"""
    primary_reply_action: str
    """Primary reply action"""
    primary_reply_pause_duration: str
    """Primary reply pause duration"""
    reply_count: str
    """Reply count"""
    ruleset: str
    """Ruleset"""
    schedule: str
    """Schedule"""
    schedule_count: str
    """Schedule count"""
    schedule_interval_type: str
    """Schedule interval type"""
    secondary_reply_action: str
    """Secondary reply action"""
    secondary_reply_pause_duration: str
    """Secondary reply pause duration"""
    sequence_states: str
    """Sequence states"""
    sequence_step_count: str
    """Sequence step count"""
    sequence_steps: str
    """Sequence steps"""
    sequence_type: str
    """Sequence type"""
    share_type: str
    """Share type"""
    tags: str
    """Tags"""
    tasks: str
    """Tasks"""
    throttle_capacity: str
    """Throttle capacity"""
    throttle_max_adds_per_day: str
    """Throttle max adds per day"""
    throttle_paused: str
    """Throttle paused"""
    throttle_paused_at: str
    """Throttle paused at"""
    transactional: str
    """Transactional"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""


class SequencesSortFilter(TypedDict, total=False):
    """Available fields for sorting sequences search results."""
    automation_percentage: AirbyteSortOrder
    """Automation percentage"""
    bounce_count: AirbyteSortOrder
    """Bounce count"""
    calls: AirbyteSortOrder
    """Calls"""
    click_count: AirbyteSortOrder
    """Click count"""
    content_category_memberships: AirbyteSortOrder
    """Content category memberships"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    deliver_count: AirbyteSortOrder
    """Deliver count"""
    description: AirbyteSortOrder
    """Description"""
    duration_in_days: AirbyteSortOrder
    """Duration in days"""
    enabled: AirbyteSortOrder
    """Enabled"""
    enabled_at: AirbyteSortOrder
    """Enabled at"""
    failure_count: AirbyteSortOrder
    """Failure count"""
    finish_on_reply: AirbyteSortOrder
    """Finish on reply"""
    id: AirbyteSortOrder
    """Unique sequence identifier"""
    last_used_at: AirbyteSortOrder
    """Last used at"""
    locked: AirbyteSortOrder
    """Locked"""
    locked_at: AirbyteSortOrder
    """Locked at"""
    mailings: AirbyteSortOrder
    """Mailings"""
    max_activations: AirbyteSortOrder
    """Max activations"""
    name: AirbyteSortOrder
    """Name"""
    negative_reply_count: AirbyteSortOrder
    """Negative reply count"""
    neutral_reply_count: AirbyteSortOrder
    """Neutral reply count"""
    num_contacted_prospects: AirbyteSortOrder
    """Num contacted prospects"""
    num_replied_prospects: AirbyteSortOrder
    """Num replied prospects"""
    open_count: AirbyteSortOrder
    """Open count"""
    opt_out_count: AirbyteSortOrder
    """Opt out count"""
    owner: AirbyteSortOrder
    """Owner"""
    positive_reply_count: AirbyteSortOrder
    """Positive reply count"""
    primary_reply_action: AirbyteSortOrder
    """Primary reply action"""
    primary_reply_pause_duration: AirbyteSortOrder
    """Primary reply pause duration"""
    reply_count: AirbyteSortOrder
    """Reply count"""
    ruleset: AirbyteSortOrder
    """Ruleset"""
    schedule: AirbyteSortOrder
    """Schedule"""
    schedule_count: AirbyteSortOrder
    """Schedule count"""
    schedule_interval_type: AirbyteSortOrder
    """Schedule interval type"""
    secondary_reply_action: AirbyteSortOrder
    """Secondary reply action"""
    secondary_reply_pause_duration: AirbyteSortOrder
    """Secondary reply pause duration"""
    sequence_states: AirbyteSortOrder
    """Sequence states"""
    sequence_step_count: AirbyteSortOrder
    """Sequence step count"""
    sequence_steps: AirbyteSortOrder
    """Sequence steps"""
    sequence_type: AirbyteSortOrder
    """Sequence type"""
    share_type: AirbyteSortOrder
    """Share type"""
    tags: AirbyteSortOrder
    """Tags"""
    tasks: AirbyteSortOrder
    """Tasks"""
    throttle_capacity: AirbyteSortOrder
    """Throttle capacity"""
    throttle_max_adds_per_day: AirbyteSortOrder
    """Throttle max adds per day"""
    throttle_paused: AirbyteSortOrder
    """Throttle paused"""
    throttle_paused_at: AirbyteSortOrder
    """Throttle paused at"""
    transactional: AirbyteSortOrder
    """Transactional"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""


# Entity-specific condition types for sequences
class SequencesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SequencesSearchFilter


class SequencesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SequencesSearchFilter


class SequencesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SequencesSearchFilter


class SequencesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SequencesSearchFilter


class SequencesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SequencesSearchFilter


class SequencesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SequencesSearchFilter


class SequencesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SequencesStringFilter


class SequencesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SequencesStringFilter


class SequencesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SequencesStringFilter


class SequencesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SequencesStringFilter


class SequencesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: SequencesAnyValueFilter


class SequencesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: SequencesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SequencesInCondition = TypedDict("SequencesInCondition", {"in": SequencesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SequencesNotCondition = TypedDict("SequencesNotCondition", {"not": "SequencesCondition"}, total=False)
"""Negates the nested condition."""

SequencesAndCondition = TypedDict("SequencesAndCondition", {"and": "list[SequencesCondition]"}, total=False)
"""True if all nested conditions are true."""

SequencesOrCondition = TypedDict("SequencesOrCondition", {"or": "list[SequencesCondition]"}, total=False)
"""True if any nested condition is true."""

SequencesAnyCondition = TypedDict("SequencesAnyCondition", {"any": SequencesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sequences condition types
SequencesCondition = (
    SequencesEqCondition
    | SequencesNeqCondition
    | SequencesGtCondition
    | SequencesGteCondition
    | SequencesLtCondition
    | SequencesLteCondition
    | SequencesInCondition
    | SequencesStartswithCondition
    | SequencesEndswithCondition
    | SequencesFuzzyCondition
    | SequencesKeywordCondition
    | SequencesContainsCondition
    | SequencesArrayContainsCondition
    | SequencesNotCondition
    | SequencesAndCondition
    | SequencesOrCondition
    | SequencesAnyCondition
)


class SequencesSearchQuery(TypedDict, total=False):
    """Search query for sequences entity."""
    filter: SequencesCondition
    sort: list[SequencesSortFilter]


# ===== SEQUENCE_STATES SEARCH TYPES =====

class SequenceStatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering sequence_states search queries."""
    account: list[Any] | None
    """Account"""
    active_at: str | None
    """Active at"""
    active_step_mailings: list[Any] | None
    """Active step mailings"""
    active_step_tasks: list[Any] | None
    """Active step tasks"""
    bounce_count: int | None
    """Bounce count"""
    call_completed_at: str | None
    """Call completed at"""
    calls: list[Any] | None
    """Calls"""
    click_count: int | None
    """Click count"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    deliver_count: int | None
    """Deliver count"""
    error_reason: str | None
    """Error reason"""
    failure_count: int | None
    """Failure count"""
    id: int | None
    """Unique sequence state identifier"""
    mailbox: list[Any] | None
    """Mailbox"""
    mailings: list[Any] | None
    """Mailings"""
    negative_reply_count: int | None
    """Negative reply count"""
    neutral_reply_count: int | None
    """Neutral reply count"""
    open_count: int | None
    """Open count"""
    opportunity: list[Any] | None
    """Opportunity"""
    opt_out_count: int | None
    """Opt out count"""
    pause_reason: str | None
    """Pause reason"""
    positive_reply_count: int | None
    """Positive reply count"""
    prospect: list[Any] | None
    """Prospect"""
    replied_at: str | None
    """Replied at"""
    reply_count: int | None
    """Reply count"""
    schedule_count: int | None
    """Schedule count"""
    sequence: list[Any] | None
    """Sequence"""
    sequence_step: list[Any] | None
    """Sequence step"""
    state: str | None
    """State"""
    state_changed_at: str | None
    """State changed at"""
    tasks: list[Any] | None
    """Tasks"""
    updated_at: str | None
    """Updated at"""


class SequenceStatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account: list[list[Any]]
    """Account"""
    active_at: list[str]
    """Active at"""
    active_step_mailings: list[list[Any]]
    """Active step mailings"""
    active_step_tasks: list[list[Any]]
    """Active step tasks"""
    bounce_count: list[int]
    """Bounce count"""
    call_completed_at: list[str]
    """Call completed at"""
    calls: list[list[Any]]
    """Calls"""
    click_count: list[int]
    """Click count"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    deliver_count: list[int]
    """Deliver count"""
    error_reason: list[str]
    """Error reason"""
    failure_count: list[int]
    """Failure count"""
    id: list[int]
    """Unique sequence state identifier"""
    mailbox: list[list[Any]]
    """Mailbox"""
    mailings: list[list[Any]]
    """Mailings"""
    negative_reply_count: list[int]
    """Negative reply count"""
    neutral_reply_count: list[int]
    """Neutral reply count"""
    open_count: list[int]
    """Open count"""
    opportunity: list[list[Any]]
    """Opportunity"""
    opt_out_count: list[int]
    """Opt out count"""
    pause_reason: list[str]
    """Pause reason"""
    positive_reply_count: list[int]
    """Positive reply count"""
    prospect: list[list[Any]]
    """Prospect"""
    replied_at: list[str]
    """Replied at"""
    reply_count: list[int]
    """Reply count"""
    schedule_count: list[int]
    """Schedule count"""
    sequence: list[list[Any]]
    """Sequence"""
    sequence_step: list[list[Any]]
    """Sequence step"""
    state: list[str]
    """State"""
    state_changed_at: list[str]
    """State changed at"""
    tasks: list[list[Any]]
    """Tasks"""
    updated_at: list[str]
    """Updated at"""


class SequenceStatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account: Any
    """Account"""
    active_at: Any
    """Active at"""
    active_step_mailings: Any
    """Active step mailings"""
    active_step_tasks: Any
    """Active step tasks"""
    bounce_count: Any
    """Bounce count"""
    call_completed_at: Any
    """Call completed at"""
    calls: Any
    """Calls"""
    click_count: Any
    """Click count"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    deliver_count: Any
    """Deliver count"""
    error_reason: Any
    """Error reason"""
    failure_count: Any
    """Failure count"""
    id: Any
    """Unique sequence state identifier"""
    mailbox: Any
    """Mailbox"""
    mailings: Any
    """Mailings"""
    negative_reply_count: Any
    """Negative reply count"""
    neutral_reply_count: Any
    """Neutral reply count"""
    open_count: Any
    """Open count"""
    opportunity: Any
    """Opportunity"""
    opt_out_count: Any
    """Opt out count"""
    pause_reason: Any
    """Pause reason"""
    positive_reply_count: Any
    """Positive reply count"""
    prospect: Any
    """Prospect"""
    replied_at: Any
    """Replied at"""
    reply_count: Any
    """Reply count"""
    schedule_count: Any
    """Schedule count"""
    sequence: Any
    """Sequence"""
    sequence_step: Any
    """Sequence step"""
    state: Any
    """State"""
    state_changed_at: Any
    """State changed at"""
    tasks: Any
    """Tasks"""
    updated_at: Any
    """Updated at"""


class SequenceStatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    account: str
    """Account"""
    active_at: str
    """Active at"""
    active_step_mailings: str
    """Active step mailings"""
    active_step_tasks: str
    """Active step tasks"""
    bounce_count: str
    """Bounce count"""
    call_completed_at: str
    """Call completed at"""
    calls: str
    """Calls"""
    click_count: str
    """Click count"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    deliver_count: str
    """Deliver count"""
    error_reason: str
    """Error reason"""
    failure_count: str
    """Failure count"""
    id: str
    """Unique sequence state identifier"""
    mailbox: str
    """Mailbox"""
    mailings: str
    """Mailings"""
    negative_reply_count: str
    """Negative reply count"""
    neutral_reply_count: str
    """Neutral reply count"""
    open_count: str
    """Open count"""
    opportunity: str
    """Opportunity"""
    opt_out_count: str
    """Opt out count"""
    pause_reason: str
    """Pause reason"""
    positive_reply_count: str
    """Positive reply count"""
    prospect: str
    """Prospect"""
    replied_at: str
    """Replied at"""
    reply_count: str
    """Reply count"""
    schedule_count: str
    """Schedule count"""
    sequence: str
    """Sequence"""
    sequence_step: str
    """Sequence step"""
    state: str
    """State"""
    state_changed_at: str
    """State changed at"""
    tasks: str
    """Tasks"""
    updated_at: str
    """Updated at"""


class SequenceStatesSortFilter(TypedDict, total=False):
    """Available fields for sorting sequence_states search results."""
    account: AirbyteSortOrder
    """Account"""
    active_at: AirbyteSortOrder
    """Active at"""
    active_step_mailings: AirbyteSortOrder
    """Active step mailings"""
    active_step_tasks: AirbyteSortOrder
    """Active step tasks"""
    bounce_count: AirbyteSortOrder
    """Bounce count"""
    call_completed_at: AirbyteSortOrder
    """Call completed at"""
    calls: AirbyteSortOrder
    """Calls"""
    click_count: AirbyteSortOrder
    """Click count"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    deliver_count: AirbyteSortOrder
    """Deliver count"""
    error_reason: AirbyteSortOrder
    """Error reason"""
    failure_count: AirbyteSortOrder
    """Failure count"""
    id: AirbyteSortOrder
    """Unique sequence state identifier"""
    mailbox: AirbyteSortOrder
    """Mailbox"""
    mailings: AirbyteSortOrder
    """Mailings"""
    negative_reply_count: AirbyteSortOrder
    """Negative reply count"""
    neutral_reply_count: AirbyteSortOrder
    """Neutral reply count"""
    open_count: AirbyteSortOrder
    """Open count"""
    opportunity: AirbyteSortOrder
    """Opportunity"""
    opt_out_count: AirbyteSortOrder
    """Opt out count"""
    pause_reason: AirbyteSortOrder
    """Pause reason"""
    positive_reply_count: AirbyteSortOrder
    """Positive reply count"""
    prospect: AirbyteSortOrder
    """Prospect"""
    replied_at: AirbyteSortOrder
    """Replied at"""
    reply_count: AirbyteSortOrder
    """Reply count"""
    schedule_count: AirbyteSortOrder
    """Schedule count"""
    sequence: AirbyteSortOrder
    """Sequence"""
    sequence_step: AirbyteSortOrder
    """Sequence step"""
    state: AirbyteSortOrder
    """State"""
    state_changed_at: AirbyteSortOrder
    """State changed at"""
    tasks: AirbyteSortOrder
    """Tasks"""
    updated_at: AirbyteSortOrder
    """Updated at"""


# Entity-specific condition types for sequence_states
class SequenceStatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SequenceStatesSearchFilter


class SequenceStatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SequenceStatesSearchFilter


class SequenceStatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SequenceStatesSearchFilter


class SequenceStatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SequenceStatesSearchFilter


class SequenceStatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SequenceStatesSearchFilter


class SequenceStatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SequenceStatesSearchFilter


class SequenceStatesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SequenceStatesStringFilter


class SequenceStatesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SequenceStatesStringFilter


class SequenceStatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SequenceStatesStringFilter


class SequenceStatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SequenceStatesStringFilter


class SequenceStatesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: SequenceStatesAnyValueFilter


class SequenceStatesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: SequenceStatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SequenceStatesInCondition = TypedDict("SequenceStatesInCondition", {"in": SequenceStatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SequenceStatesNotCondition = TypedDict("SequenceStatesNotCondition", {"not": "SequenceStatesCondition"}, total=False)
"""Negates the nested condition."""

SequenceStatesAndCondition = TypedDict("SequenceStatesAndCondition", {"and": "list[SequenceStatesCondition]"}, total=False)
"""True if all nested conditions are true."""

SequenceStatesOrCondition = TypedDict("SequenceStatesOrCondition", {"or": "list[SequenceStatesCondition]"}, total=False)
"""True if any nested condition is true."""

SequenceStatesAnyCondition = TypedDict("SequenceStatesAnyCondition", {"any": SequenceStatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sequence_states condition types
SequenceStatesCondition = (
    SequenceStatesEqCondition
    | SequenceStatesNeqCondition
    | SequenceStatesGtCondition
    | SequenceStatesGteCondition
    | SequenceStatesLtCondition
    | SequenceStatesLteCondition
    | SequenceStatesInCondition
    | SequenceStatesStartswithCondition
    | SequenceStatesEndswithCondition
    | SequenceStatesFuzzyCondition
    | SequenceStatesKeywordCondition
    | SequenceStatesContainsCondition
    | SequenceStatesArrayContainsCondition
    | SequenceStatesNotCondition
    | SequenceStatesAndCondition
    | SequenceStatesOrCondition
    | SequenceStatesAnyCondition
)


class SequenceStatesSearchQuery(TypedDict, total=False):
    """Search query for sequence_states entity."""
    filter: SequenceStatesCondition
    sort: list[SequenceStatesSortFilter]


# ===== SEQUENCE_STEPS SEARCH TYPES =====

class SequenceStepsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sequence_steps search queries."""
    bounce_count: int | None
    """Bounce count"""
    call_purpose: list[Any] | None
    """Call purpose"""
    calls: list[Any] | None
    """Calls"""
    click_count: int | None
    """Click count"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    date: str | None
    """Date"""
    deliver_count: int | None
    """Deliver count"""
    display_name: str | None
    """Display name"""
    failure_count: int | None
    """Failure count"""
    id: int | None
    """Unique sequence step identifier"""
    interval: int | None
    """Interval"""
    mailings: list[Any] | None
    """Mailings"""
    negative_reply_count: int | None
    """Negative reply count"""
    neutral_reply_count: int | None
    """Neutral reply count"""
    open_count: int | None
    """Open count"""
    opt_out_count: int | None
    """Opt out count"""
    order: int | None
    """Order"""
    positive_reply_count: int | None
    """Positive reply count"""
    reply_count: int | None
    """Reply count"""
    schedule_count: int | None
    """Schedule count"""
    sequence: list[Any] | None
    """Sequence"""
    sequence_templates: list[Any] | None
    """Sequence templates"""
    step_type: str | None
    """Step type"""
    task_auto_display: str | None
    """Task auto display"""
    task_priority: list[Any] | None
    """Task priority"""
    tasks: list[Any] | None
    """Tasks"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""


class SequenceStepsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    bounce_count: list[int]
    """Bounce count"""
    call_purpose: list[list[Any]]
    """Call purpose"""
    calls: list[list[Any]]
    """Calls"""
    click_count: list[int]
    """Click count"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    date: list[str]
    """Date"""
    deliver_count: list[int]
    """Deliver count"""
    display_name: list[str]
    """Display name"""
    failure_count: list[int]
    """Failure count"""
    id: list[int]
    """Unique sequence step identifier"""
    interval: list[int]
    """Interval"""
    mailings: list[list[Any]]
    """Mailings"""
    negative_reply_count: list[int]
    """Negative reply count"""
    neutral_reply_count: list[int]
    """Neutral reply count"""
    open_count: list[int]
    """Open count"""
    opt_out_count: list[int]
    """Opt out count"""
    order: list[int]
    """Order"""
    positive_reply_count: list[int]
    """Positive reply count"""
    reply_count: list[int]
    """Reply count"""
    schedule_count: list[int]
    """Schedule count"""
    sequence: list[list[Any]]
    """Sequence"""
    sequence_templates: list[list[Any]]
    """Sequence templates"""
    step_type: list[str]
    """Step type"""
    task_auto_display: list[str]
    """Task auto display"""
    task_priority: list[list[Any]]
    """Task priority"""
    tasks: list[list[Any]]
    """Tasks"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""


class SequenceStepsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    bounce_count: Any
    """Bounce count"""
    call_purpose: Any
    """Call purpose"""
    calls: Any
    """Calls"""
    click_count: Any
    """Click count"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    date: Any
    """Date"""
    deliver_count: Any
    """Deliver count"""
    display_name: Any
    """Display name"""
    failure_count: Any
    """Failure count"""
    id: Any
    """Unique sequence step identifier"""
    interval: Any
    """Interval"""
    mailings: Any
    """Mailings"""
    negative_reply_count: Any
    """Negative reply count"""
    neutral_reply_count: Any
    """Neutral reply count"""
    open_count: Any
    """Open count"""
    opt_out_count: Any
    """Opt out count"""
    order: Any
    """Order"""
    positive_reply_count: Any
    """Positive reply count"""
    reply_count: Any
    """Reply count"""
    schedule_count: Any
    """Schedule count"""
    sequence: Any
    """Sequence"""
    sequence_templates: Any
    """Sequence templates"""
    step_type: Any
    """Step type"""
    task_auto_display: Any
    """Task auto display"""
    task_priority: Any
    """Task priority"""
    tasks: Any
    """Tasks"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""


class SequenceStepsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    bounce_count: str
    """Bounce count"""
    call_purpose: str
    """Call purpose"""
    calls: str
    """Calls"""
    click_count: str
    """Click count"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    date: str
    """Date"""
    deliver_count: str
    """Deliver count"""
    display_name: str
    """Display name"""
    failure_count: str
    """Failure count"""
    id: str
    """Unique sequence step identifier"""
    interval: str
    """Interval"""
    mailings: str
    """Mailings"""
    negative_reply_count: str
    """Negative reply count"""
    neutral_reply_count: str
    """Neutral reply count"""
    open_count: str
    """Open count"""
    opt_out_count: str
    """Opt out count"""
    order: str
    """Order"""
    positive_reply_count: str
    """Positive reply count"""
    reply_count: str
    """Reply count"""
    schedule_count: str
    """Schedule count"""
    sequence: str
    """Sequence"""
    sequence_templates: str
    """Sequence templates"""
    step_type: str
    """Step type"""
    task_auto_display: str
    """Task auto display"""
    task_priority: str
    """Task priority"""
    tasks: str
    """Tasks"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""


class SequenceStepsSortFilter(TypedDict, total=False):
    """Available fields for sorting sequence_steps search results."""
    bounce_count: AirbyteSortOrder
    """Bounce count"""
    call_purpose: AirbyteSortOrder
    """Call purpose"""
    calls: AirbyteSortOrder
    """Calls"""
    click_count: AirbyteSortOrder
    """Click count"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    date: AirbyteSortOrder
    """Date"""
    deliver_count: AirbyteSortOrder
    """Deliver count"""
    display_name: AirbyteSortOrder
    """Display name"""
    failure_count: AirbyteSortOrder
    """Failure count"""
    id: AirbyteSortOrder
    """Unique sequence step identifier"""
    interval: AirbyteSortOrder
    """Interval"""
    mailings: AirbyteSortOrder
    """Mailings"""
    negative_reply_count: AirbyteSortOrder
    """Negative reply count"""
    neutral_reply_count: AirbyteSortOrder
    """Neutral reply count"""
    open_count: AirbyteSortOrder
    """Open count"""
    opt_out_count: AirbyteSortOrder
    """Opt out count"""
    order: AirbyteSortOrder
    """Order"""
    positive_reply_count: AirbyteSortOrder
    """Positive reply count"""
    reply_count: AirbyteSortOrder
    """Reply count"""
    schedule_count: AirbyteSortOrder
    """Schedule count"""
    sequence: AirbyteSortOrder
    """Sequence"""
    sequence_templates: AirbyteSortOrder
    """Sequence templates"""
    step_type: AirbyteSortOrder
    """Step type"""
    task_auto_display: AirbyteSortOrder
    """Task auto display"""
    task_priority: AirbyteSortOrder
    """Task priority"""
    tasks: AirbyteSortOrder
    """Tasks"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""


# Entity-specific condition types for sequence_steps
class SequenceStepsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SequenceStepsSearchFilter


class SequenceStepsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SequenceStepsSearchFilter


class SequenceStepsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SequenceStepsSearchFilter


class SequenceStepsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SequenceStepsSearchFilter


class SequenceStepsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SequenceStepsSearchFilter


class SequenceStepsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SequenceStepsSearchFilter


class SequenceStepsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SequenceStepsStringFilter


class SequenceStepsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SequenceStepsStringFilter


class SequenceStepsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SequenceStepsStringFilter


class SequenceStepsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SequenceStepsStringFilter


class SequenceStepsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: SequenceStepsAnyValueFilter


class SequenceStepsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: SequenceStepsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SequenceStepsInCondition = TypedDict("SequenceStepsInCondition", {"in": SequenceStepsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SequenceStepsNotCondition = TypedDict("SequenceStepsNotCondition", {"not": "SequenceStepsCondition"}, total=False)
"""Negates the nested condition."""

SequenceStepsAndCondition = TypedDict("SequenceStepsAndCondition", {"and": "list[SequenceStepsCondition]"}, total=False)
"""True if all nested conditions are true."""

SequenceStepsOrCondition = TypedDict("SequenceStepsOrCondition", {"or": "list[SequenceStepsCondition]"}, total=False)
"""True if any nested condition is true."""

SequenceStepsAnyCondition = TypedDict("SequenceStepsAnyCondition", {"any": SequenceStepsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sequence_steps condition types
SequenceStepsCondition = (
    SequenceStepsEqCondition
    | SequenceStepsNeqCondition
    | SequenceStepsGtCondition
    | SequenceStepsGteCondition
    | SequenceStepsLtCondition
    | SequenceStepsLteCondition
    | SequenceStepsInCondition
    | SequenceStepsStartswithCondition
    | SequenceStepsEndswithCondition
    | SequenceStepsFuzzyCondition
    | SequenceStepsKeywordCondition
    | SequenceStepsContainsCondition
    | SequenceStepsArrayContainsCondition
    | SequenceStepsNotCondition
    | SequenceStepsAndCondition
    | SequenceStepsOrCondition
    | SequenceStepsAnyCondition
)


class SequenceStepsSearchQuery(TypedDict, total=False):
    """Search query for sequence_steps entity."""
    filter: SequenceStepsCondition
    sort: list[SequenceStepsSortFilter]


# ===== SNIPPETS SEARCH TYPES =====

class SnippetsSearchFilter(TypedDict, total=False):
    """Available fields for filtering snippets search queries."""
    body_html: str | None
    """Body html"""
    body_text: str | None
    """Body text"""
    content_category_memberships: list[Any] | None
    """Content category memberships"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    id: int | None
    """Unique snippet identifier"""
    name: str | None
    """Name"""
    owner: list[Any] | None
    """Owner"""
    share_type: str | None
    """Share type"""
    tags: str | None
    """Tags"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""


class SnippetsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    body_html: list[str]
    """Body html"""
    body_text: list[str]
    """Body text"""
    content_category_memberships: list[list[Any]]
    """Content category memberships"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    id: list[int]
    """Unique snippet identifier"""
    name: list[str]
    """Name"""
    owner: list[list[Any]]
    """Owner"""
    share_type: list[str]
    """Share type"""
    tags: list[str]
    """Tags"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""


class SnippetsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    body_html: Any
    """Body html"""
    body_text: Any
    """Body text"""
    content_category_memberships: Any
    """Content category memberships"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    id: Any
    """Unique snippet identifier"""
    name: Any
    """Name"""
    owner: Any
    """Owner"""
    share_type: Any
    """Share type"""
    tags: Any
    """Tags"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""


class SnippetsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    body_html: str
    """Body html"""
    body_text: str
    """Body text"""
    content_category_memberships: str
    """Content category memberships"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    id: str
    """Unique snippet identifier"""
    name: str
    """Name"""
    owner: str
    """Owner"""
    share_type: str
    """Share type"""
    tags: str
    """Tags"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""


class SnippetsSortFilter(TypedDict, total=False):
    """Available fields for sorting snippets search results."""
    body_html: AirbyteSortOrder
    """Body html"""
    body_text: AirbyteSortOrder
    """Body text"""
    content_category_memberships: AirbyteSortOrder
    """Content category memberships"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    id: AirbyteSortOrder
    """Unique snippet identifier"""
    name: AirbyteSortOrder
    """Name"""
    owner: AirbyteSortOrder
    """Owner"""
    share_type: AirbyteSortOrder
    """Share type"""
    tags: AirbyteSortOrder
    """Tags"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""


# Entity-specific condition types for snippets
class SnippetsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SnippetsSearchFilter


class SnippetsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SnippetsSearchFilter


class SnippetsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SnippetsSearchFilter


class SnippetsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SnippetsSearchFilter


class SnippetsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SnippetsSearchFilter


class SnippetsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SnippetsSearchFilter


class SnippetsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SnippetsStringFilter


class SnippetsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SnippetsStringFilter


class SnippetsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SnippetsStringFilter


class SnippetsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SnippetsStringFilter


class SnippetsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: SnippetsAnyValueFilter


class SnippetsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: SnippetsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SnippetsInCondition = TypedDict("SnippetsInCondition", {"in": SnippetsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SnippetsNotCondition = TypedDict("SnippetsNotCondition", {"not": "SnippetsCondition"}, total=False)
"""Negates the nested condition."""

SnippetsAndCondition = TypedDict("SnippetsAndCondition", {"and": "list[SnippetsCondition]"}, total=False)
"""True if all nested conditions are true."""

SnippetsOrCondition = TypedDict("SnippetsOrCondition", {"or": "list[SnippetsCondition]"}, total=False)
"""True if any nested condition is true."""

SnippetsAnyCondition = TypedDict("SnippetsAnyCondition", {"any": SnippetsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all snippets condition types
SnippetsCondition = (
    SnippetsEqCondition
    | SnippetsNeqCondition
    | SnippetsGtCondition
    | SnippetsGteCondition
    | SnippetsLtCondition
    | SnippetsLteCondition
    | SnippetsInCondition
    | SnippetsStartswithCondition
    | SnippetsEndswithCondition
    | SnippetsFuzzyCondition
    | SnippetsKeywordCondition
    | SnippetsContainsCondition
    | SnippetsArrayContainsCondition
    | SnippetsNotCondition
    | SnippetsAndCondition
    | SnippetsOrCondition
    | SnippetsAnyCondition
)


class SnippetsSearchQuery(TypedDict, total=False):
    """Search query for snippets entity."""
    filter: SnippetsCondition
    sort: list[SnippetsSortFilter]


# ===== STAGES SEARCH TYPES =====

class StagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering stages search queries."""
    color: str | None
    """Color"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    id: int | None
    """Unique stage identifier"""
    name: str | None
    """Name"""
    order: int | None
    """Order"""
    prospects: list[Any] | None
    """Prospects"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""


class StagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    color: list[str]
    """Color"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    id: list[int]
    """Unique stage identifier"""
    name: list[str]
    """Name"""
    order: list[int]
    """Order"""
    prospects: list[list[Any]]
    """Prospects"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""


class StagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    color: Any
    """Color"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    id: Any
    """Unique stage identifier"""
    name: Any
    """Name"""
    order: Any
    """Order"""
    prospects: Any
    """Prospects"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""


class StagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    color: str
    """Color"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    id: str
    """Unique stage identifier"""
    name: str
    """Name"""
    order: str
    """Order"""
    prospects: str
    """Prospects"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""


class StagesSortFilter(TypedDict, total=False):
    """Available fields for sorting stages search results."""
    color: AirbyteSortOrder
    """Color"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    id: AirbyteSortOrder
    """Unique stage identifier"""
    name: AirbyteSortOrder
    """Name"""
    order: AirbyteSortOrder
    """Order"""
    prospects: AirbyteSortOrder
    """Prospects"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""


# Entity-specific condition types for stages
class StagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: StagesSearchFilter


class StagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: StagesSearchFilter


class StagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: StagesSearchFilter


class StagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: StagesSearchFilter


class StagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: StagesSearchFilter


class StagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: StagesSearchFilter


class StagesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: StagesStringFilter


class StagesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: StagesStringFilter


class StagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: StagesStringFilter


class StagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: StagesStringFilter


class StagesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: StagesAnyValueFilter


class StagesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: StagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
StagesInCondition = TypedDict("StagesInCondition", {"in": StagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

StagesNotCondition = TypedDict("StagesNotCondition", {"not": "StagesCondition"}, total=False)
"""Negates the nested condition."""

StagesAndCondition = TypedDict("StagesAndCondition", {"and": "list[StagesCondition]"}, total=False)
"""True if all nested conditions are true."""

StagesOrCondition = TypedDict("StagesOrCondition", {"or": "list[StagesCondition]"}, total=False)
"""True if any nested condition is true."""

StagesAnyCondition = TypedDict("StagesAnyCondition", {"any": StagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all stages condition types
StagesCondition = (
    StagesEqCondition
    | StagesNeqCondition
    | StagesGtCondition
    | StagesGteCondition
    | StagesLtCondition
    | StagesLteCondition
    | StagesInCondition
    | StagesStartswithCondition
    | StagesEndswithCondition
    | StagesFuzzyCondition
    | StagesKeywordCondition
    | StagesContainsCondition
    | StagesArrayContainsCondition
    | StagesNotCondition
    | StagesAndCondition
    | StagesOrCondition
    | StagesAnyCondition
)


class StagesSearchQuery(TypedDict, total=False):
    """Search query for stages entity."""
    filter: StagesCondition
    sort: list[StagesSortFilter]


# ===== TASKS SEARCH TYPES =====

class TasksSearchFilter(TypedDict, total=False):
    """Available fields for filtering tasks search queries."""
    account: list[Any] | None
    """Account"""
    action: str | None
    """Action"""
    autoskip_at: str | None
    """Autoskip at"""
    call: list[Any] | None
    """Call"""
    calls: list[Any] | None
    """Calls"""
    compiled_sequence_template_html: str | None
    """Compiled sequence template html"""
    completed: bool | None
    """Completed"""
    completed_at: str | None
    """Completed at"""
    completer: list[Any] | None
    """Completer"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    default_plugin_mapping: list[Any] | None
    """Default plugin mapping"""
    due_at: str | None
    """Due at"""
    id: int | None
    """Unique task identifier"""
    mailing: list[Any] | None
    """Mailing"""
    mailings: list[Any] | None
    """Mailings"""
    note: str | None
    """Note"""
    opportunity: list[Any] | None
    """Opportunity"""
    opportunity_association: str | None
    """Opportunity association"""
    owner: list[Any] | None
    """Owner"""
    prospect: list[Any] | None
    """Prospect"""
    prospect_account: list[Any] | None
    """Prospect account"""
    prospect_contacts: list[Any] | None
    """Prospect contacts"""
    prospect_owner: list[Any] | None
    """Prospect owner"""
    prospect_phone_numbers: list[Any] | None
    """Prospect phone numbers"""
    prospect_stage: list[Any] | None
    """Prospect stage"""
    scheduled_at: str | None
    """Scheduled at"""
    sequence: list[Any] | None
    """Sequence"""
    sequence_sequence_steps: list[Any] | None
    """Sequence sequence steps"""
    sequence_state: list[Any] | None
    """Sequence state"""
    sequence_state_sequence_step: list[Any] | None
    """Sequence state sequence step"""
    sequence_state_sequence_step_overrides: list[Any] | None
    """Sequence state sequence step overrides"""
    sequence_state_starting_template: list[Any] | None
    """Sequence state starting template"""
    sequence_step: list[Any] | None
    """Sequence step"""
    sequence_step_override_templates: list[Any] | None
    """Sequence step override templates"""
    sequence_template: list[Any] | None
    """Sequence template"""
    sequence_template_template: list[Any] | None
    """Sequence template template"""
    state: str | None
    """State"""
    state_changed_at: str | None
    """State changed at"""
    subject: list[Any] | None
    """Subject"""
    task_priority: list[Any] | None
    """Task priority"""
    task_theme: list[Any] | None
    """Task theme"""
    task_type: str | None
    """Task type"""
    template: list[Any] | None
    """Template"""
    updated_at: str | None
    """Updated at"""


class TasksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account: list[list[Any]]
    """Account"""
    action: list[str]
    """Action"""
    autoskip_at: list[str]
    """Autoskip at"""
    call: list[list[Any]]
    """Call"""
    calls: list[list[Any]]
    """Calls"""
    compiled_sequence_template_html: list[str]
    """Compiled sequence template html"""
    completed: list[bool]
    """Completed"""
    completed_at: list[str]
    """Completed at"""
    completer: list[list[Any]]
    """Completer"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    default_plugin_mapping: list[list[Any]]
    """Default plugin mapping"""
    due_at: list[str]
    """Due at"""
    id: list[int]
    """Unique task identifier"""
    mailing: list[list[Any]]
    """Mailing"""
    mailings: list[list[Any]]
    """Mailings"""
    note: list[str]
    """Note"""
    opportunity: list[list[Any]]
    """Opportunity"""
    opportunity_association: list[str]
    """Opportunity association"""
    owner: list[list[Any]]
    """Owner"""
    prospect: list[list[Any]]
    """Prospect"""
    prospect_account: list[list[Any]]
    """Prospect account"""
    prospect_contacts: list[list[Any]]
    """Prospect contacts"""
    prospect_owner: list[list[Any]]
    """Prospect owner"""
    prospect_phone_numbers: list[list[Any]]
    """Prospect phone numbers"""
    prospect_stage: list[list[Any]]
    """Prospect stage"""
    scheduled_at: list[str]
    """Scheduled at"""
    sequence: list[list[Any]]
    """Sequence"""
    sequence_sequence_steps: list[list[Any]]
    """Sequence sequence steps"""
    sequence_state: list[list[Any]]
    """Sequence state"""
    sequence_state_sequence_step: list[list[Any]]
    """Sequence state sequence step"""
    sequence_state_sequence_step_overrides: list[list[Any]]
    """Sequence state sequence step overrides"""
    sequence_state_starting_template: list[list[Any]]
    """Sequence state starting template"""
    sequence_step: list[list[Any]]
    """Sequence step"""
    sequence_step_override_templates: list[list[Any]]
    """Sequence step override templates"""
    sequence_template: list[list[Any]]
    """Sequence template"""
    sequence_template_template: list[list[Any]]
    """Sequence template template"""
    state: list[str]
    """State"""
    state_changed_at: list[str]
    """State changed at"""
    subject: list[list[Any]]
    """Subject"""
    task_priority: list[list[Any]]
    """Task priority"""
    task_theme: list[list[Any]]
    """Task theme"""
    task_type: list[str]
    """Task type"""
    template: list[list[Any]]
    """Template"""
    updated_at: list[str]
    """Updated at"""


class TasksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account: Any
    """Account"""
    action: Any
    """Action"""
    autoskip_at: Any
    """Autoskip at"""
    call: Any
    """Call"""
    calls: Any
    """Calls"""
    compiled_sequence_template_html: Any
    """Compiled sequence template html"""
    completed: Any
    """Completed"""
    completed_at: Any
    """Completed at"""
    completer: Any
    """Completer"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    default_plugin_mapping: Any
    """Default plugin mapping"""
    due_at: Any
    """Due at"""
    id: Any
    """Unique task identifier"""
    mailing: Any
    """Mailing"""
    mailings: Any
    """Mailings"""
    note: Any
    """Note"""
    opportunity: Any
    """Opportunity"""
    opportunity_association: Any
    """Opportunity association"""
    owner: Any
    """Owner"""
    prospect: Any
    """Prospect"""
    prospect_account: Any
    """Prospect account"""
    prospect_contacts: Any
    """Prospect contacts"""
    prospect_owner: Any
    """Prospect owner"""
    prospect_phone_numbers: Any
    """Prospect phone numbers"""
    prospect_stage: Any
    """Prospect stage"""
    scheduled_at: Any
    """Scheduled at"""
    sequence: Any
    """Sequence"""
    sequence_sequence_steps: Any
    """Sequence sequence steps"""
    sequence_state: Any
    """Sequence state"""
    sequence_state_sequence_step: Any
    """Sequence state sequence step"""
    sequence_state_sequence_step_overrides: Any
    """Sequence state sequence step overrides"""
    sequence_state_starting_template: Any
    """Sequence state starting template"""
    sequence_step: Any
    """Sequence step"""
    sequence_step_override_templates: Any
    """Sequence step override templates"""
    sequence_template: Any
    """Sequence template"""
    sequence_template_template: Any
    """Sequence template template"""
    state: Any
    """State"""
    state_changed_at: Any
    """State changed at"""
    subject: Any
    """Subject"""
    task_priority: Any
    """Task priority"""
    task_theme: Any
    """Task theme"""
    task_type: Any
    """Task type"""
    template: Any
    """Template"""
    updated_at: Any
    """Updated at"""


class TasksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    account: str
    """Account"""
    action: str
    """Action"""
    autoskip_at: str
    """Autoskip at"""
    call: str
    """Call"""
    calls: str
    """Calls"""
    compiled_sequence_template_html: str
    """Compiled sequence template html"""
    completed: str
    """Completed"""
    completed_at: str
    """Completed at"""
    completer: str
    """Completer"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    default_plugin_mapping: str
    """Default plugin mapping"""
    due_at: str
    """Due at"""
    id: str
    """Unique task identifier"""
    mailing: str
    """Mailing"""
    mailings: str
    """Mailings"""
    note: str
    """Note"""
    opportunity: str
    """Opportunity"""
    opportunity_association: str
    """Opportunity association"""
    owner: str
    """Owner"""
    prospect: str
    """Prospect"""
    prospect_account: str
    """Prospect account"""
    prospect_contacts: str
    """Prospect contacts"""
    prospect_owner: str
    """Prospect owner"""
    prospect_phone_numbers: str
    """Prospect phone numbers"""
    prospect_stage: str
    """Prospect stage"""
    scheduled_at: str
    """Scheduled at"""
    sequence: str
    """Sequence"""
    sequence_sequence_steps: str
    """Sequence sequence steps"""
    sequence_state: str
    """Sequence state"""
    sequence_state_sequence_step: str
    """Sequence state sequence step"""
    sequence_state_sequence_step_overrides: str
    """Sequence state sequence step overrides"""
    sequence_state_starting_template: str
    """Sequence state starting template"""
    sequence_step: str
    """Sequence step"""
    sequence_step_override_templates: str
    """Sequence step override templates"""
    sequence_template: str
    """Sequence template"""
    sequence_template_template: str
    """Sequence template template"""
    state: str
    """State"""
    state_changed_at: str
    """State changed at"""
    subject: str
    """Subject"""
    task_priority: str
    """Task priority"""
    task_theme: str
    """Task theme"""
    task_type: str
    """Task type"""
    template: str
    """Template"""
    updated_at: str
    """Updated at"""


class TasksSortFilter(TypedDict, total=False):
    """Available fields for sorting tasks search results."""
    account: AirbyteSortOrder
    """Account"""
    action: AirbyteSortOrder
    """Action"""
    autoskip_at: AirbyteSortOrder
    """Autoskip at"""
    call: AirbyteSortOrder
    """Call"""
    calls: AirbyteSortOrder
    """Calls"""
    compiled_sequence_template_html: AirbyteSortOrder
    """Compiled sequence template html"""
    completed: AirbyteSortOrder
    """Completed"""
    completed_at: AirbyteSortOrder
    """Completed at"""
    completer: AirbyteSortOrder
    """Completer"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    default_plugin_mapping: AirbyteSortOrder
    """Default plugin mapping"""
    due_at: AirbyteSortOrder
    """Due at"""
    id: AirbyteSortOrder
    """Unique task identifier"""
    mailing: AirbyteSortOrder
    """Mailing"""
    mailings: AirbyteSortOrder
    """Mailings"""
    note: AirbyteSortOrder
    """Note"""
    opportunity: AirbyteSortOrder
    """Opportunity"""
    opportunity_association: AirbyteSortOrder
    """Opportunity association"""
    owner: AirbyteSortOrder
    """Owner"""
    prospect: AirbyteSortOrder
    """Prospect"""
    prospect_account: AirbyteSortOrder
    """Prospect account"""
    prospect_contacts: AirbyteSortOrder
    """Prospect contacts"""
    prospect_owner: AirbyteSortOrder
    """Prospect owner"""
    prospect_phone_numbers: AirbyteSortOrder
    """Prospect phone numbers"""
    prospect_stage: AirbyteSortOrder
    """Prospect stage"""
    scheduled_at: AirbyteSortOrder
    """Scheduled at"""
    sequence: AirbyteSortOrder
    """Sequence"""
    sequence_sequence_steps: AirbyteSortOrder
    """Sequence sequence steps"""
    sequence_state: AirbyteSortOrder
    """Sequence state"""
    sequence_state_sequence_step: AirbyteSortOrder
    """Sequence state sequence step"""
    sequence_state_sequence_step_overrides: AirbyteSortOrder
    """Sequence state sequence step overrides"""
    sequence_state_starting_template: AirbyteSortOrder
    """Sequence state starting template"""
    sequence_step: AirbyteSortOrder
    """Sequence step"""
    sequence_step_override_templates: AirbyteSortOrder
    """Sequence step override templates"""
    sequence_template: AirbyteSortOrder
    """Sequence template"""
    sequence_template_template: AirbyteSortOrder
    """Sequence template template"""
    state: AirbyteSortOrder
    """State"""
    state_changed_at: AirbyteSortOrder
    """State changed at"""
    subject: AirbyteSortOrder
    """Subject"""
    task_priority: AirbyteSortOrder
    """Task priority"""
    task_theme: AirbyteSortOrder
    """Task theme"""
    task_type: AirbyteSortOrder
    """Task type"""
    template: AirbyteSortOrder
    """Template"""
    updated_at: AirbyteSortOrder
    """Updated at"""


# Entity-specific condition types for tasks
class TasksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TasksSearchFilter


class TasksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TasksSearchFilter


class TasksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TasksSearchFilter


class TasksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TasksSearchFilter


class TasksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TasksSearchFilter


class TasksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TasksSearchFilter


class TasksStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TasksStringFilter


class TasksEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TasksStringFilter


class TasksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TasksStringFilter


class TasksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TasksStringFilter


class TasksContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: TasksAnyValueFilter


class TasksArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: TasksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TasksInCondition = TypedDict("TasksInCondition", {"in": TasksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TasksNotCondition = TypedDict("TasksNotCondition", {"not": "TasksCondition"}, total=False)
"""Negates the nested condition."""

TasksAndCondition = TypedDict("TasksAndCondition", {"and": "list[TasksCondition]"}, total=False)
"""True if all nested conditions are true."""

TasksOrCondition = TypedDict("TasksOrCondition", {"or": "list[TasksCondition]"}, total=False)
"""True if any nested condition is true."""

TasksAnyCondition = TypedDict("TasksAnyCondition", {"any": TasksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tasks condition types
TasksCondition = (
    TasksEqCondition
    | TasksNeqCondition
    | TasksGtCondition
    | TasksGteCondition
    | TasksLtCondition
    | TasksLteCondition
    | TasksInCondition
    | TasksStartswithCondition
    | TasksEndswithCondition
    | TasksFuzzyCondition
    | TasksKeywordCondition
    | TasksContainsCondition
    | TasksArrayContainsCondition
    | TasksNotCondition
    | TasksAndCondition
    | TasksOrCondition
    | TasksAnyCondition
)


class TasksSearchQuery(TypedDict, total=False):
    """Search query for tasks entity."""
    filter: TasksCondition
    sort: list[TasksSortFilter]


# ===== TEMPLATES SEARCH TYPES =====

class TemplatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering templates search queries."""
    archived: bool | None
    """Archived"""
    archived_at: str | None
    """Archived at"""
    bcc_recipients: str | None
    """Bcc recipients"""
    body_html: str | None
    """Body html"""
    body_text: str | None
    """Body text"""
    bounce_count: int | None
    """Bounce count"""
    cc_recipients: str | None
    """Cc recipients"""
    click_count: int | None
    """Click count"""
    content_category_memberships: list[Any] | None
    """Content category memberships"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    deliver_count: int | None
    """Deliver count"""
    failure_count: int | None
    """Failure count"""
    id: int | None
    """Unique template identifier"""
    last_used_at: str | None
    """Last used at"""
    name: str | None
    """Name"""
    negative_reply_count: int | None
    """Negative reply count"""
    neutral_reply_count: int | None
    """Neutral reply count"""
    open_count: int | None
    """Open count"""
    opt_out_count: int | None
    """Opt out count"""
    owner: list[Any] | None
    """Owner"""
    positive_reply_count: int | None
    """Positive reply count"""
    recipients: list[Any] | None
    """Recipients"""
    reply_count: int | None
    """Reply count"""
    schedule_count: int | None
    """Schedule count"""
    sequence_templates: list[Any] | None
    """Sequence templates"""
    share_type: str | None
    """Share type"""
    subject: str | None
    """Subject"""
    tags: str | None
    """Tags"""
    to_recipients: str | None
    """To recipients"""
    track_links: bool | None
    """Track links"""
    track_opens: bool | None
    """Track opens"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""


class TemplatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Archived"""
    archived_at: list[str]
    """Archived at"""
    bcc_recipients: list[str]
    """Bcc recipients"""
    body_html: list[str]
    """Body html"""
    body_text: list[str]
    """Body text"""
    bounce_count: list[int]
    """Bounce count"""
    cc_recipients: list[str]
    """Cc recipients"""
    click_count: list[int]
    """Click count"""
    content_category_memberships: list[list[Any]]
    """Content category memberships"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    deliver_count: list[int]
    """Deliver count"""
    failure_count: list[int]
    """Failure count"""
    id: list[int]
    """Unique template identifier"""
    last_used_at: list[str]
    """Last used at"""
    name: list[str]
    """Name"""
    negative_reply_count: list[int]
    """Negative reply count"""
    neutral_reply_count: list[int]
    """Neutral reply count"""
    open_count: list[int]
    """Open count"""
    opt_out_count: list[int]
    """Opt out count"""
    owner: list[list[Any]]
    """Owner"""
    positive_reply_count: list[int]
    """Positive reply count"""
    recipients: list[list[Any]]
    """Recipients"""
    reply_count: list[int]
    """Reply count"""
    schedule_count: list[int]
    """Schedule count"""
    sequence_templates: list[list[Any]]
    """Sequence templates"""
    share_type: list[str]
    """Share type"""
    subject: list[str]
    """Subject"""
    tags: list[str]
    """Tags"""
    to_recipients: list[str]
    """To recipients"""
    track_links: list[bool]
    """Track links"""
    track_opens: list[bool]
    """Track opens"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""


class TemplatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Archived"""
    archived_at: Any
    """Archived at"""
    bcc_recipients: Any
    """Bcc recipients"""
    body_html: Any
    """Body html"""
    body_text: Any
    """Body text"""
    bounce_count: Any
    """Bounce count"""
    cc_recipients: Any
    """Cc recipients"""
    click_count: Any
    """Click count"""
    content_category_memberships: Any
    """Content category memberships"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    deliver_count: Any
    """Deliver count"""
    failure_count: Any
    """Failure count"""
    id: Any
    """Unique template identifier"""
    last_used_at: Any
    """Last used at"""
    name: Any
    """Name"""
    negative_reply_count: Any
    """Negative reply count"""
    neutral_reply_count: Any
    """Neutral reply count"""
    open_count: Any
    """Open count"""
    opt_out_count: Any
    """Opt out count"""
    owner: Any
    """Owner"""
    positive_reply_count: Any
    """Positive reply count"""
    recipients: Any
    """Recipients"""
    reply_count: Any
    """Reply count"""
    schedule_count: Any
    """Schedule count"""
    sequence_templates: Any
    """Sequence templates"""
    share_type: Any
    """Share type"""
    subject: Any
    """Subject"""
    tags: Any
    """Tags"""
    to_recipients: Any
    """To recipients"""
    track_links: Any
    """Track links"""
    track_opens: Any
    """Track opens"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""


class TemplatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    archived: str
    """Archived"""
    archived_at: str
    """Archived at"""
    bcc_recipients: str
    """Bcc recipients"""
    body_html: str
    """Body html"""
    body_text: str
    """Body text"""
    bounce_count: str
    """Bounce count"""
    cc_recipients: str
    """Cc recipients"""
    click_count: str
    """Click count"""
    content_category_memberships: str
    """Content category memberships"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    deliver_count: str
    """Deliver count"""
    failure_count: str
    """Failure count"""
    id: str
    """Unique template identifier"""
    last_used_at: str
    """Last used at"""
    name: str
    """Name"""
    negative_reply_count: str
    """Negative reply count"""
    neutral_reply_count: str
    """Neutral reply count"""
    open_count: str
    """Open count"""
    opt_out_count: str
    """Opt out count"""
    owner: str
    """Owner"""
    positive_reply_count: str
    """Positive reply count"""
    recipients: str
    """Recipients"""
    reply_count: str
    """Reply count"""
    schedule_count: str
    """Schedule count"""
    sequence_templates: str
    """Sequence templates"""
    share_type: str
    """Share type"""
    subject: str
    """Subject"""
    tags: str
    """Tags"""
    to_recipients: str
    """To recipients"""
    track_links: str
    """Track links"""
    track_opens: str
    """Track opens"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""


class TemplatesSortFilter(TypedDict, total=False):
    """Available fields for sorting templates search results."""
    archived: AirbyteSortOrder
    """Archived"""
    archived_at: AirbyteSortOrder
    """Archived at"""
    bcc_recipients: AirbyteSortOrder
    """Bcc recipients"""
    body_html: AirbyteSortOrder
    """Body html"""
    body_text: AirbyteSortOrder
    """Body text"""
    bounce_count: AirbyteSortOrder
    """Bounce count"""
    cc_recipients: AirbyteSortOrder
    """Cc recipients"""
    click_count: AirbyteSortOrder
    """Click count"""
    content_category_memberships: AirbyteSortOrder
    """Content category memberships"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    deliver_count: AirbyteSortOrder
    """Deliver count"""
    failure_count: AirbyteSortOrder
    """Failure count"""
    id: AirbyteSortOrder
    """Unique template identifier"""
    last_used_at: AirbyteSortOrder
    """Last used at"""
    name: AirbyteSortOrder
    """Name"""
    negative_reply_count: AirbyteSortOrder
    """Negative reply count"""
    neutral_reply_count: AirbyteSortOrder
    """Neutral reply count"""
    open_count: AirbyteSortOrder
    """Open count"""
    opt_out_count: AirbyteSortOrder
    """Opt out count"""
    owner: AirbyteSortOrder
    """Owner"""
    positive_reply_count: AirbyteSortOrder
    """Positive reply count"""
    recipients: AirbyteSortOrder
    """Recipients"""
    reply_count: AirbyteSortOrder
    """Reply count"""
    schedule_count: AirbyteSortOrder
    """Schedule count"""
    sequence_templates: AirbyteSortOrder
    """Sequence templates"""
    share_type: AirbyteSortOrder
    """Share type"""
    subject: AirbyteSortOrder
    """Subject"""
    tags: AirbyteSortOrder
    """Tags"""
    to_recipients: AirbyteSortOrder
    """To recipients"""
    track_links: AirbyteSortOrder
    """Track links"""
    track_opens: AirbyteSortOrder
    """Track opens"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""


# Entity-specific condition types for templates
class TemplatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TemplatesSearchFilter


class TemplatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TemplatesSearchFilter


class TemplatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TemplatesSearchFilter


class TemplatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TemplatesSearchFilter


class TemplatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TemplatesSearchFilter


class TemplatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TemplatesSearchFilter


class TemplatesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TemplatesStringFilter


class TemplatesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TemplatesStringFilter


class TemplatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TemplatesStringFilter


class TemplatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TemplatesStringFilter


class TemplatesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: TemplatesAnyValueFilter


class TemplatesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: TemplatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TemplatesInCondition = TypedDict("TemplatesInCondition", {"in": TemplatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TemplatesNotCondition = TypedDict("TemplatesNotCondition", {"not": "TemplatesCondition"}, total=False)
"""Negates the nested condition."""

TemplatesAndCondition = TypedDict("TemplatesAndCondition", {"and": "list[TemplatesCondition]"}, total=False)
"""True if all nested conditions are true."""

TemplatesOrCondition = TypedDict("TemplatesOrCondition", {"or": "list[TemplatesCondition]"}, total=False)
"""True if any nested condition is true."""

TemplatesAnyCondition = TypedDict("TemplatesAnyCondition", {"any": TemplatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all templates condition types
TemplatesCondition = (
    TemplatesEqCondition
    | TemplatesNeqCondition
    | TemplatesGtCondition
    | TemplatesGteCondition
    | TemplatesLtCondition
    | TemplatesLteCondition
    | TemplatesInCondition
    | TemplatesStartswithCondition
    | TemplatesEndswithCondition
    | TemplatesFuzzyCondition
    | TemplatesKeywordCondition
    | TemplatesContainsCondition
    | TemplatesArrayContainsCondition
    | TemplatesNotCondition
    | TemplatesAndCondition
    | TemplatesOrCondition
    | TemplatesAnyCondition
)


class TemplatesSearchQuery(TypedDict, total=False):
    """Search query for templates entity."""
    filter: TemplatesCondition
    sort: list[TemplatesSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    accounts_view_id: int | None
    """Accounts view id"""
    active_prospects_count: int | None
    """Active prospects count"""
    activity_notifications_disabled: bool | None
    """Activity notifications disabled"""
    batches: list[Any] | None
    """Batches"""
    batches_view_id: int | None
    """Batches view id"""
    bounce_warning_email_enabled: bool | None
    """Bounce warning email enabled"""
    bridge_phone: str | None
    """Bridge phone"""
    bridge_phone_extension: str | None
    """Bridge phone extension"""
    buyer_language_preference: str | None
    """Buyer language preference"""
    calendar: list[Any] | None
    """Calendar"""
    calendar_events_view_id: int | None
    """Calendar events view id"""
    calls_view_id: int | None
    """Calls view id"""
    content_categories: list[Any] | None
    """Content categories"""
    content_category_ownerships: list[Any] | None
    """Content category ownerships"""
    controlled_tab_default: str | None
    """Controlled tab default"""
    created_at: str | None
    """Created at"""
    creator: list[Any] | None
    """Creator"""
    current_sign_in_at: str | None
    """Current sign in at"""
    custom1: str | None
    """Custom field 1"""
    custom2: str | None
    """Custom field 2"""
    custom3: str | None
    """Custom field 3"""
    custom4: str | None
    """Custom field 4"""
    custom5: str | None
    """Custom field 5"""
    daily_digest_email_enabled: bool | None
    """Daily digest email enabled"""
    default_ruleset_id: int | None
    """Default ruleset id"""
    default_schedule_id: int | None
    """Default schedule id"""
    duties: list[Any] | None
    """Duties"""
    duties_set_at: str | None
    """Duties set at"""
    email: str | None
    """Email"""
    enable_voice_recordings: bool | None
    """Enable voice recordings"""
    engagement_emails_enabled: bool | None
    """Engagement emails enabled"""
    favorites: list[Any] | None
    """Favorites"""
    first_name: str | None
    """First name"""
    global_id: str | None
    """Global id"""
    id: int | None
    """Unique user identifier"""
    imports_view_id: int | None
    """Imports view id"""
    inbound_bridge_phone: str | None
    """Inbound bridge phone"""
    inbound_bridge_phone_extension: str | None
    """Inbound bridge phone extension"""
    inbound_call_behavior: str | None
    """Inbound call behavior"""
    inbound_phone_type: str | None
    """Inbound phone type"""
    inbound_voicemail_custom_message_text: str | None
    """Inbound voicemail custom message text"""
    inbound_voicemail_message_text_voice: str | None
    """Inbound voicemail message text voice"""
    inbound_voicemail_prompt_type: str | None
    """Inbound voicemail prompt type"""
    job_role: list[Any] | None
    """Job role"""
    kaia_recordings_view_id: int | None
    """Kaia recordings view id"""
    keep_bridge_phone_connected: bool | None
    """Keep bridge phone connected"""
    language_preference: str | None
    """Language preference"""
    last_name: str | None
    """Last name"""
    last_sign_in_at: str | None
    """Last sign in at"""
    link_to_sequence_state_in_task_flow: bool | None
    """Link to sequence state in task flow"""
    live_listen_view_id: int | None
    """Live listen view id"""
    locked: bool | None
    """Locked"""
    mailbox: list[Any] | None
    """Mailbox"""
    mailbox_error_email_enabled: bool | None
    """Mailbox error email enabled"""
    mailboxes: list[Any] | None
    """Mailboxes"""
    mailings_delivered_count: int | None
    """Mailings delivered count"""
    mailings_replied_count: int | None
    """Mailings replied count"""
    mailings_view_id: int | None
    """Mailings view id"""
    meeting_engagement_notification_enabled: bool | None
    """Meeting engagement notification enabled"""
    meeting_types_view_id: int | None
    """Meeting types view id"""
    name: str | None
    """Name"""
    notifications_enabled: bool | None
    """Notifications enabled"""
    oce_click_to_dial_everywhere: bool | None
    """Oce click to dial everywhere"""
    oce_gmail_toolbar: bool | None
    """Oce gmail toolbar"""
    oce_gmail_tracking_state: str | None
    """Oce gmail tracking state"""
    oce_salesforce_email_decorating: bool | None
    """Oce salesforce email decorating"""
    oce_salesforce_phone_decorating: bool | None
    """Oce salesforce phone decorating"""
    oce_universal_task_flow: bool | None
    """Oce universal task flow"""
    oce_window_mode: bool | None
    """Oce window mode"""
    onboarded_at: str | None
    """Onboarded at"""
    opportunities_view_id: int | None
    """Opportunities view id"""
    orca_standalone_enabled: bool | None
    """Orca standalone enabled"""
    outbound_voicemails: list[Any] | None
    """Outbound voicemails"""
    password_expires_at: str | None
    """Password expires at"""
    phone: list[Any] | None
    """Phone"""
    phone_country_code: str | None
    """Phone country code"""
    phone_number: str | None
    """Phone number"""
    phone_type: str | None
    """Phone type"""
    phones: list[Any] | None
    """Phones"""
    phones_view_id: int | None
    """Phones view id"""
    plugin_alert_notification_enabled: bool | None
    """Plugin alert notification enabled"""
    preferred_voice_region: str | None
    """Preferred voice region"""
    prefers_local_presence: bool | None
    """Prefers local presence"""
    primary_timezone: str | None
    """Primary timezone"""
    profile: list[Any] | None
    """Profile"""
    prospect_detail_default: str | None
    """Prospect detail default"""
    prospects_view_id: int | None
    """Prospects view id"""
    recipients: list[Any] | None
    """Recipients"""
    reports_sequence_performance_view_id: int | None
    """Reports sequence performance view id"""
    reports_team_perf_view_id: int | None
    """Reports team perf view id"""
    reports_team_performance_intraday_view_id: int | None
    """Reports team performance intraday view id"""
    reports_team_performance_view_id: int | None
    """Reports team performance view id"""
    reports_view_id: int | None
    """Reports view id"""
    role: list[Any] | None
    """Role"""
    scim_external_id: str | None
    """Scim external id"""
    scim_source: str | None
    """Scim source"""
    secondary_timezone: str | None
    """Secondary timezone"""
    send_invite_fallback: bool | None
    """Send invite fallback"""
    sender_notifications_excluded: bool | None
    """Sender notifications excluded"""
    sequence_states_view_id: int | None
    """Sequence states view id"""
    sequences_view_id: int | None
    """Sequences view id"""
    sms_phone: list[Any] | None
    """Sms phone"""
    snippets_view_id: int | None
    """Snippets view id"""
    tasks_due_count: int | None
    """Tasks due count"""
    tasks_view_id: int | None
    """Tasks view id"""
    teams: list[Any] | None
    """Teams"""
    teams_view_id: int | None
    """Teams view id"""
    templates_view_id: int | None
    """Templates view id"""
    tertiary_timezone: str | None
    """Tertiary timezone"""
    texting_email_notifications: bool | None
    """Texting email notifications"""
    title: str | None
    """Title"""
    unknown_reply_email_enabled: bool | None
    """Unknown reply email enabled"""
    updated_at: str | None
    """Updated at"""
    updater: list[Any] | None
    """Updater"""
    use_sales_navigator_for_linked_in_tasks: bool | None
    """Use sales navigator for linked in tasks"""
    user_guid: str | None
    """User guid"""
    username: str | None
    """Username"""
    users_view_id: int | None
    """Users view id"""
    voicemail_notification_enabled: bool | None
    """Voicemail notification enabled"""
    voicemail_prompts: list[Any] | None
    """Voicemail prompts"""
    weekly_digest_email_enabled: bool | None
    """Weekly digest email enabled"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    accounts_view_id: list[int]
    """Accounts view id"""
    active_prospects_count: list[int]
    """Active prospects count"""
    activity_notifications_disabled: list[bool]
    """Activity notifications disabled"""
    batches: list[list[Any]]
    """Batches"""
    batches_view_id: list[int]
    """Batches view id"""
    bounce_warning_email_enabled: list[bool]
    """Bounce warning email enabled"""
    bridge_phone: list[str]
    """Bridge phone"""
    bridge_phone_extension: list[str]
    """Bridge phone extension"""
    buyer_language_preference: list[str]
    """Buyer language preference"""
    calendar: list[list[Any]]
    """Calendar"""
    calendar_events_view_id: list[int]
    """Calendar events view id"""
    calls_view_id: list[int]
    """Calls view id"""
    content_categories: list[list[Any]]
    """Content categories"""
    content_category_ownerships: list[list[Any]]
    """Content category ownerships"""
    controlled_tab_default: list[str]
    """Controlled tab default"""
    created_at: list[str]
    """Created at"""
    creator: list[list[Any]]
    """Creator"""
    current_sign_in_at: list[str]
    """Current sign in at"""
    custom1: list[str]
    """Custom field 1"""
    custom2: list[str]
    """Custom field 2"""
    custom3: list[str]
    """Custom field 3"""
    custom4: list[str]
    """Custom field 4"""
    custom5: list[str]
    """Custom field 5"""
    daily_digest_email_enabled: list[bool]
    """Daily digest email enabled"""
    default_ruleset_id: list[int]
    """Default ruleset id"""
    default_schedule_id: list[int]
    """Default schedule id"""
    duties: list[list[Any]]
    """Duties"""
    duties_set_at: list[str]
    """Duties set at"""
    email: list[str]
    """Email"""
    enable_voice_recordings: list[bool]
    """Enable voice recordings"""
    engagement_emails_enabled: list[bool]
    """Engagement emails enabled"""
    favorites: list[list[Any]]
    """Favorites"""
    first_name: list[str]
    """First name"""
    global_id: list[str]
    """Global id"""
    id: list[int]
    """Unique user identifier"""
    imports_view_id: list[int]
    """Imports view id"""
    inbound_bridge_phone: list[str]
    """Inbound bridge phone"""
    inbound_bridge_phone_extension: list[str]
    """Inbound bridge phone extension"""
    inbound_call_behavior: list[str]
    """Inbound call behavior"""
    inbound_phone_type: list[str]
    """Inbound phone type"""
    inbound_voicemail_custom_message_text: list[str]
    """Inbound voicemail custom message text"""
    inbound_voicemail_message_text_voice: list[str]
    """Inbound voicemail message text voice"""
    inbound_voicemail_prompt_type: list[str]
    """Inbound voicemail prompt type"""
    job_role: list[list[Any]]
    """Job role"""
    kaia_recordings_view_id: list[int]
    """Kaia recordings view id"""
    keep_bridge_phone_connected: list[bool]
    """Keep bridge phone connected"""
    language_preference: list[str]
    """Language preference"""
    last_name: list[str]
    """Last name"""
    last_sign_in_at: list[str]
    """Last sign in at"""
    link_to_sequence_state_in_task_flow: list[bool]
    """Link to sequence state in task flow"""
    live_listen_view_id: list[int]
    """Live listen view id"""
    locked: list[bool]
    """Locked"""
    mailbox: list[list[Any]]
    """Mailbox"""
    mailbox_error_email_enabled: list[bool]
    """Mailbox error email enabled"""
    mailboxes: list[list[Any]]
    """Mailboxes"""
    mailings_delivered_count: list[int]
    """Mailings delivered count"""
    mailings_replied_count: list[int]
    """Mailings replied count"""
    mailings_view_id: list[int]
    """Mailings view id"""
    meeting_engagement_notification_enabled: list[bool]
    """Meeting engagement notification enabled"""
    meeting_types_view_id: list[int]
    """Meeting types view id"""
    name: list[str]
    """Name"""
    notifications_enabled: list[bool]
    """Notifications enabled"""
    oce_click_to_dial_everywhere: list[bool]
    """Oce click to dial everywhere"""
    oce_gmail_toolbar: list[bool]
    """Oce gmail toolbar"""
    oce_gmail_tracking_state: list[str]
    """Oce gmail tracking state"""
    oce_salesforce_email_decorating: list[bool]
    """Oce salesforce email decorating"""
    oce_salesforce_phone_decorating: list[bool]
    """Oce salesforce phone decorating"""
    oce_universal_task_flow: list[bool]
    """Oce universal task flow"""
    oce_window_mode: list[bool]
    """Oce window mode"""
    onboarded_at: list[str]
    """Onboarded at"""
    opportunities_view_id: list[int]
    """Opportunities view id"""
    orca_standalone_enabled: list[bool]
    """Orca standalone enabled"""
    outbound_voicemails: list[list[Any]]
    """Outbound voicemails"""
    password_expires_at: list[str]
    """Password expires at"""
    phone: list[list[Any]]
    """Phone"""
    phone_country_code: list[str]
    """Phone country code"""
    phone_number: list[str]
    """Phone number"""
    phone_type: list[str]
    """Phone type"""
    phones: list[list[Any]]
    """Phones"""
    phones_view_id: list[int]
    """Phones view id"""
    plugin_alert_notification_enabled: list[bool]
    """Plugin alert notification enabled"""
    preferred_voice_region: list[str]
    """Preferred voice region"""
    prefers_local_presence: list[bool]
    """Prefers local presence"""
    primary_timezone: list[str]
    """Primary timezone"""
    profile: list[list[Any]]
    """Profile"""
    prospect_detail_default: list[str]
    """Prospect detail default"""
    prospects_view_id: list[int]
    """Prospects view id"""
    recipients: list[list[Any]]
    """Recipients"""
    reports_sequence_performance_view_id: list[int]
    """Reports sequence performance view id"""
    reports_team_perf_view_id: list[int]
    """Reports team perf view id"""
    reports_team_performance_intraday_view_id: list[int]
    """Reports team performance intraday view id"""
    reports_team_performance_view_id: list[int]
    """Reports team performance view id"""
    reports_view_id: list[int]
    """Reports view id"""
    role: list[list[Any]]
    """Role"""
    scim_external_id: list[str]
    """Scim external id"""
    scim_source: list[str]
    """Scim source"""
    secondary_timezone: list[str]
    """Secondary timezone"""
    send_invite_fallback: list[bool]
    """Send invite fallback"""
    sender_notifications_excluded: list[bool]
    """Sender notifications excluded"""
    sequence_states_view_id: list[int]
    """Sequence states view id"""
    sequences_view_id: list[int]
    """Sequences view id"""
    sms_phone: list[list[Any]]
    """Sms phone"""
    snippets_view_id: list[int]
    """Snippets view id"""
    tasks_due_count: list[int]
    """Tasks due count"""
    tasks_view_id: list[int]
    """Tasks view id"""
    teams: list[list[Any]]
    """Teams"""
    teams_view_id: list[int]
    """Teams view id"""
    templates_view_id: list[int]
    """Templates view id"""
    tertiary_timezone: list[str]
    """Tertiary timezone"""
    texting_email_notifications: list[bool]
    """Texting email notifications"""
    title: list[str]
    """Title"""
    unknown_reply_email_enabled: list[bool]
    """Unknown reply email enabled"""
    updated_at: list[str]
    """Updated at"""
    updater: list[list[Any]]
    """Updater"""
    use_sales_navigator_for_linked_in_tasks: list[bool]
    """Use sales navigator for linked in tasks"""
    user_guid: list[str]
    """User guid"""
    username: list[str]
    """Username"""
    users_view_id: list[int]
    """Users view id"""
    voicemail_notification_enabled: list[bool]
    """Voicemail notification enabled"""
    voicemail_prompts: list[list[Any]]
    """Voicemail prompts"""
    weekly_digest_email_enabled: list[bool]
    """Weekly digest email enabled"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    accounts_view_id: Any
    """Accounts view id"""
    active_prospects_count: Any
    """Active prospects count"""
    activity_notifications_disabled: Any
    """Activity notifications disabled"""
    batches: Any
    """Batches"""
    batches_view_id: Any
    """Batches view id"""
    bounce_warning_email_enabled: Any
    """Bounce warning email enabled"""
    bridge_phone: Any
    """Bridge phone"""
    bridge_phone_extension: Any
    """Bridge phone extension"""
    buyer_language_preference: Any
    """Buyer language preference"""
    calendar: Any
    """Calendar"""
    calendar_events_view_id: Any
    """Calendar events view id"""
    calls_view_id: Any
    """Calls view id"""
    content_categories: Any
    """Content categories"""
    content_category_ownerships: Any
    """Content category ownerships"""
    controlled_tab_default: Any
    """Controlled tab default"""
    created_at: Any
    """Created at"""
    creator: Any
    """Creator"""
    current_sign_in_at: Any
    """Current sign in at"""
    custom1: Any
    """Custom field 1"""
    custom2: Any
    """Custom field 2"""
    custom3: Any
    """Custom field 3"""
    custom4: Any
    """Custom field 4"""
    custom5: Any
    """Custom field 5"""
    daily_digest_email_enabled: Any
    """Daily digest email enabled"""
    default_ruleset_id: Any
    """Default ruleset id"""
    default_schedule_id: Any
    """Default schedule id"""
    duties: Any
    """Duties"""
    duties_set_at: Any
    """Duties set at"""
    email: Any
    """Email"""
    enable_voice_recordings: Any
    """Enable voice recordings"""
    engagement_emails_enabled: Any
    """Engagement emails enabled"""
    favorites: Any
    """Favorites"""
    first_name: Any
    """First name"""
    global_id: Any
    """Global id"""
    id: Any
    """Unique user identifier"""
    imports_view_id: Any
    """Imports view id"""
    inbound_bridge_phone: Any
    """Inbound bridge phone"""
    inbound_bridge_phone_extension: Any
    """Inbound bridge phone extension"""
    inbound_call_behavior: Any
    """Inbound call behavior"""
    inbound_phone_type: Any
    """Inbound phone type"""
    inbound_voicemail_custom_message_text: Any
    """Inbound voicemail custom message text"""
    inbound_voicemail_message_text_voice: Any
    """Inbound voicemail message text voice"""
    inbound_voicemail_prompt_type: Any
    """Inbound voicemail prompt type"""
    job_role: Any
    """Job role"""
    kaia_recordings_view_id: Any
    """Kaia recordings view id"""
    keep_bridge_phone_connected: Any
    """Keep bridge phone connected"""
    language_preference: Any
    """Language preference"""
    last_name: Any
    """Last name"""
    last_sign_in_at: Any
    """Last sign in at"""
    link_to_sequence_state_in_task_flow: Any
    """Link to sequence state in task flow"""
    live_listen_view_id: Any
    """Live listen view id"""
    locked: Any
    """Locked"""
    mailbox: Any
    """Mailbox"""
    mailbox_error_email_enabled: Any
    """Mailbox error email enabled"""
    mailboxes: Any
    """Mailboxes"""
    mailings_delivered_count: Any
    """Mailings delivered count"""
    mailings_replied_count: Any
    """Mailings replied count"""
    mailings_view_id: Any
    """Mailings view id"""
    meeting_engagement_notification_enabled: Any
    """Meeting engagement notification enabled"""
    meeting_types_view_id: Any
    """Meeting types view id"""
    name: Any
    """Name"""
    notifications_enabled: Any
    """Notifications enabled"""
    oce_click_to_dial_everywhere: Any
    """Oce click to dial everywhere"""
    oce_gmail_toolbar: Any
    """Oce gmail toolbar"""
    oce_gmail_tracking_state: Any
    """Oce gmail tracking state"""
    oce_salesforce_email_decorating: Any
    """Oce salesforce email decorating"""
    oce_salesforce_phone_decorating: Any
    """Oce salesforce phone decorating"""
    oce_universal_task_flow: Any
    """Oce universal task flow"""
    oce_window_mode: Any
    """Oce window mode"""
    onboarded_at: Any
    """Onboarded at"""
    opportunities_view_id: Any
    """Opportunities view id"""
    orca_standalone_enabled: Any
    """Orca standalone enabled"""
    outbound_voicemails: Any
    """Outbound voicemails"""
    password_expires_at: Any
    """Password expires at"""
    phone: Any
    """Phone"""
    phone_country_code: Any
    """Phone country code"""
    phone_number: Any
    """Phone number"""
    phone_type: Any
    """Phone type"""
    phones: Any
    """Phones"""
    phones_view_id: Any
    """Phones view id"""
    plugin_alert_notification_enabled: Any
    """Plugin alert notification enabled"""
    preferred_voice_region: Any
    """Preferred voice region"""
    prefers_local_presence: Any
    """Prefers local presence"""
    primary_timezone: Any
    """Primary timezone"""
    profile: Any
    """Profile"""
    prospect_detail_default: Any
    """Prospect detail default"""
    prospects_view_id: Any
    """Prospects view id"""
    recipients: Any
    """Recipients"""
    reports_sequence_performance_view_id: Any
    """Reports sequence performance view id"""
    reports_team_perf_view_id: Any
    """Reports team perf view id"""
    reports_team_performance_intraday_view_id: Any
    """Reports team performance intraday view id"""
    reports_team_performance_view_id: Any
    """Reports team performance view id"""
    reports_view_id: Any
    """Reports view id"""
    role: Any
    """Role"""
    scim_external_id: Any
    """Scim external id"""
    scim_source: Any
    """Scim source"""
    secondary_timezone: Any
    """Secondary timezone"""
    send_invite_fallback: Any
    """Send invite fallback"""
    sender_notifications_excluded: Any
    """Sender notifications excluded"""
    sequence_states_view_id: Any
    """Sequence states view id"""
    sequences_view_id: Any
    """Sequences view id"""
    sms_phone: Any
    """Sms phone"""
    snippets_view_id: Any
    """Snippets view id"""
    tasks_due_count: Any
    """Tasks due count"""
    tasks_view_id: Any
    """Tasks view id"""
    teams: Any
    """Teams"""
    teams_view_id: Any
    """Teams view id"""
    templates_view_id: Any
    """Templates view id"""
    tertiary_timezone: Any
    """Tertiary timezone"""
    texting_email_notifications: Any
    """Texting email notifications"""
    title: Any
    """Title"""
    unknown_reply_email_enabled: Any
    """Unknown reply email enabled"""
    updated_at: Any
    """Updated at"""
    updater: Any
    """Updater"""
    use_sales_navigator_for_linked_in_tasks: Any
    """Use sales navigator for linked in tasks"""
    user_guid: Any
    """User guid"""
    username: Any
    """Username"""
    users_view_id: Any
    """Users view id"""
    voicemail_notification_enabled: Any
    """Voicemail notification enabled"""
    voicemail_prompts: Any
    """Voicemail prompts"""
    weekly_digest_email_enabled: Any
    """Weekly digest email enabled"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    accounts_view_id: str
    """Accounts view id"""
    active_prospects_count: str
    """Active prospects count"""
    activity_notifications_disabled: str
    """Activity notifications disabled"""
    batches: str
    """Batches"""
    batches_view_id: str
    """Batches view id"""
    bounce_warning_email_enabled: str
    """Bounce warning email enabled"""
    bridge_phone: str
    """Bridge phone"""
    bridge_phone_extension: str
    """Bridge phone extension"""
    buyer_language_preference: str
    """Buyer language preference"""
    calendar: str
    """Calendar"""
    calendar_events_view_id: str
    """Calendar events view id"""
    calls_view_id: str
    """Calls view id"""
    content_categories: str
    """Content categories"""
    content_category_ownerships: str
    """Content category ownerships"""
    controlled_tab_default: str
    """Controlled tab default"""
    created_at: str
    """Created at"""
    creator: str
    """Creator"""
    current_sign_in_at: str
    """Current sign in at"""
    custom1: str
    """Custom field 1"""
    custom2: str
    """Custom field 2"""
    custom3: str
    """Custom field 3"""
    custom4: str
    """Custom field 4"""
    custom5: str
    """Custom field 5"""
    daily_digest_email_enabled: str
    """Daily digest email enabled"""
    default_ruleset_id: str
    """Default ruleset id"""
    default_schedule_id: str
    """Default schedule id"""
    duties: str
    """Duties"""
    duties_set_at: str
    """Duties set at"""
    email: str
    """Email"""
    enable_voice_recordings: str
    """Enable voice recordings"""
    engagement_emails_enabled: str
    """Engagement emails enabled"""
    favorites: str
    """Favorites"""
    first_name: str
    """First name"""
    global_id: str
    """Global id"""
    id: str
    """Unique user identifier"""
    imports_view_id: str
    """Imports view id"""
    inbound_bridge_phone: str
    """Inbound bridge phone"""
    inbound_bridge_phone_extension: str
    """Inbound bridge phone extension"""
    inbound_call_behavior: str
    """Inbound call behavior"""
    inbound_phone_type: str
    """Inbound phone type"""
    inbound_voicemail_custom_message_text: str
    """Inbound voicemail custom message text"""
    inbound_voicemail_message_text_voice: str
    """Inbound voicemail message text voice"""
    inbound_voicemail_prompt_type: str
    """Inbound voicemail prompt type"""
    job_role: str
    """Job role"""
    kaia_recordings_view_id: str
    """Kaia recordings view id"""
    keep_bridge_phone_connected: str
    """Keep bridge phone connected"""
    language_preference: str
    """Language preference"""
    last_name: str
    """Last name"""
    last_sign_in_at: str
    """Last sign in at"""
    link_to_sequence_state_in_task_flow: str
    """Link to sequence state in task flow"""
    live_listen_view_id: str
    """Live listen view id"""
    locked: str
    """Locked"""
    mailbox: str
    """Mailbox"""
    mailbox_error_email_enabled: str
    """Mailbox error email enabled"""
    mailboxes: str
    """Mailboxes"""
    mailings_delivered_count: str
    """Mailings delivered count"""
    mailings_replied_count: str
    """Mailings replied count"""
    mailings_view_id: str
    """Mailings view id"""
    meeting_engagement_notification_enabled: str
    """Meeting engagement notification enabled"""
    meeting_types_view_id: str
    """Meeting types view id"""
    name: str
    """Name"""
    notifications_enabled: str
    """Notifications enabled"""
    oce_click_to_dial_everywhere: str
    """Oce click to dial everywhere"""
    oce_gmail_toolbar: str
    """Oce gmail toolbar"""
    oce_gmail_tracking_state: str
    """Oce gmail tracking state"""
    oce_salesforce_email_decorating: str
    """Oce salesforce email decorating"""
    oce_salesforce_phone_decorating: str
    """Oce salesforce phone decorating"""
    oce_universal_task_flow: str
    """Oce universal task flow"""
    oce_window_mode: str
    """Oce window mode"""
    onboarded_at: str
    """Onboarded at"""
    opportunities_view_id: str
    """Opportunities view id"""
    orca_standalone_enabled: str
    """Orca standalone enabled"""
    outbound_voicemails: str
    """Outbound voicemails"""
    password_expires_at: str
    """Password expires at"""
    phone: str
    """Phone"""
    phone_country_code: str
    """Phone country code"""
    phone_number: str
    """Phone number"""
    phone_type: str
    """Phone type"""
    phones: str
    """Phones"""
    phones_view_id: str
    """Phones view id"""
    plugin_alert_notification_enabled: str
    """Plugin alert notification enabled"""
    preferred_voice_region: str
    """Preferred voice region"""
    prefers_local_presence: str
    """Prefers local presence"""
    primary_timezone: str
    """Primary timezone"""
    profile: str
    """Profile"""
    prospect_detail_default: str
    """Prospect detail default"""
    prospects_view_id: str
    """Prospects view id"""
    recipients: str
    """Recipients"""
    reports_sequence_performance_view_id: str
    """Reports sequence performance view id"""
    reports_team_perf_view_id: str
    """Reports team perf view id"""
    reports_team_performance_intraday_view_id: str
    """Reports team performance intraday view id"""
    reports_team_performance_view_id: str
    """Reports team performance view id"""
    reports_view_id: str
    """Reports view id"""
    role: str
    """Role"""
    scim_external_id: str
    """Scim external id"""
    scim_source: str
    """Scim source"""
    secondary_timezone: str
    """Secondary timezone"""
    send_invite_fallback: str
    """Send invite fallback"""
    sender_notifications_excluded: str
    """Sender notifications excluded"""
    sequence_states_view_id: str
    """Sequence states view id"""
    sequences_view_id: str
    """Sequences view id"""
    sms_phone: str
    """Sms phone"""
    snippets_view_id: str
    """Snippets view id"""
    tasks_due_count: str
    """Tasks due count"""
    tasks_view_id: str
    """Tasks view id"""
    teams: str
    """Teams"""
    teams_view_id: str
    """Teams view id"""
    templates_view_id: str
    """Templates view id"""
    tertiary_timezone: str
    """Tertiary timezone"""
    texting_email_notifications: str
    """Texting email notifications"""
    title: str
    """Title"""
    unknown_reply_email_enabled: str
    """Unknown reply email enabled"""
    updated_at: str
    """Updated at"""
    updater: str
    """Updater"""
    use_sales_navigator_for_linked_in_tasks: str
    """Use sales navigator for linked in tasks"""
    user_guid: str
    """User guid"""
    username: str
    """Username"""
    users_view_id: str
    """Users view id"""
    voicemail_notification_enabled: str
    """Voicemail notification enabled"""
    voicemail_prompts: str
    """Voicemail prompts"""
    weekly_digest_email_enabled: str
    """Weekly digest email enabled"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    accounts_view_id: AirbyteSortOrder
    """Accounts view id"""
    active_prospects_count: AirbyteSortOrder
    """Active prospects count"""
    activity_notifications_disabled: AirbyteSortOrder
    """Activity notifications disabled"""
    batches: AirbyteSortOrder
    """Batches"""
    batches_view_id: AirbyteSortOrder
    """Batches view id"""
    bounce_warning_email_enabled: AirbyteSortOrder
    """Bounce warning email enabled"""
    bridge_phone: AirbyteSortOrder
    """Bridge phone"""
    bridge_phone_extension: AirbyteSortOrder
    """Bridge phone extension"""
    buyer_language_preference: AirbyteSortOrder
    """Buyer language preference"""
    calendar: AirbyteSortOrder
    """Calendar"""
    calendar_events_view_id: AirbyteSortOrder
    """Calendar events view id"""
    calls_view_id: AirbyteSortOrder
    """Calls view id"""
    content_categories: AirbyteSortOrder
    """Content categories"""
    content_category_ownerships: AirbyteSortOrder
    """Content category ownerships"""
    controlled_tab_default: AirbyteSortOrder
    """Controlled tab default"""
    created_at: AirbyteSortOrder
    """Created at"""
    creator: AirbyteSortOrder
    """Creator"""
    current_sign_in_at: AirbyteSortOrder
    """Current sign in at"""
    custom1: AirbyteSortOrder
    """Custom field 1"""
    custom2: AirbyteSortOrder
    """Custom field 2"""
    custom3: AirbyteSortOrder
    """Custom field 3"""
    custom4: AirbyteSortOrder
    """Custom field 4"""
    custom5: AirbyteSortOrder
    """Custom field 5"""
    daily_digest_email_enabled: AirbyteSortOrder
    """Daily digest email enabled"""
    default_ruleset_id: AirbyteSortOrder
    """Default ruleset id"""
    default_schedule_id: AirbyteSortOrder
    """Default schedule id"""
    duties: AirbyteSortOrder
    """Duties"""
    duties_set_at: AirbyteSortOrder
    """Duties set at"""
    email: AirbyteSortOrder
    """Email"""
    enable_voice_recordings: AirbyteSortOrder
    """Enable voice recordings"""
    engagement_emails_enabled: AirbyteSortOrder
    """Engagement emails enabled"""
    favorites: AirbyteSortOrder
    """Favorites"""
    first_name: AirbyteSortOrder
    """First name"""
    global_id: AirbyteSortOrder
    """Global id"""
    id: AirbyteSortOrder
    """Unique user identifier"""
    imports_view_id: AirbyteSortOrder
    """Imports view id"""
    inbound_bridge_phone: AirbyteSortOrder
    """Inbound bridge phone"""
    inbound_bridge_phone_extension: AirbyteSortOrder
    """Inbound bridge phone extension"""
    inbound_call_behavior: AirbyteSortOrder
    """Inbound call behavior"""
    inbound_phone_type: AirbyteSortOrder
    """Inbound phone type"""
    inbound_voicemail_custom_message_text: AirbyteSortOrder
    """Inbound voicemail custom message text"""
    inbound_voicemail_message_text_voice: AirbyteSortOrder
    """Inbound voicemail message text voice"""
    inbound_voicemail_prompt_type: AirbyteSortOrder
    """Inbound voicemail prompt type"""
    job_role: AirbyteSortOrder
    """Job role"""
    kaia_recordings_view_id: AirbyteSortOrder
    """Kaia recordings view id"""
    keep_bridge_phone_connected: AirbyteSortOrder
    """Keep bridge phone connected"""
    language_preference: AirbyteSortOrder
    """Language preference"""
    last_name: AirbyteSortOrder
    """Last name"""
    last_sign_in_at: AirbyteSortOrder
    """Last sign in at"""
    link_to_sequence_state_in_task_flow: AirbyteSortOrder
    """Link to sequence state in task flow"""
    live_listen_view_id: AirbyteSortOrder
    """Live listen view id"""
    locked: AirbyteSortOrder
    """Locked"""
    mailbox: AirbyteSortOrder
    """Mailbox"""
    mailbox_error_email_enabled: AirbyteSortOrder
    """Mailbox error email enabled"""
    mailboxes: AirbyteSortOrder
    """Mailboxes"""
    mailings_delivered_count: AirbyteSortOrder
    """Mailings delivered count"""
    mailings_replied_count: AirbyteSortOrder
    """Mailings replied count"""
    mailings_view_id: AirbyteSortOrder
    """Mailings view id"""
    meeting_engagement_notification_enabled: AirbyteSortOrder
    """Meeting engagement notification enabled"""
    meeting_types_view_id: AirbyteSortOrder
    """Meeting types view id"""
    name: AirbyteSortOrder
    """Name"""
    notifications_enabled: AirbyteSortOrder
    """Notifications enabled"""
    oce_click_to_dial_everywhere: AirbyteSortOrder
    """Oce click to dial everywhere"""
    oce_gmail_toolbar: AirbyteSortOrder
    """Oce gmail toolbar"""
    oce_gmail_tracking_state: AirbyteSortOrder
    """Oce gmail tracking state"""
    oce_salesforce_email_decorating: AirbyteSortOrder
    """Oce salesforce email decorating"""
    oce_salesforce_phone_decorating: AirbyteSortOrder
    """Oce salesforce phone decorating"""
    oce_universal_task_flow: AirbyteSortOrder
    """Oce universal task flow"""
    oce_window_mode: AirbyteSortOrder
    """Oce window mode"""
    onboarded_at: AirbyteSortOrder
    """Onboarded at"""
    opportunities_view_id: AirbyteSortOrder
    """Opportunities view id"""
    orca_standalone_enabled: AirbyteSortOrder
    """Orca standalone enabled"""
    outbound_voicemails: AirbyteSortOrder
    """Outbound voicemails"""
    password_expires_at: AirbyteSortOrder
    """Password expires at"""
    phone: AirbyteSortOrder
    """Phone"""
    phone_country_code: AirbyteSortOrder
    """Phone country code"""
    phone_number: AirbyteSortOrder
    """Phone number"""
    phone_type: AirbyteSortOrder
    """Phone type"""
    phones: AirbyteSortOrder
    """Phones"""
    phones_view_id: AirbyteSortOrder
    """Phones view id"""
    plugin_alert_notification_enabled: AirbyteSortOrder
    """Plugin alert notification enabled"""
    preferred_voice_region: AirbyteSortOrder
    """Preferred voice region"""
    prefers_local_presence: AirbyteSortOrder
    """Prefers local presence"""
    primary_timezone: AirbyteSortOrder
    """Primary timezone"""
    profile: AirbyteSortOrder
    """Profile"""
    prospect_detail_default: AirbyteSortOrder
    """Prospect detail default"""
    prospects_view_id: AirbyteSortOrder
    """Prospects view id"""
    recipients: AirbyteSortOrder
    """Recipients"""
    reports_sequence_performance_view_id: AirbyteSortOrder
    """Reports sequence performance view id"""
    reports_team_perf_view_id: AirbyteSortOrder
    """Reports team perf view id"""
    reports_team_performance_intraday_view_id: AirbyteSortOrder
    """Reports team performance intraday view id"""
    reports_team_performance_view_id: AirbyteSortOrder
    """Reports team performance view id"""
    reports_view_id: AirbyteSortOrder
    """Reports view id"""
    role: AirbyteSortOrder
    """Role"""
    scim_external_id: AirbyteSortOrder
    """Scim external id"""
    scim_source: AirbyteSortOrder
    """Scim source"""
    secondary_timezone: AirbyteSortOrder
    """Secondary timezone"""
    send_invite_fallback: AirbyteSortOrder
    """Send invite fallback"""
    sender_notifications_excluded: AirbyteSortOrder
    """Sender notifications excluded"""
    sequence_states_view_id: AirbyteSortOrder
    """Sequence states view id"""
    sequences_view_id: AirbyteSortOrder
    """Sequences view id"""
    sms_phone: AirbyteSortOrder
    """Sms phone"""
    snippets_view_id: AirbyteSortOrder
    """Snippets view id"""
    tasks_due_count: AirbyteSortOrder
    """Tasks due count"""
    tasks_view_id: AirbyteSortOrder
    """Tasks view id"""
    teams: AirbyteSortOrder
    """Teams"""
    teams_view_id: AirbyteSortOrder
    """Teams view id"""
    templates_view_id: AirbyteSortOrder
    """Templates view id"""
    tertiary_timezone: AirbyteSortOrder
    """Tertiary timezone"""
    texting_email_notifications: AirbyteSortOrder
    """Texting email notifications"""
    title: AirbyteSortOrder
    """Title"""
    unknown_reply_email_enabled: AirbyteSortOrder
    """Unknown reply email enabled"""
    updated_at: AirbyteSortOrder
    """Updated at"""
    updater: AirbyteSortOrder
    """Updater"""
    use_sales_navigator_for_linked_in_tasks: AirbyteSortOrder
    """Use sales navigator for linked in tasks"""
    user_guid: AirbyteSortOrder
    """User guid"""
    username: AirbyteSortOrder
    """Username"""
    users_view_id: AirbyteSortOrder
    """Users view id"""
    voicemail_notification_enabled: AirbyteSortOrder
    """Voicemail notification enabled"""
    voicemail_prompts: AirbyteSortOrder
    """Voicemail prompts"""
    weekly_digest_email_enabled: AirbyteSortOrder
    """Weekly digest email enabled"""


# Entity-specific condition types for users
class UsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsersSearchFilter


class UsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsersSearchFilter


class UsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsersSearchFilter


class UsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsersSearchFilter


class UsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsersSearchFilter


class UsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsersSearchFilter


class UsersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: UsersStringFilter


class UsersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: UsersAnyValueFilter


class UsersArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: UsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsersInCondition = TypedDict("UsersInCondition", {"in": UsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsersNotCondition = TypedDict("UsersNotCondition", {"not": "UsersCondition"}, total=False)
"""Negates the nested condition."""

UsersAndCondition = TypedDict("UsersAndCondition", {"and": "list[UsersCondition]"}, total=False)
"""True if all nested conditions are true."""

UsersOrCondition = TypedDict("UsersOrCondition", {"or": "list[UsersCondition]"}, total=False)
"""True if any nested condition is true."""

UsersAnyCondition = TypedDict("UsersAnyCondition", {"any": UsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all users condition types
UsersCondition = (
    UsersEqCondition
    | UsersNeqCondition
    | UsersGtCondition
    | UsersGteCondition
    | UsersLtCondition
    | UsersLteCondition
    | UsersInCondition
    | UsersStartswithCondition
    | UsersEndswithCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersArrayContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
