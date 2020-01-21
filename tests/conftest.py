import sys
from io import StringIO
from typing import Iterator, List, Optional
from unittest import mock

import pytest

from danger_python.danger import Danger
from tests.fixtures.danger import danger_input_file_fixture


@pytest.fixture
def modified_files() -> List[str]:
    return []


@pytest.fixture
def created_files() -> List[str]:
    return []


@pytest.fixture
def deleted_files() -> List[str]:
    return []


@pytest.fixture
def danger(
    modified_files: List[str], created_files: List[str], deleted_files: List[str]
) -> Iterator[Danger]:
    Danger.dsl = None
    stdin = sys.stdin
    sys.stdin = StringIO("/var/path/to/json/file.json")
    read_data = danger_input_file_fixture(
        modified_files=modified_files,
        created_files=created_files,
        deleted_files=deleted_files,
    )

    with mock.patch("builtins.open", mock.mock_open(read_data=read_data)):
        yield Danger()

    sys.stdin = stdin
    Danger.dsl = None
