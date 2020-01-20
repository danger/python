import json
import sys
from contextlib import contextmanager
from io import StringIO
from typing import Any, Dict
from unittest import mock

from danger_python.danger import Danger


@contextmanager
def danger_json_input_fixture(input_json: Dict[str, Any]) -> Danger:
    Danger.dsl = None
    stdin = sys.stdin
    read_data = json.dumps(input_json)
    sys.stdin = StringIO("/var/path/to/json/file.json")

    with mock.patch("builtins.open", mock.mock_open(read_data=read_data)):
        yield Danger()

    sys.stdin = stdin
    Danger.dsl = None
