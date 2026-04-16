"""
Github connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import GithubConnector
from .models import (
    GithubAuthConfig,
    GithubReplicationConfig,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    BranchesSearchData,
    BranchesSearchResult,
    CommentsSearchData,
    CommentsSearchResult,
    IssuesSearchData,
    IssuesSearchResult,
    OrganizationsSearchData,
    OrganizationsSearchResult,
    PullRequestsSearchData,
    PullRequestsSearchResult,
    RepositoriesSearchData,
    RepositoriesSearchResult,
    StargazersSearchData,
    StargazersSearchResult,
    TagsSearchData,
    TagsSearchResult,
    TeamsSearchData,
    TeamsSearchResult,
    UsersSearchData,
    UsersSearchResult,
)
from airbyte_agent_sdk.types import AirbyteAuthConfig

__all__ = [
    "GithubConnector",
    "AirbyteAuthConfig",
    "GithubAuthConfig",
    "GithubReplicationConfig",
    "AirbyteSearchMeta",
    "AirbyteSearchResult",
    "BranchesSearchData",
    "BranchesSearchResult",
    "CommentsSearchData",
    "CommentsSearchResult",
    "IssuesSearchData",
    "IssuesSearchResult",
    "OrganizationsSearchData",
    "OrganizationsSearchResult",
    "PullRequestsSearchData",
    "PullRequestsSearchResult",
    "RepositoriesSearchData",
    "RepositoriesSearchResult",
    "StargazersSearchData",
    "StargazersSearchResult",
    "TagsSearchData",
    "TagsSearchResult",
    "TeamsSearchData",
    "TeamsSearchResult",
    "UsersSearchData",
    "UsersSearchResult",
]