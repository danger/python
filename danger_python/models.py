from typing import List

from pydantic import BaseModel


class GitDSL(BaseModel):
    modified_files: List[str]
    created_files: List[str]
    deleted_files: List[str]


class GithubPullRequestDSL(BaseModel):
    title: str


class GithubDSL(BaseModel):
    pr: GithubPullRequestDSL


class DangerDSL(BaseModel):
    git: GitDSL
    github: GithubDSL
