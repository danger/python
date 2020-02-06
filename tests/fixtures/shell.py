from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SubprocessFixture:
    commands: List[str]
    kwargs: Dict[str, Any]
    exit_code: int
    output: Optional[str]
