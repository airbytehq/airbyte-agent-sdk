"""
Type definitions for github connector.
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

class RepositoriesGetParams(TypedDict):
    """Parameters for repositories.get operation"""
    owner: str
    repo: str
    fields: NotRequired[list[str]]

class RepositoriesListParams(TypedDict):
    """Parameters for repositories.list operation"""
    username: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class RepositoriesApiSearchParams(TypedDict):
    """Parameters for repositories.api_search operation"""
    query: str
    limit: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class OrgRepositoriesListParams(TypedDict):
    """Parameters for org_repositories.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class BranchesListParams(TypedDict):
    """Parameters for branches.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class BranchesGetParams(TypedDict):
    """Parameters for branches.get operation"""
    owner: str
    repo: str
    branch: str
    fields: NotRequired[list[str]]

class CommitsListParams(TypedDict):
    """Parameters for commits.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    path: NotRequired[str]
    fields: NotRequired[list[str]]

class CommitsGetParams(TypedDict):
    """Parameters for commits.get operation"""
    owner: str
    repo: str
    sha: str
    fields: NotRequired[list[str]]

class ReleasesListParams(TypedDict):
    """Parameters for releases.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ReleasesGetParams(TypedDict):
    """Parameters for releases.get operation"""
    owner: str
    repo: str
    tag: str
    fields: NotRequired[list[str]]

class IssuesListParams(TypedDict):
    """Parameters for issues.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class IssuesApiSearchParams(TypedDict):
    """Parameters for issues.api_search operation"""
    query: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class IssuesCreateParams(TypedDict):
    """Parameters for issues.create operation"""
    title: str
    body: NotRequired[str]
    labels: NotRequired[list[str]]
    assignees: NotRequired[list[str]]
    milestone: NotRequired[int | None]
    owner: str
    repo: str

class IssuesUpdateParams(TypedDict):
    """Parameters for issues.update operation"""
    title: NotRequired[str]
    body: NotRequired[str]
    state: NotRequired[str]
    state_reason: NotRequired[str | None]
    labels: NotRequired[list[str]]
    assignees: NotRequired[list[str]]
    milestone: NotRequired[int | None]
    owner: str
    repo: str
    issue_number: str

class CommentsCreateParams(TypedDict):
    """Parameters for comments.create operation"""
    body: str
    owner: str
    repo: str
    issue_number: str

class PullRequestsCreateParams(TypedDict):
    """Parameters for pull_requests.create operation"""
    title: str
    head: str
    base: str
    body: NotRequired[str]
    draft: NotRequired[bool]
    maintainer_can_modify: NotRequired[bool]
    owner: str
    repo: str

class PullRequestsListParams(TypedDict):
    """Parameters for pull_requests.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class PullRequestsGetParams(TypedDict):
    """Parameters for pull_requests.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class PullRequestsApiSearchParams(TypedDict):
    """Parameters for pull_requests.api_search operation"""
    query: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ReviewsListParams(TypedDict):
    """Parameters for reviews.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class CommentsListParams(TypedDict):
    """Parameters for comments.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class CommentsGetParams(TypedDict):
    """Parameters for comments.get operation"""
    id: str
    fields: NotRequired[list[str]]

class PrCommentsListParams(TypedDict):
    """Parameters for pr_comments.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class PrCommentsGetParams(TypedDict):
    """Parameters for pr_comments.get operation"""
    id: str
    fields: NotRequired[list[str]]

class LabelsListParams(TypedDict):
    """Parameters for labels.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class LabelsGetParams(TypedDict):
    """Parameters for labels.get operation"""
    owner: str
    repo: str
    name: str
    fields: NotRequired[list[str]]

class MilestonesListParams(TypedDict):
    """Parameters for milestones.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class MilestonesGetParams(TypedDict):
    """Parameters for milestones.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class OrganizationsGetParams(TypedDict):
    """Parameters for organizations.get operation"""
    org: str
    fields: NotRequired[list[str]]

class OrganizationsListParams(TypedDict):
    """Parameters for organizations.list operation"""
    username: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    username: str
    fields: NotRequired[list[str]]

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class UsersApiSearchParams(TypedDict):
    """Parameters for users.api_search operation"""
    query: str
    limit: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    org: str
    team_slug: str
    fields: NotRequired[list[str]]

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TagsGetParams(TypedDict):
    """Parameters for tags.get operation"""
    owner: str
    repo: str
    tag: str
    fields: NotRequired[list[str]]

class StargazersListParams(TypedDict):
    """Parameters for stargazers.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ViewerGetParams(TypedDict):
    """Parameters for viewer.get operation"""
    fields: NotRequired[list[str]]

class ViewerRepositoriesListParams(TypedDict):
    """Parameters for viewer_repositories.list operation"""
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    org: str
    project_number: int
    fields: NotRequired[list[str]]

class ProjectItemsListParams(TypedDict):
    """Parameters for project_items.list operation"""
    org: str
    project_number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class DiscussionsListParams(TypedDict):
    """Parameters for discussions.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    answered: NotRequired[bool]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class DiscussionsGetParams(TypedDict):
    """Parameters for discussions.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class DiscussionsApiSearchParams(TypedDict):
    """Parameters for discussions.api_search operation"""
    query: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class FileContentGetParams(TypedDict):
    """Parameters for file_content.get operation"""
    owner: str
    repo: str
    path: str
    ref: NotRequired[str]
    fields: NotRequired[list[str]]

class DirectoryContentListParams(TypedDict):
    """Parameters for directory_content.list operation"""
    owner: str
    repo: str
    path: str
    ref: NotRequired[str]
    fields: NotRequired[list[str]]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== BRANCHES SEARCH TYPES =====

class BranchesSearchFilter(TypedDict, total=False):
    """Available fields for filtering branches search queries."""
    name: str | None
    """Branch name (e.g. `main`, `feature/foo`)"""
    prefix: str | None
    """Git ref prefix for the branch (typically `refs/heads/`)"""


class BranchesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    name: list[str]
    """Branch name (e.g. `main`, `feature/foo`)"""
    prefix: list[str]
    """Git ref prefix for the branch (typically `refs/heads/`)"""


class BranchesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    name: Any
    """Branch name (e.g. `main`, `feature/foo`)"""
    prefix: Any
    """Git ref prefix for the branch (typically `refs/heads/`)"""


class BranchesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    name: str
    """Branch name (e.g. `main`, `feature/foo`)"""
    prefix: str
    """Git ref prefix for the branch (typically `refs/heads/`)"""


class BranchesSortFilter(TypedDict, total=False):
    """Available fields for sorting branches search results."""
    name: AirbyteSortOrder
    """Branch name (e.g. `main`, `feature/foo`)"""
    prefix: AirbyteSortOrder
    """Git ref prefix for the branch (typically `refs/heads/`)"""


# Entity-specific condition types for branches
class BranchesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BranchesSearchFilter


class BranchesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BranchesSearchFilter


class BranchesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BranchesSearchFilter


class BranchesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BranchesSearchFilter


class BranchesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BranchesSearchFilter


class BranchesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BranchesSearchFilter


class BranchesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BranchesStringFilter


class BranchesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BranchesStringFilter


class BranchesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BranchesStringFilter


class BranchesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BranchesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BranchesInCondition = TypedDict("BranchesInCondition", {"in": BranchesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BranchesNotCondition = TypedDict("BranchesNotCondition", {"not": "BranchesCondition"}, total=False)
"""Negates the nested condition."""

BranchesAndCondition = TypedDict("BranchesAndCondition", {"and": "list[BranchesCondition]"}, total=False)
"""True if all nested conditions are true."""

BranchesOrCondition = TypedDict("BranchesOrCondition", {"or": "list[BranchesCondition]"}, total=False)
"""True if any nested condition is true."""

BranchesAnyCondition = TypedDict("BranchesAnyCondition", {"any": BranchesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all branches condition types
BranchesCondition = (
    BranchesEqCondition
    | BranchesNeqCondition
    | BranchesGtCondition
    | BranchesGteCondition
    | BranchesLtCondition
    | BranchesLteCondition
    | BranchesInCondition
    | BranchesLikeCondition
    | BranchesFuzzyCondition
    | BranchesKeywordCondition
    | BranchesContainsCondition
    | BranchesNotCondition
    | BranchesAndCondition
    | BranchesOrCondition
    | BranchesAnyCondition
)


class BranchesSearchQuery(TypedDict, total=False):
    """Search query for branches entity."""
    filter: BranchesCondition
    sort: list[BranchesSortFilter]


# ===== COMMENTS SEARCH TYPES =====

class CommentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering comments search queries."""
    id: str | None
    """GraphQL node ID of the comment"""
    database_id: int | None
    """REST API numeric identifier for the comment"""
    body: str | None
    """Markdown body of the comment"""
    created_at: str | None
    """ISO 8601 timestamp when the comment was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the comment was last updated"""
    url: str | None
    """Permalink to the comment on GitHub"""
    is_minimized: bool | None
    """Whether the comment has been hidden/collapsed"""


class CommentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the comment"""
    database_id: list[int]
    """REST API numeric identifier for the comment"""
    body: list[str]
    """Markdown body of the comment"""
    created_at: list[str]
    """ISO 8601 timestamp when the comment was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the comment was last updated"""
    url: list[str]
    """Permalink to the comment on GitHub"""
    is_minimized: list[bool]
    """Whether the comment has been hidden/collapsed"""


class CommentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the comment"""
    database_id: Any
    """REST API numeric identifier for the comment"""
    body: Any
    """Markdown body of the comment"""
    created_at: Any
    """ISO 8601 timestamp when the comment was created"""
    updated_at: Any
    """ISO 8601 timestamp when the comment was last updated"""
    url: Any
    """Permalink to the comment on GitHub"""
    is_minimized: Any
    """Whether the comment has been hidden/collapsed"""


class CommentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the comment"""
    database_id: str
    """REST API numeric identifier for the comment"""
    body: str
    """Markdown body of the comment"""
    created_at: str
    """ISO 8601 timestamp when the comment was created"""
    updated_at: str
    """ISO 8601 timestamp when the comment was last updated"""
    url: str
    """Permalink to the comment on GitHub"""
    is_minimized: str
    """Whether the comment has been hidden/collapsed"""


class CommentsSortFilter(TypedDict, total=False):
    """Available fields for sorting comments search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the comment"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the comment"""
    body: AirbyteSortOrder
    """Markdown body of the comment"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the comment was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the comment was last updated"""
    url: AirbyteSortOrder
    """Permalink to the comment on GitHub"""
    is_minimized: AirbyteSortOrder
    """Whether the comment has been hidden/collapsed"""


# Entity-specific condition types for comments
class CommentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CommentsSearchFilter


class CommentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CommentsSearchFilter


class CommentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CommentsSearchFilter


class CommentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CommentsSearchFilter


class CommentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CommentsSearchFilter


class CommentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CommentsSearchFilter


class CommentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CommentsStringFilter


class CommentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CommentsStringFilter


class CommentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CommentsStringFilter


class CommentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CommentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CommentsInCondition = TypedDict("CommentsInCondition", {"in": CommentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CommentsNotCondition = TypedDict("CommentsNotCondition", {"not": "CommentsCondition"}, total=False)
"""Negates the nested condition."""

CommentsAndCondition = TypedDict("CommentsAndCondition", {"and": "list[CommentsCondition]"}, total=False)
"""True if all nested conditions are true."""

CommentsOrCondition = TypedDict("CommentsOrCondition", {"or": "list[CommentsCondition]"}, total=False)
"""True if any nested condition is true."""

CommentsAnyCondition = TypedDict("CommentsAnyCondition", {"any": CommentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all comments condition types
CommentsCondition = (
    CommentsEqCondition
    | CommentsNeqCondition
    | CommentsGtCondition
    | CommentsGteCondition
    | CommentsLtCondition
    | CommentsLteCondition
    | CommentsInCondition
    | CommentsLikeCondition
    | CommentsFuzzyCondition
    | CommentsKeywordCondition
    | CommentsContainsCondition
    | CommentsNotCondition
    | CommentsAndCondition
    | CommentsOrCondition
    | CommentsAnyCondition
)


class CommentsSearchQuery(TypedDict, total=False):
    """Search query for comments entity."""
    filter: CommentsCondition
    sort: list[CommentsSortFilter]


# ===== ISSUES SEARCH TYPES =====

class IssuesSearchFilter(TypedDict, total=False):
    """Available fields for filtering issues search queries."""
    id: str | None
    """GraphQL node ID of the issue"""
    database_id: int | None
    """REST API numeric identifier for the issue"""
    number: int | None
    """Repository-scoped issue number"""
    title: str | None
    """Issue title"""
    state: str | None
    """Issue state: `OPEN` or `CLOSED`"""
    state_reason: str | None
    """Reason the issue is in its current state (e.g. `COMPLETED`, `NOT_PLANNED`)"""
    created_at: str | None
    """ISO 8601 timestamp when the issue was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: str | None
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: bool | None
    """Whether the conversation on the issue is locked"""
    url: str | None
    """Permalink to the issue on GitHub"""


class IssuesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the issue"""
    database_id: list[int]
    """REST API numeric identifier for the issue"""
    number: list[int]
    """Repository-scoped issue number"""
    title: list[str]
    """Issue title"""
    state: list[str]
    """Issue state: `OPEN` or `CLOSED`"""
    state_reason: list[str]
    """Reason the issue is in its current state (e.g. `COMPLETED`, `NOT_PLANNED`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the issue was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: list[str]
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: list[bool]
    """Whether the conversation on the issue is locked"""
    url: list[str]
    """Permalink to the issue on GitHub"""


class IssuesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the issue"""
    database_id: Any
    """REST API numeric identifier for the issue"""
    number: Any
    """Repository-scoped issue number"""
    title: Any
    """Issue title"""
    state: Any
    """Issue state: `OPEN` or `CLOSED`"""
    state_reason: Any
    """Reason the issue is in its current state (e.g. `COMPLETED`, `NOT_PLANNED`)"""
    created_at: Any
    """ISO 8601 timestamp when the issue was created"""
    updated_at: Any
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: Any
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: Any
    """Whether the conversation on the issue is locked"""
    url: Any
    """Permalink to the issue on GitHub"""


class IssuesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the issue"""
    database_id: str
    """REST API numeric identifier for the issue"""
    number: str
    """Repository-scoped issue number"""
    title: str
    """Issue title"""
    state: str
    """Issue state: `OPEN` or `CLOSED`"""
    state_reason: str
    """Reason the issue is in its current state (e.g. `COMPLETED`, `NOT_PLANNED`)"""
    created_at: str
    """ISO 8601 timestamp when the issue was created"""
    updated_at: str
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: str
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: str
    """Whether the conversation on the issue is locked"""
    url: str
    """Permalink to the issue on GitHub"""


class IssuesSortFilter(TypedDict, total=False):
    """Available fields for sorting issues search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the issue"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the issue"""
    number: AirbyteSortOrder
    """Repository-scoped issue number"""
    title: AirbyteSortOrder
    """Issue title"""
    state: AirbyteSortOrder
    """Issue state: `OPEN` or `CLOSED`"""
    state_reason: AirbyteSortOrder
    """Reason the issue is in its current state (e.g. `COMPLETED`, `NOT_PLANNED`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the issue was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: AirbyteSortOrder
    """Whether the conversation on the issue is locked"""
    url: AirbyteSortOrder
    """Permalink to the issue on GitHub"""


# Entity-specific condition types for issues
class IssuesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IssuesSearchFilter


class IssuesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IssuesSearchFilter


class IssuesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IssuesSearchFilter


class IssuesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IssuesSearchFilter


class IssuesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IssuesSearchFilter


class IssuesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IssuesSearchFilter


class IssuesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IssuesStringFilter


class IssuesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssuesStringFilter


class IssuesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssuesStringFilter


class IssuesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IssuesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IssuesInCondition = TypedDict("IssuesInCondition", {"in": IssuesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IssuesNotCondition = TypedDict("IssuesNotCondition", {"not": "IssuesCondition"}, total=False)
"""Negates the nested condition."""

IssuesAndCondition = TypedDict("IssuesAndCondition", {"and": "list[IssuesCondition]"}, total=False)
"""True if all nested conditions are true."""

IssuesOrCondition = TypedDict("IssuesOrCondition", {"or": "list[IssuesCondition]"}, total=False)
"""True if any nested condition is true."""

IssuesAnyCondition = TypedDict("IssuesAnyCondition", {"any": IssuesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all issues condition types
IssuesCondition = (
    IssuesEqCondition
    | IssuesNeqCondition
    | IssuesGtCondition
    | IssuesGteCondition
    | IssuesLtCondition
    | IssuesLteCondition
    | IssuesInCondition
    | IssuesLikeCondition
    | IssuesFuzzyCondition
    | IssuesKeywordCondition
    | IssuesContainsCondition
    | IssuesNotCondition
    | IssuesAndCondition
    | IssuesOrCondition
    | IssuesAnyCondition
)


class IssuesSearchQuery(TypedDict, total=False):
    """Search query for issues entity."""
    filter: IssuesCondition
    sort: list[IssuesSortFilter]


# ===== ORGANIZATIONS SEARCH TYPES =====

class OrganizationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering organizations search queries."""
    id: str | None
    """GraphQL node ID of the organization"""
    database_id: int | None
    """REST API numeric identifier for the organization"""
    login: str | None
    """Organization login/handle (unique URL slug)"""
    name: str | None
    """Display name of the organization"""
    description: str | None
    """Short public description of the organization"""
    email: str | None
    """Public contact email for the organization, if set"""
    location: str | None
    """Public location of the organization, if set"""
    is_verified: bool | None
    """Whether the organization has a verified domain"""
    created_at: str | None
    """ISO 8601 timestamp when the organization was created"""


class OrganizationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the organization"""
    database_id: list[int]
    """REST API numeric identifier for the organization"""
    login: list[str]
    """Organization login/handle (unique URL slug)"""
    name: list[str]
    """Display name of the organization"""
    description: list[str]
    """Short public description of the organization"""
    email: list[str]
    """Public contact email for the organization, if set"""
    location: list[str]
    """Public location of the organization, if set"""
    is_verified: list[bool]
    """Whether the organization has a verified domain"""
    created_at: list[str]
    """ISO 8601 timestamp when the organization was created"""


class OrganizationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the organization"""
    database_id: Any
    """REST API numeric identifier for the organization"""
    login: Any
    """Organization login/handle (unique URL slug)"""
    name: Any
    """Display name of the organization"""
    description: Any
    """Short public description of the organization"""
    email: Any
    """Public contact email for the organization, if set"""
    location: Any
    """Public location of the organization, if set"""
    is_verified: Any
    """Whether the organization has a verified domain"""
    created_at: Any
    """ISO 8601 timestamp when the organization was created"""


class OrganizationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the organization"""
    database_id: str
    """REST API numeric identifier for the organization"""
    login: str
    """Organization login/handle (unique URL slug)"""
    name: str
    """Display name of the organization"""
    description: str
    """Short public description of the organization"""
    email: str
    """Public contact email for the organization, if set"""
    location: str
    """Public location of the organization, if set"""
    is_verified: str
    """Whether the organization has a verified domain"""
    created_at: str
    """ISO 8601 timestamp when the organization was created"""


class OrganizationsSortFilter(TypedDict, total=False):
    """Available fields for sorting organizations search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the organization"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the organization"""
    login: AirbyteSortOrder
    """Organization login/handle (unique URL slug)"""
    name: AirbyteSortOrder
    """Display name of the organization"""
    description: AirbyteSortOrder
    """Short public description of the organization"""
    email: AirbyteSortOrder
    """Public contact email for the organization, if set"""
    location: AirbyteSortOrder
    """Public location of the organization, if set"""
    is_verified: AirbyteSortOrder
    """Whether the organization has a verified domain"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the organization was created"""


# Entity-specific condition types for organizations
class OrganizationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrganizationsSearchFilter


class OrganizationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrganizationsSearchFilter


class OrganizationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrganizationsSearchFilter


class OrganizationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrganizationsSearchFilter


class OrganizationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrganizationsSearchFilter


class OrganizationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrganizationsSearchFilter


class OrganizationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrganizationsStringFilter


class OrganizationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrganizationsStringFilter


class OrganizationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrganizationsStringFilter


class OrganizationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrganizationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrganizationsInCondition = TypedDict("OrganizationsInCondition", {"in": OrganizationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrganizationsNotCondition = TypedDict("OrganizationsNotCondition", {"not": "OrganizationsCondition"}, total=False)
"""Negates the nested condition."""

OrganizationsAndCondition = TypedDict("OrganizationsAndCondition", {"and": "list[OrganizationsCondition]"}, total=False)
"""True if all nested conditions are true."""

OrganizationsOrCondition = TypedDict("OrganizationsOrCondition", {"or": "list[OrganizationsCondition]"}, total=False)
"""True if any nested condition is true."""

OrganizationsAnyCondition = TypedDict("OrganizationsAnyCondition", {"any": OrganizationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all organizations condition types
OrganizationsCondition = (
    OrganizationsEqCondition
    | OrganizationsNeqCondition
    | OrganizationsGtCondition
    | OrganizationsGteCondition
    | OrganizationsLtCondition
    | OrganizationsLteCondition
    | OrganizationsInCondition
    | OrganizationsLikeCondition
    | OrganizationsFuzzyCondition
    | OrganizationsKeywordCondition
    | OrganizationsContainsCondition
    | OrganizationsNotCondition
    | OrganizationsAndCondition
    | OrganizationsOrCondition
    | OrganizationsAnyCondition
)


class OrganizationsSearchQuery(TypedDict, total=False):
    """Search query for organizations entity."""
    filter: OrganizationsCondition
    sort: list[OrganizationsSortFilter]


# ===== PULL_REQUESTS SEARCH TYPES =====

class PullRequestsSearchFilter(TypedDict, total=False):
    """Available fields for filtering pull_requests search queries."""
    id: str | None
    """GraphQL node ID of the pull request"""
    database_id: int | None
    """REST API numeric identifier for the pull request"""
    number: int | None
    """Repository-scoped pull request number"""
    title: str | None
    """Pull request title"""
    state: str | None
    """Pull request state: `OPEN`, `CLOSED`, or `MERGED`"""
    is_draft: bool | None
    """Whether the pull request is still a draft"""
    merged: bool | None
    """Whether the pull request has been merged"""
    created_at: str | None
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: str | None
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: str | None
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    base_ref_name: str | None
    """Name of the branch being merged into"""
    head_ref_name: str | None
    """Name of the branch with the proposed changes"""
    url: str | None
    """Permalink to the pull request on GitHub"""


class PullRequestsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the pull request"""
    database_id: list[int]
    """REST API numeric identifier for the pull request"""
    number: list[int]
    """Repository-scoped pull request number"""
    title: list[str]
    """Pull request title"""
    state: list[str]
    """Pull request state: `OPEN`, `CLOSED`, or `MERGED`"""
    is_draft: list[bool]
    """Whether the pull request is still a draft"""
    merged: list[bool]
    """Whether the pull request has been merged"""
    created_at: list[str]
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: list[str]
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: list[str]
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    base_ref_name: list[str]
    """Name of the branch being merged into"""
    head_ref_name: list[str]
    """Name of the branch with the proposed changes"""
    url: list[str]
    """Permalink to the pull request on GitHub"""


class PullRequestsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the pull request"""
    database_id: Any
    """REST API numeric identifier for the pull request"""
    number: Any
    """Repository-scoped pull request number"""
    title: Any
    """Pull request title"""
    state: Any
    """Pull request state: `OPEN`, `CLOSED`, or `MERGED`"""
    is_draft: Any
    """Whether the pull request is still a draft"""
    merged: Any
    """Whether the pull request has been merged"""
    created_at: Any
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: Any
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: Any
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: Any
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    base_ref_name: Any
    """Name of the branch being merged into"""
    head_ref_name: Any
    """Name of the branch with the proposed changes"""
    url: Any
    """Permalink to the pull request on GitHub"""


class PullRequestsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the pull request"""
    database_id: str
    """REST API numeric identifier for the pull request"""
    number: str
    """Repository-scoped pull request number"""
    title: str
    """Pull request title"""
    state: str
    """Pull request state: `OPEN`, `CLOSED`, or `MERGED`"""
    is_draft: str
    """Whether the pull request is still a draft"""
    merged: str
    """Whether the pull request has been merged"""
    created_at: str
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: str
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: str
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: str
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    base_ref_name: str
    """Name of the branch being merged into"""
    head_ref_name: str
    """Name of the branch with the proposed changes"""
    url: str
    """Permalink to the pull request on GitHub"""


class PullRequestsSortFilter(TypedDict, total=False):
    """Available fields for sorting pull_requests search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the pull request"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the pull request"""
    number: AirbyteSortOrder
    """Repository-scoped pull request number"""
    title: AirbyteSortOrder
    """Pull request title"""
    state: AirbyteSortOrder
    """Pull request state: `OPEN`, `CLOSED`, or `MERGED`"""
    is_draft: AirbyteSortOrder
    """Whether the pull request is still a draft"""
    merged: AirbyteSortOrder
    """Whether the pull request has been merged"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: AirbyteSortOrder
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    base_ref_name: AirbyteSortOrder
    """Name of the branch being merged into"""
    head_ref_name: AirbyteSortOrder
    """Name of the branch with the proposed changes"""
    url: AirbyteSortOrder
    """Permalink to the pull request on GitHub"""


# Entity-specific condition types for pull_requests
class PullRequestsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PullRequestsSearchFilter


class PullRequestsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PullRequestsSearchFilter


class PullRequestsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PullRequestsSearchFilter


class PullRequestsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PullRequestsSearchFilter


class PullRequestsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PullRequestsSearchFilter


class PullRequestsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PullRequestsSearchFilter


class PullRequestsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PullRequestsStringFilter


class PullRequestsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PullRequestsStringFilter


class PullRequestsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PullRequestsStringFilter


class PullRequestsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PullRequestsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PullRequestsInCondition = TypedDict("PullRequestsInCondition", {"in": PullRequestsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PullRequestsNotCondition = TypedDict("PullRequestsNotCondition", {"not": "PullRequestsCondition"}, total=False)
"""Negates the nested condition."""

PullRequestsAndCondition = TypedDict("PullRequestsAndCondition", {"and": "list[PullRequestsCondition]"}, total=False)
"""True if all nested conditions are true."""

PullRequestsOrCondition = TypedDict("PullRequestsOrCondition", {"or": "list[PullRequestsCondition]"}, total=False)
"""True if any nested condition is true."""

PullRequestsAnyCondition = TypedDict("PullRequestsAnyCondition", {"any": PullRequestsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all pull_requests condition types
PullRequestsCondition = (
    PullRequestsEqCondition
    | PullRequestsNeqCondition
    | PullRequestsGtCondition
    | PullRequestsGteCondition
    | PullRequestsLtCondition
    | PullRequestsLteCondition
    | PullRequestsInCondition
    | PullRequestsLikeCondition
    | PullRequestsFuzzyCondition
    | PullRequestsKeywordCondition
    | PullRequestsContainsCondition
    | PullRequestsNotCondition
    | PullRequestsAndCondition
    | PullRequestsOrCondition
    | PullRequestsAnyCondition
)


class PullRequestsSearchQuery(TypedDict, total=False):
    """Search query for pull_requests entity."""
    filter: PullRequestsCondition
    sort: list[PullRequestsSortFilter]


# ===== REPOSITORIES SEARCH TYPES =====

class RepositoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering repositories search queries."""
    id: str | None
    """GraphQL node ID of the repository"""
    name: str | None
    """Short repository name (without owner)"""
    name_with_owner: str | None
    """Fully-qualified `owner/name` identifier for the repository"""
    description: str | None
    """Short description of the repository"""
    url: str | None
    """Canonical GitHub URL for the repository"""
    created_at: str | None
    """ISO 8601 timestamp when the repository was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: str | None
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: int | None
    """Number of forks of the repository"""
    stargazer_count: int | None
    """Number of users who have starred the repository"""
    is_private: bool | None
    """Whether the repository is private"""
    is_fork: bool | None
    """Whether the repository is a fork of another repository"""
    is_archived: bool | None
    """Whether the repository has been archived"""


class RepositoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the repository"""
    name: list[str]
    """Short repository name (without owner)"""
    name_with_owner: list[str]
    """Fully-qualified `owner/name` identifier for the repository"""
    description: list[str]
    """Short description of the repository"""
    url: list[str]
    """Canonical GitHub URL for the repository"""
    created_at: list[str]
    """ISO 8601 timestamp when the repository was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: list[str]
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: list[int]
    """Number of forks of the repository"""
    stargazer_count: list[int]
    """Number of users who have starred the repository"""
    is_private: list[bool]
    """Whether the repository is private"""
    is_fork: list[bool]
    """Whether the repository is a fork of another repository"""
    is_archived: list[bool]
    """Whether the repository has been archived"""


class RepositoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the repository"""
    name: Any
    """Short repository name (without owner)"""
    name_with_owner: Any
    """Fully-qualified `owner/name` identifier for the repository"""
    description: Any
    """Short description of the repository"""
    url: Any
    """Canonical GitHub URL for the repository"""
    created_at: Any
    """ISO 8601 timestamp when the repository was created"""
    updated_at: Any
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: Any
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: Any
    """Number of forks of the repository"""
    stargazer_count: Any
    """Number of users who have starred the repository"""
    is_private: Any
    """Whether the repository is private"""
    is_fork: Any
    """Whether the repository is a fork of another repository"""
    is_archived: Any
    """Whether the repository has been archived"""


class RepositoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the repository"""
    name: str
    """Short repository name (without owner)"""
    name_with_owner: str
    """Fully-qualified `owner/name` identifier for the repository"""
    description: str
    """Short description of the repository"""
    url: str
    """Canonical GitHub URL for the repository"""
    created_at: str
    """ISO 8601 timestamp when the repository was created"""
    updated_at: str
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: str
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: str
    """Number of forks of the repository"""
    stargazer_count: str
    """Number of users who have starred the repository"""
    is_private: str
    """Whether the repository is private"""
    is_fork: str
    """Whether the repository is a fork of another repository"""
    is_archived: str
    """Whether the repository has been archived"""


class RepositoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting repositories search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the repository"""
    name: AirbyteSortOrder
    """Short repository name (without owner)"""
    name_with_owner: AirbyteSortOrder
    """Fully-qualified `owner/name` identifier for the repository"""
    description: AirbyteSortOrder
    """Short description of the repository"""
    url: AirbyteSortOrder
    """Canonical GitHub URL for the repository"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the repository was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: AirbyteSortOrder
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: AirbyteSortOrder
    """Number of forks of the repository"""
    stargazer_count: AirbyteSortOrder
    """Number of users who have starred the repository"""
    is_private: AirbyteSortOrder
    """Whether the repository is private"""
    is_fork: AirbyteSortOrder
    """Whether the repository is a fork of another repository"""
    is_archived: AirbyteSortOrder
    """Whether the repository has been archived"""


# Entity-specific condition types for repositories
class RepositoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: RepositoriesSearchFilter


class RepositoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: RepositoriesSearchFilter


class RepositoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: RepositoriesSearchFilter


class RepositoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: RepositoriesSearchFilter


class RepositoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: RepositoriesSearchFilter


class RepositoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: RepositoriesSearchFilter


class RepositoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: RepositoriesStringFilter


class RepositoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: RepositoriesStringFilter


class RepositoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: RepositoriesStringFilter


class RepositoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: RepositoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
RepositoriesInCondition = TypedDict("RepositoriesInCondition", {"in": RepositoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

RepositoriesNotCondition = TypedDict("RepositoriesNotCondition", {"not": "RepositoriesCondition"}, total=False)
"""Negates the nested condition."""

RepositoriesAndCondition = TypedDict("RepositoriesAndCondition", {"and": "list[RepositoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

RepositoriesOrCondition = TypedDict("RepositoriesOrCondition", {"or": "list[RepositoriesCondition]"}, total=False)
"""True if any nested condition is true."""

RepositoriesAnyCondition = TypedDict("RepositoriesAnyCondition", {"any": RepositoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all repositories condition types
RepositoriesCondition = (
    RepositoriesEqCondition
    | RepositoriesNeqCondition
    | RepositoriesGtCondition
    | RepositoriesGteCondition
    | RepositoriesLtCondition
    | RepositoriesLteCondition
    | RepositoriesInCondition
    | RepositoriesLikeCondition
    | RepositoriesFuzzyCondition
    | RepositoriesKeywordCondition
    | RepositoriesContainsCondition
    | RepositoriesNotCondition
    | RepositoriesAndCondition
    | RepositoriesOrCondition
    | RepositoriesAnyCondition
)


class RepositoriesSearchQuery(TypedDict, total=False):
    """Search query for repositories entity."""
    filter: RepositoriesCondition
    sort: list[RepositoriesSortFilter]


# ===== STARGAZERS SEARCH TYPES =====

class StargazersSearchFilter(TypedDict, total=False):
    """Available fields for filtering stargazers search queries."""
    starred_at: str | None
    """ISO 8601 timestamp when the user starred the repository"""


class StargazersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    starred_at: list[str]
    """ISO 8601 timestamp when the user starred the repository"""


class StargazersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    starred_at: Any
    """ISO 8601 timestamp when the user starred the repository"""


class StargazersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    starred_at: str
    """ISO 8601 timestamp when the user starred the repository"""


class StargazersSortFilter(TypedDict, total=False):
    """Available fields for sorting stargazers search results."""
    starred_at: AirbyteSortOrder
    """ISO 8601 timestamp when the user starred the repository"""


# Entity-specific condition types for stargazers
class StargazersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: StargazersSearchFilter


class StargazersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: StargazersSearchFilter


class StargazersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: StargazersSearchFilter


class StargazersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: StargazersSearchFilter


class StargazersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: StargazersSearchFilter


class StargazersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: StargazersSearchFilter


class StargazersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: StargazersStringFilter


class StargazersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: StargazersStringFilter


class StargazersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: StargazersStringFilter


class StargazersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: StargazersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
StargazersInCondition = TypedDict("StargazersInCondition", {"in": StargazersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

StargazersNotCondition = TypedDict("StargazersNotCondition", {"not": "StargazersCondition"}, total=False)
"""Negates the nested condition."""

StargazersAndCondition = TypedDict("StargazersAndCondition", {"and": "list[StargazersCondition]"}, total=False)
"""True if all nested conditions are true."""

StargazersOrCondition = TypedDict("StargazersOrCondition", {"or": "list[StargazersCondition]"}, total=False)
"""True if any nested condition is true."""

StargazersAnyCondition = TypedDict("StargazersAnyCondition", {"any": StargazersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all stargazers condition types
StargazersCondition = (
    StargazersEqCondition
    | StargazersNeqCondition
    | StargazersGtCondition
    | StargazersGteCondition
    | StargazersLtCondition
    | StargazersLteCondition
    | StargazersInCondition
    | StargazersLikeCondition
    | StargazersFuzzyCondition
    | StargazersKeywordCondition
    | StargazersContainsCondition
    | StargazersNotCondition
    | StargazersAndCondition
    | StargazersOrCondition
    | StargazersAnyCondition
)


class StargazersSearchQuery(TypedDict, total=False):
    """Search query for stargazers entity."""
    filter: StargazersCondition
    sort: list[StargazersSortFilter]


# ===== TAGS SEARCH TYPES =====

class TagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tags search queries."""
    name: str | None
    """Tag name (e.g. `v1.2.3`)"""
    prefix: str | None
    """Git ref prefix for the tag (typically `refs/tags/`)"""


class TagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    name: list[str]
    """Tag name (e.g. `v1.2.3`)"""
    prefix: list[str]
    """Git ref prefix for the tag (typically `refs/tags/`)"""


class TagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    name: Any
    """Tag name (e.g. `v1.2.3`)"""
    prefix: Any
    """Git ref prefix for the tag (typically `refs/tags/`)"""


class TagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    name: str
    """Tag name (e.g. `v1.2.3`)"""
    prefix: str
    """Git ref prefix for the tag (typically `refs/tags/`)"""


class TagsSortFilter(TypedDict, total=False):
    """Available fields for sorting tags search results."""
    name: AirbyteSortOrder
    """Tag name (e.g. `v1.2.3`)"""
    prefix: AirbyteSortOrder
    """Git ref prefix for the tag (typically `refs/tags/`)"""


# Entity-specific condition types for tags
class TagsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TagsSearchFilter


class TagsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TagsSearchFilter


class TagsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TagsSearchFilter


class TagsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TagsSearchFilter


class TagsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TagsSearchFilter


class TagsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TagsSearchFilter


class TagsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TagsStringFilter


class TagsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TagsStringFilter


class TagsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TagsStringFilter


class TagsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TagsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TagsInCondition = TypedDict("TagsInCondition", {"in": TagsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TagsNotCondition = TypedDict("TagsNotCondition", {"not": "TagsCondition"}, total=False)
"""Negates the nested condition."""

TagsAndCondition = TypedDict("TagsAndCondition", {"and": "list[TagsCondition]"}, total=False)
"""True if all nested conditions are true."""

TagsOrCondition = TypedDict("TagsOrCondition", {"or": "list[TagsCondition]"}, total=False)
"""True if any nested condition is true."""

TagsAnyCondition = TypedDict("TagsAnyCondition", {"any": TagsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tags condition types
TagsCondition = (
    TagsEqCondition
    | TagsNeqCondition
    | TagsGtCondition
    | TagsGteCondition
    | TagsLtCondition
    | TagsLteCondition
    | TagsInCondition
    | TagsLikeCondition
    | TagsFuzzyCondition
    | TagsKeywordCondition
    | TagsContainsCondition
    | TagsNotCondition
    | TagsAndCondition
    | TagsOrCondition
    | TagsAnyCondition
)


class TagsSearchQuery(TypedDict, total=False):
    """Search query for tags entity."""
    filter: TagsCondition
    sort: list[TagsSortFilter]


# ===== TEAMS SEARCH TYPES =====

class TeamsSearchFilter(TypedDict, total=False):
    """Available fields for filtering teams search queries."""
    id: str | None
    """GraphQL node ID of the team"""
    database_id: int | None
    """REST API numeric identifier for the team"""
    slug: str | None
    """URL-friendly slug for the team within its organization"""
    name: str | None
    """Display name of the team"""
    description: str | None
    """Short description of the team"""
    privacy: str | None
    """Team visibility: `SECRET` or `VISIBLE`"""
    url: str | None
    """Permalink to the team on GitHub"""
    created_at: str | None
    """ISO 8601 timestamp when the team was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the team was last updated"""


class TeamsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the team"""
    database_id: list[int]
    """REST API numeric identifier for the team"""
    slug: list[str]
    """URL-friendly slug for the team within its organization"""
    name: list[str]
    """Display name of the team"""
    description: list[str]
    """Short description of the team"""
    privacy: list[str]
    """Team visibility: `SECRET` or `VISIBLE`"""
    url: list[str]
    """Permalink to the team on GitHub"""
    created_at: list[str]
    """ISO 8601 timestamp when the team was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the team was last updated"""


class TeamsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the team"""
    database_id: Any
    """REST API numeric identifier for the team"""
    slug: Any
    """URL-friendly slug for the team within its organization"""
    name: Any
    """Display name of the team"""
    description: Any
    """Short description of the team"""
    privacy: Any
    """Team visibility: `SECRET` or `VISIBLE`"""
    url: Any
    """Permalink to the team on GitHub"""
    created_at: Any
    """ISO 8601 timestamp when the team was created"""
    updated_at: Any
    """ISO 8601 timestamp when the team was last updated"""


class TeamsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the team"""
    database_id: str
    """REST API numeric identifier for the team"""
    slug: str
    """URL-friendly slug for the team within its organization"""
    name: str
    """Display name of the team"""
    description: str
    """Short description of the team"""
    privacy: str
    """Team visibility: `SECRET` or `VISIBLE`"""
    url: str
    """Permalink to the team on GitHub"""
    created_at: str
    """ISO 8601 timestamp when the team was created"""
    updated_at: str
    """ISO 8601 timestamp when the team was last updated"""


class TeamsSortFilter(TypedDict, total=False):
    """Available fields for sorting teams search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the team"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the team"""
    slug: AirbyteSortOrder
    """URL-friendly slug for the team within its organization"""
    name: AirbyteSortOrder
    """Display name of the team"""
    description: AirbyteSortOrder
    """Short description of the team"""
    privacy: AirbyteSortOrder
    """Team visibility: `SECRET` or `VISIBLE`"""
    url: AirbyteSortOrder
    """Permalink to the team on GitHub"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the team was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the team was last updated"""


# Entity-specific condition types for teams
class TeamsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TeamsSearchFilter


class TeamsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TeamsSearchFilter


class TeamsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TeamsSearchFilter


class TeamsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TeamsSearchFilter


class TeamsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TeamsSearchFilter


class TeamsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TeamsSearchFilter


class TeamsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TeamsStringFilter


class TeamsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TeamsStringFilter


class TeamsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TeamsStringFilter


class TeamsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TeamsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TeamsInCondition = TypedDict("TeamsInCondition", {"in": TeamsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TeamsNotCondition = TypedDict("TeamsNotCondition", {"not": "TeamsCondition"}, total=False)
"""Negates the nested condition."""

TeamsAndCondition = TypedDict("TeamsAndCondition", {"and": "list[TeamsCondition]"}, total=False)
"""True if all nested conditions are true."""

TeamsOrCondition = TypedDict("TeamsOrCondition", {"or": "list[TeamsCondition]"}, total=False)
"""True if any nested condition is true."""

TeamsAnyCondition = TypedDict("TeamsAnyCondition", {"any": TeamsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all teams condition types
TeamsCondition = (
    TeamsEqCondition
    | TeamsNeqCondition
    | TeamsGtCondition
    | TeamsGteCondition
    | TeamsLtCondition
    | TeamsLteCondition
    | TeamsInCondition
    | TeamsLikeCondition
    | TeamsFuzzyCondition
    | TeamsKeywordCondition
    | TeamsContainsCondition
    | TeamsNotCondition
    | TeamsAndCondition
    | TeamsOrCondition
    | TeamsAnyCondition
)


class TeamsSearchQuery(TypedDict, total=False):
    """Search query for teams entity."""
    filter: TeamsCondition
    sort: list[TeamsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    id: str | None
    """GraphQL node ID of the user"""
    database_id: int | None
    """REST API numeric identifier for the user"""
    login: str | None
    """User login/handle"""
    name: str | None
    """Public display name of the user, if set"""
    email: str | None
    """Public email address of the user, if set"""
    company: str | None
    """Public company affiliation of the user, if set"""
    location: str | None
    """Public location of the user, if set"""
    twitter_username: str | None
    """Public Twitter/X username of the user, if set"""
    url: str | None
    """Permalink to the user's profile on GitHub"""
    created_at: str | None
    """ISO 8601 timestamp when the user account was created"""
    is_hireable: bool | None
    """Whether the user has marked themselves as available for hire"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """GraphQL node ID of the user"""
    database_id: list[int]
    """REST API numeric identifier for the user"""
    login: list[str]
    """User login/handle"""
    name: list[str]
    """Public display name of the user, if set"""
    email: list[str]
    """Public email address of the user, if set"""
    company: list[str]
    """Public company affiliation of the user, if set"""
    location: list[str]
    """Public location of the user, if set"""
    twitter_username: list[str]
    """Public Twitter/X username of the user, if set"""
    url: list[str]
    """Permalink to the user's profile on GitHub"""
    created_at: list[str]
    """ISO 8601 timestamp when the user account was created"""
    is_hireable: list[bool]
    """Whether the user has marked themselves as available for hire"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """GraphQL node ID of the user"""
    database_id: Any
    """REST API numeric identifier for the user"""
    login: Any
    """User login/handle"""
    name: Any
    """Public display name of the user, if set"""
    email: Any
    """Public email address of the user, if set"""
    company: Any
    """Public company affiliation of the user, if set"""
    location: Any
    """Public location of the user, if set"""
    twitter_username: Any
    """Public Twitter/X username of the user, if set"""
    url: Any
    """Permalink to the user's profile on GitHub"""
    created_at: Any
    """ISO 8601 timestamp when the user account was created"""
    is_hireable: Any
    """Whether the user has marked themselves as available for hire"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """GraphQL node ID of the user"""
    database_id: str
    """REST API numeric identifier for the user"""
    login: str
    """User login/handle"""
    name: str
    """Public display name of the user, if set"""
    email: str
    """Public email address of the user, if set"""
    company: str
    """Public company affiliation of the user, if set"""
    location: str
    """Public location of the user, if set"""
    twitter_username: str
    """Public Twitter/X username of the user, if set"""
    url: str
    """Permalink to the user's profile on GitHub"""
    created_at: str
    """ISO 8601 timestamp when the user account was created"""
    is_hireable: str
    """Whether the user has marked themselves as available for hire"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    id: AirbyteSortOrder
    """GraphQL node ID of the user"""
    database_id: AirbyteSortOrder
    """REST API numeric identifier for the user"""
    login: AirbyteSortOrder
    """User login/handle"""
    name: AirbyteSortOrder
    """Public display name of the user, if set"""
    email: AirbyteSortOrder
    """Public email address of the user, if set"""
    company: AirbyteSortOrder
    """Public company affiliation of the user, if set"""
    location: AirbyteSortOrder
    """Public location of the user, if set"""
    twitter_username: AirbyteSortOrder
    """Public Twitter/X username of the user, if set"""
    url: AirbyteSortOrder
    """Permalink to the user's profile on GitHub"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the user account was created"""
    is_hireable: AirbyteSortOrder
    """Whether the user has marked themselves as available for hire"""


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


class UsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UsersAnyValueFilter


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
    | UsersLikeCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
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
