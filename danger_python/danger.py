from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Violation:
    message: str
    file_name: Optional[str] = None
    line: Optional[int] = None


def serialize_violation(violation: Violation) -> Dict[str, Any]:
    violation_json = {
        "message": violation.message,
        "file": violation.file_name,
        "line": violation.line,
    }

    return {key: value for key, value in violation_json.items() if value}
