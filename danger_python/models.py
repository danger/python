from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel


class ApplicationSettings(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ApplicationSettingsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ApplicationSettingsHeaders(BaseModel):
    pass


class BitBucketCloudCommit(BaseModel):
    author: Optional["BitBucketCloudCommitAuthor"]
    date: Optional[str]
    hash: Optional[str]
    links: Optional["BitBucketCloudLinksHtml"]
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


class BitBucketCloudLinksHtml(BaseModel):
    html: Optional["BitBucketCloudLinksHtmlHtml"]

    class Config:
        fields = {
            "html": "html",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatuses(
    BaseModel
):
    activity: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesActivity"
    ]
    approve: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesApprove"
    ]
    comments: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesComments"
    ]
    commits: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesCommits"
    ]
    decline: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesDecline"
    ]
    diff: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesDiff"
    ]
    html: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesHtml"
    ]
    merge: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesMerge"
    ]
    self_: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesSelf"
    ]
    statuses: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesStatuses"
    ]

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


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesActivity(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesApprove(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesComments(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesCommits(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesDecline(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesDiff(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesHtml(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesMerge(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesSelf(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesStatuses(
    BaseModel
):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlHtml(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlSelf(BaseModel):
    html: Optional["BitBucketCloudLinksHtmlSelfHtml"]
    self_: Optional["BitBucketCloudLinksHtmlSelfSelf"]

    class Config:
        fields = {
            "html": "html",
            "self_": "self",
        }


class BitBucketCloudLinksHtmlSelfHtml(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
        }


class BitBucketCloudLinksHtmlSelfSelf(BaseModel):
    href: Optional[str]

    class Config:
        fields = {
            "href": "href",
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
    links: Optional["BitBucketCloudLinksHtmlSelf"]
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
    links: Optional["BitBucketCloudLinksHtmlSelf"]
    title: Optional[str]

    class Config:
        fields = {
            "id": "id",
            "links": "links",
            "title": "title",
        }


class BitBucketCloudPRDSL(BaseModel):
    author: Optional["BitBucketCloudUser"]
    created_on: Optional[str]
    description: Optional[str]
    destination: Optional["BitBucketCloudMergeRef"]
    id: Optional[int]
    links: Optional[
        "BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatuses"
    ]
    participants: Optional[List["BitBucketCloudPRParticipant"]]
    reviewers: Optional[List["BitBucketCloudUser"]]
    source: Optional["BitBucketCloudMergeRef"]
    state: Optional["BitBucketCloudPRDSLState"]
    title: Optional[str]
    updated_on: Optional[str]

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


class Branches(BaseModel):
    camelize: Optional[bool]
    headers: Optional["BranchesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class BranchesHeaders(BaseModel):
    pass


class BroadcastMessages(BaseModel):
    camelize: Optional[bool]
    headers: Optional["BroadcastMessagesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class BroadcastMessagesHeaders(BaseModel):
    pass


class CliArgs(BaseModel):
    base: Optional[str]
    dangerfile: Optional[str]
    external_ci_provider: Optional[str]
    id: Optional[str]
    staging: Optional[bool]
    text_only: Optional[str]
    verbose: Optional[str]

    class Config:
        fields = {
            "base": "base",
            "dangerfile": "dangerfile",
            "external_ci_provider": "externalCiProvider",
            "id": "id",
            "staging": "staging",
            "text_only": "textOnly",
            "verbose": "verbose",
        }


class CommitDiscussions(BaseModel):
    camelize: Optional[bool]
    headers: Optional["CommitDiscussionsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class CommitDiscussionsHeaders(BaseModel):
    pass


class Commits(BaseModel):
    camelize: Optional[bool]
    headers: Optional["CommitsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class CommitsHeaders(BaseModel):
    pass


class ContainerRegistry(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ContainerRegistryHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ContainerRegistryHeaders(BaseModel):
    pass


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


class DeployKeys(BaseModel):
    camelize: Optional[bool]
    headers: Optional["DeployKeysHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class DeployKeysHeaders(BaseModel):
    pass


class Deployments(BaseModel):
    camelize: Optional[bool]
    headers: Optional["DeploymentsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class DeploymentsHeaders(BaseModel):
    pass


class EndpointInterfaceObject(BaseModel):
    defaults: Optional["EndpointInterfaceObjectDEFAULTS"]
    defaults: Optional["EndpointInterfaceObjectDefaults"]
    merge: Optional["EndpointInterfaceObjectMerge"]
    parse: Optional["EndpointInterfaceObjectParse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceObjectDEFAULTS(BaseModel):
    pass


class EndpointInterfaceObjectDefaults(BaseModel):
    pass


class EndpointInterfaceObjectMerge(BaseModel):
    pass


class EndpointInterfaceObjectParse(BaseModel):
    pass


class EndpointInterfaceUrlString(BaseModel):
    defaults: Optional["EndpointInterfaceUrlStringDEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlStringDefaults"]
    merge: Optional["EndpointInterfaceUrlStringMerge"]
    parse: Optional["EndpointInterfaceUrlStringParse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString1(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString1DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString1Defaults"]
    merge: Optional["EndpointInterfaceUrlString1Merge"]
    parse: Optional["EndpointInterfaceUrlString1Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString10(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString10DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString10Defaults"]
    merge: Optional["EndpointInterfaceUrlString10Merge"]
    parse: Optional["EndpointInterfaceUrlString10Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString100(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString100DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString100Defaults"]
    merge: Optional["EndpointInterfaceUrlString100Merge"]
    parse: Optional["EndpointInterfaceUrlString100Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString100DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString100Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString100Merge(BaseModel):
    pass


class EndpointInterfaceUrlString100Parse(BaseModel):
    pass


class EndpointInterfaceUrlString101(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString101DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString101Defaults"]
    merge: Optional["EndpointInterfaceUrlString101Merge"]
    parse: Optional["EndpointInterfaceUrlString101Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString101DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString101Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString101Merge(BaseModel):
    pass


class EndpointInterfaceUrlString101Parse(BaseModel):
    pass


class EndpointInterfaceUrlString102(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString102DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString102Defaults"]
    merge: Optional["EndpointInterfaceUrlString102Merge"]
    parse: Optional["EndpointInterfaceUrlString102Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString102DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString102Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString102Merge(BaseModel):
    pass


class EndpointInterfaceUrlString102Parse(BaseModel):
    pass


class EndpointInterfaceUrlString103(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString103DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString103Defaults"]
    merge: Optional["EndpointInterfaceUrlString103Merge"]
    parse: Optional["EndpointInterfaceUrlString103Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString103DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString103Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString103Merge(BaseModel):
    pass


class EndpointInterfaceUrlString103Parse(BaseModel):
    pass


class EndpointInterfaceUrlString104(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString104DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString104Defaults"]
    merge: Optional["EndpointInterfaceUrlString104Merge"]
    parse: Optional["EndpointInterfaceUrlString104Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString104DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString104Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString104Merge(BaseModel):
    pass


class EndpointInterfaceUrlString104Parse(BaseModel):
    pass


class EndpointInterfaceUrlString105(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString105DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString105Defaults"]
    merge: Optional["EndpointInterfaceUrlString105Merge"]
    parse: Optional["EndpointInterfaceUrlString105Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString105DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString105Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString105Merge(BaseModel):
    pass


class EndpointInterfaceUrlString105Parse(BaseModel):
    pass


class EndpointInterfaceUrlString106(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString106DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString106Defaults"]
    merge: Optional["EndpointInterfaceUrlString106Merge"]
    parse: Optional["EndpointInterfaceUrlString106Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString106DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString106Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString106Merge(BaseModel):
    pass


class EndpointInterfaceUrlString106Parse(BaseModel):
    pass


class EndpointInterfaceUrlString107(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString107DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString107Defaults"]
    merge: Optional["EndpointInterfaceUrlString107Merge"]
    parse: Optional["EndpointInterfaceUrlString107Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString107DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString107Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString107Merge(BaseModel):
    pass


class EndpointInterfaceUrlString107Parse(BaseModel):
    pass


class EndpointInterfaceUrlString108(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString108DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString108Defaults"]
    merge: Optional["EndpointInterfaceUrlString108Merge"]
    parse: Optional["EndpointInterfaceUrlString108Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString108DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString108Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString108Merge(BaseModel):
    pass


class EndpointInterfaceUrlString108Parse(BaseModel):
    pass


class EndpointInterfaceUrlString109(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString109DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString109Defaults"]
    merge: Optional["EndpointInterfaceUrlString109Merge"]
    parse: Optional["EndpointInterfaceUrlString109Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString109DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString109Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString109Merge(BaseModel):
    pass


class EndpointInterfaceUrlString109Parse(BaseModel):
    pass


class EndpointInterfaceUrlString10DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString10Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString10Merge(BaseModel):
    pass


class EndpointInterfaceUrlString10Parse(BaseModel):
    pass


class EndpointInterfaceUrlString11(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString11DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString11Defaults"]
    merge: Optional["EndpointInterfaceUrlString11Merge"]
    parse: Optional["EndpointInterfaceUrlString11Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString110(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString110DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString110Defaults"]
    merge: Optional["EndpointInterfaceUrlString110Merge"]
    parse: Optional["EndpointInterfaceUrlString110Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString110DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString110Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString110Merge(BaseModel):
    pass


class EndpointInterfaceUrlString110Parse(BaseModel):
    pass


class EndpointInterfaceUrlString111(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString111DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString111Defaults"]
    merge: Optional["EndpointInterfaceUrlString111Merge"]
    parse: Optional["EndpointInterfaceUrlString111Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString111DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString111Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString111Merge(BaseModel):
    pass


class EndpointInterfaceUrlString111Parse(BaseModel):
    pass


class EndpointInterfaceUrlString112(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString112DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString112Defaults"]
    merge: Optional["EndpointInterfaceUrlString112Merge"]
    parse: Optional["EndpointInterfaceUrlString112Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString112DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString112Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString112Merge(BaseModel):
    pass


class EndpointInterfaceUrlString112Parse(BaseModel):
    pass


class EndpointInterfaceUrlString113(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString113DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString113Defaults"]
    merge: Optional["EndpointInterfaceUrlString113Merge"]
    parse: Optional["EndpointInterfaceUrlString113Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString113DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString113Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString113Merge(BaseModel):
    pass


class EndpointInterfaceUrlString113Parse(BaseModel):
    pass


class EndpointInterfaceUrlString114(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString114DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString114Defaults"]
    merge: Optional["EndpointInterfaceUrlString114Merge"]
    parse: Optional["EndpointInterfaceUrlString114Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString114DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString114Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString114Merge(BaseModel):
    pass


class EndpointInterfaceUrlString114Parse(BaseModel):
    pass


class EndpointInterfaceUrlString115(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString115DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString115Defaults"]
    merge: Optional["EndpointInterfaceUrlString115Merge"]
    parse: Optional["EndpointInterfaceUrlString115Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString115DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString115Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString115Merge(BaseModel):
    pass


class EndpointInterfaceUrlString115Parse(BaseModel):
    pass


class EndpointInterfaceUrlString116(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString116DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString116Defaults"]
    merge: Optional["EndpointInterfaceUrlString116Merge"]
    parse: Optional["EndpointInterfaceUrlString116Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString116DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString116Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString116Merge(BaseModel):
    pass


class EndpointInterfaceUrlString116Parse(BaseModel):
    pass


class EndpointInterfaceUrlString117(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString117DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString117Defaults"]
    merge: Optional["EndpointInterfaceUrlString117Merge"]
    parse: Optional["EndpointInterfaceUrlString117Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString117DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString117Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString117Merge(BaseModel):
    pass


class EndpointInterfaceUrlString117Parse(BaseModel):
    pass


class EndpointInterfaceUrlString118(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString118DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString118Defaults"]
    merge: Optional["EndpointInterfaceUrlString118Merge"]
    parse: Optional["EndpointInterfaceUrlString118Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString118DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString118Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString118Merge(BaseModel):
    pass


class EndpointInterfaceUrlString118Parse(BaseModel):
    pass


class EndpointInterfaceUrlString119(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString119DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString119Defaults"]
    merge: Optional["EndpointInterfaceUrlString119Merge"]
    parse: Optional["EndpointInterfaceUrlString119Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString119DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString119Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString119Merge(BaseModel):
    pass


class EndpointInterfaceUrlString119Parse(BaseModel):
    pass


class EndpointInterfaceUrlString11DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString11Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString11Merge(BaseModel):
    pass


class EndpointInterfaceUrlString11Parse(BaseModel):
    pass


class EndpointInterfaceUrlString12(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString12DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString12Defaults"]
    merge: Optional["EndpointInterfaceUrlString12Merge"]
    parse: Optional["EndpointInterfaceUrlString12Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString120(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString120DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString120Defaults"]
    merge: Optional["EndpointInterfaceUrlString120Merge"]
    parse: Optional["EndpointInterfaceUrlString120Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString120DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString120Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString120Merge(BaseModel):
    pass


class EndpointInterfaceUrlString120Parse(BaseModel):
    pass


class EndpointInterfaceUrlString121(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString121DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString121Defaults"]
    merge: Optional["EndpointInterfaceUrlString121Merge"]
    parse: Optional["EndpointInterfaceUrlString121Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString121DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString121Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString121Merge(BaseModel):
    pass


class EndpointInterfaceUrlString121Parse(BaseModel):
    pass


class EndpointInterfaceUrlString122(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString122DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString122Defaults"]
    merge: Optional["EndpointInterfaceUrlString122Merge"]
    parse: Optional["EndpointInterfaceUrlString122Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString122DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString122Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString122Merge(BaseModel):
    pass


class EndpointInterfaceUrlString122Parse(BaseModel):
    pass


class EndpointInterfaceUrlString123(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString123DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString123Defaults"]
    merge: Optional["EndpointInterfaceUrlString123Merge"]
    parse: Optional["EndpointInterfaceUrlString123Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString123DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString123Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString123Merge(BaseModel):
    pass


class EndpointInterfaceUrlString123Parse(BaseModel):
    pass


class EndpointInterfaceUrlString124(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString124DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString124Defaults"]
    merge: Optional["EndpointInterfaceUrlString124Merge"]
    parse: Optional["EndpointInterfaceUrlString124Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString124DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString124Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString124Merge(BaseModel):
    pass


class EndpointInterfaceUrlString124Parse(BaseModel):
    pass


class EndpointInterfaceUrlString125(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString125DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString125Defaults"]
    merge: Optional["EndpointInterfaceUrlString125Merge"]
    parse: Optional["EndpointInterfaceUrlString125Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString125DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString125Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString125Merge(BaseModel):
    pass


class EndpointInterfaceUrlString125Parse(BaseModel):
    pass


class EndpointInterfaceUrlString126(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString126DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString126Defaults"]
    merge: Optional["EndpointInterfaceUrlString126Merge"]
    parse: Optional["EndpointInterfaceUrlString126Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString126DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString126Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString126Merge(BaseModel):
    pass


class EndpointInterfaceUrlString126Parse(BaseModel):
    pass


class EndpointInterfaceUrlString127(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString127DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString127Defaults"]
    merge: Optional["EndpointInterfaceUrlString127Merge"]
    parse: Optional["EndpointInterfaceUrlString127Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString127DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString127Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString127Merge(BaseModel):
    pass


class EndpointInterfaceUrlString127Parse(BaseModel):
    pass


class EndpointInterfaceUrlString128(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString128DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString128Defaults"]
    merge: Optional["EndpointInterfaceUrlString128Merge"]
    parse: Optional["EndpointInterfaceUrlString128Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString128DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString128Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString128Merge(BaseModel):
    pass


class EndpointInterfaceUrlString128Parse(BaseModel):
    pass


class EndpointInterfaceUrlString129(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString129DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString129Defaults"]
    merge: Optional["EndpointInterfaceUrlString129Merge"]
    parse: Optional["EndpointInterfaceUrlString129Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString129DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString129Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString129Merge(BaseModel):
    pass


class EndpointInterfaceUrlString129Parse(BaseModel):
    pass


class EndpointInterfaceUrlString12DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString12Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString12Merge(BaseModel):
    pass


class EndpointInterfaceUrlString12Parse(BaseModel):
    pass


class EndpointInterfaceUrlString13(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString13DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString13Defaults"]
    merge: Optional["EndpointInterfaceUrlString13Merge"]
    parse: Optional["EndpointInterfaceUrlString13Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString130(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString130DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString130Defaults"]
    merge: Optional["EndpointInterfaceUrlString130Merge"]
    parse: Optional["EndpointInterfaceUrlString130Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString130DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString130Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString130Merge(BaseModel):
    pass


class EndpointInterfaceUrlString130Parse(BaseModel):
    pass


class EndpointInterfaceUrlString131(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString131DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString131Defaults"]
    merge: Optional["EndpointInterfaceUrlString131Merge"]
    parse: Optional["EndpointInterfaceUrlString131Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString131DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString131Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString131Merge(BaseModel):
    pass


class EndpointInterfaceUrlString131Parse(BaseModel):
    pass


class EndpointInterfaceUrlString132(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString132DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString132Defaults"]
    merge: Optional["EndpointInterfaceUrlString132Merge"]
    parse: Optional["EndpointInterfaceUrlString132Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString132DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString132Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString132Merge(BaseModel):
    pass


class EndpointInterfaceUrlString132Parse(BaseModel):
    pass


class EndpointInterfaceUrlString133(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString133DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString133Defaults"]
    merge: Optional["EndpointInterfaceUrlString133Merge"]
    parse: Optional["EndpointInterfaceUrlString133Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString133DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString133Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString133Merge(BaseModel):
    pass


class EndpointInterfaceUrlString133Parse(BaseModel):
    pass


class EndpointInterfaceUrlString134(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString134DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString134Defaults"]
    merge: Optional["EndpointInterfaceUrlString134Merge"]
    parse: Optional["EndpointInterfaceUrlString134Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString134DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString134Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString134Merge(BaseModel):
    pass


class EndpointInterfaceUrlString134Parse(BaseModel):
    pass


class EndpointInterfaceUrlString135(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString135DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString135Defaults"]
    merge: Optional["EndpointInterfaceUrlString135Merge"]
    parse: Optional["EndpointInterfaceUrlString135Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString135DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString135Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString135Merge(BaseModel):
    pass


class EndpointInterfaceUrlString135Parse(BaseModel):
    pass


class EndpointInterfaceUrlString136(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString136DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString136Defaults"]
    merge: Optional["EndpointInterfaceUrlString136Merge"]
    parse: Optional["EndpointInterfaceUrlString136Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString136DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString136Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString136Merge(BaseModel):
    pass


class EndpointInterfaceUrlString136Parse(BaseModel):
    pass


class EndpointInterfaceUrlString137(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString137DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString137Defaults"]
    merge: Optional["EndpointInterfaceUrlString137Merge"]
    parse: Optional["EndpointInterfaceUrlString137Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString137DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString137Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString137Merge(BaseModel):
    pass


class EndpointInterfaceUrlString137Parse(BaseModel):
    pass


class EndpointInterfaceUrlString138(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString138DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString138Defaults"]
    merge: Optional["EndpointInterfaceUrlString138Merge"]
    parse: Optional["EndpointInterfaceUrlString138Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString138DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString138Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString138Merge(BaseModel):
    pass


class EndpointInterfaceUrlString138Parse(BaseModel):
    pass


class EndpointInterfaceUrlString139(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString139DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString139Defaults"]
    merge: Optional["EndpointInterfaceUrlString139Merge"]
    parse: Optional["EndpointInterfaceUrlString139Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString139DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString139Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString139Merge(BaseModel):
    pass


class EndpointInterfaceUrlString139Parse(BaseModel):
    pass


class EndpointInterfaceUrlString13DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString13Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString13Merge(BaseModel):
    pass


class EndpointInterfaceUrlString13Parse(BaseModel):
    pass


class EndpointInterfaceUrlString14(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString14DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString14Defaults"]
    merge: Optional["EndpointInterfaceUrlString14Merge"]
    parse: Optional["EndpointInterfaceUrlString14Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString140(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString140DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString140Defaults"]
    merge: Optional["EndpointInterfaceUrlString140Merge"]
    parse: Optional["EndpointInterfaceUrlString140Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString140DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString140Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString140Merge(BaseModel):
    pass


class EndpointInterfaceUrlString140Parse(BaseModel):
    pass


class EndpointInterfaceUrlString141(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString141DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString141Defaults"]
    merge: Optional["EndpointInterfaceUrlString141Merge"]
    parse: Optional["EndpointInterfaceUrlString141Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString141DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString141Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString141Merge(BaseModel):
    pass


class EndpointInterfaceUrlString141Parse(BaseModel):
    pass


class EndpointInterfaceUrlString142(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString142DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString142Defaults"]
    merge: Optional["EndpointInterfaceUrlString142Merge"]
    parse: Optional["EndpointInterfaceUrlString142Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString142DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString142Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString142Merge(BaseModel):
    pass


class EndpointInterfaceUrlString142Parse(BaseModel):
    pass


class EndpointInterfaceUrlString143(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString143DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString143Defaults"]
    merge: Optional["EndpointInterfaceUrlString143Merge"]
    parse: Optional["EndpointInterfaceUrlString143Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString143DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString143Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString143Merge(BaseModel):
    pass


class EndpointInterfaceUrlString143Parse(BaseModel):
    pass


class EndpointInterfaceUrlString144(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString144DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString144Defaults"]
    merge: Optional["EndpointInterfaceUrlString144Merge"]
    parse: Optional["EndpointInterfaceUrlString144Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString144DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString144Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString144Merge(BaseModel):
    pass


class EndpointInterfaceUrlString144Parse(BaseModel):
    pass


class EndpointInterfaceUrlString145(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString145DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString145Defaults"]
    merge: Optional["EndpointInterfaceUrlString145Merge"]
    parse: Optional["EndpointInterfaceUrlString145Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString145DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString145Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString145Merge(BaseModel):
    pass


class EndpointInterfaceUrlString145Parse(BaseModel):
    pass


class EndpointInterfaceUrlString146(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString146DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString146Defaults"]
    merge: Optional["EndpointInterfaceUrlString146Merge"]
    parse: Optional["EndpointInterfaceUrlString146Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString146DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString146Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString146Merge(BaseModel):
    pass


class EndpointInterfaceUrlString146Parse(BaseModel):
    pass


class EndpointInterfaceUrlString147(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString147DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString147Defaults"]
    merge: Optional["EndpointInterfaceUrlString147Merge"]
    parse: Optional["EndpointInterfaceUrlString147Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString147DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString147Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString147Merge(BaseModel):
    pass


class EndpointInterfaceUrlString147Parse(BaseModel):
    pass


class EndpointInterfaceUrlString148(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString148DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString148Defaults"]
    merge: Optional["EndpointInterfaceUrlString148Merge"]
    parse: Optional["EndpointInterfaceUrlString148Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString148DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString148Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString148Merge(BaseModel):
    pass


class EndpointInterfaceUrlString148Parse(BaseModel):
    pass


class EndpointInterfaceUrlString149(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString149DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString149Defaults"]
    merge: Optional["EndpointInterfaceUrlString149Merge"]
    parse: Optional["EndpointInterfaceUrlString149Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString149DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString149Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString149Merge(BaseModel):
    pass


class EndpointInterfaceUrlString149Parse(BaseModel):
    pass


class EndpointInterfaceUrlString14DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString14Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString14Merge(BaseModel):
    pass


class EndpointInterfaceUrlString14Parse(BaseModel):
    pass


class EndpointInterfaceUrlString15(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString15DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString15Defaults"]
    merge: Optional["EndpointInterfaceUrlString15Merge"]
    parse: Optional["EndpointInterfaceUrlString15Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString150(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString150DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString150Defaults"]
    merge: Optional["EndpointInterfaceUrlString150Merge"]
    parse: Optional["EndpointInterfaceUrlString150Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString150DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString150Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString150Merge(BaseModel):
    pass


class EndpointInterfaceUrlString150Parse(BaseModel):
    pass


class EndpointInterfaceUrlString151(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString151DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString151Defaults"]
    merge: Optional["EndpointInterfaceUrlString151Merge"]
    parse: Optional["EndpointInterfaceUrlString151Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString151DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString151Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString151Merge(BaseModel):
    pass


class EndpointInterfaceUrlString151Parse(BaseModel):
    pass


class EndpointInterfaceUrlString152(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString152DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString152Defaults"]
    merge: Optional["EndpointInterfaceUrlString152Merge"]
    parse: Optional["EndpointInterfaceUrlString152Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString152DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString152Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString152Merge(BaseModel):
    pass


class EndpointInterfaceUrlString152Parse(BaseModel):
    pass


class EndpointInterfaceUrlString153(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString153DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString153Defaults"]
    merge: Optional["EndpointInterfaceUrlString153Merge"]
    parse: Optional["EndpointInterfaceUrlString153Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString153DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString153Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString153Merge(BaseModel):
    pass


class EndpointInterfaceUrlString153Parse(BaseModel):
    pass


class EndpointInterfaceUrlString154(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString154DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString154Defaults"]
    merge: Optional["EndpointInterfaceUrlString154Merge"]
    parse: Optional["EndpointInterfaceUrlString154Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString154DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString154Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString154Merge(BaseModel):
    pass


class EndpointInterfaceUrlString154Parse(BaseModel):
    pass


class EndpointInterfaceUrlString155(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString155DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString155Defaults"]
    merge: Optional["EndpointInterfaceUrlString155Merge"]
    parse: Optional["EndpointInterfaceUrlString155Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString155DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString155Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString155Merge(BaseModel):
    pass


class EndpointInterfaceUrlString155Parse(BaseModel):
    pass


class EndpointInterfaceUrlString156(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString156DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString156Defaults"]
    merge: Optional["EndpointInterfaceUrlString156Merge"]
    parse: Optional["EndpointInterfaceUrlString156Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString156DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString156Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString156Merge(BaseModel):
    pass


class EndpointInterfaceUrlString156Parse(BaseModel):
    pass


class EndpointInterfaceUrlString157(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString157DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString157Defaults"]
    merge: Optional["EndpointInterfaceUrlString157Merge"]
    parse: Optional["EndpointInterfaceUrlString157Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString157DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString157Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString157Merge(BaseModel):
    pass


class EndpointInterfaceUrlString157Parse(BaseModel):
    pass


class EndpointInterfaceUrlString158(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString158DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString158Defaults"]
    merge: Optional["EndpointInterfaceUrlString158Merge"]
    parse: Optional["EndpointInterfaceUrlString158Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString158DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString158Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString158Merge(BaseModel):
    pass


class EndpointInterfaceUrlString158Parse(BaseModel):
    pass


class EndpointInterfaceUrlString159(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString159DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString159Defaults"]
    merge: Optional["EndpointInterfaceUrlString159Merge"]
    parse: Optional["EndpointInterfaceUrlString159Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString159DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString159Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString159Merge(BaseModel):
    pass


class EndpointInterfaceUrlString159Parse(BaseModel):
    pass


class EndpointInterfaceUrlString15DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString15Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString15Merge(BaseModel):
    pass


class EndpointInterfaceUrlString15Parse(BaseModel):
    pass


class EndpointInterfaceUrlString16(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString16DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString16Defaults"]
    merge: Optional["EndpointInterfaceUrlString16Merge"]
    parse: Optional["EndpointInterfaceUrlString16Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString160(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString160DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString160Defaults"]
    merge: Optional["EndpointInterfaceUrlString160Merge"]
    parse: Optional["EndpointInterfaceUrlString160Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString160DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString160Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString160Merge(BaseModel):
    pass


class EndpointInterfaceUrlString160Parse(BaseModel):
    pass


class EndpointInterfaceUrlString161(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString161DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString161Defaults"]
    merge: Optional["EndpointInterfaceUrlString161Merge"]
    parse: Optional["EndpointInterfaceUrlString161Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString161DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString161Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString161Merge(BaseModel):
    pass


class EndpointInterfaceUrlString161Parse(BaseModel):
    pass


class EndpointInterfaceUrlString162(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString162DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString162Defaults"]
    merge: Optional["EndpointInterfaceUrlString162Merge"]
    parse: Optional["EndpointInterfaceUrlString162Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString162DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString162Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString162Merge(BaseModel):
    pass


class EndpointInterfaceUrlString162Parse(BaseModel):
    pass


class EndpointInterfaceUrlString163(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString163DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString163Defaults"]
    merge: Optional["EndpointInterfaceUrlString163Merge"]
    parse: Optional["EndpointInterfaceUrlString163Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString163DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString163Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString163Merge(BaseModel):
    pass


class EndpointInterfaceUrlString163Parse(BaseModel):
    pass


class EndpointInterfaceUrlString164(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString164DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString164Defaults"]
    merge: Optional["EndpointInterfaceUrlString164Merge"]
    parse: Optional["EndpointInterfaceUrlString164Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString164DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString164Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString164Merge(BaseModel):
    pass


class EndpointInterfaceUrlString164Parse(BaseModel):
    pass


class EndpointInterfaceUrlString165(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString165DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString165Defaults"]
    merge: Optional["EndpointInterfaceUrlString165Merge"]
    parse: Optional["EndpointInterfaceUrlString165Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString165DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString165Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString165Merge(BaseModel):
    pass


class EndpointInterfaceUrlString165Parse(BaseModel):
    pass


class EndpointInterfaceUrlString166(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString166DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString166Defaults"]
    merge: Optional["EndpointInterfaceUrlString166Merge"]
    parse: Optional["EndpointInterfaceUrlString166Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString166DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString166Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString166Merge(BaseModel):
    pass


class EndpointInterfaceUrlString166Parse(BaseModel):
    pass


class EndpointInterfaceUrlString167(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString167DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString167Defaults"]
    merge: Optional["EndpointInterfaceUrlString167Merge"]
    parse: Optional["EndpointInterfaceUrlString167Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString167DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString167Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString167Merge(BaseModel):
    pass


class EndpointInterfaceUrlString167Parse(BaseModel):
    pass


class EndpointInterfaceUrlString168(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString168DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString168Defaults"]
    merge: Optional["EndpointInterfaceUrlString168Merge"]
    parse: Optional["EndpointInterfaceUrlString168Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString168DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString168Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString168Merge(BaseModel):
    pass


class EndpointInterfaceUrlString168Parse(BaseModel):
    pass


class EndpointInterfaceUrlString169(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString169DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString169Defaults"]
    merge: Optional["EndpointInterfaceUrlString169Merge"]
    parse: Optional["EndpointInterfaceUrlString169Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString169DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString169Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString169Merge(BaseModel):
    pass


class EndpointInterfaceUrlString169Parse(BaseModel):
    pass


class EndpointInterfaceUrlString16DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString16Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString16Merge(BaseModel):
    pass


class EndpointInterfaceUrlString16Parse(BaseModel):
    pass


class EndpointInterfaceUrlString17(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString17DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString17Defaults"]
    merge: Optional["EndpointInterfaceUrlString17Merge"]
    parse: Optional["EndpointInterfaceUrlString17Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString170(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString170DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString170Defaults"]
    merge: Optional["EndpointInterfaceUrlString170Merge"]
    parse: Optional["EndpointInterfaceUrlString170Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString170DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString170Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString170Merge(BaseModel):
    pass


class EndpointInterfaceUrlString170Parse(BaseModel):
    pass


class EndpointInterfaceUrlString171(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString171DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString171Defaults"]
    merge: Optional["EndpointInterfaceUrlString171Merge"]
    parse: Optional["EndpointInterfaceUrlString171Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString171DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString171Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString171Merge(BaseModel):
    pass


class EndpointInterfaceUrlString171Parse(BaseModel):
    pass


class EndpointInterfaceUrlString172(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString172DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString172Defaults"]
    merge: Optional["EndpointInterfaceUrlString172Merge"]
    parse: Optional["EndpointInterfaceUrlString172Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString172DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString172Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString172Merge(BaseModel):
    pass


class EndpointInterfaceUrlString172Parse(BaseModel):
    pass


class EndpointInterfaceUrlString173(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString173DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString173Defaults"]
    merge: Optional["EndpointInterfaceUrlString173Merge"]
    parse: Optional["EndpointInterfaceUrlString173Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString173DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString173Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString173Merge(BaseModel):
    pass


class EndpointInterfaceUrlString173Parse(BaseModel):
    pass


class EndpointInterfaceUrlString174(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString174DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString174Defaults"]
    merge: Optional["EndpointInterfaceUrlString174Merge"]
    parse: Optional["EndpointInterfaceUrlString174Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString174DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString174Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString174Merge(BaseModel):
    pass


class EndpointInterfaceUrlString174Parse(BaseModel):
    pass


class EndpointInterfaceUrlString175(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString175DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString175Defaults"]
    merge: Optional["EndpointInterfaceUrlString175Merge"]
    parse: Optional["EndpointInterfaceUrlString175Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString175DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString175Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString175Merge(BaseModel):
    pass


class EndpointInterfaceUrlString175Parse(BaseModel):
    pass


class EndpointInterfaceUrlString176(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString176DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString176Defaults"]
    merge: Optional["EndpointInterfaceUrlString176Merge"]
    parse: Optional["EndpointInterfaceUrlString176Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString176DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString176Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString176Merge(BaseModel):
    pass


class EndpointInterfaceUrlString176Parse(BaseModel):
    pass


class EndpointInterfaceUrlString177(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString177DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString177Defaults"]
    merge: Optional["EndpointInterfaceUrlString177Merge"]
    parse: Optional["EndpointInterfaceUrlString177Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString177DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString177Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString177Merge(BaseModel):
    pass


class EndpointInterfaceUrlString177Parse(BaseModel):
    pass


class EndpointInterfaceUrlString178(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString178DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString178Defaults"]
    merge: Optional["EndpointInterfaceUrlString178Merge"]
    parse: Optional["EndpointInterfaceUrlString178Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString178DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString178Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString178Merge(BaseModel):
    pass


class EndpointInterfaceUrlString178Parse(BaseModel):
    pass


class EndpointInterfaceUrlString179(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString179DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString179Defaults"]
    merge: Optional["EndpointInterfaceUrlString179Merge"]
    parse: Optional["EndpointInterfaceUrlString179Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString179DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString179Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString179Merge(BaseModel):
    pass


class EndpointInterfaceUrlString179Parse(BaseModel):
    pass


class EndpointInterfaceUrlString17DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString17Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString17Merge(BaseModel):
    pass


class EndpointInterfaceUrlString17Parse(BaseModel):
    pass


class EndpointInterfaceUrlString18(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString18DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString18Defaults"]
    merge: Optional["EndpointInterfaceUrlString18Merge"]
    parse: Optional["EndpointInterfaceUrlString18Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString180(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString180DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString180Defaults"]
    merge: Optional["EndpointInterfaceUrlString180Merge"]
    parse: Optional["EndpointInterfaceUrlString180Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString180DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString180Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString180Merge(BaseModel):
    pass


class EndpointInterfaceUrlString180Parse(BaseModel):
    pass


class EndpointInterfaceUrlString181(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString181DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString181Defaults"]
    merge: Optional["EndpointInterfaceUrlString181Merge"]
    parse: Optional["EndpointInterfaceUrlString181Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString181DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString181Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString181Merge(BaseModel):
    pass


class EndpointInterfaceUrlString181Parse(BaseModel):
    pass


class EndpointInterfaceUrlString182(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString182DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString182Defaults"]
    merge: Optional["EndpointInterfaceUrlString182Merge"]
    parse: Optional["EndpointInterfaceUrlString182Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString182DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString182Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString182Merge(BaseModel):
    pass


class EndpointInterfaceUrlString182Parse(BaseModel):
    pass


class EndpointInterfaceUrlString183(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString183DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString183Defaults"]
    merge: Optional["EndpointInterfaceUrlString183Merge"]
    parse: Optional["EndpointInterfaceUrlString183Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString183DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString183Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString183Merge(BaseModel):
    pass


class EndpointInterfaceUrlString183Parse(BaseModel):
    pass


class EndpointInterfaceUrlString184(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString184DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString184Defaults"]
    merge: Optional["EndpointInterfaceUrlString184Merge"]
    parse: Optional["EndpointInterfaceUrlString184Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString184DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString184Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString184Merge(BaseModel):
    pass


class EndpointInterfaceUrlString184Parse(BaseModel):
    pass


class EndpointInterfaceUrlString185(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString185DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString185Defaults"]
    merge: Optional["EndpointInterfaceUrlString185Merge"]
    parse: Optional["EndpointInterfaceUrlString185Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString185DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString185Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString185Merge(BaseModel):
    pass


class EndpointInterfaceUrlString185Parse(BaseModel):
    pass


class EndpointInterfaceUrlString186(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString186DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString186Defaults"]
    merge: Optional["EndpointInterfaceUrlString186Merge"]
    parse: Optional["EndpointInterfaceUrlString186Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString186DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString186Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString186Merge(BaseModel):
    pass


class EndpointInterfaceUrlString186Parse(BaseModel):
    pass


class EndpointInterfaceUrlString187(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString187DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString187Defaults"]
    merge: Optional["EndpointInterfaceUrlString187Merge"]
    parse: Optional["EndpointInterfaceUrlString187Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString187DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString187Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString187Merge(BaseModel):
    pass


class EndpointInterfaceUrlString187Parse(BaseModel):
    pass


class EndpointInterfaceUrlString188(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString188DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString188Defaults"]
    merge: Optional["EndpointInterfaceUrlString188Merge"]
    parse: Optional["EndpointInterfaceUrlString188Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString188DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString188Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString188Merge(BaseModel):
    pass


class EndpointInterfaceUrlString188Parse(BaseModel):
    pass


class EndpointInterfaceUrlString189(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString189DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString189Defaults"]
    merge: Optional["EndpointInterfaceUrlString189Merge"]
    parse: Optional["EndpointInterfaceUrlString189Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString189DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString189Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString189Merge(BaseModel):
    pass


class EndpointInterfaceUrlString189Parse(BaseModel):
    pass


class EndpointInterfaceUrlString18DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString18Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString18Merge(BaseModel):
    pass


class EndpointInterfaceUrlString18Parse(BaseModel):
    pass


class EndpointInterfaceUrlString19(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString19DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString19Defaults"]
    merge: Optional["EndpointInterfaceUrlString19Merge"]
    parse: Optional["EndpointInterfaceUrlString19Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString190(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString190DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString190Defaults"]
    merge: Optional["EndpointInterfaceUrlString190Merge"]
    parse: Optional["EndpointInterfaceUrlString190Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString190DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString190Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString190Merge(BaseModel):
    pass


class EndpointInterfaceUrlString190Parse(BaseModel):
    pass


class EndpointInterfaceUrlString191(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString191DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString191Defaults"]
    merge: Optional["EndpointInterfaceUrlString191Merge"]
    parse: Optional["EndpointInterfaceUrlString191Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString191DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString191Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString191Merge(BaseModel):
    pass


class EndpointInterfaceUrlString191Parse(BaseModel):
    pass


class EndpointInterfaceUrlString192(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString192DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString192Defaults"]
    merge: Optional["EndpointInterfaceUrlString192Merge"]
    parse: Optional["EndpointInterfaceUrlString192Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString192DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString192Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString192Merge(BaseModel):
    pass


class EndpointInterfaceUrlString192Parse(BaseModel):
    pass


class EndpointInterfaceUrlString193(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString193DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString193Defaults"]
    merge: Optional["EndpointInterfaceUrlString193Merge"]
    parse: Optional["EndpointInterfaceUrlString193Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString193DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString193Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString193Merge(BaseModel):
    pass


class EndpointInterfaceUrlString193Parse(BaseModel):
    pass


class EndpointInterfaceUrlString194(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString194DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString194Defaults"]
    merge: Optional["EndpointInterfaceUrlString194Merge"]
    parse: Optional["EndpointInterfaceUrlString194Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString194DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString194Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString194Merge(BaseModel):
    pass


class EndpointInterfaceUrlString194Parse(BaseModel):
    pass


class EndpointInterfaceUrlString195(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString195DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString195Defaults"]
    merge: Optional["EndpointInterfaceUrlString195Merge"]
    parse: Optional["EndpointInterfaceUrlString195Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString195DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString195Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString195Merge(BaseModel):
    pass


class EndpointInterfaceUrlString195Parse(BaseModel):
    pass


class EndpointInterfaceUrlString196(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString196DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString196Defaults"]
    merge: Optional["EndpointInterfaceUrlString196Merge"]
    parse: Optional["EndpointInterfaceUrlString196Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString196DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString196Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString196Merge(BaseModel):
    pass


class EndpointInterfaceUrlString196Parse(BaseModel):
    pass


class EndpointInterfaceUrlString197(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString197DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString197Defaults"]
    merge: Optional["EndpointInterfaceUrlString197Merge"]
    parse: Optional["EndpointInterfaceUrlString197Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString197DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString197Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString197Merge(BaseModel):
    pass


class EndpointInterfaceUrlString197Parse(BaseModel):
    pass


class EndpointInterfaceUrlString198(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString198DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString198Defaults"]
    merge: Optional["EndpointInterfaceUrlString198Merge"]
    parse: Optional["EndpointInterfaceUrlString198Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString198DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString198Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString198Merge(BaseModel):
    pass


class EndpointInterfaceUrlString198Parse(BaseModel):
    pass


class EndpointInterfaceUrlString199(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString199DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString199Defaults"]
    merge: Optional["EndpointInterfaceUrlString199Merge"]
    parse: Optional["EndpointInterfaceUrlString199Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString199DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString199Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString199Merge(BaseModel):
    pass


class EndpointInterfaceUrlString199Parse(BaseModel):
    pass


class EndpointInterfaceUrlString19DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString19Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString19Merge(BaseModel):
    pass


class EndpointInterfaceUrlString19Parse(BaseModel):
    pass


class EndpointInterfaceUrlString1DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString1Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString1Merge(BaseModel):
    pass


class EndpointInterfaceUrlString1Parse(BaseModel):
    pass


class EndpointInterfaceUrlString2(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString2DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString2Defaults"]
    merge: Optional["EndpointInterfaceUrlString2Merge"]
    parse: Optional["EndpointInterfaceUrlString2Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString20(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString20DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString20Defaults"]
    merge: Optional["EndpointInterfaceUrlString20Merge"]
    parse: Optional["EndpointInterfaceUrlString20Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString200(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString200DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString200Defaults"]
    merge: Optional["EndpointInterfaceUrlString200Merge"]
    parse: Optional["EndpointInterfaceUrlString200Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString200DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString200Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString200Merge(BaseModel):
    pass


class EndpointInterfaceUrlString200Parse(BaseModel):
    pass


class EndpointInterfaceUrlString201(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString201DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString201Defaults"]
    merge: Optional["EndpointInterfaceUrlString201Merge"]
    parse: Optional["EndpointInterfaceUrlString201Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString201DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString201Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString201Merge(BaseModel):
    pass


class EndpointInterfaceUrlString201Parse(BaseModel):
    pass


class EndpointInterfaceUrlString202(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString202DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString202Defaults"]
    merge: Optional["EndpointInterfaceUrlString202Merge"]
    parse: Optional["EndpointInterfaceUrlString202Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString202DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString202Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString202Merge(BaseModel):
    pass


class EndpointInterfaceUrlString202Parse(BaseModel):
    pass


class EndpointInterfaceUrlString203(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString203DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString203Defaults"]
    merge: Optional["EndpointInterfaceUrlString203Merge"]
    parse: Optional["EndpointInterfaceUrlString203Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString203DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString203Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString203Merge(BaseModel):
    pass


class EndpointInterfaceUrlString203Parse(BaseModel):
    pass


class EndpointInterfaceUrlString204(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString204DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString204Defaults"]
    merge: Optional["EndpointInterfaceUrlString204Merge"]
    parse: Optional["EndpointInterfaceUrlString204Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString204DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString204Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString204Merge(BaseModel):
    pass


class EndpointInterfaceUrlString204Parse(BaseModel):
    pass


class EndpointInterfaceUrlString205(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString205DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString205Defaults"]
    merge: Optional["EndpointInterfaceUrlString205Merge"]
    parse: Optional["EndpointInterfaceUrlString205Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString205DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString205Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString205Merge(BaseModel):
    pass


class EndpointInterfaceUrlString205Parse(BaseModel):
    pass


class EndpointInterfaceUrlString206(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString206DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString206Defaults"]
    merge: Optional["EndpointInterfaceUrlString206Merge"]
    parse: Optional["EndpointInterfaceUrlString206Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString206DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString206Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString206Merge(BaseModel):
    pass


class EndpointInterfaceUrlString206Parse(BaseModel):
    pass


class EndpointInterfaceUrlString207(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString207DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString207Defaults"]
    merge: Optional["EndpointInterfaceUrlString207Merge"]
    parse: Optional["EndpointInterfaceUrlString207Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString207DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString207Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString207Merge(BaseModel):
    pass


class EndpointInterfaceUrlString207Parse(BaseModel):
    pass


class EndpointInterfaceUrlString208(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString208DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString208Defaults"]
    merge: Optional["EndpointInterfaceUrlString208Merge"]
    parse: Optional["EndpointInterfaceUrlString208Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString208DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString208Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString208Merge(BaseModel):
    pass


class EndpointInterfaceUrlString208Parse(BaseModel):
    pass


class EndpointInterfaceUrlString209(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString209DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString209Defaults"]
    merge: Optional["EndpointInterfaceUrlString209Merge"]
    parse: Optional["EndpointInterfaceUrlString209Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString209DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString209Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString209Merge(BaseModel):
    pass


class EndpointInterfaceUrlString209Parse(BaseModel):
    pass


class EndpointInterfaceUrlString20DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString20Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString20Merge(BaseModel):
    pass


class EndpointInterfaceUrlString20Parse(BaseModel):
    pass


class EndpointInterfaceUrlString21(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString21DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString21Defaults"]
    merge: Optional["EndpointInterfaceUrlString21Merge"]
    parse: Optional["EndpointInterfaceUrlString21Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString210(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString210DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString210Defaults"]
    merge: Optional["EndpointInterfaceUrlString210Merge"]
    parse: Optional["EndpointInterfaceUrlString210Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString210DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString210Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString210Merge(BaseModel):
    pass


class EndpointInterfaceUrlString210Parse(BaseModel):
    pass


class EndpointInterfaceUrlString211(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString211DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString211Defaults"]
    merge: Optional["EndpointInterfaceUrlString211Merge"]
    parse: Optional["EndpointInterfaceUrlString211Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString211DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString211Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString211Merge(BaseModel):
    pass


class EndpointInterfaceUrlString211Parse(BaseModel):
    pass


class EndpointInterfaceUrlString212(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString212DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString212Defaults"]
    merge: Optional["EndpointInterfaceUrlString212Merge"]
    parse: Optional["EndpointInterfaceUrlString212Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString212DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString212Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString212Merge(BaseModel):
    pass


class EndpointInterfaceUrlString212Parse(BaseModel):
    pass


class EndpointInterfaceUrlString213(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString213DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString213Defaults"]
    merge: Optional["EndpointInterfaceUrlString213Merge"]
    parse: Optional["EndpointInterfaceUrlString213Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString213DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString213Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString213Merge(BaseModel):
    pass


class EndpointInterfaceUrlString213Parse(BaseModel):
    pass


class EndpointInterfaceUrlString214(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString214DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString214Defaults"]
    merge: Optional["EndpointInterfaceUrlString214Merge"]
    parse: Optional["EndpointInterfaceUrlString214Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString214DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString214Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString214Merge(BaseModel):
    pass


class EndpointInterfaceUrlString214Parse(BaseModel):
    pass


class EndpointInterfaceUrlString215(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString215DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString215Defaults"]
    merge: Optional["EndpointInterfaceUrlString215Merge"]
    parse: Optional["EndpointInterfaceUrlString215Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString215DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString215Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString215Merge(BaseModel):
    pass


class EndpointInterfaceUrlString215Parse(BaseModel):
    pass


class EndpointInterfaceUrlString216(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString216DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString216Defaults"]
    merge: Optional["EndpointInterfaceUrlString216Merge"]
    parse: Optional["EndpointInterfaceUrlString216Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString216DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString216Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString216Merge(BaseModel):
    pass


class EndpointInterfaceUrlString216Parse(BaseModel):
    pass


class EndpointInterfaceUrlString217(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString217DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString217Defaults"]
    merge: Optional["EndpointInterfaceUrlString217Merge"]
    parse: Optional["EndpointInterfaceUrlString217Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString217DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString217Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString217Merge(BaseModel):
    pass


class EndpointInterfaceUrlString217Parse(BaseModel):
    pass


class EndpointInterfaceUrlString218(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString218DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString218Defaults"]
    merge: Optional["EndpointInterfaceUrlString218Merge"]
    parse: Optional["EndpointInterfaceUrlString218Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString218DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString218Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString218Merge(BaseModel):
    pass


class EndpointInterfaceUrlString218Parse(BaseModel):
    pass


class EndpointInterfaceUrlString219(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString219DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString219Defaults"]
    merge: Optional["EndpointInterfaceUrlString219Merge"]
    parse: Optional["EndpointInterfaceUrlString219Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString219DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString219Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString219Merge(BaseModel):
    pass


class EndpointInterfaceUrlString219Parse(BaseModel):
    pass


class EndpointInterfaceUrlString21DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString21Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString21Merge(BaseModel):
    pass


class EndpointInterfaceUrlString21Parse(BaseModel):
    pass


class EndpointInterfaceUrlString22(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString22DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString22Defaults"]
    merge: Optional["EndpointInterfaceUrlString22Merge"]
    parse: Optional["EndpointInterfaceUrlString22Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString220(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString220DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString220Defaults"]
    merge: Optional["EndpointInterfaceUrlString220Merge"]
    parse: Optional["EndpointInterfaceUrlString220Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString220DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString220Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString220Merge(BaseModel):
    pass


class EndpointInterfaceUrlString220Parse(BaseModel):
    pass


class EndpointInterfaceUrlString221(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString221DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString221Defaults"]
    merge: Optional["EndpointInterfaceUrlString221Merge"]
    parse: Optional["EndpointInterfaceUrlString221Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString221DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString221Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString221Merge(BaseModel):
    pass


class EndpointInterfaceUrlString221Parse(BaseModel):
    pass


class EndpointInterfaceUrlString222(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString222DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString222Defaults"]
    merge: Optional["EndpointInterfaceUrlString222Merge"]
    parse: Optional["EndpointInterfaceUrlString222Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString222DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString222Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString222Merge(BaseModel):
    pass


class EndpointInterfaceUrlString222Parse(BaseModel):
    pass


class EndpointInterfaceUrlString223(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString223DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString223Defaults"]
    merge: Optional["EndpointInterfaceUrlString223Merge"]
    parse: Optional["EndpointInterfaceUrlString223Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString223DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString223Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString223Merge(BaseModel):
    pass


class EndpointInterfaceUrlString223Parse(BaseModel):
    pass


class EndpointInterfaceUrlString224(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString224DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString224Defaults"]
    merge: Optional["EndpointInterfaceUrlString224Merge"]
    parse: Optional["EndpointInterfaceUrlString224Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString224DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString224Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString224Merge(BaseModel):
    pass


class EndpointInterfaceUrlString224Parse(BaseModel):
    pass


class EndpointInterfaceUrlString225(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString225DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString225Defaults"]
    merge: Optional["EndpointInterfaceUrlString225Merge"]
    parse: Optional["EndpointInterfaceUrlString225Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString225DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString225Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString225Merge(BaseModel):
    pass


class EndpointInterfaceUrlString225Parse(BaseModel):
    pass


class EndpointInterfaceUrlString226(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString226DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString226Defaults"]
    merge: Optional["EndpointInterfaceUrlString226Merge"]
    parse: Optional["EndpointInterfaceUrlString226Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString226DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString226Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString226Merge(BaseModel):
    pass


class EndpointInterfaceUrlString226Parse(BaseModel):
    pass


class EndpointInterfaceUrlString227(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString227DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString227Defaults"]
    merge: Optional["EndpointInterfaceUrlString227Merge"]
    parse: Optional["EndpointInterfaceUrlString227Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString227DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString227Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString227Merge(BaseModel):
    pass


class EndpointInterfaceUrlString227Parse(BaseModel):
    pass


class EndpointInterfaceUrlString228(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString228DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString228Defaults"]
    merge: Optional["EndpointInterfaceUrlString228Merge"]
    parse: Optional["EndpointInterfaceUrlString228Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString228DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString228Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString228Merge(BaseModel):
    pass


class EndpointInterfaceUrlString228Parse(BaseModel):
    pass


class EndpointInterfaceUrlString229(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString229DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString229Defaults"]
    merge: Optional["EndpointInterfaceUrlString229Merge"]
    parse: Optional["EndpointInterfaceUrlString229Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString229DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString229Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString229Merge(BaseModel):
    pass


class EndpointInterfaceUrlString229Parse(BaseModel):
    pass


class EndpointInterfaceUrlString22DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString22Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString22Merge(BaseModel):
    pass


class EndpointInterfaceUrlString22Parse(BaseModel):
    pass


class EndpointInterfaceUrlString23(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString23DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString23Defaults"]
    merge: Optional["EndpointInterfaceUrlString23Merge"]
    parse: Optional["EndpointInterfaceUrlString23Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString230(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString230DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString230Defaults"]
    merge: Optional["EndpointInterfaceUrlString230Merge"]
    parse: Optional["EndpointInterfaceUrlString230Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString230DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString230Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString230Merge(BaseModel):
    pass


class EndpointInterfaceUrlString230Parse(BaseModel):
    pass


class EndpointInterfaceUrlString231(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString231DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString231Defaults"]
    merge: Optional["EndpointInterfaceUrlString231Merge"]
    parse: Optional["EndpointInterfaceUrlString231Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString231DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString231Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString231Merge(BaseModel):
    pass


class EndpointInterfaceUrlString231Parse(BaseModel):
    pass


class EndpointInterfaceUrlString232(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString232DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString232Defaults"]
    merge: Optional["EndpointInterfaceUrlString232Merge"]
    parse: Optional["EndpointInterfaceUrlString232Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString232DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString232Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString232Merge(BaseModel):
    pass


class EndpointInterfaceUrlString232Parse(BaseModel):
    pass


class EndpointInterfaceUrlString233(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString233DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString233Defaults"]
    merge: Optional["EndpointInterfaceUrlString233Merge"]
    parse: Optional["EndpointInterfaceUrlString233Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString233DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString233Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString233Merge(BaseModel):
    pass


class EndpointInterfaceUrlString233Parse(BaseModel):
    pass


class EndpointInterfaceUrlString234(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString234DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString234Defaults"]
    merge: Optional["EndpointInterfaceUrlString234Merge"]
    parse: Optional["EndpointInterfaceUrlString234Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString234DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString234Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString234Merge(BaseModel):
    pass


class EndpointInterfaceUrlString234Parse(BaseModel):
    pass


class EndpointInterfaceUrlString235(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString235DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString235Defaults"]
    merge: Optional["EndpointInterfaceUrlString235Merge"]
    parse: Optional["EndpointInterfaceUrlString235Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString235DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString235Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString235Merge(BaseModel):
    pass


class EndpointInterfaceUrlString235Parse(BaseModel):
    pass


class EndpointInterfaceUrlString236(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString236DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString236Defaults"]
    merge: Optional["EndpointInterfaceUrlString236Merge"]
    parse: Optional["EndpointInterfaceUrlString236Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString236DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString236Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString236Merge(BaseModel):
    pass


class EndpointInterfaceUrlString236Parse(BaseModel):
    pass


class EndpointInterfaceUrlString237(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString237DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString237Defaults"]
    merge: Optional["EndpointInterfaceUrlString237Merge"]
    parse: Optional["EndpointInterfaceUrlString237Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString237DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString237Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString237Merge(BaseModel):
    pass


class EndpointInterfaceUrlString237Parse(BaseModel):
    pass


class EndpointInterfaceUrlString238(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString238DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString238Defaults"]
    merge: Optional["EndpointInterfaceUrlString238Merge"]
    parse: Optional["EndpointInterfaceUrlString238Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString238DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString238Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString238Merge(BaseModel):
    pass


class EndpointInterfaceUrlString238Parse(BaseModel):
    pass


class EndpointInterfaceUrlString239(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString239DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString239Defaults"]
    merge: Optional["EndpointInterfaceUrlString239Merge"]
    parse: Optional["EndpointInterfaceUrlString239Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString239DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString239Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString239Merge(BaseModel):
    pass


class EndpointInterfaceUrlString239Parse(BaseModel):
    pass


class EndpointInterfaceUrlString23DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString23Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString23Merge(BaseModel):
    pass


class EndpointInterfaceUrlString23Parse(BaseModel):
    pass


class EndpointInterfaceUrlString24(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString24DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString24Defaults"]
    merge: Optional["EndpointInterfaceUrlString24Merge"]
    parse: Optional["EndpointInterfaceUrlString24Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString240(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString240DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString240Defaults"]
    merge: Optional["EndpointInterfaceUrlString240Merge"]
    parse: Optional["EndpointInterfaceUrlString240Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString240DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString240Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString240Merge(BaseModel):
    pass


class EndpointInterfaceUrlString240Parse(BaseModel):
    pass


class EndpointInterfaceUrlString241(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString241DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString241Defaults"]
    merge: Optional["EndpointInterfaceUrlString241Merge"]
    parse: Optional["EndpointInterfaceUrlString241Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString241DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString241Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString241Merge(BaseModel):
    pass


class EndpointInterfaceUrlString241Parse(BaseModel):
    pass


class EndpointInterfaceUrlString242(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString242DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString242Defaults"]
    merge: Optional["EndpointInterfaceUrlString242Merge"]
    parse: Optional["EndpointInterfaceUrlString242Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString242DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString242Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString242Merge(BaseModel):
    pass


class EndpointInterfaceUrlString242Parse(BaseModel):
    pass


class EndpointInterfaceUrlString243(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString243DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString243Defaults"]
    merge: Optional["EndpointInterfaceUrlString243Merge"]
    parse: Optional["EndpointInterfaceUrlString243Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString243DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString243Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString243Merge(BaseModel):
    pass


class EndpointInterfaceUrlString243Parse(BaseModel):
    pass


class EndpointInterfaceUrlString244(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString244DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString244Defaults"]
    merge: Optional["EndpointInterfaceUrlString244Merge"]
    parse: Optional["EndpointInterfaceUrlString244Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString244DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString244Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString244Merge(BaseModel):
    pass


class EndpointInterfaceUrlString244Parse(BaseModel):
    pass


class EndpointInterfaceUrlString245(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString245DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString245Defaults"]
    merge: Optional["EndpointInterfaceUrlString245Merge"]
    parse: Optional["EndpointInterfaceUrlString245Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString245DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString245Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString245Merge(BaseModel):
    pass


class EndpointInterfaceUrlString245Parse(BaseModel):
    pass


class EndpointInterfaceUrlString246(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString246DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString246Defaults"]
    merge: Optional["EndpointInterfaceUrlString246Merge"]
    parse: Optional["EndpointInterfaceUrlString246Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString246DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString246Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString246Merge(BaseModel):
    pass


class EndpointInterfaceUrlString246Parse(BaseModel):
    pass


class EndpointInterfaceUrlString247(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString247DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString247Defaults"]
    merge: Optional["EndpointInterfaceUrlString247Merge"]
    parse: Optional["EndpointInterfaceUrlString247Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString247DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString247Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString247Merge(BaseModel):
    pass


class EndpointInterfaceUrlString247Parse(BaseModel):
    pass


class EndpointInterfaceUrlString248(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString248DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString248Defaults"]
    merge: Optional["EndpointInterfaceUrlString248Merge"]
    parse: Optional["EndpointInterfaceUrlString248Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString248DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString248Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString248Merge(BaseModel):
    pass


class EndpointInterfaceUrlString248Parse(BaseModel):
    pass


class EndpointInterfaceUrlString249(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString249DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString249Defaults"]
    merge: Optional["EndpointInterfaceUrlString249Merge"]
    parse: Optional["EndpointInterfaceUrlString249Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString249DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString249Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString249Merge(BaseModel):
    pass


class EndpointInterfaceUrlString249Parse(BaseModel):
    pass


class EndpointInterfaceUrlString24DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString24Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString24Merge(BaseModel):
    pass


class EndpointInterfaceUrlString24Parse(BaseModel):
    pass


class EndpointInterfaceUrlString25(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString25DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString25Defaults"]
    merge: Optional["EndpointInterfaceUrlString25Merge"]
    parse: Optional["EndpointInterfaceUrlString25Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString250(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString250DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString250Defaults"]
    merge: Optional["EndpointInterfaceUrlString250Merge"]
    parse: Optional["EndpointInterfaceUrlString250Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString250DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString250Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString250Merge(BaseModel):
    pass


class EndpointInterfaceUrlString250Parse(BaseModel):
    pass


class EndpointInterfaceUrlString251(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString251DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString251Defaults"]
    merge: Optional["EndpointInterfaceUrlString251Merge"]
    parse: Optional["EndpointInterfaceUrlString251Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString251DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString251Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString251Merge(BaseModel):
    pass


class EndpointInterfaceUrlString251Parse(BaseModel):
    pass


class EndpointInterfaceUrlString252(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString252DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString252Defaults"]
    merge: Optional["EndpointInterfaceUrlString252Merge"]
    parse: Optional["EndpointInterfaceUrlString252Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString252DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString252Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString252Merge(BaseModel):
    pass


class EndpointInterfaceUrlString252Parse(BaseModel):
    pass


class EndpointInterfaceUrlString253(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString253DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString253Defaults"]
    merge: Optional["EndpointInterfaceUrlString253Merge"]
    parse: Optional["EndpointInterfaceUrlString253Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString253DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString253Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString253Merge(BaseModel):
    pass


class EndpointInterfaceUrlString253Parse(BaseModel):
    pass


class EndpointInterfaceUrlString254(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString254DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString254Defaults"]
    merge: Optional["EndpointInterfaceUrlString254Merge"]
    parse: Optional["EndpointInterfaceUrlString254Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString254DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString254Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString254Merge(BaseModel):
    pass


class EndpointInterfaceUrlString254Parse(BaseModel):
    pass


class EndpointInterfaceUrlString255(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString255DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString255Defaults"]
    merge: Optional["EndpointInterfaceUrlString255Merge"]
    parse: Optional["EndpointInterfaceUrlString255Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString255DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString255Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString255Merge(BaseModel):
    pass


class EndpointInterfaceUrlString255Parse(BaseModel):
    pass


class EndpointInterfaceUrlString256(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString256DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString256Defaults"]
    merge: Optional["EndpointInterfaceUrlString256Merge"]
    parse: Optional["EndpointInterfaceUrlString256Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString256DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString256Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString256Merge(BaseModel):
    pass


class EndpointInterfaceUrlString256Parse(BaseModel):
    pass


class EndpointInterfaceUrlString257(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString257DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString257Defaults"]
    merge: Optional["EndpointInterfaceUrlString257Merge"]
    parse: Optional["EndpointInterfaceUrlString257Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString257DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString257Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString257Merge(BaseModel):
    pass


class EndpointInterfaceUrlString257Parse(BaseModel):
    pass


class EndpointInterfaceUrlString258(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString258DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString258Defaults"]
    merge: Optional["EndpointInterfaceUrlString258Merge"]
    parse: Optional["EndpointInterfaceUrlString258Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString258DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString258Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString258Merge(BaseModel):
    pass


class EndpointInterfaceUrlString258Parse(BaseModel):
    pass


class EndpointInterfaceUrlString259(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString259DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString259Defaults"]
    merge: Optional["EndpointInterfaceUrlString259Merge"]
    parse: Optional["EndpointInterfaceUrlString259Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString259DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString259Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString259Merge(BaseModel):
    pass


class EndpointInterfaceUrlString259Parse(BaseModel):
    pass


class EndpointInterfaceUrlString25DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString25Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString25Merge(BaseModel):
    pass


class EndpointInterfaceUrlString25Parse(BaseModel):
    pass


class EndpointInterfaceUrlString26(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString26DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString26Defaults"]
    merge: Optional["EndpointInterfaceUrlString26Merge"]
    parse: Optional["EndpointInterfaceUrlString26Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString260(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString260DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString260Defaults"]
    merge: Optional["EndpointInterfaceUrlString260Merge"]
    parse: Optional["EndpointInterfaceUrlString260Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString260DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString260Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString260Merge(BaseModel):
    pass


class EndpointInterfaceUrlString260Parse(BaseModel):
    pass


class EndpointInterfaceUrlString261(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString261DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString261Defaults"]
    merge: Optional["EndpointInterfaceUrlString261Merge"]
    parse: Optional["EndpointInterfaceUrlString261Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString261DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString261Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString261Merge(BaseModel):
    pass


class EndpointInterfaceUrlString261Parse(BaseModel):
    pass


class EndpointInterfaceUrlString262(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString262DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString262Defaults"]
    merge: Optional["EndpointInterfaceUrlString262Merge"]
    parse: Optional["EndpointInterfaceUrlString262Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString262DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString262Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString262Merge(BaseModel):
    pass


class EndpointInterfaceUrlString262Parse(BaseModel):
    pass


class EndpointInterfaceUrlString263(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString263DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString263Defaults"]
    merge: Optional["EndpointInterfaceUrlString263Merge"]
    parse: Optional["EndpointInterfaceUrlString263Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString263DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString263Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString263Merge(BaseModel):
    pass


class EndpointInterfaceUrlString263Parse(BaseModel):
    pass


class EndpointInterfaceUrlString264(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString264DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString264Defaults"]
    merge: Optional["EndpointInterfaceUrlString264Merge"]
    parse: Optional["EndpointInterfaceUrlString264Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString264DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString264Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString264Merge(BaseModel):
    pass


class EndpointInterfaceUrlString264Parse(BaseModel):
    pass


class EndpointInterfaceUrlString265(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString265DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString265Defaults"]
    merge: Optional["EndpointInterfaceUrlString265Merge"]
    parse: Optional["EndpointInterfaceUrlString265Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString265DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString265Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString265Merge(BaseModel):
    pass


class EndpointInterfaceUrlString265Parse(BaseModel):
    pass


class EndpointInterfaceUrlString266(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString266DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString266Defaults"]
    merge: Optional["EndpointInterfaceUrlString266Merge"]
    parse: Optional["EndpointInterfaceUrlString266Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString266DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString266Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString266Merge(BaseModel):
    pass


class EndpointInterfaceUrlString266Parse(BaseModel):
    pass


class EndpointInterfaceUrlString267(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString267DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString267Defaults"]
    merge: Optional["EndpointInterfaceUrlString267Merge"]
    parse: Optional["EndpointInterfaceUrlString267Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString267DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString267Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString267Merge(BaseModel):
    pass


class EndpointInterfaceUrlString267Parse(BaseModel):
    pass


class EndpointInterfaceUrlString268(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString268DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString268Defaults"]
    merge: Optional["EndpointInterfaceUrlString268Merge"]
    parse: Optional["EndpointInterfaceUrlString268Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString268DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString268Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString268Merge(BaseModel):
    pass


class EndpointInterfaceUrlString268Parse(BaseModel):
    pass


class EndpointInterfaceUrlString269(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString269DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString269Defaults"]
    merge: Optional["EndpointInterfaceUrlString269Merge"]
    parse: Optional["EndpointInterfaceUrlString269Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString269DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString269Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString269Merge(BaseModel):
    pass


class EndpointInterfaceUrlString269Parse(BaseModel):
    pass


class EndpointInterfaceUrlString26DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString26Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString26Merge(BaseModel):
    pass


class EndpointInterfaceUrlString26Parse(BaseModel):
    pass


class EndpointInterfaceUrlString27(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString27DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString27Defaults"]
    merge: Optional["EndpointInterfaceUrlString27Merge"]
    parse: Optional["EndpointInterfaceUrlString27Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString270(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString270DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString270Defaults"]
    merge: Optional["EndpointInterfaceUrlString270Merge"]
    parse: Optional["EndpointInterfaceUrlString270Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString270DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString270Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString270Merge(BaseModel):
    pass


class EndpointInterfaceUrlString270Parse(BaseModel):
    pass


class EndpointInterfaceUrlString271(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString271DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString271Defaults"]
    merge: Optional["EndpointInterfaceUrlString271Merge"]
    parse: Optional["EndpointInterfaceUrlString271Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString271DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString271Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString271Merge(BaseModel):
    pass


class EndpointInterfaceUrlString271Parse(BaseModel):
    pass


class EndpointInterfaceUrlString272(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString272DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString272Defaults"]
    merge: Optional["EndpointInterfaceUrlString272Merge"]
    parse: Optional["EndpointInterfaceUrlString272Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString272DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString272Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString272Merge(BaseModel):
    pass


class EndpointInterfaceUrlString272Parse(BaseModel):
    pass


class EndpointInterfaceUrlString273(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString273DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString273Defaults"]
    merge: Optional["EndpointInterfaceUrlString273Merge"]
    parse: Optional["EndpointInterfaceUrlString273Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString273DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString273Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString273Merge(BaseModel):
    pass


class EndpointInterfaceUrlString273Parse(BaseModel):
    pass


class EndpointInterfaceUrlString274(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString274DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString274Defaults"]
    merge: Optional["EndpointInterfaceUrlString274Merge"]
    parse: Optional["EndpointInterfaceUrlString274Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString274DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString274Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString274Merge(BaseModel):
    pass


class EndpointInterfaceUrlString274Parse(BaseModel):
    pass


class EndpointInterfaceUrlString275(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString275DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString275Defaults"]
    merge: Optional["EndpointInterfaceUrlString275Merge"]
    parse: Optional["EndpointInterfaceUrlString275Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString275DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString275Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString275Merge(BaseModel):
    pass


class EndpointInterfaceUrlString275Parse(BaseModel):
    pass


class EndpointInterfaceUrlString276(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString276DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString276Defaults"]
    merge: Optional["EndpointInterfaceUrlString276Merge"]
    parse: Optional["EndpointInterfaceUrlString276Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString276DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString276Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString276Merge(BaseModel):
    pass


class EndpointInterfaceUrlString276Parse(BaseModel):
    pass


class EndpointInterfaceUrlString277(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString277DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString277Defaults"]
    merge: Optional["EndpointInterfaceUrlString277Merge"]
    parse: Optional["EndpointInterfaceUrlString277Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString277DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString277Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString277Merge(BaseModel):
    pass


class EndpointInterfaceUrlString277Parse(BaseModel):
    pass


class EndpointInterfaceUrlString278(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString278DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString278Defaults"]
    merge: Optional["EndpointInterfaceUrlString278Merge"]
    parse: Optional["EndpointInterfaceUrlString278Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString278DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString278Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString278Merge(BaseModel):
    pass


class EndpointInterfaceUrlString278Parse(BaseModel):
    pass


class EndpointInterfaceUrlString279(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString279DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString279Defaults"]
    merge: Optional["EndpointInterfaceUrlString279Merge"]
    parse: Optional["EndpointInterfaceUrlString279Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString279DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString279Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString279Merge(BaseModel):
    pass


class EndpointInterfaceUrlString279Parse(BaseModel):
    pass


class EndpointInterfaceUrlString27DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString27Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString27Merge(BaseModel):
    pass


class EndpointInterfaceUrlString27Parse(BaseModel):
    pass


class EndpointInterfaceUrlString28(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString28DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString28Defaults"]
    merge: Optional["EndpointInterfaceUrlString28Merge"]
    parse: Optional["EndpointInterfaceUrlString28Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString280(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString280DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString280Defaults"]
    merge: Optional["EndpointInterfaceUrlString280Merge"]
    parse: Optional["EndpointInterfaceUrlString280Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString280DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString280Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString280Merge(BaseModel):
    pass


class EndpointInterfaceUrlString280Parse(BaseModel):
    pass


class EndpointInterfaceUrlString281(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString281DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString281Defaults"]
    merge: Optional["EndpointInterfaceUrlString281Merge"]
    parse: Optional["EndpointInterfaceUrlString281Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString281DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString281Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString281Merge(BaseModel):
    pass


class EndpointInterfaceUrlString281Parse(BaseModel):
    pass


class EndpointInterfaceUrlString282(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString282DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString282Defaults"]
    merge: Optional["EndpointInterfaceUrlString282Merge"]
    parse: Optional["EndpointInterfaceUrlString282Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString282DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString282Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString282Merge(BaseModel):
    pass


class EndpointInterfaceUrlString282Parse(BaseModel):
    pass


class EndpointInterfaceUrlString283(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString283DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString283Defaults"]
    merge: Optional["EndpointInterfaceUrlString283Merge"]
    parse: Optional["EndpointInterfaceUrlString283Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString283DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString283Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString283Merge(BaseModel):
    pass


class EndpointInterfaceUrlString283Parse(BaseModel):
    pass


class EndpointInterfaceUrlString284(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString284DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString284Defaults"]
    merge: Optional["EndpointInterfaceUrlString284Merge"]
    parse: Optional["EndpointInterfaceUrlString284Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString284DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString284Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString284Merge(BaseModel):
    pass


class EndpointInterfaceUrlString284Parse(BaseModel):
    pass


class EndpointInterfaceUrlString285(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString285DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString285Defaults"]
    merge: Optional["EndpointInterfaceUrlString285Merge"]
    parse: Optional["EndpointInterfaceUrlString285Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString285DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString285Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString285Merge(BaseModel):
    pass


class EndpointInterfaceUrlString285Parse(BaseModel):
    pass


class EndpointInterfaceUrlString286(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString286DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString286Defaults"]
    merge: Optional["EndpointInterfaceUrlString286Merge"]
    parse: Optional["EndpointInterfaceUrlString286Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString286DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString286Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString286Merge(BaseModel):
    pass


class EndpointInterfaceUrlString286Parse(BaseModel):
    pass


class EndpointInterfaceUrlString287(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString287DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString287Defaults"]
    merge: Optional["EndpointInterfaceUrlString287Merge"]
    parse: Optional["EndpointInterfaceUrlString287Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString287DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString287Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString287Merge(BaseModel):
    pass


class EndpointInterfaceUrlString287Parse(BaseModel):
    pass


class EndpointInterfaceUrlString288(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString288DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString288Defaults"]
    merge: Optional["EndpointInterfaceUrlString288Merge"]
    parse: Optional["EndpointInterfaceUrlString288Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString288DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString288Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString288Merge(BaseModel):
    pass


class EndpointInterfaceUrlString288Parse(BaseModel):
    pass


class EndpointInterfaceUrlString289(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString289DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString289Defaults"]
    merge: Optional["EndpointInterfaceUrlString289Merge"]
    parse: Optional["EndpointInterfaceUrlString289Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString289DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString289Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString289Merge(BaseModel):
    pass


class EndpointInterfaceUrlString289Parse(BaseModel):
    pass


class EndpointInterfaceUrlString28DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString28Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString28Merge(BaseModel):
    pass


class EndpointInterfaceUrlString28Parse(BaseModel):
    pass


class EndpointInterfaceUrlString29(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString29DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString29Defaults"]
    merge: Optional["EndpointInterfaceUrlString29Merge"]
    parse: Optional["EndpointInterfaceUrlString29Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString290(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString290DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString290Defaults"]
    merge: Optional["EndpointInterfaceUrlString290Merge"]
    parse: Optional["EndpointInterfaceUrlString290Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString290DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString290Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString290Merge(BaseModel):
    pass


class EndpointInterfaceUrlString290Parse(BaseModel):
    pass


class EndpointInterfaceUrlString291(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString291DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString291Defaults"]
    merge: Optional["EndpointInterfaceUrlString291Merge"]
    parse: Optional["EndpointInterfaceUrlString291Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString291DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString291Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString291Merge(BaseModel):
    pass


class EndpointInterfaceUrlString291Parse(BaseModel):
    pass


class EndpointInterfaceUrlString292(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString292DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString292Defaults"]
    merge: Optional["EndpointInterfaceUrlString292Merge"]
    parse: Optional["EndpointInterfaceUrlString292Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString292DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString292Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString292Merge(BaseModel):
    pass


class EndpointInterfaceUrlString292Parse(BaseModel):
    pass


class EndpointInterfaceUrlString293(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString293DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString293Defaults"]
    merge: Optional["EndpointInterfaceUrlString293Merge"]
    parse: Optional["EndpointInterfaceUrlString293Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString293DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString293Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString293Merge(BaseModel):
    pass


class EndpointInterfaceUrlString293Parse(BaseModel):
    pass


class EndpointInterfaceUrlString294(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString294DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString294Defaults"]
    merge: Optional["EndpointInterfaceUrlString294Merge"]
    parse: Optional["EndpointInterfaceUrlString294Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString294DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString294Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString294Merge(BaseModel):
    pass


class EndpointInterfaceUrlString294Parse(BaseModel):
    pass


class EndpointInterfaceUrlString295(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString295DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString295Defaults"]
    merge: Optional["EndpointInterfaceUrlString295Merge"]
    parse: Optional["EndpointInterfaceUrlString295Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString295DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString295Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString295Merge(BaseModel):
    pass


class EndpointInterfaceUrlString295Parse(BaseModel):
    pass


class EndpointInterfaceUrlString296(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString296DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString296Defaults"]
    merge: Optional["EndpointInterfaceUrlString296Merge"]
    parse: Optional["EndpointInterfaceUrlString296Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString296DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString296Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString296Merge(BaseModel):
    pass


class EndpointInterfaceUrlString296Parse(BaseModel):
    pass


class EndpointInterfaceUrlString297(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString297DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString297Defaults"]
    merge: Optional["EndpointInterfaceUrlString297Merge"]
    parse: Optional["EndpointInterfaceUrlString297Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString297DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString297Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString297Merge(BaseModel):
    pass


class EndpointInterfaceUrlString297Parse(BaseModel):
    pass


class EndpointInterfaceUrlString298(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString298DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString298Defaults"]
    merge: Optional["EndpointInterfaceUrlString298Merge"]
    parse: Optional["EndpointInterfaceUrlString298Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString298DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString298Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString298Merge(BaseModel):
    pass


class EndpointInterfaceUrlString298Parse(BaseModel):
    pass


class EndpointInterfaceUrlString299(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString299DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString299Defaults"]
    merge: Optional["EndpointInterfaceUrlString299Merge"]
    parse: Optional["EndpointInterfaceUrlString299Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString299DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString299Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString299Merge(BaseModel):
    pass


class EndpointInterfaceUrlString299Parse(BaseModel):
    pass


class EndpointInterfaceUrlString29DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString29Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString29Merge(BaseModel):
    pass


class EndpointInterfaceUrlString29Parse(BaseModel):
    pass


class EndpointInterfaceUrlString2DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString2Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString2Merge(BaseModel):
    pass


class EndpointInterfaceUrlString2Parse(BaseModel):
    pass


class EndpointInterfaceUrlString3(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString3DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString3Defaults"]
    merge: Optional["EndpointInterfaceUrlString3Merge"]
    parse: Optional["EndpointInterfaceUrlString3Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString30(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString30DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString30Defaults"]
    merge: Optional["EndpointInterfaceUrlString30Merge"]
    parse: Optional["EndpointInterfaceUrlString30Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString300(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString300DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString300Defaults"]
    merge: Optional["EndpointInterfaceUrlString300Merge"]
    parse: Optional["EndpointInterfaceUrlString300Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString300DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString300Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString300Merge(BaseModel):
    pass


class EndpointInterfaceUrlString300Parse(BaseModel):
    pass


class EndpointInterfaceUrlString301(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString301DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString301Defaults"]
    merge: Optional["EndpointInterfaceUrlString301Merge"]
    parse: Optional["EndpointInterfaceUrlString301Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString301DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString301Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString301Merge(BaseModel):
    pass


class EndpointInterfaceUrlString301Parse(BaseModel):
    pass


class EndpointInterfaceUrlString302(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString302DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString302Defaults"]
    merge: Optional["EndpointInterfaceUrlString302Merge"]
    parse: Optional["EndpointInterfaceUrlString302Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString302DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString302Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString302Merge(BaseModel):
    pass


class EndpointInterfaceUrlString302Parse(BaseModel):
    pass


class EndpointInterfaceUrlString303(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString303DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString303Defaults"]
    merge: Optional["EndpointInterfaceUrlString303Merge"]
    parse: Optional["EndpointInterfaceUrlString303Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString303DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString303Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString303Merge(BaseModel):
    pass


class EndpointInterfaceUrlString303Parse(BaseModel):
    pass


class EndpointInterfaceUrlString304(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString304DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString304Defaults"]
    merge: Optional["EndpointInterfaceUrlString304Merge"]
    parse: Optional["EndpointInterfaceUrlString304Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString304DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString304Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString304Merge(BaseModel):
    pass


class EndpointInterfaceUrlString304Parse(BaseModel):
    pass


class EndpointInterfaceUrlString305(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString305DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString305Defaults"]
    merge: Optional["EndpointInterfaceUrlString305Merge"]
    parse: Optional["EndpointInterfaceUrlString305Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString305DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString305Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString305Merge(BaseModel):
    pass


class EndpointInterfaceUrlString305Parse(BaseModel):
    pass


class EndpointInterfaceUrlString306(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString306DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString306Defaults"]
    merge: Optional["EndpointInterfaceUrlString306Merge"]
    parse: Optional["EndpointInterfaceUrlString306Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString306DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString306Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString306Merge(BaseModel):
    pass


class EndpointInterfaceUrlString306Parse(BaseModel):
    pass


class EndpointInterfaceUrlString307(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString307DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString307Defaults"]
    merge: Optional["EndpointInterfaceUrlString307Merge"]
    parse: Optional["EndpointInterfaceUrlString307Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString307DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString307Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString307Merge(BaseModel):
    pass


class EndpointInterfaceUrlString307Parse(BaseModel):
    pass


class EndpointInterfaceUrlString308(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString308DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString308Defaults"]
    merge: Optional["EndpointInterfaceUrlString308Merge"]
    parse: Optional["EndpointInterfaceUrlString308Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString308DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString308Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString308Merge(BaseModel):
    pass


class EndpointInterfaceUrlString308Parse(BaseModel):
    pass


class EndpointInterfaceUrlString309(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString309DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString309Defaults"]
    merge: Optional["EndpointInterfaceUrlString309Merge"]
    parse: Optional["EndpointInterfaceUrlString309Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString309DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString309Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString309Merge(BaseModel):
    pass


class EndpointInterfaceUrlString309Parse(BaseModel):
    pass


class EndpointInterfaceUrlString30DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString30Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString30Merge(BaseModel):
    pass


class EndpointInterfaceUrlString30Parse(BaseModel):
    pass


class EndpointInterfaceUrlString31(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString31DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString31Defaults"]
    merge: Optional["EndpointInterfaceUrlString31Merge"]
    parse: Optional["EndpointInterfaceUrlString31Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString310(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString310DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString310Defaults"]
    merge: Optional["EndpointInterfaceUrlString310Merge"]
    parse: Optional["EndpointInterfaceUrlString310Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString310DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString310Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString310Merge(BaseModel):
    pass


class EndpointInterfaceUrlString310Parse(BaseModel):
    pass


class EndpointInterfaceUrlString311(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString311DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString311Defaults"]
    merge: Optional["EndpointInterfaceUrlString311Merge"]
    parse: Optional["EndpointInterfaceUrlString311Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString311DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString311Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString311Merge(BaseModel):
    pass


class EndpointInterfaceUrlString311Parse(BaseModel):
    pass


class EndpointInterfaceUrlString312(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString312DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString312Defaults"]
    merge: Optional["EndpointInterfaceUrlString312Merge"]
    parse: Optional["EndpointInterfaceUrlString312Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString312DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString312Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString312Merge(BaseModel):
    pass


class EndpointInterfaceUrlString312Parse(BaseModel):
    pass


class EndpointInterfaceUrlString313(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString313DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString313Defaults"]
    merge: Optional["EndpointInterfaceUrlString313Merge"]
    parse: Optional["EndpointInterfaceUrlString313Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString313DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString313Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString313Merge(BaseModel):
    pass


class EndpointInterfaceUrlString313Parse(BaseModel):
    pass


class EndpointInterfaceUrlString314(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString314DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString314Defaults"]
    merge: Optional["EndpointInterfaceUrlString314Merge"]
    parse: Optional["EndpointInterfaceUrlString314Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString314DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString314Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString314Merge(BaseModel):
    pass


class EndpointInterfaceUrlString314Parse(BaseModel):
    pass


class EndpointInterfaceUrlString315(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString315DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString315Defaults"]
    merge: Optional["EndpointInterfaceUrlString315Merge"]
    parse: Optional["EndpointInterfaceUrlString315Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString315DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString315Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString315Merge(BaseModel):
    pass


class EndpointInterfaceUrlString315Parse(BaseModel):
    pass


class EndpointInterfaceUrlString316(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString316DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString316Defaults"]
    merge: Optional["EndpointInterfaceUrlString316Merge"]
    parse: Optional["EndpointInterfaceUrlString316Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString316DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString316Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString316Merge(BaseModel):
    pass


class EndpointInterfaceUrlString316Parse(BaseModel):
    pass


class EndpointInterfaceUrlString317(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString317DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString317Defaults"]
    merge: Optional["EndpointInterfaceUrlString317Merge"]
    parse: Optional["EndpointInterfaceUrlString317Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString317DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString317Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString317Merge(BaseModel):
    pass


class EndpointInterfaceUrlString317Parse(BaseModel):
    pass


class EndpointInterfaceUrlString318(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString318DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString318Defaults"]
    merge: Optional["EndpointInterfaceUrlString318Merge"]
    parse: Optional["EndpointInterfaceUrlString318Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString318DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString318Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString318Merge(BaseModel):
    pass


class EndpointInterfaceUrlString318Parse(BaseModel):
    pass


class EndpointInterfaceUrlString319(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString319DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString319Defaults"]
    merge: Optional["EndpointInterfaceUrlString319Merge"]
    parse: Optional["EndpointInterfaceUrlString319Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString319DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString319Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString319Merge(BaseModel):
    pass


class EndpointInterfaceUrlString319Parse(BaseModel):
    pass


class EndpointInterfaceUrlString31DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString31Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString31Merge(BaseModel):
    pass


class EndpointInterfaceUrlString31Parse(BaseModel):
    pass


class EndpointInterfaceUrlString32(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString32DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString32Defaults"]
    merge: Optional["EndpointInterfaceUrlString32Merge"]
    parse: Optional["EndpointInterfaceUrlString32Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString320(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString320DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString320Defaults"]
    merge: Optional["EndpointInterfaceUrlString320Merge"]
    parse: Optional["EndpointInterfaceUrlString320Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString320DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString320Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString320Merge(BaseModel):
    pass


class EndpointInterfaceUrlString320Parse(BaseModel):
    pass


class EndpointInterfaceUrlString321(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString321DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString321Defaults"]
    merge: Optional["EndpointInterfaceUrlString321Merge"]
    parse: Optional["EndpointInterfaceUrlString321Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString321DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString321Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString321Merge(BaseModel):
    pass


class EndpointInterfaceUrlString321Parse(BaseModel):
    pass


class EndpointInterfaceUrlString322(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString322DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString322Defaults"]
    merge: Optional["EndpointInterfaceUrlString322Merge"]
    parse: Optional["EndpointInterfaceUrlString322Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString322DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString322Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString322Merge(BaseModel):
    pass


class EndpointInterfaceUrlString322Parse(BaseModel):
    pass


class EndpointInterfaceUrlString323(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString323DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString323Defaults"]
    merge: Optional["EndpointInterfaceUrlString323Merge"]
    parse: Optional["EndpointInterfaceUrlString323Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString323DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString323Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString323Merge(BaseModel):
    pass


class EndpointInterfaceUrlString323Parse(BaseModel):
    pass


class EndpointInterfaceUrlString324(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString324DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString324Defaults"]
    merge: Optional["EndpointInterfaceUrlString324Merge"]
    parse: Optional["EndpointInterfaceUrlString324Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString324DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString324Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString324Merge(BaseModel):
    pass


class EndpointInterfaceUrlString324Parse(BaseModel):
    pass


class EndpointInterfaceUrlString325(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString325DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString325Defaults"]
    merge: Optional["EndpointInterfaceUrlString325Merge"]
    parse: Optional["EndpointInterfaceUrlString325Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString325DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString325Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString325Merge(BaseModel):
    pass


class EndpointInterfaceUrlString325Parse(BaseModel):
    pass


class EndpointInterfaceUrlString326(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString326DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString326Defaults"]
    merge: Optional["EndpointInterfaceUrlString326Merge"]
    parse: Optional["EndpointInterfaceUrlString326Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString326DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString326Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString326Merge(BaseModel):
    pass


class EndpointInterfaceUrlString326Parse(BaseModel):
    pass


class EndpointInterfaceUrlString327(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString327DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString327Defaults"]
    merge: Optional["EndpointInterfaceUrlString327Merge"]
    parse: Optional["EndpointInterfaceUrlString327Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString327DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString327Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString327Merge(BaseModel):
    pass


class EndpointInterfaceUrlString327Parse(BaseModel):
    pass


class EndpointInterfaceUrlString328(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString328DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString328Defaults"]
    merge: Optional["EndpointInterfaceUrlString328Merge"]
    parse: Optional["EndpointInterfaceUrlString328Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString328DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString328Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString328Merge(BaseModel):
    pass


class EndpointInterfaceUrlString328Parse(BaseModel):
    pass


class EndpointInterfaceUrlString329(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString329DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString329Defaults"]
    merge: Optional["EndpointInterfaceUrlString329Merge"]
    parse: Optional["EndpointInterfaceUrlString329Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString329DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString329Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString329Merge(BaseModel):
    pass


class EndpointInterfaceUrlString329Parse(BaseModel):
    pass


class EndpointInterfaceUrlString32DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString32Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString32Merge(BaseModel):
    pass


class EndpointInterfaceUrlString32Parse(BaseModel):
    pass


class EndpointInterfaceUrlString33(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString33DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString33Defaults"]
    merge: Optional["EndpointInterfaceUrlString33Merge"]
    parse: Optional["EndpointInterfaceUrlString33Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString330(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString330DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString330Defaults"]
    merge: Optional["EndpointInterfaceUrlString330Merge"]
    parse: Optional["EndpointInterfaceUrlString330Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString330DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString330Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString330Merge(BaseModel):
    pass


class EndpointInterfaceUrlString330Parse(BaseModel):
    pass


class EndpointInterfaceUrlString331(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString331DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString331Defaults"]
    merge: Optional["EndpointInterfaceUrlString331Merge"]
    parse: Optional["EndpointInterfaceUrlString331Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString331DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString331Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString331Merge(BaseModel):
    pass


class EndpointInterfaceUrlString331Parse(BaseModel):
    pass


class EndpointInterfaceUrlString332(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString332DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString332Defaults"]
    merge: Optional["EndpointInterfaceUrlString332Merge"]
    parse: Optional["EndpointInterfaceUrlString332Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString332DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString332Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString332Merge(BaseModel):
    pass


class EndpointInterfaceUrlString332Parse(BaseModel):
    pass


class EndpointInterfaceUrlString333(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString333DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString333Defaults"]
    merge: Optional["EndpointInterfaceUrlString333Merge"]
    parse: Optional["EndpointInterfaceUrlString333Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString333DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString333Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString333Merge(BaseModel):
    pass


class EndpointInterfaceUrlString333Parse(BaseModel):
    pass


class EndpointInterfaceUrlString334(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString334DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString334Defaults"]
    merge: Optional["EndpointInterfaceUrlString334Merge"]
    parse: Optional["EndpointInterfaceUrlString334Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString334DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString334Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString334Merge(BaseModel):
    pass


class EndpointInterfaceUrlString334Parse(BaseModel):
    pass


class EndpointInterfaceUrlString335(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString335DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString335Defaults"]
    merge: Optional["EndpointInterfaceUrlString335Merge"]
    parse: Optional["EndpointInterfaceUrlString335Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString335DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString335Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString335Merge(BaseModel):
    pass


class EndpointInterfaceUrlString335Parse(BaseModel):
    pass


class EndpointInterfaceUrlString336(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString336DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString336Defaults"]
    merge: Optional["EndpointInterfaceUrlString336Merge"]
    parse: Optional["EndpointInterfaceUrlString336Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString336DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString336Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString336Merge(BaseModel):
    pass


class EndpointInterfaceUrlString336Parse(BaseModel):
    pass


class EndpointInterfaceUrlString337(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString337DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString337Defaults"]
    merge: Optional["EndpointInterfaceUrlString337Merge"]
    parse: Optional["EndpointInterfaceUrlString337Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString337DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString337Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString337Merge(BaseModel):
    pass


class EndpointInterfaceUrlString337Parse(BaseModel):
    pass


class EndpointInterfaceUrlString338(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString338DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString338Defaults"]
    merge: Optional["EndpointInterfaceUrlString338Merge"]
    parse: Optional["EndpointInterfaceUrlString338Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString338DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString338Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString338Merge(BaseModel):
    pass


class EndpointInterfaceUrlString338Parse(BaseModel):
    pass


class EndpointInterfaceUrlString339(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString339DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString339Defaults"]
    merge: Optional["EndpointInterfaceUrlString339Merge"]
    parse: Optional["EndpointInterfaceUrlString339Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString339DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString339Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString339Merge(BaseModel):
    pass


class EndpointInterfaceUrlString339Parse(BaseModel):
    pass


class EndpointInterfaceUrlString33DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString33Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString33Merge(BaseModel):
    pass


class EndpointInterfaceUrlString33Parse(BaseModel):
    pass


class EndpointInterfaceUrlString34(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString34DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString34Defaults"]
    merge: Optional["EndpointInterfaceUrlString34Merge"]
    parse: Optional["EndpointInterfaceUrlString34Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString340(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString340DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString340Defaults"]
    merge: Optional["EndpointInterfaceUrlString340Merge"]
    parse: Optional["EndpointInterfaceUrlString340Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString340DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString340Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString340Merge(BaseModel):
    pass


class EndpointInterfaceUrlString340Parse(BaseModel):
    pass


class EndpointInterfaceUrlString341(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString341DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString341Defaults"]
    merge: Optional["EndpointInterfaceUrlString341Merge"]
    parse: Optional["EndpointInterfaceUrlString341Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString341DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString341Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString341Merge(BaseModel):
    pass


class EndpointInterfaceUrlString341Parse(BaseModel):
    pass


class EndpointInterfaceUrlString342(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString342DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString342Defaults"]
    merge: Optional["EndpointInterfaceUrlString342Merge"]
    parse: Optional["EndpointInterfaceUrlString342Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString342DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString342Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString342Merge(BaseModel):
    pass


class EndpointInterfaceUrlString342Parse(BaseModel):
    pass


class EndpointInterfaceUrlString343(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString343DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString343Defaults"]
    merge: Optional["EndpointInterfaceUrlString343Merge"]
    parse: Optional["EndpointInterfaceUrlString343Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString343DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString343Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString343Merge(BaseModel):
    pass


class EndpointInterfaceUrlString343Parse(BaseModel):
    pass


class EndpointInterfaceUrlString344(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString344DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString344Defaults"]
    merge: Optional["EndpointInterfaceUrlString344Merge"]
    parse: Optional["EndpointInterfaceUrlString344Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString344DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString344Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString344Merge(BaseModel):
    pass


class EndpointInterfaceUrlString344Parse(BaseModel):
    pass


class EndpointInterfaceUrlString345(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString345DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString345Defaults"]
    merge: Optional["EndpointInterfaceUrlString345Merge"]
    parse: Optional["EndpointInterfaceUrlString345Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString345DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString345Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString345Merge(BaseModel):
    pass


class EndpointInterfaceUrlString345Parse(BaseModel):
    pass


class EndpointInterfaceUrlString346(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString346DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString346Defaults"]
    merge: Optional["EndpointInterfaceUrlString346Merge"]
    parse: Optional["EndpointInterfaceUrlString346Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString346DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString346Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString346Merge(BaseModel):
    pass


class EndpointInterfaceUrlString346Parse(BaseModel):
    pass


class EndpointInterfaceUrlString347(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString347DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString347Defaults"]
    merge: Optional["EndpointInterfaceUrlString347Merge"]
    parse: Optional["EndpointInterfaceUrlString347Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString347DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString347Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString347Merge(BaseModel):
    pass


class EndpointInterfaceUrlString347Parse(BaseModel):
    pass


class EndpointInterfaceUrlString348(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString348DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString348Defaults"]
    merge: Optional["EndpointInterfaceUrlString348Merge"]
    parse: Optional["EndpointInterfaceUrlString348Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString348DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString348Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString348Merge(BaseModel):
    pass


class EndpointInterfaceUrlString348Parse(BaseModel):
    pass


class EndpointInterfaceUrlString349(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString349DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString349Defaults"]
    merge: Optional["EndpointInterfaceUrlString349Merge"]
    parse: Optional["EndpointInterfaceUrlString349Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString349DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString349Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString349Merge(BaseModel):
    pass


class EndpointInterfaceUrlString349Parse(BaseModel):
    pass


class EndpointInterfaceUrlString34DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString34Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString34Merge(BaseModel):
    pass


class EndpointInterfaceUrlString34Parse(BaseModel):
    pass


class EndpointInterfaceUrlString35(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString35DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString35Defaults"]
    merge: Optional["EndpointInterfaceUrlString35Merge"]
    parse: Optional["EndpointInterfaceUrlString35Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString350(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString350DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString350Defaults"]
    merge: Optional["EndpointInterfaceUrlString350Merge"]
    parse: Optional["EndpointInterfaceUrlString350Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString350DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString350Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString350Merge(BaseModel):
    pass


class EndpointInterfaceUrlString350Parse(BaseModel):
    pass


class EndpointInterfaceUrlString351(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString351DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString351Defaults"]
    merge: Optional["EndpointInterfaceUrlString351Merge"]
    parse: Optional["EndpointInterfaceUrlString351Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString351DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString351Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString351Merge(BaseModel):
    pass


class EndpointInterfaceUrlString351Parse(BaseModel):
    pass


class EndpointInterfaceUrlString352(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString352DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString352Defaults"]
    merge: Optional["EndpointInterfaceUrlString352Merge"]
    parse: Optional["EndpointInterfaceUrlString352Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString352DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString352Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString352Merge(BaseModel):
    pass


class EndpointInterfaceUrlString352Parse(BaseModel):
    pass


class EndpointInterfaceUrlString353(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString353DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString353Defaults"]
    merge: Optional["EndpointInterfaceUrlString353Merge"]
    parse: Optional["EndpointInterfaceUrlString353Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString353DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString353Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString353Merge(BaseModel):
    pass


class EndpointInterfaceUrlString353Parse(BaseModel):
    pass


class EndpointInterfaceUrlString354(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString354DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString354Defaults"]
    merge: Optional["EndpointInterfaceUrlString354Merge"]
    parse: Optional["EndpointInterfaceUrlString354Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString354DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString354Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString354Merge(BaseModel):
    pass


class EndpointInterfaceUrlString354Parse(BaseModel):
    pass


class EndpointInterfaceUrlString355(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString355DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString355Defaults"]
    merge: Optional["EndpointInterfaceUrlString355Merge"]
    parse: Optional["EndpointInterfaceUrlString355Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString355DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString355Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString355Merge(BaseModel):
    pass


class EndpointInterfaceUrlString355Parse(BaseModel):
    pass


class EndpointInterfaceUrlString356(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString356DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString356Defaults"]
    merge: Optional["EndpointInterfaceUrlString356Merge"]
    parse: Optional["EndpointInterfaceUrlString356Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString356DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString356Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString356Merge(BaseModel):
    pass


class EndpointInterfaceUrlString356Parse(BaseModel):
    pass


class EndpointInterfaceUrlString357(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString357DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString357Defaults"]
    merge: Optional["EndpointInterfaceUrlString357Merge"]
    parse: Optional["EndpointInterfaceUrlString357Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString357DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString357Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString357Merge(BaseModel):
    pass


class EndpointInterfaceUrlString357Parse(BaseModel):
    pass


class EndpointInterfaceUrlString358(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString358DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString358Defaults"]
    merge: Optional["EndpointInterfaceUrlString358Merge"]
    parse: Optional["EndpointInterfaceUrlString358Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString358DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString358Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString358Merge(BaseModel):
    pass


class EndpointInterfaceUrlString358Parse(BaseModel):
    pass


class EndpointInterfaceUrlString359(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString359DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString359Defaults"]
    merge: Optional["EndpointInterfaceUrlString359Merge"]
    parse: Optional["EndpointInterfaceUrlString359Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString359DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString359Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString359Merge(BaseModel):
    pass


class EndpointInterfaceUrlString359Parse(BaseModel):
    pass


class EndpointInterfaceUrlString35DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString35Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString35Merge(BaseModel):
    pass


class EndpointInterfaceUrlString35Parse(BaseModel):
    pass


class EndpointInterfaceUrlString36(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString36DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString36Defaults"]
    merge: Optional["EndpointInterfaceUrlString36Merge"]
    parse: Optional["EndpointInterfaceUrlString36Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString360(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString360DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString360Defaults"]
    merge: Optional["EndpointInterfaceUrlString360Merge"]
    parse: Optional["EndpointInterfaceUrlString360Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString360DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString360Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString360Merge(BaseModel):
    pass


class EndpointInterfaceUrlString360Parse(BaseModel):
    pass


class EndpointInterfaceUrlString361(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString361DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString361Defaults"]
    merge: Optional["EndpointInterfaceUrlString361Merge"]
    parse: Optional["EndpointInterfaceUrlString361Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString361DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString361Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString361Merge(BaseModel):
    pass


class EndpointInterfaceUrlString361Parse(BaseModel):
    pass


class EndpointInterfaceUrlString362(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString362DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString362Defaults"]
    merge: Optional["EndpointInterfaceUrlString362Merge"]
    parse: Optional["EndpointInterfaceUrlString362Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString362DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString362Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString362Merge(BaseModel):
    pass


class EndpointInterfaceUrlString362Parse(BaseModel):
    pass


class EndpointInterfaceUrlString363(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString363DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString363Defaults"]
    merge: Optional["EndpointInterfaceUrlString363Merge"]
    parse: Optional["EndpointInterfaceUrlString363Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString363DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString363Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString363Merge(BaseModel):
    pass


class EndpointInterfaceUrlString363Parse(BaseModel):
    pass


class EndpointInterfaceUrlString364(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString364DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString364Defaults"]
    merge: Optional["EndpointInterfaceUrlString364Merge"]
    parse: Optional["EndpointInterfaceUrlString364Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString364DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString364Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString364Merge(BaseModel):
    pass


class EndpointInterfaceUrlString364Parse(BaseModel):
    pass


class EndpointInterfaceUrlString365(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString365DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString365Defaults"]
    merge: Optional["EndpointInterfaceUrlString365Merge"]
    parse: Optional["EndpointInterfaceUrlString365Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString365DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString365Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString365Merge(BaseModel):
    pass


class EndpointInterfaceUrlString365Parse(BaseModel):
    pass


class EndpointInterfaceUrlString366(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString366DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString366Defaults"]
    merge: Optional["EndpointInterfaceUrlString366Merge"]
    parse: Optional["EndpointInterfaceUrlString366Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString366DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString366Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString366Merge(BaseModel):
    pass


class EndpointInterfaceUrlString366Parse(BaseModel):
    pass


class EndpointInterfaceUrlString367(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString367DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString367Defaults"]
    merge: Optional["EndpointInterfaceUrlString367Merge"]
    parse: Optional["EndpointInterfaceUrlString367Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString367DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString367Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString367Merge(BaseModel):
    pass


class EndpointInterfaceUrlString367Parse(BaseModel):
    pass


class EndpointInterfaceUrlString368(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString368DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString368Defaults"]
    merge: Optional["EndpointInterfaceUrlString368Merge"]
    parse: Optional["EndpointInterfaceUrlString368Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString368DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString368Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString368Merge(BaseModel):
    pass


class EndpointInterfaceUrlString368Parse(BaseModel):
    pass


class EndpointInterfaceUrlString369(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString369DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString369Defaults"]
    merge: Optional["EndpointInterfaceUrlString369Merge"]
    parse: Optional["EndpointInterfaceUrlString369Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString369DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString369Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString369Merge(BaseModel):
    pass


class EndpointInterfaceUrlString369Parse(BaseModel):
    pass


class EndpointInterfaceUrlString36DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString36Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString36Merge(BaseModel):
    pass


class EndpointInterfaceUrlString36Parse(BaseModel):
    pass


class EndpointInterfaceUrlString37(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString37DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString37Defaults"]
    merge: Optional["EndpointInterfaceUrlString37Merge"]
    parse: Optional["EndpointInterfaceUrlString37Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString370(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString370DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString370Defaults"]
    merge: Optional["EndpointInterfaceUrlString370Merge"]
    parse: Optional["EndpointInterfaceUrlString370Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString370DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString370Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString370Merge(BaseModel):
    pass


class EndpointInterfaceUrlString370Parse(BaseModel):
    pass


class EndpointInterfaceUrlString371(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString371DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString371Defaults"]
    merge: Optional["EndpointInterfaceUrlString371Merge"]
    parse: Optional["EndpointInterfaceUrlString371Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString371DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString371Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString371Merge(BaseModel):
    pass


class EndpointInterfaceUrlString371Parse(BaseModel):
    pass


class EndpointInterfaceUrlString372(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString372DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString372Defaults"]
    merge: Optional["EndpointInterfaceUrlString372Merge"]
    parse: Optional["EndpointInterfaceUrlString372Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString372DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString372Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString372Merge(BaseModel):
    pass


class EndpointInterfaceUrlString372Parse(BaseModel):
    pass


class EndpointInterfaceUrlString373(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString373DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString373Defaults"]
    merge: Optional["EndpointInterfaceUrlString373Merge"]
    parse: Optional["EndpointInterfaceUrlString373Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString373DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString373Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString373Merge(BaseModel):
    pass


class EndpointInterfaceUrlString373Parse(BaseModel):
    pass


class EndpointInterfaceUrlString374(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString374DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString374Defaults"]
    merge: Optional["EndpointInterfaceUrlString374Merge"]
    parse: Optional["EndpointInterfaceUrlString374Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString374DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString374Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString374Merge(BaseModel):
    pass


class EndpointInterfaceUrlString374Parse(BaseModel):
    pass


class EndpointInterfaceUrlString375(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString375DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString375Defaults"]
    merge: Optional["EndpointInterfaceUrlString375Merge"]
    parse: Optional["EndpointInterfaceUrlString375Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString375DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString375Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString375Merge(BaseModel):
    pass


class EndpointInterfaceUrlString375Parse(BaseModel):
    pass


class EndpointInterfaceUrlString376(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString376DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString376Defaults"]
    merge: Optional["EndpointInterfaceUrlString376Merge"]
    parse: Optional["EndpointInterfaceUrlString376Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString376DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString376Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString376Merge(BaseModel):
    pass


class EndpointInterfaceUrlString376Parse(BaseModel):
    pass


class EndpointInterfaceUrlString377(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString377DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString377Defaults"]
    merge: Optional["EndpointInterfaceUrlString377Merge"]
    parse: Optional["EndpointInterfaceUrlString377Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString377DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString377Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString377Merge(BaseModel):
    pass


class EndpointInterfaceUrlString377Parse(BaseModel):
    pass


class EndpointInterfaceUrlString378(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString378DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString378Defaults"]
    merge: Optional["EndpointInterfaceUrlString378Merge"]
    parse: Optional["EndpointInterfaceUrlString378Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString378DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString378Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString378Merge(BaseModel):
    pass


class EndpointInterfaceUrlString378Parse(BaseModel):
    pass


class EndpointInterfaceUrlString379(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString379DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString379Defaults"]
    merge: Optional["EndpointInterfaceUrlString379Merge"]
    parse: Optional["EndpointInterfaceUrlString379Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString379DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString379Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString379Merge(BaseModel):
    pass


class EndpointInterfaceUrlString379Parse(BaseModel):
    pass


class EndpointInterfaceUrlString37DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString37Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString37Merge(BaseModel):
    pass


class EndpointInterfaceUrlString37Parse(BaseModel):
    pass


class EndpointInterfaceUrlString38(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString38DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString38Defaults"]
    merge: Optional["EndpointInterfaceUrlString38Merge"]
    parse: Optional["EndpointInterfaceUrlString38Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString380(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString380DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString380Defaults"]
    merge: Optional["EndpointInterfaceUrlString380Merge"]
    parse: Optional["EndpointInterfaceUrlString380Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString380DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString380Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString380Merge(BaseModel):
    pass


class EndpointInterfaceUrlString380Parse(BaseModel):
    pass


class EndpointInterfaceUrlString381(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString381DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString381Defaults"]
    merge: Optional["EndpointInterfaceUrlString381Merge"]
    parse: Optional["EndpointInterfaceUrlString381Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString381DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString381Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString381Merge(BaseModel):
    pass


class EndpointInterfaceUrlString381Parse(BaseModel):
    pass


class EndpointInterfaceUrlString382(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString382DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString382Defaults"]
    merge: Optional["EndpointInterfaceUrlString382Merge"]
    parse: Optional["EndpointInterfaceUrlString382Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString382DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString382Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString382Merge(BaseModel):
    pass


class EndpointInterfaceUrlString382Parse(BaseModel):
    pass


class EndpointInterfaceUrlString383(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString383DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString383Defaults"]
    merge: Optional["EndpointInterfaceUrlString383Merge"]
    parse: Optional["EndpointInterfaceUrlString383Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString383DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString383Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString383Merge(BaseModel):
    pass


class EndpointInterfaceUrlString383Parse(BaseModel):
    pass


class EndpointInterfaceUrlString384(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString384DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString384Defaults"]
    merge: Optional["EndpointInterfaceUrlString384Merge"]
    parse: Optional["EndpointInterfaceUrlString384Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString384DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString384Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString384Merge(BaseModel):
    pass


class EndpointInterfaceUrlString384Parse(BaseModel):
    pass


class EndpointInterfaceUrlString385(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString385DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString385Defaults"]
    merge: Optional["EndpointInterfaceUrlString385Merge"]
    parse: Optional["EndpointInterfaceUrlString385Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString385DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString385Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString385Merge(BaseModel):
    pass


class EndpointInterfaceUrlString385Parse(BaseModel):
    pass


class EndpointInterfaceUrlString386(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString386DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString386Defaults"]
    merge: Optional["EndpointInterfaceUrlString386Merge"]
    parse: Optional["EndpointInterfaceUrlString386Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString386DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString386Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString386Merge(BaseModel):
    pass


class EndpointInterfaceUrlString386Parse(BaseModel):
    pass


class EndpointInterfaceUrlString387(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString387DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString387Defaults"]
    merge: Optional["EndpointInterfaceUrlString387Merge"]
    parse: Optional["EndpointInterfaceUrlString387Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString387DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString387Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString387Merge(BaseModel):
    pass


class EndpointInterfaceUrlString387Parse(BaseModel):
    pass


class EndpointInterfaceUrlString388(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString388DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString388Defaults"]
    merge: Optional["EndpointInterfaceUrlString388Merge"]
    parse: Optional["EndpointInterfaceUrlString388Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString388DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString388Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString388Merge(BaseModel):
    pass


class EndpointInterfaceUrlString388Parse(BaseModel):
    pass


class EndpointInterfaceUrlString389(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString389DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString389Defaults"]
    merge: Optional["EndpointInterfaceUrlString389Merge"]
    parse: Optional["EndpointInterfaceUrlString389Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString389DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString389Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString389Merge(BaseModel):
    pass


class EndpointInterfaceUrlString389Parse(BaseModel):
    pass


class EndpointInterfaceUrlString38DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString38Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString38Merge(BaseModel):
    pass


class EndpointInterfaceUrlString38Parse(BaseModel):
    pass


class EndpointInterfaceUrlString39(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString39DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString39Defaults"]
    merge: Optional["EndpointInterfaceUrlString39Merge"]
    parse: Optional["EndpointInterfaceUrlString39Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString390(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString390DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString390Defaults"]
    merge: Optional["EndpointInterfaceUrlString390Merge"]
    parse: Optional["EndpointInterfaceUrlString390Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString390DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString390Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString390Merge(BaseModel):
    pass


class EndpointInterfaceUrlString390Parse(BaseModel):
    pass


class EndpointInterfaceUrlString391(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString391DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString391Defaults"]
    merge: Optional["EndpointInterfaceUrlString391Merge"]
    parse: Optional["EndpointInterfaceUrlString391Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString391DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString391Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString391Merge(BaseModel):
    pass


class EndpointInterfaceUrlString391Parse(BaseModel):
    pass


class EndpointInterfaceUrlString392(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString392DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString392Defaults"]
    merge: Optional["EndpointInterfaceUrlString392Merge"]
    parse: Optional["EndpointInterfaceUrlString392Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString392DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString392Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString392Merge(BaseModel):
    pass


class EndpointInterfaceUrlString392Parse(BaseModel):
    pass


class EndpointInterfaceUrlString393(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString393DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString393Defaults"]
    merge: Optional["EndpointInterfaceUrlString393Merge"]
    parse: Optional["EndpointInterfaceUrlString393Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString393DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString393Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString393Merge(BaseModel):
    pass


class EndpointInterfaceUrlString393Parse(BaseModel):
    pass


class EndpointInterfaceUrlString394(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString394DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString394Defaults"]
    merge: Optional["EndpointInterfaceUrlString394Merge"]
    parse: Optional["EndpointInterfaceUrlString394Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString394DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString394Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString394Merge(BaseModel):
    pass


class EndpointInterfaceUrlString394Parse(BaseModel):
    pass


class EndpointInterfaceUrlString395(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString395DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString395Defaults"]
    merge: Optional["EndpointInterfaceUrlString395Merge"]
    parse: Optional["EndpointInterfaceUrlString395Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString395DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString395Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString395Merge(BaseModel):
    pass


class EndpointInterfaceUrlString395Parse(BaseModel):
    pass


class EndpointInterfaceUrlString396(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString396DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString396Defaults"]
    merge: Optional["EndpointInterfaceUrlString396Merge"]
    parse: Optional["EndpointInterfaceUrlString396Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString396DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString396Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString396Merge(BaseModel):
    pass


class EndpointInterfaceUrlString396Parse(BaseModel):
    pass


class EndpointInterfaceUrlString397(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString397DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString397Defaults"]
    merge: Optional["EndpointInterfaceUrlString397Merge"]
    parse: Optional["EndpointInterfaceUrlString397Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString397DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString397Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString397Merge(BaseModel):
    pass


class EndpointInterfaceUrlString397Parse(BaseModel):
    pass


class EndpointInterfaceUrlString398(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString398DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString398Defaults"]
    merge: Optional["EndpointInterfaceUrlString398Merge"]
    parse: Optional["EndpointInterfaceUrlString398Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString398DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString398Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString398Merge(BaseModel):
    pass


class EndpointInterfaceUrlString398Parse(BaseModel):
    pass


class EndpointInterfaceUrlString399(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString399DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString399Defaults"]
    merge: Optional["EndpointInterfaceUrlString399Merge"]
    parse: Optional["EndpointInterfaceUrlString399Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString399DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString399Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString399Merge(BaseModel):
    pass


class EndpointInterfaceUrlString399Parse(BaseModel):
    pass


class EndpointInterfaceUrlString39DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString39Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString39Merge(BaseModel):
    pass


class EndpointInterfaceUrlString39Parse(BaseModel):
    pass


class EndpointInterfaceUrlString3DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString3Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString3Merge(BaseModel):
    pass


class EndpointInterfaceUrlString3Parse(BaseModel):
    pass


class EndpointInterfaceUrlString4(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString4DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString4Defaults"]
    merge: Optional["EndpointInterfaceUrlString4Merge"]
    parse: Optional["EndpointInterfaceUrlString4Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString40(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString40DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString40Defaults"]
    merge: Optional["EndpointInterfaceUrlString40Merge"]
    parse: Optional["EndpointInterfaceUrlString40Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString400(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString400DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString400Defaults"]
    merge: Optional["EndpointInterfaceUrlString400Merge"]
    parse: Optional["EndpointInterfaceUrlString400Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString400DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString400Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString400Merge(BaseModel):
    pass


class EndpointInterfaceUrlString400Parse(BaseModel):
    pass


class EndpointInterfaceUrlString401(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString401DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString401Defaults"]
    merge: Optional["EndpointInterfaceUrlString401Merge"]
    parse: Optional["EndpointInterfaceUrlString401Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString401DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString401Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString401Merge(BaseModel):
    pass


class EndpointInterfaceUrlString401Parse(BaseModel):
    pass


class EndpointInterfaceUrlString402(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString402DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString402Defaults"]
    merge: Optional["EndpointInterfaceUrlString402Merge"]
    parse: Optional["EndpointInterfaceUrlString402Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString402DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString402Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString402Merge(BaseModel):
    pass


class EndpointInterfaceUrlString402Parse(BaseModel):
    pass


class EndpointInterfaceUrlString403(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString403DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString403Defaults"]
    merge: Optional["EndpointInterfaceUrlString403Merge"]
    parse: Optional["EndpointInterfaceUrlString403Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString403DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString403Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString403Merge(BaseModel):
    pass


class EndpointInterfaceUrlString403Parse(BaseModel):
    pass


class EndpointInterfaceUrlString404(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString404DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString404Defaults"]
    merge: Optional["EndpointInterfaceUrlString404Merge"]
    parse: Optional["EndpointInterfaceUrlString404Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString404DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString404Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString404Merge(BaseModel):
    pass


class EndpointInterfaceUrlString404Parse(BaseModel):
    pass


class EndpointInterfaceUrlString405(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString405DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString405Defaults"]
    merge: Optional["EndpointInterfaceUrlString405Merge"]
    parse: Optional["EndpointInterfaceUrlString405Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString405DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString405Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString405Merge(BaseModel):
    pass


class EndpointInterfaceUrlString405Parse(BaseModel):
    pass


class EndpointInterfaceUrlString406(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString406DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString406Defaults"]
    merge: Optional["EndpointInterfaceUrlString406Merge"]
    parse: Optional["EndpointInterfaceUrlString406Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString406DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString406Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString406Merge(BaseModel):
    pass


class EndpointInterfaceUrlString406Parse(BaseModel):
    pass


class EndpointInterfaceUrlString407(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString407DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString407Defaults"]
    merge: Optional["EndpointInterfaceUrlString407Merge"]
    parse: Optional["EndpointInterfaceUrlString407Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString407DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString407Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString407Merge(BaseModel):
    pass


class EndpointInterfaceUrlString407Parse(BaseModel):
    pass


class EndpointInterfaceUrlString408(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString408DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString408Defaults"]
    merge: Optional["EndpointInterfaceUrlString408Merge"]
    parse: Optional["EndpointInterfaceUrlString408Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString408DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString408Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString408Merge(BaseModel):
    pass


class EndpointInterfaceUrlString408Parse(BaseModel):
    pass


class EndpointInterfaceUrlString409(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString409DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString409Defaults"]
    merge: Optional["EndpointInterfaceUrlString409Merge"]
    parse: Optional["EndpointInterfaceUrlString409Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString409DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString409Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString409Merge(BaseModel):
    pass


class EndpointInterfaceUrlString409Parse(BaseModel):
    pass


class EndpointInterfaceUrlString40DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString40Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString40Merge(BaseModel):
    pass


class EndpointInterfaceUrlString40Parse(BaseModel):
    pass


class EndpointInterfaceUrlString41(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString41DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString41Defaults"]
    merge: Optional["EndpointInterfaceUrlString41Merge"]
    parse: Optional["EndpointInterfaceUrlString41Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString410(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString410DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString410Defaults"]
    merge: Optional["EndpointInterfaceUrlString410Merge"]
    parse: Optional["EndpointInterfaceUrlString410Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString410DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString410Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString410Merge(BaseModel):
    pass


class EndpointInterfaceUrlString410Parse(BaseModel):
    pass


class EndpointInterfaceUrlString411(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString411DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString411Defaults"]
    merge: Optional["EndpointInterfaceUrlString411Merge"]
    parse: Optional["EndpointInterfaceUrlString411Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString411DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString411Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString411Merge(BaseModel):
    pass


class EndpointInterfaceUrlString411Parse(BaseModel):
    pass


class EndpointInterfaceUrlString412(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString412DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString412Defaults"]
    merge: Optional["EndpointInterfaceUrlString412Merge"]
    parse: Optional["EndpointInterfaceUrlString412Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString412DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString412Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString412Merge(BaseModel):
    pass


class EndpointInterfaceUrlString412Parse(BaseModel):
    pass


class EndpointInterfaceUrlString413(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString413DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString413Defaults"]
    merge: Optional["EndpointInterfaceUrlString413Merge"]
    parse: Optional["EndpointInterfaceUrlString413Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString413DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString413Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString413Merge(BaseModel):
    pass


class EndpointInterfaceUrlString413Parse(BaseModel):
    pass


class EndpointInterfaceUrlString414(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString414DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString414Defaults"]
    merge: Optional["EndpointInterfaceUrlString414Merge"]
    parse: Optional["EndpointInterfaceUrlString414Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString414DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString414Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString414Merge(BaseModel):
    pass


class EndpointInterfaceUrlString414Parse(BaseModel):
    pass


class EndpointInterfaceUrlString415(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString415DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString415Defaults"]
    merge: Optional["EndpointInterfaceUrlString415Merge"]
    parse: Optional["EndpointInterfaceUrlString415Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString415DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString415Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString415Merge(BaseModel):
    pass


class EndpointInterfaceUrlString415Parse(BaseModel):
    pass


class EndpointInterfaceUrlString416(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString416DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString416Defaults"]
    merge: Optional["EndpointInterfaceUrlString416Merge"]
    parse: Optional["EndpointInterfaceUrlString416Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString416DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString416Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString416Merge(BaseModel):
    pass


class EndpointInterfaceUrlString416Parse(BaseModel):
    pass


class EndpointInterfaceUrlString417(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString417DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString417Defaults"]
    merge: Optional["EndpointInterfaceUrlString417Merge"]
    parse: Optional["EndpointInterfaceUrlString417Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString417DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString417Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString417Merge(BaseModel):
    pass


class EndpointInterfaceUrlString417Parse(BaseModel):
    pass


class EndpointInterfaceUrlString418(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString418DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString418Defaults"]
    merge: Optional["EndpointInterfaceUrlString418Merge"]
    parse: Optional["EndpointInterfaceUrlString418Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString418DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString418Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString418Merge(BaseModel):
    pass


class EndpointInterfaceUrlString418Parse(BaseModel):
    pass


class EndpointInterfaceUrlString419(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString419DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString419Defaults"]
    merge: Optional["EndpointInterfaceUrlString419Merge"]
    parse: Optional["EndpointInterfaceUrlString419Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString419DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString419Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString419Merge(BaseModel):
    pass


class EndpointInterfaceUrlString419Parse(BaseModel):
    pass


class EndpointInterfaceUrlString41DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString41Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString41Merge(BaseModel):
    pass


class EndpointInterfaceUrlString41Parse(BaseModel):
    pass


class EndpointInterfaceUrlString42(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString42DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString42Defaults"]
    merge: Optional["EndpointInterfaceUrlString42Merge"]
    parse: Optional["EndpointInterfaceUrlString42Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString420(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString420DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString420Defaults"]
    merge: Optional["EndpointInterfaceUrlString420Merge"]
    parse: Optional["EndpointInterfaceUrlString420Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString420DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString420Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString420Merge(BaseModel):
    pass


class EndpointInterfaceUrlString420Parse(BaseModel):
    pass


class EndpointInterfaceUrlString421(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString421DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString421Defaults"]
    merge: Optional["EndpointInterfaceUrlString421Merge"]
    parse: Optional["EndpointInterfaceUrlString421Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString421DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString421Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString421Merge(BaseModel):
    pass


class EndpointInterfaceUrlString421Parse(BaseModel):
    pass


class EndpointInterfaceUrlString422(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString422DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString422Defaults"]
    merge: Optional["EndpointInterfaceUrlString422Merge"]
    parse: Optional["EndpointInterfaceUrlString422Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString422DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString422Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString422Merge(BaseModel):
    pass


class EndpointInterfaceUrlString422Parse(BaseModel):
    pass


class EndpointInterfaceUrlString423(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString423DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString423Defaults"]
    merge: Optional["EndpointInterfaceUrlString423Merge"]
    parse: Optional["EndpointInterfaceUrlString423Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString423DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString423Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString423Merge(BaseModel):
    pass


class EndpointInterfaceUrlString423Parse(BaseModel):
    pass


class EndpointInterfaceUrlString424(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString424DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString424Defaults"]
    merge: Optional["EndpointInterfaceUrlString424Merge"]
    parse: Optional["EndpointInterfaceUrlString424Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString424DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString424Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString424Merge(BaseModel):
    pass


class EndpointInterfaceUrlString424Parse(BaseModel):
    pass


class EndpointInterfaceUrlString425(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString425DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString425Defaults"]
    merge: Optional["EndpointInterfaceUrlString425Merge"]
    parse: Optional["EndpointInterfaceUrlString425Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString425DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString425Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString425Merge(BaseModel):
    pass


class EndpointInterfaceUrlString425Parse(BaseModel):
    pass


class EndpointInterfaceUrlString426(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString426DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString426Defaults"]
    merge: Optional["EndpointInterfaceUrlString426Merge"]
    parse: Optional["EndpointInterfaceUrlString426Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString426DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString426Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString426Merge(BaseModel):
    pass


class EndpointInterfaceUrlString426Parse(BaseModel):
    pass


class EndpointInterfaceUrlString427(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString427DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString427Defaults"]
    merge: Optional["EndpointInterfaceUrlString427Merge"]
    parse: Optional["EndpointInterfaceUrlString427Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString427DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString427Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString427Merge(BaseModel):
    pass


class EndpointInterfaceUrlString427Parse(BaseModel):
    pass


class EndpointInterfaceUrlString428(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString428DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString428Defaults"]
    merge: Optional["EndpointInterfaceUrlString428Merge"]
    parse: Optional["EndpointInterfaceUrlString428Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString428DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString428Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString428Merge(BaseModel):
    pass


class EndpointInterfaceUrlString428Parse(BaseModel):
    pass


class EndpointInterfaceUrlString429(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString429DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString429Defaults"]
    merge: Optional["EndpointInterfaceUrlString429Merge"]
    parse: Optional["EndpointInterfaceUrlString429Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString429DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString429Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString429Merge(BaseModel):
    pass


class EndpointInterfaceUrlString429Parse(BaseModel):
    pass


class EndpointInterfaceUrlString42DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString42Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString42Merge(BaseModel):
    pass


class EndpointInterfaceUrlString42Parse(BaseModel):
    pass


class EndpointInterfaceUrlString43(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString43DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString43Defaults"]
    merge: Optional["EndpointInterfaceUrlString43Merge"]
    parse: Optional["EndpointInterfaceUrlString43Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString430(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString430DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString430Defaults"]
    merge: Optional["EndpointInterfaceUrlString430Merge"]
    parse: Optional["EndpointInterfaceUrlString430Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString430DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString430Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString430Merge(BaseModel):
    pass


class EndpointInterfaceUrlString430Parse(BaseModel):
    pass


class EndpointInterfaceUrlString431(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString431DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString431Defaults"]
    merge: Optional["EndpointInterfaceUrlString431Merge"]
    parse: Optional["EndpointInterfaceUrlString431Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString431DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString431Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString431Merge(BaseModel):
    pass


class EndpointInterfaceUrlString431Parse(BaseModel):
    pass


class EndpointInterfaceUrlString432(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString432DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString432Defaults"]
    merge: Optional["EndpointInterfaceUrlString432Merge"]
    parse: Optional["EndpointInterfaceUrlString432Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString432DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString432Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString432Merge(BaseModel):
    pass


class EndpointInterfaceUrlString432Parse(BaseModel):
    pass


class EndpointInterfaceUrlString433(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString433DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString433Defaults"]
    merge: Optional["EndpointInterfaceUrlString433Merge"]
    parse: Optional["EndpointInterfaceUrlString433Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString433DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString433Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString433Merge(BaseModel):
    pass


class EndpointInterfaceUrlString433Parse(BaseModel):
    pass


class EndpointInterfaceUrlString434(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString434DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString434Defaults"]
    merge: Optional["EndpointInterfaceUrlString434Merge"]
    parse: Optional["EndpointInterfaceUrlString434Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString434DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString434Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString434Merge(BaseModel):
    pass


class EndpointInterfaceUrlString434Parse(BaseModel):
    pass


class EndpointInterfaceUrlString435(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString435DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString435Defaults"]
    merge: Optional["EndpointInterfaceUrlString435Merge"]
    parse: Optional["EndpointInterfaceUrlString435Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString435DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString435Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString435Merge(BaseModel):
    pass


class EndpointInterfaceUrlString435Parse(BaseModel):
    pass


class EndpointInterfaceUrlString436(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString436DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString436Defaults"]
    merge: Optional["EndpointInterfaceUrlString436Merge"]
    parse: Optional["EndpointInterfaceUrlString436Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString436DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString436Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString436Merge(BaseModel):
    pass


class EndpointInterfaceUrlString436Parse(BaseModel):
    pass


class EndpointInterfaceUrlString437(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString437DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString437Defaults"]
    merge: Optional["EndpointInterfaceUrlString437Merge"]
    parse: Optional["EndpointInterfaceUrlString437Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString437DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString437Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString437Merge(BaseModel):
    pass


class EndpointInterfaceUrlString437Parse(BaseModel):
    pass


class EndpointInterfaceUrlString438(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString438DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString438Defaults"]
    merge: Optional["EndpointInterfaceUrlString438Merge"]
    parse: Optional["EndpointInterfaceUrlString438Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString438DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString438Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString438Merge(BaseModel):
    pass


class EndpointInterfaceUrlString438Parse(BaseModel):
    pass


class EndpointInterfaceUrlString439(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString439DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString439Defaults"]
    merge: Optional["EndpointInterfaceUrlString439Merge"]
    parse: Optional["EndpointInterfaceUrlString439Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString439DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString439Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString439Merge(BaseModel):
    pass


class EndpointInterfaceUrlString439Parse(BaseModel):
    pass


class EndpointInterfaceUrlString43DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString43Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString43Merge(BaseModel):
    pass


class EndpointInterfaceUrlString43Parse(BaseModel):
    pass


class EndpointInterfaceUrlString44(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString44DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString44Defaults"]
    merge: Optional["EndpointInterfaceUrlString44Merge"]
    parse: Optional["EndpointInterfaceUrlString44Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString440(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString440DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString440Defaults"]
    merge: Optional["EndpointInterfaceUrlString440Merge"]
    parse: Optional["EndpointInterfaceUrlString440Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString440DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString440Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString440Merge(BaseModel):
    pass


class EndpointInterfaceUrlString440Parse(BaseModel):
    pass


class EndpointInterfaceUrlString441(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString441DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString441Defaults"]
    merge: Optional["EndpointInterfaceUrlString441Merge"]
    parse: Optional["EndpointInterfaceUrlString441Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString441DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString441Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString441Merge(BaseModel):
    pass


class EndpointInterfaceUrlString441Parse(BaseModel):
    pass


class EndpointInterfaceUrlString442(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString442DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString442Defaults"]
    merge: Optional["EndpointInterfaceUrlString442Merge"]
    parse: Optional["EndpointInterfaceUrlString442Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString442DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString442Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString442Merge(BaseModel):
    pass


class EndpointInterfaceUrlString442Parse(BaseModel):
    pass


class EndpointInterfaceUrlString443(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString443DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString443Defaults"]
    merge: Optional["EndpointInterfaceUrlString443Merge"]
    parse: Optional["EndpointInterfaceUrlString443Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString443DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString443Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString443Merge(BaseModel):
    pass


class EndpointInterfaceUrlString443Parse(BaseModel):
    pass


class EndpointInterfaceUrlString444(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString444DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString444Defaults"]
    merge: Optional["EndpointInterfaceUrlString444Merge"]
    parse: Optional["EndpointInterfaceUrlString444Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString444DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString444Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString444Merge(BaseModel):
    pass


class EndpointInterfaceUrlString444Parse(BaseModel):
    pass


class EndpointInterfaceUrlString445(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString445DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString445Defaults"]
    merge: Optional["EndpointInterfaceUrlString445Merge"]
    parse: Optional["EndpointInterfaceUrlString445Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString445DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString445Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString445Merge(BaseModel):
    pass


class EndpointInterfaceUrlString445Parse(BaseModel):
    pass


class EndpointInterfaceUrlString446(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString446DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString446Defaults"]
    merge: Optional["EndpointInterfaceUrlString446Merge"]
    parse: Optional["EndpointInterfaceUrlString446Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString446DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString446Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString446Merge(BaseModel):
    pass


class EndpointInterfaceUrlString446Parse(BaseModel):
    pass


class EndpointInterfaceUrlString447(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString447DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString447Defaults"]
    merge: Optional["EndpointInterfaceUrlString447Merge"]
    parse: Optional["EndpointInterfaceUrlString447Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString447DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString447Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString447Merge(BaseModel):
    pass


class EndpointInterfaceUrlString447Parse(BaseModel):
    pass


class EndpointInterfaceUrlString448(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString448DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString448Defaults"]
    merge: Optional["EndpointInterfaceUrlString448Merge"]
    parse: Optional["EndpointInterfaceUrlString448Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString448DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString448Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString448Merge(BaseModel):
    pass


class EndpointInterfaceUrlString448Parse(BaseModel):
    pass


class EndpointInterfaceUrlString449(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString449DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString449Defaults"]
    merge: Optional["EndpointInterfaceUrlString449Merge"]
    parse: Optional["EndpointInterfaceUrlString449Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString449DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString449Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString449Merge(BaseModel):
    pass


class EndpointInterfaceUrlString449Parse(BaseModel):
    pass


class EndpointInterfaceUrlString44DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString44Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString44Merge(BaseModel):
    pass


class EndpointInterfaceUrlString44Parse(BaseModel):
    pass


class EndpointInterfaceUrlString45(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString45DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString45Defaults"]
    merge: Optional["EndpointInterfaceUrlString45Merge"]
    parse: Optional["EndpointInterfaceUrlString45Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString450(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString450DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString450Defaults"]
    merge: Optional["EndpointInterfaceUrlString450Merge"]
    parse: Optional["EndpointInterfaceUrlString450Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString450DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString450Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString450Merge(BaseModel):
    pass


class EndpointInterfaceUrlString450Parse(BaseModel):
    pass


class EndpointInterfaceUrlString451(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString451DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString451Defaults"]
    merge: Optional["EndpointInterfaceUrlString451Merge"]
    parse: Optional["EndpointInterfaceUrlString451Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString451DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString451Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString451Merge(BaseModel):
    pass


class EndpointInterfaceUrlString451Parse(BaseModel):
    pass


class EndpointInterfaceUrlString452(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString452DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString452Defaults"]
    merge: Optional["EndpointInterfaceUrlString452Merge"]
    parse: Optional["EndpointInterfaceUrlString452Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString452DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString452Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString452Merge(BaseModel):
    pass


class EndpointInterfaceUrlString452Parse(BaseModel):
    pass


class EndpointInterfaceUrlString453(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString453DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString453Defaults"]
    merge: Optional["EndpointInterfaceUrlString453Merge"]
    parse: Optional["EndpointInterfaceUrlString453Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString453DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString453Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString453Merge(BaseModel):
    pass


class EndpointInterfaceUrlString453Parse(BaseModel):
    pass


class EndpointInterfaceUrlString454(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString454DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString454Defaults"]
    merge: Optional["EndpointInterfaceUrlString454Merge"]
    parse: Optional["EndpointInterfaceUrlString454Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString454DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString454Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString454Merge(BaseModel):
    pass


class EndpointInterfaceUrlString454Parse(BaseModel):
    pass


class EndpointInterfaceUrlString455(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString455DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString455Defaults"]
    merge: Optional["EndpointInterfaceUrlString455Merge"]
    parse: Optional["EndpointInterfaceUrlString455Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString455DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString455Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString455Merge(BaseModel):
    pass


class EndpointInterfaceUrlString455Parse(BaseModel):
    pass


class EndpointInterfaceUrlString456(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString456DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString456Defaults"]
    merge: Optional["EndpointInterfaceUrlString456Merge"]
    parse: Optional["EndpointInterfaceUrlString456Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString456DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString456Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString456Merge(BaseModel):
    pass


class EndpointInterfaceUrlString456Parse(BaseModel):
    pass


class EndpointInterfaceUrlString457(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString457DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString457Defaults"]
    merge: Optional["EndpointInterfaceUrlString457Merge"]
    parse: Optional["EndpointInterfaceUrlString457Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString457DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString457Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString457Merge(BaseModel):
    pass


class EndpointInterfaceUrlString457Parse(BaseModel):
    pass


class EndpointInterfaceUrlString458(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString458DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString458Defaults"]
    merge: Optional["EndpointInterfaceUrlString458Merge"]
    parse: Optional["EndpointInterfaceUrlString458Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString458DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString458Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString458Merge(BaseModel):
    pass


class EndpointInterfaceUrlString458Parse(BaseModel):
    pass


class EndpointInterfaceUrlString459(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString459DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString459Defaults"]
    merge: Optional["EndpointInterfaceUrlString459Merge"]
    parse: Optional["EndpointInterfaceUrlString459Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString459DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString459Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString459Merge(BaseModel):
    pass


class EndpointInterfaceUrlString459Parse(BaseModel):
    pass


class EndpointInterfaceUrlString45DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString45Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString45Merge(BaseModel):
    pass


class EndpointInterfaceUrlString45Parse(BaseModel):
    pass


class EndpointInterfaceUrlString46(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString46DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString46Defaults"]
    merge: Optional["EndpointInterfaceUrlString46Merge"]
    parse: Optional["EndpointInterfaceUrlString46Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString460(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString460DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString460Defaults"]
    merge: Optional["EndpointInterfaceUrlString460Merge"]
    parse: Optional["EndpointInterfaceUrlString460Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString460DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString460Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString460Merge(BaseModel):
    pass


class EndpointInterfaceUrlString460Parse(BaseModel):
    pass


class EndpointInterfaceUrlString461(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString461DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString461Defaults"]
    merge: Optional["EndpointInterfaceUrlString461Merge"]
    parse: Optional["EndpointInterfaceUrlString461Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString461DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString461Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString461Merge(BaseModel):
    pass


class EndpointInterfaceUrlString461Parse(BaseModel):
    pass


class EndpointInterfaceUrlString462(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString462DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString462Defaults"]
    merge: Optional["EndpointInterfaceUrlString462Merge"]
    parse: Optional["EndpointInterfaceUrlString462Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString462DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString462Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString462Merge(BaseModel):
    pass


class EndpointInterfaceUrlString462Parse(BaseModel):
    pass


class EndpointInterfaceUrlString463(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString463DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString463Defaults"]
    merge: Optional["EndpointInterfaceUrlString463Merge"]
    parse: Optional["EndpointInterfaceUrlString463Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString463DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString463Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString463Merge(BaseModel):
    pass


class EndpointInterfaceUrlString463Parse(BaseModel):
    pass


class EndpointInterfaceUrlString464(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString464DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString464Defaults"]
    merge: Optional["EndpointInterfaceUrlString464Merge"]
    parse: Optional["EndpointInterfaceUrlString464Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString464DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString464Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString464Merge(BaseModel):
    pass


class EndpointInterfaceUrlString464Parse(BaseModel):
    pass


class EndpointInterfaceUrlString465(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString465DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString465Defaults"]
    merge: Optional["EndpointInterfaceUrlString465Merge"]
    parse: Optional["EndpointInterfaceUrlString465Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString465DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString465Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString465Merge(BaseModel):
    pass


class EndpointInterfaceUrlString465Parse(BaseModel):
    pass


class EndpointInterfaceUrlString466(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString466DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString466Defaults"]
    merge: Optional["EndpointInterfaceUrlString466Merge"]
    parse: Optional["EndpointInterfaceUrlString466Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString466DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString466Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString466Merge(BaseModel):
    pass


class EndpointInterfaceUrlString466Parse(BaseModel):
    pass


class EndpointInterfaceUrlString467(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString467DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString467Defaults"]
    merge: Optional["EndpointInterfaceUrlString467Merge"]
    parse: Optional["EndpointInterfaceUrlString467Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString467DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString467Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString467Merge(BaseModel):
    pass


class EndpointInterfaceUrlString467Parse(BaseModel):
    pass


class EndpointInterfaceUrlString468(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString468DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString468Defaults"]
    merge: Optional["EndpointInterfaceUrlString468Merge"]
    parse: Optional["EndpointInterfaceUrlString468Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString468DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString468Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString468Merge(BaseModel):
    pass


class EndpointInterfaceUrlString468Parse(BaseModel):
    pass


class EndpointInterfaceUrlString469(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString469DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString469Defaults"]
    merge: Optional["EndpointInterfaceUrlString469Merge"]
    parse: Optional["EndpointInterfaceUrlString469Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString469DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString469Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString469Merge(BaseModel):
    pass


class EndpointInterfaceUrlString469Parse(BaseModel):
    pass


class EndpointInterfaceUrlString46DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString46Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString46Merge(BaseModel):
    pass


class EndpointInterfaceUrlString46Parse(BaseModel):
    pass


class EndpointInterfaceUrlString47(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString47DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString47Defaults"]
    merge: Optional["EndpointInterfaceUrlString47Merge"]
    parse: Optional["EndpointInterfaceUrlString47Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString470(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString470DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString470Defaults"]
    merge: Optional["EndpointInterfaceUrlString470Merge"]
    parse: Optional["EndpointInterfaceUrlString470Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString470DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString470Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString470Merge(BaseModel):
    pass


class EndpointInterfaceUrlString470Parse(BaseModel):
    pass


class EndpointInterfaceUrlString471(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString471DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString471Defaults"]
    merge: Optional["EndpointInterfaceUrlString471Merge"]
    parse: Optional["EndpointInterfaceUrlString471Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString471DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString471Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString471Merge(BaseModel):
    pass


class EndpointInterfaceUrlString471Parse(BaseModel):
    pass


class EndpointInterfaceUrlString472(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString472DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString472Defaults"]
    merge: Optional["EndpointInterfaceUrlString472Merge"]
    parse: Optional["EndpointInterfaceUrlString472Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString472DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString472Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString472Merge(BaseModel):
    pass


class EndpointInterfaceUrlString472Parse(BaseModel):
    pass


class EndpointInterfaceUrlString473(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString473DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString473Defaults"]
    merge: Optional["EndpointInterfaceUrlString473Merge"]
    parse: Optional["EndpointInterfaceUrlString473Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString473DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString473Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString473Merge(BaseModel):
    pass


class EndpointInterfaceUrlString473Parse(BaseModel):
    pass


class EndpointInterfaceUrlString474(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString474DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString474Defaults"]
    merge: Optional["EndpointInterfaceUrlString474Merge"]
    parse: Optional["EndpointInterfaceUrlString474Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString474DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString474Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString474Merge(BaseModel):
    pass


class EndpointInterfaceUrlString474Parse(BaseModel):
    pass


class EndpointInterfaceUrlString475(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString475DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString475Defaults"]
    merge: Optional["EndpointInterfaceUrlString475Merge"]
    parse: Optional["EndpointInterfaceUrlString475Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString475DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString475Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString475Merge(BaseModel):
    pass


class EndpointInterfaceUrlString475Parse(BaseModel):
    pass


class EndpointInterfaceUrlString476(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString476DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString476Defaults"]
    merge: Optional["EndpointInterfaceUrlString476Merge"]
    parse: Optional["EndpointInterfaceUrlString476Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString476DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString476Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString476Merge(BaseModel):
    pass


class EndpointInterfaceUrlString476Parse(BaseModel):
    pass


class EndpointInterfaceUrlString477(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString477DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString477Defaults"]
    merge: Optional["EndpointInterfaceUrlString477Merge"]
    parse: Optional["EndpointInterfaceUrlString477Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString477DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString477Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString477Merge(BaseModel):
    pass


class EndpointInterfaceUrlString477Parse(BaseModel):
    pass


class EndpointInterfaceUrlString478(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString478DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString478Defaults"]
    merge: Optional["EndpointInterfaceUrlString478Merge"]
    parse: Optional["EndpointInterfaceUrlString478Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString478DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString478Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString478Merge(BaseModel):
    pass


class EndpointInterfaceUrlString478Parse(BaseModel):
    pass


class EndpointInterfaceUrlString479(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString479DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString479Defaults"]
    merge: Optional["EndpointInterfaceUrlString479Merge"]
    parse: Optional["EndpointInterfaceUrlString479Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString479DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString479Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString479Merge(BaseModel):
    pass


class EndpointInterfaceUrlString479Parse(BaseModel):
    pass


class EndpointInterfaceUrlString47DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString47Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString47Merge(BaseModel):
    pass


class EndpointInterfaceUrlString47Parse(BaseModel):
    pass


class EndpointInterfaceUrlString48(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString48DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString48Defaults"]
    merge: Optional["EndpointInterfaceUrlString48Merge"]
    parse: Optional["EndpointInterfaceUrlString48Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString480(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString480DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString480Defaults"]
    merge: Optional["EndpointInterfaceUrlString480Merge"]
    parse: Optional["EndpointInterfaceUrlString480Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString480DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString480Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString480Merge(BaseModel):
    pass


class EndpointInterfaceUrlString480Parse(BaseModel):
    pass


class EndpointInterfaceUrlString481(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString481DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString481Defaults"]
    merge: Optional["EndpointInterfaceUrlString481Merge"]
    parse: Optional["EndpointInterfaceUrlString481Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString481DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString481Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString481Merge(BaseModel):
    pass


class EndpointInterfaceUrlString481Parse(BaseModel):
    pass


class EndpointInterfaceUrlString482(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString482DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString482Defaults"]
    merge: Optional["EndpointInterfaceUrlString482Merge"]
    parse: Optional["EndpointInterfaceUrlString482Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString482DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString482Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString482Merge(BaseModel):
    pass


class EndpointInterfaceUrlString482Parse(BaseModel):
    pass


class EndpointInterfaceUrlString483(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString483DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString483Defaults"]
    merge: Optional["EndpointInterfaceUrlString483Merge"]
    parse: Optional["EndpointInterfaceUrlString483Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString483DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString483Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString483Merge(BaseModel):
    pass


class EndpointInterfaceUrlString483Parse(BaseModel):
    pass


class EndpointInterfaceUrlString484(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString484DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString484Defaults"]
    merge: Optional["EndpointInterfaceUrlString484Merge"]
    parse: Optional["EndpointInterfaceUrlString484Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString484DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString484Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString484Merge(BaseModel):
    pass


class EndpointInterfaceUrlString484Parse(BaseModel):
    pass


class EndpointInterfaceUrlString485(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString485DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString485Defaults"]
    merge: Optional["EndpointInterfaceUrlString485Merge"]
    parse: Optional["EndpointInterfaceUrlString485Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString485DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString485Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString485Merge(BaseModel):
    pass


class EndpointInterfaceUrlString485Parse(BaseModel):
    pass


class EndpointInterfaceUrlString486(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString486DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString486Defaults"]
    merge: Optional["EndpointInterfaceUrlString486Merge"]
    parse: Optional["EndpointInterfaceUrlString486Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString486DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString486Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString486Merge(BaseModel):
    pass


class EndpointInterfaceUrlString486Parse(BaseModel):
    pass


class EndpointInterfaceUrlString487(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString487DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString487Defaults"]
    merge: Optional["EndpointInterfaceUrlString487Merge"]
    parse: Optional["EndpointInterfaceUrlString487Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString487DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString487Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString487Merge(BaseModel):
    pass


class EndpointInterfaceUrlString487Parse(BaseModel):
    pass


class EndpointInterfaceUrlString488(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString488DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString488Defaults"]
    merge: Optional["EndpointInterfaceUrlString488Merge"]
    parse: Optional["EndpointInterfaceUrlString488Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString488DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString488Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString488Merge(BaseModel):
    pass


class EndpointInterfaceUrlString488Parse(BaseModel):
    pass


class EndpointInterfaceUrlString489(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString489DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString489Defaults"]
    merge: Optional["EndpointInterfaceUrlString489Merge"]
    parse: Optional["EndpointInterfaceUrlString489Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString489DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString489Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString489Merge(BaseModel):
    pass


class EndpointInterfaceUrlString489Parse(BaseModel):
    pass


class EndpointInterfaceUrlString48DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString48Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString48Merge(BaseModel):
    pass


class EndpointInterfaceUrlString48Parse(BaseModel):
    pass


class EndpointInterfaceUrlString49(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString49DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString49Defaults"]
    merge: Optional["EndpointInterfaceUrlString49Merge"]
    parse: Optional["EndpointInterfaceUrlString49Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString490(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString490DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString490Defaults"]
    merge: Optional["EndpointInterfaceUrlString490Merge"]
    parse: Optional["EndpointInterfaceUrlString490Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString490DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString490Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString490Merge(BaseModel):
    pass


class EndpointInterfaceUrlString490Parse(BaseModel):
    pass


class EndpointInterfaceUrlString491(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString491DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString491Defaults"]
    merge: Optional["EndpointInterfaceUrlString491Merge"]
    parse: Optional["EndpointInterfaceUrlString491Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString491DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString491Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString491Merge(BaseModel):
    pass


class EndpointInterfaceUrlString491Parse(BaseModel):
    pass


class EndpointInterfaceUrlString492(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString492DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString492Defaults"]
    merge: Optional["EndpointInterfaceUrlString492Merge"]
    parse: Optional["EndpointInterfaceUrlString492Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString492DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString492Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString492Merge(BaseModel):
    pass


class EndpointInterfaceUrlString492Parse(BaseModel):
    pass


class EndpointInterfaceUrlString493(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString493DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString493Defaults"]
    merge: Optional["EndpointInterfaceUrlString493Merge"]
    parse: Optional["EndpointInterfaceUrlString493Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString493DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString493Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString493Merge(BaseModel):
    pass


class EndpointInterfaceUrlString493Parse(BaseModel):
    pass


class EndpointInterfaceUrlString494(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString494DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString494Defaults"]
    merge: Optional["EndpointInterfaceUrlString494Merge"]
    parse: Optional["EndpointInterfaceUrlString494Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString494DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString494Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString494Merge(BaseModel):
    pass


class EndpointInterfaceUrlString494Parse(BaseModel):
    pass


class EndpointInterfaceUrlString495(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString495DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString495Defaults"]
    merge: Optional["EndpointInterfaceUrlString495Merge"]
    parse: Optional["EndpointInterfaceUrlString495Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString495DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString495Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString495Merge(BaseModel):
    pass


class EndpointInterfaceUrlString495Parse(BaseModel):
    pass


class EndpointInterfaceUrlString496(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString496DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString496Defaults"]
    merge: Optional["EndpointInterfaceUrlString496Merge"]
    parse: Optional["EndpointInterfaceUrlString496Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString496DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString496Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString496Merge(BaseModel):
    pass


class EndpointInterfaceUrlString496Parse(BaseModel):
    pass


class EndpointInterfaceUrlString497(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString497DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString497Defaults"]
    merge: Optional["EndpointInterfaceUrlString497Merge"]
    parse: Optional["EndpointInterfaceUrlString497Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString497DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString497Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString497Merge(BaseModel):
    pass


class EndpointInterfaceUrlString497Parse(BaseModel):
    pass


class EndpointInterfaceUrlString498(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString498DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString498Defaults"]
    merge: Optional["EndpointInterfaceUrlString498Merge"]
    parse: Optional["EndpointInterfaceUrlString498Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString498DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString498Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString498Merge(BaseModel):
    pass


class EndpointInterfaceUrlString498Parse(BaseModel):
    pass


class EndpointInterfaceUrlString499(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString499DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString499Defaults"]
    merge: Optional["EndpointInterfaceUrlString499Merge"]
    parse: Optional["EndpointInterfaceUrlString499Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString499DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString499Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString499Merge(BaseModel):
    pass


class EndpointInterfaceUrlString499Parse(BaseModel):
    pass


class EndpointInterfaceUrlString49DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString49Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString49Merge(BaseModel):
    pass


class EndpointInterfaceUrlString49Parse(BaseModel):
    pass


class EndpointInterfaceUrlString4DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString4Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString4Merge(BaseModel):
    pass


class EndpointInterfaceUrlString4Parse(BaseModel):
    pass


class EndpointInterfaceUrlString5(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString5DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString5Defaults"]
    merge: Optional["EndpointInterfaceUrlString5Merge"]
    parse: Optional["EndpointInterfaceUrlString5Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString50(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString50DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString50Defaults"]
    merge: Optional["EndpointInterfaceUrlString50Merge"]
    parse: Optional["EndpointInterfaceUrlString50Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString500(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString500DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString500Defaults"]
    merge: Optional["EndpointInterfaceUrlString500Merge"]
    parse: Optional["EndpointInterfaceUrlString500Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString500DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString500Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString500Merge(BaseModel):
    pass


class EndpointInterfaceUrlString500Parse(BaseModel):
    pass


class EndpointInterfaceUrlString501(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString501DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString501Defaults"]
    merge: Optional["EndpointInterfaceUrlString501Merge"]
    parse: Optional["EndpointInterfaceUrlString501Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString501DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString501Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString501Merge(BaseModel):
    pass


class EndpointInterfaceUrlString501Parse(BaseModel):
    pass


class EndpointInterfaceUrlString502(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString502DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString502Defaults"]
    merge: Optional["EndpointInterfaceUrlString502Merge"]
    parse: Optional["EndpointInterfaceUrlString502Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString502DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString502Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString502Merge(BaseModel):
    pass


class EndpointInterfaceUrlString502Parse(BaseModel):
    pass


class EndpointInterfaceUrlString503(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString503DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString503Defaults"]
    merge: Optional["EndpointInterfaceUrlString503Merge"]
    parse: Optional["EndpointInterfaceUrlString503Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString503DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString503Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString503Merge(BaseModel):
    pass


class EndpointInterfaceUrlString503Parse(BaseModel):
    pass


class EndpointInterfaceUrlString504(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString504DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString504Defaults"]
    merge: Optional["EndpointInterfaceUrlString504Merge"]
    parse: Optional["EndpointInterfaceUrlString504Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString504DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString504Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString504Merge(BaseModel):
    pass


class EndpointInterfaceUrlString504Parse(BaseModel):
    pass


class EndpointInterfaceUrlString505(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString505DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString505Defaults"]
    merge: Optional["EndpointInterfaceUrlString505Merge"]
    parse: Optional["EndpointInterfaceUrlString505Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString505DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString505Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString505Merge(BaseModel):
    pass


class EndpointInterfaceUrlString505Parse(BaseModel):
    pass


class EndpointInterfaceUrlString506(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString506DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString506Defaults"]
    merge: Optional["EndpointInterfaceUrlString506Merge"]
    parse: Optional["EndpointInterfaceUrlString506Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString506DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString506Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString506Merge(BaseModel):
    pass


class EndpointInterfaceUrlString506Parse(BaseModel):
    pass


class EndpointInterfaceUrlString507(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString507DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString507Defaults"]
    merge: Optional["EndpointInterfaceUrlString507Merge"]
    parse: Optional["EndpointInterfaceUrlString507Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString507DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString507Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString507Merge(BaseModel):
    pass


class EndpointInterfaceUrlString507Parse(BaseModel):
    pass


class EndpointInterfaceUrlString508(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString508DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString508Defaults"]
    merge: Optional["EndpointInterfaceUrlString508Merge"]
    parse: Optional["EndpointInterfaceUrlString508Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString508DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString508Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString508Merge(BaseModel):
    pass


class EndpointInterfaceUrlString508Parse(BaseModel):
    pass


class EndpointInterfaceUrlString509(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString509DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString509Defaults"]
    merge: Optional["EndpointInterfaceUrlString509Merge"]
    parse: Optional["EndpointInterfaceUrlString509Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString509DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString509Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString509Merge(BaseModel):
    pass


class EndpointInterfaceUrlString509Parse(BaseModel):
    pass


class EndpointInterfaceUrlString50DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString50Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString50Merge(BaseModel):
    pass


class EndpointInterfaceUrlString50Parse(BaseModel):
    pass


class EndpointInterfaceUrlString51(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString51DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString51Defaults"]
    merge: Optional["EndpointInterfaceUrlString51Merge"]
    parse: Optional["EndpointInterfaceUrlString51Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString510(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString510DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString510Defaults"]
    merge: Optional["EndpointInterfaceUrlString510Merge"]
    parse: Optional["EndpointInterfaceUrlString510Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString510DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString510Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString510Merge(BaseModel):
    pass


class EndpointInterfaceUrlString510Parse(BaseModel):
    pass


class EndpointInterfaceUrlString511(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString511DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString511Defaults"]
    merge: Optional["EndpointInterfaceUrlString511Merge"]
    parse: Optional["EndpointInterfaceUrlString511Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString511DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString511Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString511Merge(BaseModel):
    pass


class EndpointInterfaceUrlString511Parse(BaseModel):
    pass


class EndpointInterfaceUrlString512(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString512DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString512Defaults"]
    merge: Optional["EndpointInterfaceUrlString512Merge"]
    parse: Optional["EndpointInterfaceUrlString512Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString512DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString512Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString512Merge(BaseModel):
    pass


class EndpointInterfaceUrlString512Parse(BaseModel):
    pass


class EndpointInterfaceUrlString513(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString513DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString513Defaults"]
    merge: Optional["EndpointInterfaceUrlString513Merge"]
    parse: Optional["EndpointInterfaceUrlString513Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString513DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString513Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString513Merge(BaseModel):
    pass


class EndpointInterfaceUrlString513Parse(BaseModel):
    pass


class EndpointInterfaceUrlString514(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString514DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString514Defaults"]
    merge: Optional["EndpointInterfaceUrlString514Merge"]
    parse: Optional["EndpointInterfaceUrlString514Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString514DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString514Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString514Merge(BaseModel):
    pass


class EndpointInterfaceUrlString514Parse(BaseModel):
    pass


class EndpointInterfaceUrlString515(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString515DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString515Defaults"]
    merge: Optional["EndpointInterfaceUrlString515Merge"]
    parse: Optional["EndpointInterfaceUrlString515Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString515DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString515Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString515Merge(BaseModel):
    pass


class EndpointInterfaceUrlString515Parse(BaseModel):
    pass


class EndpointInterfaceUrlString516(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString516DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString516Defaults"]
    merge: Optional["EndpointInterfaceUrlString516Merge"]
    parse: Optional["EndpointInterfaceUrlString516Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString516DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString516Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString516Merge(BaseModel):
    pass


class EndpointInterfaceUrlString516Parse(BaseModel):
    pass


class EndpointInterfaceUrlString517(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString517DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString517Defaults"]
    merge: Optional["EndpointInterfaceUrlString517Merge"]
    parse: Optional["EndpointInterfaceUrlString517Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString517DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString517Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString517Merge(BaseModel):
    pass


class EndpointInterfaceUrlString517Parse(BaseModel):
    pass


class EndpointInterfaceUrlString518(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString518DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString518Defaults"]
    merge: Optional["EndpointInterfaceUrlString518Merge"]
    parse: Optional["EndpointInterfaceUrlString518Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString518DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString518Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString518Merge(BaseModel):
    pass


class EndpointInterfaceUrlString518Parse(BaseModel):
    pass


class EndpointInterfaceUrlString519(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString519DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString519Defaults"]
    merge: Optional["EndpointInterfaceUrlString519Merge"]
    parse: Optional["EndpointInterfaceUrlString519Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString519DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString519Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString519Merge(BaseModel):
    pass


class EndpointInterfaceUrlString519Parse(BaseModel):
    pass


class EndpointInterfaceUrlString51DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString51Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString51Merge(BaseModel):
    pass


class EndpointInterfaceUrlString51Parse(BaseModel):
    pass


class EndpointInterfaceUrlString52(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString52DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString52Defaults"]
    merge: Optional["EndpointInterfaceUrlString52Merge"]
    parse: Optional["EndpointInterfaceUrlString52Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString520(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString520DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString520Defaults"]
    merge: Optional["EndpointInterfaceUrlString520Merge"]
    parse: Optional["EndpointInterfaceUrlString520Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString520DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString520Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString520Merge(BaseModel):
    pass


class EndpointInterfaceUrlString520Parse(BaseModel):
    pass


class EndpointInterfaceUrlString521(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString521DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString521Defaults"]
    merge: Optional["EndpointInterfaceUrlString521Merge"]
    parse: Optional["EndpointInterfaceUrlString521Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString521DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString521Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString521Merge(BaseModel):
    pass


class EndpointInterfaceUrlString521Parse(BaseModel):
    pass


class EndpointInterfaceUrlString522(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString522DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString522Defaults"]
    merge: Optional["EndpointInterfaceUrlString522Merge"]
    parse: Optional["EndpointInterfaceUrlString522Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString522DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString522Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString522Merge(BaseModel):
    pass


class EndpointInterfaceUrlString522Parse(BaseModel):
    pass


class EndpointInterfaceUrlString523(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString523DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString523Defaults"]
    merge: Optional["EndpointInterfaceUrlString523Merge"]
    parse: Optional["EndpointInterfaceUrlString523Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString523DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString523Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString523Merge(BaseModel):
    pass


class EndpointInterfaceUrlString523Parse(BaseModel):
    pass


class EndpointInterfaceUrlString524(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString524DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString524Defaults"]
    merge: Optional["EndpointInterfaceUrlString524Merge"]
    parse: Optional["EndpointInterfaceUrlString524Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString524DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString524Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString524Merge(BaseModel):
    pass


class EndpointInterfaceUrlString524Parse(BaseModel):
    pass


class EndpointInterfaceUrlString525(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString525DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString525Defaults"]
    merge: Optional["EndpointInterfaceUrlString525Merge"]
    parse: Optional["EndpointInterfaceUrlString525Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString525DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString525Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString525Merge(BaseModel):
    pass


class EndpointInterfaceUrlString525Parse(BaseModel):
    pass


class EndpointInterfaceUrlString526(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString526DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString526Defaults"]
    merge: Optional["EndpointInterfaceUrlString526Merge"]
    parse: Optional["EndpointInterfaceUrlString526Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString526DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString526Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString526Merge(BaseModel):
    pass


class EndpointInterfaceUrlString526Parse(BaseModel):
    pass


class EndpointInterfaceUrlString527(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString527DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString527Defaults"]
    merge: Optional["EndpointInterfaceUrlString527Merge"]
    parse: Optional["EndpointInterfaceUrlString527Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString527DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString527Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString527Merge(BaseModel):
    pass


class EndpointInterfaceUrlString527Parse(BaseModel):
    pass


class EndpointInterfaceUrlString528(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString528DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString528Defaults"]
    merge: Optional["EndpointInterfaceUrlString528Merge"]
    parse: Optional["EndpointInterfaceUrlString528Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString528DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString528Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString528Merge(BaseModel):
    pass


class EndpointInterfaceUrlString528Parse(BaseModel):
    pass


class EndpointInterfaceUrlString529(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString529DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString529Defaults"]
    merge: Optional["EndpointInterfaceUrlString529Merge"]
    parse: Optional["EndpointInterfaceUrlString529Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString529DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString529Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString529Merge(BaseModel):
    pass


class EndpointInterfaceUrlString529Parse(BaseModel):
    pass


class EndpointInterfaceUrlString52DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString52Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString52Merge(BaseModel):
    pass


class EndpointInterfaceUrlString52Parse(BaseModel):
    pass


class EndpointInterfaceUrlString53(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString53DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString53Defaults"]
    merge: Optional["EndpointInterfaceUrlString53Merge"]
    parse: Optional["EndpointInterfaceUrlString53Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString530(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString530DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString530Defaults"]
    merge: Optional["EndpointInterfaceUrlString530Merge"]
    parse: Optional["EndpointInterfaceUrlString530Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString530DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString530Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString530Merge(BaseModel):
    pass


class EndpointInterfaceUrlString530Parse(BaseModel):
    pass


class EndpointInterfaceUrlString531(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString531DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString531Defaults"]
    merge: Optional["EndpointInterfaceUrlString531Merge"]
    parse: Optional["EndpointInterfaceUrlString531Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString531DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString531Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString531Merge(BaseModel):
    pass


class EndpointInterfaceUrlString531Parse(BaseModel):
    pass


class EndpointInterfaceUrlString532(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString532DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString532Defaults"]
    merge: Optional["EndpointInterfaceUrlString532Merge"]
    parse: Optional["EndpointInterfaceUrlString532Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString532DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString532Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString532Merge(BaseModel):
    pass


class EndpointInterfaceUrlString532Parse(BaseModel):
    pass


class EndpointInterfaceUrlString533(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString533DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString533Defaults"]
    merge: Optional["EndpointInterfaceUrlString533Merge"]
    parse: Optional["EndpointInterfaceUrlString533Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString533DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString533Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString533Merge(BaseModel):
    pass


class EndpointInterfaceUrlString533Parse(BaseModel):
    pass


class EndpointInterfaceUrlString534(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString534DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString534Defaults"]
    merge: Optional["EndpointInterfaceUrlString534Merge"]
    parse: Optional["EndpointInterfaceUrlString534Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString534DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString534Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString534Merge(BaseModel):
    pass


class EndpointInterfaceUrlString534Parse(BaseModel):
    pass


class EndpointInterfaceUrlString535(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString535DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString535Defaults"]
    merge: Optional["EndpointInterfaceUrlString535Merge"]
    parse: Optional["EndpointInterfaceUrlString535Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString535DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString535Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString535Merge(BaseModel):
    pass


class EndpointInterfaceUrlString535Parse(BaseModel):
    pass


class EndpointInterfaceUrlString536(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString536DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString536Defaults"]
    merge: Optional["EndpointInterfaceUrlString536Merge"]
    parse: Optional["EndpointInterfaceUrlString536Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString536DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString536Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString536Merge(BaseModel):
    pass


class EndpointInterfaceUrlString536Parse(BaseModel):
    pass


class EndpointInterfaceUrlString537(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString537DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString537Defaults"]
    merge: Optional["EndpointInterfaceUrlString537Merge"]
    parse: Optional["EndpointInterfaceUrlString537Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString537DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString537Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString537Merge(BaseModel):
    pass


class EndpointInterfaceUrlString537Parse(BaseModel):
    pass


class EndpointInterfaceUrlString538(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString538DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString538Defaults"]
    merge: Optional["EndpointInterfaceUrlString538Merge"]
    parse: Optional["EndpointInterfaceUrlString538Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString538DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString538Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString538Merge(BaseModel):
    pass


class EndpointInterfaceUrlString538Parse(BaseModel):
    pass


class EndpointInterfaceUrlString539(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString539DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString539Defaults"]
    merge: Optional["EndpointInterfaceUrlString539Merge"]
    parse: Optional["EndpointInterfaceUrlString539Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString539DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString539Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString539Merge(BaseModel):
    pass


class EndpointInterfaceUrlString539Parse(BaseModel):
    pass


class EndpointInterfaceUrlString53DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString53Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString53Merge(BaseModel):
    pass


class EndpointInterfaceUrlString53Parse(BaseModel):
    pass


class EndpointInterfaceUrlString54(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString54DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString54Defaults"]
    merge: Optional["EndpointInterfaceUrlString54Merge"]
    parse: Optional["EndpointInterfaceUrlString54Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString540(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString540DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString540Defaults"]
    merge: Optional["EndpointInterfaceUrlString540Merge"]
    parse: Optional["EndpointInterfaceUrlString540Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString540DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString540Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString540Merge(BaseModel):
    pass


class EndpointInterfaceUrlString540Parse(BaseModel):
    pass


class EndpointInterfaceUrlString541(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString541DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString541Defaults"]
    merge: Optional["EndpointInterfaceUrlString541Merge"]
    parse: Optional["EndpointInterfaceUrlString541Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString541DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString541Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString541Merge(BaseModel):
    pass


class EndpointInterfaceUrlString541Parse(BaseModel):
    pass


class EndpointInterfaceUrlString542(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString542DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString542Defaults"]
    merge: Optional["EndpointInterfaceUrlString542Merge"]
    parse: Optional["EndpointInterfaceUrlString542Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString542DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString542Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString542Merge(BaseModel):
    pass


class EndpointInterfaceUrlString542Parse(BaseModel):
    pass


class EndpointInterfaceUrlString543(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString543DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString543Defaults"]
    merge: Optional["EndpointInterfaceUrlString543Merge"]
    parse: Optional["EndpointInterfaceUrlString543Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString543DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString543Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString543Merge(BaseModel):
    pass


class EndpointInterfaceUrlString543Parse(BaseModel):
    pass


class EndpointInterfaceUrlString544(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString544DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString544Defaults"]
    merge: Optional["EndpointInterfaceUrlString544Merge"]
    parse: Optional["EndpointInterfaceUrlString544Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString544DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString544Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString544Merge(BaseModel):
    pass


class EndpointInterfaceUrlString544Parse(BaseModel):
    pass


class EndpointInterfaceUrlString545(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString545DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString545Defaults"]
    merge: Optional["EndpointInterfaceUrlString545Merge"]
    parse: Optional["EndpointInterfaceUrlString545Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString545DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString545Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString545Merge(BaseModel):
    pass


class EndpointInterfaceUrlString545Parse(BaseModel):
    pass


class EndpointInterfaceUrlString546(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString546DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString546Defaults"]
    merge: Optional["EndpointInterfaceUrlString546Merge"]
    parse: Optional["EndpointInterfaceUrlString546Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString546DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString546Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString546Merge(BaseModel):
    pass


class EndpointInterfaceUrlString546Parse(BaseModel):
    pass


class EndpointInterfaceUrlString547(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString547DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString547Defaults"]
    merge: Optional["EndpointInterfaceUrlString547Merge"]
    parse: Optional["EndpointInterfaceUrlString547Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString547DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString547Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString547Merge(BaseModel):
    pass


class EndpointInterfaceUrlString547Parse(BaseModel):
    pass


class EndpointInterfaceUrlString548(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString548DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString548Defaults"]
    merge: Optional["EndpointInterfaceUrlString548Merge"]
    parse: Optional["EndpointInterfaceUrlString548Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString548DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString548Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString548Merge(BaseModel):
    pass


class EndpointInterfaceUrlString548Parse(BaseModel):
    pass


class EndpointInterfaceUrlString549(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString549DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString549Defaults"]
    merge: Optional["EndpointInterfaceUrlString549Merge"]
    parse: Optional["EndpointInterfaceUrlString549Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString549DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString549Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString549Merge(BaseModel):
    pass


class EndpointInterfaceUrlString549Parse(BaseModel):
    pass


class EndpointInterfaceUrlString54DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString54Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString54Merge(BaseModel):
    pass


class EndpointInterfaceUrlString54Parse(BaseModel):
    pass


class EndpointInterfaceUrlString55(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString55DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString55Defaults"]
    merge: Optional["EndpointInterfaceUrlString55Merge"]
    parse: Optional["EndpointInterfaceUrlString55Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString550(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString550DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString550Defaults"]
    merge: Optional["EndpointInterfaceUrlString550Merge"]
    parse: Optional["EndpointInterfaceUrlString550Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString550DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString550Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString550Merge(BaseModel):
    pass


class EndpointInterfaceUrlString550Parse(BaseModel):
    pass


class EndpointInterfaceUrlString551(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString551DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString551Defaults"]
    merge: Optional["EndpointInterfaceUrlString551Merge"]
    parse: Optional["EndpointInterfaceUrlString551Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString551DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString551Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString551Merge(BaseModel):
    pass


class EndpointInterfaceUrlString551Parse(BaseModel):
    pass


class EndpointInterfaceUrlString552(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString552DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString552Defaults"]
    merge: Optional["EndpointInterfaceUrlString552Merge"]
    parse: Optional["EndpointInterfaceUrlString552Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString552DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString552Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString552Merge(BaseModel):
    pass


class EndpointInterfaceUrlString552Parse(BaseModel):
    pass


class EndpointInterfaceUrlString553(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString553DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString553Defaults"]
    merge: Optional["EndpointInterfaceUrlString553Merge"]
    parse: Optional["EndpointInterfaceUrlString553Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString553DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString553Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString553Merge(BaseModel):
    pass


class EndpointInterfaceUrlString553Parse(BaseModel):
    pass


class EndpointInterfaceUrlString554(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString554DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString554Defaults"]
    merge: Optional["EndpointInterfaceUrlString554Merge"]
    parse: Optional["EndpointInterfaceUrlString554Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString554DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString554Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString554Merge(BaseModel):
    pass


class EndpointInterfaceUrlString554Parse(BaseModel):
    pass


class EndpointInterfaceUrlString555(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString555DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString555Defaults"]
    merge: Optional["EndpointInterfaceUrlString555Merge"]
    parse: Optional["EndpointInterfaceUrlString555Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString555DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString555Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString555Merge(BaseModel):
    pass


class EndpointInterfaceUrlString555Parse(BaseModel):
    pass


class EndpointInterfaceUrlString556(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString556DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString556Defaults"]
    merge: Optional["EndpointInterfaceUrlString556Merge"]
    parse: Optional["EndpointInterfaceUrlString556Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString556DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString556Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString556Merge(BaseModel):
    pass


class EndpointInterfaceUrlString556Parse(BaseModel):
    pass


class EndpointInterfaceUrlString557(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString557DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString557Defaults"]
    merge: Optional["EndpointInterfaceUrlString557Merge"]
    parse: Optional["EndpointInterfaceUrlString557Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString557DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString557Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString557Merge(BaseModel):
    pass


class EndpointInterfaceUrlString557Parse(BaseModel):
    pass


class EndpointInterfaceUrlString558(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString558DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString558Defaults"]
    merge: Optional["EndpointInterfaceUrlString558Merge"]
    parse: Optional["EndpointInterfaceUrlString558Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString558DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString558Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString558Merge(BaseModel):
    pass


class EndpointInterfaceUrlString558Parse(BaseModel):
    pass


class EndpointInterfaceUrlString559(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString559DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString559Defaults"]
    merge: Optional["EndpointInterfaceUrlString559Merge"]
    parse: Optional["EndpointInterfaceUrlString559Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString559DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString559Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString559Merge(BaseModel):
    pass


class EndpointInterfaceUrlString559Parse(BaseModel):
    pass


class EndpointInterfaceUrlString55DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString55Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString55Merge(BaseModel):
    pass


class EndpointInterfaceUrlString55Parse(BaseModel):
    pass


class EndpointInterfaceUrlString56(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString56DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString56Defaults"]
    merge: Optional["EndpointInterfaceUrlString56Merge"]
    parse: Optional["EndpointInterfaceUrlString56Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString560(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString560DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString560Defaults"]
    merge: Optional["EndpointInterfaceUrlString560Merge"]
    parse: Optional["EndpointInterfaceUrlString560Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString560DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString560Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString560Merge(BaseModel):
    pass


class EndpointInterfaceUrlString560Parse(BaseModel):
    pass


class EndpointInterfaceUrlString561(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString561DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString561Defaults"]
    merge: Optional["EndpointInterfaceUrlString561Merge"]
    parse: Optional["EndpointInterfaceUrlString561Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString561DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString561Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString561Merge(BaseModel):
    pass


class EndpointInterfaceUrlString561Parse(BaseModel):
    pass


class EndpointInterfaceUrlString562(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString562DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString562Defaults"]
    merge: Optional["EndpointInterfaceUrlString562Merge"]
    parse: Optional["EndpointInterfaceUrlString562Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString562DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString562Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString562Merge(BaseModel):
    pass


class EndpointInterfaceUrlString562Parse(BaseModel):
    pass


class EndpointInterfaceUrlString563(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString563DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString563Defaults"]
    merge: Optional["EndpointInterfaceUrlString563Merge"]
    parse: Optional["EndpointInterfaceUrlString563Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString563DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString563Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString563Merge(BaseModel):
    pass


class EndpointInterfaceUrlString563Parse(BaseModel):
    pass


class EndpointInterfaceUrlString564(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString564DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString564Defaults"]
    merge: Optional["EndpointInterfaceUrlString564Merge"]
    parse: Optional["EndpointInterfaceUrlString564Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString564DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString564Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString564Merge(BaseModel):
    pass


class EndpointInterfaceUrlString564Parse(BaseModel):
    pass


class EndpointInterfaceUrlString565(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString565DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString565Defaults"]
    merge: Optional["EndpointInterfaceUrlString565Merge"]
    parse: Optional["EndpointInterfaceUrlString565Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString565DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString565Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString565Merge(BaseModel):
    pass


class EndpointInterfaceUrlString565Parse(BaseModel):
    pass


class EndpointInterfaceUrlString566(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString566DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString566Defaults"]
    merge: Optional["EndpointInterfaceUrlString566Merge"]
    parse: Optional["EndpointInterfaceUrlString566Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString566DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString566Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString566Merge(BaseModel):
    pass


class EndpointInterfaceUrlString566Parse(BaseModel):
    pass


class EndpointInterfaceUrlString567(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString567DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString567Defaults"]
    merge: Optional["EndpointInterfaceUrlString567Merge"]
    parse: Optional["EndpointInterfaceUrlString567Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString567DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString567Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString567Merge(BaseModel):
    pass


class EndpointInterfaceUrlString567Parse(BaseModel):
    pass


class EndpointInterfaceUrlString568(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString568DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString568Defaults"]
    merge: Optional["EndpointInterfaceUrlString568Merge"]
    parse: Optional["EndpointInterfaceUrlString568Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString568DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString568Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString568Merge(BaseModel):
    pass


class EndpointInterfaceUrlString568Parse(BaseModel):
    pass


class EndpointInterfaceUrlString569(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString569DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString569Defaults"]
    merge: Optional["EndpointInterfaceUrlString569Merge"]
    parse: Optional["EndpointInterfaceUrlString569Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString569DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString569Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString569Merge(BaseModel):
    pass


class EndpointInterfaceUrlString569Parse(BaseModel):
    pass


class EndpointInterfaceUrlString56DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString56Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString56Merge(BaseModel):
    pass


class EndpointInterfaceUrlString56Parse(BaseModel):
    pass


class EndpointInterfaceUrlString57(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString57DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString57Defaults"]
    merge: Optional["EndpointInterfaceUrlString57Merge"]
    parse: Optional["EndpointInterfaceUrlString57Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString570(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString570DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString570Defaults"]
    merge: Optional["EndpointInterfaceUrlString570Merge"]
    parse: Optional["EndpointInterfaceUrlString570Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString570DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString570Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString570Merge(BaseModel):
    pass


class EndpointInterfaceUrlString570Parse(BaseModel):
    pass


class EndpointInterfaceUrlString571(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString571DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString571Defaults"]
    merge: Optional["EndpointInterfaceUrlString571Merge"]
    parse: Optional["EndpointInterfaceUrlString571Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString571DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString571Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString571Merge(BaseModel):
    pass


class EndpointInterfaceUrlString571Parse(BaseModel):
    pass


class EndpointInterfaceUrlString572(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString572DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString572Defaults"]
    merge: Optional["EndpointInterfaceUrlString572Merge"]
    parse: Optional["EndpointInterfaceUrlString572Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString572DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString572Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString572Merge(BaseModel):
    pass


class EndpointInterfaceUrlString572Parse(BaseModel):
    pass


class EndpointInterfaceUrlString573(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString573DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString573Defaults"]
    merge: Optional["EndpointInterfaceUrlString573Merge"]
    parse: Optional["EndpointInterfaceUrlString573Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString573DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString573Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString573Merge(BaseModel):
    pass


class EndpointInterfaceUrlString573Parse(BaseModel):
    pass


class EndpointInterfaceUrlString574(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString574DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString574Defaults"]
    merge: Optional["EndpointInterfaceUrlString574Merge"]
    parse: Optional["EndpointInterfaceUrlString574Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString574DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString574Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString574Merge(BaseModel):
    pass


class EndpointInterfaceUrlString574Parse(BaseModel):
    pass


class EndpointInterfaceUrlString575(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString575DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString575Defaults"]
    merge: Optional["EndpointInterfaceUrlString575Merge"]
    parse: Optional["EndpointInterfaceUrlString575Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString575DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString575Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString575Merge(BaseModel):
    pass


class EndpointInterfaceUrlString575Parse(BaseModel):
    pass


class EndpointInterfaceUrlString576(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString576DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString576Defaults"]
    merge: Optional["EndpointInterfaceUrlString576Merge"]
    parse: Optional["EndpointInterfaceUrlString576Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString576DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString576Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString576Merge(BaseModel):
    pass


class EndpointInterfaceUrlString576Parse(BaseModel):
    pass


class EndpointInterfaceUrlString577(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString577DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString577Defaults"]
    merge: Optional["EndpointInterfaceUrlString577Merge"]
    parse: Optional["EndpointInterfaceUrlString577Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString577DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString577Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString577Merge(BaseModel):
    pass


class EndpointInterfaceUrlString577Parse(BaseModel):
    pass


class EndpointInterfaceUrlString578(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString578DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString578Defaults"]
    merge: Optional["EndpointInterfaceUrlString578Merge"]
    parse: Optional["EndpointInterfaceUrlString578Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString578DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString578Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString578Merge(BaseModel):
    pass


class EndpointInterfaceUrlString578Parse(BaseModel):
    pass


class EndpointInterfaceUrlString579(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString579DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString579Defaults"]
    merge: Optional["EndpointInterfaceUrlString579Merge"]
    parse: Optional["EndpointInterfaceUrlString579Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString579DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString579Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString579Merge(BaseModel):
    pass


class EndpointInterfaceUrlString579Parse(BaseModel):
    pass


class EndpointInterfaceUrlString57DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString57Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString57Merge(BaseModel):
    pass


class EndpointInterfaceUrlString57Parse(BaseModel):
    pass


class EndpointInterfaceUrlString58(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString58DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString58Defaults"]
    merge: Optional["EndpointInterfaceUrlString58Merge"]
    parse: Optional["EndpointInterfaceUrlString58Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString580(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString580DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString580Defaults"]
    merge: Optional["EndpointInterfaceUrlString580Merge"]
    parse: Optional["EndpointInterfaceUrlString580Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString580DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString580Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString580Merge(BaseModel):
    pass


class EndpointInterfaceUrlString580Parse(BaseModel):
    pass


class EndpointInterfaceUrlString581(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString581DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString581Defaults"]
    merge: Optional["EndpointInterfaceUrlString581Merge"]
    parse: Optional["EndpointInterfaceUrlString581Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString581DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString581Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString581Merge(BaseModel):
    pass


class EndpointInterfaceUrlString581Parse(BaseModel):
    pass


class EndpointInterfaceUrlString582(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString582DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString582Defaults"]
    merge: Optional["EndpointInterfaceUrlString582Merge"]
    parse: Optional["EndpointInterfaceUrlString582Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString582DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString582Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString582Merge(BaseModel):
    pass


class EndpointInterfaceUrlString582Parse(BaseModel):
    pass


class EndpointInterfaceUrlString583(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString583DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString583Defaults"]
    merge: Optional["EndpointInterfaceUrlString583Merge"]
    parse: Optional["EndpointInterfaceUrlString583Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString583DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString583Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString583Merge(BaseModel):
    pass


class EndpointInterfaceUrlString583Parse(BaseModel):
    pass


class EndpointInterfaceUrlString584(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString584DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString584Defaults"]
    merge: Optional["EndpointInterfaceUrlString584Merge"]
    parse: Optional["EndpointInterfaceUrlString584Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString584DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString584Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString584Merge(BaseModel):
    pass


class EndpointInterfaceUrlString584Parse(BaseModel):
    pass


class EndpointInterfaceUrlString585(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString585DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString585Defaults"]
    merge: Optional["EndpointInterfaceUrlString585Merge"]
    parse: Optional["EndpointInterfaceUrlString585Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString585DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString585Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString585Merge(BaseModel):
    pass


class EndpointInterfaceUrlString585Parse(BaseModel):
    pass


class EndpointInterfaceUrlString586(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString586DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString586Defaults"]
    merge: Optional["EndpointInterfaceUrlString586Merge"]
    parse: Optional["EndpointInterfaceUrlString586Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString586DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString586Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString586Merge(BaseModel):
    pass


class EndpointInterfaceUrlString586Parse(BaseModel):
    pass


class EndpointInterfaceUrlString587(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString587DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString587Defaults"]
    merge: Optional["EndpointInterfaceUrlString587Merge"]
    parse: Optional["EndpointInterfaceUrlString587Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString587DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString587Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString587Merge(BaseModel):
    pass


class EndpointInterfaceUrlString587Parse(BaseModel):
    pass


class EndpointInterfaceUrlString588(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString588DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString588Defaults"]
    merge: Optional["EndpointInterfaceUrlString588Merge"]
    parse: Optional["EndpointInterfaceUrlString588Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString588DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString588Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString588Merge(BaseModel):
    pass


class EndpointInterfaceUrlString588Parse(BaseModel):
    pass


class EndpointInterfaceUrlString589(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString589DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString589Defaults"]
    merge: Optional["EndpointInterfaceUrlString589Merge"]
    parse: Optional["EndpointInterfaceUrlString589Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString589DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString589Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString589Merge(BaseModel):
    pass


class EndpointInterfaceUrlString589Parse(BaseModel):
    pass


class EndpointInterfaceUrlString58DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString58Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString58Merge(BaseModel):
    pass


class EndpointInterfaceUrlString58Parse(BaseModel):
    pass


class EndpointInterfaceUrlString59(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString59DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString59Defaults"]
    merge: Optional["EndpointInterfaceUrlString59Merge"]
    parse: Optional["EndpointInterfaceUrlString59Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString590(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString590DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString590Defaults"]
    merge: Optional["EndpointInterfaceUrlString590Merge"]
    parse: Optional["EndpointInterfaceUrlString590Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString590DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString590Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString590Merge(BaseModel):
    pass


class EndpointInterfaceUrlString590Parse(BaseModel):
    pass


class EndpointInterfaceUrlString591(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString591DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString591Defaults"]
    merge: Optional["EndpointInterfaceUrlString591Merge"]
    parse: Optional["EndpointInterfaceUrlString591Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString591DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString591Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString591Merge(BaseModel):
    pass


class EndpointInterfaceUrlString591Parse(BaseModel):
    pass


class EndpointInterfaceUrlString592(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString592DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString592Defaults"]
    merge: Optional["EndpointInterfaceUrlString592Merge"]
    parse: Optional["EndpointInterfaceUrlString592Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString592DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString592Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString592Merge(BaseModel):
    pass


class EndpointInterfaceUrlString592Parse(BaseModel):
    pass


class EndpointInterfaceUrlString593(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString593DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString593Defaults"]
    merge: Optional["EndpointInterfaceUrlString593Merge"]
    parse: Optional["EndpointInterfaceUrlString593Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString593DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString593Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString593Merge(BaseModel):
    pass


class EndpointInterfaceUrlString593Parse(BaseModel):
    pass


class EndpointInterfaceUrlString594(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString594DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString594Defaults"]
    merge: Optional["EndpointInterfaceUrlString594Merge"]
    parse: Optional["EndpointInterfaceUrlString594Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString594DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString594Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString594Merge(BaseModel):
    pass


class EndpointInterfaceUrlString594Parse(BaseModel):
    pass


class EndpointInterfaceUrlString595(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString595DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString595Defaults"]
    merge: Optional["EndpointInterfaceUrlString595Merge"]
    parse: Optional["EndpointInterfaceUrlString595Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString595DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString595Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString595Merge(BaseModel):
    pass


class EndpointInterfaceUrlString595Parse(BaseModel):
    pass


class EndpointInterfaceUrlString596(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString596DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString596Defaults"]
    merge: Optional["EndpointInterfaceUrlString596Merge"]
    parse: Optional["EndpointInterfaceUrlString596Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString596DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString596Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString596Merge(BaseModel):
    pass


class EndpointInterfaceUrlString596Parse(BaseModel):
    pass


class EndpointInterfaceUrlString597(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString597DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString597Defaults"]
    merge: Optional["EndpointInterfaceUrlString597Merge"]
    parse: Optional["EndpointInterfaceUrlString597Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString597DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString597Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString597Merge(BaseModel):
    pass


class EndpointInterfaceUrlString597Parse(BaseModel):
    pass


class EndpointInterfaceUrlString598(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString598DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString598Defaults"]
    merge: Optional["EndpointInterfaceUrlString598Merge"]
    parse: Optional["EndpointInterfaceUrlString598Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString598DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString598Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString598Merge(BaseModel):
    pass


class EndpointInterfaceUrlString598Parse(BaseModel):
    pass


class EndpointInterfaceUrlString599(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString599DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString599Defaults"]
    merge: Optional["EndpointInterfaceUrlString599Merge"]
    parse: Optional["EndpointInterfaceUrlString599Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString599DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString599Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString599Merge(BaseModel):
    pass


class EndpointInterfaceUrlString599Parse(BaseModel):
    pass


class EndpointInterfaceUrlString59DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString59Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString59Merge(BaseModel):
    pass


class EndpointInterfaceUrlString59Parse(BaseModel):
    pass


class EndpointInterfaceUrlString5DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString5Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString5Merge(BaseModel):
    pass


class EndpointInterfaceUrlString5Parse(BaseModel):
    pass


class EndpointInterfaceUrlString6(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString6DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString6Defaults"]
    merge: Optional["EndpointInterfaceUrlString6Merge"]
    parse: Optional["EndpointInterfaceUrlString6Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString60(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString60DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString60Defaults"]
    merge: Optional["EndpointInterfaceUrlString60Merge"]
    parse: Optional["EndpointInterfaceUrlString60Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString600(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString600DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString600Defaults"]
    merge: Optional["EndpointInterfaceUrlString600Merge"]
    parse: Optional["EndpointInterfaceUrlString600Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString600DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString600Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString600Merge(BaseModel):
    pass


class EndpointInterfaceUrlString600Parse(BaseModel):
    pass


class EndpointInterfaceUrlString601(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString601DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString601Defaults"]
    merge: Optional["EndpointInterfaceUrlString601Merge"]
    parse: Optional["EndpointInterfaceUrlString601Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString601DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString601Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString601Merge(BaseModel):
    pass


class EndpointInterfaceUrlString601Parse(BaseModel):
    pass


class EndpointInterfaceUrlString602(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString602DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString602Defaults"]
    merge: Optional["EndpointInterfaceUrlString602Merge"]
    parse: Optional["EndpointInterfaceUrlString602Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString602DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString602Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString602Merge(BaseModel):
    pass


class EndpointInterfaceUrlString602Parse(BaseModel):
    pass


class EndpointInterfaceUrlString603(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString603DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString603Defaults"]
    merge: Optional["EndpointInterfaceUrlString603Merge"]
    parse: Optional["EndpointInterfaceUrlString603Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString603DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString603Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString603Merge(BaseModel):
    pass


class EndpointInterfaceUrlString603Parse(BaseModel):
    pass


class EndpointInterfaceUrlString604(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString604DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString604Defaults"]
    merge: Optional["EndpointInterfaceUrlString604Merge"]
    parse: Optional["EndpointInterfaceUrlString604Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString604DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString604Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString604Merge(BaseModel):
    pass


class EndpointInterfaceUrlString604Parse(BaseModel):
    pass


class EndpointInterfaceUrlString605(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString605DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString605Defaults"]
    merge: Optional["EndpointInterfaceUrlString605Merge"]
    parse: Optional["EndpointInterfaceUrlString605Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString605DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString605Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString605Merge(BaseModel):
    pass


class EndpointInterfaceUrlString605Parse(BaseModel):
    pass


class EndpointInterfaceUrlString606(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString606DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString606Defaults"]
    merge: Optional["EndpointInterfaceUrlString606Merge"]
    parse: Optional["EndpointInterfaceUrlString606Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString606DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString606Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString606Merge(BaseModel):
    pass


class EndpointInterfaceUrlString606Parse(BaseModel):
    pass


class EndpointInterfaceUrlString607(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString607DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString607Defaults"]
    merge: Optional["EndpointInterfaceUrlString607Merge"]
    parse: Optional["EndpointInterfaceUrlString607Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString607DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString607Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString607Merge(BaseModel):
    pass


class EndpointInterfaceUrlString607Parse(BaseModel):
    pass


class EndpointInterfaceUrlString608(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString608DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString608Defaults"]
    merge: Optional["EndpointInterfaceUrlString608Merge"]
    parse: Optional["EndpointInterfaceUrlString608Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString608DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString608Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString608Merge(BaseModel):
    pass


class EndpointInterfaceUrlString608Parse(BaseModel):
    pass


class EndpointInterfaceUrlString609(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString609DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString609Defaults"]
    merge: Optional["EndpointInterfaceUrlString609Merge"]
    parse: Optional["EndpointInterfaceUrlString609Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString609DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString609Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString609Merge(BaseModel):
    pass


class EndpointInterfaceUrlString609Parse(BaseModel):
    pass


class EndpointInterfaceUrlString60DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString60Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString60Merge(BaseModel):
    pass


class EndpointInterfaceUrlString60Parse(BaseModel):
    pass


class EndpointInterfaceUrlString61(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString61DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString61Defaults"]
    merge: Optional["EndpointInterfaceUrlString61Merge"]
    parse: Optional["EndpointInterfaceUrlString61Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString610(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString610DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString610Defaults"]
    merge: Optional["EndpointInterfaceUrlString610Merge"]
    parse: Optional["EndpointInterfaceUrlString610Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString610DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString610Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString610Merge(BaseModel):
    pass


class EndpointInterfaceUrlString610Parse(BaseModel):
    pass


class EndpointInterfaceUrlString611(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString611DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString611Defaults"]
    merge: Optional["EndpointInterfaceUrlString611Merge"]
    parse: Optional["EndpointInterfaceUrlString611Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString611DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString611Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString611Merge(BaseModel):
    pass


class EndpointInterfaceUrlString611Parse(BaseModel):
    pass


class EndpointInterfaceUrlString612(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString612DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString612Defaults"]
    merge: Optional["EndpointInterfaceUrlString612Merge"]
    parse: Optional["EndpointInterfaceUrlString612Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString612DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString612Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString612Merge(BaseModel):
    pass


class EndpointInterfaceUrlString612Parse(BaseModel):
    pass


class EndpointInterfaceUrlString613(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString613DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString613Defaults"]
    merge: Optional["EndpointInterfaceUrlString613Merge"]
    parse: Optional["EndpointInterfaceUrlString613Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString613DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString613Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString613Merge(BaseModel):
    pass


class EndpointInterfaceUrlString613Parse(BaseModel):
    pass


class EndpointInterfaceUrlString614(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString614DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString614Defaults"]
    merge: Optional["EndpointInterfaceUrlString614Merge"]
    parse: Optional["EndpointInterfaceUrlString614Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString614DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString614Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString614Merge(BaseModel):
    pass


class EndpointInterfaceUrlString614Parse(BaseModel):
    pass


class EndpointInterfaceUrlString615(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString615DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString615Defaults"]
    merge: Optional["EndpointInterfaceUrlString615Merge"]
    parse: Optional["EndpointInterfaceUrlString615Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString615DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString615Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString615Merge(BaseModel):
    pass


class EndpointInterfaceUrlString615Parse(BaseModel):
    pass


class EndpointInterfaceUrlString616(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString616DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString616Defaults"]
    merge: Optional["EndpointInterfaceUrlString616Merge"]
    parse: Optional["EndpointInterfaceUrlString616Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString616DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString616Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString616Merge(BaseModel):
    pass


class EndpointInterfaceUrlString616Parse(BaseModel):
    pass


class EndpointInterfaceUrlString617(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString617DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString617Defaults"]
    merge: Optional["EndpointInterfaceUrlString617Merge"]
    parse: Optional["EndpointInterfaceUrlString617Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString617DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString617Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString617Merge(BaseModel):
    pass


class EndpointInterfaceUrlString617Parse(BaseModel):
    pass


class EndpointInterfaceUrlString618(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString618DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString618Defaults"]
    merge: Optional["EndpointInterfaceUrlString618Merge"]
    parse: Optional["EndpointInterfaceUrlString618Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString618DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString618Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString618Merge(BaseModel):
    pass


class EndpointInterfaceUrlString618Parse(BaseModel):
    pass


class EndpointInterfaceUrlString619(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString619DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString619Defaults"]
    merge: Optional["EndpointInterfaceUrlString619Merge"]
    parse: Optional["EndpointInterfaceUrlString619Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString619DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString619Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString619Merge(BaseModel):
    pass


class EndpointInterfaceUrlString619Parse(BaseModel):
    pass


class EndpointInterfaceUrlString61DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString61Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString61Merge(BaseModel):
    pass


class EndpointInterfaceUrlString61Parse(BaseModel):
    pass


class EndpointInterfaceUrlString62(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString62DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString62Defaults"]
    merge: Optional["EndpointInterfaceUrlString62Merge"]
    parse: Optional["EndpointInterfaceUrlString62Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString620(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString620DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString620Defaults"]
    merge: Optional["EndpointInterfaceUrlString620Merge"]
    parse: Optional["EndpointInterfaceUrlString620Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString620DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString620Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString620Merge(BaseModel):
    pass


class EndpointInterfaceUrlString620Parse(BaseModel):
    pass


class EndpointInterfaceUrlString621(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString621DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString621Defaults"]
    merge: Optional["EndpointInterfaceUrlString621Merge"]
    parse: Optional["EndpointInterfaceUrlString621Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString621DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString621Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString621Merge(BaseModel):
    pass


class EndpointInterfaceUrlString621Parse(BaseModel):
    pass


class EndpointInterfaceUrlString622(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString622DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString622Defaults"]
    merge: Optional["EndpointInterfaceUrlString622Merge"]
    parse: Optional["EndpointInterfaceUrlString622Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString622DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString622Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString622Merge(BaseModel):
    pass


class EndpointInterfaceUrlString622Parse(BaseModel):
    pass


class EndpointInterfaceUrlString623(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString623DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString623Defaults"]
    merge: Optional["EndpointInterfaceUrlString623Merge"]
    parse: Optional["EndpointInterfaceUrlString623Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString623DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString623Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString623Merge(BaseModel):
    pass


class EndpointInterfaceUrlString623Parse(BaseModel):
    pass


class EndpointInterfaceUrlString624(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString624DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString624Defaults"]
    merge: Optional["EndpointInterfaceUrlString624Merge"]
    parse: Optional["EndpointInterfaceUrlString624Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString624DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString624Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString624Merge(BaseModel):
    pass


class EndpointInterfaceUrlString624Parse(BaseModel):
    pass


class EndpointInterfaceUrlString625(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString625DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString625Defaults"]
    merge: Optional["EndpointInterfaceUrlString625Merge"]
    parse: Optional["EndpointInterfaceUrlString625Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString625DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString625Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString625Merge(BaseModel):
    pass


class EndpointInterfaceUrlString625Parse(BaseModel):
    pass


class EndpointInterfaceUrlString626(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString626DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString626Defaults"]
    merge: Optional["EndpointInterfaceUrlString626Merge"]
    parse: Optional["EndpointInterfaceUrlString626Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString626DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString626Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString626Merge(BaseModel):
    pass


class EndpointInterfaceUrlString626Parse(BaseModel):
    pass


class EndpointInterfaceUrlString627(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString627DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString627Defaults"]
    merge: Optional["EndpointInterfaceUrlString627Merge"]
    parse: Optional["EndpointInterfaceUrlString627Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString627DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString627Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString627Merge(BaseModel):
    pass


class EndpointInterfaceUrlString627Parse(BaseModel):
    pass


class EndpointInterfaceUrlString628(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString628DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString628Defaults"]
    merge: Optional["EndpointInterfaceUrlString628Merge"]
    parse: Optional["EndpointInterfaceUrlString628Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString628DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString628Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString628Merge(BaseModel):
    pass


class EndpointInterfaceUrlString628Parse(BaseModel):
    pass


class EndpointInterfaceUrlString629(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString629DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString629Defaults"]
    merge: Optional["EndpointInterfaceUrlString629Merge"]
    parse: Optional["EndpointInterfaceUrlString629Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString629DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString629Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString629Merge(BaseModel):
    pass


class EndpointInterfaceUrlString629Parse(BaseModel):
    pass


class EndpointInterfaceUrlString62DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString62Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString62Merge(BaseModel):
    pass


class EndpointInterfaceUrlString62Parse(BaseModel):
    pass


class EndpointInterfaceUrlString63(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString63DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString63Defaults"]
    merge: Optional["EndpointInterfaceUrlString63Merge"]
    parse: Optional["EndpointInterfaceUrlString63Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString630(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString630DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString630Defaults"]
    merge: Optional["EndpointInterfaceUrlString630Merge"]
    parse: Optional["EndpointInterfaceUrlString630Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString630DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString630Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString630Merge(BaseModel):
    pass


class EndpointInterfaceUrlString630Parse(BaseModel):
    pass


class EndpointInterfaceUrlString631(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString631DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString631Defaults"]
    merge: Optional["EndpointInterfaceUrlString631Merge"]
    parse: Optional["EndpointInterfaceUrlString631Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString631DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString631Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString631Merge(BaseModel):
    pass


class EndpointInterfaceUrlString631Parse(BaseModel):
    pass


class EndpointInterfaceUrlString632(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString632DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString632Defaults"]
    merge: Optional["EndpointInterfaceUrlString632Merge"]
    parse: Optional["EndpointInterfaceUrlString632Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString632DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString632Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString632Merge(BaseModel):
    pass


class EndpointInterfaceUrlString632Parse(BaseModel):
    pass


class EndpointInterfaceUrlString633(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString633DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString633Defaults"]
    merge: Optional["EndpointInterfaceUrlString633Merge"]
    parse: Optional["EndpointInterfaceUrlString633Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString633DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString633Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString633Merge(BaseModel):
    pass


class EndpointInterfaceUrlString633Parse(BaseModel):
    pass


class EndpointInterfaceUrlString634(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString634DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString634Defaults"]
    merge: Optional["EndpointInterfaceUrlString634Merge"]
    parse: Optional["EndpointInterfaceUrlString634Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString634DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString634Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString634Merge(BaseModel):
    pass


class EndpointInterfaceUrlString634Parse(BaseModel):
    pass


class EndpointInterfaceUrlString635(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString635DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString635Defaults"]
    merge: Optional["EndpointInterfaceUrlString635Merge"]
    parse: Optional["EndpointInterfaceUrlString635Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString635DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString635Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString635Merge(BaseModel):
    pass


class EndpointInterfaceUrlString635Parse(BaseModel):
    pass


class EndpointInterfaceUrlString636(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString636DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString636Defaults"]
    merge: Optional["EndpointInterfaceUrlString636Merge"]
    parse: Optional["EndpointInterfaceUrlString636Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString636DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString636Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString636Merge(BaseModel):
    pass


class EndpointInterfaceUrlString636Parse(BaseModel):
    pass


class EndpointInterfaceUrlString637(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString637DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString637Defaults"]
    merge: Optional["EndpointInterfaceUrlString637Merge"]
    parse: Optional["EndpointInterfaceUrlString637Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString637DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString637Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString637Merge(BaseModel):
    pass


class EndpointInterfaceUrlString637Parse(BaseModel):
    pass


class EndpointInterfaceUrlString638(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString638DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString638Defaults"]
    merge: Optional["EndpointInterfaceUrlString638Merge"]
    parse: Optional["EndpointInterfaceUrlString638Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString638DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString638Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString638Merge(BaseModel):
    pass


class EndpointInterfaceUrlString638Parse(BaseModel):
    pass


class EndpointInterfaceUrlString639(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString639DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString639Defaults"]
    merge: Optional["EndpointInterfaceUrlString639Merge"]
    parse: Optional["EndpointInterfaceUrlString639Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString639DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString639Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString639Merge(BaseModel):
    pass


class EndpointInterfaceUrlString639Parse(BaseModel):
    pass


class EndpointInterfaceUrlString63DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString63Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString63Merge(BaseModel):
    pass


class EndpointInterfaceUrlString63Parse(BaseModel):
    pass


class EndpointInterfaceUrlString64(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString64DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString64Defaults"]
    merge: Optional["EndpointInterfaceUrlString64Merge"]
    parse: Optional["EndpointInterfaceUrlString64Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString640(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString640DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString640Defaults"]
    merge: Optional["EndpointInterfaceUrlString640Merge"]
    parse: Optional["EndpointInterfaceUrlString640Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString640DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString640Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString640Merge(BaseModel):
    pass


class EndpointInterfaceUrlString640Parse(BaseModel):
    pass


class EndpointInterfaceUrlString641(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString641DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString641Defaults"]
    merge: Optional["EndpointInterfaceUrlString641Merge"]
    parse: Optional["EndpointInterfaceUrlString641Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString641DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString641Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString641Merge(BaseModel):
    pass


class EndpointInterfaceUrlString641Parse(BaseModel):
    pass


class EndpointInterfaceUrlString642(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString642DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString642Defaults"]
    merge: Optional["EndpointInterfaceUrlString642Merge"]
    parse: Optional["EndpointInterfaceUrlString642Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString642DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString642Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString642Merge(BaseModel):
    pass


class EndpointInterfaceUrlString642Parse(BaseModel):
    pass


class EndpointInterfaceUrlString643(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString643DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString643Defaults"]
    merge: Optional["EndpointInterfaceUrlString643Merge"]
    parse: Optional["EndpointInterfaceUrlString643Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString643DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString643Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString643Merge(BaseModel):
    pass


class EndpointInterfaceUrlString643Parse(BaseModel):
    pass


class EndpointInterfaceUrlString644(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString644DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString644Defaults"]
    merge: Optional["EndpointInterfaceUrlString644Merge"]
    parse: Optional["EndpointInterfaceUrlString644Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString644DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString644Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString644Merge(BaseModel):
    pass


class EndpointInterfaceUrlString644Parse(BaseModel):
    pass


class EndpointInterfaceUrlString645(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString645DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString645Defaults"]
    merge: Optional["EndpointInterfaceUrlString645Merge"]
    parse: Optional["EndpointInterfaceUrlString645Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString645DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString645Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString645Merge(BaseModel):
    pass


class EndpointInterfaceUrlString645Parse(BaseModel):
    pass


class EndpointInterfaceUrlString646(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString646DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString646Defaults"]
    merge: Optional["EndpointInterfaceUrlString646Merge"]
    parse: Optional["EndpointInterfaceUrlString646Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString646DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString646Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString646Merge(BaseModel):
    pass


class EndpointInterfaceUrlString646Parse(BaseModel):
    pass


class EndpointInterfaceUrlString647(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString647DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString647Defaults"]
    merge: Optional["EndpointInterfaceUrlString647Merge"]
    parse: Optional["EndpointInterfaceUrlString647Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString647DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString647Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString647Merge(BaseModel):
    pass


class EndpointInterfaceUrlString647Parse(BaseModel):
    pass


class EndpointInterfaceUrlString648(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString648DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString648Defaults"]
    merge: Optional["EndpointInterfaceUrlString648Merge"]
    parse: Optional["EndpointInterfaceUrlString648Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString648DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString648Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString648Merge(BaseModel):
    pass


class EndpointInterfaceUrlString648Parse(BaseModel):
    pass


class EndpointInterfaceUrlString649(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString649DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString649Defaults"]
    merge: Optional["EndpointInterfaceUrlString649Merge"]
    parse: Optional["EndpointInterfaceUrlString649Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString649DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString649Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString649Merge(BaseModel):
    pass


class EndpointInterfaceUrlString649Parse(BaseModel):
    pass


class EndpointInterfaceUrlString64DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString64Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString64Merge(BaseModel):
    pass


class EndpointInterfaceUrlString64Parse(BaseModel):
    pass


class EndpointInterfaceUrlString65(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString65DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString65Defaults"]
    merge: Optional["EndpointInterfaceUrlString65Merge"]
    parse: Optional["EndpointInterfaceUrlString65Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString650(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString650DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString650Defaults"]
    merge: Optional["EndpointInterfaceUrlString650Merge"]
    parse: Optional["EndpointInterfaceUrlString650Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString650DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString650Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString650Merge(BaseModel):
    pass


class EndpointInterfaceUrlString650Parse(BaseModel):
    pass


class EndpointInterfaceUrlString651(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString651DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString651Defaults"]
    merge: Optional["EndpointInterfaceUrlString651Merge"]
    parse: Optional["EndpointInterfaceUrlString651Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString651DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString651Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString651Merge(BaseModel):
    pass


class EndpointInterfaceUrlString651Parse(BaseModel):
    pass


class EndpointInterfaceUrlString652(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString652DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString652Defaults"]
    merge: Optional["EndpointInterfaceUrlString652Merge"]
    parse: Optional["EndpointInterfaceUrlString652Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString652DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString652Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString652Merge(BaseModel):
    pass


class EndpointInterfaceUrlString652Parse(BaseModel):
    pass


class EndpointInterfaceUrlString653(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString653DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString653Defaults"]
    merge: Optional["EndpointInterfaceUrlString653Merge"]
    parse: Optional["EndpointInterfaceUrlString653Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString653DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString653Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString653Merge(BaseModel):
    pass


class EndpointInterfaceUrlString653Parse(BaseModel):
    pass


class EndpointInterfaceUrlString654(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString654DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString654Defaults"]
    merge: Optional["EndpointInterfaceUrlString654Merge"]
    parse: Optional["EndpointInterfaceUrlString654Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString654DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString654Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString654Merge(BaseModel):
    pass


class EndpointInterfaceUrlString654Parse(BaseModel):
    pass


class EndpointInterfaceUrlString655(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString655DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString655Defaults"]
    merge: Optional["EndpointInterfaceUrlString655Merge"]
    parse: Optional["EndpointInterfaceUrlString655Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString655DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString655Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString655Merge(BaseModel):
    pass


class EndpointInterfaceUrlString655Parse(BaseModel):
    pass


class EndpointInterfaceUrlString656(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString656DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString656Defaults"]
    merge: Optional["EndpointInterfaceUrlString656Merge"]
    parse: Optional["EndpointInterfaceUrlString656Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString656DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString656Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString656Merge(BaseModel):
    pass


class EndpointInterfaceUrlString656Parse(BaseModel):
    pass


class EndpointInterfaceUrlString657(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString657DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString657Defaults"]
    merge: Optional["EndpointInterfaceUrlString657Merge"]
    parse: Optional["EndpointInterfaceUrlString657Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString657DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString657Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString657Merge(BaseModel):
    pass


class EndpointInterfaceUrlString657Parse(BaseModel):
    pass


class EndpointInterfaceUrlString658(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString658DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString658Defaults"]
    merge: Optional["EndpointInterfaceUrlString658Merge"]
    parse: Optional["EndpointInterfaceUrlString658Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString658DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString658Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString658Merge(BaseModel):
    pass


class EndpointInterfaceUrlString658Parse(BaseModel):
    pass


class EndpointInterfaceUrlString659(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString659DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString659Defaults"]
    merge: Optional["EndpointInterfaceUrlString659Merge"]
    parse: Optional["EndpointInterfaceUrlString659Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString659DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString659Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString659Merge(BaseModel):
    pass


class EndpointInterfaceUrlString659Parse(BaseModel):
    pass


class EndpointInterfaceUrlString65DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString65Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString65Merge(BaseModel):
    pass


class EndpointInterfaceUrlString65Parse(BaseModel):
    pass


class EndpointInterfaceUrlString66(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString66DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString66Defaults"]
    merge: Optional["EndpointInterfaceUrlString66Merge"]
    parse: Optional["EndpointInterfaceUrlString66Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString660(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString660DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString660Defaults"]
    merge: Optional["EndpointInterfaceUrlString660Merge"]
    parse: Optional["EndpointInterfaceUrlString660Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString660DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString660Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString660Merge(BaseModel):
    pass


class EndpointInterfaceUrlString660Parse(BaseModel):
    pass


class EndpointInterfaceUrlString661(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString661DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString661Defaults"]
    merge: Optional["EndpointInterfaceUrlString661Merge"]
    parse: Optional["EndpointInterfaceUrlString661Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString661DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString661Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString661Merge(BaseModel):
    pass


class EndpointInterfaceUrlString661Parse(BaseModel):
    pass


class EndpointInterfaceUrlString662(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString662DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString662Defaults"]
    merge: Optional["EndpointInterfaceUrlString662Merge"]
    parse: Optional["EndpointInterfaceUrlString662Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString662DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString662Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString662Merge(BaseModel):
    pass


class EndpointInterfaceUrlString662Parse(BaseModel):
    pass


class EndpointInterfaceUrlString663(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString663DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString663Defaults"]
    merge: Optional["EndpointInterfaceUrlString663Merge"]
    parse: Optional["EndpointInterfaceUrlString663Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString663DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString663Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString663Merge(BaseModel):
    pass


class EndpointInterfaceUrlString663Parse(BaseModel):
    pass


class EndpointInterfaceUrlString664(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString664DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString664Defaults"]
    merge: Optional["EndpointInterfaceUrlString664Merge"]
    parse: Optional["EndpointInterfaceUrlString664Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString664DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString664Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString664Merge(BaseModel):
    pass


class EndpointInterfaceUrlString664Parse(BaseModel):
    pass


class EndpointInterfaceUrlString665(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString665DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString665Defaults"]
    merge: Optional["EndpointInterfaceUrlString665Merge"]
    parse: Optional["EndpointInterfaceUrlString665Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString665DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString665Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString665Merge(BaseModel):
    pass


class EndpointInterfaceUrlString665Parse(BaseModel):
    pass


class EndpointInterfaceUrlString666(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString666DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString666Defaults"]
    merge: Optional["EndpointInterfaceUrlString666Merge"]
    parse: Optional["EndpointInterfaceUrlString666Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString666DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString666Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString666Merge(BaseModel):
    pass


class EndpointInterfaceUrlString666Parse(BaseModel):
    pass


class EndpointInterfaceUrlString667(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString667DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString667Defaults"]
    merge: Optional["EndpointInterfaceUrlString667Merge"]
    parse: Optional["EndpointInterfaceUrlString667Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString667DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString667Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString667Merge(BaseModel):
    pass


class EndpointInterfaceUrlString667Parse(BaseModel):
    pass


class EndpointInterfaceUrlString668(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString668DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString668Defaults"]
    merge: Optional["EndpointInterfaceUrlString668Merge"]
    parse: Optional["EndpointInterfaceUrlString668Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString668DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString668Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString668Merge(BaseModel):
    pass


class EndpointInterfaceUrlString668Parse(BaseModel):
    pass


class EndpointInterfaceUrlString669(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString669DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString669Defaults"]
    merge: Optional["EndpointInterfaceUrlString669Merge"]
    parse: Optional["EndpointInterfaceUrlString669Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString669DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString669Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString669Merge(BaseModel):
    pass


class EndpointInterfaceUrlString669Parse(BaseModel):
    pass


class EndpointInterfaceUrlString66DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString66Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString66Merge(BaseModel):
    pass


class EndpointInterfaceUrlString66Parse(BaseModel):
    pass


class EndpointInterfaceUrlString67(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString67DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString67Defaults"]
    merge: Optional["EndpointInterfaceUrlString67Merge"]
    parse: Optional["EndpointInterfaceUrlString67Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString670(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString670DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString670Defaults"]
    merge: Optional["EndpointInterfaceUrlString670Merge"]
    parse: Optional["EndpointInterfaceUrlString670Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString670DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString670Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString670Merge(BaseModel):
    pass


class EndpointInterfaceUrlString670Parse(BaseModel):
    pass


class EndpointInterfaceUrlString671(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString671DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString671Defaults"]
    merge: Optional["EndpointInterfaceUrlString671Merge"]
    parse: Optional["EndpointInterfaceUrlString671Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString671DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString671Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString671Merge(BaseModel):
    pass


class EndpointInterfaceUrlString671Parse(BaseModel):
    pass


class EndpointInterfaceUrlString672(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString672DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString672Defaults"]
    merge: Optional["EndpointInterfaceUrlString672Merge"]
    parse: Optional["EndpointInterfaceUrlString672Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString672DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString672Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString672Merge(BaseModel):
    pass


class EndpointInterfaceUrlString672Parse(BaseModel):
    pass


class EndpointInterfaceUrlString673(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString673DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString673Defaults"]
    merge: Optional["EndpointInterfaceUrlString673Merge"]
    parse: Optional["EndpointInterfaceUrlString673Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString673DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString673Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString673Merge(BaseModel):
    pass


class EndpointInterfaceUrlString673Parse(BaseModel):
    pass


class EndpointInterfaceUrlString674(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString674DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString674Defaults"]
    merge: Optional["EndpointInterfaceUrlString674Merge"]
    parse: Optional["EndpointInterfaceUrlString674Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString674DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString674Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString674Merge(BaseModel):
    pass


class EndpointInterfaceUrlString674Parse(BaseModel):
    pass


class EndpointInterfaceUrlString675(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString675DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString675Defaults"]
    merge: Optional["EndpointInterfaceUrlString675Merge"]
    parse: Optional["EndpointInterfaceUrlString675Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString675DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString675Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString675Merge(BaseModel):
    pass


class EndpointInterfaceUrlString675Parse(BaseModel):
    pass


class EndpointInterfaceUrlString676(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString676DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString676Defaults"]
    merge: Optional["EndpointInterfaceUrlString676Merge"]
    parse: Optional["EndpointInterfaceUrlString676Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString676DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString676Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString676Merge(BaseModel):
    pass


class EndpointInterfaceUrlString676Parse(BaseModel):
    pass


class EndpointInterfaceUrlString677(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString677DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString677Defaults"]
    merge: Optional["EndpointInterfaceUrlString677Merge"]
    parse: Optional["EndpointInterfaceUrlString677Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString677DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString677Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString677Merge(BaseModel):
    pass


class EndpointInterfaceUrlString677Parse(BaseModel):
    pass


class EndpointInterfaceUrlString678(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString678DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString678Defaults"]
    merge: Optional["EndpointInterfaceUrlString678Merge"]
    parse: Optional["EndpointInterfaceUrlString678Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString678DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString678Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString678Merge(BaseModel):
    pass


class EndpointInterfaceUrlString678Parse(BaseModel):
    pass


class EndpointInterfaceUrlString679(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString679DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString679Defaults"]
    merge: Optional["EndpointInterfaceUrlString679Merge"]
    parse: Optional["EndpointInterfaceUrlString679Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString679DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString679Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString679Merge(BaseModel):
    pass


class EndpointInterfaceUrlString679Parse(BaseModel):
    pass


class EndpointInterfaceUrlString67DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString67Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString67Merge(BaseModel):
    pass


class EndpointInterfaceUrlString67Parse(BaseModel):
    pass


class EndpointInterfaceUrlString68(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString68DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString68Defaults"]
    merge: Optional["EndpointInterfaceUrlString68Merge"]
    parse: Optional["EndpointInterfaceUrlString68Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString680(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString680DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString680Defaults"]
    merge: Optional["EndpointInterfaceUrlString680Merge"]
    parse: Optional["EndpointInterfaceUrlString680Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString680DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString680Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString680Merge(BaseModel):
    pass


class EndpointInterfaceUrlString680Parse(BaseModel):
    pass


class EndpointInterfaceUrlString681(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString681DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString681Defaults"]
    merge: Optional["EndpointInterfaceUrlString681Merge"]
    parse: Optional["EndpointInterfaceUrlString681Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString681DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString681Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString681Merge(BaseModel):
    pass


class EndpointInterfaceUrlString681Parse(BaseModel):
    pass


class EndpointInterfaceUrlString682(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString682DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString682Defaults"]
    merge: Optional["EndpointInterfaceUrlString682Merge"]
    parse: Optional["EndpointInterfaceUrlString682Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString682DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString682Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString682Merge(BaseModel):
    pass


class EndpointInterfaceUrlString682Parse(BaseModel):
    pass


class EndpointInterfaceUrlString683(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString683DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString683Defaults"]
    merge: Optional["EndpointInterfaceUrlString683Merge"]
    parse: Optional["EndpointInterfaceUrlString683Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString683DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString683Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString683Merge(BaseModel):
    pass


class EndpointInterfaceUrlString683Parse(BaseModel):
    pass


class EndpointInterfaceUrlString684(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString684DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString684Defaults"]
    merge: Optional["EndpointInterfaceUrlString684Merge"]
    parse: Optional["EndpointInterfaceUrlString684Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString684DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString684Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString684Merge(BaseModel):
    pass


class EndpointInterfaceUrlString684Parse(BaseModel):
    pass


class EndpointInterfaceUrlString685(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString685DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString685Defaults"]
    merge: Optional["EndpointInterfaceUrlString685Merge"]
    parse: Optional["EndpointInterfaceUrlString685Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString685DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString685Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString685Merge(BaseModel):
    pass


class EndpointInterfaceUrlString685Parse(BaseModel):
    pass


class EndpointInterfaceUrlString686(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString686DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString686Defaults"]
    merge: Optional["EndpointInterfaceUrlString686Merge"]
    parse: Optional["EndpointInterfaceUrlString686Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString686DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString686Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString686Merge(BaseModel):
    pass


class EndpointInterfaceUrlString686Parse(BaseModel):
    pass


class EndpointInterfaceUrlString687(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString687DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString687Defaults"]
    merge: Optional["EndpointInterfaceUrlString687Merge"]
    parse: Optional["EndpointInterfaceUrlString687Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString687DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString687Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString687Merge(BaseModel):
    pass


class EndpointInterfaceUrlString687Parse(BaseModel):
    pass


class EndpointInterfaceUrlString688(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString688DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString688Defaults"]
    merge: Optional["EndpointInterfaceUrlString688Merge"]
    parse: Optional["EndpointInterfaceUrlString688Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString688DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString688Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString688Merge(BaseModel):
    pass


class EndpointInterfaceUrlString688Parse(BaseModel):
    pass


class EndpointInterfaceUrlString689(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString689DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString689Defaults"]
    merge: Optional["EndpointInterfaceUrlString689Merge"]
    parse: Optional["EndpointInterfaceUrlString689Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString689DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString689Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString689Merge(BaseModel):
    pass


class EndpointInterfaceUrlString689Parse(BaseModel):
    pass


class EndpointInterfaceUrlString68DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString68Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString68Merge(BaseModel):
    pass


class EndpointInterfaceUrlString68Parse(BaseModel):
    pass


class EndpointInterfaceUrlString69(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString69DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString69Defaults"]
    merge: Optional["EndpointInterfaceUrlString69Merge"]
    parse: Optional["EndpointInterfaceUrlString69Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString690(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString690DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString690Defaults"]
    merge: Optional["EndpointInterfaceUrlString690Merge"]
    parse: Optional["EndpointInterfaceUrlString690Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString690DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString690Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString690Merge(BaseModel):
    pass


class EndpointInterfaceUrlString690Parse(BaseModel):
    pass


class EndpointInterfaceUrlString691(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString691DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString691Defaults"]
    merge: Optional["EndpointInterfaceUrlString691Merge"]
    parse: Optional["EndpointInterfaceUrlString691Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString691DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString691Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString691Merge(BaseModel):
    pass


class EndpointInterfaceUrlString691Parse(BaseModel):
    pass


class EndpointInterfaceUrlString692(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString692DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString692Defaults"]
    merge: Optional["EndpointInterfaceUrlString692Merge"]
    parse: Optional["EndpointInterfaceUrlString692Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString692DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString692Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString692Merge(BaseModel):
    pass


class EndpointInterfaceUrlString692Parse(BaseModel):
    pass


class EndpointInterfaceUrlString693(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString693DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString693Defaults"]
    merge: Optional["EndpointInterfaceUrlString693Merge"]
    parse: Optional["EndpointInterfaceUrlString693Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString693DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString693Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString693Merge(BaseModel):
    pass


class EndpointInterfaceUrlString693Parse(BaseModel):
    pass


class EndpointInterfaceUrlString69DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString69Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString69Merge(BaseModel):
    pass


class EndpointInterfaceUrlString69Parse(BaseModel):
    pass


class EndpointInterfaceUrlString6DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString6Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString6Merge(BaseModel):
    pass


class EndpointInterfaceUrlString6Parse(BaseModel):
    pass


class EndpointInterfaceUrlString7(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString7DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString7Defaults"]
    merge: Optional["EndpointInterfaceUrlString7Merge"]
    parse: Optional["EndpointInterfaceUrlString7Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString70(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString70DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString70Defaults"]
    merge: Optional["EndpointInterfaceUrlString70Merge"]
    parse: Optional["EndpointInterfaceUrlString70Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString70DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString70Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString70Merge(BaseModel):
    pass


class EndpointInterfaceUrlString70Parse(BaseModel):
    pass


class EndpointInterfaceUrlString71(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString71DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString71Defaults"]
    merge: Optional["EndpointInterfaceUrlString71Merge"]
    parse: Optional["EndpointInterfaceUrlString71Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString71DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString71Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString71Merge(BaseModel):
    pass


class EndpointInterfaceUrlString71Parse(BaseModel):
    pass


class EndpointInterfaceUrlString72(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString72DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString72Defaults"]
    merge: Optional["EndpointInterfaceUrlString72Merge"]
    parse: Optional["EndpointInterfaceUrlString72Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString72DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString72Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString72Merge(BaseModel):
    pass


class EndpointInterfaceUrlString72Parse(BaseModel):
    pass


class EndpointInterfaceUrlString73(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString73DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString73Defaults"]
    merge: Optional["EndpointInterfaceUrlString73Merge"]
    parse: Optional["EndpointInterfaceUrlString73Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString73DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString73Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString73Merge(BaseModel):
    pass


class EndpointInterfaceUrlString73Parse(BaseModel):
    pass


class EndpointInterfaceUrlString74(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString74DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString74Defaults"]
    merge: Optional["EndpointInterfaceUrlString74Merge"]
    parse: Optional["EndpointInterfaceUrlString74Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString74DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString74Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString74Merge(BaseModel):
    pass


class EndpointInterfaceUrlString74Parse(BaseModel):
    pass


class EndpointInterfaceUrlString75(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString75DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString75Defaults"]
    merge: Optional["EndpointInterfaceUrlString75Merge"]
    parse: Optional["EndpointInterfaceUrlString75Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString75DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString75Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString75Merge(BaseModel):
    pass


class EndpointInterfaceUrlString75Parse(BaseModel):
    pass


class EndpointInterfaceUrlString76(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString76DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString76Defaults"]
    merge: Optional["EndpointInterfaceUrlString76Merge"]
    parse: Optional["EndpointInterfaceUrlString76Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString76DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString76Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString76Merge(BaseModel):
    pass


class EndpointInterfaceUrlString76Parse(BaseModel):
    pass


class EndpointInterfaceUrlString77(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString77DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString77Defaults"]
    merge: Optional["EndpointInterfaceUrlString77Merge"]
    parse: Optional["EndpointInterfaceUrlString77Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString77DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString77Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString77Merge(BaseModel):
    pass


class EndpointInterfaceUrlString77Parse(BaseModel):
    pass


class EndpointInterfaceUrlString78(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString78DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString78Defaults"]
    merge: Optional["EndpointInterfaceUrlString78Merge"]
    parse: Optional["EndpointInterfaceUrlString78Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString78DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString78Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString78Merge(BaseModel):
    pass


class EndpointInterfaceUrlString78Parse(BaseModel):
    pass


class EndpointInterfaceUrlString79(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString79DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString79Defaults"]
    merge: Optional["EndpointInterfaceUrlString79Merge"]
    parse: Optional["EndpointInterfaceUrlString79Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString79DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString79Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString79Merge(BaseModel):
    pass


class EndpointInterfaceUrlString79Parse(BaseModel):
    pass


class EndpointInterfaceUrlString7DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString7Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString7Merge(BaseModel):
    pass


class EndpointInterfaceUrlString7Parse(BaseModel):
    pass


class EndpointInterfaceUrlString8(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString8DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString8Defaults"]
    merge: Optional["EndpointInterfaceUrlString8Merge"]
    parse: Optional["EndpointInterfaceUrlString8Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString80(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString80DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString80Defaults"]
    merge: Optional["EndpointInterfaceUrlString80Merge"]
    parse: Optional["EndpointInterfaceUrlString80Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString80DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString80Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString80Merge(BaseModel):
    pass


class EndpointInterfaceUrlString80Parse(BaseModel):
    pass


class EndpointInterfaceUrlString81(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString81DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString81Defaults"]
    merge: Optional["EndpointInterfaceUrlString81Merge"]
    parse: Optional["EndpointInterfaceUrlString81Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString81DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString81Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString81Merge(BaseModel):
    pass


class EndpointInterfaceUrlString81Parse(BaseModel):
    pass


class EndpointInterfaceUrlString82(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString82DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString82Defaults"]
    merge: Optional["EndpointInterfaceUrlString82Merge"]
    parse: Optional["EndpointInterfaceUrlString82Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString82DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString82Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString82Merge(BaseModel):
    pass


class EndpointInterfaceUrlString82Parse(BaseModel):
    pass


class EndpointInterfaceUrlString83(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString83DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString83Defaults"]
    merge: Optional["EndpointInterfaceUrlString83Merge"]
    parse: Optional["EndpointInterfaceUrlString83Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString83DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString83Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString83Merge(BaseModel):
    pass


class EndpointInterfaceUrlString83Parse(BaseModel):
    pass


class EndpointInterfaceUrlString84(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString84DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString84Defaults"]
    merge: Optional["EndpointInterfaceUrlString84Merge"]
    parse: Optional["EndpointInterfaceUrlString84Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString84DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString84Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString84Merge(BaseModel):
    pass


class EndpointInterfaceUrlString84Parse(BaseModel):
    pass


class EndpointInterfaceUrlString85(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString85DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString85Defaults"]
    merge: Optional["EndpointInterfaceUrlString85Merge"]
    parse: Optional["EndpointInterfaceUrlString85Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString85DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString85Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString85Merge(BaseModel):
    pass


class EndpointInterfaceUrlString85Parse(BaseModel):
    pass


class EndpointInterfaceUrlString86(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString86DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString86Defaults"]
    merge: Optional["EndpointInterfaceUrlString86Merge"]
    parse: Optional["EndpointInterfaceUrlString86Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString86DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString86Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString86Merge(BaseModel):
    pass


class EndpointInterfaceUrlString86Parse(BaseModel):
    pass


class EndpointInterfaceUrlString87(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString87DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString87Defaults"]
    merge: Optional["EndpointInterfaceUrlString87Merge"]
    parse: Optional["EndpointInterfaceUrlString87Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString87DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString87Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString87Merge(BaseModel):
    pass


class EndpointInterfaceUrlString87Parse(BaseModel):
    pass


class EndpointInterfaceUrlString88(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString88DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString88Defaults"]
    merge: Optional["EndpointInterfaceUrlString88Merge"]
    parse: Optional["EndpointInterfaceUrlString88Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString88DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString88Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString88Merge(BaseModel):
    pass


class EndpointInterfaceUrlString88Parse(BaseModel):
    pass


class EndpointInterfaceUrlString89(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString89DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString89Defaults"]
    merge: Optional["EndpointInterfaceUrlString89Merge"]
    parse: Optional["EndpointInterfaceUrlString89Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString89DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString89Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString89Merge(BaseModel):
    pass


class EndpointInterfaceUrlString89Parse(BaseModel):
    pass


class EndpointInterfaceUrlString8DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString8Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString8Merge(BaseModel):
    pass


class EndpointInterfaceUrlString8Parse(BaseModel):
    pass


class EndpointInterfaceUrlString9(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString9DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString9Defaults"]
    merge: Optional["EndpointInterfaceUrlString9Merge"]
    parse: Optional["EndpointInterfaceUrlString9Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString90(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString90DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString90Defaults"]
    merge: Optional["EndpointInterfaceUrlString90Merge"]
    parse: Optional["EndpointInterfaceUrlString90Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString90DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString90Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString90Merge(BaseModel):
    pass


class EndpointInterfaceUrlString90Parse(BaseModel):
    pass


class EndpointInterfaceUrlString91(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString91DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString91Defaults"]
    merge: Optional["EndpointInterfaceUrlString91Merge"]
    parse: Optional["EndpointInterfaceUrlString91Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString91DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString91Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString91Merge(BaseModel):
    pass


class EndpointInterfaceUrlString91Parse(BaseModel):
    pass


class EndpointInterfaceUrlString92(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString92DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString92Defaults"]
    merge: Optional["EndpointInterfaceUrlString92Merge"]
    parse: Optional["EndpointInterfaceUrlString92Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString92DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString92Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString92Merge(BaseModel):
    pass


class EndpointInterfaceUrlString92Parse(BaseModel):
    pass


class EndpointInterfaceUrlString93(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString93DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString93Defaults"]
    merge: Optional["EndpointInterfaceUrlString93Merge"]
    parse: Optional["EndpointInterfaceUrlString93Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString93DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString93Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString93Merge(BaseModel):
    pass


class EndpointInterfaceUrlString93Parse(BaseModel):
    pass


class EndpointInterfaceUrlString94(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString94DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString94Defaults"]
    merge: Optional["EndpointInterfaceUrlString94Merge"]
    parse: Optional["EndpointInterfaceUrlString94Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString94DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString94Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString94Merge(BaseModel):
    pass


class EndpointInterfaceUrlString94Parse(BaseModel):
    pass


class EndpointInterfaceUrlString95(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString95DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString95Defaults"]
    merge: Optional["EndpointInterfaceUrlString95Merge"]
    parse: Optional["EndpointInterfaceUrlString95Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString95DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString95Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString95Merge(BaseModel):
    pass


class EndpointInterfaceUrlString95Parse(BaseModel):
    pass


class EndpointInterfaceUrlString96(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString96DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString96Defaults"]
    merge: Optional["EndpointInterfaceUrlString96Merge"]
    parse: Optional["EndpointInterfaceUrlString96Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString96DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString96Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString96Merge(BaseModel):
    pass


class EndpointInterfaceUrlString96Parse(BaseModel):
    pass


class EndpointInterfaceUrlString97(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString97DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString97Defaults"]
    merge: Optional["EndpointInterfaceUrlString97Merge"]
    parse: Optional["EndpointInterfaceUrlString97Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString97DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString97Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString97Merge(BaseModel):
    pass


class EndpointInterfaceUrlString97Parse(BaseModel):
    pass


class EndpointInterfaceUrlString98(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString98DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString98Defaults"]
    merge: Optional["EndpointInterfaceUrlString98Merge"]
    parse: Optional["EndpointInterfaceUrlString98Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString98DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString98Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString98Merge(BaseModel):
    pass


class EndpointInterfaceUrlString98Parse(BaseModel):
    pass


class EndpointInterfaceUrlString99(BaseModel):
    defaults: Optional["EndpointInterfaceUrlString99DEFAULTS"]
    defaults: Optional["EndpointInterfaceUrlString99Defaults"]
    merge: Optional["EndpointInterfaceUrlString99Merge"]
    parse: Optional["EndpointInterfaceUrlString99Parse"]

    class Config:
        fields = {
            "defaults": "DEFAULTS",
            "defaults": "defaults",
            "merge": "merge",
            "parse": "parse",
        }


class EndpointInterfaceUrlString99DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString99Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString99Merge(BaseModel):
    pass


class EndpointInterfaceUrlString99Parse(BaseModel):
    pass


class EndpointInterfaceUrlString9DEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlString9Defaults(BaseModel):
    pass


class EndpointInterfaceUrlString9Merge(BaseModel):
    pass


class EndpointInterfaceUrlString9Parse(BaseModel):
    pass


class EndpointInterfaceUrlStringDEFAULTS(BaseModel):
    url: Optional[str]

    class Config:
        fields = {
            "url": "url",
        }


class EndpointInterfaceUrlStringDefaults(BaseModel):
    pass


class EndpointInterfaceUrlStringMerge(BaseModel):
    pass


class EndpointInterfaceUrlStringParse(BaseModel):
    pass


class Environments(BaseModel):
    camelize: Optional[bool]
    headers: Optional["EnvironmentsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class EnvironmentsHeaders(BaseModel):
    pass


class EpicDiscussions(BaseModel):
    camelize: Optional[bool]
    headers: Optional["EpicDiscussionsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class EpicDiscussionsHeaders(BaseModel):
    pass


class EpicIssues(BaseModel):
    camelize: Optional[bool]
    headers: Optional["EpicIssuesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class EpicIssuesHeaders(BaseModel):
    pass


class EpicNotes(BaseModel):
    camelize: Optional[bool]
    headers: Optional["EpicNotesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class EpicNotesHeaders(BaseModel):
    pass


class Epics(BaseModel):
    camelize: Optional[bool]
    headers: Optional["EpicsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class EpicsHeaders(BaseModel):
    pass


class Events(BaseModel):
    camelize: Optional[bool]
    headers: Optional["EventsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class EventsHeaders(BaseModel):
    pass


class FeatureFlags(BaseModel):
    camelize: Optional[bool]
    headers: Optional["FeatureFlagsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class FeatureFlagsHeaders(BaseModel):
    pass


class GeoNodes(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GeoNodesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GeoNodesHeaders(BaseModel):
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
    set_summary_markdown: Optional["GitHubDSLSetSummaryMarkdown"]
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
            "set_summary_markdown": "setSummaryMarkdown",
            "this_pr": "thisPR",
            "utils": "utils",
        }


class GitHubDSLSetSummaryMarkdown(BaseModel):
    pass


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
    draft: Optional[bool]
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
            "draft": "draft",
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
    COMMENT = "COMMENT"
    PENDING = "PENDING"
    REQUEST_CHANGES = "REQUEST_CHANGES"


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


class GitLabApproval(BaseModel):
    approvals_left: Optional[int]
    approvals_required: Optional[int]
    approved_by: Any
    created_at: Optional[str]
    description: Optional[str]
    id: Optional[int]
    iid: Optional[int]
    merge_status: Optional["GitLabApprovalMergeStatus"]
    project_id: Optional[int]
    state: Optional["GitLabApprovalState"]
    title: Optional[str]
    updated_at: Optional[str]

    class Config:
        fields = {
            "approvals_left": "approvals_left",
            "approvals_required": "approvals_required",
            "approved_by": "approved_by",
            "created_at": "created_at",
            "description": "description",
            "id": "id",
            "iid": "iid",
            "merge_status": "merge_status",
            "project_id": "project_id",
            "state": "state",
            "title": "title",
            "updated_at": "updated_at",
        }


class GitLabApprovalMergeStatus(Enum):
    CAN_BE_MERGED = "can_be_merged"


class GitLabApprovalState(Enum):
    CLOSED = "closed"
    LOCKED = "locked"
    MERGED = "merged"
    OPEN = "open"


class GitLabCIYMLTemplates(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GitLabCIYMLTemplatesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GitLabCIYMLTemplatesHeaders(BaseModel):
    pass


class GitLabDSL(BaseModel):
    api: Optional[
        "MapperTypeofimportUsersOrtatheroxDevDangerDangerJsNodeModulesGitbeakerCoreDistTypesServicesIndexUsersUserCustomAttributesUserEmailsUserImpersonationTokensUserKeysUserGPGKeysGroupsGroupAccessRequestsGroupBadgesGroupCustomAttributesGroupIssueBoardsGroupMembersGroupMilestonesGroupProjectsGroupVariablesGroupLabelsGroupDeployTokensEpicsEpicIssuesEpicNotesEpicDiscussionsBranchesCommitsCommitDiscussionsContainerRegistryDeployKeysDeploymentsEnvironmentsIssuesIssuesStatisticsIssueAwardEmojisIssueNotesIssueDiscussionsJobsLabelsMergeRequestsMergeRequestAwardEmojisMergeRequestDiscussionsMergeRequestNotesPackagesPipelinesPipelineSchedulesPipelineScheduleVariablesProjectsProjectAccessRequestsProjectBadgesProjectCustomAttributesProjectImportExportProjectIssueBoardsProjectHooksProjectMembersProjectMilestonesProjectSnippetsProjectSnippetNotesProjectSnippetDiscussionsProjectSnippetAwardEmojisProtectedBranchesProtectedTagsProjectVariablesProjectDeployTokensPushRulesReleasesReleaseLinksRepositoriesRepositoryFilesRunnersServicesTagsTodosTriggersVulnerabilityFindingsApplicationSettingsBroadcastMessagesEventsFeatureFlagsGeoNodesGitignoreTemplatesGitLabCIYMLTemplatesKeysLicenseLicenceTemplatesLintNamespacesNotificationSettingsMarkdownPagesDomainsSearchSidekiqMetricsSnippetsSystemHooksVersionWikis"
    ]
    approvals: Optional["GitLabApproval"]
    commits: Optional[List["GitLabMRCommit"]]
    metadata: Optional["RepoMetaData"]
    mr: Optional["GitLabMR"]
    utils: Optional["GitLabDSLUtils"]

    class Config:
        fields = {
            "api": "api",
            "approvals": "approvals",
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
    assignees: Optional[List["GitLabUser"]]
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
    reviewers: Optional[List["GitLabUser"]]
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
            "assignees": "assignees",
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
            "reviewers": "reviewers",
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
    UNCHECKED = "unchecked"
    CANNOT_BE_MERGED_RECHECK = "cannot_be_merged_recheck"
    CHECKING = "checking"
    CANNOT_BE_MERGED_RECHECKING = "cannot_be_merged_rechecking"
    CAN_BE_MERGED = "can_be_merged"
    CANNOT_BE_MERGED = "cannot_be_merged"


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


class GitignoreTemplates(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GitignoreTemplatesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GitignoreTemplatesHeaders(BaseModel):
    pass


class Graphql(BaseModel):
    defaults: Optional["GraphqlDefaults"]
    endpoint: Optional["EndpointInterfaceObject"]

    class Config:
        fields = {
            "defaults": "defaults",
            "endpoint": "endpoint",
        }


class GraphqlDefaults(BaseModel):
    pass


class GroupAccessRequests(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupAccessRequestsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupAccessRequestsHeaders(BaseModel):
    pass


class GroupBadges(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupBadgesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupBadgesHeaders(BaseModel):
    pass


class GroupCustomAttributes(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupCustomAttributesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupCustomAttributesHeaders(BaseModel):
    pass


class GroupDeployTokens(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupDeployTokensHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupDeployTokensHeaders(BaseModel):
    pass


class GroupIssueBoards(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupIssueBoardsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupIssueBoardsHeaders(BaseModel):
    pass


class GroupLabels(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupLabelsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupLabelsHeaders(BaseModel):
    pass


class GroupMembers(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupMembersHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupMembersHeaders(BaseModel):
    pass


class GroupMilestones(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupMilestonesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupMilestonesHeaders(BaseModel):
    pass


class GroupProjects(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupProjectsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupProjectsHeaders(BaseModel):
    pass


class GroupVariables(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupVariablesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupVariablesHeaders(BaseModel):
    pass


class Groups(BaseModel):
    camelize: Optional[bool]
    headers: Optional["GroupsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class GroupsHeaders(BaseModel):
    pass


class HookCollectionHooksKeyofHooks(BaseModel):
    api: Optional["PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemove"]

    class Config:
        fields = {
            "api": "api",
        }


class IssueAwardEmojis(BaseModel):
    camelize: Optional[bool]
    headers: Optional["IssueAwardEmojisHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource_type": "resourceType",
            "url": "url",
        }


class IssueAwardEmojisHeaders(BaseModel):
    pass


class IssueDiscussions(BaseModel):
    camelize: Optional[bool]
    headers: Optional["IssueDiscussionsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class IssueDiscussionsHeaders(BaseModel):
    pass


class IssueNotes(BaseModel):
    camelize: Optional[bool]
    headers: Optional["IssueNotesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class IssueNotesHeaders(BaseModel):
    pass


class Issues(BaseModel):
    camelize: Optional[bool]
    headers: Optional["IssuesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class IssuesHeaders(BaseModel):
    pass


class IssuesStatistics(BaseModel):
    camelize: Optional[bool]
    headers: Optional["IssuesStatisticsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class IssuesStatisticsHeaders(BaseModel):
    pass


class JIRAIssue(BaseModel):
    key: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "key": "key",
            "url": "url",
        }


class Jobs(BaseModel):
    camelize: Optional[bool]
    headers: Optional["JobsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class JobsHeaders(BaseModel):
    pass


class Keys(BaseModel):
    camelize: Optional[bool]
    headers: Optional["KeysHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class KeysHeaders(BaseModel):
    pass


class Labels(BaseModel):
    camelize: Optional[bool]
    headers: Optional["LabelsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class LabelsHeaders(BaseModel):
    pass


class LicenceTemplates(BaseModel):
    camelize: Optional[bool]
    headers: Optional["LicenceTemplatesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class LicenceTemplatesHeaders(BaseModel):
    pass


class License(BaseModel):
    camelize: Optional[bool]
    headers: Optional["LicenseHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class LicenseHeaders(BaseModel):
    pass


class Lint(BaseModel):
    camelize: Optional[bool]
    headers: Optional["LintHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class LintHeaders(BaseModel):
    pass


class MapperTypeofimportUsersOrtatheroxDevDangerDangerJsNodeModulesGitbeakerCoreDistTypesServicesIndexUsersUserCustomAttributesUserEmailsUserImpersonationTokensUserKeysUserGPGKeysGroupsGroupAccessRequestsGroupBadgesGroupCustomAttributesGroupIssueBoardsGroupMembersGroupMilestonesGroupProjectsGroupVariablesGroupLabelsGroupDeployTokensEpicsEpicIssuesEpicNotesEpicDiscussionsBranchesCommitsCommitDiscussionsContainerRegistryDeployKeysDeploymentsEnvironmentsIssuesIssuesStatisticsIssueAwardEmojisIssueNotesIssueDiscussionsJobsLabelsMergeRequestsMergeRequestAwardEmojisMergeRequestDiscussionsMergeRequestNotesPackagesPipelinesPipelineSchedulesPipelineScheduleVariablesProjectsProjectAccessRequestsProjectBadgesProjectCustomAttributesProjectImportExportProjectIssueBoardsProjectHooksProjectMembersProjectMilestonesProjectSnippetsProjectSnippetNotesProjectSnippetDiscussionsProjectSnippetAwardEmojisProtectedBranchesProtectedTagsProjectVariablesProjectDeployTokensPushRulesReleasesReleaseLinksRepositoriesRepositoryFilesRunnersServicesTagsTodosTriggersVulnerabilityFindingsApplicationSettingsBroadcastMessagesEventsFeatureFlagsGeoNodesGitignoreTemplatesGitLabCIYMLTemplatesKeysLicenseLicenceTemplatesLintNamespacesNotificationSettingsMarkdownPagesDomainsSearchSidekiqMetricsSnippetsSystemHooksVersionWikis(
    BaseModel
):
    application_settings: Optional["ApplicationSettings"]
    branches: Optional["Branches"]
    broadcast_messages: Optional["BroadcastMessages"]
    commit_discussions: Optional["CommitDiscussions"]
    commits: Optional["Commits"]
    container_registry: Optional["ContainerRegistry"]
    deploy_keys: Optional["DeployKeys"]
    deployments: Optional["Deployments"]
    environments: Optional["Environments"]
    epic_discussions: Optional["EpicDiscussions"]
    epic_issues: Optional["EpicIssues"]
    epic_notes: Optional["EpicNotes"]
    epics: Optional["Epics"]
    events: Optional["Events"]
    feature_flags: Optional["FeatureFlags"]
    geo_nodes: Optional["GeoNodes"]
    git_lab_c_i_y_m_l_templates: Optional["GitLabCIYMLTemplates"]
    gitignore_templates: Optional["GitignoreTemplates"]
    group_access_requests: Optional["GroupAccessRequests"]
    group_badges: Optional["GroupBadges"]
    group_custom_attributes: Optional["GroupCustomAttributes"]
    group_deploy_tokens: Optional["GroupDeployTokens"]
    group_issue_boards: Optional["GroupIssueBoards"]
    group_labels: Optional["GroupLabels"]
    group_members: Optional["GroupMembers"]
    group_milestones: Optional["GroupMilestones"]
    group_projects: Optional["GroupProjects"]
    group_variables: Optional["GroupVariables"]
    groups: Optional["Groups"]
    issue_award_emojis: Optional["IssueAwardEmojis"]
    issue_discussions: Optional["IssueDiscussions"]
    issue_notes: Optional["IssueNotes"]
    issues: Optional["Issues"]
    issues_statistics: Optional["IssuesStatistics"]
    jobs: Optional["Jobs"]
    keys: Optional["Keys"]
    labels: Optional["Labels"]
    licence_templates: Optional["LicenceTemplates"]
    license: Optional["License"]
    lint: Optional["Lint"]
    markdown: Optional["Markdown"]
    merge_request_award_emojis: Optional["MergeRequestAwardEmojis"]
    merge_request_discussions: Optional["MergeRequestDiscussions"]
    merge_request_notes: Optional["MergeRequestNotes"]
    merge_requests: Optional["MergeRequests"]
    namespaces: Optional["Namespaces"]
    notification_settings: Optional["NotificationSettings"]
    packages: Optional["Packages"]
    pages_domains: Optional["PagesDomains"]
    pipeline_schedule_variables: Optional["PipelineScheduleVariables"]
    pipeline_schedules: Optional["PipelineSchedules"]
    pipelines: Optional["Pipelines"]
    project_access_requests: Optional["ProjectAccessRequests"]
    project_badges: Optional["ProjectBadges"]
    project_custom_attributes: Optional["ProjectCustomAttributes"]
    project_deploy_tokens: Optional["ProjectDeployTokens"]
    project_hooks: Optional["ProjectHooks"]
    project_import_export: Optional["ProjectImportExport"]
    project_issue_boards: Optional["ProjectIssueBoards"]
    project_members: Optional["ProjectMembers"]
    project_milestones: Optional["ProjectMilestones"]
    project_snippet_award_emojis: Optional["ProjectSnippetAwardEmojis"]
    project_snippet_discussions: Optional["ProjectSnippetDiscussions"]
    project_snippet_notes: Optional["ProjectSnippetNotes"]
    project_snippets: Optional["ProjectSnippets"]
    project_variables: Optional["ProjectVariables"]
    projects: Optional["Projects"]
    protected_branches: Optional["ProtectedBranches"]
    protected_tags: Optional["ProtectedTags"]
    push_rules: Optional["PushRules"]
    release_links: Optional["ReleaseLinks"]
    releases: Optional["Releases"]
    repositories: Optional["Repositories"]
    repository_files: Optional["RepositoryFiles"]
    runners: Optional["Runners"]
    search: Optional["Search"]
    services: Optional["Services"]
    sidekiq_metrics: Optional["SidekiqMetrics"]
    snippets: Optional["Snippets"]
    system_hooks: Optional["SystemHooks"]
    tags: Optional["Tags"]
    todos: Optional["Todos"]
    triggers: Optional["Triggers"]
    user_custom_attributes: Optional["UserCustomAttributes"]
    user_emails: Optional["UserEmails"]
    user_g_p_g_keys: Optional["UserGPGKeys"]
    user_impersonation_tokens: Optional["UserImpersonationTokens"]
    user_keys: Optional["UserKeys"]
    users: Optional["Users"]
    version: Optional["Version"]
    vulnerability_findings: Optional["VulnerabilityFindings"]
    wikis: Optional["Wikis"]

    class Config:
        fields = {
            "application_settings": "ApplicationSettings",
            "branches": "Branches",
            "broadcast_messages": "BroadcastMessages",
            "commit_discussions": "CommitDiscussions",
            "commits": "Commits",
            "container_registry": "ContainerRegistry",
            "deploy_keys": "DeployKeys",
            "deployments": "Deployments",
            "environments": "Environments",
            "epic_discussions": "EpicDiscussions",
            "epic_issues": "EpicIssues",
            "epic_notes": "EpicNotes",
            "epics": "Epics",
            "events": "Events",
            "feature_flags": "FeatureFlags",
            "geo_nodes": "GeoNodes",
            "git_lab_c_i_y_m_l_templates": "GitLabCIYMLTemplates",
            "gitignore_templates": "GitignoreTemplates",
            "group_access_requests": "GroupAccessRequests",
            "group_badges": "GroupBadges",
            "group_custom_attributes": "GroupCustomAttributes",
            "group_deploy_tokens": "GroupDeployTokens",
            "group_issue_boards": "GroupIssueBoards",
            "group_labels": "GroupLabels",
            "group_members": "GroupMembers",
            "group_milestones": "GroupMilestones",
            "group_projects": "GroupProjects",
            "group_variables": "GroupVariables",
            "groups": "Groups",
            "issue_award_emojis": "IssueAwardEmojis",
            "issue_discussions": "IssueDiscussions",
            "issue_notes": "IssueNotes",
            "issues": "Issues",
            "issues_statistics": "IssuesStatistics",
            "jobs": "Jobs",
            "keys": "Keys",
            "labels": "Labels",
            "licence_templates": "LicenceTemplates",
            "license": "License",
            "lint": "Lint",
            "markdown": "Markdown",
            "merge_request_award_emojis": "MergeRequestAwardEmojis",
            "merge_request_discussions": "MergeRequestDiscussions",
            "merge_request_notes": "MergeRequestNotes",
            "merge_requests": "MergeRequests",
            "namespaces": "Namespaces",
            "notification_settings": "NotificationSettings",
            "packages": "Packages",
            "pages_domains": "PagesDomains",
            "pipeline_schedule_variables": "PipelineScheduleVariables",
            "pipeline_schedules": "PipelineSchedules",
            "pipelines": "Pipelines",
            "project_access_requests": "ProjectAccessRequests",
            "project_badges": "ProjectBadges",
            "project_custom_attributes": "ProjectCustomAttributes",
            "project_deploy_tokens": "ProjectDeployTokens",
            "project_hooks": "ProjectHooks",
            "project_import_export": "ProjectImportExport",
            "project_issue_boards": "ProjectIssueBoards",
            "project_members": "ProjectMembers",
            "project_milestones": "ProjectMilestones",
            "project_snippet_award_emojis": "ProjectSnippetAwardEmojis",
            "project_snippet_discussions": "ProjectSnippetDiscussions",
            "project_snippet_notes": "ProjectSnippetNotes",
            "project_snippets": "ProjectSnippets",
            "project_variables": "ProjectVariables",
            "projects": "Projects",
            "protected_branches": "ProtectedBranches",
            "protected_tags": "ProtectedTags",
            "push_rules": "PushRules",
            "release_links": "ReleaseLinks",
            "releases": "Releases",
            "repositories": "Repositories",
            "repository_files": "RepositoryFiles",
            "runners": "Runners",
            "search": "Search",
            "services": "Services",
            "sidekiq_metrics": "SidekiqMetrics",
            "snippets": "Snippets",
            "system_hooks": "SystemHooks",
            "tags": "Tags",
            "todos": "Todos",
            "triggers": "Triggers",
            "user_custom_attributes": "UserCustomAttributes",
            "user_emails": "UserEmails",
            "user_g_p_g_keys": "UserGPGKeys",
            "user_impersonation_tokens": "UserImpersonationTokens",
            "user_keys": "UserKeys",
            "users": "Users",
            "version": "Version",
            "vulnerability_findings": "VulnerabilityFindings",
            "wikis": "Wikis",
        }


class Markdown(BaseModel):
    camelize: Optional[bool]
    headers: Optional["MarkdownHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class MarkdownHeaders(BaseModel):
    pass


class MergeRequestAwardEmojis(BaseModel):
    camelize: Optional[bool]
    headers: Optional["MergeRequestAwardEmojisHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource_type": "resourceType",
            "url": "url",
        }


class MergeRequestAwardEmojisHeaders(BaseModel):
    pass


class MergeRequestDiscussions(BaseModel):
    camelize: Optional[bool]
    headers: Optional["MergeRequestDiscussionsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class MergeRequestDiscussionsHeaders(BaseModel):
    pass


class MergeRequestNotes(BaseModel):
    camelize: Optional[bool]
    headers: Optional["MergeRequestNotesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class MergeRequestNotesHeaders(BaseModel):
    pass


class MergeRequests(BaseModel):
    camelize: Optional[bool]
    headers: Optional["MergeRequestsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class MergeRequestsHeaders(BaseModel):
    pass


class Namespaces(BaseModel):
    camelize: Optional[bool]
    headers: Optional["NamespacesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class NamespacesHeaders(BaseModel):
    pass


class NotificationSettings(BaseModel):
    camelize: Optional[bool]
    headers: Optional["NotificationSettingsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class NotificationSettingsHeaders(BaseModel):
    pass


class Octokit(BaseModel):
    auth: Optional["OctokitAuth"]
    graphql: Optional["Graphql"]
    hook: Optional["HookCollectionHooksKeyofHooks"]
    log: Optional["OctokitLog"]
    request: Optional["RequestInterfaceObject"]

    class Config:
        fields = {
            "auth": "auth",
            "graphql": "graphql",
            "hook": "hook",
            "log": "log",
            "request": "request",
        }


class OctokitAuth(BaseModel):
    pass


class OctokitLog(BaseModel):
    debug: Optional["OctokitLogDebug"]
    error: Optional["OctokitLogError"]
    info: Optional["OctokitLogInfo"]
    warn: Optional["OctokitLogWarn"]

    class Config:
        fields = {
            "debug": "debug",
            "error": "error",
            "info": "info",
            "warn": "warn",
        }


class OctokitLogDebug(BaseModel):
    pass


class OctokitLogError(BaseModel):
    pass


class OctokitLogInfo(BaseModel):
    pass


class OctokitLogWarn(BaseModel):
    pass


class Packages(BaseModel):
    camelize: Optional[bool]
    headers: Optional["PackagesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class PackagesHeaders(BaseModel):
    pass


class PagesDomains(BaseModel):
    camelize: Optional[bool]
    headers: Optional["PagesDomainsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class PagesDomainsHeaders(BaseModel):
    pass


class PaginateInterface(BaseModel):
    iterator: Optional["PaginateInterfaceIterator"]

    class Config:
        fields = {
            "iterator": "iterator",
        }


class PaginateInterfaceIterator(BaseModel):
    pass


class PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemove(BaseModel):
    after: Optional["PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveAfter"]
    before: Optional[
        "PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveBefore"
    ]
    error: Optional["PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveError"]
    remove: Optional[
        "PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveRemove"
    ]
    wrap: Optional["PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveWrap"]

    class Config:
        fields = {
            "after": "after",
            "before": "before",
            "error": "error",
            "remove": "remove",
            "wrap": "wrap",
        }


class PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveAfter(BaseModel):
    pass


class PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveBefore(BaseModel):
    pass


class PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveError(BaseModel):
    pass


class PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveRemove(BaseModel):
    pass


class PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveWrap(BaseModel):
    pass


class PipelineScheduleVariables(BaseModel):
    camelize: Optional[bool]
    headers: Optional["PipelineScheduleVariablesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class PipelineScheduleVariablesHeaders(BaseModel):
    pass


class PipelineSchedules(BaseModel):
    camelize: Optional[bool]
    headers: Optional["PipelineSchedulesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class PipelineSchedulesHeaders(BaseModel):
    pass


class Pipelines(BaseModel):
    camelize: Optional[bool]
    headers: Optional["PipelinesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class PipelinesHeaders(BaseModel):
    pass


class ProjectAccessRequests(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectAccessRequestsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectAccessRequestsHeaders(BaseModel):
    pass


class ProjectBadges(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectBadgesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectBadgesHeaders(BaseModel):
    pass


class ProjectCustomAttributes(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectCustomAttributesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectCustomAttributesHeaders(BaseModel):
    pass


class ProjectDeployTokens(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectDeployTokensHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectDeployTokensHeaders(BaseModel):
    pass


class ProjectHooks(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectHooksHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectHooksHeaders(BaseModel):
    pass


class ProjectImportExport(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectImportExportHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectImportExportHeaders(BaseModel):
    pass


class ProjectIssueBoards(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectIssueBoardsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectIssueBoardsHeaders(BaseModel):
    pass


class ProjectMembers(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectMembersHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectMembersHeaders(BaseModel):
    pass


class ProjectMilestones(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectMilestonesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectMilestonesHeaders(BaseModel):
    pass


class ProjectSnippetAwardEmojis(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectSnippetAwardEmojisHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource_type": "resourceType",
            "url": "url",
        }


class ProjectSnippetAwardEmojisHeaders(BaseModel):
    pass


class ProjectSnippetDiscussions(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectSnippetDiscussionsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class ProjectSnippetDiscussionsHeaders(BaseModel):
    pass


class ProjectSnippetNotes(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectSnippetNotesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    resource2_type: Optional[str]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "resource2_type": "resource2Type",
            "url": "url",
        }


class ProjectSnippetNotesHeaders(BaseModel):
    pass


class ProjectSnippets(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectSnippetsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectSnippetsHeaders(BaseModel):
    pass


class ProjectVariables(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectVariablesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectVariablesHeaders(BaseModel):
    pass


class Projects(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProjectsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProjectsHeaders(BaseModel):
    pass


class ProtectedBranches(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProtectedBranchesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProtectedBranchesHeaders(BaseModel):
    pass


class ProtectedTags(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ProtectedTagsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ProtectedTagsHeaders(BaseModel):
    pass


class PushRules(BaseModel):
    camelize: Optional[bool]
    headers: Optional["PushRulesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class PushRulesHeaders(BaseModel):
    pass


class ReleaseLinks(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ReleaseLinksHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ReleaseLinksHeaders(BaseModel):
    pass


class Releases(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ReleasesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ReleasesHeaders(BaseModel):
    pass


class RepoMetaData(BaseModel):
    pull_request_id: Optional[str]
    repo_slug: Optional[str]

    class Config:
        fields = {
            "pull_request_id": "pullRequestID",
            "repo_slug": "repoSlug",
        }


class Repositories(BaseModel):
    camelize: Optional[bool]
    headers: Optional["RepositoriesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class RepositoriesHeaders(BaseModel):
    pass


class RepositoryFiles(BaseModel):
    camelize: Optional[bool]
    headers: Optional["RepositoryFilesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class RepositoryFilesHeaders(BaseModel):
    pass


class RequestInterfaceObject(BaseModel):
    defaults: Optional["RequestInterfaceObjectDefaults"]
    endpoint: Optional["EndpointInterfaceObject"]

    class Config:
        fields = {
            "defaults": "defaults",
            "endpoint": "endpoint",
        }


class RequestInterfaceObjectDefaults(BaseModel):
    pass


class RequestMethod(Enum):
    DELETE = "DELETE"
    GET = "GET"
    HEAD = "HEAD"
    PATCH = "PATCH"
    POST = "POST"
    PUT = "PUT"


class RequesterType(BaseModel):
    pass


class Runners(BaseModel):
    camelize: Optional[bool]
    headers: Optional["RunnersHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class RunnersHeaders(BaseModel):
    pass


class Search(BaseModel):
    camelize: Optional[bool]
    headers: Optional["SearchHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class SearchHeaders(BaseModel):
    pass


class Services(BaseModel):
    camelize: Optional[bool]
    headers: Optional["ServicesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class ServicesHeaders(BaseModel):
    pass


class SidekiqMetrics(BaseModel):
    camelize: Optional[bool]
    headers: Optional["SidekiqMetricsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class SidekiqMetricsHeaders(BaseModel):
    pass


class Snippets(BaseModel):
    camelize: Optional[bool]
    headers: Optional["SnippetsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class SnippetsHeaders(BaseModel):
    pass


class SystemHooks(BaseModel):
    camelize: Optional[bool]
    headers: Optional["SystemHooksHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class SystemHooksHeaders(BaseModel):
    pass


class Tags(BaseModel):
    camelize: Optional[bool]
    headers: Optional["TagsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class TagsHeaders(BaseModel):
    pass


class Todos(BaseModel):
    camelize: Optional[bool]
    headers: Optional["TodosHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class TodosHeaders(BaseModel):
    pass


class Triggers(BaseModel):
    camelize: Optional[bool]
    headers: Optional["TriggersHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class TriggersHeaders(BaseModel):
    pass


class UserCustomAttributes(BaseModel):
    camelize: Optional[bool]
    headers: Optional["UserCustomAttributesHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class UserCustomAttributesHeaders(BaseModel):
    pass


class UserEmails(BaseModel):
    camelize: Optional[bool]
    headers: Optional["UserEmailsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class UserEmailsHeaders(BaseModel):
    pass


class UserGPGKeys(BaseModel):
    camelize: Optional[bool]
    headers: Optional["UserGPGKeysHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class UserGPGKeysHeaders(BaseModel):
    pass


class UserImpersonationTokens(BaseModel):
    camelize: Optional[bool]
    headers: Optional["UserImpersonationTokensHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class UserImpersonationTokensHeaders(BaseModel):
    pass


class UserKeys(BaseModel):
    camelize: Optional[bool]
    headers: Optional["UserKeysHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class UserKeysHeaders(BaseModel):
    pass


class Users(BaseModel):
    camelize: Optional[bool]
    headers: Optional["UsersHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class UsersHeaders(BaseModel):
    pass


class Version(BaseModel):
    camelize: Optional[bool]
    headers: Optional["VersionHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class VersionHeaders(BaseModel):
    pass


class VulnerabilityFindings(BaseModel):
    camelize: Optional[bool]
    headers: Optional["VulnerabilityFindingsHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class VulnerabilityFindingsHeaders(BaseModel):
    pass


class Wikis(BaseModel):
    camelize: Optional[bool]
    headers: Optional["WikisHeaders"]
    reject_unauthorized: Optional[bool]
    request_timeout: Optional[int]
    requester: Optional["RequesterType"]
    url: Optional[str]

    class Config:
        fields = {
            "camelize": "camelize",
            "headers": "headers",
            "reject_unauthorized": "rejectUnauthorized",
            "request_timeout": "requestTimeout",
            "requester": "requester",
            "url": "url",
        }


class WikisHeaders(BaseModel):
    pass


ApplicationSettings.update_forward_refs()

ApplicationSettingsHeaders.update_forward_refs()

BitBucketCloudCommit.update_forward_refs()

BitBucketCloudCommitAuthor.update_forward_refs()

BitBucketCloudCommitParents.update_forward_refs()

BitBucketCloudContent.update_forward_refs()


BitBucketCloudJSONDSL.update_forward_refs()

BitBucketCloudLinksHtml.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatuses.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesActivity.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesApprove.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesComments.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesCommits.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesDecline.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesDiff.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesHtml.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesMerge.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesSelf.update_forward_refs()

BitBucketCloudLinksHtmlActivityCommentsMergeCommitsSelfDeclineDiffApproveStatusesStatuses.update_forward_refs()

BitBucketCloudLinksHtmlHtml.update_forward_refs()

BitBucketCloudLinksHtmlSelf.update_forward_refs()

BitBucketCloudLinksHtmlSelfHtml.update_forward_refs()

BitBucketCloudLinksHtmlSelfSelf.update_forward_refs()

BitBucketCloudMergeRef.update_forward_refs()

BitBucketCloudMergeRefBranch.update_forward_refs()

BitBucketCloudMergeRefCommit.update_forward_refs()

BitBucketCloudPRActivity.update_forward_refs()

BitBucketCloudPRActivityPullRequest.update_forward_refs()

BitBucketCloudPRComment.update_forward_refs()

BitBucketCloudPRCommentInline.update_forward_refs()

BitBucketCloudPRCommentPullrequest.update_forward_refs()

BitBucketCloudPRDSL.update_forward_refs()


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


Branches.update_forward_refs()

BranchesHeaders.update_forward_refs()

BroadcastMessages.update_forward_refs()

BroadcastMessagesHeaders.update_forward_refs()

CliArgs.update_forward_refs()

CommitDiscussions.update_forward_refs()

CommitDiscussionsHeaders.update_forward_refs()

Commits.update_forward_refs()

CommitsHeaders.update_forward_refs()

ContainerRegistry.update_forward_refs()

ContainerRegistryHeaders.update_forward_refs()

DangerDSLJSONType.update_forward_refs()

DangerDSLJSONTypeSettings.update_forward_refs()

DangerDSLJSONTypeSettingsGithub.update_forward_refs()

DeployKeys.update_forward_refs()

DeployKeysHeaders.update_forward_refs()

Deployments.update_forward_refs()

DeploymentsHeaders.update_forward_refs()

EndpointInterfaceObject.update_forward_refs()

EndpointInterfaceObjectDEFAULTS.update_forward_refs()

EndpointInterfaceObjectDefaults.update_forward_refs()

EndpointInterfaceObjectMerge.update_forward_refs()

EndpointInterfaceObjectParse.update_forward_refs()

EndpointInterfaceUrlString.update_forward_refs()

EndpointInterfaceUrlString1.update_forward_refs()

EndpointInterfaceUrlString10.update_forward_refs()

EndpointInterfaceUrlString100.update_forward_refs()

EndpointInterfaceUrlString100DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString100Defaults.update_forward_refs()

EndpointInterfaceUrlString100Merge.update_forward_refs()

EndpointInterfaceUrlString100Parse.update_forward_refs()

EndpointInterfaceUrlString101.update_forward_refs()

EndpointInterfaceUrlString101DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString101Defaults.update_forward_refs()

EndpointInterfaceUrlString101Merge.update_forward_refs()

EndpointInterfaceUrlString101Parse.update_forward_refs()

EndpointInterfaceUrlString102.update_forward_refs()

EndpointInterfaceUrlString102DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString102Defaults.update_forward_refs()

EndpointInterfaceUrlString102Merge.update_forward_refs()

EndpointInterfaceUrlString102Parse.update_forward_refs()

EndpointInterfaceUrlString103.update_forward_refs()

EndpointInterfaceUrlString103DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString103Defaults.update_forward_refs()

EndpointInterfaceUrlString103Merge.update_forward_refs()

EndpointInterfaceUrlString103Parse.update_forward_refs()

EndpointInterfaceUrlString104.update_forward_refs()

EndpointInterfaceUrlString104DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString104Defaults.update_forward_refs()

EndpointInterfaceUrlString104Merge.update_forward_refs()

EndpointInterfaceUrlString104Parse.update_forward_refs()

EndpointInterfaceUrlString105.update_forward_refs()

EndpointInterfaceUrlString105DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString105Defaults.update_forward_refs()

EndpointInterfaceUrlString105Merge.update_forward_refs()

EndpointInterfaceUrlString105Parse.update_forward_refs()

EndpointInterfaceUrlString106.update_forward_refs()

EndpointInterfaceUrlString106DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString106Defaults.update_forward_refs()

EndpointInterfaceUrlString106Merge.update_forward_refs()

EndpointInterfaceUrlString106Parse.update_forward_refs()

EndpointInterfaceUrlString107.update_forward_refs()

EndpointInterfaceUrlString107DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString107Defaults.update_forward_refs()

EndpointInterfaceUrlString107Merge.update_forward_refs()

EndpointInterfaceUrlString107Parse.update_forward_refs()

EndpointInterfaceUrlString108.update_forward_refs()

EndpointInterfaceUrlString108DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString108Defaults.update_forward_refs()

EndpointInterfaceUrlString108Merge.update_forward_refs()

EndpointInterfaceUrlString108Parse.update_forward_refs()

EndpointInterfaceUrlString109.update_forward_refs()

EndpointInterfaceUrlString109DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString109Defaults.update_forward_refs()

EndpointInterfaceUrlString109Merge.update_forward_refs()

EndpointInterfaceUrlString109Parse.update_forward_refs()

EndpointInterfaceUrlString10DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString10Defaults.update_forward_refs()

EndpointInterfaceUrlString10Merge.update_forward_refs()

EndpointInterfaceUrlString10Parse.update_forward_refs()

EndpointInterfaceUrlString11.update_forward_refs()

EndpointInterfaceUrlString110.update_forward_refs()

EndpointInterfaceUrlString110DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString110Defaults.update_forward_refs()

EndpointInterfaceUrlString110Merge.update_forward_refs()

EndpointInterfaceUrlString110Parse.update_forward_refs()

EndpointInterfaceUrlString111.update_forward_refs()

EndpointInterfaceUrlString111DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString111Defaults.update_forward_refs()

EndpointInterfaceUrlString111Merge.update_forward_refs()

EndpointInterfaceUrlString111Parse.update_forward_refs()

EndpointInterfaceUrlString112.update_forward_refs()

EndpointInterfaceUrlString112DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString112Defaults.update_forward_refs()

EndpointInterfaceUrlString112Merge.update_forward_refs()

EndpointInterfaceUrlString112Parse.update_forward_refs()

EndpointInterfaceUrlString113.update_forward_refs()

EndpointInterfaceUrlString113DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString113Defaults.update_forward_refs()

EndpointInterfaceUrlString113Merge.update_forward_refs()

EndpointInterfaceUrlString113Parse.update_forward_refs()

EndpointInterfaceUrlString114.update_forward_refs()

EndpointInterfaceUrlString114DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString114Defaults.update_forward_refs()

EndpointInterfaceUrlString114Merge.update_forward_refs()

EndpointInterfaceUrlString114Parse.update_forward_refs()

EndpointInterfaceUrlString115.update_forward_refs()

EndpointInterfaceUrlString115DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString115Defaults.update_forward_refs()

EndpointInterfaceUrlString115Merge.update_forward_refs()

EndpointInterfaceUrlString115Parse.update_forward_refs()

EndpointInterfaceUrlString116.update_forward_refs()

EndpointInterfaceUrlString116DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString116Defaults.update_forward_refs()

EndpointInterfaceUrlString116Merge.update_forward_refs()

EndpointInterfaceUrlString116Parse.update_forward_refs()

EndpointInterfaceUrlString117.update_forward_refs()

EndpointInterfaceUrlString117DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString117Defaults.update_forward_refs()

EndpointInterfaceUrlString117Merge.update_forward_refs()

EndpointInterfaceUrlString117Parse.update_forward_refs()

EndpointInterfaceUrlString118.update_forward_refs()

EndpointInterfaceUrlString118DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString118Defaults.update_forward_refs()

EndpointInterfaceUrlString118Merge.update_forward_refs()

EndpointInterfaceUrlString118Parse.update_forward_refs()

EndpointInterfaceUrlString119.update_forward_refs()

EndpointInterfaceUrlString119DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString119Defaults.update_forward_refs()

EndpointInterfaceUrlString119Merge.update_forward_refs()

EndpointInterfaceUrlString119Parse.update_forward_refs()

EndpointInterfaceUrlString11DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString11Defaults.update_forward_refs()

EndpointInterfaceUrlString11Merge.update_forward_refs()

EndpointInterfaceUrlString11Parse.update_forward_refs()

EndpointInterfaceUrlString12.update_forward_refs()

EndpointInterfaceUrlString120.update_forward_refs()

EndpointInterfaceUrlString120DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString120Defaults.update_forward_refs()

EndpointInterfaceUrlString120Merge.update_forward_refs()

EndpointInterfaceUrlString120Parse.update_forward_refs()

EndpointInterfaceUrlString121.update_forward_refs()

EndpointInterfaceUrlString121DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString121Defaults.update_forward_refs()

EndpointInterfaceUrlString121Merge.update_forward_refs()

EndpointInterfaceUrlString121Parse.update_forward_refs()

EndpointInterfaceUrlString122.update_forward_refs()

EndpointInterfaceUrlString122DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString122Defaults.update_forward_refs()

EndpointInterfaceUrlString122Merge.update_forward_refs()

EndpointInterfaceUrlString122Parse.update_forward_refs()

EndpointInterfaceUrlString123.update_forward_refs()

EndpointInterfaceUrlString123DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString123Defaults.update_forward_refs()

EndpointInterfaceUrlString123Merge.update_forward_refs()

EndpointInterfaceUrlString123Parse.update_forward_refs()

EndpointInterfaceUrlString124.update_forward_refs()

EndpointInterfaceUrlString124DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString124Defaults.update_forward_refs()

EndpointInterfaceUrlString124Merge.update_forward_refs()

EndpointInterfaceUrlString124Parse.update_forward_refs()

EndpointInterfaceUrlString125.update_forward_refs()

EndpointInterfaceUrlString125DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString125Defaults.update_forward_refs()

EndpointInterfaceUrlString125Merge.update_forward_refs()

EndpointInterfaceUrlString125Parse.update_forward_refs()

EndpointInterfaceUrlString126.update_forward_refs()

EndpointInterfaceUrlString126DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString126Defaults.update_forward_refs()

EndpointInterfaceUrlString126Merge.update_forward_refs()

EndpointInterfaceUrlString126Parse.update_forward_refs()

EndpointInterfaceUrlString127.update_forward_refs()

EndpointInterfaceUrlString127DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString127Defaults.update_forward_refs()

EndpointInterfaceUrlString127Merge.update_forward_refs()

EndpointInterfaceUrlString127Parse.update_forward_refs()

EndpointInterfaceUrlString128.update_forward_refs()

EndpointInterfaceUrlString128DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString128Defaults.update_forward_refs()

EndpointInterfaceUrlString128Merge.update_forward_refs()

EndpointInterfaceUrlString128Parse.update_forward_refs()

EndpointInterfaceUrlString129.update_forward_refs()

EndpointInterfaceUrlString129DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString129Defaults.update_forward_refs()

EndpointInterfaceUrlString129Merge.update_forward_refs()

EndpointInterfaceUrlString129Parse.update_forward_refs()

EndpointInterfaceUrlString12DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString12Defaults.update_forward_refs()

EndpointInterfaceUrlString12Merge.update_forward_refs()

EndpointInterfaceUrlString12Parse.update_forward_refs()

EndpointInterfaceUrlString13.update_forward_refs()

EndpointInterfaceUrlString130.update_forward_refs()

EndpointInterfaceUrlString130DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString130Defaults.update_forward_refs()

EndpointInterfaceUrlString130Merge.update_forward_refs()

EndpointInterfaceUrlString130Parse.update_forward_refs()

EndpointInterfaceUrlString131.update_forward_refs()

EndpointInterfaceUrlString131DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString131Defaults.update_forward_refs()

EndpointInterfaceUrlString131Merge.update_forward_refs()

EndpointInterfaceUrlString131Parse.update_forward_refs()

EndpointInterfaceUrlString132.update_forward_refs()

EndpointInterfaceUrlString132DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString132Defaults.update_forward_refs()

EndpointInterfaceUrlString132Merge.update_forward_refs()

EndpointInterfaceUrlString132Parse.update_forward_refs()

EndpointInterfaceUrlString133.update_forward_refs()

EndpointInterfaceUrlString133DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString133Defaults.update_forward_refs()

EndpointInterfaceUrlString133Merge.update_forward_refs()

EndpointInterfaceUrlString133Parse.update_forward_refs()

EndpointInterfaceUrlString134.update_forward_refs()

EndpointInterfaceUrlString134DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString134Defaults.update_forward_refs()

EndpointInterfaceUrlString134Merge.update_forward_refs()

EndpointInterfaceUrlString134Parse.update_forward_refs()

EndpointInterfaceUrlString135.update_forward_refs()

EndpointInterfaceUrlString135DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString135Defaults.update_forward_refs()

EndpointInterfaceUrlString135Merge.update_forward_refs()

EndpointInterfaceUrlString135Parse.update_forward_refs()

EndpointInterfaceUrlString136.update_forward_refs()

EndpointInterfaceUrlString136DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString136Defaults.update_forward_refs()

EndpointInterfaceUrlString136Merge.update_forward_refs()

EndpointInterfaceUrlString136Parse.update_forward_refs()

EndpointInterfaceUrlString137.update_forward_refs()

EndpointInterfaceUrlString137DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString137Defaults.update_forward_refs()

EndpointInterfaceUrlString137Merge.update_forward_refs()

EndpointInterfaceUrlString137Parse.update_forward_refs()

EndpointInterfaceUrlString138.update_forward_refs()

EndpointInterfaceUrlString138DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString138Defaults.update_forward_refs()

EndpointInterfaceUrlString138Merge.update_forward_refs()

EndpointInterfaceUrlString138Parse.update_forward_refs()

EndpointInterfaceUrlString139.update_forward_refs()

EndpointInterfaceUrlString139DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString139Defaults.update_forward_refs()

EndpointInterfaceUrlString139Merge.update_forward_refs()

EndpointInterfaceUrlString139Parse.update_forward_refs()

EndpointInterfaceUrlString13DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString13Defaults.update_forward_refs()

EndpointInterfaceUrlString13Merge.update_forward_refs()

EndpointInterfaceUrlString13Parse.update_forward_refs()

EndpointInterfaceUrlString14.update_forward_refs()

EndpointInterfaceUrlString140.update_forward_refs()

EndpointInterfaceUrlString140DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString140Defaults.update_forward_refs()

EndpointInterfaceUrlString140Merge.update_forward_refs()

EndpointInterfaceUrlString140Parse.update_forward_refs()

EndpointInterfaceUrlString141.update_forward_refs()

EndpointInterfaceUrlString141DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString141Defaults.update_forward_refs()

EndpointInterfaceUrlString141Merge.update_forward_refs()

EndpointInterfaceUrlString141Parse.update_forward_refs()

EndpointInterfaceUrlString142.update_forward_refs()

EndpointInterfaceUrlString142DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString142Defaults.update_forward_refs()

EndpointInterfaceUrlString142Merge.update_forward_refs()

EndpointInterfaceUrlString142Parse.update_forward_refs()

EndpointInterfaceUrlString143.update_forward_refs()

EndpointInterfaceUrlString143DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString143Defaults.update_forward_refs()

EndpointInterfaceUrlString143Merge.update_forward_refs()

EndpointInterfaceUrlString143Parse.update_forward_refs()

EndpointInterfaceUrlString144.update_forward_refs()

EndpointInterfaceUrlString144DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString144Defaults.update_forward_refs()

EndpointInterfaceUrlString144Merge.update_forward_refs()

EndpointInterfaceUrlString144Parse.update_forward_refs()

EndpointInterfaceUrlString145.update_forward_refs()

EndpointInterfaceUrlString145DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString145Defaults.update_forward_refs()

EndpointInterfaceUrlString145Merge.update_forward_refs()

EndpointInterfaceUrlString145Parse.update_forward_refs()

EndpointInterfaceUrlString146.update_forward_refs()

EndpointInterfaceUrlString146DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString146Defaults.update_forward_refs()

EndpointInterfaceUrlString146Merge.update_forward_refs()

EndpointInterfaceUrlString146Parse.update_forward_refs()

EndpointInterfaceUrlString147.update_forward_refs()

EndpointInterfaceUrlString147DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString147Defaults.update_forward_refs()

EndpointInterfaceUrlString147Merge.update_forward_refs()

EndpointInterfaceUrlString147Parse.update_forward_refs()

EndpointInterfaceUrlString148.update_forward_refs()

EndpointInterfaceUrlString148DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString148Defaults.update_forward_refs()

EndpointInterfaceUrlString148Merge.update_forward_refs()

EndpointInterfaceUrlString148Parse.update_forward_refs()

EndpointInterfaceUrlString149.update_forward_refs()

EndpointInterfaceUrlString149DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString149Defaults.update_forward_refs()

EndpointInterfaceUrlString149Merge.update_forward_refs()

EndpointInterfaceUrlString149Parse.update_forward_refs()

EndpointInterfaceUrlString14DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString14Defaults.update_forward_refs()

EndpointInterfaceUrlString14Merge.update_forward_refs()

EndpointInterfaceUrlString14Parse.update_forward_refs()

EndpointInterfaceUrlString15.update_forward_refs()

EndpointInterfaceUrlString150.update_forward_refs()

EndpointInterfaceUrlString150DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString150Defaults.update_forward_refs()

EndpointInterfaceUrlString150Merge.update_forward_refs()

EndpointInterfaceUrlString150Parse.update_forward_refs()

EndpointInterfaceUrlString151.update_forward_refs()

EndpointInterfaceUrlString151DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString151Defaults.update_forward_refs()

EndpointInterfaceUrlString151Merge.update_forward_refs()

EndpointInterfaceUrlString151Parse.update_forward_refs()

EndpointInterfaceUrlString152.update_forward_refs()

EndpointInterfaceUrlString152DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString152Defaults.update_forward_refs()

EndpointInterfaceUrlString152Merge.update_forward_refs()

EndpointInterfaceUrlString152Parse.update_forward_refs()

EndpointInterfaceUrlString153.update_forward_refs()

EndpointInterfaceUrlString153DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString153Defaults.update_forward_refs()

EndpointInterfaceUrlString153Merge.update_forward_refs()

EndpointInterfaceUrlString153Parse.update_forward_refs()

EndpointInterfaceUrlString154.update_forward_refs()

EndpointInterfaceUrlString154DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString154Defaults.update_forward_refs()

EndpointInterfaceUrlString154Merge.update_forward_refs()

EndpointInterfaceUrlString154Parse.update_forward_refs()

EndpointInterfaceUrlString155.update_forward_refs()

EndpointInterfaceUrlString155DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString155Defaults.update_forward_refs()

EndpointInterfaceUrlString155Merge.update_forward_refs()

EndpointInterfaceUrlString155Parse.update_forward_refs()

EndpointInterfaceUrlString156.update_forward_refs()

EndpointInterfaceUrlString156DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString156Defaults.update_forward_refs()

EndpointInterfaceUrlString156Merge.update_forward_refs()

EndpointInterfaceUrlString156Parse.update_forward_refs()

EndpointInterfaceUrlString157.update_forward_refs()

EndpointInterfaceUrlString157DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString157Defaults.update_forward_refs()

EndpointInterfaceUrlString157Merge.update_forward_refs()

EndpointInterfaceUrlString157Parse.update_forward_refs()

EndpointInterfaceUrlString158.update_forward_refs()

EndpointInterfaceUrlString158DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString158Defaults.update_forward_refs()

EndpointInterfaceUrlString158Merge.update_forward_refs()

EndpointInterfaceUrlString158Parse.update_forward_refs()

EndpointInterfaceUrlString159.update_forward_refs()

EndpointInterfaceUrlString159DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString159Defaults.update_forward_refs()

EndpointInterfaceUrlString159Merge.update_forward_refs()

EndpointInterfaceUrlString159Parse.update_forward_refs()

EndpointInterfaceUrlString15DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString15Defaults.update_forward_refs()

EndpointInterfaceUrlString15Merge.update_forward_refs()

EndpointInterfaceUrlString15Parse.update_forward_refs()

EndpointInterfaceUrlString16.update_forward_refs()

EndpointInterfaceUrlString160.update_forward_refs()

EndpointInterfaceUrlString160DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString160Defaults.update_forward_refs()

EndpointInterfaceUrlString160Merge.update_forward_refs()

EndpointInterfaceUrlString160Parse.update_forward_refs()

EndpointInterfaceUrlString161.update_forward_refs()

EndpointInterfaceUrlString161DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString161Defaults.update_forward_refs()

EndpointInterfaceUrlString161Merge.update_forward_refs()

EndpointInterfaceUrlString161Parse.update_forward_refs()

EndpointInterfaceUrlString162.update_forward_refs()

EndpointInterfaceUrlString162DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString162Defaults.update_forward_refs()

EndpointInterfaceUrlString162Merge.update_forward_refs()

EndpointInterfaceUrlString162Parse.update_forward_refs()

EndpointInterfaceUrlString163.update_forward_refs()

EndpointInterfaceUrlString163DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString163Defaults.update_forward_refs()

EndpointInterfaceUrlString163Merge.update_forward_refs()

EndpointInterfaceUrlString163Parse.update_forward_refs()

EndpointInterfaceUrlString164.update_forward_refs()

EndpointInterfaceUrlString164DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString164Defaults.update_forward_refs()

EndpointInterfaceUrlString164Merge.update_forward_refs()

EndpointInterfaceUrlString164Parse.update_forward_refs()

EndpointInterfaceUrlString165.update_forward_refs()

EndpointInterfaceUrlString165DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString165Defaults.update_forward_refs()

EndpointInterfaceUrlString165Merge.update_forward_refs()

EndpointInterfaceUrlString165Parse.update_forward_refs()

EndpointInterfaceUrlString166.update_forward_refs()

EndpointInterfaceUrlString166DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString166Defaults.update_forward_refs()

EndpointInterfaceUrlString166Merge.update_forward_refs()

EndpointInterfaceUrlString166Parse.update_forward_refs()

EndpointInterfaceUrlString167.update_forward_refs()

EndpointInterfaceUrlString167DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString167Defaults.update_forward_refs()

EndpointInterfaceUrlString167Merge.update_forward_refs()

EndpointInterfaceUrlString167Parse.update_forward_refs()

EndpointInterfaceUrlString168.update_forward_refs()

EndpointInterfaceUrlString168DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString168Defaults.update_forward_refs()

EndpointInterfaceUrlString168Merge.update_forward_refs()

EndpointInterfaceUrlString168Parse.update_forward_refs()

EndpointInterfaceUrlString169.update_forward_refs()

EndpointInterfaceUrlString169DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString169Defaults.update_forward_refs()

EndpointInterfaceUrlString169Merge.update_forward_refs()

EndpointInterfaceUrlString169Parse.update_forward_refs()

EndpointInterfaceUrlString16DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString16Defaults.update_forward_refs()

EndpointInterfaceUrlString16Merge.update_forward_refs()

EndpointInterfaceUrlString16Parse.update_forward_refs()

EndpointInterfaceUrlString17.update_forward_refs()

EndpointInterfaceUrlString170.update_forward_refs()

EndpointInterfaceUrlString170DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString170Defaults.update_forward_refs()

EndpointInterfaceUrlString170Merge.update_forward_refs()

EndpointInterfaceUrlString170Parse.update_forward_refs()

EndpointInterfaceUrlString171.update_forward_refs()

EndpointInterfaceUrlString171DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString171Defaults.update_forward_refs()

EndpointInterfaceUrlString171Merge.update_forward_refs()

EndpointInterfaceUrlString171Parse.update_forward_refs()

EndpointInterfaceUrlString172.update_forward_refs()

EndpointInterfaceUrlString172DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString172Defaults.update_forward_refs()

EndpointInterfaceUrlString172Merge.update_forward_refs()

EndpointInterfaceUrlString172Parse.update_forward_refs()

EndpointInterfaceUrlString173.update_forward_refs()

EndpointInterfaceUrlString173DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString173Defaults.update_forward_refs()

EndpointInterfaceUrlString173Merge.update_forward_refs()

EndpointInterfaceUrlString173Parse.update_forward_refs()

EndpointInterfaceUrlString174.update_forward_refs()

EndpointInterfaceUrlString174DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString174Defaults.update_forward_refs()

EndpointInterfaceUrlString174Merge.update_forward_refs()

EndpointInterfaceUrlString174Parse.update_forward_refs()

EndpointInterfaceUrlString175.update_forward_refs()

EndpointInterfaceUrlString175DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString175Defaults.update_forward_refs()

EndpointInterfaceUrlString175Merge.update_forward_refs()

EndpointInterfaceUrlString175Parse.update_forward_refs()

EndpointInterfaceUrlString176.update_forward_refs()

EndpointInterfaceUrlString176DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString176Defaults.update_forward_refs()

EndpointInterfaceUrlString176Merge.update_forward_refs()

EndpointInterfaceUrlString176Parse.update_forward_refs()

EndpointInterfaceUrlString177.update_forward_refs()

EndpointInterfaceUrlString177DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString177Defaults.update_forward_refs()

EndpointInterfaceUrlString177Merge.update_forward_refs()

EndpointInterfaceUrlString177Parse.update_forward_refs()

EndpointInterfaceUrlString178.update_forward_refs()

EndpointInterfaceUrlString178DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString178Defaults.update_forward_refs()

EndpointInterfaceUrlString178Merge.update_forward_refs()

EndpointInterfaceUrlString178Parse.update_forward_refs()

EndpointInterfaceUrlString179.update_forward_refs()

EndpointInterfaceUrlString179DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString179Defaults.update_forward_refs()

EndpointInterfaceUrlString179Merge.update_forward_refs()

EndpointInterfaceUrlString179Parse.update_forward_refs()

EndpointInterfaceUrlString17DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString17Defaults.update_forward_refs()

EndpointInterfaceUrlString17Merge.update_forward_refs()

EndpointInterfaceUrlString17Parse.update_forward_refs()

EndpointInterfaceUrlString18.update_forward_refs()

EndpointInterfaceUrlString180.update_forward_refs()

EndpointInterfaceUrlString180DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString180Defaults.update_forward_refs()

EndpointInterfaceUrlString180Merge.update_forward_refs()

EndpointInterfaceUrlString180Parse.update_forward_refs()

EndpointInterfaceUrlString181.update_forward_refs()

EndpointInterfaceUrlString181DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString181Defaults.update_forward_refs()

EndpointInterfaceUrlString181Merge.update_forward_refs()

EndpointInterfaceUrlString181Parse.update_forward_refs()

EndpointInterfaceUrlString182.update_forward_refs()

EndpointInterfaceUrlString182DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString182Defaults.update_forward_refs()

EndpointInterfaceUrlString182Merge.update_forward_refs()

EndpointInterfaceUrlString182Parse.update_forward_refs()

EndpointInterfaceUrlString183.update_forward_refs()

EndpointInterfaceUrlString183DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString183Defaults.update_forward_refs()

EndpointInterfaceUrlString183Merge.update_forward_refs()

EndpointInterfaceUrlString183Parse.update_forward_refs()

EndpointInterfaceUrlString184.update_forward_refs()

EndpointInterfaceUrlString184DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString184Defaults.update_forward_refs()

EndpointInterfaceUrlString184Merge.update_forward_refs()

EndpointInterfaceUrlString184Parse.update_forward_refs()

EndpointInterfaceUrlString185.update_forward_refs()

EndpointInterfaceUrlString185DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString185Defaults.update_forward_refs()

EndpointInterfaceUrlString185Merge.update_forward_refs()

EndpointInterfaceUrlString185Parse.update_forward_refs()

EndpointInterfaceUrlString186.update_forward_refs()

EndpointInterfaceUrlString186DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString186Defaults.update_forward_refs()

EndpointInterfaceUrlString186Merge.update_forward_refs()

EndpointInterfaceUrlString186Parse.update_forward_refs()

EndpointInterfaceUrlString187.update_forward_refs()

EndpointInterfaceUrlString187DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString187Defaults.update_forward_refs()

EndpointInterfaceUrlString187Merge.update_forward_refs()

EndpointInterfaceUrlString187Parse.update_forward_refs()

EndpointInterfaceUrlString188.update_forward_refs()

EndpointInterfaceUrlString188DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString188Defaults.update_forward_refs()

EndpointInterfaceUrlString188Merge.update_forward_refs()

EndpointInterfaceUrlString188Parse.update_forward_refs()

EndpointInterfaceUrlString189.update_forward_refs()

EndpointInterfaceUrlString189DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString189Defaults.update_forward_refs()

EndpointInterfaceUrlString189Merge.update_forward_refs()

EndpointInterfaceUrlString189Parse.update_forward_refs()

EndpointInterfaceUrlString18DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString18Defaults.update_forward_refs()

EndpointInterfaceUrlString18Merge.update_forward_refs()

EndpointInterfaceUrlString18Parse.update_forward_refs()

EndpointInterfaceUrlString19.update_forward_refs()

EndpointInterfaceUrlString190.update_forward_refs()

EndpointInterfaceUrlString190DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString190Defaults.update_forward_refs()

EndpointInterfaceUrlString190Merge.update_forward_refs()

EndpointInterfaceUrlString190Parse.update_forward_refs()

EndpointInterfaceUrlString191.update_forward_refs()

EndpointInterfaceUrlString191DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString191Defaults.update_forward_refs()

EndpointInterfaceUrlString191Merge.update_forward_refs()

EndpointInterfaceUrlString191Parse.update_forward_refs()

EndpointInterfaceUrlString192.update_forward_refs()

EndpointInterfaceUrlString192DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString192Defaults.update_forward_refs()

EndpointInterfaceUrlString192Merge.update_forward_refs()

EndpointInterfaceUrlString192Parse.update_forward_refs()

EndpointInterfaceUrlString193.update_forward_refs()

EndpointInterfaceUrlString193DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString193Defaults.update_forward_refs()

EndpointInterfaceUrlString193Merge.update_forward_refs()

EndpointInterfaceUrlString193Parse.update_forward_refs()

EndpointInterfaceUrlString194.update_forward_refs()

EndpointInterfaceUrlString194DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString194Defaults.update_forward_refs()

EndpointInterfaceUrlString194Merge.update_forward_refs()

EndpointInterfaceUrlString194Parse.update_forward_refs()

EndpointInterfaceUrlString195.update_forward_refs()

EndpointInterfaceUrlString195DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString195Defaults.update_forward_refs()

EndpointInterfaceUrlString195Merge.update_forward_refs()

EndpointInterfaceUrlString195Parse.update_forward_refs()

EndpointInterfaceUrlString196.update_forward_refs()

EndpointInterfaceUrlString196DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString196Defaults.update_forward_refs()

EndpointInterfaceUrlString196Merge.update_forward_refs()

EndpointInterfaceUrlString196Parse.update_forward_refs()

EndpointInterfaceUrlString197.update_forward_refs()

EndpointInterfaceUrlString197DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString197Defaults.update_forward_refs()

EndpointInterfaceUrlString197Merge.update_forward_refs()

EndpointInterfaceUrlString197Parse.update_forward_refs()

EndpointInterfaceUrlString198.update_forward_refs()

EndpointInterfaceUrlString198DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString198Defaults.update_forward_refs()

EndpointInterfaceUrlString198Merge.update_forward_refs()

EndpointInterfaceUrlString198Parse.update_forward_refs()

EndpointInterfaceUrlString199.update_forward_refs()

EndpointInterfaceUrlString199DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString199Defaults.update_forward_refs()

EndpointInterfaceUrlString199Merge.update_forward_refs()

EndpointInterfaceUrlString199Parse.update_forward_refs()

EndpointInterfaceUrlString19DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString19Defaults.update_forward_refs()

EndpointInterfaceUrlString19Merge.update_forward_refs()

EndpointInterfaceUrlString19Parse.update_forward_refs()

EndpointInterfaceUrlString1DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString1Defaults.update_forward_refs()

EndpointInterfaceUrlString1Merge.update_forward_refs()

EndpointInterfaceUrlString1Parse.update_forward_refs()

EndpointInterfaceUrlString2.update_forward_refs()

EndpointInterfaceUrlString20.update_forward_refs()

EndpointInterfaceUrlString200.update_forward_refs()

EndpointInterfaceUrlString200DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString200Defaults.update_forward_refs()

EndpointInterfaceUrlString200Merge.update_forward_refs()

EndpointInterfaceUrlString200Parse.update_forward_refs()

EndpointInterfaceUrlString201.update_forward_refs()

EndpointInterfaceUrlString201DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString201Defaults.update_forward_refs()

EndpointInterfaceUrlString201Merge.update_forward_refs()

EndpointInterfaceUrlString201Parse.update_forward_refs()

EndpointInterfaceUrlString202.update_forward_refs()

EndpointInterfaceUrlString202DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString202Defaults.update_forward_refs()

EndpointInterfaceUrlString202Merge.update_forward_refs()

EndpointInterfaceUrlString202Parse.update_forward_refs()

EndpointInterfaceUrlString203.update_forward_refs()

EndpointInterfaceUrlString203DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString203Defaults.update_forward_refs()

EndpointInterfaceUrlString203Merge.update_forward_refs()

EndpointInterfaceUrlString203Parse.update_forward_refs()

EndpointInterfaceUrlString204.update_forward_refs()

EndpointInterfaceUrlString204DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString204Defaults.update_forward_refs()

EndpointInterfaceUrlString204Merge.update_forward_refs()

EndpointInterfaceUrlString204Parse.update_forward_refs()

EndpointInterfaceUrlString205.update_forward_refs()

EndpointInterfaceUrlString205DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString205Defaults.update_forward_refs()

EndpointInterfaceUrlString205Merge.update_forward_refs()

EndpointInterfaceUrlString205Parse.update_forward_refs()

EndpointInterfaceUrlString206.update_forward_refs()

EndpointInterfaceUrlString206DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString206Defaults.update_forward_refs()

EndpointInterfaceUrlString206Merge.update_forward_refs()

EndpointInterfaceUrlString206Parse.update_forward_refs()

EndpointInterfaceUrlString207.update_forward_refs()

EndpointInterfaceUrlString207DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString207Defaults.update_forward_refs()

EndpointInterfaceUrlString207Merge.update_forward_refs()

EndpointInterfaceUrlString207Parse.update_forward_refs()

EndpointInterfaceUrlString208.update_forward_refs()

EndpointInterfaceUrlString208DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString208Defaults.update_forward_refs()

EndpointInterfaceUrlString208Merge.update_forward_refs()

EndpointInterfaceUrlString208Parse.update_forward_refs()

EndpointInterfaceUrlString209.update_forward_refs()

EndpointInterfaceUrlString209DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString209Defaults.update_forward_refs()

EndpointInterfaceUrlString209Merge.update_forward_refs()

EndpointInterfaceUrlString209Parse.update_forward_refs()

EndpointInterfaceUrlString20DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString20Defaults.update_forward_refs()

EndpointInterfaceUrlString20Merge.update_forward_refs()

EndpointInterfaceUrlString20Parse.update_forward_refs()

EndpointInterfaceUrlString21.update_forward_refs()

EndpointInterfaceUrlString210.update_forward_refs()

EndpointInterfaceUrlString210DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString210Defaults.update_forward_refs()

EndpointInterfaceUrlString210Merge.update_forward_refs()

EndpointInterfaceUrlString210Parse.update_forward_refs()

EndpointInterfaceUrlString211.update_forward_refs()

EndpointInterfaceUrlString211DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString211Defaults.update_forward_refs()

EndpointInterfaceUrlString211Merge.update_forward_refs()

EndpointInterfaceUrlString211Parse.update_forward_refs()

EndpointInterfaceUrlString212.update_forward_refs()

EndpointInterfaceUrlString212DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString212Defaults.update_forward_refs()

EndpointInterfaceUrlString212Merge.update_forward_refs()

EndpointInterfaceUrlString212Parse.update_forward_refs()

EndpointInterfaceUrlString213.update_forward_refs()

EndpointInterfaceUrlString213DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString213Defaults.update_forward_refs()

EndpointInterfaceUrlString213Merge.update_forward_refs()

EndpointInterfaceUrlString213Parse.update_forward_refs()

EndpointInterfaceUrlString214.update_forward_refs()

EndpointInterfaceUrlString214DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString214Defaults.update_forward_refs()

EndpointInterfaceUrlString214Merge.update_forward_refs()

EndpointInterfaceUrlString214Parse.update_forward_refs()

EndpointInterfaceUrlString215.update_forward_refs()

EndpointInterfaceUrlString215DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString215Defaults.update_forward_refs()

EndpointInterfaceUrlString215Merge.update_forward_refs()

EndpointInterfaceUrlString215Parse.update_forward_refs()

EndpointInterfaceUrlString216.update_forward_refs()

EndpointInterfaceUrlString216DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString216Defaults.update_forward_refs()

EndpointInterfaceUrlString216Merge.update_forward_refs()

EndpointInterfaceUrlString216Parse.update_forward_refs()

EndpointInterfaceUrlString217.update_forward_refs()

EndpointInterfaceUrlString217DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString217Defaults.update_forward_refs()

EndpointInterfaceUrlString217Merge.update_forward_refs()

EndpointInterfaceUrlString217Parse.update_forward_refs()

EndpointInterfaceUrlString218.update_forward_refs()

EndpointInterfaceUrlString218DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString218Defaults.update_forward_refs()

EndpointInterfaceUrlString218Merge.update_forward_refs()

EndpointInterfaceUrlString218Parse.update_forward_refs()

EndpointInterfaceUrlString219.update_forward_refs()

EndpointInterfaceUrlString219DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString219Defaults.update_forward_refs()

EndpointInterfaceUrlString219Merge.update_forward_refs()

EndpointInterfaceUrlString219Parse.update_forward_refs()

EndpointInterfaceUrlString21DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString21Defaults.update_forward_refs()

EndpointInterfaceUrlString21Merge.update_forward_refs()

EndpointInterfaceUrlString21Parse.update_forward_refs()

EndpointInterfaceUrlString22.update_forward_refs()

EndpointInterfaceUrlString220.update_forward_refs()

EndpointInterfaceUrlString220DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString220Defaults.update_forward_refs()

EndpointInterfaceUrlString220Merge.update_forward_refs()

EndpointInterfaceUrlString220Parse.update_forward_refs()

EndpointInterfaceUrlString221.update_forward_refs()

EndpointInterfaceUrlString221DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString221Defaults.update_forward_refs()

EndpointInterfaceUrlString221Merge.update_forward_refs()

EndpointInterfaceUrlString221Parse.update_forward_refs()

EndpointInterfaceUrlString222.update_forward_refs()

EndpointInterfaceUrlString222DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString222Defaults.update_forward_refs()

EndpointInterfaceUrlString222Merge.update_forward_refs()

EndpointInterfaceUrlString222Parse.update_forward_refs()

EndpointInterfaceUrlString223.update_forward_refs()

EndpointInterfaceUrlString223DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString223Defaults.update_forward_refs()

EndpointInterfaceUrlString223Merge.update_forward_refs()

EndpointInterfaceUrlString223Parse.update_forward_refs()

EndpointInterfaceUrlString224.update_forward_refs()

EndpointInterfaceUrlString224DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString224Defaults.update_forward_refs()

EndpointInterfaceUrlString224Merge.update_forward_refs()

EndpointInterfaceUrlString224Parse.update_forward_refs()

EndpointInterfaceUrlString225.update_forward_refs()

EndpointInterfaceUrlString225DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString225Defaults.update_forward_refs()

EndpointInterfaceUrlString225Merge.update_forward_refs()

EndpointInterfaceUrlString225Parse.update_forward_refs()

EndpointInterfaceUrlString226.update_forward_refs()

EndpointInterfaceUrlString226DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString226Defaults.update_forward_refs()

EndpointInterfaceUrlString226Merge.update_forward_refs()

EndpointInterfaceUrlString226Parse.update_forward_refs()

EndpointInterfaceUrlString227.update_forward_refs()

EndpointInterfaceUrlString227DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString227Defaults.update_forward_refs()

EndpointInterfaceUrlString227Merge.update_forward_refs()

EndpointInterfaceUrlString227Parse.update_forward_refs()

EndpointInterfaceUrlString228.update_forward_refs()

EndpointInterfaceUrlString228DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString228Defaults.update_forward_refs()

EndpointInterfaceUrlString228Merge.update_forward_refs()

EndpointInterfaceUrlString228Parse.update_forward_refs()

EndpointInterfaceUrlString229.update_forward_refs()

EndpointInterfaceUrlString229DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString229Defaults.update_forward_refs()

EndpointInterfaceUrlString229Merge.update_forward_refs()

EndpointInterfaceUrlString229Parse.update_forward_refs()

EndpointInterfaceUrlString22DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString22Defaults.update_forward_refs()

EndpointInterfaceUrlString22Merge.update_forward_refs()

EndpointInterfaceUrlString22Parse.update_forward_refs()

EndpointInterfaceUrlString23.update_forward_refs()

EndpointInterfaceUrlString230.update_forward_refs()

EndpointInterfaceUrlString230DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString230Defaults.update_forward_refs()

EndpointInterfaceUrlString230Merge.update_forward_refs()

EndpointInterfaceUrlString230Parse.update_forward_refs()

EndpointInterfaceUrlString231.update_forward_refs()

EndpointInterfaceUrlString231DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString231Defaults.update_forward_refs()

EndpointInterfaceUrlString231Merge.update_forward_refs()

EndpointInterfaceUrlString231Parse.update_forward_refs()

EndpointInterfaceUrlString232.update_forward_refs()

EndpointInterfaceUrlString232DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString232Defaults.update_forward_refs()

EndpointInterfaceUrlString232Merge.update_forward_refs()

EndpointInterfaceUrlString232Parse.update_forward_refs()

EndpointInterfaceUrlString233.update_forward_refs()

EndpointInterfaceUrlString233DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString233Defaults.update_forward_refs()

EndpointInterfaceUrlString233Merge.update_forward_refs()

EndpointInterfaceUrlString233Parse.update_forward_refs()

EndpointInterfaceUrlString234.update_forward_refs()

EndpointInterfaceUrlString234DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString234Defaults.update_forward_refs()

EndpointInterfaceUrlString234Merge.update_forward_refs()

EndpointInterfaceUrlString234Parse.update_forward_refs()

EndpointInterfaceUrlString235.update_forward_refs()

EndpointInterfaceUrlString235DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString235Defaults.update_forward_refs()

EndpointInterfaceUrlString235Merge.update_forward_refs()

EndpointInterfaceUrlString235Parse.update_forward_refs()

EndpointInterfaceUrlString236.update_forward_refs()

EndpointInterfaceUrlString236DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString236Defaults.update_forward_refs()

EndpointInterfaceUrlString236Merge.update_forward_refs()

EndpointInterfaceUrlString236Parse.update_forward_refs()

EndpointInterfaceUrlString237.update_forward_refs()

EndpointInterfaceUrlString237DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString237Defaults.update_forward_refs()

EndpointInterfaceUrlString237Merge.update_forward_refs()

EndpointInterfaceUrlString237Parse.update_forward_refs()

EndpointInterfaceUrlString238.update_forward_refs()

EndpointInterfaceUrlString238DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString238Defaults.update_forward_refs()

EndpointInterfaceUrlString238Merge.update_forward_refs()

EndpointInterfaceUrlString238Parse.update_forward_refs()

EndpointInterfaceUrlString239.update_forward_refs()

EndpointInterfaceUrlString239DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString239Defaults.update_forward_refs()

EndpointInterfaceUrlString239Merge.update_forward_refs()

EndpointInterfaceUrlString239Parse.update_forward_refs()

EndpointInterfaceUrlString23DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString23Defaults.update_forward_refs()

EndpointInterfaceUrlString23Merge.update_forward_refs()

EndpointInterfaceUrlString23Parse.update_forward_refs()

EndpointInterfaceUrlString24.update_forward_refs()

EndpointInterfaceUrlString240.update_forward_refs()

EndpointInterfaceUrlString240DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString240Defaults.update_forward_refs()

EndpointInterfaceUrlString240Merge.update_forward_refs()

EndpointInterfaceUrlString240Parse.update_forward_refs()

EndpointInterfaceUrlString241.update_forward_refs()

EndpointInterfaceUrlString241DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString241Defaults.update_forward_refs()

EndpointInterfaceUrlString241Merge.update_forward_refs()

EndpointInterfaceUrlString241Parse.update_forward_refs()

EndpointInterfaceUrlString242.update_forward_refs()

EndpointInterfaceUrlString242DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString242Defaults.update_forward_refs()

EndpointInterfaceUrlString242Merge.update_forward_refs()

EndpointInterfaceUrlString242Parse.update_forward_refs()

EndpointInterfaceUrlString243.update_forward_refs()

EndpointInterfaceUrlString243DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString243Defaults.update_forward_refs()

EndpointInterfaceUrlString243Merge.update_forward_refs()

EndpointInterfaceUrlString243Parse.update_forward_refs()

EndpointInterfaceUrlString244.update_forward_refs()

EndpointInterfaceUrlString244DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString244Defaults.update_forward_refs()

EndpointInterfaceUrlString244Merge.update_forward_refs()

EndpointInterfaceUrlString244Parse.update_forward_refs()

EndpointInterfaceUrlString245.update_forward_refs()

EndpointInterfaceUrlString245DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString245Defaults.update_forward_refs()

EndpointInterfaceUrlString245Merge.update_forward_refs()

EndpointInterfaceUrlString245Parse.update_forward_refs()

EndpointInterfaceUrlString246.update_forward_refs()

EndpointInterfaceUrlString246DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString246Defaults.update_forward_refs()

EndpointInterfaceUrlString246Merge.update_forward_refs()

EndpointInterfaceUrlString246Parse.update_forward_refs()

EndpointInterfaceUrlString247.update_forward_refs()

EndpointInterfaceUrlString247DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString247Defaults.update_forward_refs()

EndpointInterfaceUrlString247Merge.update_forward_refs()

EndpointInterfaceUrlString247Parse.update_forward_refs()

EndpointInterfaceUrlString248.update_forward_refs()

EndpointInterfaceUrlString248DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString248Defaults.update_forward_refs()

EndpointInterfaceUrlString248Merge.update_forward_refs()

EndpointInterfaceUrlString248Parse.update_forward_refs()

EndpointInterfaceUrlString249.update_forward_refs()

EndpointInterfaceUrlString249DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString249Defaults.update_forward_refs()

EndpointInterfaceUrlString249Merge.update_forward_refs()

EndpointInterfaceUrlString249Parse.update_forward_refs()

EndpointInterfaceUrlString24DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString24Defaults.update_forward_refs()

EndpointInterfaceUrlString24Merge.update_forward_refs()

EndpointInterfaceUrlString24Parse.update_forward_refs()

EndpointInterfaceUrlString25.update_forward_refs()

EndpointInterfaceUrlString250.update_forward_refs()

EndpointInterfaceUrlString250DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString250Defaults.update_forward_refs()

EndpointInterfaceUrlString250Merge.update_forward_refs()

EndpointInterfaceUrlString250Parse.update_forward_refs()

EndpointInterfaceUrlString251.update_forward_refs()

EndpointInterfaceUrlString251DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString251Defaults.update_forward_refs()

EndpointInterfaceUrlString251Merge.update_forward_refs()

EndpointInterfaceUrlString251Parse.update_forward_refs()

EndpointInterfaceUrlString252.update_forward_refs()

EndpointInterfaceUrlString252DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString252Defaults.update_forward_refs()

EndpointInterfaceUrlString252Merge.update_forward_refs()

EndpointInterfaceUrlString252Parse.update_forward_refs()

EndpointInterfaceUrlString253.update_forward_refs()

EndpointInterfaceUrlString253DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString253Defaults.update_forward_refs()

EndpointInterfaceUrlString253Merge.update_forward_refs()

EndpointInterfaceUrlString253Parse.update_forward_refs()

EndpointInterfaceUrlString254.update_forward_refs()

EndpointInterfaceUrlString254DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString254Defaults.update_forward_refs()

EndpointInterfaceUrlString254Merge.update_forward_refs()

EndpointInterfaceUrlString254Parse.update_forward_refs()

EndpointInterfaceUrlString255.update_forward_refs()

EndpointInterfaceUrlString255DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString255Defaults.update_forward_refs()

EndpointInterfaceUrlString255Merge.update_forward_refs()

EndpointInterfaceUrlString255Parse.update_forward_refs()

EndpointInterfaceUrlString256.update_forward_refs()

EndpointInterfaceUrlString256DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString256Defaults.update_forward_refs()

EndpointInterfaceUrlString256Merge.update_forward_refs()

EndpointInterfaceUrlString256Parse.update_forward_refs()

EndpointInterfaceUrlString257.update_forward_refs()

EndpointInterfaceUrlString257DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString257Defaults.update_forward_refs()

EndpointInterfaceUrlString257Merge.update_forward_refs()

EndpointInterfaceUrlString257Parse.update_forward_refs()

EndpointInterfaceUrlString258.update_forward_refs()

EndpointInterfaceUrlString258DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString258Defaults.update_forward_refs()

EndpointInterfaceUrlString258Merge.update_forward_refs()

EndpointInterfaceUrlString258Parse.update_forward_refs()

EndpointInterfaceUrlString259.update_forward_refs()

EndpointInterfaceUrlString259DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString259Defaults.update_forward_refs()

EndpointInterfaceUrlString259Merge.update_forward_refs()

EndpointInterfaceUrlString259Parse.update_forward_refs()

EndpointInterfaceUrlString25DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString25Defaults.update_forward_refs()

EndpointInterfaceUrlString25Merge.update_forward_refs()

EndpointInterfaceUrlString25Parse.update_forward_refs()

EndpointInterfaceUrlString26.update_forward_refs()

EndpointInterfaceUrlString260.update_forward_refs()

EndpointInterfaceUrlString260DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString260Defaults.update_forward_refs()

EndpointInterfaceUrlString260Merge.update_forward_refs()

EndpointInterfaceUrlString260Parse.update_forward_refs()

EndpointInterfaceUrlString261.update_forward_refs()

EndpointInterfaceUrlString261DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString261Defaults.update_forward_refs()

EndpointInterfaceUrlString261Merge.update_forward_refs()

EndpointInterfaceUrlString261Parse.update_forward_refs()

EndpointInterfaceUrlString262.update_forward_refs()

EndpointInterfaceUrlString262DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString262Defaults.update_forward_refs()

EndpointInterfaceUrlString262Merge.update_forward_refs()

EndpointInterfaceUrlString262Parse.update_forward_refs()

EndpointInterfaceUrlString263.update_forward_refs()

EndpointInterfaceUrlString263DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString263Defaults.update_forward_refs()

EndpointInterfaceUrlString263Merge.update_forward_refs()

EndpointInterfaceUrlString263Parse.update_forward_refs()

EndpointInterfaceUrlString264.update_forward_refs()

EndpointInterfaceUrlString264DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString264Defaults.update_forward_refs()

EndpointInterfaceUrlString264Merge.update_forward_refs()

EndpointInterfaceUrlString264Parse.update_forward_refs()

EndpointInterfaceUrlString265.update_forward_refs()

EndpointInterfaceUrlString265DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString265Defaults.update_forward_refs()

EndpointInterfaceUrlString265Merge.update_forward_refs()

EndpointInterfaceUrlString265Parse.update_forward_refs()

EndpointInterfaceUrlString266.update_forward_refs()

EndpointInterfaceUrlString266DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString266Defaults.update_forward_refs()

EndpointInterfaceUrlString266Merge.update_forward_refs()

EndpointInterfaceUrlString266Parse.update_forward_refs()

EndpointInterfaceUrlString267.update_forward_refs()

EndpointInterfaceUrlString267DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString267Defaults.update_forward_refs()

EndpointInterfaceUrlString267Merge.update_forward_refs()

EndpointInterfaceUrlString267Parse.update_forward_refs()

EndpointInterfaceUrlString268.update_forward_refs()

EndpointInterfaceUrlString268DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString268Defaults.update_forward_refs()

EndpointInterfaceUrlString268Merge.update_forward_refs()

EndpointInterfaceUrlString268Parse.update_forward_refs()

EndpointInterfaceUrlString269.update_forward_refs()

EndpointInterfaceUrlString269DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString269Defaults.update_forward_refs()

EndpointInterfaceUrlString269Merge.update_forward_refs()

EndpointInterfaceUrlString269Parse.update_forward_refs()

EndpointInterfaceUrlString26DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString26Defaults.update_forward_refs()

EndpointInterfaceUrlString26Merge.update_forward_refs()

EndpointInterfaceUrlString26Parse.update_forward_refs()

EndpointInterfaceUrlString27.update_forward_refs()

EndpointInterfaceUrlString270.update_forward_refs()

EndpointInterfaceUrlString270DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString270Defaults.update_forward_refs()

EndpointInterfaceUrlString270Merge.update_forward_refs()

EndpointInterfaceUrlString270Parse.update_forward_refs()

EndpointInterfaceUrlString271.update_forward_refs()

EndpointInterfaceUrlString271DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString271Defaults.update_forward_refs()

EndpointInterfaceUrlString271Merge.update_forward_refs()

EndpointInterfaceUrlString271Parse.update_forward_refs()

EndpointInterfaceUrlString272.update_forward_refs()

EndpointInterfaceUrlString272DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString272Defaults.update_forward_refs()

EndpointInterfaceUrlString272Merge.update_forward_refs()

EndpointInterfaceUrlString272Parse.update_forward_refs()

EndpointInterfaceUrlString273.update_forward_refs()

EndpointInterfaceUrlString273DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString273Defaults.update_forward_refs()

EndpointInterfaceUrlString273Merge.update_forward_refs()

EndpointInterfaceUrlString273Parse.update_forward_refs()

EndpointInterfaceUrlString274.update_forward_refs()

EndpointInterfaceUrlString274DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString274Defaults.update_forward_refs()

EndpointInterfaceUrlString274Merge.update_forward_refs()

EndpointInterfaceUrlString274Parse.update_forward_refs()

EndpointInterfaceUrlString275.update_forward_refs()

EndpointInterfaceUrlString275DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString275Defaults.update_forward_refs()

EndpointInterfaceUrlString275Merge.update_forward_refs()

EndpointInterfaceUrlString275Parse.update_forward_refs()

EndpointInterfaceUrlString276.update_forward_refs()

EndpointInterfaceUrlString276DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString276Defaults.update_forward_refs()

EndpointInterfaceUrlString276Merge.update_forward_refs()

EndpointInterfaceUrlString276Parse.update_forward_refs()

EndpointInterfaceUrlString277.update_forward_refs()

EndpointInterfaceUrlString277DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString277Defaults.update_forward_refs()

EndpointInterfaceUrlString277Merge.update_forward_refs()

EndpointInterfaceUrlString277Parse.update_forward_refs()

EndpointInterfaceUrlString278.update_forward_refs()

EndpointInterfaceUrlString278DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString278Defaults.update_forward_refs()

EndpointInterfaceUrlString278Merge.update_forward_refs()

EndpointInterfaceUrlString278Parse.update_forward_refs()

EndpointInterfaceUrlString279.update_forward_refs()

EndpointInterfaceUrlString279DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString279Defaults.update_forward_refs()

EndpointInterfaceUrlString279Merge.update_forward_refs()

EndpointInterfaceUrlString279Parse.update_forward_refs()

EndpointInterfaceUrlString27DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString27Defaults.update_forward_refs()

EndpointInterfaceUrlString27Merge.update_forward_refs()

EndpointInterfaceUrlString27Parse.update_forward_refs()

EndpointInterfaceUrlString28.update_forward_refs()

EndpointInterfaceUrlString280.update_forward_refs()

EndpointInterfaceUrlString280DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString280Defaults.update_forward_refs()

EndpointInterfaceUrlString280Merge.update_forward_refs()

EndpointInterfaceUrlString280Parse.update_forward_refs()

EndpointInterfaceUrlString281.update_forward_refs()

EndpointInterfaceUrlString281DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString281Defaults.update_forward_refs()

EndpointInterfaceUrlString281Merge.update_forward_refs()

EndpointInterfaceUrlString281Parse.update_forward_refs()

EndpointInterfaceUrlString282.update_forward_refs()

EndpointInterfaceUrlString282DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString282Defaults.update_forward_refs()

EndpointInterfaceUrlString282Merge.update_forward_refs()

EndpointInterfaceUrlString282Parse.update_forward_refs()

EndpointInterfaceUrlString283.update_forward_refs()

EndpointInterfaceUrlString283DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString283Defaults.update_forward_refs()

EndpointInterfaceUrlString283Merge.update_forward_refs()

EndpointInterfaceUrlString283Parse.update_forward_refs()

EndpointInterfaceUrlString284.update_forward_refs()

EndpointInterfaceUrlString284DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString284Defaults.update_forward_refs()

EndpointInterfaceUrlString284Merge.update_forward_refs()

EndpointInterfaceUrlString284Parse.update_forward_refs()

EndpointInterfaceUrlString285.update_forward_refs()

EndpointInterfaceUrlString285DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString285Defaults.update_forward_refs()

EndpointInterfaceUrlString285Merge.update_forward_refs()

EndpointInterfaceUrlString285Parse.update_forward_refs()

EndpointInterfaceUrlString286.update_forward_refs()

EndpointInterfaceUrlString286DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString286Defaults.update_forward_refs()

EndpointInterfaceUrlString286Merge.update_forward_refs()

EndpointInterfaceUrlString286Parse.update_forward_refs()

EndpointInterfaceUrlString287.update_forward_refs()

EndpointInterfaceUrlString287DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString287Defaults.update_forward_refs()

EndpointInterfaceUrlString287Merge.update_forward_refs()

EndpointInterfaceUrlString287Parse.update_forward_refs()

EndpointInterfaceUrlString288.update_forward_refs()

EndpointInterfaceUrlString288DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString288Defaults.update_forward_refs()

EndpointInterfaceUrlString288Merge.update_forward_refs()

EndpointInterfaceUrlString288Parse.update_forward_refs()

EndpointInterfaceUrlString289.update_forward_refs()

EndpointInterfaceUrlString289DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString289Defaults.update_forward_refs()

EndpointInterfaceUrlString289Merge.update_forward_refs()

EndpointInterfaceUrlString289Parse.update_forward_refs()

EndpointInterfaceUrlString28DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString28Defaults.update_forward_refs()

EndpointInterfaceUrlString28Merge.update_forward_refs()

EndpointInterfaceUrlString28Parse.update_forward_refs()

EndpointInterfaceUrlString29.update_forward_refs()

EndpointInterfaceUrlString290.update_forward_refs()

EndpointInterfaceUrlString290DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString290Defaults.update_forward_refs()

EndpointInterfaceUrlString290Merge.update_forward_refs()

EndpointInterfaceUrlString290Parse.update_forward_refs()

EndpointInterfaceUrlString291.update_forward_refs()

EndpointInterfaceUrlString291DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString291Defaults.update_forward_refs()

EndpointInterfaceUrlString291Merge.update_forward_refs()

EndpointInterfaceUrlString291Parse.update_forward_refs()

EndpointInterfaceUrlString292.update_forward_refs()

EndpointInterfaceUrlString292DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString292Defaults.update_forward_refs()

EndpointInterfaceUrlString292Merge.update_forward_refs()

EndpointInterfaceUrlString292Parse.update_forward_refs()

EndpointInterfaceUrlString293.update_forward_refs()

EndpointInterfaceUrlString293DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString293Defaults.update_forward_refs()

EndpointInterfaceUrlString293Merge.update_forward_refs()

EndpointInterfaceUrlString293Parse.update_forward_refs()

EndpointInterfaceUrlString294.update_forward_refs()

EndpointInterfaceUrlString294DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString294Defaults.update_forward_refs()

EndpointInterfaceUrlString294Merge.update_forward_refs()

EndpointInterfaceUrlString294Parse.update_forward_refs()

EndpointInterfaceUrlString295.update_forward_refs()

EndpointInterfaceUrlString295DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString295Defaults.update_forward_refs()

EndpointInterfaceUrlString295Merge.update_forward_refs()

EndpointInterfaceUrlString295Parse.update_forward_refs()

EndpointInterfaceUrlString296.update_forward_refs()

EndpointInterfaceUrlString296DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString296Defaults.update_forward_refs()

EndpointInterfaceUrlString296Merge.update_forward_refs()

EndpointInterfaceUrlString296Parse.update_forward_refs()

EndpointInterfaceUrlString297.update_forward_refs()

EndpointInterfaceUrlString297DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString297Defaults.update_forward_refs()

EndpointInterfaceUrlString297Merge.update_forward_refs()

EndpointInterfaceUrlString297Parse.update_forward_refs()

EndpointInterfaceUrlString298.update_forward_refs()

EndpointInterfaceUrlString298DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString298Defaults.update_forward_refs()

EndpointInterfaceUrlString298Merge.update_forward_refs()

EndpointInterfaceUrlString298Parse.update_forward_refs()

EndpointInterfaceUrlString299.update_forward_refs()

EndpointInterfaceUrlString299DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString299Defaults.update_forward_refs()

EndpointInterfaceUrlString299Merge.update_forward_refs()

EndpointInterfaceUrlString299Parse.update_forward_refs()

EndpointInterfaceUrlString29DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString29Defaults.update_forward_refs()

EndpointInterfaceUrlString29Merge.update_forward_refs()

EndpointInterfaceUrlString29Parse.update_forward_refs()

EndpointInterfaceUrlString2DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString2Defaults.update_forward_refs()

EndpointInterfaceUrlString2Merge.update_forward_refs()

EndpointInterfaceUrlString2Parse.update_forward_refs()

EndpointInterfaceUrlString3.update_forward_refs()

EndpointInterfaceUrlString30.update_forward_refs()

EndpointInterfaceUrlString300.update_forward_refs()

EndpointInterfaceUrlString300DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString300Defaults.update_forward_refs()

EndpointInterfaceUrlString300Merge.update_forward_refs()

EndpointInterfaceUrlString300Parse.update_forward_refs()

EndpointInterfaceUrlString301.update_forward_refs()

EndpointInterfaceUrlString301DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString301Defaults.update_forward_refs()

EndpointInterfaceUrlString301Merge.update_forward_refs()

EndpointInterfaceUrlString301Parse.update_forward_refs()

EndpointInterfaceUrlString302.update_forward_refs()

EndpointInterfaceUrlString302DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString302Defaults.update_forward_refs()

EndpointInterfaceUrlString302Merge.update_forward_refs()

EndpointInterfaceUrlString302Parse.update_forward_refs()

EndpointInterfaceUrlString303.update_forward_refs()

EndpointInterfaceUrlString303DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString303Defaults.update_forward_refs()

EndpointInterfaceUrlString303Merge.update_forward_refs()

EndpointInterfaceUrlString303Parse.update_forward_refs()

EndpointInterfaceUrlString304.update_forward_refs()

EndpointInterfaceUrlString304DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString304Defaults.update_forward_refs()

EndpointInterfaceUrlString304Merge.update_forward_refs()

EndpointInterfaceUrlString304Parse.update_forward_refs()

EndpointInterfaceUrlString305.update_forward_refs()

EndpointInterfaceUrlString305DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString305Defaults.update_forward_refs()

EndpointInterfaceUrlString305Merge.update_forward_refs()

EndpointInterfaceUrlString305Parse.update_forward_refs()

EndpointInterfaceUrlString306.update_forward_refs()

EndpointInterfaceUrlString306DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString306Defaults.update_forward_refs()

EndpointInterfaceUrlString306Merge.update_forward_refs()

EndpointInterfaceUrlString306Parse.update_forward_refs()

EndpointInterfaceUrlString307.update_forward_refs()

EndpointInterfaceUrlString307DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString307Defaults.update_forward_refs()

EndpointInterfaceUrlString307Merge.update_forward_refs()

EndpointInterfaceUrlString307Parse.update_forward_refs()

EndpointInterfaceUrlString308.update_forward_refs()

EndpointInterfaceUrlString308DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString308Defaults.update_forward_refs()

EndpointInterfaceUrlString308Merge.update_forward_refs()

EndpointInterfaceUrlString308Parse.update_forward_refs()

EndpointInterfaceUrlString309.update_forward_refs()

EndpointInterfaceUrlString309DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString309Defaults.update_forward_refs()

EndpointInterfaceUrlString309Merge.update_forward_refs()

EndpointInterfaceUrlString309Parse.update_forward_refs()

EndpointInterfaceUrlString30DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString30Defaults.update_forward_refs()

EndpointInterfaceUrlString30Merge.update_forward_refs()

EndpointInterfaceUrlString30Parse.update_forward_refs()

EndpointInterfaceUrlString31.update_forward_refs()

EndpointInterfaceUrlString310.update_forward_refs()

EndpointInterfaceUrlString310DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString310Defaults.update_forward_refs()

EndpointInterfaceUrlString310Merge.update_forward_refs()

EndpointInterfaceUrlString310Parse.update_forward_refs()

EndpointInterfaceUrlString311.update_forward_refs()

EndpointInterfaceUrlString311DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString311Defaults.update_forward_refs()

EndpointInterfaceUrlString311Merge.update_forward_refs()

EndpointInterfaceUrlString311Parse.update_forward_refs()

EndpointInterfaceUrlString312.update_forward_refs()

EndpointInterfaceUrlString312DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString312Defaults.update_forward_refs()

EndpointInterfaceUrlString312Merge.update_forward_refs()

EndpointInterfaceUrlString312Parse.update_forward_refs()

EndpointInterfaceUrlString313.update_forward_refs()

EndpointInterfaceUrlString313DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString313Defaults.update_forward_refs()

EndpointInterfaceUrlString313Merge.update_forward_refs()

EndpointInterfaceUrlString313Parse.update_forward_refs()

EndpointInterfaceUrlString314.update_forward_refs()

EndpointInterfaceUrlString314DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString314Defaults.update_forward_refs()

EndpointInterfaceUrlString314Merge.update_forward_refs()

EndpointInterfaceUrlString314Parse.update_forward_refs()

EndpointInterfaceUrlString315.update_forward_refs()

EndpointInterfaceUrlString315DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString315Defaults.update_forward_refs()

EndpointInterfaceUrlString315Merge.update_forward_refs()

EndpointInterfaceUrlString315Parse.update_forward_refs()

EndpointInterfaceUrlString316.update_forward_refs()

EndpointInterfaceUrlString316DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString316Defaults.update_forward_refs()

EndpointInterfaceUrlString316Merge.update_forward_refs()

EndpointInterfaceUrlString316Parse.update_forward_refs()

EndpointInterfaceUrlString317.update_forward_refs()

EndpointInterfaceUrlString317DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString317Defaults.update_forward_refs()

EndpointInterfaceUrlString317Merge.update_forward_refs()

EndpointInterfaceUrlString317Parse.update_forward_refs()

EndpointInterfaceUrlString318.update_forward_refs()

EndpointInterfaceUrlString318DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString318Defaults.update_forward_refs()

EndpointInterfaceUrlString318Merge.update_forward_refs()

EndpointInterfaceUrlString318Parse.update_forward_refs()

EndpointInterfaceUrlString319.update_forward_refs()

EndpointInterfaceUrlString319DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString319Defaults.update_forward_refs()

EndpointInterfaceUrlString319Merge.update_forward_refs()

EndpointInterfaceUrlString319Parse.update_forward_refs()

EndpointInterfaceUrlString31DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString31Defaults.update_forward_refs()

EndpointInterfaceUrlString31Merge.update_forward_refs()

EndpointInterfaceUrlString31Parse.update_forward_refs()

EndpointInterfaceUrlString32.update_forward_refs()

EndpointInterfaceUrlString320.update_forward_refs()

EndpointInterfaceUrlString320DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString320Defaults.update_forward_refs()

EndpointInterfaceUrlString320Merge.update_forward_refs()

EndpointInterfaceUrlString320Parse.update_forward_refs()

EndpointInterfaceUrlString321.update_forward_refs()

EndpointInterfaceUrlString321DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString321Defaults.update_forward_refs()

EndpointInterfaceUrlString321Merge.update_forward_refs()

EndpointInterfaceUrlString321Parse.update_forward_refs()

EndpointInterfaceUrlString322.update_forward_refs()

EndpointInterfaceUrlString322DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString322Defaults.update_forward_refs()

EndpointInterfaceUrlString322Merge.update_forward_refs()

EndpointInterfaceUrlString322Parse.update_forward_refs()

EndpointInterfaceUrlString323.update_forward_refs()

EndpointInterfaceUrlString323DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString323Defaults.update_forward_refs()

EndpointInterfaceUrlString323Merge.update_forward_refs()

EndpointInterfaceUrlString323Parse.update_forward_refs()

EndpointInterfaceUrlString324.update_forward_refs()

EndpointInterfaceUrlString324DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString324Defaults.update_forward_refs()

EndpointInterfaceUrlString324Merge.update_forward_refs()

EndpointInterfaceUrlString324Parse.update_forward_refs()

EndpointInterfaceUrlString325.update_forward_refs()

EndpointInterfaceUrlString325DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString325Defaults.update_forward_refs()

EndpointInterfaceUrlString325Merge.update_forward_refs()

EndpointInterfaceUrlString325Parse.update_forward_refs()

EndpointInterfaceUrlString326.update_forward_refs()

EndpointInterfaceUrlString326DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString326Defaults.update_forward_refs()

EndpointInterfaceUrlString326Merge.update_forward_refs()

EndpointInterfaceUrlString326Parse.update_forward_refs()

EndpointInterfaceUrlString327.update_forward_refs()

EndpointInterfaceUrlString327DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString327Defaults.update_forward_refs()

EndpointInterfaceUrlString327Merge.update_forward_refs()

EndpointInterfaceUrlString327Parse.update_forward_refs()

EndpointInterfaceUrlString328.update_forward_refs()

EndpointInterfaceUrlString328DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString328Defaults.update_forward_refs()

EndpointInterfaceUrlString328Merge.update_forward_refs()

EndpointInterfaceUrlString328Parse.update_forward_refs()

EndpointInterfaceUrlString329.update_forward_refs()

EndpointInterfaceUrlString329DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString329Defaults.update_forward_refs()

EndpointInterfaceUrlString329Merge.update_forward_refs()

EndpointInterfaceUrlString329Parse.update_forward_refs()

EndpointInterfaceUrlString32DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString32Defaults.update_forward_refs()

EndpointInterfaceUrlString32Merge.update_forward_refs()

EndpointInterfaceUrlString32Parse.update_forward_refs()

EndpointInterfaceUrlString33.update_forward_refs()

EndpointInterfaceUrlString330.update_forward_refs()

EndpointInterfaceUrlString330DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString330Defaults.update_forward_refs()

EndpointInterfaceUrlString330Merge.update_forward_refs()

EndpointInterfaceUrlString330Parse.update_forward_refs()

EndpointInterfaceUrlString331.update_forward_refs()

EndpointInterfaceUrlString331DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString331Defaults.update_forward_refs()

EndpointInterfaceUrlString331Merge.update_forward_refs()

EndpointInterfaceUrlString331Parse.update_forward_refs()

EndpointInterfaceUrlString332.update_forward_refs()

EndpointInterfaceUrlString332DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString332Defaults.update_forward_refs()

EndpointInterfaceUrlString332Merge.update_forward_refs()

EndpointInterfaceUrlString332Parse.update_forward_refs()

EndpointInterfaceUrlString333.update_forward_refs()

EndpointInterfaceUrlString333DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString333Defaults.update_forward_refs()

EndpointInterfaceUrlString333Merge.update_forward_refs()

EndpointInterfaceUrlString333Parse.update_forward_refs()

EndpointInterfaceUrlString334.update_forward_refs()

EndpointInterfaceUrlString334DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString334Defaults.update_forward_refs()

EndpointInterfaceUrlString334Merge.update_forward_refs()

EndpointInterfaceUrlString334Parse.update_forward_refs()

EndpointInterfaceUrlString335.update_forward_refs()

EndpointInterfaceUrlString335DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString335Defaults.update_forward_refs()

EndpointInterfaceUrlString335Merge.update_forward_refs()

EndpointInterfaceUrlString335Parse.update_forward_refs()

EndpointInterfaceUrlString336.update_forward_refs()

EndpointInterfaceUrlString336DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString336Defaults.update_forward_refs()

EndpointInterfaceUrlString336Merge.update_forward_refs()

EndpointInterfaceUrlString336Parse.update_forward_refs()

EndpointInterfaceUrlString337.update_forward_refs()

EndpointInterfaceUrlString337DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString337Defaults.update_forward_refs()

EndpointInterfaceUrlString337Merge.update_forward_refs()

EndpointInterfaceUrlString337Parse.update_forward_refs()

EndpointInterfaceUrlString338.update_forward_refs()

EndpointInterfaceUrlString338DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString338Defaults.update_forward_refs()

EndpointInterfaceUrlString338Merge.update_forward_refs()

EndpointInterfaceUrlString338Parse.update_forward_refs()

EndpointInterfaceUrlString339.update_forward_refs()

EndpointInterfaceUrlString339DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString339Defaults.update_forward_refs()

EndpointInterfaceUrlString339Merge.update_forward_refs()

EndpointInterfaceUrlString339Parse.update_forward_refs()

EndpointInterfaceUrlString33DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString33Defaults.update_forward_refs()

EndpointInterfaceUrlString33Merge.update_forward_refs()

EndpointInterfaceUrlString33Parse.update_forward_refs()

EndpointInterfaceUrlString34.update_forward_refs()

EndpointInterfaceUrlString340.update_forward_refs()

EndpointInterfaceUrlString340DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString340Defaults.update_forward_refs()

EndpointInterfaceUrlString340Merge.update_forward_refs()

EndpointInterfaceUrlString340Parse.update_forward_refs()

EndpointInterfaceUrlString341.update_forward_refs()

EndpointInterfaceUrlString341DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString341Defaults.update_forward_refs()

EndpointInterfaceUrlString341Merge.update_forward_refs()

EndpointInterfaceUrlString341Parse.update_forward_refs()

EndpointInterfaceUrlString342.update_forward_refs()

EndpointInterfaceUrlString342DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString342Defaults.update_forward_refs()

EndpointInterfaceUrlString342Merge.update_forward_refs()

EndpointInterfaceUrlString342Parse.update_forward_refs()

EndpointInterfaceUrlString343.update_forward_refs()

EndpointInterfaceUrlString343DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString343Defaults.update_forward_refs()

EndpointInterfaceUrlString343Merge.update_forward_refs()

EndpointInterfaceUrlString343Parse.update_forward_refs()

EndpointInterfaceUrlString344.update_forward_refs()

EndpointInterfaceUrlString344DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString344Defaults.update_forward_refs()

EndpointInterfaceUrlString344Merge.update_forward_refs()

EndpointInterfaceUrlString344Parse.update_forward_refs()

EndpointInterfaceUrlString345.update_forward_refs()

EndpointInterfaceUrlString345DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString345Defaults.update_forward_refs()

EndpointInterfaceUrlString345Merge.update_forward_refs()

EndpointInterfaceUrlString345Parse.update_forward_refs()

EndpointInterfaceUrlString346.update_forward_refs()

EndpointInterfaceUrlString346DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString346Defaults.update_forward_refs()

EndpointInterfaceUrlString346Merge.update_forward_refs()

EndpointInterfaceUrlString346Parse.update_forward_refs()

EndpointInterfaceUrlString347.update_forward_refs()

EndpointInterfaceUrlString347DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString347Defaults.update_forward_refs()

EndpointInterfaceUrlString347Merge.update_forward_refs()

EndpointInterfaceUrlString347Parse.update_forward_refs()

EndpointInterfaceUrlString348.update_forward_refs()

EndpointInterfaceUrlString348DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString348Defaults.update_forward_refs()

EndpointInterfaceUrlString348Merge.update_forward_refs()

EndpointInterfaceUrlString348Parse.update_forward_refs()

EndpointInterfaceUrlString349.update_forward_refs()

EndpointInterfaceUrlString349DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString349Defaults.update_forward_refs()

EndpointInterfaceUrlString349Merge.update_forward_refs()

EndpointInterfaceUrlString349Parse.update_forward_refs()

EndpointInterfaceUrlString34DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString34Defaults.update_forward_refs()

EndpointInterfaceUrlString34Merge.update_forward_refs()

EndpointInterfaceUrlString34Parse.update_forward_refs()

EndpointInterfaceUrlString35.update_forward_refs()

EndpointInterfaceUrlString350.update_forward_refs()

EndpointInterfaceUrlString350DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString350Defaults.update_forward_refs()

EndpointInterfaceUrlString350Merge.update_forward_refs()

EndpointInterfaceUrlString350Parse.update_forward_refs()

EndpointInterfaceUrlString351.update_forward_refs()

EndpointInterfaceUrlString351DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString351Defaults.update_forward_refs()

EndpointInterfaceUrlString351Merge.update_forward_refs()

EndpointInterfaceUrlString351Parse.update_forward_refs()

EndpointInterfaceUrlString352.update_forward_refs()

EndpointInterfaceUrlString352DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString352Defaults.update_forward_refs()

EndpointInterfaceUrlString352Merge.update_forward_refs()

EndpointInterfaceUrlString352Parse.update_forward_refs()

EndpointInterfaceUrlString353.update_forward_refs()

EndpointInterfaceUrlString353DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString353Defaults.update_forward_refs()

EndpointInterfaceUrlString353Merge.update_forward_refs()

EndpointInterfaceUrlString353Parse.update_forward_refs()

EndpointInterfaceUrlString354.update_forward_refs()

EndpointInterfaceUrlString354DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString354Defaults.update_forward_refs()

EndpointInterfaceUrlString354Merge.update_forward_refs()

EndpointInterfaceUrlString354Parse.update_forward_refs()

EndpointInterfaceUrlString355.update_forward_refs()

EndpointInterfaceUrlString355DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString355Defaults.update_forward_refs()

EndpointInterfaceUrlString355Merge.update_forward_refs()

EndpointInterfaceUrlString355Parse.update_forward_refs()

EndpointInterfaceUrlString356.update_forward_refs()

EndpointInterfaceUrlString356DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString356Defaults.update_forward_refs()

EndpointInterfaceUrlString356Merge.update_forward_refs()

EndpointInterfaceUrlString356Parse.update_forward_refs()

EndpointInterfaceUrlString357.update_forward_refs()

EndpointInterfaceUrlString357DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString357Defaults.update_forward_refs()

EndpointInterfaceUrlString357Merge.update_forward_refs()

EndpointInterfaceUrlString357Parse.update_forward_refs()

EndpointInterfaceUrlString358.update_forward_refs()

EndpointInterfaceUrlString358DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString358Defaults.update_forward_refs()

EndpointInterfaceUrlString358Merge.update_forward_refs()

EndpointInterfaceUrlString358Parse.update_forward_refs()

EndpointInterfaceUrlString359.update_forward_refs()

EndpointInterfaceUrlString359DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString359Defaults.update_forward_refs()

EndpointInterfaceUrlString359Merge.update_forward_refs()

EndpointInterfaceUrlString359Parse.update_forward_refs()

EndpointInterfaceUrlString35DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString35Defaults.update_forward_refs()

EndpointInterfaceUrlString35Merge.update_forward_refs()

EndpointInterfaceUrlString35Parse.update_forward_refs()

EndpointInterfaceUrlString36.update_forward_refs()

EndpointInterfaceUrlString360.update_forward_refs()

EndpointInterfaceUrlString360DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString360Defaults.update_forward_refs()

EndpointInterfaceUrlString360Merge.update_forward_refs()

EndpointInterfaceUrlString360Parse.update_forward_refs()

EndpointInterfaceUrlString361.update_forward_refs()

EndpointInterfaceUrlString361DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString361Defaults.update_forward_refs()

EndpointInterfaceUrlString361Merge.update_forward_refs()

EndpointInterfaceUrlString361Parse.update_forward_refs()

EndpointInterfaceUrlString362.update_forward_refs()

EndpointInterfaceUrlString362DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString362Defaults.update_forward_refs()

EndpointInterfaceUrlString362Merge.update_forward_refs()

EndpointInterfaceUrlString362Parse.update_forward_refs()

EndpointInterfaceUrlString363.update_forward_refs()

EndpointInterfaceUrlString363DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString363Defaults.update_forward_refs()

EndpointInterfaceUrlString363Merge.update_forward_refs()

EndpointInterfaceUrlString363Parse.update_forward_refs()

EndpointInterfaceUrlString364.update_forward_refs()

EndpointInterfaceUrlString364DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString364Defaults.update_forward_refs()

EndpointInterfaceUrlString364Merge.update_forward_refs()

EndpointInterfaceUrlString364Parse.update_forward_refs()

EndpointInterfaceUrlString365.update_forward_refs()

EndpointInterfaceUrlString365DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString365Defaults.update_forward_refs()

EndpointInterfaceUrlString365Merge.update_forward_refs()

EndpointInterfaceUrlString365Parse.update_forward_refs()

EndpointInterfaceUrlString366.update_forward_refs()

EndpointInterfaceUrlString366DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString366Defaults.update_forward_refs()

EndpointInterfaceUrlString366Merge.update_forward_refs()

EndpointInterfaceUrlString366Parse.update_forward_refs()

EndpointInterfaceUrlString367.update_forward_refs()

EndpointInterfaceUrlString367DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString367Defaults.update_forward_refs()

EndpointInterfaceUrlString367Merge.update_forward_refs()

EndpointInterfaceUrlString367Parse.update_forward_refs()

EndpointInterfaceUrlString368.update_forward_refs()

EndpointInterfaceUrlString368DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString368Defaults.update_forward_refs()

EndpointInterfaceUrlString368Merge.update_forward_refs()

EndpointInterfaceUrlString368Parse.update_forward_refs()

EndpointInterfaceUrlString369.update_forward_refs()

EndpointInterfaceUrlString369DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString369Defaults.update_forward_refs()

EndpointInterfaceUrlString369Merge.update_forward_refs()

EndpointInterfaceUrlString369Parse.update_forward_refs()

EndpointInterfaceUrlString36DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString36Defaults.update_forward_refs()

EndpointInterfaceUrlString36Merge.update_forward_refs()

EndpointInterfaceUrlString36Parse.update_forward_refs()

EndpointInterfaceUrlString37.update_forward_refs()

EndpointInterfaceUrlString370.update_forward_refs()

EndpointInterfaceUrlString370DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString370Defaults.update_forward_refs()

EndpointInterfaceUrlString370Merge.update_forward_refs()

EndpointInterfaceUrlString370Parse.update_forward_refs()

EndpointInterfaceUrlString371.update_forward_refs()

EndpointInterfaceUrlString371DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString371Defaults.update_forward_refs()

EndpointInterfaceUrlString371Merge.update_forward_refs()

EndpointInterfaceUrlString371Parse.update_forward_refs()

EndpointInterfaceUrlString372.update_forward_refs()

EndpointInterfaceUrlString372DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString372Defaults.update_forward_refs()

EndpointInterfaceUrlString372Merge.update_forward_refs()

EndpointInterfaceUrlString372Parse.update_forward_refs()

EndpointInterfaceUrlString373.update_forward_refs()

EndpointInterfaceUrlString373DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString373Defaults.update_forward_refs()

EndpointInterfaceUrlString373Merge.update_forward_refs()

EndpointInterfaceUrlString373Parse.update_forward_refs()

EndpointInterfaceUrlString374.update_forward_refs()

EndpointInterfaceUrlString374DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString374Defaults.update_forward_refs()

EndpointInterfaceUrlString374Merge.update_forward_refs()

EndpointInterfaceUrlString374Parse.update_forward_refs()

EndpointInterfaceUrlString375.update_forward_refs()

EndpointInterfaceUrlString375DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString375Defaults.update_forward_refs()

EndpointInterfaceUrlString375Merge.update_forward_refs()

EndpointInterfaceUrlString375Parse.update_forward_refs()

EndpointInterfaceUrlString376.update_forward_refs()

EndpointInterfaceUrlString376DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString376Defaults.update_forward_refs()

EndpointInterfaceUrlString376Merge.update_forward_refs()

EndpointInterfaceUrlString376Parse.update_forward_refs()

EndpointInterfaceUrlString377.update_forward_refs()

EndpointInterfaceUrlString377DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString377Defaults.update_forward_refs()

EndpointInterfaceUrlString377Merge.update_forward_refs()

EndpointInterfaceUrlString377Parse.update_forward_refs()

EndpointInterfaceUrlString378.update_forward_refs()

EndpointInterfaceUrlString378DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString378Defaults.update_forward_refs()

EndpointInterfaceUrlString378Merge.update_forward_refs()

EndpointInterfaceUrlString378Parse.update_forward_refs()

EndpointInterfaceUrlString379.update_forward_refs()

EndpointInterfaceUrlString379DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString379Defaults.update_forward_refs()

EndpointInterfaceUrlString379Merge.update_forward_refs()

EndpointInterfaceUrlString379Parse.update_forward_refs()

EndpointInterfaceUrlString37DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString37Defaults.update_forward_refs()

EndpointInterfaceUrlString37Merge.update_forward_refs()

EndpointInterfaceUrlString37Parse.update_forward_refs()

EndpointInterfaceUrlString38.update_forward_refs()

EndpointInterfaceUrlString380.update_forward_refs()

EndpointInterfaceUrlString380DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString380Defaults.update_forward_refs()

EndpointInterfaceUrlString380Merge.update_forward_refs()

EndpointInterfaceUrlString380Parse.update_forward_refs()

EndpointInterfaceUrlString381.update_forward_refs()

EndpointInterfaceUrlString381DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString381Defaults.update_forward_refs()

EndpointInterfaceUrlString381Merge.update_forward_refs()

EndpointInterfaceUrlString381Parse.update_forward_refs()

EndpointInterfaceUrlString382.update_forward_refs()

EndpointInterfaceUrlString382DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString382Defaults.update_forward_refs()

EndpointInterfaceUrlString382Merge.update_forward_refs()

EndpointInterfaceUrlString382Parse.update_forward_refs()

EndpointInterfaceUrlString383.update_forward_refs()

EndpointInterfaceUrlString383DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString383Defaults.update_forward_refs()

EndpointInterfaceUrlString383Merge.update_forward_refs()

EndpointInterfaceUrlString383Parse.update_forward_refs()

EndpointInterfaceUrlString384.update_forward_refs()

EndpointInterfaceUrlString384DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString384Defaults.update_forward_refs()

EndpointInterfaceUrlString384Merge.update_forward_refs()

EndpointInterfaceUrlString384Parse.update_forward_refs()

EndpointInterfaceUrlString385.update_forward_refs()

EndpointInterfaceUrlString385DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString385Defaults.update_forward_refs()

EndpointInterfaceUrlString385Merge.update_forward_refs()

EndpointInterfaceUrlString385Parse.update_forward_refs()

EndpointInterfaceUrlString386.update_forward_refs()

EndpointInterfaceUrlString386DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString386Defaults.update_forward_refs()

EndpointInterfaceUrlString386Merge.update_forward_refs()

EndpointInterfaceUrlString386Parse.update_forward_refs()

EndpointInterfaceUrlString387.update_forward_refs()

EndpointInterfaceUrlString387DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString387Defaults.update_forward_refs()

EndpointInterfaceUrlString387Merge.update_forward_refs()

EndpointInterfaceUrlString387Parse.update_forward_refs()

EndpointInterfaceUrlString388.update_forward_refs()

EndpointInterfaceUrlString388DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString388Defaults.update_forward_refs()

EndpointInterfaceUrlString388Merge.update_forward_refs()

EndpointInterfaceUrlString388Parse.update_forward_refs()

EndpointInterfaceUrlString389.update_forward_refs()

EndpointInterfaceUrlString389DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString389Defaults.update_forward_refs()

EndpointInterfaceUrlString389Merge.update_forward_refs()

EndpointInterfaceUrlString389Parse.update_forward_refs()

EndpointInterfaceUrlString38DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString38Defaults.update_forward_refs()

EndpointInterfaceUrlString38Merge.update_forward_refs()

EndpointInterfaceUrlString38Parse.update_forward_refs()

EndpointInterfaceUrlString39.update_forward_refs()

EndpointInterfaceUrlString390.update_forward_refs()

EndpointInterfaceUrlString390DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString390Defaults.update_forward_refs()

EndpointInterfaceUrlString390Merge.update_forward_refs()

EndpointInterfaceUrlString390Parse.update_forward_refs()

EndpointInterfaceUrlString391.update_forward_refs()

EndpointInterfaceUrlString391DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString391Defaults.update_forward_refs()

EndpointInterfaceUrlString391Merge.update_forward_refs()

EndpointInterfaceUrlString391Parse.update_forward_refs()

EndpointInterfaceUrlString392.update_forward_refs()

EndpointInterfaceUrlString392DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString392Defaults.update_forward_refs()

EndpointInterfaceUrlString392Merge.update_forward_refs()

EndpointInterfaceUrlString392Parse.update_forward_refs()

EndpointInterfaceUrlString393.update_forward_refs()

EndpointInterfaceUrlString393DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString393Defaults.update_forward_refs()

EndpointInterfaceUrlString393Merge.update_forward_refs()

EndpointInterfaceUrlString393Parse.update_forward_refs()

EndpointInterfaceUrlString394.update_forward_refs()

EndpointInterfaceUrlString394DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString394Defaults.update_forward_refs()

EndpointInterfaceUrlString394Merge.update_forward_refs()

EndpointInterfaceUrlString394Parse.update_forward_refs()

EndpointInterfaceUrlString395.update_forward_refs()

EndpointInterfaceUrlString395DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString395Defaults.update_forward_refs()

EndpointInterfaceUrlString395Merge.update_forward_refs()

EndpointInterfaceUrlString395Parse.update_forward_refs()

EndpointInterfaceUrlString396.update_forward_refs()

EndpointInterfaceUrlString396DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString396Defaults.update_forward_refs()

EndpointInterfaceUrlString396Merge.update_forward_refs()

EndpointInterfaceUrlString396Parse.update_forward_refs()

EndpointInterfaceUrlString397.update_forward_refs()

EndpointInterfaceUrlString397DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString397Defaults.update_forward_refs()

EndpointInterfaceUrlString397Merge.update_forward_refs()

EndpointInterfaceUrlString397Parse.update_forward_refs()

EndpointInterfaceUrlString398.update_forward_refs()

EndpointInterfaceUrlString398DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString398Defaults.update_forward_refs()

EndpointInterfaceUrlString398Merge.update_forward_refs()

EndpointInterfaceUrlString398Parse.update_forward_refs()

EndpointInterfaceUrlString399.update_forward_refs()

EndpointInterfaceUrlString399DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString399Defaults.update_forward_refs()

EndpointInterfaceUrlString399Merge.update_forward_refs()

EndpointInterfaceUrlString399Parse.update_forward_refs()

EndpointInterfaceUrlString39DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString39Defaults.update_forward_refs()

EndpointInterfaceUrlString39Merge.update_forward_refs()

EndpointInterfaceUrlString39Parse.update_forward_refs()

EndpointInterfaceUrlString3DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString3Defaults.update_forward_refs()

EndpointInterfaceUrlString3Merge.update_forward_refs()

EndpointInterfaceUrlString3Parse.update_forward_refs()

EndpointInterfaceUrlString4.update_forward_refs()

EndpointInterfaceUrlString40.update_forward_refs()

EndpointInterfaceUrlString400.update_forward_refs()

EndpointInterfaceUrlString400DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString400Defaults.update_forward_refs()

EndpointInterfaceUrlString400Merge.update_forward_refs()

EndpointInterfaceUrlString400Parse.update_forward_refs()

EndpointInterfaceUrlString401.update_forward_refs()

EndpointInterfaceUrlString401DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString401Defaults.update_forward_refs()

EndpointInterfaceUrlString401Merge.update_forward_refs()

EndpointInterfaceUrlString401Parse.update_forward_refs()

EndpointInterfaceUrlString402.update_forward_refs()

EndpointInterfaceUrlString402DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString402Defaults.update_forward_refs()

EndpointInterfaceUrlString402Merge.update_forward_refs()

EndpointInterfaceUrlString402Parse.update_forward_refs()

EndpointInterfaceUrlString403.update_forward_refs()

EndpointInterfaceUrlString403DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString403Defaults.update_forward_refs()

EndpointInterfaceUrlString403Merge.update_forward_refs()

EndpointInterfaceUrlString403Parse.update_forward_refs()

EndpointInterfaceUrlString404.update_forward_refs()

EndpointInterfaceUrlString404DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString404Defaults.update_forward_refs()

EndpointInterfaceUrlString404Merge.update_forward_refs()

EndpointInterfaceUrlString404Parse.update_forward_refs()

EndpointInterfaceUrlString405.update_forward_refs()

EndpointInterfaceUrlString405DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString405Defaults.update_forward_refs()

EndpointInterfaceUrlString405Merge.update_forward_refs()

EndpointInterfaceUrlString405Parse.update_forward_refs()

EndpointInterfaceUrlString406.update_forward_refs()

EndpointInterfaceUrlString406DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString406Defaults.update_forward_refs()

EndpointInterfaceUrlString406Merge.update_forward_refs()

EndpointInterfaceUrlString406Parse.update_forward_refs()

EndpointInterfaceUrlString407.update_forward_refs()

EndpointInterfaceUrlString407DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString407Defaults.update_forward_refs()

EndpointInterfaceUrlString407Merge.update_forward_refs()

EndpointInterfaceUrlString407Parse.update_forward_refs()

EndpointInterfaceUrlString408.update_forward_refs()

EndpointInterfaceUrlString408DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString408Defaults.update_forward_refs()

EndpointInterfaceUrlString408Merge.update_forward_refs()

EndpointInterfaceUrlString408Parse.update_forward_refs()

EndpointInterfaceUrlString409.update_forward_refs()

EndpointInterfaceUrlString409DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString409Defaults.update_forward_refs()

EndpointInterfaceUrlString409Merge.update_forward_refs()

EndpointInterfaceUrlString409Parse.update_forward_refs()

EndpointInterfaceUrlString40DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString40Defaults.update_forward_refs()

EndpointInterfaceUrlString40Merge.update_forward_refs()

EndpointInterfaceUrlString40Parse.update_forward_refs()

EndpointInterfaceUrlString41.update_forward_refs()

EndpointInterfaceUrlString410.update_forward_refs()

EndpointInterfaceUrlString410DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString410Defaults.update_forward_refs()

EndpointInterfaceUrlString410Merge.update_forward_refs()

EndpointInterfaceUrlString410Parse.update_forward_refs()

EndpointInterfaceUrlString411.update_forward_refs()

EndpointInterfaceUrlString411DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString411Defaults.update_forward_refs()

EndpointInterfaceUrlString411Merge.update_forward_refs()

EndpointInterfaceUrlString411Parse.update_forward_refs()

EndpointInterfaceUrlString412.update_forward_refs()

EndpointInterfaceUrlString412DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString412Defaults.update_forward_refs()

EndpointInterfaceUrlString412Merge.update_forward_refs()

EndpointInterfaceUrlString412Parse.update_forward_refs()

EndpointInterfaceUrlString413.update_forward_refs()

EndpointInterfaceUrlString413DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString413Defaults.update_forward_refs()

EndpointInterfaceUrlString413Merge.update_forward_refs()

EndpointInterfaceUrlString413Parse.update_forward_refs()

EndpointInterfaceUrlString414.update_forward_refs()

EndpointInterfaceUrlString414DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString414Defaults.update_forward_refs()

EndpointInterfaceUrlString414Merge.update_forward_refs()

EndpointInterfaceUrlString414Parse.update_forward_refs()

EndpointInterfaceUrlString415.update_forward_refs()

EndpointInterfaceUrlString415DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString415Defaults.update_forward_refs()

EndpointInterfaceUrlString415Merge.update_forward_refs()

EndpointInterfaceUrlString415Parse.update_forward_refs()

EndpointInterfaceUrlString416.update_forward_refs()

EndpointInterfaceUrlString416DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString416Defaults.update_forward_refs()

EndpointInterfaceUrlString416Merge.update_forward_refs()

EndpointInterfaceUrlString416Parse.update_forward_refs()

EndpointInterfaceUrlString417.update_forward_refs()

EndpointInterfaceUrlString417DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString417Defaults.update_forward_refs()

EndpointInterfaceUrlString417Merge.update_forward_refs()

EndpointInterfaceUrlString417Parse.update_forward_refs()

EndpointInterfaceUrlString418.update_forward_refs()

EndpointInterfaceUrlString418DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString418Defaults.update_forward_refs()

EndpointInterfaceUrlString418Merge.update_forward_refs()

EndpointInterfaceUrlString418Parse.update_forward_refs()

EndpointInterfaceUrlString419.update_forward_refs()

EndpointInterfaceUrlString419DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString419Defaults.update_forward_refs()

EndpointInterfaceUrlString419Merge.update_forward_refs()

EndpointInterfaceUrlString419Parse.update_forward_refs()

EndpointInterfaceUrlString41DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString41Defaults.update_forward_refs()

EndpointInterfaceUrlString41Merge.update_forward_refs()

EndpointInterfaceUrlString41Parse.update_forward_refs()

EndpointInterfaceUrlString42.update_forward_refs()

EndpointInterfaceUrlString420.update_forward_refs()

EndpointInterfaceUrlString420DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString420Defaults.update_forward_refs()

EndpointInterfaceUrlString420Merge.update_forward_refs()

EndpointInterfaceUrlString420Parse.update_forward_refs()

EndpointInterfaceUrlString421.update_forward_refs()

EndpointInterfaceUrlString421DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString421Defaults.update_forward_refs()

EndpointInterfaceUrlString421Merge.update_forward_refs()

EndpointInterfaceUrlString421Parse.update_forward_refs()

EndpointInterfaceUrlString422.update_forward_refs()

EndpointInterfaceUrlString422DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString422Defaults.update_forward_refs()

EndpointInterfaceUrlString422Merge.update_forward_refs()

EndpointInterfaceUrlString422Parse.update_forward_refs()

EndpointInterfaceUrlString423.update_forward_refs()

EndpointInterfaceUrlString423DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString423Defaults.update_forward_refs()

EndpointInterfaceUrlString423Merge.update_forward_refs()

EndpointInterfaceUrlString423Parse.update_forward_refs()

EndpointInterfaceUrlString424.update_forward_refs()

EndpointInterfaceUrlString424DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString424Defaults.update_forward_refs()

EndpointInterfaceUrlString424Merge.update_forward_refs()

EndpointInterfaceUrlString424Parse.update_forward_refs()

EndpointInterfaceUrlString425.update_forward_refs()

EndpointInterfaceUrlString425DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString425Defaults.update_forward_refs()

EndpointInterfaceUrlString425Merge.update_forward_refs()

EndpointInterfaceUrlString425Parse.update_forward_refs()

EndpointInterfaceUrlString426.update_forward_refs()

EndpointInterfaceUrlString426DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString426Defaults.update_forward_refs()

EndpointInterfaceUrlString426Merge.update_forward_refs()

EndpointInterfaceUrlString426Parse.update_forward_refs()

EndpointInterfaceUrlString427.update_forward_refs()

EndpointInterfaceUrlString427DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString427Defaults.update_forward_refs()

EndpointInterfaceUrlString427Merge.update_forward_refs()

EndpointInterfaceUrlString427Parse.update_forward_refs()

EndpointInterfaceUrlString428.update_forward_refs()

EndpointInterfaceUrlString428DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString428Defaults.update_forward_refs()

EndpointInterfaceUrlString428Merge.update_forward_refs()

EndpointInterfaceUrlString428Parse.update_forward_refs()

EndpointInterfaceUrlString429.update_forward_refs()

EndpointInterfaceUrlString429DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString429Defaults.update_forward_refs()

EndpointInterfaceUrlString429Merge.update_forward_refs()

EndpointInterfaceUrlString429Parse.update_forward_refs()

EndpointInterfaceUrlString42DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString42Defaults.update_forward_refs()

EndpointInterfaceUrlString42Merge.update_forward_refs()

EndpointInterfaceUrlString42Parse.update_forward_refs()

EndpointInterfaceUrlString43.update_forward_refs()

EndpointInterfaceUrlString430.update_forward_refs()

EndpointInterfaceUrlString430DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString430Defaults.update_forward_refs()

EndpointInterfaceUrlString430Merge.update_forward_refs()

EndpointInterfaceUrlString430Parse.update_forward_refs()

EndpointInterfaceUrlString431.update_forward_refs()

EndpointInterfaceUrlString431DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString431Defaults.update_forward_refs()

EndpointInterfaceUrlString431Merge.update_forward_refs()

EndpointInterfaceUrlString431Parse.update_forward_refs()

EndpointInterfaceUrlString432.update_forward_refs()

EndpointInterfaceUrlString432DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString432Defaults.update_forward_refs()

EndpointInterfaceUrlString432Merge.update_forward_refs()

EndpointInterfaceUrlString432Parse.update_forward_refs()

EndpointInterfaceUrlString433.update_forward_refs()

EndpointInterfaceUrlString433DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString433Defaults.update_forward_refs()

EndpointInterfaceUrlString433Merge.update_forward_refs()

EndpointInterfaceUrlString433Parse.update_forward_refs()

EndpointInterfaceUrlString434.update_forward_refs()

EndpointInterfaceUrlString434DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString434Defaults.update_forward_refs()

EndpointInterfaceUrlString434Merge.update_forward_refs()

EndpointInterfaceUrlString434Parse.update_forward_refs()

EndpointInterfaceUrlString435.update_forward_refs()

EndpointInterfaceUrlString435DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString435Defaults.update_forward_refs()

EndpointInterfaceUrlString435Merge.update_forward_refs()

EndpointInterfaceUrlString435Parse.update_forward_refs()

EndpointInterfaceUrlString436.update_forward_refs()

EndpointInterfaceUrlString436DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString436Defaults.update_forward_refs()

EndpointInterfaceUrlString436Merge.update_forward_refs()

EndpointInterfaceUrlString436Parse.update_forward_refs()

EndpointInterfaceUrlString437.update_forward_refs()

EndpointInterfaceUrlString437DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString437Defaults.update_forward_refs()

EndpointInterfaceUrlString437Merge.update_forward_refs()

EndpointInterfaceUrlString437Parse.update_forward_refs()

EndpointInterfaceUrlString438.update_forward_refs()

EndpointInterfaceUrlString438DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString438Defaults.update_forward_refs()

EndpointInterfaceUrlString438Merge.update_forward_refs()

EndpointInterfaceUrlString438Parse.update_forward_refs()

EndpointInterfaceUrlString439.update_forward_refs()

EndpointInterfaceUrlString439DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString439Defaults.update_forward_refs()

EndpointInterfaceUrlString439Merge.update_forward_refs()

EndpointInterfaceUrlString439Parse.update_forward_refs()

EndpointInterfaceUrlString43DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString43Defaults.update_forward_refs()

EndpointInterfaceUrlString43Merge.update_forward_refs()

EndpointInterfaceUrlString43Parse.update_forward_refs()

EndpointInterfaceUrlString44.update_forward_refs()

EndpointInterfaceUrlString440.update_forward_refs()

EndpointInterfaceUrlString440DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString440Defaults.update_forward_refs()

EndpointInterfaceUrlString440Merge.update_forward_refs()

EndpointInterfaceUrlString440Parse.update_forward_refs()

EndpointInterfaceUrlString441.update_forward_refs()

EndpointInterfaceUrlString441DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString441Defaults.update_forward_refs()

EndpointInterfaceUrlString441Merge.update_forward_refs()

EndpointInterfaceUrlString441Parse.update_forward_refs()

EndpointInterfaceUrlString442.update_forward_refs()

EndpointInterfaceUrlString442DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString442Defaults.update_forward_refs()

EndpointInterfaceUrlString442Merge.update_forward_refs()

EndpointInterfaceUrlString442Parse.update_forward_refs()

EndpointInterfaceUrlString443.update_forward_refs()

EndpointInterfaceUrlString443DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString443Defaults.update_forward_refs()

EndpointInterfaceUrlString443Merge.update_forward_refs()

EndpointInterfaceUrlString443Parse.update_forward_refs()

EndpointInterfaceUrlString444.update_forward_refs()

EndpointInterfaceUrlString444DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString444Defaults.update_forward_refs()

EndpointInterfaceUrlString444Merge.update_forward_refs()

EndpointInterfaceUrlString444Parse.update_forward_refs()

EndpointInterfaceUrlString445.update_forward_refs()

EndpointInterfaceUrlString445DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString445Defaults.update_forward_refs()

EndpointInterfaceUrlString445Merge.update_forward_refs()

EndpointInterfaceUrlString445Parse.update_forward_refs()

EndpointInterfaceUrlString446.update_forward_refs()

EndpointInterfaceUrlString446DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString446Defaults.update_forward_refs()

EndpointInterfaceUrlString446Merge.update_forward_refs()

EndpointInterfaceUrlString446Parse.update_forward_refs()

EndpointInterfaceUrlString447.update_forward_refs()

EndpointInterfaceUrlString447DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString447Defaults.update_forward_refs()

EndpointInterfaceUrlString447Merge.update_forward_refs()

EndpointInterfaceUrlString447Parse.update_forward_refs()

EndpointInterfaceUrlString448.update_forward_refs()

EndpointInterfaceUrlString448DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString448Defaults.update_forward_refs()

EndpointInterfaceUrlString448Merge.update_forward_refs()

EndpointInterfaceUrlString448Parse.update_forward_refs()

EndpointInterfaceUrlString449.update_forward_refs()

EndpointInterfaceUrlString449DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString449Defaults.update_forward_refs()

EndpointInterfaceUrlString449Merge.update_forward_refs()

EndpointInterfaceUrlString449Parse.update_forward_refs()

EndpointInterfaceUrlString44DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString44Defaults.update_forward_refs()

EndpointInterfaceUrlString44Merge.update_forward_refs()

EndpointInterfaceUrlString44Parse.update_forward_refs()

EndpointInterfaceUrlString45.update_forward_refs()

EndpointInterfaceUrlString450.update_forward_refs()

EndpointInterfaceUrlString450DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString450Defaults.update_forward_refs()

EndpointInterfaceUrlString450Merge.update_forward_refs()

EndpointInterfaceUrlString450Parse.update_forward_refs()

EndpointInterfaceUrlString451.update_forward_refs()

EndpointInterfaceUrlString451DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString451Defaults.update_forward_refs()

EndpointInterfaceUrlString451Merge.update_forward_refs()

EndpointInterfaceUrlString451Parse.update_forward_refs()

EndpointInterfaceUrlString452.update_forward_refs()

EndpointInterfaceUrlString452DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString452Defaults.update_forward_refs()

EndpointInterfaceUrlString452Merge.update_forward_refs()

EndpointInterfaceUrlString452Parse.update_forward_refs()

EndpointInterfaceUrlString453.update_forward_refs()

EndpointInterfaceUrlString453DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString453Defaults.update_forward_refs()

EndpointInterfaceUrlString453Merge.update_forward_refs()

EndpointInterfaceUrlString453Parse.update_forward_refs()

EndpointInterfaceUrlString454.update_forward_refs()

EndpointInterfaceUrlString454DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString454Defaults.update_forward_refs()

EndpointInterfaceUrlString454Merge.update_forward_refs()

EndpointInterfaceUrlString454Parse.update_forward_refs()

EndpointInterfaceUrlString455.update_forward_refs()

EndpointInterfaceUrlString455DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString455Defaults.update_forward_refs()

EndpointInterfaceUrlString455Merge.update_forward_refs()

EndpointInterfaceUrlString455Parse.update_forward_refs()

EndpointInterfaceUrlString456.update_forward_refs()

EndpointInterfaceUrlString456DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString456Defaults.update_forward_refs()

EndpointInterfaceUrlString456Merge.update_forward_refs()

EndpointInterfaceUrlString456Parse.update_forward_refs()

EndpointInterfaceUrlString457.update_forward_refs()

EndpointInterfaceUrlString457DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString457Defaults.update_forward_refs()

EndpointInterfaceUrlString457Merge.update_forward_refs()

EndpointInterfaceUrlString457Parse.update_forward_refs()

EndpointInterfaceUrlString458.update_forward_refs()

EndpointInterfaceUrlString458DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString458Defaults.update_forward_refs()

EndpointInterfaceUrlString458Merge.update_forward_refs()

EndpointInterfaceUrlString458Parse.update_forward_refs()

EndpointInterfaceUrlString459.update_forward_refs()

EndpointInterfaceUrlString459DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString459Defaults.update_forward_refs()

EndpointInterfaceUrlString459Merge.update_forward_refs()

EndpointInterfaceUrlString459Parse.update_forward_refs()

EndpointInterfaceUrlString45DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString45Defaults.update_forward_refs()

EndpointInterfaceUrlString45Merge.update_forward_refs()

EndpointInterfaceUrlString45Parse.update_forward_refs()

EndpointInterfaceUrlString46.update_forward_refs()

EndpointInterfaceUrlString460.update_forward_refs()

EndpointInterfaceUrlString460DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString460Defaults.update_forward_refs()

EndpointInterfaceUrlString460Merge.update_forward_refs()

EndpointInterfaceUrlString460Parse.update_forward_refs()

EndpointInterfaceUrlString461.update_forward_refs()

EndpointInterfaceUrlString461DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString461Defaults.update_forward_refs()

EndpointInterfaceUrlString461Merge.update_forward_refs()

EndpointInterfaceUrlString461Parse.update_forward_refs()

EndpointInterfaceUrlString462.update_forward_refs()

EndpointInterfaceUrlString462DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString462Defaults.update_forward_refs()

EndpointInterfaceUrlString462Merge.update_forward_refs()

EndpointInterfaceUrlString462Parse.update_forward_refs()

EndpointInterfaceUrlString463.update_forward_refs()

EndpointInterfaceUrlString463DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString463Defaults.update_forward_refs()

EndpointInterfaceUrlString463Merge.update_forward_refs()

EndpointInterfaceUrlString463Parse.update_forward_refs()

EndpointInterfaceUrlString464.update_forward_refs()

EndpointInterfaceUrlString464DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString464Defaults.update_forward_refs()

EndpointInterfaceUrlString464Merge.update_forward_refs()

EndpointInterfaceUrlString464Parse.update_forward_refs()

EndpointInterfaceUrlString465.update_forward_refs()

EndpointInterfaceUrlString465DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString465Defaults.update_forward_refs()

EndpointInterfaceUrlString465Merge.update_forward_refs()

EndpointInterfaceUrlString465Parse.update_forward_refs()

EndpointInterfaceUrlString466.update_forward_refs()

EndpointInterfaceUrlString466DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString466Defaults.update_forward_refs()

EndpointInterfaceUrlString466Merge.update_forward_refs()

EndpointInterfaceUrlString466Parse.update_forward_refs()

EndpointInterfaceUrlString467.update_forward_refs()

EndpointInterfaceUrlString467DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString467Defaults.update_forward_refs()

EndpointInterfaceUrlString467Merge.update_forward_refs()

EndpointInterfaceUrlString467Parse.update_forward_refs()

EndpointInterfaceUrlString468.update_forward_refs()

EndpointInterfaceUrlString468DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString468Defaults.update_forward_refs()

EndpointInterfaceUrlString468Merge.update_forward_refs()

EndpointInterfaceUrlString468Parse.update_forward_refs()

EndpointInterfaceUrlString469.update_forward_refs()

EndpointInterfaceUrlString469DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString469Defaults.update_forward_refs()

EndpointInterfaceUrlString469Merge.update_forward_refs()

EndpointInterfaceUrlString469Parse.update_forward_refs()

EndpointInterfaceUrlString46DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString46Defaults.update_forward_refs()

EndpointInterfaceUrlString46Merge.update_forward_refs()

EndpointInterfaceUrlString46Parse.update_forward_refs()

EndpointInterfaceUrlString47.update_forward_refs()

EndpointInterfaceUrlString470.update_forward_refs()

EndpointInterfaceUrlString470DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString470Defaults.update_forward_refs()

EndpointInterfaceUrlString470Merge.update_forward_refs()

EndpointInterfaceUrlString470Parse.update_forward_refs()

EndpointInterfaceUrlString471.update_forward_refs()

EndpointInterfaceUrlString471DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString471Defaults.update_forward_refs()

EndpointInterfaceUrlString471Merge.update_forward_refs()

EndpointInterfaceUrlString471Parse.update_forward_refs()

EndpointInterfaceUrlString472.update_forward_refs()

EndpointInterfaceUrlString472DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString472Defaults.update_forward_refs()

EndpointInterfaceUrlString472Merge.update_forward_refs()

EndpointInterfaceUrlString472Parse.update_forward_refs()

EndpointInterfaceUrlString473.update_forward_refs()

EndpointInterfaceUrlString473DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString473Defaults.update_forward_refs()

EndpointInterfaceUrlString473Merge.update_forward_refs()

EndpointInterfaceUrlString473Parse.update_forward_refs()

EndpointInterfaceUrlString474.update_forward_refs()

EndpointInterfaceUrlString474DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString474Defaults.update_forward_refs()

EndpointInterfaceUrlString474Merge.update_forward_refs()

EndpointInterfaceUrlString474Parse.update_forward_refs()

EndpointInterfaceUrlString475.update_forward_refs()

EndpointInterfaceUrlString475DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString475Defaults.update_forward_refs()

EndpointInterfaceUrlString475Merge.update_forward_refs()

EndpointInterfaceUrlString475Parse.update_forward_refs()

EndpointInterfaceUrlString476.update_forward_refs()

EndpointInterfaceUrlString476DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString476Defaults.update_forward_refs()

EndpointInterfaceUrlString476Merge.update_forward_refs()

EndpointInterfaceUrlString476Parse.update_forward_refs()

EndpointInterfaceUrlString477.update_forward_refs()

EndpointInterfaceUrlString477DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString477Defaults.update_forward_refs()

EndpointInterfaceUrlString477Merge.update_forward_refs()

EndpointInterfaceUrlString477Parse.update_forward_refs()

EndpointInterfaceUrlString478.update_forward_refs()

EndpointInterfaceUrlString478DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString478Defaults.update_forward_refs()

EndpointInterfaceUrlString478Merge.update_forward_refs()

EndpointInterfaceUrlString478Parse.update_forward_refs()

EndpointInterfaceUrlString479.update_forward_refs()

EndpointInterfaceUrlString479DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString479Defaults.update_forward_refs()

EndpointInterfaceUrlString479Merge.update_forward_refs()

EndpointInterfaceUrlString479Parse.update_forward_refs()

EndpointInterfaceUrlString47DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString47Defaults.update_forward_refs()

EndpointInterfaceUrlString47Merge.update_forward_refs()

EndpointInterfaceUrlString47Parse.update_forward_refs()

EndpointInterfaceUrlString48.update_forward_refs()

EndpointInterfaceUrlString480.update_forward_refs()

EndpointInterfaceUrlString480DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString480Defaults.update_forward_refs()

EndpointInterfaceUrlString480Merge.update_forward_refs()

EndpointInterfaceUrlString480Parse.update_forward_refs()

EndpointInterfaceUrlString481.update_forward_refs()

EndpointInterfaceUrlString481DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString481Defaults.update_forward_refs()

EndpointInterfaceUrlString481Merge.update_forward_refs()

EndpointInterfaceUrlString481Parse.update_forward_refs()

EndpointInterfaceUrlString482.update_forward_refs()

EndpointInterfaceUrlString482DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString482Defaults.update_forward_refs()

EndpointInterfaceUrlString482Merge.update_forward_refs()

EndpointInterfaceUrlString482Parse.update_forward_refs()

EndpointInterfaceUrlString483.update_forward_refs()

EndpointInterfaceUrlString483DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString483Defaults.update_forward_refs()

EndpointInterfaceUrlString483Merge.update_forward_refs()

EndpointInterfaceUrlString483Parse.update_forward_refs()

EndpointInterfaceUrlString484.update_forward_refs()

EndpointInterfaceUrlString484DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString484Defaults.update_forward_refs()

EndpointInterfaceUrlString484Merge.update_forward_refs()

EndpointInterfaceUrlString484Parse.update_forward_refs()

EndpointInterfaceUrlString485.update_forward_refs()

EndpointInterfaceUrlString485DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString485Defaults.update_forward_refs()

EndpointInterfaceUrlString485Merge.update_forward_refs()

EndpointInterfaceUrlString485Parse.update_forward_refs()

EndpointInterfaceUrlString486.update_forward_refs()

EndpointInterfaceUrlString486DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString486Defaults.update_forward_refs()

EndpointInterfaceUrlString486Merge.update_forward_refs()

EndpointInterfaceUrlString486Parse.update_forward_refs()

EndpointInterfaceUrlString487.update_forward_refs()

EndpointInterfaceUrlString487DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString487Defaults.update_forward_refs()

EndpointInterfaceUrlString487Merge.update_forward_refs()

EndpointInterfaceUrlString487Parse.update_forward_refs()

EndpointInterfaceUrlString488.update_forward_refs()

EndpointInterfaceUrlString488DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString488Defaults.update_forward_refs()

EndpointInterfaceUrlString488Merge.update_forward_refs()

EndpointInterfaceUrlString488Parse.update_forward_refs()

EndpointInterfaceUrlString489.update_forward_refs()

EndpointInterfaceUrlString489DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString489Defaults.update_forward_refs()

EndpointInterfaceUrlString489Merge.update_forward_refs()

EndpointInterfaceUrlString489Parse.update_forward_refs()

EndpointInterfaceUrlString48DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString48Defaults.update_forward_refs()

EndpointInterfaceUrlString48Merge.update_forward_refs()

EndpointInterfaceUrlString48Parse.update_forward_refs()

EndpointInterfaceUrlString49.update_forward_refs()

EndpointInterfaceUrlString490.update_forward_refs()

EndpointInterfaceUrlString490DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString490Defaults.update_forward_refs()

EndpointInterfaceUrlString490Merge.update_forward_refs()

EndpointInterfaceUrlString490Parse.update_forward_refs()

EndpointInterfaceUrlString491.update_forward_refs()

EndpointInterfaceUrlString491DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString491Defaults.update_forward_refs()

EndpointInterfaceUrlString491Merge.update_forward_refs()

EndpointInterfaceUrlString491Parse.update_forward_refs()

EndpointInterfaceUrlString492.update_forward_refs()

EndpointInterfaceUrlString492DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString492Defaults.update_forward_refs()

EndpointInterfaceUrlString492Merge.update_forward_refs()

EndpointInterfaceUrlString492Parse.update_forward_refs()

EndpointInterfaceUrlString493.update_forward_refs()

EndpointInterfaceUrlString493DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString493Defaults.update_forward_refs()

EndpointInterfaceUrlString493Merge.update_forward_refs()

EndpointInterfaceUrlString493Parse.update_forward_refs()

EndpointInterfaceUrlString494.update_forward_refs()

EndpointInterfaceUrlString494DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString494Defaults.update_forward_refs()

EndpointInterfaceUrlString494Merge.update_forward_refs()

EndpointInterfaceUrlString494Parse.update_forward_refs()

EndpointInterfaceUrlString495.update_forward_refs()

EndpointInterfaceUrlString495DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString495Defaults.update_forward_refs()

EndpointInterfaceUrlString495Merge.update_forward_refs()

EndpointInterfaceUrlString495Parse.update_forward_refs()

EndpointInterfaceUrlString496.update_forward_refs()

EndpointInterfaceUrlString496DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString496Defaults.update_forward_refs()

EndpointInterfaceUrlString496Merge.update_forward_refs()

EndpointInterfaceUrlString496Parse.update_forward_refs()

EndpointInterfaceUrlString497.update_forward_refs()

EndpointInterfaceUrlString497DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString497Defaults.update_forward_refs()

EndpointInterfaceUrlString497Merge.update_forward_refs()

EndpointInterfaceUrlString497Parse.update_forward_refs()

EndpointInterfaceUrlString498.update_forward_refs()

EndpointInterfaceUrlString498DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString498Defaults.update_forward_refs()

EndpointInterfaceUrlString498Merge.update_forward_refs()

EndpointInterfaceUrlString498Parse.update_forward_refs()

EndpointInterfaceUrlString499.update_forward_refs()

EndpointInterfaceUrlString499DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString499Defaults.update_forward_refs()

EndpointInterfaceUrlString499Merge.update_forward_refs()

EndpointInterfaceUrlString499Parse.update_forward_refs()

EndpointInterfaceUrlString49DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString49Defaults.update_forward_refs()

EndpointInterfaceUrlString49Merge.update_forward_refs()

EndpointInterfaceUrlString49Parse.update_forward_refs()

EndpointInterfaceUrlString4DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString4Defaults.update_forward_refs()

EndpointInterfaceUrlString4Merge.update_forward_refs()

EndpointInterfaceUrlString4Parse.update_forward_refs()

EndpointInterfaceUrlString5.update_forward_refs()

EndpointInterfaceUrlString50.update_forward_refs()

EndpointInterfaceUrlString500.update_forward_refs()

EndpointInterfaceUrlString500DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString500Defaults.update_forward_refs()

EndpointInterfaceUrlString500Merge.update_forward_refs()

EndpointInterfaceUrlString500Parse.update_forward_refs()

EndpointInterfaceUrlString501.update_forward_refs()

EndpointInterfaceUrlString501DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString501Defaults.update_forward_refs()

EndpointInterfaceUrlString501Merge.update_forward_refs()

EndpointInterfaceUrlString501Parse.update_forward_refs()

EndpointInterfaceUrlString502.update_forward_refs()

EndpointInterfaceUrlString502DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString502Defaults.update_forward_refs()

EndpointInterfaceUrlString502Merge.update_forward_refs()

EndpointInterfaceUrlString502Parse.update_forward_refs()

EndpointInterfaceUrlString503.update_forward_refs()

EndpointInterfaceUrlString503DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString503Defaults.update_forward_refs()

EndpointInterfaceUrlString503Merge.update_forward_refs()

EndpointInterfaceUrlString503Parse.update_forward_refs()

EndpointInterfaceUrlString504.update_forward_refs()

EndpointInterfaceUrlString504DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString504Defaults.update_forward_refs()

EndpointInterfaceUrlString504Merge.update_forward_refs()

EndpointInterfaceUrlString504Parse.update_forward_refs()

EndpointInterfaceUrlString505.update_forward_refs()

EndpointInterfaceUrlString505DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString505Defaults.update_forward_refs()

EndpointInterfaceUrlString505Merge.update_forward_refs()

EndpointInterfaceUrlString505Parse.update_forward_refs()

EndpointInterfaceUrlString506.update_forward_refs()

EndpointInterfaceUrlString506DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString506Defaults.update_forward_refs()

EndpointInterfaceUrlString506Merge.update_forward_refs()

EndpointInterfaceUrlString506Parse.update_forward_refs()

EndpointInterfaceUrlString507.update_forward_refs()

EndpointInterfaceUrlString507DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString507Defaults.update_forward_refs()

EndpointInterfaceUrlString507Merge.update_forward_refs()

EndpointInterfaceUrlString507Parse.update_forward_refs()

EndpointInterfaceUrlString508.update_forward_refs()

EndpointInterfaceUrlString508DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString508Defaults.update_forward_refs()

EndpointInterfaceUrlString508Merge.update_forward_refs()

EndpointInterfaceUrlString508Parse.update_forward_refs()

EndpointInterfaceUrlString509.update_forward_refs()

EndpointInterfaceUrlString509DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString509Defaults.update_forward_refs()

EndpointInterfaceUrlString509Merge.update_forward_refs()

EndpointInterfaceUrlString509Parse.update_forward_refs()

EndpointInterfaceUrlString50DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString50Defaults.update_forward_refs()

EndpointInterfaceUrlString50Merge.update_forward_refs()

EndpointInterfaceUrlString50Parse.update_forward_refs()

EndpointInterfaceUrlString51.update_forward_refs()

EndpointInterfaceUrlString510.update_forward_refs()

EndpointInterfaceUrlString510DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString510Defaults.update_forward_refs()

EndpointInterfaceUrlString510Merge.update_forward_refs()

EndpointInterfaceUrlString510Parse.update_forward_refs()

EndpointInterfaceUrlString511.update_forward_refs()

EndpointInterfaceUrlString511DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString511Defaults.update_forward_refs()

EndpointInterfaceUrlString511Merge.update_forward_refs()

EndpointInterfaceUrlString511Parse.update_forward_refs()

EndpointInterfaceUrlString512.update_forward_refs()

EndpointInterfaceUrlString512DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString512Defaults.update_forward_refs()

EndpointInterfaceUrlString512Merge.update_forward_refs()

EndpointInterfaceUrlString512Parse.update_forward_refs()

EndpointInterfaceUrlString513.update_forward_refs()

EndpointInterfaceUrlString513DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString513Defaults.update_forward_refs()

EndpointInterfaceUrlString513Merge.update_forward_refs()

EndpointInterfaceUrlString513Parse.update_forward_refs()

EndpointInterfaceUrlString514.update_forward_refs()

EndpointInterfaceUrlString514DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString514Defaults.update_forward_refs()

EndpointInterfaceUrlString514Merge.update_forward_refs()

EndpointInterfaceUrlString514Parse.update_forward_refs()

EndpointInterfaceUrlString515.update_forward_refs()

EndpointInterfaceUrlString515DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString515Defaults.update_forward_refs()

EndpointInterfaceUrlString515Merge.update_forward_refs()

EndpointInterfaceUrlString515Parse.update_forward_refs()

EndpointInterfaceUrlString516.update_forward_refs()

EndpointInterfaceUrlString516DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString516Defaults.update_forward_refs()

EndpointInterfaceUrlString516Merge.update_forward_refs()

EndpointInterfaceUrlString516Parse.update_forward_refs()

EndpointInterfaceUrlString517.update_forward_refs()

EndpointInterfaceUrlString517DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString517Defaults.update_forward_refs()

EndpointInterfaceUrlString517Merge.update_forward_refs()

EndpointInterfaceUrlString517Parse.update_forward_refs()

EndpointInterfaceUrlString518.update_forward_refs()

EndpointInterfaceUrlString518DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString518Defaults.update_forward_refs()

EndpointInterfaceUrlString518Merge.update_forward_refs()

EndpointInterfaceUrlString518Parse.update_forward_refs()

EndpointInterfaceUrlString519.update_forward_refs()

EndpointInterfaceUrlString519DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString519Defaults.update_forward_refs()

EndpointInterfaceUrlString519Merge.update_forward_refs()

EndpointInterfaceUrlString519Parse.update_forward_refs()

EndpointInterfaceUrlString51DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString51Defaults.update_forward_refs()

EndpointInterfaceUrlString51Merge.update_forward_refs()

EndpointInterfaceUrlString51Parse.update_forward_refs()

EndpointInterfaceUrlString52.update_forward_refs()

EndpointInterfaceUrlString520.update_forward_refs()

EndpointInterfaceUrlString520DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString520Defaults.update_forward_refs()

EndpointInterfaceUrlString520Merge.update_forward_refs()

EndpointInterfaceUrlString520Parse.update_forward_refs()

EndpointInterfaceUrlString521.update_forward_refs()

EndpointInterfaceUrlString521DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString521Defaults.update_forward_refs()

EndpointInterfaceUrlString521Merge.update_forward_refs()

EndpointInterfaceUrlString521Parse.update_forward_refs()

EndpointInterfaceUrlString522.update_forward_refs()

EndpointInterfaceUrlString522DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString522Defaults.update_forward_refs()

EndpointInterfaceUrlString522Merge.update_forward_refs()

EndpointInterfaceUrlString522Parse.update_forward_refs()

EndpointInterfaceUrlString523.update_forward_refs()

EndpointInterfaceUrlString523DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString523Defaults.update_forward_refs()

EndpointInterfaceUrlString523Merge.update_forward_refs()

EndpointInterfaceUrlString523Parse.update_forward_refs()

EndpointInterfaceUrlString524.update_forward_refs()

EndpointInterfaceUrlString524DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString524Defaults.update_forward_refs()

EndpointInterfaceUrlString524Merge.update_forward_refs()

EndpointInterfaceUrlString524Parse.update_forward_refs()

EndpointInterfaceUrlString525.update_forward_refs()

EndpointInterfaceUrlString525DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString525Defaults.update_forward_refs()

EndpointInterfaceUrlString525Merge.update_forward_refs()

EndpointInterfaceUrlString525Parse.update_forward_refs()

EndpointInterfaceUrlString526.update_forward_refs()

EndpointInterfaceUrlString526DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString526Defaults.update_forward_refs()

EndpointInterfaceUrlString526Merge.update_forward_refs()

EndpointInterfaceUrlString526Parse.update_forward_refs()

EndpointInterfaceUrlString527.update_forward_refs()

EndpointInterfaceUrlString527DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString527Defaults.update_forward_refs()

EndpointInterfaceUrlString527Merge.update_forward_refs()

EndpointInterfaceUrlString527Parse.update_forward_refs()

EndpointInterfaceUrlString528.update_forward_refs()

EndpointInterfaceUrlString528DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString528Defaults.update_forward_refs()

EndpointInterfaceUrlString528Merge.update_forward_refs()

EndpointInterfaceUrlString528Parse.update_forward_refs()

EndpointInterfaceUrlString529.update_forward_refs()

EndpointInterfaceUrlString529DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString529Defaults.update_forward_refs()

EndpointInterfaceUrlString529Merge.update_forward_refs()

EndpointInterfaceUrlString529Parse.update_forward_refs()

EndpointInterfaceUrlString52DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString52Defaults.update_forward_refs()

EndpointInterfaceUrlString52Merge.update_forward_refs()

EndpointInterfaceUrlString52Parse.update_forward_refs()

EndpointInterfaceUrlString53.update_forward_refs()

EndpointInterfaceUrlString530.update_forward_refs()

EndpointInterfaceUrlString530DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString530Defaults.update_forward_refs()

EndpointInterfaceUrlString530Merge.update_forward_refs()

EndpointInterfaceUrlString530Parse.update_forward_refs()

EndpointInterfaceUrlString531.update_forward_refs()

EndpointInterfaceUrlString531DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString531Defaults.update_forward_refs()

EndpointInterfaceUrlString531Merge.update_forward_refs()

EndpointInterfaceUrlString531Parse.update_forward_refs()

EndpointInterfaceUrlString532.update_forward_refs()

EndpointInterfaceUrlString532DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString532Defaults.update_forward_refs()

EndpointInterfaceUrlString532Merge.update_forward_refs()

EndpointInterfaceUrlString532Parse.update_forward_refs()

EndpointInterfaceUrlString533.update_forward_refs()

EndpointInterfaceUrlString533DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString533Defaults.update_forward_refs()

EndpointInterfaceUrlString533Merge.update_forward_refs()

EndpointInterfaceUrlString533Parse.update_forward_refs()

EndpointInterfaceUrlString534.update_forward_refs()

EndpointInterfaceUrlString534DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString534Defaults.update_forward_refs()

EndpointInterfaceUrlString534Merge.update_forward_refs()

EndpointInterfaceUrlString534Parse.update_forward_refs()

EndpointInterfaceUrlString535.update_forward_refs()

EndpointInterfaceUrlString535DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString535Defaults.update_forward_refs()

EndpointInterfaceUrlString535Merge.update_forward_refs()

EndpointInterfaceUrlString535Parse.update_forward_refs()

EndpointInterfaceUrlString536.update_forward_refs()

EndpointInterfaceUrlString536DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString536Defaults.update_forward_refs()

EndpointInterfaceUrlString536Merge.update_forward_refs()

EndpointInterfaceUrlString536Parse.update_forward_refs()

EndpointInterfaceUrlString537.update_forward_refs()

EndpointInterfaceUrlString537DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString537Defaults.update_forward_refs()

EndpointInterfaceUrlString537Merge.update_forward_refs()

EndpointInterfaceUrlString537Parse.update_forward_refs()

EndpointInterfaceUrlString538.update_forward_refs()

EndpointInterfaceUrlString538DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString538Defaults.update_forward_refs()

EndpointInterfaceUrlString538Merge.update_forward_refs()

EndpointInterfaceUrlString538Parse.update_forward_refs()

EndpointInterfaceUrlString539.update_forward_refs()

EndpointInterfaceUrlString539DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString539Defaults.update_forward_refs()

EndpointInterfaceUrlString539Merge.update_forward_refs()

EndpointInterfaceUrlString539Parse.update_forward_refs()

EndpointInterfaceUrlString53DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString53Defaults.update_forward_refs()

EndpointInterfaceUrlString53Merge.update_forward_refs()

EndpointInterfaceUrlString53Parse.update_forward_refs()

EndpointInterfaceUrlString54.update_forward_refs()

EndpointInterfaceUrlString540.update_forward_refs()

EndpointInterfaceUrlString540DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString540Defaults.update_forward_refs()

EndpointInterfaceUrlString540Merge.update_forward_refs()

EndpointInterfaceUrlString540Parse.update_forward_refs()

EndpointInterfaceUrlString541.update_forward_refs()

EndpointInterfaceUrlString541DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString541Defaults.update_forward_refs()

EndpointInterfaceUrlString541Merge.update_forward_refs()

EndpointInterfaceUrlString541Parse.update_forward_refs()

EndpointInterfaceUrlString542.update_forward_refs()

EndpointInterfaceUrlString542DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString542Defaults.update_forward_refs()

EndpointInterfaceUrlString542Merge.update_forward_refs()

EndpointInterfaceUrlString542Parse.update_forward_refs()

EndpointInterfaceUrlString543.update_forward_refs()

EndpointInterfaceUrlString543DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString543Defaults.update_forward_refs()

EndpointInterfaceUrlString543Merge.update_forward_refs()

EndpointInterfaceUrlString543Parse.update_forward_refs()

EndpointInterfaceUrlString544.update_forward_refs()

EndpointInterfaceUrlString544DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString544Defaults.update_forward_refs()

EndpointInterfaceUrlString544Merge.update_forward_refs()

EndpointInterfaceUrlString544Parse.update_forward_refs()

EndpointInterfaceUrlString545.update_forward_refs()

EndpointInterfaceUrlString545DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString545Defaults.update_forward_refs()

EndpointInterfaceUrlString545Merge.update_forward_refs()

EndpointInterfaceUrlString545Parse.update_forward_refs()

EndpointInterfaceUrlString546.update_forward_refs()

EndpointInterfaceUrlString546DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString546Defaults.update_forward_refs()

EndpointInterfaceUrlString546Merge.update_forward_refs()

EndpointInterfaceUrlString546Parse.update_forward_refs()

EndpointInterfaceUrlString547.update_forward_refs()

EndpointInterfaceUrlString547DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString547Defaults.update_forward_refs()

EndpointInterfaceUrlString547Merge.update_forward_refs()

EndpointInterfaceUrlString547Parse.update_forward_refs()

EndpointInterfaceUrlString548.update_forward_refs()

EndpointInterfaceUrlString548DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString548Defaults.update_forward_refs()

EndpointInterfaceUrlString548Merge.update_forward_refs()

EndpointInterfaceUrlString548Parse.update_forward_refs()

EndpointInterfaceUrlString549.update_forward_refs()

EndpointInterfaceUrlString549DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString549Defaults.update_forward_refs()

EndpointInterfaceUrlString549Merge.update_forward_refs()

EndpointInterfaceUrlString549Parse.update_forward_refs()

EndpointInterfaceUrlString54DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString54Defaults.update_forward_refs()

EndpointInterfaceUrlString54Merge.update_forward_refs()

EndpointInterfaceUrlString54Parse.update_forward_refs()

EndpointInterfaceUrlString55.update_forward_refs()

EndpointInterfaceUrlString550.update_forward_refs()

EndpointInterfaceUrlString550DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString550Defaults.update_forward_refs()

EndpointInterfaceUrlString550Merge.update_forward_refs()

EndpointInterfaceUrlString550Parse.update_forward_refs()

EndpointInterfaceUrlString551.update_forward_refs()

EndpointInterfaceUrlString551DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString551Defaults.update_forward_refs()

EndpointInterfaceUrlString551Merge.update_forward_refs()

EndpointInterfaceUrlString551Parse.update_forward_refs()

EndpointInterfaceUrlString552.update_forward_refs()

EndpointInterfaceUrlString552DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString552Defaults.update_forward_refs()

EndpointInterfaceUrlString552Merge.update_forward_refs()

EndpointInterfaceUrlString552Parse.update_forward_refs()

EndpointInterfaceUrlString553.update_forward_refs()

EndpointInterfaceUrlString553DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString553Defaults.update_forward_refs()

EndpointInterfaceUrlString553Merge.update_forward_refs()

EndpointInterfaceUrlString553Parse.update_forward_refs()

EndpointInterfaceUrlString554.update_forward_refs()

EndpointInterfaceUrlString554DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString554Defaults.update_forward_refs()

EndpointInterfaceUrlString554Merge.update_forward_refs()

EndpointInterfaceUrlString554Parse.update_forward_refs()

EndpointInterfaceUrlString555.update_forward_refs()

EndpointInterfaceUrlString555DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString555Defaults.update_forward_refs()

EndpointInterfaceUrlString555Merge.update_forward_refs()

EndpointInterfaceUrlString555Parse.update_forward_refs()

EndpointInterfaceUrlString556.update_forward_refs()

EndpointInterfaceUrlString556DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString556Defaults.update_forward_refs()

EndpointInterfaceUrlString556Merge.update_forward_refs()

EndpointInterfaceUrlString556Parse.update_forward_refs()

EndpointInterfaceUrlString557.update_forward_refs()

EndpointInterfaceUrlString557DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString557Defaults.update_forward_refs()

EndpointInterfaceUrlString557Merge.update_forward_refs()

EndpointInterfaceUrlString557Parse.update_forward_refs()

EndpointInterfaceUrlString558.update_forward_refs()

EndpointInterfaceUrlString558DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString558Defaults.update_forward_refs()

EndpointInterfaceUrlString558Merge.update_forward_refs()

EndpointInterfaceUrlString558Parse.update_forward_refs()

EndpointInterfaceUrlString559.update_forward_refs()

EndpointInterfaceUrlString559DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString559Defaults.update_forward_refs()

EndpointInterfaceUrlString559Merge.update_forward_refs()

EndpointInterfaceUrlString559Parse.update_forward_refs()

EndpointInterfaceUrlString55DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString55Defaults.update_forward_refs()

EndpointInterfaceUrlString55Merge.update_forward_refs()

EndpointInterfaceUrlString55Parse.update_forward_refs()

EndpointInterfaceUrlString56.update_forward_refs()

EndpointInterfaceUrlString560.update_forward_refs()

EndpointInterfaceUrlString560DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString560Defaults.update_forward_refs()

EndpointInterfaceUrlString560Merge.update_forward_refs()

EndpointInterfaceUrlString560Parse.update_forward_refs()

EndpointInterfaceUrlString561.update_forward_refs()

EndpointInterfaceUrlString561DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString561Defaults.update_forward_refs()

EndpointInterfaceUrlString561Merge.update_forward_refs()

EndpointInterfaceUrlString561Parse.update_forward_refs()

EndpointInterfaceUrlString562.update_forward_refs()

EndpointInterfaceUrlString562DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString562Defaults.update_forward_refs()

EndpointInterfaceUrlString562Merge.update_forward_refs()

EndpointInterfaceUrlString562Parse.update_forward_refs()

EndpointInterfaceUrlString563.update_forward_refs()

EndpointInterfaceUrlString563DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString563Defaults.update_forward_refs()

EndpointInterfaceUrlString563Merge.update_forward_refs()

EndpointInterfaceUrlString563Parse.update_forward_refs()

EndpointInterfaceUrlString564.update_forward_refs()

EndpointInterfaceUrlString564DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString564Defaults.update_forward_refs()

EndpointInterfaceUrlString564Merge.update_forward_refs()

EndpointInterfaceUrlString564Parse.update_forward_refs()

EndpointInterfaceUrlString565.update_forward_refs()

EndpointInterfaceUrlString565DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString565Defaults.update_forward_refs()

EndpointInterfaceUrlString565Merge.update_forward_refs()

EndpointInterfaceUrlString565Parse.update_forward_refs()

EndpointInterfaceUrlString566.update_forward_refs()

EndpointInterfaceUrlString566DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString566Defaults.update_forward_refs()

EndpointInterfaceUrlString566Merge.update_forward_refs()

EndpointInterfaceUrlString566Parse.update_forward_refs()

EndpointInterfaceUrlString567.update_forward_refs()

EndpointInterfaceUrlString567DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString567Defaults.update_forward_refs()

EndpointInterfaceUrlString567Merge.update_forward_refs()

EndpointInterfaceUrlString567Parse.update_forward_refs()

EndpointInterfaceUrlString568.update_forward_refs()

EndpointInterfaceUrlString568DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString568Defaults.update_forward_refs()

EndpointInterfaceUrlString568Merge.update_forward_refs()

EndpointInterfaceUrlString568Parse.update_forward_refs()

EndpointInterfaceUrlString569.update_forward_refs()

EndpointInterfaceUrlString569DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString569Defaults.update_forward_refs()

EndpointInterfaceUrlString569Merge.update_forward_refs()

EndpointInterfaceUrlString569Parse.update_forward_refs()

EndpointInterfaceUrlString56DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString56Defaults.update_forward_refs()

EndpointInterfaceUrlString56Merge.update_forward_refs()

EndpointInterfaceUrlString56Parse.update_forward_refs()

EndpointInterfaceUrlString57.update_forward_refs()

EndpointInterfaceUrlString570.update_forward_refs()

EndpointInterfaceUrlString570DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString570Defaults.update_forward_refs()

EndpointInterfaceUrlString570Merge.update_forward_refs()

EndpointInterfaceUrlString570Parse.update_forward_refs()

EndpointInterfaceUrlString571.update_forward_refs()

EndpointInterfaceUrlString571DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString571Defaults.update_forward_refs()

EndpointInterfaceUrlString571Merge.update_forward_refs()

EndpointInterfaceUrlString571Parse.update_forward_refs()

EndpointInterfaceUrlString572.update_forward_refs()

EndpointInterfaceUrlString572DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString572Defaults.update_forward_refs()

EndpointInterfaceUrlString572Merge.update_forward_refs()

EndpointInterfaceUrlString572Parse.update_forward_refs()

EndpointInterfaceUrlString573.update_forward_refs()

EndpointInterfaceUrlString573DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString573Defaults.update_forward_refs()

EndpointInterfaceUrlString573Merge.update_forward_refs()

EndpointInterfaceUrlString573Parse.update_forward_refs()

EndpointInterfaceUrlString574.update_forward_refs()

EndpointInterfaceUrlString574DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString574Defaults.update_forward_refs()

EndpointInterfaceUrlString574Merge.update_forward_refs()

EndpointInterfaceUrlString574Parse.update_forward_refs()

EndpointInterfaceUrlString575.update_forward_refs()

EndpointInterfaceUrlString575DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString575Defaults.update_forward_refs()

EndpointInterfaceUrlString575Merge.update_forward_refs()

EndpointInterfaceUrlString575Parse.update_forward_refs()

EndpointInterfaceUrlString576.update_forward_refs()

EndpointInterfaceUrlString576DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString576Defaults.update_forward_refs()

EndpointInterfaceUrlString576Merge.update_forward_refs()

EndpointInterfaceUrlString576Parse.update_forward_refs()

EndpointInterfaceUrlString577.update_forward_refs()

EndpointInterfaceUrlString577DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString577Defaults.update_forward_refs()

EndpointInterfaceUrlString577Merge.update_forward_refs()

EndpointInterfaceUrlString577Parse.update_forward_refs()

EndpointInterfaceUrlString578.update_forward_refs()

EndpointInterfaceUrlString578DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString578Defaults.update_forward_refs()

EndpointInterfaceUrlString578Merge.update_forward_refs()

EndpointInterfaceUrlString578Parse.update_forward_refs()

EndpointInterfaceUrlString579.update_forward_refs()

EndpointInterfaceUrlString579DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString579Defaults.update_forward_refs()

EndpointInterfaceUrlString579Merge.update_forward_refs()

EndpointInterfaceUrlString579Parse.update_forward_refs()

EndpointInterfaceUrlString57DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString57Defaults.update_forward_refs()

EndpointInterfaceUrlString57Merge.update_forward_refs()

EndpointInterfaceUrlString57Parse.update_forward_refs()

EndpointInterfaceUrlString58.update_forward_refs()

EndpointInterfaceUrlString580.update_forward_refs()

EndpointInterfaceUrlString580DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString580Defaults.update_forward_refs()

EndpointInterfaceUrlString580Merge.update_forward_refs()

EndpointInterfaceUrlString580Parse.update_forward_refs()

EndpointInterfaceUrlString581.update_forward_refs()

EndpointInterfaceUrlString581DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString581Defaults.update_forward_refs()

EndpointInterfaceUrlString581Merge.update_forward_refs()

EndpointInterfaceUrlString581Parse.update_forward_refs()

EndpointInterfaceUrlString582.update_forward_refs()

EndpointInterfaceUrlString582DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString582Defaults.update_forward_refs()

EndpointInterfaceUrlString582Merge.update_forward_refs()

EndpointInterfaceUrlString582Parse.update_forward_refs()

EndpointInterfaceUrlString583.update_forward_refs()

EndpointInterfaceUrlString583DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString583Defaults.update_forward_refs()

EndpointInterfaceUrlString583Merge.update_forward_refs()

EndpointInterfaceUrlString583Parse.update_forward_refs()

EndpointInterfaceUrlString584.update_forward_refs()

EndpointInterfaceUrlString584DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString584Defaults.update_forward_refs()

EndpointInterfaceUrlString584Merge.update_forward_refs()

EndpointInterfaceUrlString584Parse.update_forward_refs()

EndpointInterfaceUrlString585.update_forward_refs()

EndpointInterfaceUrlString585DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString585Defaults.update_forward_refs()

EndpointInterfaceUrlString585Merge.update_forward_refs()

EndpointInterfaceUrlString585Parse.update_forward_refs()

EndpointInterfaceUrlString586.update_forward_refs()

EndpointInterfaceUrlString586DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString586Defaults.update_forward_refs()

EndpointInterfaceUrlString586Merge.update_forward_refs()

EndpointInterfaceUrlString586Parse.update_forward_refs()

EndpointInterfaceUrlString587.update_forward_refs()

EndpointInterfaceUrlString587DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString587Defaults.update_forward_refs()

EndpointInterfaceUrlString587Merge.update_forward_refs()

EndpointInterfaceUrlString587Parse.update_forward_refs()

EndpointInterfaceUrlString588.update_forward_refs()

EndpointInterfaceUrlString588DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString588Defaults.update_forward_refs()

EndpointInterfaceUrlString588Merge.update_forward_refs()

EndpointInterfaceUrlString588Parse.update_forward_refs()

EndpointInterfaceUrlString589.update_forward_refs()

EndpointInterfaceUrlString589DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString589Defaults.update_forward_refs()

EndpointInterfaceUrlString589Merge.update_forward_refs()

EndpointInterfaceUrlString589Parse.update_forward_refs()

EndpointInterfaceUrlString58DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString58Defaults.update_forward_refs()

EndpointInterfaceUrlString58Merge.update_forward_refs()

EndpointInterfaceUrlString58Parse.update_forward_refs()

EndpointInterfaceUrlString59.update_forward_refs()

EndpointInterfaceUrlString590.update_forward_refs()

EndpointInterfaceUrlString590DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString590Defaults.update_forward_refs()

EndpointInterfaceUrlString590Merge.update_forward_refs()

EndpointInterfaceUrlString590Parse.update_forward_refs()

EndpointInterfaceUrlString591.update_forward_refs()

EndpointInterfaceUrlString591DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString591Defaults.update_forward_refs()

EndpointInterfaceUrlString591Merge.update_forward_refs()

EndpointInterfaceUrlString591Parse.update_forward_refs()

EndpointInterfaceUrlString592.update_forward_refs()

EndpointInterfaceUrlString592DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString592Defaults.update_forward_refs()

EndpointInterfaceUrlString592Merge.update_forward_refs()

EndpointInterfaceUrlString592Parse.update_forward_refs()

EndpointInterfaceUrlString593.update_forward_refs()

EndpointInterfaceUrlString593DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString593Defaults.update_forward_refs()

EndpointInterfaceUrlString593Merge.update_forward_refs()

EndpointInterfaceUrlString593Parse.update_forward_refs()

EndpointInterfaceUrlString594.update_forward_refs()

EndpointInterfaceUrlString594DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString594Defaults.update_forward_refs()

EndpointInterfaceUrlString594Merge.update_forward_refs()

EndpointInterfaceUrlString594Parse.update_forward_refs()

EndpointInterfaceUrlString595.update_forward_refs()

EndpointInterfaceUrlString595DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString595Defaults.update_forward_refs()

EndpointInterfaceUrlString595Merge.update_forward_refs()

EndpointInterfaceUrlString595Parse.update_forward_refs()

EndpointInterfaceUrlString596.update_forward_refs()

EndpointInterfaceUrlString596DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString596Defaults.update_forward_refs()

EndpointInterfaceUrlString596Merge.update_forward_refs()

EndpointInterfaceUrlString596Parse.update_forward_refs()

EndpointInterfaceUrlString597.update_forward_refs()

EndpointInterfaceUrlString597DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString597Defaults.update_forward_refs()

EndpointInterfaceUrlString597Merge.update_forward_refs()

EndpointInterfaceUrlString597Parse.update_forward_refs()

EndpointInterfaceUrlString598.update_forward_refs()

EndpointInterfaceUrlString598DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString598Defaults.update_forward_refs()

EndpointInterfaceUrlString598Merge.update_forward_refs()

EndpointInterfaceUrlString598Parse.update_forward_refs()

EndpointInterfaceUrlString599.update_forward_refs()

EndpointInterfaceUrlString599DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString599Defaults.update_forward_refs()

EndpointInterfaceUrlString599Merge.update_forward_refs()

EndpointInterfaceUrlString599Parse.update_forward_refs()

EndpointInterfaceUrlString59DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString59Defaults.update_forward_refs()

EndpointInterfaceUrlString59Merge.update_forward_refs()

EndpointInterfaceUrlString59Parse.update_forward_refs()

EndpointInterfaceUrlString5DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString5Defaults.update_forward_refs()

EndpointInterfaceUrlString5Merge.update_forward_refs()

EndpointInterfaceUrlString5Parse.update_forward_refs()

EndpointInterfaceUrlString6.update_forward_refs()

EndpointInterfaceUrlString60.update_forward_refs()

EndpointInterfaceUrlString600.update_forward_refs()

EndpointInterfaceUrlString600DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString600Defaults.update_forward_refs()

EndpointInterfaceUrlString600Merge.update_forward_refs()

EndpointInterfaceUrlString600Parse.update_forward_refs()

EndpointInterfaceUrlString601.update_forward_refs()

EndpointInterfaceUrlString601DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString601Defaults.update_forward_refs()

EndpointInterfaceUrlString601Merge.update_forward_refs()

EndpointInterfaceUrlString601Parse.update_forward_refs()

EndpointInterfaceUrlString602.update_forward_refs()

EndpointInterfaceUrlString602DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString602Defaults.update_forward_refs()

EndpointInterfaceUrlString602Merge.update_forward_refs()

EndpointInterfaceUrlString602Parse.update_forward_refs()

EndpointInterfaceUrlString603.update_forward_refs()

EndpointInterfaceUrlString603DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString603Defaults.update_forward_refs()

EndpointInterfaceUrlString603Merge.update_forward_refs()

EndpointInterfaceUrlString603Parse.update_forward_refs()

EndpointInterfaceUrlString604.update_forward_refs()

EndpointInterfaceUrlString604DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString604Defaults.update_forward_refs()

EndpointInterfaceUrlString604Merge.update_forward_refs()

EndpointInterfaceUrlString604Parse.update_forward_refs()

EndpointInterfaceUrlString605.update_forward_refs()

EndpointInterfaceUrlString605DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString605Defaults.update_forward_refs()

EndpointInterfaceUrlString605Merge.update_forward_refs()

EndpointInterfaceUrlString605Parse.update_forward_refs()

EndpointInterfaceUrlString606.update_forward_refs()

EndpointInterfaceUrlString606DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString606Defaults.update_forward_refs()

EndpointInterfaceUrlString606Merge.update_forward_refs()

EndpointInterfaceUrlString606Parse.update_forward_refs()

EndpointInterfaceUrlString607.update_forward_refs()

EndpointInterfaceUrlString607DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString607Defaults.update_forward_refs()

EndpointInterfaceUrlString607Merge.update_forward_refs()

EndpointInterfaceUrlString607Parse.update_forward_refs()

EndpointInterfaceUrlString608.update_forward_refs()

EndpointInterfaceUrlString608DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString608Defaults.update_forward_refs()

EndpointInterfaceUrlString608Merge.update_forward_refs()

EndpointInterfaceUrlString608Parse.update_forward_refs()

EndpointInterfaceUrlString609.update_forward_refs()

EndpointInterfaceUrlString609DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString609Defaults.update_forward_refs()

EndpointInterfaceUrlString609Merge.update_forward_refs()

EndpointInterfaceUrlString609Parse.update_forward_refs()

EndpointInterfaceUrlString60DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString60Defaults.update_forward_refs()

EndpointInterfaceUrlString60Merge.update_forward_refs()

EndpointInterfaceUrlString60Parse.update_forward_refs()

EndpointInterfaceUrlString61.update_forward_refs()

EndpointInterfaceUrlString610.update_forward_refs()

EndpointInterfaceUrlString610DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString610Defaults.update_forward_refs()

EndpointInterfaceUrlString610Merge.update_forward_refs()

EndpointInterfaceUrlString610Parse.update_forward_refs()

EndpointInterfaceUrlString611.update_forward_refs()

EndpointInterfaceUrlString611DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString611Defaults.update_forward_refs()

EndpointInterfaceUrlString611Merge.update_forward_refs()

EndpointInterfaceUrlString611Parse.update_forward_refs()

EndpointInterfaceUrlString612.update_forward_refs()

EndpointInterfaceUrlString612DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString612Defaults.update_forward_refs()

EndpointInterfaceUrlString612Merge.update_forward_refs()

EndpointInterfaceUrlString612Parse.update_forward_refs()

EndpointInterfaceUrlString613.update_forward_refs()

EndpointInterfaceUrlString613DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString613Defaults.update_forward_refs()

EndpointInterfaceUrlString613Merge.update_forward_refs()

EndpointInterfaceUrlString613Parse.update_forward_refs()

EndpointInterfaceUrlString614.update_forward_refs()

EndpointInterfaceUrlString614DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString614Defaults.update_forward_refs()

EndpointInterfaceUrlString614Merge.update_forward_refs()

EndpointInterfaceUrlString614Parse.update_forward_refs()

EndpointInterfaceUrlString615.update_forward_refs()

EndpointInterfaceUrlString615DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString615Defaults.update_forward_refs()

EndpointInterfaceUrlString615Merge.update_forward_refs()

EndpointInterfaceUrlString615Parse.update_forward_refs()

EndpointInterfaceUrlString616.update_forward_refs()

EndpointInterfaceUrlString616DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString616Defaults.update_forward_refs()

EndpointInterfaceUrlString616Merge.update_forward_refs()

EndpointInterfaceUrlString616Parse.update_forward_refs()

EndpointInterfaceUrlString617.update_forward_refs()

EndpointInterfaceUrlString617DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString617Defaults.update_forward_refs()

EndpointInterfaceUrlString617Merge.update_forward_refs()

EndpointInterfaceUrlString617Parse.update_forward_refs()

EndpointInterfaceUrlString618.update_forward_refs()

EndpointInterfaceUrlString618DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString618Defaults.update_forward_refs()

EndpointInterfaceUrlString618Merge.update_forward_refs()

EndpointInterfaceUrlString618Parse.update_forward_refs()

EndpointInterfaceUrlString619.update_forward_refs()

EndpointInterfaceUrlString619DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString619Defaults.update_forward_refs()

EndpointInterfaceUrlString619Merge.update_forward_refs()

EndpointInterfaceUrlString619Parse.update_forward_refs()

EndpointInterfaceUrlString61DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString61Defaults.update_forward_refs()

EndpointInterfaceUrlString61Merge.update_forward_refs()

EndpointInterfaceUrlString61Parse.update_forward_refs()

EndpointInterfaceUrlString62.update_forward_refs()

EndpointInterfaceUrlString620.update_forward_refs()

EndpointInterfaceUrlString620DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString620Defaults.update_forward_refs()

EndpointInterfaceUrlString620Merge.update_forward_refs()

EndpointInterfaceUrlString620Parse.update_forward_refs()

EndpointInterfaceUrlString621.update_forward_refs()

EndpointInterfaceUrlString621DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString621Defaults.update_forward_refs()

EndpointInterfaceUrlString621Merge.update_forward_refs()

EndpointInterfaceUrlString621Parse.update_forward_refs()

EndpointInterfaceUrlString622.update_forward_refs()

EndpointInterfaceUrlString622DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString622Defaults.update_forward_refs()

EndpointInterfaceUrlString622Merge.update_forward_refs()

EndpointInterfaceUrlString622Parse.update_forward_refs()

EndpointInterfaceUrlString623.update_forward_refs()

EndpointInterfaceUrlString623DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString623Defaults.update_forward_refs()

EndpointInterfaceUrlString623Merge.update_forward_refs()

EndpointInterfaceUrlString623Parse.update_forward_refs()

EndpointInterfaceUrlString624.update_forward_refs()

EndpointInterfaceUrlString624DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString624Defaults.update_forward_refs()

EndpointInterfaceUrlString624Merge.update_forward_refs()

EndpointInterfaceUrlString624Parse.update_forward_refs()

EndpointInterfaceUrlString625.update_forward_refs()

EndpointInterfaceUrlString625DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString625Defaults.update_forward_refs()

EndpointInterfaceUrlString625Merge.update_forward_refs()

EndpointInterfaceUrlString625Parse.update_forward_refs()

EndpointInterfaceUrlString626.update_forward_refs()

EndpointInterfaceUrlString626DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString626Defaults.update_forward_refs()

EndpointInterfaceUrlString626Merge.update_forward_refs()

EndpointInterfaceUrlString626Parse.update_forward_refs()

EndpointInterfaceUrlString627.update_forward_refs()

EndpointInterfaceUrlString627DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString627Defaults.update_forward_refs()

EndpointInterfaceUrlString627Merge.update_forward_refs()

EndpointInterfaceUrlString627Parse.update_forward_refs()

EndpointInterfaceUrlString628.update_forward_refs()

EndpointInterfaceUrlString628DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString628Defaults.update_forward_refs()

EndpointInterfaceUrlString628Merge.update_forward_refs()

EndpointInterfaceUrlString628Parse.update_forward_refs()

EndpointInterfaceUrlString629.update_forward_refs()

EndpointInterfaceUrlString629DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString629Defaults.update_forward_refs()

EndpointInterfaceUrlString629Merge.update_forward_refs()

EndpointInterfaceUrlString629Parse.update_forward_refs()

EndpointInterfaceUrlString62DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString62Defaults.update_forward_refs()

EndpointInterfaceUrlString62Merge.update_forward_refs()

EndpointInterfaceUrlString62Parse.update_forward_refs()

EndpointInterfaceUrlString63.update_forward_refs()

EndpointInterfaceUrlString630.update_forward_refs()

EndpointInterfaceUrlString630DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString630Defaults.update_forward_refs()

EndpointInterfaceUrlString630Merge.update_forward_refs()

EndpointInterfaceUrlString630Parse.update_forward_refs()

EndpointInterfaceUrlString631.update_forward_refs()

EndpointInterfaceUrlString631DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString631Defaults.update_forward_refs()

EndpointInterfaceUrlString631Merge.update_forward_refs()

EndpointInterfaceUrlString631Parse.update_forward_refs()

EndpointInterfaceUrlString632.update_forward_refs()

EndpointInterfaceUrlString632DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString632Defaults.update_forward_refs()

EndpointInterfaceUrlString632Merge.update_forward_refs()

EndpointInterfaceUrlString632Parse.update_forward_refs()

EndpointInterfaceUrlString633.update_forward_refs()

EndpointInterfaceUrlString633DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString633Defaults.update_forward_refs()

EndpointInterfaceUrlString633Merge.update_forward_refs()

EndpointInterfaceUrlString633Parse.update_forward_refs()

EndpointInterfaceUrlString634.update_forward_refs()

EndpointInterfaceUrlString634DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString634Defaults.update_forward_refs()

EndpointInterfaceUrlString634Merge.update_forward_refs()

EndpointInterfaceUrlString634Parse.update_forward_refs()

EndpointInterfaceUrlString635.update_forward_refs()

EndpointInterfaceUrlString635DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString635Defaults.update_forward_refs()

EndpointInterfaceUrlString635Merge.update_forward_refs()

EndpointInterfaceUrlString635Parse.update_forward_refs()

EndpointInterfaceUrlString636.update_forward_refs()

EndpointInterfaceUrlString636DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString636Defaults.update_forward_refs()

EndpointInterfaceUrlString636Merge.update_forward_refs()

EndpointInterfaceUrlString636Parse.update_forward_refs()

EndpointInterfaceUrlString637.update_forward_refs()

EndpointInterfaceUrlString637DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString637Defaults.update_forward_refs()

EndpointInterfaceUrlString637Merge.update_forward_refs()

EndpointInterfaceUrlString637Parse.update_forward_refs()

EndpointInterfaceUrlString638.update_forward_refs()

EndpointInterfaceUrlString638DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString638Defaults.update_forward_refs()

EndpointInterfaceUrlString638Merge.update_forward_refs()

EndpointInterfaceUrlString638Parse.update_forward_refs()

EndpointInterfaceUrlString639.update_forward_refs()

EndpointInterfaceUrlString639DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString639Defaults.update_forward_refs()

EndpointInterfaceUrlString639Merge.update_forward_refs()

EndpointInterfaceUrlString639Parse.update_forward_refs()

EndpointInterfaceUrlString63DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString63Defaults.update_forward_refs()

EndpointInterfaceUrlString63Merge.update_forward_refs()

EndpointInterfaceUrlString63Parse.update_forward_refs()

EndpointInterfaceUrlString64.update_forward_refs()

EndpointInterfaceUrlString640.update_forward_refs()

EndpointInterfaceUrlString640DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString640Defaults.update_forward_refs()

EndpointInterfaceUrlString640Merge.update_forward_refs()

EndpointInterfaceUrlString640Parse.update_forward_refs()

EndpointInterfaceUrlString641.update_forward_refs()

EndpointInterfaceUrlString641DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString641Defaults.update_forward_refs()

EndpointInterfaceUrlString641Merge.update_forward_refs()

EndpointInterfaceUrlString641Parse.update_forward_refs()

EndpointInterfaceUrlString642.update_forward_refs()

EndpointInterfaceUrlString642DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString642Defaults.update_forward_refs()

EndpointInterfaceUrlString642Merge.update_forward_refs()

EndpointInterfaceUrlString642Parse.update_forward_refs()

EndpointInterfaceUrlString643.update_forward_refs()

EndpointInterfaceUrlString643DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString643Defaults.update_forward_refs()

EndpointInterfaceUrlString643Merge.update_forward_refs()

EndpointInterfaceUrlString643Parse.update_forward_refs()

EndpointInterfaceUrlString644.update_forward_refs()

EndpointInterfaceUrlString644DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString644Defaults.update_forward_refs()

EndpointInterfaceUrlString644Merge.update_forward_refs()

EndpointInterfaceUrlString644Parse.update_forward_refs()

EndpointInterfaceUrlString645.update_forward_refs()

EndpointInterfaceUrlString645DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString645Defaults.update_forward_refs()

EndpointInterfaceUrlString645Merge.update_forward_refs()

EndpointInterfaceUrlString645Parse.update_forward_refs()

EndpointInterfaceUrlString646.update_forward_refs()

EndpointInterfaceUrlString646DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString646Defaults.update_forward_refs()

EndpointInterfaceUrlString646Merge.update_forward_refs()

EndpointInterfaceUrlString646Parse.update_forward_refs()

EndpointInterfaceUrlString647.update_forward_refs()

EndpointInterfaceUrlString647DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString647Defaults.update_forward_refs()

EndpointInterfaceUrlString647Merge.update_forward_refs()

EndpointInterfaceUrlString647Parse.update_forward_refs()

EndpointInterfaceUrlString648.update_forward_refs()

EndpointInterfaceUrlString648DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString648Defaults.update_forward_refs()

EndpointInterfaceUrlString648Merge.update_forward_refs()

EndpointInterfaceUrlString648Parse.update_forward_refs()

EndpointInterfaceUrlString649.update_forward_refs()

EndpointInterfaceUrlString649DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString649Defaults.update_forward_refs()

EndpointInterfaceUrlString649Merge.update_forward_refs()

EndpointInterfaceUrlString649Parse.update_forward_refs()

EndpointInterfaceUrlString64DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString64Defaults.update_forward_refs()

EndpointInterfaceUrlString64Merge.update_forward_refs()

EndpointInterfaceUrlString64Parse.update_forward_refs()

EndpointInterfaceUrlString65.update_forward_refs()

EndpointInterfaceUrlString650.update_forward_refs()

EndpointInterfaceUrlString650DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString650Defaults.update_forward_refs()

EndpointInterfaceUrlString650Merge.update_forward_refs()

EndpointInterfaceUrlString650Parse.update_forward_refs()

EndpointInterfaceUrlString651.update_forward_refs()

EndpointInterfaceUrlString651DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString651Defaults.update_forward_refs()

EndpointInterfaceUrlString651Merge.update_forward_refs()

EndpointInterfaceUrlString651Parse.update_forward_refs()

EndpointInterfaceUrlString652.update_forward_refs()

EndpointInterfaceUrlString652DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString652Defaults.update_forward_refs()

EndpointInterfaceUrlString652Merge.update_forward_refs()

EndpointInterfaceUrlString652Parse.update_forward_refs()

EndpointInterfaceUrlString653.update_forward_refs()

EndpointInterfaceUrlString653DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString653Defaults.update_forward_refs()

EndpointInterfaceUrlString653Merge.update_forward_refs()

EndpointInterfaceUrlString653Parse.update_forward_refs()

EndpointInterfaceUrlString654.update_forward_refs()

EndpointInterfaceUrlString654DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString654Defaults.update_forward_refs()

EndpointInterfaceUrlString654Merge.update_forward_refs()

EndpointInterfaceUrlString654Parse.update_forward_refs()

EndpointInterfaceUrlString655.update_forward_refs()

EndpointInterfaceUrlString655DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString655Defaults.update_forward_refs()

EndpointInterfaceUrlString655Merge.update_forward_refs()

EndpointInterfaceUrlString655Parse.update_forward_refs()

EndpointInterfaceUrlString656.update_forward_refs()

EndpointInterfaceUrlString656DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString656Defaults.update_forward_refs()

EndpointInterfaceUrlString656Merge.update_forward_refs()

EndpointInterfaceUrlString656Parse.update_forward_refs()

EndpointInterfaceUrlString657.update_forward_refs()

EndpointInterfaceUrlString657DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString657Defaults.update_forward_refs()

EndpointInterfaceUrlString657Merge.update_forward_refs()

EndpointInterfaceUrlString657Parse.update_forward_refs()

EndpointInterfaceUrlString658.update_forward_refs()

EndpointInterfaceUrlString658DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString658Defaults.update_forward_refs()

EndpointInterfaceUrlString658Merge.update_forward_refs()

EndpointInterfaceUrlString658Parse.update_forward_refs()

EndpointInterfaceUrlString659.update_forward_refs()

EndpointInterfaceUrlString659DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString659Defaults.update_forward_refs()

EndpointInterfaceUrlString659Merge.update_forward_refs()

EndpointInterfaceUrlString659Parse.update_forward_refs()

EndpointInterfaceUrlString65DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString65Defaults.update_forward_refs()

EndpointInterfaceUrlString65Merge.update_forward_refs()

EndpointInterfaceUrlString65Parse.update_forward_refs()

EndpointInterfaceUrlString66.update_forward_refs()

EndpointInterfaceUrlString660.update_forward_refs()

EndpointInterfaceUrlString660DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString660Defaults.update_forward_refs()

EndpointInterfaceUrlString660Merge.update_forward_refs()

EndpointInterfaceUrlString660Parse.update_forward_refs()

EndpointInterfaceUrlString661.update_forward_refs()

EndpointInterfaceUrlString661DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString661Defaults.update_forward_refs()

EndpointInterfaceUrlString661Merge.update_forward_refs()

EndpointInterfaceUrlString661Parse.update_forward_refs()

EndpointInterfaceUrlString662.update_forward_refs()

EndpointInterfaceUrlString662DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString662Defaults.update_forward_refs()

EndpointInterfaceUrlString662Merge.update_forward_refs()

EndpointInterfaceUrlString662Parse.update_forward_refs()

EndpointInterfaceUrlString663.update_forward_refs()

EndpointInterfaceUrlString663DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString663Defaults.update_forward_refs()

EndpointInterfaceUrlString663Merge.update_forward_refs()

EndpointInterfaceUrlString663Parse.update_forward_refs()

EndpointInterfaceUrlString664.update_forward_refs()

EndpointInterfaceUrlString664DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString664Defaults.update_forward_refs()

EndpointInterfaceUrlString664Merge.update_forward_refs()

EndpointInterfaceUrlString664Parse.update_forward_refs()

EndpointInterfaceUrlString665.update_forward_refs()

EndpointInterfaceUrlString665DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString665Defaults.update_forward_refs()

EndpointInterfaceUrlString665Merge.update_forward_refs()

EndpointInterfaceUrlString665Parse.update_forward_refs()

EndpointInterfaceUrlString666.update_forward_refs()

EndpointInterfaceUrlString666DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString666Defaults.update_forward_refs()

EndpointInterfaceUrlString666Merge.update_forward_refs()

EndpointInterfaceUrlString666Parse.update_forward_refs()

EndpointInterfaceUrlString667.update_forward_refs()

EndpointInterfaceUrlString667DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString667Defaults.update_forward_refs()

EndpointInterfaceUrlString667Merge.update_forward_refs()

EndpointInterfaceUrlString667Parse.update_forward_refs()

EndpointInterfaceUrlString668.update_forward_refs()

EndpointInterfaceUrlString668DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString668Defaults.update_forward_refs()

EndpointInterfaceUrlString668Merge.update_forward_refs()

EndpointInterfaceUrlString668Parse.update_forward_refs()

EndpointInterfaceUrlString669.update_forward_refs()

EndpointInterfaceUrlString669DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString669Defaults.update_forward_refs()

EndpointInterfaceUrlString669Merge.update_forward_refs()

EndpointInterfaceUrlString669Parse.update_forward_refs()

EndpointInterfaceUrlString66DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString66Defaults.update_forward_refs()

EndpointInterfaceUrlString66Merge.update_forward_refs()

EndpointInterfaceUrlString66Parse.update_forward_refs()

EndpointInterfaceUrlString67.update_forward_refs()

EndpointInterfaceUrlString670.update_forward_refs()

EndpointInterfaceUrlString670DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString670Defaults.update_forward_refs()

EndpointInterfaceUrlString670Merge.update_forward_refs()

EndpointInterfaceUrlString670Parse.update_forward_refs()

EndpointInterfaceUrlString671.update_forward_refs()

EndpointInterfaceUrlString671DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString671Defaults.update_forward_refs()

EndpointInterfaceUrlString671Merge.update_forward_refs()

EndpointInterfaceUrlString671Parse.update_forward_refs()

EndpointInterfaceUrlString672.update_forward_refs()

EndpointInterfaceUrlString672DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString672Defaults.update_forward_refs()

EndpointInterfaceUrlString672Merge.update_forward_refs()

EndpointInterfaceUrlString672Parse.update_forward_refs()

EndpointInterfaceUrlString673.update_forward_refs()

EndpointInterfaceUrlString673DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString673Defaults.update_forward_refs()

EndpointInterfaceUrlString673Merge.update_forward_refs()

EndpointInterfaceUrlString673Parse.update_forward_refs()

EndpointInterfaceUrlString674.update_forward_refs()

EndpointInterfaceUrlString674DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString674Defaults.update_forward_refs()

EndpointInterfaceUrlString674Merge.update_forward_refs()

EndpointInterfaceUrlString674Parse.update_forward_refs()

EndpointInterfaceUrlString675.update_forward_refs()

EndpointInterfaceUrlString675DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString675Defaults.update_forward_refs()

EndpointInterfaceUrlString675Merge.update_forward_refs()

EndpointInterfaceUrlString675Parse.update_forward_refs()

EndpointInterfaceUrlString676.update_forward_refs()

EndpointInterfaceUrlString676DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString676Defaults.update_forward_refs()

EndpointInterfaceUrlString676Merge.update_forward_refs()

EndpointInterfaceUrlString676Parse.update_forward_refs()

EndpointInterfaceUrlString677.update_forward_refs()

EndpointInterfaceUrlString677DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString677Defaults.update_forward_refs()

EndpointInterfaceUrlString677Merge.update_forward_refs()

EndpointInterfaceUrlString677Parse.update_forward_refs()

EndpointInterfaceUrlString678.update_forward_refs()

EndpointInterfaceUrlString678DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString678Defaults.update_forward_refs()

EndpointInterfaceUrlString678Merge.update_forward_refs()

EndpointInterfaceUrlString678Parse.update_forward_refs()

EndpointInterfaceUrlString679.update_forward_refs()

EndpointInterfaceUrlString679DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString679Defaults.update_forward_refs()

EndpointInterfaceUrlString679Merge.update_forward_refs()

EndpointInterfaceUrlString679Parse.update_forward_refs()

EndpointInterfaceUrlString67DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString67Defaults.update_forward_refs()

EndpointInterfaceUrlString67Merge.update_forward_refs()

EndpointInterfaceUrlString67Parse.update_forward_refs()

EndpointInterfaceUrlString68.update_forward_refs()

EndpointInterfaceUrlString680.update_forward_refs()

EndpointInterfaceUrlString680DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString680Defaults.update_forward_refs()

EndpointInterfaceUrlString680Merge.update_forward_refs()

EndpointInterfaceUrlString680Parse.update_forward_refs()

EndpointInterfaceUrlString681.update_forward_refs()

EndpointInterfaceUrlString681DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString681Defaults.update_forward_refs()

EndpointInterfaceUrlString681Merge.update_forward_refs()

EndpointInterfaceUrlString681Parse.update_forward_refs()

EndpointInterfaceUrlString682.update_forward_refs()

EndpointInterfaceUrlString682DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString682Defaults.update_forward_refs()

EndpointInterfaceUrlString682Merge.update_forward_refs()

EndpointInterfaceUrlString682Parse.update_forward_refs()

EndpointInterfaceUrlString683.update_forward_refs()

EndpointInterfaceUrlString683DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString683Defaults.update_forward_refs()

EndpointInterfaceUrlString683Merge.update_forward_refs()

EndpointInterfaceUrlString683Parse.update_forward_refs()

EndpointInterfaceUrlString684.update_forward_refs()

EndpointInterfaceUrlString684DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString684Defaults.update_forward_refs()

EndpointInterfaceUrlString684Merge.update_forward_refs()

EndpointInterfaceUrlString684Parse.update_forward_refs()

EndpointInterfaceUrlString685.update_forward_refs()

EndpointInterfaceUrlString685DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString685Defaults.update_forward_refs()

EndpointInterfaceUrlString685Merge.update_forward_refs()

EndpointInterfaceUrlString685Parse.update_forward_refs()

EndpointInterfaceUrlString686.update_forward_refs()

EndpointInterfaceUrlString686DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString686Defaults.update_forward_refs()

EndpointInterfaceUrlString686Merge.update_forward_refs()

EndpointInterfaceUrlString686Parse.update_forward_refs()

EndpointInterfaceUrlString687.update_forward_refs()

EndpointInterfaceUrlString687DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString687Defaults.update_forward_refs()

EndpointInterfaceUrlString687Merge.update_forward_refs()

EndpointInterfaceUrlString687Parse.update_forward_refs()

EndpointInterfaceUrlString688.update_forward_refs()

EndpointInterfaceUrlString688DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString688Defaults.update_forward_refs()

EndpointInterfaceUrlString688Merge.update_forward_refs()

EndpointInterfaceUrlString688Parse.update_forward_refs()

EndpointInterfaceUrlString689.update_forward_refs()

EndpointInterfaceUrlString689DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString689Defaults.update_forward_refs()

EndpointInterfaceUrlString689Merge.update_forward_refs()

EndpointInterfaceUrlString689Parse.update_forward_refs()

EndpointInterfaceUrlString68DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString68Defaults.update_forward_refs()

EndpointInterfaceUrlString68Merge.update_forward_refs()

EndpointInterfaceUrlString68Parse.update_forward_refs()

EndpointInterfaceUrlString69.update_forward_refs()

EndpointInterfaceUrlString690.update_forward_refs()

EndpointInterfaceUrlString690DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString690Defaults.update_forward_refs()

EndpointInterfaceUrlString690Merge.update_forward_refs()

EndpointInterfaceUrlString690Parse.update_forward_refs()

EndpointInterfaceUrlString691.update_forward_refs()

EndpointInterfaceUrlString691DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString691Defaults.update_forward_refs()

EndpointInterfaceUrlString691Merge.update_forward_refs()

EndpointInterfaceUrlString691Parse.update_forward_refs()

EndpointInterfaceUrlString692.update_forward_refs()

EndpointInterfaceUrlString692DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString692Defaults.update_forward_refs()

EndpointInterfaceUrlString692Merge.update_forward_refs()

EndpointInterfaceUrlString692Parse.update_forward_refs()

EndpointInterfaceUrlString693.update_forward_refs()

EndpointInterfaceUrlString693DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString693Defaults.update_forward_refs()

EndpointInterfaceUrlString693Merge.update_forward_refs()

EndpointInterfaceUrlString693Parse.update_forward_refs()

EndpointInterfaceUrlString69DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString69Defaults.update_forward_refs()

EndpointInterfaceUrlString69Merge.update_forward_refs()

EndpointInterfaceUrlString69Parse.update_forward_refs()

EndpointInterfaceUrlString6DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString6Defaults.update_forward_refs()

EndpointInterfaceUrlString6Merge.update_forward_refs()

EndpointInterfaceUrlString6Parse.update_forward_refs()

EndpointInterfaceUrlString7.update_forward_refs()

EndpointInterfaceUrlString70.update_forward_refs()

EndpointInterfaceUrlString70DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString70Defaults.update_forward_refs()

EndpointInterfaceUrlString70Merge.update_forward_refs()

EndpointInterfaceUrlString70Parse.update_forward_refs()

EndpointInterfaceUrlString71.update_forward_refs()

EndpointInterfaceUrlString71DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString71Defaults.update_forward_refs()

EndpointInterfaceUrlString71Merge.update_forward_refs()

EndpointInterfaceUrlString71Parse.update_forward_refs()

EndpointInterfaceUrlString72.update_forward_refs()

EndpointInterfaceUrlString72DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString72Defaults.update_forward_refs()

EndpointInterfaceUrlString72Merge.update_forward_refs()

EndpointInterfaceUrlString72Parse.update_forward_refs()

EndpointInterfaceUrlString73.update_forward_refs()

EndpointInterfaceUrlString73DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString73Defaults.update_forward_refs()

EndpointInterfaceUrlString73Merge.update_forward_refs()

EndpointInterfaceUrlString73Parse.update_forward_refs()

EndpointInterfaceUrlString74.update_forward_refs()

EndpointInterfaceUrlString74DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString74Defaults.update_forward_refs()

EndpointInterfaceUrlString74Merge.update_forward_refs()

EndpointInterfaceUrlString74Parse.update_forward_refs()

EndpointInterfaceUrlString75.update_forward_refs()

EndpointInterfaceUrlString75DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString75Defaults.update_forward_refs()

EndpointInterfaceUrlString75Merge.update_forward_refs()

EndpointInterfaceUrlString75Parse.update_forward_refs()

EndpointInterfaceUrlString76.update_forward_refs()

EndpointInterfaceUrlString76DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString76Defaults.update_forward_refs()

EndpointInterfaceUrlString76Merge.update_forward_refs()

EndpointInterfaceUrlString76Parse.update_forward_refs()

EndpointInterfaceUrlString77.update_forward_refs()

EndpointInterfaceUrlString77DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString77Defaults.update_forward_refs()

EndpointInterfaceUrlString77Merge.update_forward_refs()

EndpointInterfaceUrlString77Parse.update_forward_refs()

EndpointInterfaceUrlString78.update_forward_refs()

EndpointInterfaceUrlString78DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString78Defaults.update_forward_refs()

EndpointInterfaceUrlString78Merge.update_forward_refs()

EndpointInterfaceUrlString78Parse.update_forward_refs()

EndpointInterfaceUrlString79.update_forward_refs()

EndpointInterfaceUrlString79DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString79Defaults.update_forward_refs()

EndpointInterfaceUrlString79Merge.update_forward_refs()

EndpointInterfaceUrlString79Parse.update_forward_refs()

EndpointInterfaceUrlString7DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString7Defaults.update_forward_refs()

EndpointInterfaceUrlString7Merge.update_forward_refs()

EndpointInterfaceUrlString7Parse.update_forward_refs()

EndpointInterfaceUrlString8.update_forward_refs()

EndpointInterfaceUrlString80.update_forward_refs()

EndpointInterfaceUrlString80DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString80Defaults.update_forward_refs()

EndpointInterfaceUrlString80Merge.update_forward_refs()

EndpointInterfaceUrlString80Parse.update_forward_refs()

EndpointInterfaceUrlString81.update_forward_refs()

EndpointInterfaceUrlString81DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString81Defaults.update_forward_refs()

EndpointInterfaceUrlString81Merge.update_forward_refs()

EndpointInterfaceUrlString81Parse.update_forward_refs()

EndpointInterfaceUrlString82.update_forward_refs()

EndpointInterfaceUrlString82DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString82Defaults.update_forward_refs()

EndpointInterfaceUrlString82Merge.update_forward_refs()

EndpointInterfaceUrlString82Parse.update_forward_refs()

EndpointInterfaceUrlString83.update_forward_refs()

EndpointInterfaceUrlString83DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString83Defaults.update_forward_refs()

EndpointInterfaceUrlString83Merge.update_forward_refs()

EndpointInterfaceUrlString83Parse.update_forward_refs()

EndpointInterfaceUrlString84.update_forward_refs()

EndpointInterfaceUrlString84DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString84Defaults.update_forward_refs()

EndpointInterfaceUrlString84Merge.update_forward_refs()

EndpointInterfaceUrlString84Parse.update_forward_refs()

EndpointInterfaceUrlString85.update_forward_refs()

EndpointInterfaceUrlString85DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString85Defaults.update_forward_refs()

EndpointInterfaceUrlString85Merge.update_forward_refs()

EndpointInterfaceUrlString85Parse.update_forward_refs()

EndpointInterfaceUrlString86.update_forward_refs()

EndpointInterfaceUrlString86DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString86Defaults.update_forward_refs()

EndpointInterfaceUrlString86Merge.update_forward_refs()

EndpointInterfaceUrlString86Parse.update_forward_refs()

EndpointInterfaceUrlString87.update_forward_refs()

EndpointInterfaceUrlString87DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString87Defaults.update_forward_refs()

EndpointInterfaceUrlString87Merge.update_forward_refs()

EndpointInterfaceUrlString87Parse.update_forward_refs()

EndpointInterfaceUrlString88.update_forward_refs()

EndpointInterfaceUrlString88DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString88Defaults.update_forward_refs()

EndpointInterfaceUrlString88Merge.update_forward_refs()

EndpointInterfaceUrlString88Parse.update_forward_refs()

EndpointInterfaceUrlString89.update_forward_refs()

EndpointInterfaceUrlString89DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString89Defaults.update_forward_refs()

EndpointInterfaceUrlString89Merge.update_forward_refs()

EndpointInterfaceUrlString89Parse.update_forward_refs()

EndpointInterfaceUrlString8DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString8Defaults.update_forward_refs()

EndpointInterfaceUrlString8Merge.update_forward_refs()

EndpointInterfaceUrlString8Parse.update_forward_refs()

EndpointInterfaceUrlString9.update_forward_refs()

EndpointInterfaceUrlString90.update_forward_refs()

EndpointInterfaceUrlString90DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString90Defaults.update_forward_refs()

EndpointInterfaceUrlString90Merge.update_forward_refs()

EndpointInterfaceUrlString90Parse.update_forward_refs()

EndpointInterfaceUrlString91.update_forward_refs()

EndpointInterfaceUrlString91DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString91Defaults.update_forward_refs()

EndpointInterfaceUrlString91Merge.update_forward_refs()

EndpointInterfaceUrlString91Parse.update_forward_refs()

EndpointInterfaceUrlString92.update_forward_refs()

EndpointInterfaceUrlString92DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString92Defaults.update_forward_refs()

EndpointInterfaceUrlString92Merge.update_forward_refs()

EndpointInterfaceUrlString92Parse.update_forward_refs()

EndpointInterfaceUrlString93.update_forward_refs()

EndpointInterfaceUrlString93DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString93Defaults.update_forward_refs()

EndpointInterfaceUrlString93Merge.update_forward_refs()

EndpointInterfaceUrlString93Parse.update_forward_refs()

EndpointInterfaceUrlString94.update_forward_refs()

EndpointInterfaceUrlString94DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString94Defaults.update_forward_refs()

EndpointInterfaceUrlString94Merge.update_forward_refs()

EndpointInterfaceUrlString94Parse.update_forward_refs()

EndpointInterfaceUrlString95.update_forward_refs()

EndpointInterfaceUrlString95DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString95Defaults.update_forward_refs()

EndpointInterfaceUrlString95Merge.update_forward_refs()

EndpointInterfaceUrlString95Parse.update_forward_refs()

EndpointInterfaceUrlString96.update_forward_refs()

EndpointInterfaceUrlString96DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString96Defaults.update_forward_refs()

EndpointInterfaceUrlString96Merge.update_forward_refs()

EndpointInterfaceUrlString96Parse.update_forward_refs()

EndpointInterfaceUrlString97.update_forward_refs()

EndpointInterfaceUrlString97DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString97Defaults.update_forward_refs()

EndpointInterfaceUrlString97Merge.update_forward_refs()

EndpointInterfaceUrlString97Parse.update_forward_refs()

EndpointInterfaceUrlString98.update_forward_refs()

EndpointInterfaceUrlString98DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString98Defaults.update_forward_refs()

EndpointInterfaceUrlString98Merge.update_forward_refs()

EndpointInterfaceUrlString98Parse.update_forward_refs()

EndpointInterfaceUrlString99.update_forward_refs()

EndpointInterfaceUrlString99DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString99Defaults.update_forward_refs()

EndpointInterfaceUrlString99Merge.update_forward_refs()

EndpointInterfaceUrlString99Parse.update_forward_refs()

EndpointInterfaceUrlString9DEFAULTS.update_forward_refs()

EndpointInterfaceUrlString9Defaults.update_forward_refs()

EndpointInterfaceUrlString9Merge.update_forward_refs()

EndpointInterfaceUrlString9Parse.update_forward_refs()

EndpointInterfaceUrlStringDEFAULTS.update_forward_refs()

EndpointInterfaceUrlStringDefaults.update_forward_refs()

EndpointInterfaceUrlStringMerge.update_forward_refs()

EndpointInterfaceUrlStringParse.update_forward_refs()

Environments.update_forward_refs()

EnvironmentsHeaders.update_forward_refs()

EpicDiscussions.update_forward_refs()

EpicDiscussionsHeaders.update_forward_refs()

EpicIssues.update_forward_refs()

EpicIssuesHeaders.update_forward_refs()

EpicNotes.update_forward_refs()

EpicNotesHeaders.update_forward_refs()

Epics.update_forward_refs()

EpicsHeaders.update_forward_refs()

Events.update_forward_refs()

EventsHeaders.update_forward_refs()

FeatureFlags.update_forward_refs()

FeatureFlagsHeaders.update_forward_refs()

GeoNodes.update_forward_refs()

GeoNodesHeaders.update_forward_refs()

GitCommit.update_forward_refs()

GitCommitAuthor.update_forward_refs()

GitHubAPIPR.update_forward_refs()

GitHubCommit.update_forward_refs()

GitHubDSL.update_forward_refs()

GitHubDSLSetSummaryMarkdown.update_forward_refs()

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

GitLabApproval.update_forward_refs()


GitLabCIYMLTemplates.update_forward_refs()

GitLabCIYMLTemplatesHeaders.update_forward_refs()

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


GitignoreTemplates.update_forward_refs()

GitignoreTemplatesHeaders.update_forward_refs()

Graphql.update_forward_refs()

GraphqlDefaults.update_forward_refs()

GroupAccessRequests.update_forward_refs()

GroupAccessRequestsHeaders.update_forward_refs()

GroupBadges.update_forward_refs()

GroupBadgesHeaders.update_forward_refs()

GroupCustomAttributes.update_forward_refs()

GroupCustomAttributesHeaders.update_forward_refs()

GroupDeployTokens.update_forward_refs()

GroupDeployTokensHeaders.update_forward_refs()

GroupIssueBoards.update_forward_refs()

GroupIssueBoardsHeaders.update_forward_refs()

GroupLabels.update_forward_refs()

GroupLabelsHeaders.update_forward_refs()

GroupMembers.update_forward_refs()

GroupMembersHeaders.update_forward_refs()

GroupMilestones.update_forward_refs()

GroupMilestonesHeaders.update_forward_refs()

GroupProjects.update_forward_refs()

GroupProjectsHeaders.update_forward_refs()

GroupVariables.update_forward_refs()

GroupVariablesHeaders.update_forward_refs()

Groups.update_forward_refs()

GroupsHeaders.update_forward_refs()

HookCollectionHooksKeyofHooks.update_forward_refs()

IssueAwardEmojis.update_forward_refs()

IssueAwardEmojisHeaders.update_forward_refs()

IssueDiscussions.update_forward_refs()

IssueDiscussionsHeaders.update_forward_refs()

IssueNotes.update_forward_refs()

IssueNotesHeaders.update_forward_refs()

Issues.update_forward_refs()

IssuesHeaders.update_forward_refs()

IssuesStatistics.update_forward_refs()

IssuesStatisticsHeaders.update_forward_refs()

JIRAIssue.update_forward_refs()

Jobs.update_forward_refs()

JobsHeaders.update_forward_refs()

Keys.update_forward_refs()

KeysHeaders.update_forward_refs()

Labels.update_forward_refs()

LabelsHeaders.update_forward_refs()

LicenceTemplates.update_forward_refs()

LicenceTemplatesHeaders.update_forward_refs()

License.update_forward_refs()

LicenseHeaders.update_forward_refs()

Lint.update_forward_refs()

LintHeaders.update_forward_refs()

MapperTypeofimportUsersOrtatheroxDevDangerDangerJsNodeModulesGitbeakerCoreDistTypesServicesIndexUsersUserCustomAttributesUserEmailsUserImpersonationTokensUserKeysUserGPGKeysGroupsGroupAccessRequestsGroupBadgesGroupCustomAttributesGroupIssueBoardsGroupMembersGroupMilestonesGroupProjectsGroupVariablesGroupLabelsGroupDeployTokensEpicsEpicIssuesEpicNotesEpicDiscussionsBranchesCommitsCommitDiscussionsContainerRegistryDeployKeysDeploymentsEnvironmentsIssuesIssuesStatisticsIssueAwardEmojisIssueNotesIssueDiscussionsJobsLabelsMergeRequestsMergeRequestAwardEmojisMergeRequestDiscussionsMergeRequestNotesPackagesPipelinesPipelineSchedulesPipelineScheduleVariablesProjectsProjectAccessRequestsProjectBadgesProjectCustomAttributesProjectImportExportProjectIssueBoardsProjectHooksProjectMembersProjectMilestonesProjectSnippetsProjectSnippetNotesProjectSnippetDiscussionsProjectSnippetAwardEmojisProtectedBranchesProtectedTagsProjectVariablesProjectDeployTokensPushRulesReleasesReleaseLinksRepositoriesRepositoryFilesRunnersServicesTagsTodosTriggersVulnerabilityFindingsApplicationSettingsBroadcastMessagesEventsFeatureFlagsGeoNodesGitignoreTemplatesGitLabCIYMLTemplatesKeysLicenseLicenceTemplatesLintNamespacesNotificationSettingsMarkdownPagesDomainsSearchSidekiqMetricsSnippetsSystemHooksVersionWikis.update_forward_refs()

Markdown.update_forward_refs()

MarkdownHeaders.update_forward_refs()

MergeRequestAwardEmojis.update_forward_refs()

MergeRequestAwardEmojisHeaders.update_forward_refs()

MergeRequestDiscussions.update_forward_refs()

MergeRequestDiscussionsHeaders.update_forward_refs()

MergeRequestNotes.update_forward_refs()

MergeRequestNotesHeaders.update_forward_refs()

MergeRequests.update_forward_refs()

MergeRequestsHeaders.update_forward_refs()

Namespaces.update_forward_refs()

NamespacesHeaders.update_forward_refs()

NotificationSettings.update_forward_refs()

NotificationSettingsHeaders.update_forward_refs()

Octokit.update_forward_refs()

OctokitAuth.update_forward_refs()

OctokitLog.update_forward_refs()

OctokitLogDebug.update_forward_refs()

OctokitLogError.update_forward_refs()

OctokitLogInfo.update_forward_refs()

OctokitLogWarn.update_forward_refs()

Packages.update_forward_refs()

PackagesHeaders.update_forward_refs()

PagesDomains.update_forward_refs()

PagesDomainsHeaders.update_forward_refs()

PaginateInterface.update_forward_refs()

PaginateInterfaceIterator.update_forward_refs()

PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemove.update_forward_refs()

PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveAfter.update_forward_refs()

PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveBefore.update_forward_refs()

PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveError.update_forward_refs()

PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveRemove.update_forward_refs()

PickHookCollectionHooksKeyofHooksErrorBeforeAfterWrapRemoveWrap.update_forward_refs()

PipelineScheduleVariables.update_forward_refs()

PipelineScheduleVariablesHeaders.update_forward_refs()

PipelineSchedules.update_forward_refs()

PipelineSchedulesHeaders.update_forward_refs()

Pipelines.update_forward_refs()

PipelinesHeaders.update_forward_refs()

ProjectAccessRequests.update_forward_refs()

ProjectAccessRequestsHeaders.update_forward_refs()

ProjectBadges.update_forward_refs()

ProjectBadgesHeaders.update_forward_refs()

ProjectCustomAttributes.update_forward_refs()

ProjectCustomAttributesHeaders.update_forward_refs()

ProjectDeployTokens.update_forward_refs()

ProjectDeployTokensHeaders.update_forward_refs()

ProjectHooks.update_forward_refs()

ProjectHooksHeaders.update_forward_refs()

ProjectImportExport.update_forward_refs()

ProjectImportExportHeaders.update_forward_refs()

ProjectIssueBoards.update_forward_refs()

ProjectIssueBoardsHeaders.update_forward_refs()

ProjectMembers.update_forward_refs()

ProjectMembersHeaders.update_forward_refs()

ProjectMilestones.update_forward_refs()

ProjectMilestonesHeaders.update_forward_refs()

ProjectSnippetAwardEmojis.update_forward_refs()

ProjectSnippetAwardEmojisHeaders.update_forward_refs()

ProjectSnippetDiscussions.update_forward_refs()

ProjectSnippetDiscussionsHeaders.update_forward_refs()

ProjectSnippetNotes.update_forward_refs()

ProjectSnippetNotesHeaders.update_forward_refs()

ProjectSnippets.update_forward_refs()

ProjectSnippetsHeaders.update_forward_refs()

ProjectVariables.update_forward_refs()

ProjectVariablesHeaders.update_forward_refs()

Projects.update_forward_refs()

ProjectsHeaders.update_forward_refs()

ProtectedBranches.update_forward_refs()

ProtectedBranchesHeaders.update_forward_refs()

ProtectedTags.update_forward_refs()

ProtectedTagsHeaders.update_forward_refs()

PushRules.update_forward_refs()

PushRulesHeaders.update_forward_refs()

ReleaseLinks.update_forward_refs()

ReleaseLinksHeaders.update_forward_refs()

Releases.update_forward_refs()

ReleasesHeaders.update_forward_refs()

RepoMetaData.update_forward_refs()

Repositories.update_forward_refs()

RepositoriesHeaders.update_forward_refs()

RepositoryFiles.update_forward_refs()

RepositoryFilesHeaders.update_forward_refs()

RequestInterfaceObject.update_forward_refs()

RequestInterfaceObjectDefaults.update_forward_refs()


RequesterType.update_forward_refs()

Runners.update_forward_refs()

RunnersHeaders.update_forward_refs()

Search.update_forward_refs()

SearchHeaders.update_forward_refs()

Services.update_forward_refs()

ServicesHeaders.update_forward_refs()

SidekiqMetrics.update_forward_refs()

SidekiqMetricsHeaders.update_forward_refs()

Snippets.update_forward_refs()

SnippetsHeaders.update_forward_refs()

SystemHooks.update_forward_refs()

SystemHooksHeaders.update_forward_refs()

Tags.update_forward_refs()

TagsHeaders.update_forward_refs()

Todos.update_forward_refs()

TodosHeaders.update_forward_refs()

Triggers.update_forward_refs()

TriggersHeaders.update_forward_refs()

UserCustomAttributes.update_forward_refs()

UserCustomAttributesHeaders.update_forward_refs()

UserEmails.update_forward_refs()

UserEmailsHeaders.update_forward_refs()

UserGPGKeys.update_forward_refs()

UserGPGKeysHeaders.update_forward_refs()

UserImpersonationTokens.update_forward_refs()

UserImpersonationTokensHeaders.update_forward_refs()

UserKeys.update_forward_refs()

UserKeysHeaders.update_forward_refs()

Users.update_forward_refs()

UsersHeaders.update_forward_refs()

Version.update_forward_refs()

VersionHeaders.update_forward_refs()

VulnerabilityFindings.update_forward_refs()

VulnerabilityFindingsHeaders.update_forward_refs()

Wikis.update_forward_refs()

WikisHeaders.update_forward_refs()
