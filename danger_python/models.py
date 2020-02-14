from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel


class BitBucketCloudCommit(BaseModel):
    author: Optional["BitBucketCloudCommitAuthor"]
    date: Optional[str]
    hash: Optional[str]
    links: Optional["BitBucketCloudCommitsLinks"]
    message: Optional[str]
    parents: Optional[List["BitBucketCloudCommitParents"]]

    class Config:
        fields = {
            "author": "author",
            "date": "date",
            "hash": "hash",
            "links": "links",
            "message": "message",
            "parents": "parents",
        }


class BitBucketCloudCommitAuthor(BaseModel):
    raw: Optional[str]
    user: Optional["BitBucketCloudUser"]

    class Config:
        fields = {
            "raw": "raw",
            "user": "user",
        }


class BitBucketCloudCommitParents(BaseModel):
    hash: Optional[str]

    class Config:
        fields = {
            "hash": "hash",
        }


class BitBucketCloudCommitsLinks(BaseModel):
    html: Optional["BitBucketCloudCommitsLinksHtml"]

    class Config:
        fields = {
            "html": "html",
        }


class BitBucketCloudCommitsLinksHtml(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinks(BaseModel):
    activity: Optional["BitBucketCloudCompletePRLinksActivity"]
    approve: Optional["BitBucketCloudCompletePRLinksApprove"]
    comments: Optional["BitBucketCloudCompletePRLinksComments"]
    commits: Optional["BitBucketCloudCompletePRLinksCommits"]
    decline: Optional["BitBucketCloudCompletePRLinksDecline"]
    diff: Optional["BitBucketCloudCompletePRLinksDiff"]
    html: Optional["BitBucketCloudCompletePRLinksHtml"]
    merge: Optional["BitBucketCloudCompletePRLinksMerge"]
    self_: Optional["BitBucketCloudCompletePRLinksSelf"]
    statuses: Optional["BitBucketCloudCompletePRLinksStatuses"]

    class Config:
        fields = {
            "activity": "activity",
            "approve": "approve",
            "comments": "comments",
            "commits": "commits",
            "decline": "decline",
            "diff": "diff",
            "html": "html",
            "merge": "merge",
            "self_": "self",
            "statuses": "statuses",
        }


class BitBucketCloudCompletePRLinksActivity(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksApprove(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksComments(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksCommits(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksDecline(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksDiff(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksHtml(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksMerge(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksSelf(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudCompletePRLinksStatuses(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudContent(BaseModel):
    html: Optional[str]
    markup: Optional[str]
    raw: Optional[str]
    type: Optional["BitBucketCloudContentType"]

    class Config:
        fields = {
            "html": "html",
            "markup": "markup",
            "raw": "raw",
            "type": "type",
        }


class BitBucketCloudContentType(Enum):
    RENDERED = "rendered"


class BitBucketCloudJSONDSL(BaseModel):
    activities: Optional[List["BitBucketCloudPRActivity"]]
    comments: Optional[List["BitBucketCloudPRComment"]]
    commits: Optional[List["BitBucketCloudCommit"]]
    metadata: Optional["RepoMetaData"]
    pr: Optional["BitBucketCloudPRDSL"]

    class Config:
        fields = {
            "activities": "activities",
            "comments": "comments",
            "commits": "commits",
            "metadata": "metadata",
            "pr": "pr",
        }


class BitBucketCloudMergeRef(BaseModel):
    branch: Optional["BitBucketCloudMergeRefBranch"]
    commit: Optional["BitBucketCloudMergeRefCommit"]
    repository: Optional["BitBucketCloudRepo"]

    class Config:
        fields = {
            "branch": "branch",
            "commit": "commit",
            "repository": "repository",
        }


class BitBucketCloudMergeRefBranch(BaseModel):
    name: Optional[str]

    class Config:
        fields = {
            "name": "name",
        }


class BitBucketCloudMergeRefCommit(BaseModel):
    hash: Optional[str]

    class Config:
        fields = {
            "hash": "hash",
        }


class BitBucketCloudPRActivity(BaseModel):
    comment: Optional["BitBucketCloudPRComment"]
    pull_request: Optional["BitBucketCloudPRActivityPullRequest"]

    class Config:
        fields = {
            "comment": "comment",
            "pull_request": "pull_request",
        }


class BitBucketCloudPRActivityPullRequest(BaseModel):
    id: Optional[int]
    title: Optional[str]

    class Config:
        fields = {
            "id": "id",
            "title": "title",
        }


class BitBucketCloudPRComment(BaseModel):
    content: Optional["BitBucketCloudContent"]
    created_on: Optional[str]
    deleted: Optional[bool]
    id: Optional[int]
    inline: Optional["BitBucketCloudPRCommentInline"]
    links: Optional["BitBucketCloudPRLinks"]
    pullrequest: Optional["BitBucketCloudPRCommentPullrequest"]
    type: Optional[str]
    updated_on: Optional[str]
    user: Optional["BitBucketCloudUser"]

    class Config:
        fields = {
            "content": "content",
            "created_on": "created_on",
            "deleted": "deleted",
            "id": "id",
            "inline": "inline",
            "links": "links",
            "pullrequest": "pullrequest",
            "type": "type",
            "updated_on": "updated_on",
            "user": "user",
        }


class BitBucketCloudPRCommentInline(BaseModel):
    from_: Optional[int]
    path: Optional[str]
    to: Optional[int]

    class Config:
        fields = {
            "from_": "from",
            "path": "path",
            "to": "to",
        }


class BitBucketCloudPRCommentPullrequest(BaseModel):
    id: Optional[int]
    links: Optional["BitBucketCloudPRLinks"]
    title: Optional[str]

    class Config:
        fields = {
            "id": "id",
            "links": "links",
            "title": "title",
        }


class BitBucketCloudPRDSL(BaseModel):
    author: Optional["BitBucketCloudUser"]
    created_on: Optional[int]
    description: Optional[str]
    destination: Optional["BitBucketCloudMergeRef"]
    id: Optional[int]
    links: Optional["BitBucketCloudCompletePRLinks"]
    participants: Optional[List["BitBucketCloudPRParticipant"]]
    reviewers: Optional[List["BitBucketCloudUser"]]
    source: Optional["BitBucketCloudMergeRef"]
    state: Optional["BitBucketCloudPRDSLState"]
    title: Optional[str]
    updated_on: Optional[int]

    class Config:
        fields = {
            "author": "author",
            "created_on": "created_on",
            "description": "description",
            "destination": "destination",
            "id": "id",
            "links": "links",
            "participants": "participants",
            "reviewers": "reviewers",
            "source": "source",
            "state": "state",
            "title": "title",
            "updated_on": "updated_on",
        }


class BitBucketCloudPRDSLState(Enum):
    DECLINED = "DECLINED"
    MERGED = "MERGED"
    OPEN = "OPEN"
    SUPERSEDED = "SUPERSEDED"


class BitBucketCloudPRLinks(BaseModel):
    html: Optional["BitBucketCloudPRLinksHtml"]
    self_: Optional["BitBucketCloudPRLinksSelf"]

    class Config:
        fields = {
            "html": "html",
            "self_": "self",
        }


class BitBucketCloudPRLinksHtml(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudPRLinksSelf(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudPRParticipant(BaseModel):
    approved: Optional[bool]
    role: Optional["BitBucketCloudPRParticipantRole"]
    user: Optional["BitBucketCloudUser"]

    class Config:
        fields = {
            "approved": "approved",
            "role": "role",
            "user": "user",
        }


class BitBucketCloudPRParticipantRole(Enum):
    PARTICIPANT = "PARTICIPANT"
    REVIEWER = "REVIEWER"


class BitBucketCloudRepo(BaseModel):
    full_name: Optional[str]
    name: Optional[str]
    uuid: Optional[str]

    class Config:
        fields = {
            "full_name": "full_name",
            "name": "name",
            "uuid": "uuid",
        }


class BitBucketCloudUser(BaseModel):
    account_id: Optional[str]
    display_name: Optional[str]
    nickname: Optional[str]
    uuid: Optional[str]

    class Config:
        fields = {
            "account_id": "account_id",
            "display_name": "display_name",
            "nickname": "nickname",
            "uuid": "uuid",
        }


class BitBucketServerCommit(BaseModel):
    author: Optional["BitBucketServerCommitAuthor"]
    author_timestamp: Optional[int]
    committer: Optional["BitBucketServerCommitCommitter"]
    committer_timestamp: Optional[int]
    display_id: Optional[str]
    id: Optional[str]
    message: Optional[str]
    parents: Optional[List["BitBucketServerCommitParents"]]

    class Config:
        fields = {
            "author": "author",
            "author_timestamp": "authorTimestamp",
            "committer": "committer",
            "committer_timestamp": "committerTimestamp",
            "display_id": "displayId",
            "id": "id",
            "message": "message",
            "parents": "parents",
        }


class BitBucketServerCommitAuthor(BaseModel):
    display_name: Optional[str]
    email_address: Optional[str]
    name: Optional[str]

    class Config:
        fields = {
            "display_name": "displayName",
            "email_address": "emailAddress",
            "name": "name",
        }


class BitBucketServerCommitCommitter(BaseModel):
    display_name: Optional[str]
    email_address: Optional[str]
    name: Optional[str]

    class Config:
        fields = {
            "display_name": "displayName",
            "email_address": "emailAddress",
            "name": "name",
        }


class BitBucketServerCommitParents(BaseModel):
    display_id: Optional[str]
    id: Optional[str]

    class Config:
        fields = {
            "display_id": "displayId",
            "id": "id",
        }


class BitBucketServerJSONDSL(BaseModel):
    activities: Optional[List["BitBucketServerPRActivity"]]
    comments: Optional[List["BitBucketServerPRActivity"]]
    commits: Optional[List["BitBucketServerCommit"]]
    issues: Optional[List["JIRAIssue"]]
    metadata: Optional["RepoMetaData"]
    pr: Optional["BitBucketServerPRDSL"]

    class Config:
        fields = {
            "activities": "activities",
            "comments": "comments",
            "commits": "commits",
            "issues": "issues",
            "metadata": "metadata",
            "pr": "pr",
        }


class BitBucketServerLinks(Enum):
    CLONE = "clone"
    SELF = "self"


class BitBucketServerMergeRef(BaseModel):
    display_id: Optional[str]
    id: Optional[str]
    latest_commit: Optional[str]
    repository: Optional["BitBucketServerRepo"]

    class Config:
        fields = {
            "display_id": "displayId",
            "id": "id",
            "latest_commit": "latestCommit",
            "repository": "repository",
        }


class BitBucketServerPRActivity(BaseModel):
    action: Optional["BitBucketServerPRActivityAction"]
    comment: Optional["BitBucketServerPRComment"]
    comment_action: Optional["BitBucketServerPRActivityCommentAction"]
    comment_anchor: Optional["BitBucketServerPRActivityCommentAnchor"]
    created_date: Optional[int]
    id: Optional[int]
    user: Optional["BitBucketServerUser"]

    class Config:
        fields = {
            "action": "action",
            "comment": "comment",
            "comment_action": "commentAction",
            "comment_anchor": "commentAnchor",
            "created_date": "createdDate",
            "id": "id",
            "user": "user",
        }


class BitBucketServerPRActivityAction(Enum):
    COMMENTED = "COMMENTED"
    DECLINED = "DECLINED"
    MERGED = "MERGED"
    OPENED = "OPENED"
    UPDATED = "UPDATED"


class BitBucketServerPRActivityCommentAction(Enum):
    ADDED = "ADDED"
    UPDATED = "UPDATED"


class BitBucketServerPRActivityCommentAnchor(BaseModel):
    diff_type: Optional["BitBucketServerPRActivityCommentAnchorDiffType"]
    file_type: Optional["BitBucketServerPRActivityCommentAnchorFileType"]
    from_hash: Optional[str]
    line: Optional[int]
    line_type: Optional["BitBucketServerPRActivityCommentAnchorLineType"]
    path: Optional[str]
    src_path: Optional[str]
    to_hash: Optional[str]

    class Config:
        fields = {
            "diff_type": "diffType",
            "file_type": "fileType",
            "from_hash": "fromHash",
            "line": "line",
            "line_type": "lineType",
            "path": "path",
            "src_path": "srcPath",
            "to_hash": "toHash",
        }


class BitBucketServerPRActivityCommentAnchorDiffType(Enum):
    COMMIT = "COMMIT"
    EFFECTIVE = "EFFECTIVE"
    RANGE = "RANGE"
    REQUIRED = "REQUIRED"


class BitBucketServerPRActivityCommentAnchorFileType(Enum):
    FROM = "FROM"
    TO = "TO"


class BitBucketServerPRActivityCommentAnchorLineType(Enum):
    ADDED = "ADDED"
    CONTEXT = "CONTEXT"
    REMOVED = "REMOVED"


class BitBucketServerPRComment(BaseModel):
    author: Optional["BitBucketServerUser"]
    comments: Optional[List["BitBucketServerPRActivity"]]
    created_date: Optional[int]
    id: Optional[int]
    parent: Optional["BitBucketServerPRCommentParent"]
    permitted_operations: Optional["BitBucketServerPRCommentPermittedOperations"]
    text: Optional[str]
    updated_date: Optional[int]
    version: Optional[int]

    class Config:
        fields = {
            "author": "author",
            "comments": "comments",
            "created_date": "createdDate",
            "id": "id",
            "parent": "parent",
            "permitted_operations": "permittedOperations",
            "text": "text",
            "updated_date": "updatedDate",
            "version": "version",
        }


class BitBucketServerPRCommentParent(BaseModel):
    id: Optional[int]

    class Config:
        fields = {
            "id": "id",
        }


class BitBucketServerPRCommentPermittedOperations(BaseModel):
    deletable: Optional[bool]
    editable: Optional[bool]

    class Config:
        fields = {
            "deletable": "deletable",
            "editable": "editable",
        }


class BitBucketServerPRDSL(BaseModel):
    author: Optional["BitBucketServerPRParticipant"]
    closed: Optional[bool]
    created_date: Optional[int]
    description: Optional[str]
    from_ref: Optional["BitBucketServerMergeRef"]
    id: Optional[int]
    links: Optional["BitBucketServerPRDSLLinks"]
    locked: Optional[bool]
    open: Optional[bool]
    participants: Optional[List["BitBucketServerPRParticipant"]]
    reviewers: Optional[List["BitBucketServerPRParticipant"]]
    state: Optional["BitBucketServerPRDSLState"]
    title: Optional[str]
    to_ref: Optional["BitBucketServerMergeRef"]
    updated_date: Optional[int]
    version: Optional[int]

    class Config:
        fields = {
            "author": "author",
            "closed": "closed",
            "created_date": "createdDate",
            "description": "description",
            "from_ref": "fromRef",
            "id": "id",
            "links": "links",
            "locked": "locked",
            "open": "open",
            "participants": "participants",
            "reviewers": "reviewers",
            "state": "state",
            "title": "title",
            "to_ref": "toRef",
            "updated_date": "updatedDate",
            "version": "version",
        }


class BitBucketServerPRDSLLinks(Enum):
    SELF = "self"


class BitBucketServerPRDSLState(Enum):
    DECLINED = "DECLINED"
    MERGED = "MERGED"
    OPEN = "OPEN"
    SUPERSEDED = "SUPERSEDED"


class BitBucketServerPRParticipant(BaseModel):
    approved: Optional[bool]
    role: Optional["BitBucketServerPRParticipantRole"]
    status: Optional["BitBucketServerPRParticipantStatus"]
    user: Optional["BitBucketServerUser"]

    class Config:
        fields = {
            "approved": "approved",
            "role": "role",
            "status": "status",
            "user": "user",
        }


class BitBucketServerPRParticipantRole(Enum):
    AUTHOR = "AUTHOR"
    PARTICIPANT = "PARTICIPANT"
    REVIEWER = "REVIEWER"


class BitBucketServerPRParticipantStatus(Enum):
    APPROVED = "APPROVED"
    NEEDS_WORK = "NEEDS_WORK"
    UNAPPROVED = "UNAPPROVED"


class BitBucketServerRepo(BaseModel):
    forkable: Optional[bool]
    links: Optional["BitBucketServerLinks"]
    name: Optional[str]
    project: Optional["BitBucketServerRepoProject"]
    public: Optional[bool]
    scm_id: Optional[str]
    slug: Optional[str]

    class Config:
        fields = {
            "forkable": "forkable",
            "links": "links",
            "name": "name",
            "project": "project",
            "public": "public",
            "scm_id": "scmId",
            "slug": "slug",
        }


class BitBucketServerRepoProject(BaseModel):
    id: Optional[int]
    key: Optional[str]
    links: Optional["BitBucketServerRepoProjectLinks"]
    name: Optional[str]
    public: Optional[bool]
    type: Optional[str]

    class Config:
        fields = {
            "id": "id",
            "key": "key",
            "links": "links",
            "name": "name",
            "public": "public",
            "type": "type",
        }


class BitBucketServerRepoProjectLinks(Enum):
    SELF = "self"


class BitBucketServerUser(BaseModel):
    active: Optional[bool]
    display_name: Optional[str]
    email_address: Optional[str]
    id: Optional[int]
    name: Optional[str]
    slug: Optional[str]
    type: Optional["BitBucketServerUserType"]

    class Config:
        fields = {
            "active": "active",
            "display_name": "displayName",
            "email_address": "emailAddress",
            "id": "id",
            "name": "name",
            "slug": "slug",
            "type": "type",
        }


class BitBucketServerUserType(Enum):
    NORMAL = "NORMAL"
    SERVICE = "SERVICE"


class CliArgs(BaseModel):
    base: Optional[str]
    dangerfile: Optional[str]
    external_ci_provider: Optional[str]
    id: Optional[str]
    text_only: Optional[str]
    verbose: Optional[str]

    class Config:
        fields = {
            "base": "base",
            "dangerfile": "dangerfile",
            "external_ci_provider": "externalCiProvider",
            "id": "id",
            "text_only": "textOnly",
            "verbose": "verbose",
        }


class DangerDSLJSONType(BaseModel):
    bitbucket_cloud: Optional["BitBucketCloudJSONDSL"]
    bitbucket_server: Optional["BitBucketServerJSONDSL"]
    git: Optional["GitJSONDSL"]
    github: Optional["GitHubDSL"]
    gitlab: Optional["GitLabDSL"]
    settings: Optional["DangerDSLJSONTypeSettings"]

    class Config:
        fields = {
            "bitbucket_cloud": "bitbucket_cloud",
            "bitbucket_server": "bitbucket_server",
            "git": "git",
            "github": "github",
            "gitlab": "gitlab",
            "settings": "settings",
        }


class DangerDSLJSONTypeSettings(BaseModel):
    cli_args: Optional["CliArgs"]
    github: Optional["DangerDSLJSONTypeSettingsGithub"]

    class Config:
        fields = {
            "cli_args": "cliArgs",
            "github": "github",
        }


class DangerDSLJSONTypeSettingsGithub(BaseModel):
    access_token: Optional[str]
    additional_headers: Any
    base_url: Optional[str]

    class Config:
        fields = {
            "access_token": "accessToken",
            "additional_headers": "additionalHeaders",
            "base_url": "baseURL",
        }


class Endpoint(BaseModel):
    defaults: Optional["EndpointOptions"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
        }


class EndpointOptions(BaseModel):
    base_url: Optional[str]
    data: Any
    headers: Optional["EndpointOptionsHeaders"]
    method: Optional["EndpointOptionsMethod"]
    request: Optional["EndpointOptionsRequest"]
    url: Optional[str]

    class Config:
        fields = {
            "base_url": "baseUrl",
            "data": "data",
            "headers": "headers",
            "method": "method",
            "request": "request",
            "url": "url",
        }


class EndpointOptionsHeaders(BaseModel):
    pass


class EndpointOptionsMethod(Enum):
    DELETE = "DELETE"
    GET = "GET"
    HEAD = "HEAD"
    PATCH = "PATCH"
    POST = "POST"
    PUT = "PUT"


class EndpointOptionsRequest(BaseModel):
    pass


class GitCommit(BaseModel):
    author: Optional["GitCommitAuthor"]
    committer: Optional["GitCommitAuthor"]
    message: Optional[str]
    parents: Optional[List[str]]
    sha: Optional[str]
    tree: Any
    url: Optional[str]

    class Config:
        fields = {
            "author": "author",
            "committer": "committer",
            "message": "message",
            "parents": "parents",
            "sha": "sha",
            "tree": "tree",
            "url": "url",
        }


class GitCommitAuthor(BaseModel):
    date: Optional[str]
    email: Optional[str]
    name: Optional[str]

    class Config:
        fields = {
            "date": "date",
            "email": "email",
            "name": "name",
        }


class GitHubAPIPR(BaseModel):
    number: Optional[int]
    owner: Optional[str]
    repo: Optional[str]

    class Config:
        fields = {
            "number": "number",
            "owner": "owner",
            "repo": "repo",
        }


class GitHubCommit(BaseModel):
    author: Optional["GitHubUser"]
    commit: Optional["GitCommit"]
    committer: Optional["GitHubUser"]
    parents: Optional[List[Any]]
    sha: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "author": "author",
            "commit": "commit",
            "committer": "committer",
            "parents": "parents",
            "sha": "sha",
            "url": "url",
        }


class GitHubDSL(BaseModel):
    api: Optional["Octokit"]
    commits: Optional[List["GitHubCommit"]]
    issue: Optional["GitHubIssue"]
    pr: Optional["GitHubPRDSL"]
    requested_reviewers: Optional["GitHubReviewers"]
    reviews: Optional[List["GitHubReview"]]
    this_pr: Optional["GitHubAPIPR"]
    utils: Optional["GitHubUtilsDSL"]

    class Config:
        fields = {
            "api": "api",
            "commits": "commits",
            "issue": "issue",
            "pr": "pr",
            "requested_reviewers": "requested_reviewers",
            "reviews": "reviews",
            "this_pr": "thisPR",
            "utils": "utils",
        }


class GitHubIssue(BaseModel):
    labels: Optional[List["GitHubIssueLabel"]]

    class Config:
        fields = {
            "labels": "labels",
        }


class GitHubIssueLabel(BaseModel):
    color: Optional[str]
    id: Optional[int]
    name: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "color": "color",
            "id": "id",
            "name": "name",
            "url": "url",
        }


class GitHubMergeRef(BaseModel):
    label: Optional[str]
    ref: Optional[str]
    repo: Optional["GitHubRepo"]
    sha: Optional[str]
    user: Optional["GitHubUser"]

    class Config:
        fields = {
            "label": "label",
            "ref": "ref",
            "repo": "repo",
            "sha": "sha",
            "user": "user",
        }


class GitHubPRDSL(BaseModel):
    additions: Optional[int]
    assignee: Optional["GitHubUser"]
    assignees: Optional[List["GitHubUser"]]
    author_association: Optional["GitHubPRDSLAuthorAssociation"]
    base: Optional["GitHubMergeRef"]
    body: Optional[str]
    changed_files: Optional[int]
    closed_at: Optional[str]
    comments: Optional[int]
    commits: Optional[int]
    created_at: Optional[str]
    deletions: Optional[int]
    head: Optional["GitHubMergeRef"]
    html_url: Optional[str]
    locked: Optional[bool]
    merged: Optional[bool]
    merged_at: Optional[str]
    number: Optional[int]
    review_comments: Optional[int]
    state: Optional["GitHubPRDSLState"]
    title: Optional[str]
    updated_at: Optional[str]
    user: Optional["GitHubUser"]

    class Config:
        fields = {
            "additions": "additions",
            "assignee": "assignee",
            "assignees": "assignees",
            "author_association": "author_association",
            "base": "base",
            "body": "body",
            "changed_files": "changed_files",
            "closed_at": "closed_at",
            "comments": "comments",
            "commits": "commits",
            "created_at": "created_at",
            "deletions": "deletions",
            "head": "head",
            "html_url": "html_url",
            "locked": "locked",
            "merged": "merged",
            "merged_at": "merged_at",
            "number": "number",
            "review_comments": "review_comments",
            "state": "state",
            "title": "title",
            "updated_at": "updated_at",
            "user": "user",
        }


class GitHubPRDSLAuthorAssociation(Enum):
    COLLABORATOR = "COLLABORATOR"
    CONTRIBUTOR = "CONTRIBUTOR"
    FIRST_TIMER = "FIRST_TIMER"
    FIRST_TIME_CONTRIBUTOR = "FIRST_TIME_CONTRIBUTOR"
    MEMBER = "MEMBER"
    NONE = "NONE"
    OWNER = "OWNER"


class GitHubPRDSLState(Enum):
    CLOSED = "closed"
    LOCKED = "locked"
    MERGED = "merged"
    OPEN = "open"


class GitHubRepo(BaseModel):
    assignee: Optional["GitHubUser"]
    assignees: Optional[List["GitHubUser"]]
    description: Optional[str]
    fork: Optional[bool]
    full_name: Optional[str]
    html_url: Optional[str]
    id: Optional[int]
    name: Optional[str]
    owner: Optional["GitHubUser"]
    private: Optional[bool]

    class Config:
        fields = {
            "assignee": "assignee",
            "assignees": "assignees",
            "description": "description",
            "fork": "fork",
            "full_name": "full_name",
            "html_url": "html_url",
            "id": "id",
            "name": "name",
            "owner": "owner",
            "private": "private",
        }


class GitHubReview(BaseModel):
    body: Optional[str]
    commit_id: Optional[str]
    id: Optional[int]
    state: Optional["GitHubReviewState"]
    user: Optional["GitHubUser"]

    class Config:
        fields = {
            "body": "body",
            "commit_id": "commit_id",
            "id": "id",
            "state": "state",
            "user": "user",
        }


class GitHubReviewState(Enum):
    APPROVED = "APPROVED"
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    COMMENTED = "COMMENTED"
    DISMISSED = "DISMISSED"
    PENDING = "PENDING"


class GitHubReviewers(BaseModel):
    teams: Optional[List[Any]]
    users: Optional[List["GitHubUser"]]

    class Config:
        fields = {
            "teams": "teams",
            "users": "users",
        }


class GitHubUser(BaseModel):
    avatar_url: Optional[str]
    href: Optional[str]
    id: Optional[int]
    login: Optional[str]
    type: Optional["GitHubUserType"]

    class Config:
        fields = {
            "avatar_url": "avatar_url",
            "href": "href",
            "id": "id",
            "login": "login",
            "type": "type",
        }


class GitHubUserType(Enum):
    BOT = "Bot"
    ORGANIZATION = "Organization"
    USER = "User"


class GitHubUtilsDSL(BaseModel):
    create_or_add_label: Optional["GitHubUtilsDSLCreateOrAddLabel"]
    create_or_update_pr: Optional["GitHubUtilsDSLCreateOrUpdatePR"]
    create_updated_issue_with_id: Optional["GitHubUtilsDSLCreateUpdatedIssueWithID"]

    class Config:
        fields = {
            "create_or_add_label": "createOrAddLabel",
            "create_or_update_pr": "createOrUpdatePR",
            "create_updated_issue_with_id": "createUpdatedIssueWithID",
        }


class GitHubUtilsDSLCreateOrAddLabel(BaseModel):
    pass


class GitHubUtilsDSLCreateOrUpdatePR(BaseModel):
    pass


class GitHubUtilsDSLCreateUpdatedIssueWithID(BaseModel):
    pass


class GitJSONDSL(BaseModel):
    commits: Optional[List["GitCommit"]]
    created_files: Optional[List[str]]
    deleted_files: Optional[List[str]]
    modified_files: Optional[List[str]]

    class Config:
        fields = {
            "commits": "commits",
            "created_files": "created_files",
            "deleted_files": "deleted_files",
            "modified_files": "modified_files",
        }


class GitLabDSL(BaseModel):
    commits: Optional[List["GitLabMRCommit"]]
    metadata: Optional["RepoMetaData"]
    mr: Optional["GitLabMR"]
    utils: Optional["GitLabDSLUtils"]

    class Config:
        fields = {
            "commits": "commits",
            "metadata": "metadata",
            "mr": "mr",
            "utils": "utils",
        }


class GitLabDSLUtils(BaseModel):
    pass


class GitLabMR(BaseModel):
    allow_collaboration: Optional[bool]
    allow_maintainer_to_push: Optional[bool]
    approvals_before_merge: Any
    assignee: Optional["GitLabUser"]
    author: Optional["GitLabUser"]
    changes_count: Optional[str]
    closed_at: Optional[str]
    closed_by: Optional["GitLabUser"]
    created_at: Optional[str]
    description: Optional[str]
    diff_refs: Optional["GitLabMRDiffRefs"]
    discussion_locked: Any
    diverged_commits_count: Optional[int]
    downvotes: Optional[int]
    first_deployed_to_production_at: Optional[str]
    force_remove_source_branch: Optional[bool]
    id: Optional[int]
    iid: Optional[int]
    labels: Optional[List[str]]
    latest_build_finished_at: Optional[str]
    latest_build_started_at: Optional[str]
    merge_commit_sha: Optional[str]
    merge_error: Any
    merge_status: Optional["GitLabMRMergeStatus"]
    merge_when_pipeline_succeeds: Optional[bool]
    merged_at: Optional[str]
    merged_by: Optional["GitLabUser"]
    milestone: Optional["GitLabMRMilestone"]
    pipeline: Optional["GitLabMRPipeline"]
    project_id: Optional[int]
    rebase_in_progress: Optional[bool]
    sha: Optional[str]
    should_remove_source_branch: Optional[bool]
    source_branch: Optional[str]
    source_project_id: Optional[int]
    squash: Optional[bool]
    state: Optional["GitLabMRState"]
    subscribed: Optional[bool]
    target_branch: Optional[str]
    target_project_id: Optional[int]
    time_stats: Optional["GitLabMRTimeStats"]
    title: Optional[str]
    updated_at: Optional[str]
    upvotes: Optional[int]
    user: Optional["GitLabMRUser"]
    user_notes_count: Optional[int]
    web_url: Optional[str]
    work_in_progress: Optional[bool]

    class Config:
        fields = {
            "allow_collaboration": "allow_collaboration",
            "allow_maintainer_to_push": "allow_maintainer_to_push",
            "approvals_before_merge": "approvals_before_merge",
            "assignee": "assignee",
            "author": "author",
            "changes_count": "changes_count",
            "closed_at": "closed_at",
            "closed_by": "closed_by",
            "created_at": "created_at",
            "description": "description",
            "diff_refs": "diff_refs",
            "discussion_locked": "discussion_locked",
            "diverged_commits_count": "diverged_commits_count",
            "downvotes": "downvotes",
            "first_deployed_to_production_at": "first_deployed_to_production_at",
            "force_remove_source_branch": "force_remove_source_branch",
            "id": "id",
            "iid": "iid",
            "labels": "labels",
            "latest_build_finished_at": "latest_build_finished_at",
            "latest_build_started_at": "latest_build_started_at",
            "merge_commit_sha": "merge_commit_sha",
            "merge_error": "merge_error",
            "merge_status": "merge_status",
            "merge_when_pipeline_succeeds": "merge_when_pipeline_succeeds",
            "merged_at": "merged_at",
            "merged_by": "merged_by",
            "milestone": "milestone",
            "pipeline": "pipeline",
            "project_id": "project_id",
            "rebase_in_progress": "rebase_in_progress",
            "sha": "sha",
            "should_remove_source_branch": "should_remove_source_branch",
            "source_branch": "source_branch",
            "source_project_id": "source_project_id",
            "squash": "squash",
            "state": "state",
            "subscribed": "subscribed",
            "target_branch": "target_branch",
            "target_project_id": "target_project_id",
            "time_stats": "time_stats",
            "title": "title",
            "updated_at": "updated_at",
            "upvotes": "upvotes",
            "user": "user",
            "user_notes_count": "user_notes_count",
            "web_url": "web_url",
            "work_in_progress": "work_in_progress",
        }


class GitLabMRCommit(BaseModel):
    author_email: Optional[str]
    author_name: Optional[str]
    authored_date: Optional[str]
    committed_date: Optional[str]
    committer_email: Optional[str]
    committer_name: Optional[str]
    created_at: Optional[str]
    id: Optional[str]
    message: Optional[str]
    parent_ids: Optional[List[str]]
    short_id: Optional[str]
    title: Optional[str]

    class Config:
        fields = {
            "author_email": "author_email",
            "author_name": "author_name",
            "authored_date": "authored_date",
            "committed_date": "committed_date",
            "committer_email": "committer_email",
            "committer_name": "committer_name",
            "created_at": "created_at",
            "id": "id",
            "message": "message",
            "parent_ids": "parent_ids",
            "short_id": "short_id",
            "title": "title",
        }


class GitLabMRDiffRefs(BaseModel):
    base_sha: Optional[str]
    head_sha: Optional[str]
    start_sha: Optional[str]

    class Config:
        fields = {
            "base_sha": "base_sha",
            "head_sha": "head_sha",
            "start_sha": "start_sha",
        }


class GitLabMRMergeStatus(Enum):
    CAN_BE_MERGED = "can_be_merged"


class GitLabMRMilestone(BaseModel):
    created_at: Optional[str]
    description: Optional[str]
    due_date: Optional[str]
    id: Optional[int]
    iid: Optional[int]
    project_id: Optional[int]
    start_date: Optional[str]
    state: Optional["GitLabMRMilestoneState"]
    title: Optional[str]
    updated_at: Optional[str]
    web_url: Optional[str]

    class Config:
        fields = {
            "created_at": "created_at",
            "description": "description",
            "due_date": "due_date",
            "id": "id",
            "iid": "iid",
            "project_id": "project_id",
            "start_date": "start_date",
            "state": "state",
            "title": "title",
            "updated_at": "updated_at",
            "web_url": "web_url",
        }


class GitLabMRMilestoneState(Enum):
    ACTIVE = "active"
    CLOSED = "closed"


class GitLabMRPipeline(BaseModel):
    id: Optional[int]
    ref: Optional[str]
    sha: Optional[str]
    status: Optional["GitLabMRPipelineStatus"]
    web_url: Optional[str]

    class Config:
        fields = {
            "id": "id",
            "ref": "ref",
            "sha": "sha",
            "status": "status",
            "web_url": "web_url",
        }


class GitLabMRPipelineStatus(Enum):
    CANCELED = "canceled"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SKIPPED = "skipped"
    SUCCESS = "success"


class GitLabMRState(Enum):
    CLOSED = "closed"
    LOCKED = "locked"
    MERGED = "merged"
    OPEN = "open"


class GitLabMRTimeStats(BaseModel):
    human_time_estimate: Optional[int]
    human_total_time_spent: Optional[int]
    time_estimate: Optional[int]
    total_time_spent: Optional[int]

    class Config:
        fields = {
            "human_time_estimate": "human_time_estimate",
            "human_total_time_spent": "human_total_time_spent",
            "time_estimate": "time_estimate",
            "total_time_spent": "total_time_spent",
        }


class GitLabMRUser(BaseModel):
    can_merge: Optional[bool]

    class Config:
        fields = {
            "can_merge": "can_merge",
        }


class GitLabUser(BaseModel):
    avatar_url: Optional[str]
    id: Optional[int]
    name: Optional[str]
    state: Optional["GitLabUserState"]
    username: Optional[str]
    web_url: Optional[str]

    class Config:
        fields = {
            "avatar_url": "avatar_url",
            "id": "id",
            "name": "name",
            "state": "state",
            "username": "username",
            "web_url": "web_url",
        }


class GitLabUserState(Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"


class JIRAIssue(BaseModel):
    key: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "key": "key",
            "url": "url",
        }


class Log(BaseModel):
    debug: Optional["LogDebug"]
    error: Optional["LogError"]
    info: Optional["LogInfo"]
    warn: Optional["LogWarn"]

    class Config:
        fields = {
            "debug": "debug",
            "error": "error",
            "info": "info",
            "warn": "warn",
        }


class LogDebug(BaseModel):
    pass


class LogError(BaseModel):
    pass


class LogInfo(BaseModel):
    pass


class LogWarn(BaseModel):
    pass


class Octokit(BaseModel):
    activity: Optional["OctokitActivity"]
    apps: Optional["OctokitApps"]
    checks: Optional["OctokitChecks"]
    codes_of_conduct: Optional["OctokitCodesOfConduct"]
    emojis: Optional["OctokitEmojis"]
    gists: Optional["OctokitGists"]
    git: Optional["OctokitGit"]
    gitignore: Optional["OctokitGitignore"]
    hook: Optional["OctokitHook"]
    interactions: Optional["OctokitInteractions"]
    issues: Optional["OctokitIssues"]
    licenses: Optional["OctokitLicenses"]
    log: Optional["Log"]
    markdown: Optional["OctokitMarkdown"]
    meta: Optional["OctokitMeta"]
    migrations: Optional["OctokitMigrations"]
    oauth_authorizations: Optional["OctokitOauthAuthorizations"]
    orgs: Optional["OctokitOrgs"]
    paginate: Optional["Paginate"]
    projects: Optional["OctokitProjects"]
    pulls: Optional["OctokitPulls"]
    rate_limit: Optional["OctokitRateLimit"]
    reactions: Optional["OctokitReactions"]
    repos: Optional["OctokitRepos"]
    request: Optional["Request"]
    search: Optional["OctokitSearch"]
    teams: Optional["OctokitTeams"]
    users: Optional["OctokitUsers"]

    class Config:
        fields = {
            "activity": "activity",
            "apps": "apps",
            "checks": "checks",
            "codes_of_conduct": "codesOfConduct",
            "emojis": "emojis",
            "gists": "gists",
            "git": "git",
            "gitignore": "gitignore",
            "hook": "hook",
            "interactions": "interactions",
            "issues": "issues",
            "licenses": "licenses",
            "log": "log",
            "markdown": "markdown",
            "meta": "meta",
            "migrations": "migrations",
            "oauth_authorizations": "oauthAuthorizations",
            "orgs": "orgs",
            "paginate": "paginate",
            "projects": "projects",
            "pulls": "pulls",
            "rate_limit": "rateLimit",
            "reactions": "reactions",
            "repos": "repos",
            "request": "request",
            "search": "search",
            "teams": "teams",
            "users": "users",
        }


class OctokitActivity(BaseModel):
    check_starring_repo: Optional["OctokitActivityCheckStarringRepo"]
    delete_repo_subscription: Optional["OctokitActivityDeleteRepoSubscription"]
    delete_thread_subscription: Optional["OctokitActivityDeleteThreadSubscription"]
    get_repo_subscription: Optional["OctokitActivityGetRepoSubscription"]
    get_thread: Optional["OctokitActivityGetThread"]
    get_thread_subscription: Optional["OctokitActivityGetThreadSubscription"]
    list_events_for_org: Optional["OctokitActivityListEventsForOrg"]
    list_events_for_user: Optional["OctokitActivityListEventsForUser"]
    list_feeds: Optional["OctokitActivityListFeeds"]
    list_notifications: Optional["OctokitActivityListNotifications"]
    list_notifications_for_repo: Optional["OctokitActivityListNotificationsForRepo"]
    list_public_events: Optional["OctokitActivityListPublicEvents"]
    list_public_events_for_org: Optional["OctokitActivityListPublicEventsForOrg"]
    list_public_events_for_repo_network: Optional[
        "OctokitActivityListPublicEventsForRepoNetwork"
    ]
    list_public_events_for_user: Optional["OctokitActivityListPublicEventsForUser"]
    list_received_events_for_user: Optional["OctokitActivityListReceivedEventsForUser"]
    list_received_public_events_for_user: Optional[
        "OctokitActivityListReceivedPublicEventsForUser"
    ]
    list_repo_events: Optional["OctokitActivityListRepoEvents"]
    list_repos_starred_by_authenticated_user: Optional[
        "OctokitActivityListReposStarredByAuthenticatedUser"
    ]
    list_repos_starred_by_user: Optional["OctokitActivityListReposStarredByUser"]
    list_repos_watched_by_user: Optional["OctokitActivityListReposWatchedByUser"]
    list_stargazers_for_repo: Optional["OctokitActivityListStargazersForRepo"]
    list_watched_repos_for_authenticated_user: Optional[
        "OctokitActivityListWatchedReposForAuthenticatedUser"
    ]
    list_watchers_for_repo: Optional["OctokitActivityListWatchersForRepo"]
    mark_as_read: Optional["OctokitActivityMarkAsRead"]
    mark_notifications_as_read_for_repo: Optional[
        "OctokitActivityMarkNotificationsAsReadForRepo"
    ]
    mark_thread_as_read: Optional["OctokitActivityMarkThreadAsRead"]
    set_repo_subscription: Optional["OctokitActivitySetRepoSubscription"]
    set_thread_subscription: Optional["OctokitActivitySetThreadSubscription"]
    star_repo: Optional["OctokitActivityStarRepo"]
    unstar_repo: Optional["OctokitActivityUnstarRepo"]

    class Config:
        fields = {
            "check_starring_repo": "checkStarringRepo",
            "delete_repo_subscription": "deleteRepoSubscription",
            "delete_thread_subscription": "deleteThreadSubscription",
            "get_repo_subscription": "getRepoSubscription",
            "get_thread": "getThread",
            "get_thread_subscription": "getThreadSubscription",
            "list_events_for_org": "listEventsForOrg",
            "list_events_for_user": "listEventsForUser",
            "list_feeds": "listFeeds",
            "list_notifications": "listNotifications",
            "list_notifications_for_repo": "listNotificationsForRepo",
            "list_public_events": "listPublicEvents",
            "list_public_events_for_org": "listPublicEventsForOrg",
            "list_public_events_for_repo_network": "listPublicEventsForRepoNetwork",
            "list_public_events_for_user": "listPublicEventsForUser",
            "list_received_events_for_user": "listReceivedEventsForUser",
            "list_received_public_events_for_user": "listReceivedPublicEventsForUser",
            "list_repo_events": "listRepoEvents",
            "list_repos_starred_by_authenticated_user": "listReposStarredByAuthenticatedUser",
            "list_repos_starred_by_user": "listReposStarredByUser",
            "list_repos_watched_by_user": "listReposWatchedByUser",
            "list_stargazers_for_repo": "listStargazersForRepo",
            "list_watched_repos_for_authenticated_user": "listWatchedReposForAuthenticatedUser",
            "list_watchers_for_repo": "listWatchersForRepo",
            "mark_as_read": "markAsRead",
            "mark_notifications_as_read_for_repo": "markNotificationsAsReadForRepo",
            "mark_thread_as_read": "markThreadAsRead",
            "set_repo_subscription": "setRepoSubscription",
            "set_thread_subscription": "setThreadSubscription",
            "star_repo": "starRepo",
            "unstar_repo": "unstarRepo",
        }


class OctokitActivityCheckStarringRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityDeleteRepoSubscription(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityDeleteThreadSubscription(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityGetRepoSubscription(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityGetThread(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityGetThreadSubscription(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListEventsForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListEventsForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListFeeds(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListNotifications(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListNotificationsForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListPublicEvents(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListPublicEventsForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListPublicEventsForRepoNetwork(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListPublicEventsForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListReceivedEventsForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListReceivedPublicEventsForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListRepoEvents(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListReposStarredByAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListReposStarredByUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListReposWatchedByUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListStargazersForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListWatchedReposForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityListWatchersForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityMarkAsRead(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityMarkNotificationsAsReadForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityMarkThreadAsRead(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivitySetRepoSubscription(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivitySetThreadSubscription(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityStarRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitActivityUnstarRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitApps(BaseModel):
    add_repo_to_installation: Optional["OctokitAppsAddRepoToInstallation"]
    check_account_is_associated_with_any: Optional[
        "OctokitAppsCheckAccountIsAssociatedWithAny"
    ]
    check_account_is_associated_with_any_stubbed: Optional[
        "OctokitAppsCheckAccountIsAssociatedWithAnyStubbed"
    ]
    create_content_attachment: Optional["OctokitAppsCreateContentAttachment"]
    create_from_manifest: Optional["OctokitAppsCreateFromManifest"]
    create_installation_token: Optional["OctokitAppsCreateInstallationToken"]
    find_org_installation: Optional["OctokitAppsFindOrgInstallation"]
    find_repo_installation: Optional["OctokitAppsFindRepoInstallation"]
    find_user_installation: Optional["OctokitAppsFindUserInstallation"]
    get_authenticated: Optional["OctokitAppsGetAuthenticated"]
    get_by_slug: Optional["OctokitAppsGetBySlug"]
    get_installation: Optional["OctokitAppsGetInstallation"]
    list_accounts_user_or_org_on_plan: Optional[
        "OctokitAppsListAccountsUserOrOrgOnPlan"
    ]
    list_accounts_user_or_org_on_plan_stubbed: Optional[
        "OctokitAppsListAccountsUserOrOrgOnPlanStubbed"
    ]
    list_installation_repos_for_authenticated_user: Optional[
        "OctokitAppsListInstallationReposForAuthenticatedUser"
    ]
    list_installations: Optional["OctokitAppsListInstallations"]
    list_installations_for_authenticated_user: Optional[
        "OctokitAppsListInstallationsForAuthenticatedUser"
    ]
    list_marketplace_purchases_for_authenticated_user: Optional[
        "OctokitAppsListMarketplacePurchasesForAuthenticatedUser"
    ]
    list_marketplace_purchases_for_authenticated_user_stubbed: Optional[
        "OctokitAppsListMarketplacePurchasesForAuthenticatedUserStubbed"
    ]
    list_plans: Optional["OctokitAppsListPlans"]
    list_plans_stubbed: Optional["OctokitAppsListPlansStubbed"]
    list_repos: Optional["OctokitAppsListRepos"]
    remove_repo_from_installation: Optional["OctokitAppsRemoveRepoFromInstallation"]

    class Config:
        fields = {
            "add_repo_to_installation": "addRepoToInstallation",
            "check_account_is_associated_with_any": "checkAccountIsAssociatedWithAny",
            "check_account_is_associated_with_any_stubbed": "checkAccountIsAssociatedWithAnyStubbed",
            "create_content_attachment": "createContentAttachment",
            "create_from_manifest": "createFromManifest",
            "create_installation_token": "createInstallationToken",
            "find_org_installation": "findOrgInstallation",
            "find_repo_installation": "findRepoInstallation",
            "find_user_installation": "findUserInstallation",
            "get_authenticated": "getAuthenticated",
            "get_by_slug": "getBySlug",
            "get_installation": "getInstallation",
            "list_accounts_user_or_org_on_plan": "listAccountsUserOrOrgOnPlan",
            "list_accounts_user_or_org_on_plan_stubbed": "listAccountsUserOrOrgOnPlanStubbed",
            "list_installation_repos_for_authenticated_user": "listInstallationReposForAuthenticatedUser",
            "list_installations": "listInstallations",
            "list_installations_for_authenticated_user": "listInstallationsForAuthenticatedUser",
            "list_marketplace_purchases_for_authenticated_user": "listMarketplacePurchasesForAuthenticatedUser",
            "list_marketplace_purchases_for_authenticated_user_stubbed": "listMarketplacePurchasesForAuthenticatedUserStubbed",
            "list_plans": "listPlans",
            "list_plans_stubbed": "listPlansStubbed",
            "list_repos": "listRepos",
            "remove_repo_from_installation": "removeRepoFromInstallation",
        }


class OctokitAppsAddRepoToInstallation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsCheckAccountIsAssociatedWithAny(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsCheckAccountIsAssociatedWithAnyStubbed(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsCreateContentAttachment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsCreateFromManifest(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsCreateInstallationToken(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsFindOrgInstallation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsFindRepoInstallation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsFindUserInstallation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsGetAuthenticated(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsGetBySlug(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsGetInstallation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListAccountsUserOrOrgOnPlan(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListAccountsUserOrOrgOnPlanStubbed(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListInstallationReposForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListInstallations(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListInstallationsForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListMarketplacePurchasesForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListMarketplacePurchasesForAuthenticatedUserStubbed(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListPlans(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListPlansStubbed(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsListRepos(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitAppsRemoveRepoFromInstallation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecks(BaseModel):
    create: Optional["OctokitChecksCreate"]
    create_suite: Optional["OctokitChecksCreateSuite"]
    get: Optional["OctokitChecksGet"]
    get_suite: Optional["OctokitChecksGetSuite"]
    list_annotations: Optional["OctokitChecksListAnnotations"]
    list_for_ref: Optional["OctokitChecksListForRef"]
    list_for_suite: Optional["OctokitChecksListForSuite"]
    list_suites_for_ref: Optional["OctokitChecksListSuitesForRef"]
    rerequest_suite: Optional["OctokitChecksRerequestSuite"]
    set_suites_preferences: Optional["OctokitChecksSetSuitesPreferences"]
    update: Optional["OctokitChecksUpdate"]

    class Config:
        fields = {
            "create": "create",
            "create_suite": "createSuite",
            "get": "get",
            "get_suite": "getSuite",
            "list_annotations": "listAnnotations",
            "list_for_ref": "listForRef",
            "list_for_suite": "listForSuite",
            "list_suites_for_ref": "listSuitesForRef",
            "rerequest_suite": "rerequestSuite",
            "set_suites_preferences": "setSuitesPreferences",
            "update": "update",
        }


class OctokitChecksCreate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksCreateSuite(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksGetSuite(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksListAnnotations(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksListForRef(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksListForSuite(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksListSuitesForRef(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksRerequestSuite(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksSetSuitesPreferences(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitChecksUpdate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitCodesOfConduct(BaseModel):
    get_conduct_code: Optional["OctokitCodesOfConductGetConductCode"]
    get_for_repo: Optional["OctokitCodesOfConductGetForRepo"]
    list_conduct_codes: Optional["OctokitCodesOfConductListConductCodes"]

    class Config:
        fields = {
            "get_conduct_code": "getConductCode",
            "get_for_repo": "getForRepo",
            "list_conduct_codes": "listConductCodes",
        }


class OctokitCodesOfConductGetConductCode(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitCodesOfConductGetForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitCodesOfConductListConductCodes(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitEmojis(BaseModel):
    get: Optional["OctokitEmojisGet"]

    class Config:
        fields = {
            "get": "get",
        }


class OctokitEmojisGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGists(BaseModel):
    check_is_starred: Optional["OctokitGistsCheckIsStarred"]
    create: Optional["OctokitGistsCreate"]
    create_comment: Optional["OctokitGistsCreateComment"]
    delete: Optional["OctokitGistsDelete"]
    delete_comment: Optional["OctokitGistsDeleteComment"]
    fork: Optional["OctokitGistsFork"]
    get: Optional["OctokitGistsGet"]
    get_comment: Optional["OctokitGistsGetComment"]
    get_revision: Optional["OctokitGistsGetRevision"]
    list: Optional["OctokitGistsList"]
    list_comments: Optional["OctokitGistsListComments"]
    list_commits: Optional["OctokitGistsListCommits"]
    list_forks: Optional["OctokitGistsListForks"]
    list_public: Optional["OctokitGistsListPublic"]
    list_public_for_user: Optional["OctokitGistsListPublicForUser"]
    list_starred: Optional["OctokitGistsListStarred"]
    star: Optional["OctokitGistsStar"]
    unstar: Optional["OctokitGistsUnstar"]
    update: Optional["OctokitGistsUpdate"]
    update_comment: Optional["OctokitGistsUpdateComment"]

    class Config:
        fields = {
            "check_is_starred": "checkIsStarred",
            "create": "create",
            "create_comment": "createComment",
            "delete": "delete",
            "delete_comment": "deleteComment",
            "fork": "fork",
            "get": "get",
            "get_comment": "getComment",
            "get_revision": "getRevision",
            "list": "list",
            "list_comments": "listComments",
            "list_commits": "listCommits",
            "list_forks": "listForks",
            "list_public": "listPublic",
            "list_public_for_user": "listPublicForUser",
            "list_starred": "listStarred",
            "star": "star",
            "unstar": "unstar",
            "update": "update",
            "update_comment": "updateComment",
        }


class OctokitGistsCheckIsStarred(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsCreate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsCreateComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsDelete(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsDeleteComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsFork(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsGetComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsGetRevision(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsList(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsListComments(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsListCommits(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsListForks(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsListPublic(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsListPublicForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsListStarred(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsStar(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsUnstar(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsUpdate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGistsUpdateComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGit(BaseModel):
    create_blob: Optional["OctokitGitCreateBlob"]
    create_commit: Optional["OctokitGitCreateCommit"]
    create_ref: Optional["OctokitGitCreateRef"]
    create_tag: Optional["OctokitGitCreateTag"]
    create_tree: Optional["OctokitGitCreateTree"]
    delete_ref: Optional["OctokitGitDeleteRef"]
    get_blob: Optional["OctokitGitGetBlob"]
    get_commit: Optional["OctokitGitGetCommit"]
    get_ref: Optional["OctokitGitGetRef"]
    get_tag: Optional["OctokitGitGetTag"]
    get_tree: Optional["OctokitGitGetTree"]
    list_refs: Optional["OctokitGitListRefs"]
    update_ref: Optional["OctokitGitUpdateRef"]

    class Config:
        fields = {
            "create_blob": "createBlob",
            "create_commit": "createCommit",
            "create_ref": "createRef",
            "create_tag": "createTag",
            "create_tree": "createTree",
            "delete_ref": "deleteRef",
            "get_blob": "getBlob",
            "get_commit": "getCommit",
            "get_ref": "getRef",
            "get_tag": "getTag",
            "get_tree": "getTree",
            "list_refs": "listRefs",
            "update_ref": "updateRef",
        }


class OctokitGitCreateBlob(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitCreateCommit(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitCreateRef(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitCreateTag(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitCreateTree(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitDeleteRef(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitGetBlob(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitGetCommit(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitGetRef(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitGetTag(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitGetTree(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitListRefs(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitUpdateRef(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitignore(BaseModel):
    get_template: Optional["OctokitGitignoreGetTemplate"]
    list_templates: Optional["OctokitGitignoreListTemplates"]

    class Config:
        fields = {
            "get_template": "getTemplate",
            "list_templates": "listTemplates",
        }


class OctokitGitignoreGetTemplate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitGitignoreListTemplates(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitHook(BaseModel):
    pass


class OctokitInteractions(BaseModel):
    add_or_update_restrictions_for_org: Optional[
        "OctokitInteractionsAddOrUpdateRestrictionsForOrg"
    ]
    add_or_update_restrictions_for_repo: Optional[
        "OctokitInteractionsAddOrUpdateRestrictionsForRepo"
    ]
    get_restrictions_for_org: Optional["OctokitInteractionsGetRestrictionsForOrg"]
    get_restrictions_for_repo: Optional["OctokitInteractionsGetRestrictionsForRepo"]
    remove_restrictions_for_org: Optional["OctokitInteractionsRemoveRestrictionsForOrg"]
    remove_restrictions_for_repo: Optional[
        "OctokitInteractionsRemoveRestrictionsForRepo"
    ]

    class Config:
        fields = {
            "add_or_update_restrictions_for_org": "addOrUpdateRestrictionsForOrg",
            "add_or_update_restrictions_for_repo": "addOrUpdateRestrictionsForRepo",
            "get_restrictions_for_org": "getRestrictionsForOrg",
            "get_restrictions_for_repo": "getRestrictionsForRepo",
            "remove_restrictions_for_org": "removeRestrictionsForOrg",
            "remove_restrictions_for_repo": "removeRestrictionsForRepo",
        }


class OctokitInteractionsAddOrUpdateRestrictionsForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitInteractionsAddOrUpdateRestrictionsForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitInteractionsGetRestrictionsForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitInteractionsGetRestrictionsForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitInteractionsRemoveRestrictionsForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitInteractionsRemoveRestrictionsForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssues(BaseModel):
    add_assignees: Optional["OctokitIssuesAddAssignees"]
    add_labels: Optional["OctokitIssuesAddLabels"]
    check_assignee: Optional["OctokitIssuesCheckAssignee"]
    create: Optional["OctokitIssuesCreate"]
    create_comment: Optional["OctokitIssuesCreateComment"]
    create_label: Optional["OctokitIssuesCreateLabel"]
    create_milestone: Optional["OctokitIssuesCreateMilestone"]
    delete_comment: Optional["OctokitIssuesDeleteComment"]
    delete_label: Optional["OctokitIssuesDeleteLabel"]
    delete_milestone: Optional["OctokitIssuesDeleteMilestone"]
    get: Optional["OctokitIssuesGet"]
    get_comment: Optional["OctokitIssuesGetComment"]
    get_event: Optional["OctokitIssuesGetEvent"]
    get_label: Optional["OctokitIssuesGetLabel"]
    get_milestone: Optional["OctokitIssuesGetMilestone"]
    list: Optional["OctokitIssuesList"]
    list_assignees: Optional["OctokitIssuesListAssignees"]
    list_comments: Optional["OctokitIssuesListComments"]
    list_comments_for_repo: Optional["OctokitIssuesListCommentsForRepo"]
    list_events: Optional["OctokitIssuesListEvents"]
    list_events_for_repo: Optional["OctokitIssuesListEventsForRepo"]
    list_events_for_timeline: Optional["OctokitIssuesListEventsForTimeline"]
    list_for_authenticated_user: Optional["OctokitIssuesListForAuthenticatedUser"]
    list_for_org: Optional["OctokitIssuesListForOrg"]
    list_for_repo: Optional["OctokitIssuesListForRepo"]
    list_labels_for_milestone: Optional["OctokitIssuesListLabelsForMilestone"]
    list_labels_for_repo: Optional["OctokitIssuesListLabelsForRepo"]
    list_labels_on_issue: Optional["OctokitIssuesListLabelsOnIssue"]
    list_milestones_for_repo: Optional["OctokitIssuesListMilestonesForRepo"]
    lock: Optional["OctokitIssuesLock"]
    remove_assignees: Optional["OctokitIssuesRemoveAssignees"]
    remove_label: Optional["OctokitIssuesRemoveLabel"]
    remove_labels: Optional["OctokitIssuesRemoveLabels"]
    replace_labels: Optional["OctokitIssuesReplaceLabels"]
    unlock: Optional["OctokitIssuesUnlock"]
    update: Optional["OctokitIssuesUpdate"]
    update_comment: Optional["OctokitIssuesUpdateComment"]
    update_label: Optional["OctokitIssuesUpdateLabel"]
    update_milestone: Optional["OctokitIssuesUpdateMilestone"]

    class Config:
        fields = {
            "add_assignees": "addAssignees",
            "add_labels": "addLabels",
            "check_assignee": "checkAssignee",
            "create": "create",
            "create_comment": "createComment",
            "create_label": "createLabel",
            "create_milestone": "createMilestone",
            "delete_comment": "deleteComment",
            "delete_label": "deleteLabel",
            "delete_milestone": "deleteMilestone",
            "get": "get",
            "get_comment": "getComment",
            "get_event": "getEvent",
            "get_label": "getLabel",
            "get_milestone": "getMilestone",
            "list": "list",
            "list_assignees": "listAssignees",
            "list_comments": "listComments",
            "list_comments_for_repo": "listCommentsForRepo",
            "list_events": "listEvents",
            "list_events_for_repo": "listEventsForRepo",
            "list_events_for_timeline": "listEventsForTimeline",
            "list_for_authenticated_user": "listForAuthenticatedUser",
            "list_for_org": "listForOrg",
            "list_for_repo": "listForRepo",
            "list_labels_for_milestone": "listLabelsForMilestone",
            "list_labels_for_repo": "listLabelsForRepo",
            "list_labels_on_issue": "listLabelsOnIssue",
            "list_milestones_for_repo": "listMilestonesForRepo",
            "lock": "lock",
            "remove_assignees": "removeAssignees",
            "remove_label": "removeLabel",
            "remove_labels": "removeLabels",
            "replace_labels": "replaceLabels",
            "unlock": "unlock",
            "update": "update",
            "update_comment": "updateComment",
            "update_label": "updateLabel",
            "update_milestone": "updateMilestone",
        }


class OctokitIssuesAddAssignees(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesAddLabels(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesCheckAssignee(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesCreate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesCreateComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesCreateLabel(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesCreateMilestone(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesDeleteComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesDeleteLabel(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesDeleteMilestone(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesGetComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesGetEvent(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesGetLabel(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesGetMilestone(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesList(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListAssignees(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListComments(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListCommentsForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListEvents(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListEventsForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListEventsForTimeline(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListLabelsForMilestone(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListLabelsForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListLabelsOnIssue(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesListMilestonesForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesLock(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesRemoveAssignees(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesRemoveLabel(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesRemoveLabels(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesReplaceLabels(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesUnlock(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesUpdate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesUpdateComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesUpdateLabel(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitIssuesUpdateMilestone(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitLicenses(BaseModel):
    get: Optional["OctokitLicensesGet"]
    get_for_repo: Optional["OctokitLicensesGetForRepo"]
    list: Optional["OctokitLicensesList"]

    class Config:
        fields = {
            "get": "get",
            "get_for_repo": "getForRepo",
            "list": "list",
        }


class OctokitLicensesGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitLicensesGetForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitLicensesList(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMarkdown(BaseModel):
    render: Optional["OctokitMarkdownRender"]
    render_raw: Optional["OctokitMarkdownRenderRaw"]

    class Config:
        fields = {
            "render": "render",
            "render_raw": "renderRaw",
        }


class OctokitMarkdownRender(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMarkdownRenderRaw(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMeta(BaseModel):
    get: Optional["OctokitMetaGet"]

    class Config:
        fields = {
            "get": "get",
        }


class OctokitMetaGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrations(BaseModel):
    cancel_import: Optional["OctokitMigrationsCancelImport"]
    delete_archive_for_authenticated_user: Optional[
        "OctokitMigrationsDeleteArchiveForAuthenticatedUser"
    ]
    delete_archive_for_org: Optional["OctokitMigrationsDeleteArchiveForOrg"]
    get_archive_for_authenticated_user: Optional[
        "OctokitMigrationsGetArchiveForAuthenticatedUser"
    ]
    get_archive_for_org: Optional["OctokitMigrationsGetArchiveForOrg"]
    get_commit_authors: Optional["OctokitMigrationsGetCommitAuthors"]
    get_import_progress: Optional["OctokitMigrationsGetImportProgress"]
    get_large_files: Optional["OctokitMigrationsGetLargeFiles"]
    get_status_for_authenticated_user: Optional[
        "OctokitMigrationsGetStatusForAuthenticatedUser"
    ]
    get_status_for_org: Optional["OctokitMigrationsGetStatusForOrg"]
    list_for_authenticated_user: Optional["OctokitMigrationsListForAuthenticatedUser"]
    list_for_org: Optional["OctokitMigrationsListForOrg"]
    map_commit_author: Optional["OctokitMigrationsMapCommitAuthor"]
    set_lfs_preference: Optional["OctokitMigrationsSetLfsPreference"]
    start_for_authenticated_user: Optional["OctokitMigrationsStartForAuthenticatedUser"]
    start_for_org: Optional["OctokitMigrationsStartForOrg"]
    start_import: Optional["OctokitMigrationsStartImport"]
    unlock_repo_for_authenticated_user: Optional[
        "OctokitMigrationsUnlockRepoForAuthenticatedUser"
    ]
    unlock_repo_for_org: Optional["OctokitMigrationsUnlockRepoForOrg"]
    update_import: Optional["OctokitMigrationsUpdateImport"]

    class Config:
        fields = {
            "cancel_import": "cancelImport",
            "delete_archive_for_authenticated_user": "deleteArchiveForAuthenticatedUser",
            "delete_archive_for_org": "deleteArchiveForOrg",
            "get_archive_for_authenticated_user": "getArchiveForAuthenticatedUser",
            "get_archive_for_org": "getArchiveForOrg",
            "get_commit_authors": "getCommitAuthors",
            "get_import_progress": "getImportProgress",
            "get_large_files": "getLargeFiles",
            "get_status_for_authenticated_user": "getStatusForAuthenticatedUser",
            "get_status_for_org": "getStatusForOrg",
            "list_for_authenticated_user": "listForAuthenticatedUser",
            "list_for_org": "listForOrg",
            "map_commit_author": "mapCommitAuthor",
            "set_lfs_preference": "setLfsPreference",
            "start_for_authenticated_user": "startForAuthenticatedUser",
            "start_for_org": "startForOrg",
            "start_import": "startImport",
            "unlock_repo_for_authenticated_user": "unlockRepoForAuthenticatedUser",
            "unlock_repo_for_org": "unlockRepoForOrg",
            "update_import": "updateImport",
        }


class OctokitMigrationsCancelImport(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsDeleteArchiveForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsDeleteArchiveForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsGetArchiveForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsGetArchiveForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsGetCommitAuthors(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsGetImportProgress(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsGetLargeFiles(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsGetStatusForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsGetStatusForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsListForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsListForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsMapCommitAuthor(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsSetLfsPreference(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsStartForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsStartForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsStartImport(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsUnlockRepoForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsUnlockRepoForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitMigrationsUpdateImport(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizations(BaseModel):
    check_authorization: Optional["OctokitOauthAuthorizationsCheckAuthorization"]
    create_authorization: Optional["OctokitOauthAuthorizationsCreateAuthorization"]
    delete_authorization: Optional["OctokitOauthAuthorizationsDeleteAuthorization"]
    delete_grant: Optional["OctokitOauthAuthorizationsDeleteGrant"]
    get_authorization: Optional["OctokitOauthAuthorizationsGetAuthorization"]
    get_grant: Optional["OctokitOauthAuthorizationsGetGrant"]
    get_or_create_authorization_for_app: Optional[
        "OctokitOauthAuthorizationsGetOrCreateAuthorizationForApp"
    ]
    get_or_create_authorization_for_app_and_fingerprint: Optional[
        "OctokitOauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint"
    ]
    get_or_create_authorization_for_app_fingerprint: Optional[
        "OctokitOauthAuthorizationsGetOrCreateAuthorizationForAppFingerprint"
    ]
    list_authorizations: Optional["OctokitOauthAuthorizationsListAuthorizations"]
    list_grants: Optional["OctokitOauthAuthorizationsListGrants"]
    reset_authorization: Optional["OctokitOauthAuthorizationsResetAuthorization"]
    revoke_authorization_for_application: Optional[
        "OctokitOauthAuthorizationsRevokeAuthorizationForApplication"
    ]
    revoke_grant_for_application: Optional[
        "OctokitOauthAuthorizationsRevokeGrantForApplication"
    ]
    update_authorization: Optional["OctokitOauthAuthorizationsUpdateAuthorization"]

    class Config:
        fields = {
            "check_authorization": "checkAuthorization",
            "create_authorization": "createAuthorization",
            "delete_authorization": "deleteAuthorization",
            "delete_grant": "deleteGrant",
            "get_authorization": "getAuthorization",
            "get_grant": "getGrant",
            "get_or_create_authorization_for_app": "getOrCreateAuthorizationForApp",
            "get_or_create_authorization_for_app_and_fingerprint": "getOrCreateAuthorizationForAppAndFingerprint",
            "get_or_create_authorization_for_app_fingerprint": "getOrCreateAuthorizationForAppFingerprint",
            "list_authorizations": "listAuthorizations",
            "list_grants": "listGrants",
            "reset_authorization": "resetAuthorization",
            "revoke_authorization_for_application": "revokeAuthorizationForApplication",
            "revoke_grant_for_application": "revokeGrantForApplication",
            "update_authorization": "updateAuthorization",
        }


class OctokitOauthAuthorizationsCheckAuthorization(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsCreateAuthorization(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsDeleteAuthorization(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsDeleteGrant(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsGetAuthorization(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsGetGrant(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsGetOrCreateAuthorizationForApp(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsGetOrCreateAuthorizationForAppFingerprint(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsListAuthorizations(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsListGrants(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsResetAuthorization(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsRevokeAuthorizationForApplication(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsRevokeGrantForApplication(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOauthAuthorizationsUpdateAuthorization(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgs(BaseModel):
    add_or_update_membership: Optional["OctokitOrgsAddOrUpdateMembership"]
    block_user: Optional["OctokitOrgsBlockUser"]
    check_blocked_user: Optional["OctokitOrgsCheckBlockedUser"]
    check_membership: Optional["OctokitOrgsCheckMembership"]
    check_public_membership: Optional["OctokitOrgsCheckPublicMembership"]
    conceal_membership: Optional["OctokitOrgsConcealMembership"]
    convert_member_to_outside_collaborator: Optional[
        "OctokitOrgsConvertMemberToOutsideCollaborator"
    ]
    create_hook: Optional["OctokitOrgsCreateHook"]
    create_invitation: Optional["OctokitOrgsCreateInvitation"]
    delete_hook: Optional["OctokitOrgsDeleteHook"]
    get: Optional["OctokitOrgsGet"]
    get_hook: Optional["OctokitOrgsGetHook"]
    get_membership: Optional["OctokitOrgsGetMembership"]
    get_membership_for_authenticated_user: Optional[
        "OctokitOrgsGetMembershipForAuthenticatedUser"
    ]
    list: Optional["OctokitOrgsList"]
    list_blocked_users: Optional["OctokitOrgsListBlockedUsers"]
    list_for_authenticated_user: Optional["OctokitOrgsListForAuthenticatedUser"]
    list_for_user: Optional["OctokitOrgsListForUser"]
    list_hooks: Optional["OctokitOrgsListHooks"]
    list_invitation_teams: Optional["OctokitOrgsListInvitationTeams"]
    list_members: Optional["OctokitOrgsListMembers"]
    list_memberships: Optional["OctokitOrgsListMemberships"]
    list_outside_collaborators: Optional["OctokitOrgsListOutsideCollaborators"]
    list_pending_invitations: Optional["OctokitOrgsListPendingInvitations"]
    list_public_members: Optional["OctokitOrgsListPublicMembers"]
    ping_hook: Optional["OctokitOrgsPingHook"]
    publicize_membership: Optional["OctokitOrgsPublicizeMembership"]
    remove_member: Optional["OctokitOrgsRemoveMember"]
    remove_membership: Optional["OctokitOrgsRemoveMembership"]
    remove_outside_collaborator: Optional["OctokitOrgsRemoveOutsideCollaborator"]
    unblock_user: Optional["OctokitOrgsUnblockUser"]
    update: Optional["OctokitOrgsUpdate"]
    update_hook: Optional["OctokitOrgsUpdateHook"]
    update_membership: Optional["OctokitOrgsUpdateMembership"]

    class Config:
        fields = {
            "add_or_update_membership": "addOrUpdateMembership",
            "block_user": "blockUser",
            "check_blocked_user": "checkBlockedUser",
            "check_membership": "checkMembership",
            "check_public_membership": "checkPublicMembership",
            "conceal_membership": "concealMembership",
            "convert_member_to_outside_collaborator": "convertMemberToOutsideCollaborator",
            "create_hook": "createHook",
            "create_invitation": "createInvitation",
            "delete_hook": "deleteHook",
            "get": "get",
            "get_hook": "getHook",
            "get_membership": "getMembership",
            "get_membership_for_authenticated_user": "getMembershipForAuthenticatedUser",
            "list": "list",
            "list_blocked_users": "listBlockedUsers",
            "list_for_authenticated_user": "listForAuthenticatedUser",
            "list_for_user": "listForUser",
            "list_hooks": "listHooks",
            "list_invitation_teams": "listInvitationTeams",
            "list_members": "listMembers",
            "list_memberships": "listMemberships",
            "list_outside_collaborators": "listOutsideCollaborators",
            "list_pending_invitations": "listPendingInvitations",
            "list_public_members": "listPublicMembers",
            "ping_hook": "pingHook",
            "publicize_membership": "publicizeMembership",
            "remove_member": "removeMember",
            "remove_membership": "removeMembership",
            "remove_outside_collaborator": "removeOutsideCollaborator",
            "unblock_user": "unblockUser",
            "update": "update",
            "update_hook": "updateHook",
            "update_membership": "updateMembership",
        }


class OctokitOrgsAddOrUpdateMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsBlockUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsCheckBlockedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsCheckMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsCheckPublicMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsConcealMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsConvertMemberToOutsideCollaborator(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsCreateHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsCreateInvitation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsDeleteHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsGetHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsGetMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsGetMembershipForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsList(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListBlockedUsers(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListHooks(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListInvitationTeams(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListMembers(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListMemberships(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListOutsideCollaborators(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListPendingInvitations(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsListPublicMembers(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsPingHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsPublicizeMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsRemoveMember(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsRemoveMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsRemoveOutsideCollaborator(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsUnblockUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsUpdate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsUpdateHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitOrgsUpdateMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjects(BaseModel):
    add_collaborator: Optional["OctokitProjectsAddCollaborator"]
    create_card: Optional["OctokitProjectsCreateCard"]
    create_column: Optional["OctokitProjectsCreateColumn"]
    create_for_org: Optional["OctokitProjectsCreateForOrg"]
    create_for_repo: Optional["OctokitProjectsCreateForRepo"]
    delete: Optional["OctokitProjectsDelete"]
    delete_card: Optional["OctokitProjectsDeleteCard"]
    delete_column: Optional["OctokitProjectsDeleteColumn"]
    get: Optional["OctokitProjectsGet"]
    get_card: Optional["OctokitProjectsGetCard"]
    get_column: Optional["OctokitProjectsGetColumn"]
    list_cards: Optional["OctokitProjectsListCards"]
    list_collaborators: Optional["OctokitProjectsListCollaborators"]
    list_columns: Optional["OctokitProjectsListColumns"]
    list_for_org: Optional["OctokitProjectsListForOrg"]
    list_for_repo: Optional["OctokitProjectsListForRepo"]
    move_card: Optional["OctokitProjectsMoveCard"]
    move_column: Optional["OctokitProjectsMoveColumn"]
    remove_collaborator: Optional["OctokitProjectsRemoveCollaborator"]
    review_user_permission_level: Optional["OctokitProjectsReviewUserPermissionLevel"]
    update: Optional["OctokitProjectsUpdate"]
    update_card: Optional["OctokitProjectsUpdateCard"]
    update_column: Optional["OctokitProjectsUpdateColumn"]

    class Config:
        fields = {
            "add_collaborator": "addCollaborator",
            "create_card": "createCard",
            "create_column": "createColumn",
            "create_for_org": "createForOrg",
            "create_for_repo": "createForRepo",
            "delete": "delete",
            "delete_card": "deleteCard",
            "delete_column": "deleteColumn",
            "get": "get",
            "get_card": "getCard",
            "get_column": "getColumn",
            "list_cards": "listCards",
            "list_collaborators": "listCollaborators",
            "list_columns": "listColumns",
            "list_for_org": "listForOrg",
            "list_for_repo": "listForRepo",
            "move_card": "moveCard",
            "move_column": "moveColumn",
            "remove_collaborator": "removeCollaborator",
            "review_user_permission_level": "reviewUserPermissionLevel",
            "update": "update",
            "update_card": "updateCard",
            "update_column": "updateColumn",
        }


class OctokitProjectsAddCollaborator(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsCreateCard(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsCreateColumn(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsCreateForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsCreateForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsDelete(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsDeleteCard(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsDeleteColumn(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsGetCard(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsGetColumn(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsListCards(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsListCollaborators(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsListColumns(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsListForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsListForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsMoveCard(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsMoveColumn(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsRemoveCollaborator(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsReviewUserPermissionLevel(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsUpdate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsUpdateCard(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitProjectsUpdateColumn(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPulls(BaseModel):
    check_if_merged: Optional["OctokitPullsCheckIfMerged"]
    create: Optional["OctokitPullsCreate"]
    create_comment: Optional["OctokitPullsCreateComment"]
    create_comment_reply: Optional["OctokitPullsCreateCommentReply"]
    create_from_issue: Optional["OctokitPullsCreateFromIssue"]
    create_review: Optional["OctokitPullsCreateReview"]
    create_review_request: Optional["OctokitPullsCreateReviewRequest"]
    delete_comment: Optional["OctokitPullsDeleteComment"]
    delete_pending_review: Optional["OctokitPullsDeletePendingReview"]
    delete_review_request: Optional["OctokitPullsDeleteReviewRequest"]
    dismiss_review: Optional["OctokitPullsDismissReview"]
    get: Optional["OctokitPullsGet"]
    get_comment: Optional["OctokitPullsGetComment"]
    get_comments_for_review: Optional["OctokitPullsGetCommentsForReview"]
    get_review: Optional["OctokitPullsGetReview"]
    list: Optional["OctokitPullsList"]
    list_comments: Optional["OctokitPullsListComments"]
    list_comments_for_repo: Optional["OctokitPullsListCommentsForRepo"]
    list_commits: Optional["OctokitPullsListCommits"]
    list_files: Optional["OctokitPullsListFiles"]
    list_review_requests: Optional["OctokitPullsListReviewRequests"]
    list_reviews: Optional["OctokitPullsListReviews"]
    merge: Optional["OctokitPullsMerge"]
    submit_review: Optional["OctokitPullsSubmitReview"]
    update: Optional["OctokitPullsUpdate"]
    update_comment: Optional["OctokitPullsUpdateComment"]
    update_review: Optional["OctokitPullsUpdateReview"]

    class Config:
        fields = {
            "check_if_merged": "checkIfMerged",
            "create": "create",
            "create_comment": "createComment",
            "create_comment_reply": "createCommentReply",
            "create_from_issue": "createFromIssue",
            "create_review": "createReview",
            "create_review_request": "createReviewRequest",
            "delete_comment": "deleteComment",
            "delete_pending_review": "deletePendingReview",
            "delete_review_request": "deleteReviewRequest",
            "dismiss_review": "dismissReview",
            "get": "get",
            "get_comment": "getComment",
            "get_comments_for_review": "getCommentsForReview",
            "get_review": "getReview",
            "list": "list",
            "list_comments": "listComments",
            "list_comments_for_repo": "listCommentsForRepo",
            "list_commits": "listCommits",
            "list_files": "listFiles",
            "list_review_requests": "listReviewRequests",
            "list_reviews": "listReviews",
            "merge": "merge",
            "submit_review": "submitReview",
            "update": "update",
            "update_comment": "updateComment",
            "update_review": "updateReview",
        }


class OctokitPullsCheckIfMerged(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsCreate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsCreateComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsCreateCommentReply(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsCreateFromIssue(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsCreateReview(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsCreateReviewRequest(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsDeleteComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsDeletePendingReview(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsDeleteReviewRequest(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsDismissReview(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsGetComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsGetCommentsForReview(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsGetReview(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsList(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsListComments(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsListCommentsForRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsListCommits(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsListFiles(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsListReviewRequests(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsListReviews(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsMerge(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsSubmitReview(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsUpdate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsUpdateComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitPullsUpdateReview(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitRateLimit(BaseModel):
    get: Optional["OctokitRateLimitGet"]

    class Config:
        fields = {
            "get": "get",
        }


class OctokitRateLimitGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactions(BaseModel):
    create_for_commit_comment: Optional["OctokitReactionsCreateForCommitComment"]
    create_for_issue: Optional["OctokitReactionsCreateForIssue"]
    create_for_issue_comment: Optional["OctokitReactionsCreateForIssueComment"]
    create_for_pull_request_review_comment: Optional[
        "OctokitReactionsCreateForPullRequestReviewComment"
    ]
    create_for_team_discussion: Optional["OctokitReactionsCreateForTeamDiscussion"]
    create_for_team_discussion_comment: Optional[
        "OctokitReactionsCreateForTeamDiscussionComment"
    ]
    delete: Optional["OctokitReactionsDelete"]
    list_for_commit_comment: Optional["OctokitReactionsListForCommitComment"]
    list_for_issue: Optional["OctokitReactionsListForIssue"]
    list_for_issue_comment: Optional["OctokitReactionsListForIssueComment"]
    list_for_pull_request_review_comment: Optional[
        "OctokitReactionsListForPullRequestReviewComment"
    ]
    list_for_team_discussion: Optional["OctokitReactionsListForTeamDiscussion"]
    list_for_team_discussion_comment: Optional[
        "OctokitReactionsListForTeamDiscussionComment"
    ]

    class Config:
        fields = {
            "create_for_commit_comment": "createForCommitComment",
            "create_for_issue": "createForIssue",
            "create_for_issue_comment": "createForIssueComment",
            "create_for_pull_request_review_comment": "createForPullRequestReviewComment",
            "create_for_team_discussion": "createForTeamDiscussion",
            "create_for_team_discussion_comment": "createForTeamDiscussionComment",
            "delete": "delete",
            "list_for_commit_comment": "listForCommitComment",
            "list_for_issue": "listForIssue",
            "list_for_issue_comment": "listForIssueComment",
            "list_for_pull_request_review_comment": "listForPullRequestReviewComment",
            "list_for_team_discussion": "listForTeamDiscussion",
            "list_for_team_discussion_comment": "listForTeamDiscussionComment",
        }


class OctokitReactionsCreateForCommitComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsCreateForIssue(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsCreateForIssueComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsCreateForPullRequestReviewComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsCreateForTeamDiscussion(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsCreateForTeamDiscussionComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsDelete(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsListForCommitComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsListForIssue(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsListForIssueComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsListForPullRequestReviewComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsListForTeamDiscussion(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReactionsListForTeamDiscussionComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitRepos(BaseModel):
    accept_invitation: Optional["OctokitReposAcceptInvitation"]
    add_collaborator: Optional["OctokitReposAddCollaborator"]
    add_deploy_key: Optional["OctokitReposAddDeployKey"]
    add_protected_branch_admin_enforcement: Optional[
        "OctokitReposAddProtectedBranchAdminEnforcement"
    ]
    add_protected_branch_required_signatures: Optional[
        "OctokitReposAddProtectedBranchRequiredSignatures"
    ]
    add_protected_branch_required_status_checks_contexts: Optional[
        "OctokitReposAddProtectedBranchRequiredStatusChecksContexts"
    ]
    add_protected_branch_team_restrictions: Optional[
        "OctokitReposAddProtectedBranchTeamRestrictions"
    ]
    add_protected_branch_user_restrictions: Optional[
        "OctokitReposAddProtectedBranchUserRestrictions"
    ]
    check_collaborator: Optional["OctokitReposCheckCollaborator"]
    compare_commits: Optional["OctokitReposCompareCommits"]
    create_commit_comment: Optional["OctokitReposCreateCommitComment"]
    create_deployment: Optional["OctokitReposCreateDeployment"]
    create_deployment_status: Optional["OctokitReposCreateDeploymentStatus"]
    create_file: Optional["OctokitReposCreateFile"]
    create_for_authenticated_user: Optional["OctokitReposCreateForAuthenticatedUser"]
    create_fork: Optional["OctokitReposCreateFork"]
    create_hook: Optional["OctokitReposCreateHook"]
    create_in_org: Optional["OctokitReposCreateInOrg"]
    create_release: Optional["OctokitReposCreateRelease"]
    create_status: Optional["OctokitReposCreateStatus"]
    decline_invitation: Optional["OctokitReposDeclineInvitation"]
    delete: Optional["OctokitReposDelete"]
    delete_commit_comment: Optional["OctokitReposDeleteCommitComment"]
    delete_download: Optional["OctokitReposDeleteDownload"]
    delete_file: Optional["OctokitReposDeleteFile"]
    delete_hook: Optional["OctokitReposDeleteHook"]
    delete_invitation: Optional["OctokitReposDeleteInvitation"]
    delete_release: Optional["OctokitReposDeleteRelease"]
    delete_release_asset: Optional["OctokitReposDeleteReleaseAsset"]
    get: Optional["OctokitReposGet"]
    get_archive_link: Optional["OctokitReposGetArchiveLink"]
    get_branch: Optional["OctokitReposGetBranch"]
    get_branch_protection: Optional["OctokitReposGetBranchProtection"]
    get_clones: Optional["OctokitReposGetClones"]
    get_code_frequency_stats: Optional["OctokitReposGetCodeFrequencyStats"]
    get_collaborator_permission_level: Optional[
        "OctokitReposGetCollaboratorPermissionLevel"
    ]
    get_combined_status_for_ref: Optional["OctokitReposGetCombinedStatusForRef"]
    get_commit: Optional["OctokitReposGetCommit"]
    get_commit_activity_stats: Optional["OctokitReposGetCommitActivityStats"]
    get_commit_comment: Optional["OctokitReposGetCommitComment"]
    get_commit_ref_sha: Optional["OctokitReposGetCommitRefSha"]
    get_contents: Optional["OctokitReposGetContents"]
    get_contributors_stats: Optional["OctokitReposGetContributorsStats"]
    get_deploy_key: Optional["OctokitReposGetDeployKey"]
    get_deployment: Optional["OctokitReposGetDeployment"]
    get_deployment_status: Optional["OctokitReposGetDeploymentStatus"]
    get_download: Optional["OctokitReposGetDownload"]
    get_hook: Optional["OctokitReposGetHook"]
    get_latest_pages_build: Optional["OctokitReposGetLatestPagesBuild"]
    get_latest_release: Optional["OctokitReposGetLatestRelease"]
    get_pages: Optional["OctokitReposGetPages"]
    get_pages_build: Optional["OctokitReposGetPagesBuild"]
    get_participation_stats: Optional["OctokitReposGetParticipationStats"]
    get_protected_branch_admin_enforcement: Optional[
        "OctokitReposGetProtectedBranchAdminEnforcement"
    ]
    get_protected_branch_pull_request_review_enforcement: Optional[
        "OctokitReposGetProtectedBranchPullRequestReviewEnforcement"
    ]
    get_protected_branch_required_signatures: Optional[
        "OctokitReposGetProtectedBranchRequiredSignatures"
    ]
    get_protected_branch_required_status_checks: Optional[
        "OctokitReposGetProtectedBranchRequiredStatusChecks"
    ]
    get_protected_branch_restrictions: Optional[
        "OctokitReposGetProtectedBranchRestrictions"
    ]
    get_punch_card_stats: Optional["OctokitReposGetPunchCardStats"]
    get_readme: Optional["OctokitReposGetReadme"]
    get_release: Optional["OctokitReposGetRelease"]
    get_release_asset: Optional["OctokitReposGetReleaseAsset"]
    get_release_by_tag: Optional["OctokitReposGetReleaseByTag"]
    get_top_paths: Optional["OctokitReposGetTopPaths"]
    get_top_referrers: Optional["OctokitReposGetTopReferrers"]
    get_views: Optional["OctokitReposGetViews"]
    list: Optional["OctokitReposList"]
    list_assets_for_release: Optional["OctokitReposListAssetsForRelease"]
    list_branches: Optional["OctokitReposListBranches"]
    list_collaborators: Optional["OctokitReposListCollaborators"]
    list_comments_for_commit: Optional["OctokitReposListCommentsForCommit"]
    list_commit_comments: Optional["OctokitReposListCommitComments"]
    list_commits: Optional["OctokitReposListCommits"]
    list_contributors: Optional["OctokitReposListContributors"]
    list_deploy_keys: Optional["OctokitReposListDeployKeys"]
    list_deployment_statuses: Optional["OctokitReposListDeploymentStatuses"]
    list_deployments: Optional["OctokitReposListDeployments"]
    list_downloads: Optional["OctokitReposListDownloads"]
    list_for_org: Optional["OctokitReposListForOrg"]
    list_for_user: Optional["OctokitReposListForUser"]
    list_forks: Optional["OctokitReposListForks"]
    list_hooks: Optional["OctokitReposListHooks"]
    list_invitations: Optional["OctokitReposListInvitations"]
    list_invitations_for_authenticated_user: Optional[
        "OctokitReposListInvitationsForAuthenticatedUser"
    ]
    list_languages: Optional["OctokitReposListLanguages"]
    list_pages_builds: Optional["OctokitReposListPagesBuilds"]
    list_protected_branch_required_status_checks_contexts: Optional[
        "OctokitReposListProtectedBranchRequiredStatusChecksContexts"
    ]
    list_protected_branch_team_restrictions: Optional[
        "OctokitReposListProtectedBranchTeamRestrictions"
    ]
    list_protected_branch_user_restrictions: Optional[
        "OctokitReposListProtectedBranchUserRestrictions"
    ]
    list_public: Optional["OctokitReposListPublic"]
    list_releases: Optional["OctokitReposListReleases"]
    list_statuses_for_ref: Optional["OctokitReposListStatusesForRef"]
    list_tags: Optional["OctokitReposListTags"]
    list_teams: Optional["OctokitReposListTeams"]
    list_topics: Optional["OctokitReposListTopics"]
    merge: Optional["OctokitReposMerge"]
    ping_hook: Optional["OctokitReposPingHook"]
    remove_branch_protection: Optional["OctokitReposRemoveBranchProtection"]
    remove_collaborator: Optional["OctokitReposRemoveCollaborator"]
    remove_deploy_key: Optional["OctokitReposRemoveDeployKey"]
    remove_protected_branch_admin_enforcement: Optional[
        "OctokitReposRemoveProtectedBranchAdminEnforcement"
    ]
    remove_protected_branch_pull_request_review_enforcement: Optional[
        "OctokitReposRemoveProtectedBranchPullRequestReviewEnforcement"
    ]
    remove_protected_branch_required_signatures: Optional[
        "OctokitReposRemoveProtectedBranchRequiredSignatures"
    ]
    remove_protected_branch_required_status_checks: Optional[
        "OctokitReposRemoveProtectedBranchRequiredStatusChecks"
    ]
    remove_protected_branch_required_status_checks_contexts: Optional[
        "OctokitReposRemoveProtectedBranchRequiredStatusChecksContexts"
    ]
    remove_protected_branch_restrictions: Optional[
        "OctokitReposRemoveProtectedBranchRestrictions"
    ]
    remove_protected_branch_team_restrictions: Optional[
        "OctokitReposRemoveProtectedBranchTeamRestrictions"
    ]
    remove_protected_branch_user_restrictions: Optional[
        "OctokitReposRemoveProtectedBranchUserRestrictions"
    ]
    replace_protected_branch_required_status_checks_contexts: Optional[
        "OctokitReposReplaceProtectedBranchRequiredStatusChecksContexts"
    ]
    replace_protected_branch_team_restrictions: Optional[
        "OctokitReposReplaceProtectedBranchTeamRestrictions"
    ]
    replace_protected_branch_user_restrictions: Optional[
        "OctokitReposReplaceProtectedBranchUserRestrictions"
    ]
    replace_topics: Optional["OctokitReposReplaceTopics"]
    request_page_build: Optional["OctokitReposRequestPageBuild"]
    retrieve_community_profile_metrics: Optional[
        "OctokitReposRetrieveCommunityProfileMetrics"
    ]
    test_push_hook: Optional["OctokitReposTestPushHook"]
    transfer: Optional["OctokitReposTransfer"]
    update: Optional["OctokitReposUpdate"]
    update_branch_protection: Optional["OctokitReposUpdateBranchProtection"]
    update_commit_comment: Optional["OctokitReposUpdateCommitComment"]
    update_file: Optional["OctokitReposUpdateFile"]
    update_hook: Optional["OctokitReposUpdateHook"]
    update_information_about_pages_site: Optional[
        "OctokitReposUpdateInformationAboutPagesSite"
    ]
    update_invitation: Optional["OctokitReposUpdateInvitation"]
    update_protected_branch_pull_request_review_enforcement: Optional[
        "OctokitReposUpdateProtectedBranchPullRequestReviewEnforcement"
    ]
    update_protected_branch_required_status_checks: Optional[
        "OctokitReposUpdateProtectedBranchRequiredStatusChecks"
    ]
    update_release: Optional["OctokitReposUpdateRelease"]
    update_release_asset: Optional["OctokitReposUpdateReleaseAsset"]
    upload_release_asset: Optional["OctokitReposUploadReleaseAsset"]

    class Config:
        fields = {
            "accept_invitation": "acceptInvitation",
            "add_collaborator": "addCollaborator",
            "add_deploy_key": "addDeployKey",
            "add_protected_branch_admin_enforcement": "addProtectedBranchAdminEnforcement",
            "add_protected_branch_required_signatures": "addProtectedBranchRequiredSignatures",
            "add_protected_branch_required_status_checks_contexts": "addProtectedBranchRequiredStatusChecksContexts",
            "add_protected_branch_team_restrictions": "addProtectedBranchTeamRestrictions",
            "add_protected_branch_user_restrictions": "addProtectedBranchUserRestrictions",
            "check_collaborator": "checkCollaborator",
            "compare_commits": "compareCommits",
            "create_commit_comment": "createCommitComment",
            "create_deployment": "createDeployment",
            "create_deployment_status": "createDeploymentStatus",
            "create_file": "createFile",
            "create_for_authenticated_user": "createForAuthenticatedUser",
            "create_fork": "createFork",
            "create_hook": "createHook",
            "create_in_org": "createInOrg",
            "create_release": "createRelease",
            "create_status": "createStatus",
            "decline_invitation": "declineInvitation",
            "delete": "delete",
            "delete_commit_comment": "deleteCommitComment",
            "delete_download": "deleteDownload",
            "delete_file": "deleteFile",
            "delete_hook": "deleteHook",
            "delete_invitation": "deleteInvitation",
            "delete_release": "deleteRelease",
            "delete_release_asset": "deleteReleaseAsset",
            "get": "get",
            "get_archive_link": "getArchiveLink",
            "get_branch": "getBranch",
            "get_branch_protection": "getBranchProtection",
            "get_clones": "getClones",
            "get_code_frequency_stats": "getCodeFrequencyStats",
            "get_collaborator_permission_level": "getCollaboratorPermissionLevel",
            "get_combined_status_for_ref": "getCombinedStatusForRef",
            "get_commit": "getCommit",
            "get_commit_activity_stats": "getCommitActivityStats",
            "get_commit_comment": "getCommitComment",
            "get_commit_ref_sha": "getCommitRefSha",
            "get_contents": "getContents",
            "get_contributors_stats": "getContributorsStats",
            "get_deploy_key": "getDeployKey",
            "get_deployment": "getDeployment",
            "get_deployment_status": "getDeploymentStatus",
            "get_download": "getDownload",
            "get_hook": "getHook",
            "get_latest_pages_build": "getLatestPagesBuild",
            "get_latest_release": "getLatestRelease",
            "get_pages": "getPages",
            "get_pages_build": "getPagesBuild",
            "get_participation_stats": "getParticipationStats",
            "get_protected_branch_admin_enforcement": "getProtectedBranchAdminEnforcement",
            "get_protected_branch_pull_request_review_enforcement": "getProtectedBranchPullRequestReviewEnforcement",
            "get_protected_branch_required_signatures": "getProtectedBranchRequiredSignatures",
            "get_protected_branch_required_status_checks": "getProtectedBranchRequiredStatusChecks",
            "get_protected_branch_restrictions": "getProtectedBranchRestrictions",
            "get_punch_card_stats": "getPunchCardStats",
            "get_readme": "getReadme",
            "get_release": "getRelease",
            "get_release_asset": "getReleaseAsset",
            "get_release_by_tag": "getReleaseByTag",
            "get_top_paths": "getTopPaths",
            "get_top_referrers": "getTopReferrers",
            "get_views": "getViews",
            "list": "list",
            "list_assets_for_release": "listAssetsForRelease",
            "list_branches": "listBranches",
            "list_collaborators": "listCollaborators",
            "list_comments_for_commit": "listCommentsForCommit",
            "list_commit_comments": "listCommitComments",
            "list_commits": "listCommits",
            "list_contributors": "listContributors",
            "list_deploy_keys": "listDeployKeys",
            "list_deployment_statuses": "listDeploymentStatuses",
            "list_deployments": "listDeployments",
            "list_downloads": "listDownloads",
            "list_for_org": "listForOrg",
            "list_for_user": "listForUser",
            "list_forks": "listForks",
            "list_hooks": "listHooks",
            "list_invitations": "listInvitations",
            "list_invitations_for_authenticated_user": "listInvitationsForAuthenticatedUser",
            "list_languages": "listLanguages",
            "list_pages_builds": "listPagesBuilds",
            "list_protected_branch_required_status_checks_contexts": "listProtectedBranchRequiredStatusChecksContexts",
            "list_protected_branch_team_restrictions": "listProtectedBranchTeamRestrictions",
            "list_protected_branch_user_restrictions": "listProtectedBranchUserRestrictions",
            "list_public": "listPublic",
            "list_releases": "listReleases",
            "list_statuses_for_ref": "listStatusesForRef",
            "list_tags": "listTags",
            "list_teams": "listTeams",
            "list_topics": "listTopics",
            "merge": "merge",
            "ping_hook": "pingHook",
            "remove_branch_protection": "removeBranchProtection",
            "remove_collaborator": "removeCollaborator",
            "remove_deploy_key": "removeDeployKey",
            "remove_protected_branch_admin_enforcement": "removeProtectedBranchAdminEnforcement",
            "remove_protected_branch_pull_request_review_enforcement": "removeProtectedBranchPullRequestReviewEnforcement",
            "remove_protected_branch_required_signatures": "removeProtectedBranchRequiredSignatures",
            "remove_protected_branch_required_status_checks": "removeProtectedBranchRequiredStatusChecks",
            "remove_protected_branch_required_status_checks_contexts": "removeProtectedBranchRequiredStatusChecksContexts",
            "remove_protected_branch_restrictions": "removeProtectedBranchRestrictions",
            "remove_protected_branch_team_restrictions": "removeProtectedBranchTeamRestrictions",
            "remove_protected_branch_user_restrictions": "removeProtectedBranchUserRestrictions",
            "replace_protected_branch_required_status_checks_contexts": "replaceProtectedBranchRequiredStatusChecksContexts",
            "replace_protected_branch_team_restrictions": "replaceProtectedBranchTeamRestrictions",
            "replace_protected_branch_user_restrictions": "replaceProtectedBranchUserRestrictions",
            "replace_topics": "replaceTopics",
            "request_page_build": "requestPageBuild",
            "retrieve_community_profile_metrics": "retrieveCommunityProfileMetrics",
            "test_push_hook": "testPushHook",
            "transfer": "transfer",
            "update": "update",
            "update_branch_protection": "updateBranchProtection",
            "update_commit_comment": "updateCommitComment",
            "update_file": "updateFile",
            "update_hook": "updateHook",
            "update_information_about_pages_site": "updateInformationAboutPagesSite",
            "update_invitation": "updateInvitation",
            "update_protected_branch_pull_request_review_enforcement": "updateProtectedBranchPullRequestReviewEnforcement",
            "update_protected_branch_required_status_checks": "updateProtectedBranchRequiredStatusChecks",
            "update_release": "updateRelease",
            "update_release_asset": "updateReleaseAsset",
            "upload_release_asset": "uploadReleaseAsset",
        }


class OctokitReposAcceptInvitation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposAddCollaborator(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposAddDeployKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposAddProtectedBranchAdminEnforcement(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposAddProtectedBranchRequiredSignatures(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposAddProtectedBranchRequiredStatusChecksContexts(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposAddProtectedBranchTeamRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposAddProtectedBranchUserRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCheckCollaborator(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCompareCommits(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateCommitComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateDeployment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateDeploymentStatus(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateFile(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateFork(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateInOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateRelease(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposCreateStatus(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDeclineInvitation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDelete(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDeleteCommitComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDeleteDownload(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDeleteFile(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDeleteHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDeleteInvitation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDeleteRelease(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposDeleteReleaseAsset(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetArchiveLink(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetBranch(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetBranchProtection(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetClones(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetCodeFrequencyStats(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetCollaboratorPermissionLevel(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetCombinedStatusForRef(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetCommit(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetCommitActivityStats(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetCommitComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetCommitRefSha(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetContents(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetContributorsStats(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetDeployKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetDeployment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetDeploymentStatus(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetDownload(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetLatestPagesBuild(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetLatestRelease(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetPages(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetPagesBuild(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetParticipationStats(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetProtectedBranchAdminEnforcement(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetProtectedBranchPullRequestReviewEnforcement(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetProtectedBranchRequiredSignatures(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetProtectedBranchRequiredStatusChecks(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetProtectedBranchRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetPunchCardStats(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetReadme(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetRelease(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetReleaseAsset(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetReleaseByTag(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetTopPaths(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetTopReferrers(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposGetViews(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposList(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListAssetsForRelease(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListBranches(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListCollaborators(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListCommentsForCommit(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListCommitComments(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListCommits(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListContributors(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListDeployKeys(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListDeploymentStatuses(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListDeployments(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListDownloads(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListForOrg(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListForks(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListHooks(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListInvitations(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListInvitationsForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListLanguages(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListPagesBuilds(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListProtectedBranchRequiredStatusChecksContexts(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListProtectedBranchTeamRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListProtectedBranchUserRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListPublic(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListReleases(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListStatusesForRef(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListTags(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListTeams(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposListTopics(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposMerge(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposPingHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveBranchProtection(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveCollaborator(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveDeployKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveProtectedBranchAdminEnforcement(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveProtectedBranchPullRequestReviewEnforcement(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveProtectedBranchRequiredSignatures(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveProtectedBranchRequiredStatusChecks(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveProtectedBranchRequiredStatusChecksContexts(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveProtectedBranchRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveProtectedBranchTeamRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRemoveProtectedBranchUserRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposReplaceProtectedBranchRequiredStatusChecksContexts(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposReplaceProtectedBranchTeamRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposReplaceProtectedBranchUserRestrictions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposReplaceTopics(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRequestPageBuild(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposRetrieveCommunityProfileMetrics(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposTestPushHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposTransfer(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateBranchProtection(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateCommitComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateFile(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateHook(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateInformationAboutPagesSite(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateInvitation(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateProtectedBranchPullRequestReviewEnforcement(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateProtectedBranchRequiredStatusChecks(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateRelease(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUpdateReleaseAsset(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitReposUploadReleaseAsset(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitSearch(BaseModel):
    code: Optional["OctokitSearchCode"]
    commits: Optional["OctokitSearchCommits"]
    issues: Optional["OctokitSearchIssues"]
    issues_and_pull_requests: Optional["OctokitSearchIssuesAndPullRequests"]
    labels: Optional["OctokitSearchLabels"]
    repos: Optional["OctokitSearchRepos"]
    topics: Optional["OctokitSearchTopics"]
    users: Optional["OctokitSearchUsers"]

    class Config:
        fields = {
            "code": "code",
            "commits": "commits",
            "issues": "issues",
            "issues_and_pull_requests": "issuesAndPullRequests",
            "labels": "labels",
            "repos": "repos",
            "topics": "topics",
            "users": "users",
        }


class OctokitSearchCode(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitSearchCommits(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitSearchIssues(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitSearchIssuesAndPullRequests(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitSearchLabels(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitSearchRepos(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitSearchTopics(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitSearchUsers(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeams(BaseModel):
    add_member: Optional["OctokitTeamsAddMember"]
    add_or_update_membership: Optional["OctokitTeamsAddOrUpdateMembership"]
    add_or_update_project: Optional["OctokitTeamsAddOrUpdateProject"]
    add_or_update_repo: Optional["OctokitTeamsAddOrUpdateRepo"]
    check_manages_repo: Optional["OctokitTeamsCheckManagesRepo"]
    create: Optional["OctokitTeamsCreate"]
    create_discussion: Optional["OctokitTeamsCreateDiscussion"]
    create_discussion_comment: Optional["OctokitTeamsCreateDiscussionComment"]
    delete: Optional["OctokitTeamsDelete"]
    delete_discussion: Optional["OctokitTeamsDeleteDiscussion"]
    delete_discussion_comment: Optional["OctokitTeamsDeleteDiscussionComment"]
    get: Optional["OctokitTeamsGet"]
    get_discussion: Optional["OctokitTeamsGetDiscussion"]
    get_discussion_comment: Optional["OctokitTeamsGetDiscussionComment"]
    get_member: Optional["OctokitTeamsGetMember"]
    get_membership: Optional["OctokitTeamsGetMembership"]
    list: Optional["OctokitTeamsList"]
    list_child: Optional["OctokitTeamsListChild"]
    list_discussion_comments: Optional["OctokitTeamsListDiscussionComments"]
    list_discussions: Optional["OctokitTeamsListDiscussions"]
    list_for_authenticated_user: Optional["OctokitTeamsListForAuthenticatedUser"]
    list_members: Optional["OctokitTeamsListMembers"]
    list_pending_invitations: Optional["OctokitTeamsListPendingInvitations"]
    list_projects: Optional["OctokitTeamsListProjects"]
    list_repos: Optional["OctokitTeamsListRepos"]
    remove_member: Optional["OctokitTeamsRemoveMember"]
    remove_membership: Optional["OctokitTeamsRemoveMembership"]
    remove_project: Optional["OctokitTeamsRemoveProject"]
    remove_repo: Optional["OctokitTeamsRemoveRepo"]
    review_project: Optional["OctokitTeamsReviewProject"]
    update: Optional["OctokitTeamsUpdate"]
    update_discussion: Optional["OctokitTeamsUpdateDiscussion"]
    update_discussion_comment: Optional["OctokitTeamsUpdateDiscussionComment"]

    class Config:
        fields = {
            "add_member": "addMember",
            "add_or_update_membership": "addOrUpdateMembership",
            "add_or_update_project": "addOrUpdateProject",
            "add_or_update_repo": "addOrUpdateRepo",
            "check_manages_repo": "checkManagesRepo",
            "create": "create",
            "create_discussion": "createDiscussion",
            "create_discussion_comment": "createDiscussionComment",
            "delete": "delete",
            "delete_discussion": "deleteDiscussion",
            "delete_discussion_comment": "deleteDiscussionComment",
            "get": "get",
            "get_discussion": "getDiscussion",
            "get_discussion_comment": "getDiscussionComment",
            "get_member": "getMember",
            "get_membership": "getMembership",
            "list": "list",
            "list_child": "listChild",
            "list_discussion_comments": "listDiscussionComments",
            "list_discussions": "listDiscussions",
            "list_for_authenticated_user": "listForAuthenticatedUser",
            "list_members": "listMembers",
            "list_pending_invitations": "listPendingInvitations",
            "list_projects": "listProjects",
            "list_repos": "listRepos",
            "remove_member": "removeMember",
            "remove_membership": "removeMembership",
            "remove_project": "removeProject",
            "remove_repo": "removeRepo",
            "review_project": "reviewProject",
            "update": "update",
            "update_discussion": "updateDiscussion",
            "update_discussion_comment": "updateDiscussionComment",
        }


class OctokitTeamsAddMember(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsAddOrUpdateMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsAddOrUpdateProject(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsAddOrUpdateRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsCheckManagesRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsCreate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsCreateDiscussion(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsCreateDiscussionComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsDelete(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsDeleteDiscussion(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsDeleteDiscussionComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsGet(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsGetDiscussion(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsGetDiscussionComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsGetMember(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsGetMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsList(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsListChild(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsListDiscussionComments(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsListDiscussions(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsListForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsListMembers(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsListPendingInvitations(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsListProjects(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsListRepos(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsRemoveMember(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsRemoveMembership(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsRemoveProject(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsRemoveRepo(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsReviewProject(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsUpdate(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsUpdateDiscussion(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitTeamsUpdateDiscussionComment(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsers(BaseModel):
    add_emails: Optional["OctokitUsersAddEmails"]
    block: Optional["OctokitUsersBlock"]
    check_blocked: Optional["OctokitUsersCheckBlocked"]
    check_following: Optional["OctokitUsersCheckFollowing"]
    check_following_for_user: Optional["OctokitUsersCheckFollowingForUser"]
    create_gpg_key: Optional["OctokitUsersCreateGpgKey"]
    create_public_key: Optional["OctokitUsersCreatePublicKey"]
    delete_emails: Optional["OctokitUsersDeleteEmails"]
    delete_gpg_key: Optional["OctokitUsersDeleteGpgKey"]
    delete_public_key: Optional["OctokitUsersDeletePublicKey"]
    follow: Optional["OctokitUsersFollow"]
    get_authenticated: Optional["OctokitUsersGetAuthenticated"]
    get_by_username: Optional["OctokitUsersGetByUsername"]
    get_context_for_user: Optional["OctokitUsersGetContextForUser"]
    get_gpg_key: Optional["OctokitUsersGetGpgKey"]
    get_public_key: Optional["OctokitUsersGetPublicKey"]
    list: Optional["OctokitUsersList"]
    list_blocked: Optional["OctokitUsersListBlocked"]
    list_emails: Optional["OctokitUsersListEmails"]
    list_followers_for_authenticated_user: Optional[
        "OctokitUsersListFollowersForAuthenticatedUser"
    ]
    list_followers_for_user: Optional["OctokitUsersListFollowersForUser"]
    list_following_for_authenticated_user: Optional[
        "OctokitUsersListFollowingForAuthenticatedUser"
    ]
    list_following_for_user: Optional["OctokitUsersListFollowingForUser"]
    list_gpg_keys: Optional["OctokitUsersListGpgKeys"]
    list_gpg_keys_for_user: Optional["OctokitUsersListGpgKeysForUser"]
    list_public_emails: Optional["OctokitUsersListPublicEmails"]
    list_public_keys: Optional["OctokitUsersListPublicKeys"]
    list_public_keys_for_user: Optional["OctokitUsersListPublicKeysForUser"]
    toggle_primary_email_visibility: Optional[
        "OctokitUsersTogglePrimaryEmailVisibility"
    ]
    unblock: Optional["OctokitUsersUnblock"]
    unfollow: Optional["OctokitUsersUnfollow"]
    update_authenticated: Optional["OctokitUsersUpdateAuthenticated"]

    class Config:
        fields = {
            "add_emails": "addEmails",
            "block": "block",
            "check_blocked": "checkBlocked",
            "check_following": "checkFollowing",
            "check_following_for_user": "checkFollowingForUser",
            "create_gpg_key": "createGpgKey",
            "create_public_key": "createPublicKey",
            "delete_emails": "deleteEmails",
            "delete_gpg_key": "deleteGpgKey",
            "delete_public_key": "deletePublicKey",
            "follow": "follow",
            "get_authenticated": "getAuthenticated",
            "get_by_username": "getByUsername",
            "get_context_for_user": "getContextForUser",
            "get_gpg_key": "getGpgKey",
            "get_public_key": "getPublicKey",
            "list": "list",
            "list_blocked": "listBlocked",
            "list_emails": "listEmails",
            "list_followers_for_authenticated_user": "listFollowersForAuthenticatedUser",
            "list_followers_for_user": "listFollowersForUser",
            "list_following_for_authenticated_user": "listFollowingForAuthenticatedUser",
            "list_following_for_user": "listFollowingForUser",
            "list_gpg_keys": "listGpgKeys",
            "list_gpg_keys_for_user": "listGpgKeysForUser",
            "list_public_emails": "listPublicEmails",
            "list_public_keys": "listPublicKeys",
            "list_public_keys_for_user": "listPublicKeysForUser",
            "toggle_primary_email_visibility": "togglePrimaryEmailVisibility",
            "unblock": "unblock",
            "unfollow": "unfollow",
            "update_authenticated": "updateAuthenticated",
        }


class OctokitUsersAddEmails(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersBlock(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersCheckBlocked(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersCheckFollowing(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersCheckFollowingForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersCreateGpgKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersCreatePublicKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersDeleteEmails(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersDeleteGpgKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersDeletePublicKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersFollow(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersGetAuthenticated(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersGetByUsername(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersGetContextForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersGetGpgKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersGetPublicKey(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersList(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListBlocked(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListEmails(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListFollowersForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListFollowersForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListFollowingForAuthenticatedUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListFollowingForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListGpgKeys(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListGpgKeysForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListPublicEmails(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListPublicKeys(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersListPublicKeysForUser(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersTogglePrimaryEmailVisibility(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersUnblock(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersUnfollow(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class OctokitUsersUpdateAuthenticated(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


class Paginate(BaseModel):
    iterator: Optional["PaginateIterator"]

    class Config:
        fields = {
            "iterator": "iterator",
        }


class PaginateIterator(BaseModel):
    pass


class RepoMetaData(BaseModel):
    pull_request_id: Optional[str]
    repo_slug: Optional[str]

    class Config:
        fields = {
            "pull_request_id": "pullRequestID",
            "repo_slug": "repoSlug",
        }


class Request(BaseModel):
    endpoint: Optional["Endpoint"]

    class Config:
        fields = {
            "endpoint": "endpoint",
        }


BitBucketCloudCommit.update_forward_refs()

BitBucketCloudCommitAuthor.update_forward_refs()

BitBucketCloudCommitParents.update_forward_refs()

BitBucketCloudCommitsLinks.update_forward_refs()

BitBucketCloudCommitsLinksHtml.update_forward_refs()

BitBucketCloudCompletePRLinks.update_forward_refs()

BitBucketCloudCompletePRLinksActivity.update_forward_refs()

BitBucketCloudCompletePRLinksApprove.update_forward_refs()

BitBucketCloudCompletePRLinksComments.update_forward_refs()

BitBucketCloudCompletePRLinksCommits.update_forward_refs()

BitBucketCloudCompletePRLinksDecline.update_forward_refs()

BitBucketCloudCompletePRLinksDiff.update_forward_refs()

BitBucketCloudCompletePRLinksHtml.update_forward_refs()

BitBucketCloudCompletePRLinksMerge.update_forward_refs()

BitBucketCloudCompletePRLinksSelf.update_forward_refs()

BitBucketCloudCompletePRLinksStatuses.update_forward_refs()

BitBucketCloudContent.update_forward_refs()


BitBucketCloudJSONDSL.update_forward_refs()

BitBucketCloudMergeRef.update_forward_refs()

BitBucketCloudMergeRefBranch.update_forward_refs()

BitBucketCloudMergeRefCommit.update_forward_refs()

BitBucketCloudPRActivity.update_forward_refs()

BitBucketCloudPRActivityPullRequest.update_forward_refs()

BitBucketCloudPRComment.update_forward_refs()

BitBucketCloudPRCommentInline.update_forward_refs()

BitBucketCloudPRCommentPullrequest.update_forward_refs()

BitBucketCloudPRDSL.update_forward_refs()


BitBucketCloudPRLinks.update_forward_refs()

BitBucketCloudPRLinksHtml.update_forward_refs()

BitBucketCloudPRLinksSelf.update_forward_refs()

BitBucketCloudPRParticipant.update_forward_refs()


BitBucketCloudRepo.update_forward_refs()

BitBucketCloudUser.update_forward_refs()

BitBucketServerCommit.update_forward_refs()

BitBucketServerCommitAuthor.update_forward_refs()

BitBucketServerCommitCommitter.update_forward_refs()

BitBucketServerCommitParents.update_forward_refs()

BitBucketServerJSONDSL.update_forward_refs()


BitBucketServerMergeRef.update_forward_refs()

BitBucketServerPRActivity.update_forward_refs()


BitBucketServerPRActivityCommentAnchor.update_forward_refs()


BitBucketServerPRComment.update_forward_refs()

BitBucketServerPRCommentParent.update_forward_refs()

BitBucketServerPRCommentPermittedOperations.update_forward_refs()

BitBucketServerPRDSL.update_forward_refs()


BitBucketServerPRParticipant.update_forward_refs()


BitBucketServerRepo.update_forward_refs()

BitBucketServerRepoProject.update_forward_refs()


BitBucketServerUser.update_forward_refs()


CliArgs.update_forward_refs()

DangerDSLJSONType.update_forward_refs()

DangerDSLJSONTypeSettings.update_forward_refs()

DangerDSLJSONTypeSettingsGithub.update_forward_refs()

Endpoint.update_forward_refs()

EndpointOptions.update_forward_refs()

EndpointOptionsHeaders.update_forward_refs()


EndpointOptionsRequest.update_forward_refs()

GitCommit.update_forward_refs()

GitCommitAuthor.update_forward_refs()

GitHubAPIPR.update_forward_refs()

GitHubCommit.update_forward_refs()

GitHubDSL.update_forward_refs()

GitHubIssue.update_forward_refs()

GitHubIssueLabel.update_forward_refs()

GitHubMergeRef.update_forward_refs()

GitHubPRDSL.update_forward_refs()


GitHubRepo.update_forward_refs()

GitHubReview.update_forward_refs()


GitHubReviewers.update_forward_refs()

GitHubUser.update_forward_refs()


GitHubUtilsDSL.update_forward_refs()

GitHubUtilsDSLCreateOrAddLabel.update_forward_refs()

GitHubUtilsDSLCreateOrUpdatePR.update_forward_refs()

GitHubUtilsDSLCreateUpdatedIssueWithID.update_forward_refs()

GitJSONDSL.update_forward_refs()

GitLabDSL.update_forward_refs()

GitLabDSLUtils.update_forward_refs()

GitLabMR.update_forward_refs()

GitLabMRCommit.update_forward_refs()

GitLabMRDiffRefs.update_forward_refs()


GitLabMRMilestone.update_forward_refs()


GitLabMRPipeline.update_forward_refs()


GitLabMRTimeStats.update_forward_refs()

GitLabMRUser.update_forward_refs()

GitLabUser.update_forward_refs()


JIRAIssue.update_forward_refs()

Log.update_forward_refs()

LogDebug.update_forward_refs()

LogError.update_forward_refs()

LogInfo.update_forward_refs()

LogWarn.update_forward_refs()

Octokit.update_forward_refs()

OctokitActivity.update_forward_refs()

OctokitActivityCheckStarringRepo.update_forward_refs()

OctokitActivityDeleteRepoSubscription.update_forward_refs()

OctokitActivityDeleteThreadSubscription.update_forward_refs()

OctokitActivityGetRepoSubscription.update_forward_refs()

OctokitActivityGetThread.update_forward_refs()

OctokitActivityGetThreadSubscription.update_forward_refs()

OctokitActivityListEventsForOrg.update_forward_refs()

OctokitActivityListEventsForUser.update_forward_refs()

OctokitActivityListFeeds.update_forward_refs()

OctokitActivityListNotifications.update_forward_refs()

OctokitActivityListNotificationsForRepo.update_forward_refs()

OctokitActivityListPublicEvents.update_forward_refs()

OctokitActivityListPublicEventsForOrg.update_forward_refs()

OctokitActivityListPublicEventsForRepoNetwork.update_forward_refs()

OctokitActivityListPublicEventsForUser.update_forward_refs()

OctokitActivityListReceivedEventsForUser.update_forward_refs()

OctokitActivityListReceivedPublicEventsForUser.update_forward_refs()

OctokitActivityListRepoEvents.update_forward_refs()

OctokitActivityListReposStarredByAuthenticatedUser.update_forward_refs()

OctokitActivityListReposStarredByUser.update_forward_refs()

OctokitActivityListReposWatchedByUser.update_forward_refs()

OctokitActivityListStargazersForRepo.update_forward_refs()

OctokitActivityListWatchedReposForAuthenticatedUser.update_forward_refs()

OctokitActivityListWatchersForRepo.update_forward_refs()

OctokitActivityMarkAsRead.update_forward_refs()

OctokitActivityMarkNotificationsAsReadForRepo.update_forward_refs()

OctokitActivityMarkThreadAsRead.update_forward_refs()

OctokitActivitySetRepoSubscription.update_forward_refs()

OctokitActivitySetThreadSubscription.update_forward_refs()

OctokitActivityStarRepo.update_forward_refs()

OctokitActivityUnstarRepo.update_forward_refs()

OctokitApps.update_forward_refs()

OctokitAppsAddRepoToInstallation.update_forward_refs()

OctokitAppsCheckAccountIsAssociatedWithAny.update_forward_refs()

OctokitAppsCheckAccountIsAssociatedWithAnyStubbed.update_forward_refs()

OctokitAppsCreateContentAttachment.update_forward_refs()

OctokitAppsCreateFromManifest.update_forward_refs()

OctokitAppsCreateInstallationToken.update_forward_refs()

OctokitAppsFindOrgInstallation.update_forward_refs()

OctokitAppsFindRepoInstallation.update_forward_refs()

OctokitAppsFindUserInstallation.update_forward_refs()

OctokitAppsGetAuthenticated.update_forward_refs()

OctokitAppsGetBySlug.update_forward_refs()

OctokitAppsGetInstallation.update_forward_refs()

OctokitAppsListAccountsUserOrOrgOnPlan.update_forward_refs()

OctokitAppsListAccountsUserOrOrgOnPlanStubbed.update_forward_refs()

OctokitAppsListInstallationReposForAuthenticatedUser.update_forward_refs()

OctokitAppsListInstallations.update_forward_refs()

OctokitAppsListInstallationsForAuthenticatedUser.update_forward_refs()

OctokitAppsListMarketplacePurchasesForAuthenticatedUser.update_forward_refs()

OctokitAppsListMarketplacePurchasesForAuthenticatedUserStubbed.update_forward_refs()

OctokitAppsListPlans.update_forward_refs()

OctokitAppsListPlansStubbed.update_forward_refs()

OctokitAppsListRepos.update_forward_refs()

OctokitAppsRemoveRepoFromInstallation.update_forward_refs()

OctokitChecks.update_forward_refs()

OctokitChecksCreate.update_forward_refs()

OctokitChecksCreateSuite.update_forward_refs()

OctokitChecksGet.update_forward_refs()

OctokitChecksGetSuite.update_forward_refs()

OctokitChecksListAnnotations.update_forward_refs()

OctokitChecksListForRef.update_forward_refs()

OctokitChecksListForSuite.update_forward_refs()

OctokitChecksListSuitesForRef.update_forward_refs()

OctokitChecksRerequestSuite.update_forward_refs()

OctokitChecksSetSuitesPreferences.update_forward_refs()

OctokitChecksUpdate.update_forward_refs()

OctokitCodesOfConduct.update_forward_refs()

OctokitCodesOfConductGetConductCode.update_forward_refs()

OctokitCodesOfConductGetForRepo.update_forward_refs()

OctokitCodesOfConductListConductCodes.update_forward_refs()

OctokitEmojis.update_forward_refs()

OctokitEmojisGet.update_forward_refs()

OctokitGists.update_forward_refs()

OctokitGistsCheckIsStarred.update_forward_refs()

OctokitGistsCreate.update_forward_refs()

OctokitGistsCreateComment.update_forward_refs()

OctokitGistsDelete.update_forward_refs()

OctokitGistsDeleteComment.update_forward_refs()

OctokitGistsFork.update_forward_refs()

OctokitGistsGet.update_forward_refs()

OctokitGistsGetComment.update_forward_refs()

OctokitGistsGetRevision.update_forward_refs()

OctokitGistsList.update_forward_refs()

OctokitGistsListComments.update_forward_refs()

OctokitGistsListCommits.update_forward_refs()

OctokitGistsListForks.update_forward_refs()

OctokitGistsListPublic.update_forward_refs()

OctokitGistsListPublicForUser.update_forward_refs()

OctokitGistsListStarred.update_forward_refs()

OctokitGistsStar.update_forward_refs()

OctokitGistsUnstar.update_forward_refs()

OctokitGistsUpdate.update_forward_refs()

OctokitGistsUpdateComment.update_forward_refs()

OctokitGit.update_forward_refs()

OctokitGitCreateBlob.update_forward_refs()

OctokitGitCreateCommit.update_forward_refs()

OctokitGitCreateRef.update_forward_refs()

OctokitGitCreateTag.update_forward_refs()

OctokitGitCreateTree.update_forward_refs()

OctokitGitDeleteRef.update_forward_refs()

OctokitGitGetBlob.update_forward_refs()

OctokitGitGetCommit.update_forward_refs()

OctokitGitGetRef.update_forward_refs()

OctokitGitGetTag.update_forward_refs()

OctokitGitGetTree.update_forward_refs()

OctokitGitListRefs.update_forward_refs()

OctokitGitUpdateRef.update_forward_refs()

OctokitGitignore.update_forward_refs()

OctokitGitignoreGetTemplate.update_forward_refs()

OctokitGitignoreListTemplates.update_forward_refs()

OctokitHook.update_forward_refs()

OctokitInteractions.update_forward_refs()

OctokitInteractionsAddOrUpdateRestrictionsForOrg.update_forward_refs()

OctokitInteractionsAddOrUpdateRestrictionsForRepo.update_forward_refs()

OctokitInteractionsGetRestrictionsForOrg.update_forward_refs()

OctokitInteractionsGetRestrictionsForRepo.update_forward_refs()

OctokitInteractionsRemoveRestrictionsForOrg.update_forward_refs()

OctokitInteractionsRemoveRestrictionsForRepo.update_forward_refs()

OctokitIssues.update_forward_refs()

OctokitIssuesAddAssignees.update_forward_refs()

OctokitIssuesAddLabels.update_forward_refs()

OctokitIssuesCheckAssignee.update_forward_refs()

OctokitIssuesCreate.update_forward_refs()

OctokitIssuesCreateComment.update_forward_refs()

OctokitIssuesCreateLabel.update_forward_refs()

OctokitIssuesCreateMilestone.update_forward_refs()

OctokitIssuesDeleteComment.update_forward_refs()

OctokitIssuesDeleteLabel.update_forward_refs()

OctokitIssuesDeleteMilestone.update_forward_refs()

OctokitIssuesGet.update_forward_refs()

OctokitIssuesGetComment.update_forward_refs()

OctokitIssuesGetEvent.update_forward_refs()

OctokitIssuesGetLabel.update_forward_refs()

OctokitIssuesGetMilestone.update_forward_refs()

OctokitIssuesList.update_forward_refs()

OctokitIssuesListAssignees.update_forward_refs()

OctokitIssuesListComments.update_forward_refs()

OctokitIssuesListCommentsForRepo.update_forward_refs()

OctokitIssuesListEvents.update_forward_refs()

OctokitIssuesListEventsForRepo.update_forward_refs()

OctokitIssuesListEventsForTimeline.update_forward_refs()

OctokitIssuesListForAuthenticatedUser.update_forward_refs()

OctokitIssuesListForOrg.update_forward_refs()

OctokitIssuesListForRepo.update_forward_refs()

OctokitIssuesListLabelsForMilestone.update_forward_refs()

OctokitIssuesListLabelsForRepo.update_forward_refs()

OctokitIssuesListLabelsOnIssue.update_forward_refs()

OctokitIssuesListMilestonesForRepo.update_forward_refs()

OctokitIssuesLock.update_forward_refs()

OctokitIssuesRemoveAssignees.update_forward_refs()

OctokitIssuesRemoveLabel.update_forward_refs()

OctokitIssuesRemoveLabels.update_forward_refs()

OctokitIssuesReplaceLabels.update_forward_refs()

OctokitIssuesUnlock.update_forward_refs()

OctokitIssuesUpdate.update_forward_refs()

OctokitIssuesUpdateComment.update_forward_refs()

OctokitIssuesUpdateLabel.update_forward_refs()

OctokitIssuesUpdateMilestone.update_forward_refs()

OctokitLicenses.update_forward_refs()

OctokitLicensesGet.update_forward_refs()

OctokitLicensesGetForRepo.update_forward_refs()

OctokitLicensesList.update_forward_refs()

OctokitMarkdown.update_forward_refs()

OctokitMarkdownRender.update_forward_refs()

OctokitMarkdownRenderRaw.update_forward_refs()

OctokitMeta.update_forward_refs()

OctokitMetaGet.update_forward_refs()

OctokitMigrations.update_forward_refs()

OctokitMigrationsCancelImport.update_forward_refs()

OctokitMigrationsDeleteArchiveForAuthenticatedUser.update_forward_refs()

OctokitMigrationsDeleteArchiveForOrg.update_forward_refs()

OctokitMigrationsGetArchiveForAuthenticatedUser.update_forward_refs()

OctokitMigrationsGetArchiveForOrg.update_forward_refs()

OctokitMigrationsGetCommitAuthors.update_forward_refs()

OctokitMigrationsGetImportProgress.update_forward_refs()

OctokitMigrationsGetLargeFiles.update_forward_refs()

OctokitMigrationsGetStatusForAuthenticatedUser.update_forward_refs()

OctokitMigrationsGetStatusForOrg.update_forward_refs()

OctokitMigrationsListForAuthenticatedUser.update_forward_refs()

OctokitMigrationsListForOrg.update_forward_refs()

OctokitMigrationsMapCommitAuthor.update_forward_refs()

OctokitMigrationsSetLfsPreference.update_forward_refs()

OctokitMigrationsStartForAuthenticatedUser.update_forward_refs()

OctokitMigrationsStartForOrg.update_forward_refs()

OctokitMigrationsStartImport.update_forward_refs()

OctokitMigrationsUnlockRepoForAuthenticatedUser.update_forward_refs()

OctokitMigrationsUnlockRepoForOrg.update_forward_refs()

OctokitMigrationsUpdateImport.update_forward_refs()

OctokitOauthAuthorizations.update_forward_refs()

OctokitOauthAuthorizationsCheckAuthorization.update_forward_refs()

OctokitOauthAuthorizationsCreateAuthorization.update_forward_refs()

OctokitOauthAuthorizationsDeleteAuthorization.update_forward_refs()

OctokitOauthAuthorizationsDeleteGrant.update_forward_refs()

OctokitOauthAuthorizationsGetAuthorization.update_forward_refs()

OctokitOauthAuthorizationsGetGrant.update_forward_refs()

OctokitOauthAuthorizationsGetOrCreateAuthorizationForApp.update_forward_refs()

OctokitOauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint.update_forward_refs()

OctokitOauthAuthorizationsGetOrCreateAuthorizationForAppFingerprint.update_forward_refs()

OctokitOauthAuthorizationsListAuthorizations.update_forward_refs()

OctokitOauthAuthorizationsListGrants.update_forward_refs()

OctokitOauthAuthorizationsResetAuthorization.update_forward_refs()

OctokitOauthAuthorizationsRevokeAuthorizationForApplication.update_forward_refs()

OctokitOauthAuthorizationsRevokeGrantForApplication.update_forward_refs()

OctokitOauthAuthorizationsUpdateAuthorization.update_forward_refs()

OctokitOrgs.update_forward_refs()

OctokitOrgsAddOrUpdateMembership.update_forward_refs()

OctokitOrgsBlockUser.update_forward_refs()

OctokitOrgsCheckBlockedUser.update_forward_refs()

OctokitOrgsCheckMembership.update_forward_refs()

OctokitOrgsCheckPublicMembership.update_forward_refs()

OctokitOrgsConcealMembership.update_forward_refs()

OctokitOrgsConvertMemberToOutsideCollaborator.update_forward_refs()

OctokitOrgsCreateHook.update_forward_refs()

OctokitOrgsCreateInvitation.update_forward_refs()

OctokitOrgsDeleteHook.update_forward_refs()

OctokitOrgsGet.update_forward_refs()

OctokitOrgsGetHook.update_forward_refs()

OctokitOrgsGetMembership.update_forward_refs()

OctokitOrgsGetMembershipForAuthenticatedUser.update_forward_refs()

OctokitOrgsList.update_forward_refs()

OctokitOrgsListBlockedUsers.update_forward_refs()

OctokitOrgsListForAuthenticatedUser.update_forward_refs()

OctokitOrgsListForUser.update_forward_refs()

OctokitOrgsListHooks.update_forward_refs()

OctokitOrgsListInvitationTeams.update_forward_refs()

OctokitOrgsListMembers.update_forward_refs()

OctokitOrgsListMemberships.update_forward_refs()

OctokitOrgsListOutsideCollaborators.update_forward_refs()

OctokitOrgsListPendingInvitations.update_forward_refs()

OctokitOrgsListPublicMembers.update_forward_refs()

OctokitOrgsPingHook.update_forward_refs()

OctokitOrgsPublicizeMembership.update_forward_refs()

OctokitOrgsRemoveMember.update_forward_refs()

OctokitOrgsRemoveMembership.update_forward_refs()

OctokitOrgsRemoveOutsideCollaborator.update_forward_refs()

OctokitOrgsUnblockUser.update_forward_refs()

OctokitOrgsUpdate.update_forward_refs()

OctokitOrgsUpdateHook.update_forward_refs()

OctokitOrgsUpdateMembership.update_forward_refs()

OctokitProjects.update_forward_refs()

OctokitProjectsAddCollaborator.update_forward_refs()

OctokitProjectsCreateCard.update_forward_refs()

OctokitProjectsCreateColumn.update_forward_refs()

OctokitProjectsCreateForOrg.update_forward_refs()

OctokitProjectsCreateForRepo.update_forward_refs()

OctokitProjectsDelete.update_forward_refs()

OctokitProjectsDeleteCard.update_forward_refs()

OctokitProjectsDeleteColumn.update_forward_refs()

OctokitProjectsGet.update_forward_refs()

OctokitProjectsGetCard.update_forward_refs()

OctokitProjectsGetColumn.update_forward_refs()

OctokitProjectsListCards.update_forward_refs()

OctokitProjectsListCollaborators.update_forward_refs()

OctokitProjectsListColumns.update_forward_refs()

OctokitProjectsListForOrg.update_forward_refs()

OctokitProjectsListForRepo.update_forward_refs()

OctokitProjectsMoveCard.update_forward_refs()

OctokitProjectsMoveColumn.update_forward_refs()

OctokitProjectsRemoveCollaborator.update_forward_refs()

OctokitProjectsReviewUserPermissionLevel.update_forward_refs()

OctokitProjectsUpdate.update_forward_refs()

OctokitProjectsUpdateCard.update_forward_refs()

OctokitProjectsUpdateColumn.update_forward_refs()

OctokitPulls.update_forward_refs()

OctokitPullsCheckIfMerged.update_forward_refs()

OctokitPullsCreate.update_forward_refs()

OctokitPullsCreateComment.update_forward_refs()

OctokitPullsCreateCommentReply.update_forward_refs()

OctokitPullsCreateFromIssue.update_forward_refs()

OctokitPullsCreateReview.update_forward_refs()

OctokitPullsCreateReviewRequest.update_forward_refs()

OctokitPullsDeleteComment.update_forward_refs()

OctokitPullsDeletePendingReview.update_forward_refs()

OctokitPullsDeleteReviewRequest.update_forward_refs()

OctokitPullsDismissReview.update_forward_refs()

OctokitPullsGet.update_forward_refs()

OctokitPullsGetComment.update_forward_refs()

OctokitPullsGetCommentsForReview.update_forward_refs()

OctokitPullsGetReview.update_forward_refs()

OctokitPullsList.update_forward_refs()

OctokitPullsListComments.update_forward_refs()

OctokitPullsListCommentsForRepo.update_forward_refs()

OctokitPullsListCommits.update_forward_refs()

OctokitPullsListFiles.update_forward_refs()

OctokitPullsListReviewRequests.update_forward_refs()

OctokitPullsListReviews.update_forward_refs()

OctokitPullsMerge.update_forward_refs()

OctokitPullsSubmitReview.update_forward_refs()

OctokitPullsUpdate.update_forward_refs()

OctokitPullsUpdateComment.update_forward_refs()

OctokitPullsUpdateReview.update_forward_refs()

OctokitRateLimit.update_forward_refs()

OctokitRateLimitGet.update_forward_refs()

OctokitReactions.update_forward_refs()

OctokitReactionsCreateForCommitComment.update_forward_refs()

OctokitReactionsCreateForIssue.update_forward_refs()

OctokitReactionsCreateForIssueComment.update_forward_refs()

OctokitReactionsCreateForPullRequestReviewComment.update_forward_refs()

OctokitReactionsCreateForTeamDiscussion.update_forward_refs()

OctokitReactionsCreateForTeamDiscussionComment.update_forward_refs()

OctokitReactionsDelete.update_forward_refs()

OctokitReactionsListForCommitComment.update_forward_refs()

OctokitReactionsListForIssue.update_forward_refs()

OctokitReactionsListForIssueComment.update_forward_refs()

OctokitReactionsListForPullRequestReviewComment.update_forward_refs()

OctokitReactionsListForTeamDiscussion.update_forward_refs()

OctokitReactionsListForTeamDiscussionComment.update_forward_refs()

OctokitRepos.update_forward_refs()

OctokitReposAcceptInvitation.update_forward_refs()

OctokitReposAddCollaborator.update_forward_refs()

OctokitReposAddDeployKey.update_forward_refs()

OctokitReposAddProtectedBranchAdminEnforcement.update_forward_refs()

OctokitReposAddProtectedBranchRequiredSignatures.update_forward_refs()

OctokitReposAddProtectedBranchRequiredStatusChecksContexts.update_forward_refs()

OctokitReposAddProtectedBranchTeamRestrictions.update_forward_refs()

OctokitReposAddProtectedBranchUserRestrictions.update_forward_refs()

OctokitReposCheckCollaborator.update_forward_refs()

OctokitReposCompareCommits.update_forward_refs()

OctokitReposCreateCommitComment.update_forward_refs()

OctokitReposCreateDeployment.update_forward_refs()

OctokitReposCreateDeploymentStatus.update_forward_refs()

OctokitReposCreateFile.update_forward_refs()

OctokitReposCreateForAuthenticatedUser.update_forward_refs()

OctokitReposCreateFork.update_forward_refs()

OctokitReposCreateHook.update_forward_refs()

OctokitReposCreateInOrg.update_forward_refs()

OctokitReposCreateRelease.update_forward_refs()

OctokitReposCreateStatus.update_forward_refs()

OctokitReposDeclineInvitation.update_forward_refs()

OctokitReposDelete.update_forward_refs()

OctokitReposDeleteCommitComment.update_forward_refs()

OctokitReposDeleteDownload.update_forward_refs()

OctokitReposDeleteFile.update_forward_refs()

OctokitReposDeleteHook.update_forward_refs()

OctokitReposDeleteInvitation.update_forward_refs()

OctokitReposDeleteRelease.update_forward_refs()

OctokitReposDeleteReleaseAsset.update_forward_refs()

OctokitReposGet.update_forward_refs()

OctokitReposGetArchiveLink.update_forward_refs()

OctokitReposGetBranch.update_forward_refs()

OctokitReposGetBranchProtection.update_forward_refs()

OctokitReposGetClones.update_forward_refs()

OctokitReposGetCodeFrequencyStats.update_forward_refs()

OctokitReposGetCollaboratorPermissionLevel.update_forward_refs()

OctokitReposGetCombinedStatusForRef.update_forward_refs()

OctokitReposGetCommit.update_forward_refs()

OctokitReposGetCommitActivityStats.update_forward_refs()

OctokitReposGetCommitComment.update_forward_refs()

OctokitReposGetCommitRefSha.update_forward_refs()

OctokitReposGetContents.update_forward_refs()

OctokitReposGetContributorsStats.update_forward_refs()

OctokitReposGetDeployKey.update_forward_refs()

OctokitReposGetDeployment.update_forward_refs()

OctokitReposGetDeploymentStatus.update_forward_refs()

OctokitReposGetDownload.update_forward_refs()

OctokitReposGetHook.update_forward_refs()

OctokitReposGetLatestPagesBuild.update_forward_refs()

OctokitReposGetLatestRelease.update_forward_refs()

OctokitReposGetPages.update_forward_refs()

OctokitReposGetPagesBuild.update_forward_refs()

OctokitReposGetParticipationStats.update_forward_refs()

OctokitReposGetProtectedBranchAdminEnforcement.update_forward_refs()

OctokitReposGetProtectedBranchPullRequestReviewEnforcement.update_forward_refs()

OctokitReposGetProtectedBranchRequiredSignatures.update_forward_refs()

OctokitReposGetProtectedBranchRequiredStatusChecks.update_forward_refs()

OctokitReposGetProtectedBranchRestrictions.update_forward_refs()

OctokitReposGetPunchCardStats.update_forward_refs()

OctokitReposGetReadme.update_forward_refs()

OctokitReposGetRelease.update_forward_refs()

OctokitReposGetReleaseAsset.update_forward_refs()

OctokitReposGetReleaseByTag.update_forward_refs()

OctokitReposGetTopPaths.update_forward_refs()

OctokitReposGetTopReferrers.update_forward_refs()

OctokitReposGetViews.update_forward_refs()

OctokitReposList.update_forward_refs()

OctokitReposListAssetsForRelease.update_forward_refs()

OctokitReposListBranches.update_forward_refs()

OctokitReposListCollaborators.update_forward_refs()

OctokitReposListCommentsForCommit.update_forward_refs()

OctokitReposListCommitComments.update_forward_refs()

OctokitReposListCommits.update_forward_refs()

OctokitReposListContributors.update_forward_refs()

OctokitReposListDeployKeys.update_forward_refs()

OctokitReposListDeploymentStatuses.update_forward_refs()

OctokitReposListDeployments.update_forward_refs()

OctokitReposListDownloads.update_forward_refs()

OctokitReposListForOrg.update_forward_refs()

OctokitReposListForUser.update_forward_refs()

OctokitReposListForks.update_forward_refs()

OctokitReposListHooks.update_forward_refs()

OctokitReposListInvitations.update_forward_refs()

OctokitReposListInvitationsForAuthenticatedUser.update_forward_refs()

OctokitReposListLanguages.update_forward_refs()

OctokitReposListPagesBuilds.update_forward_refs()

OctokitReposListProtectedBranchRequiredStatusChecksContexts.update_forward_refs()

OctokitReposListProtectedBranchTeamRestrictions.update_forward_refs()

OctokitReposListProtectedBranchUserRestrictions.update_forward_refs()

OctokitReposListPublic.update_forward_refs()

OctokitReposListReleases.update_forward_refs()

OctokitReposListStatusesForRef.update_forward_refs()

OctokitReposListTags.update_forward_refs()

OctokitReposListTeams.update_forward_refs()

OctokitReposListTopics.update_forward_refs()

OctokitReposMerge.update_forward_refs()

OctokitReposPingHook.update_forward_refs()

OctokitReposRemoveBranchProtection.update_forward_refs()

OctokitReposRemoveCollaborator.update_forward_refs()

OctokitReposRemoveDeployKey.update_forward_refs()

OctokitReposRemoveProtectedBranchAdminEnforcement.update_forward_refs()

OctokitReposRemoveProtectedBranchPullRequestReviewEnforcement.update_forward_refs()

OctokitReposRemoveProtectedBranchRequiredSignatures.update_forward_refs()

OctokitReposRemoveProtectedBranchRequiredStatusChecks.update_forward_refs()

OctokitReposRemoveProtectedBranchRequiredStatusChecksContexts.update_forward_refs()

OctokitReposRemoveProtectedBranchRestrictions.update_forward_refs()

OctokitReposRemoveProtectedBranchTeamRestrictions.update_forward_refs()

OctokitReposRemoveProtectedBranchUserRestrictions.update_forward_refs()

OctokitReposReplaceProtectedBranchRequiredStatusChecksContexts.update_forward_refs()

OctokitReposReplaceProtectedBranchTeamRestrictions.update_forward_refs()

OctokitReposReplaceProtectedBranchUserRestrictions.update_forward_refs()

OctokitReposReplaceTopics.update_forward_refs()

OctokitReposRequestPageBuild.update_forward_refs()

OctokitReposRetrieveCommunityProfileMetrics.update_forward_refs()

OctokitReposTestPushHook.update_forward_refs()

OctokitReposTransfer.update_forward_refs()

OctokitReposUpdate.update_forward_refs()

OctokitReposUpdateBranchProtection.update_forward_refs()

OctokitReposUpdateCommitComment.update_forward_refs()

OctokitReposUpdateFile.update_forward_refs()

OctokitReposUpdateHook.update_forward_refs()

OctokitReposUpdateInformationAboutPagesSite.update_forward_refs()

OctokitReposUpdateInvitation.update_forward_refs()

OctokitReposUpdateProtectedBranchPullRequestReviewEnforcement.update_forward_refs()

OctokitReposUpdateProtectedBranchRequiredStatusChecks.update_forward_refs()

OctokitReposUpdateRelease.update_forward_refs()

OctokitReposUpdateReleaseAsset.update_forward_refs()

OctokitReposUploadReleaseAsset.update_forward_refs()

OctokitSearch.update_forward_refs()

OctokitSearchCode.update_forward_refs()

OctokitSearchCommits.update_forward_refs()

OctokitSearchIssues.update_forward_refs()

OctokitSearchIssuesAndPullRequests.update_forward_refs()

OctokitSearchLabels.update_forward_refs()

OctokitSearchRepos.update_forward_refs()

OctokitSearchTopics.update_forward_refs()

OctokitSearchUsers.update_forward_refs()

OctokitTeams.update_forward_refs()

OctokitTeamsAddMember.update_forward_refs()

OctokitTeamsAddOrUpdateMembership.update_forward_refs()

OctokitTeamsAddOrUpdateProject.update_forward_refs()

OctokitTeamsAddOrUpdateRepo.update_forward_refs()

OctokitTeamsCheckManagesRepo.update_forward_refs()

OctokitTeamsCreate.update_forward_refs()

OctokitTeamsCreateDiscussion.update_forward_refs()

OctokitTeamsCreateDiscussionComment.update_forward_refs()

OctokitTeamsDelete.update_forward_refs()

OctokitTeamsDeleteDiscussion.update_forward_refs()

OctokitTeamsDeleteDiscussionComment.update_forward_refs()

OctokitTeamsGet.update_forward_refs()

OctokitTeamsGetDiscussion.update_forward_refs()

OctokitTeamsGetDiscussionComment.update_forward_refs()

OctokitTeamsGetMember.update_forward_refs()

OctokitTeamsGetMembership.update_forward_refs()

OctokitTeamsList.update_forward_refs()

OctokitTeamsListChild.update_forward_refs()

OctokitTeamsListDiscussionComments.update_forward_refs()

OctokitTeamsListDiscussions.update_forward_refs()

OctokitTeamsListForAuthenticatedUser.update_forward_refs()

OctokitTeamsListMembers.update_forward_refs()

OctokitTeamsListPendingInvitations.update_forward_refs()

OctokitTeamsListProjects.update_forward_refs()

OctokitTeamsListRepos.update_forward_refs()

OctokitTeamsRemoveMember.update_forward_refs()

OctokitTeamsRemoveMembership.update_forward_refs()

OctokitTeamsRemoveProject.update_forward_refs()

OctokitTeamsRemoveRepo.update_forward_refs()

OctokitTeamsReviewProject.update_forward_refs()

OctokitTeamsUpdate.update_forward_refs()

OctokitTeamsUpdateDiscussion.update_forward_refs()

OctokitTeamsUpdateDiscussionComment.update_forward_refs()

OctokitUsers.update_forward_refs()

OctokitUsersAddEmails.update_forward_refs()

OctokitUsersBlock.update_forward_refs()

OctokitUsersCheckBlocked.update_forward_refs()

OctokitUsersCheckFollowing.update_forward_refs()

OctokitUsersCheckFollowingForUser.update_forward_refs()

OctokitUsersCreateGpgKey.update_forward_refs()

OctokitUsersCreatePublicKey.update_forward_refs()

OctokitUsersDeleteEmails.update_forward_refs()

OctokitUsersDeleteGpgKey.update_forward_refs()

OctokitUsersDeletePublicKey.update_forward_refs()

OctokitUsersFollow.update_forward_refs()

OctokitUsersGetAuthenticated.update_forward_refs()

OctokitUsersGetByUsername.update_forward_refs()

OctokitUsersGetContextForUser.update_forward_refs()

OctokitUsersGetGpgKey.update_forward_refs()

OctokitUsersGetPublicKey.update_forward_refs()

OctokitUsersList.update_forward_refs()

OctokitUsersListBlocked.update_forward_refs()

OctokitUsersListEmails.update_forward_refs()

OctokitUsersListFollowersForAuthenticatedUser.update_forward_refs()

OctokitUsersListFollowersForUser.update_forward_refs()

OctokitUsersListFollowingForAuthenticatedUser.update_forward_refs()

OctokitUsersListFollowingForUser.update_forward_refs()

OctokitUsersListGpgKeys.update_forward_refs()

OctokitUsersListGpgKeysForUser.update_forward_refs()

OctokitUsersListPublicEmails.update_forward_refs()

OctokitUsersListPublicKeys.update_forward_refs()

OctokitUsersListPublicKeysForUser.update_forward_refs()

OctokitUsersTogglePrimaryEmailVisibility.update_forward_refs()

OctokitUsersUnblock.update_forward_refs()

OctokitUsersUnfollow.update_forward_refs()

OctokitUsersUpdateAuthenticated.update_forward_refs()

Paginate.update_forward_refs()

PaginateIterator.update_forward_refs()

RepoMetaData.update_forward_refs()

Request.update_forward_refs()
