from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class GitDSL:
    modified_files: List[str]
    created_files: List[str]
    deleted_files: List[str]


@dataclass_json
@dataclass
class GithubPullRequestDSL:
    title: str


@dataclass_json
@dataclass
class GithubDSL:
    pr: GithubPullRequestDSL


@dataclass_json
@dataclass
class DangerDSL:
    git: GitDSL
    github: GithubDSL
