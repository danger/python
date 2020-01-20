import json
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .models import DangerDSL, GitDSL


@dataclass
class Violation:
    message: str
    file_name: Optional[str] = None
    line: Optional[int] = None


@dataclass
class DangerResults:
    fails: List[Violation]
    warnings: List[Violation]
    messages: List[Violation]
    markdowns: List[Violation]


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

    dsl: DangerDSL = None

    @property
    def git(self) -> GitDSL:
        return Danger.dsl.git
