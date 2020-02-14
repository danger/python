from dataclasses import dataclass
from typing import Optional


@dataclass
class SubprocessFixture:
    command: str
    exit_code: int
    output: Optional[str]
