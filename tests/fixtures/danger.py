import json
import sys
from contextlib import contextmanager
from io import StringIO
from typing import Any, Dict

from danger_python.danger import Danger


@contextmanager
def danger_input_fixture(input_json: Dict[str, Any]) -> Danger:
    Danger.dsl = None
    stdin = sys.stdin
    sys.stdin = StringIO(json.dumps(input_json))

    yield Danger()

    sys.stdin = stdin
    Danger.dsl = None
