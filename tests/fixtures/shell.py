import subprocess
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from unittest import mock


@dataclass
class SubprocessFixture:
    commands: List[str]
    kwargs: Dict[str, Any]
    exit_code: int
    output: Optional[str]
