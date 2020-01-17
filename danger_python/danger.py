from dataclasses import dataclass
from typing import Any, Dict, List, Optional


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
    return {
        "fails": list(map(serialize_violation, results.fails)),
        "warnings": list(map(serialize_violation, results.warnings)),
        "messages": list(map(serialize_violation, results.messages)),
        "markdowns": list(map(serialize_violation, results.markdowns)),
    }
