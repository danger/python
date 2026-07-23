import json
import sys
from collections.abc import Callable
from functools import partial
from operator import attrgetter
from typing import Any

from pydantic import BaseModel

from .models import (
    BitBucketCloudJSONDSL,
    BitBucketServerJSONDSL,
    DangerDSLJSONType,
    DangerDSLJSONTypeSettings,
    GitHubDSL,
    GitJSONDSL,
    GitLabDSL,
)


class Violation(BaseModel):
    message: str
    file_name: str | None = None
    line: int | None = None

    class Config:
        allow_population_by_field_name = True
        fields = {"message": "message", "file_name": "file", "line": "line"}


class DangerMeta(BaseModel):
    href: str = "https://danger.systems/python"
    name: str = "danger-python"

    class Config:
        fields = {"href": "runtimeHref", "name": "runtimeName"}


class DangerResults(BaseModel):
    fails: list[Violation] = []
    warnings: list[Violation] = []
    messages: list[Violation] = []
    markdowns: list[Violation] = []
    meta: DangerMeta = DangerMeta()


def serialize_violation(violation: Violation) -> dict[str, Any]:
    return violation.dict(exclude_none=True, by_alias=True)


def serialize_results(results: DangerResults) -> dict[str, Any]:
    return results.dict(exclude_none=True, by_alias=True)


def load_dsl() -> DangerDSLJSONType:
    file_url = sys.stdin.read().split("danger://dsl/")[-1]

    with open(file_url) as json_file:
        input_json = json.loads(json_file.read())
        return DangerDSLJSONType(**input_json["danger"])


class Danger:
    def __init__(self):
        if not Danger.dsl:
            Danger.dsl = load_dsl()
        if not Danger.results:
            Danger.results = DangerResults()

    dsl: DangerDSLJSONType | None = None
    results: DangerResults | None = None

    @property
    def git(self) -> GitJSONDSL | None:
        assert Danger.dsl is not None
        return Danger.dsl.git

    @property
    def github(self) -> GitHubDSL | None:
        assert Danger.dsl is not None
        return Danger.dsl.github

    @property
    def bitbucket_cloud(self) -> BitBucketCloudJSONDSL | None:
        assert Danger.dsl is not None
        return Danger.dsl.bitbucket_cloud

    @property
    def bitbucket_server(self) -> BitBucketServerJSONDSL | None:
        assert Danger.dsl is not None
        return Danger.dsl.bitbucket_server

    @property
    def gitlab(self) -> GitLabDSL | None:
        assert Danger.dsl is not None
        return Danger.dsl.gitlab

    @property
    def settings(self) -> DangerDSLJSONTypeSettings | None:
        assert Danger.dsl is not None
        return Danger.dsl.settings


def _add_to_results(
    field: Callable[[DangerResults], list[Violation]],
    message: str,
    file_name: str | None = None,
    line: int | None = None,
):
    assert Danger.results is not None
    violation = Violation(message=message, file_name=file_name, line=line)
    field(Danger.results).append(violation)


message = partial(_add_to_results, attrgetter("messages"))
markdown = partial(_add_to_results, attrgetter("markdowns"))
warn = partial(_add_to_results, attrgetter("warnings"))
fail = partial(_add_to_results, attrgetter("fails"))
