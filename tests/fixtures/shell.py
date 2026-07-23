from dataclasses import dataclass


@dataclass
class SubprocessFixture:
    command: str
    exit_code: int
    output: str | None
