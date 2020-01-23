import json
import sys
from dataclasses import dataclass, field
from functools import partial
from operator import attrgetter
from typing import Any, Callable, Dict, List, Optional

from .models import DangerDSL, GitDSL, GithubDSL


@dataclass
class Violation:
    message: str
    file_name: Optional[str] = None
    line: Optional[int] = None


@dataclass
class DangerResults:
    fails: List[Violation] = field(default_factory=list)
    warnings: List[Violation] = field(default_factory=list)
    messages: List[Violation] = field(default_factory=list)
    markdowns: List[Violation] = field(default_factory=list)


def serialize_violation(violation: Violation) -> Dict[str, Any]:
    violation_json = {
        "message": violation.message,
        "file": violation.file_name,
        "line": violation.line,
    }

    return {key: value for key, value in violation_json.items() if value}


def serialize_results(results: DangerResults) -> Dict[str, Any]:
    serializer = lambda violations: list(map(serialize_violation, violations))

    return {
        "fails": serializer(results.fails),
        "warnings": serializer(results.warnings),
        "messages": serializer(results.messages),
        "markdowns": serializer(results.markdowns),
    }


def load_dsl() -> DangerDSL:
    file_url = sys.stdin.read().split("danger://dsl/")[-1]

    with open(file_url, "r") as json_file:
        input_json = json.loads(json_file.read())
        return DangerDSL.from_dict(input_json["danger"])


class Danger:
    def __init__(self):
        if not Danger.dsl:
            Danger.dsl = load_dsl()
        if not Danger.results:
            Danger.results = DangerResults()

    dsl: DangerDSL = None
    results: DangerResults = None

    @property
    def git(self) -> GitDSL:
        return Danger.dsl.git

    @property
    def github(self) -> GithubDSL:
        return Danger.dsl.github


def _add_to_results(
    field: Callable[[DangerResults], List[Violation]],
    message: str,
    file_name: Optional[str] = None,
    line: Optional[int] = None,
):
    violation = Violation(message=message, file_name=file_name, line=line)
    field(Danger.results).append(violation)


message = partial(_add_to_results, attrgetter("messages"))
markdown = partial(_add_to_results, attrgetter("markdowns"))
warn = partial(_add_to_results, attrgetter("warnings"))
fail = partial(_add_to_results, attrgetter("fails"))
