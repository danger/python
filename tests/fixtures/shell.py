from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SubprocessFixture:
    commands: List[str]
    exit_code: int
    output: Optional[str]
