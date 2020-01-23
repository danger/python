import sys
from io import StringIO
from typing import Dict, Iterator, List, Optional
from unittest import mock

import pytest
from pyfakefs.fake_filesystem_unittest import Patcher

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
def stdin_str() -> str:
    return "danger://dsl//var/path/to/file.json"


@pytest.fixture
def dangerfile() -> str:
    return ""


@pytest.fixture
def stdin(stdin_str: str) -> Iterator[None]:
    real_stdin = sys.stdin
    sys.stdin = StringIO(stdin_str)
    yield
    sys.stdin = real_stdin


@pytest.fixture
def files(
    modified_files: List[str],
    created_files: List[str],
    deleted_files: List[str],
    dangerfile: str,
) -> Dict[str, str]:
    return {
        "/var/path/to/file.json": danger_input_file_fixture(
            modified_files=modified_files,
            created_files=created_files,
            deleted_files=deleted_files,
        ),
        "dangerfile.py": dangerfile,
    }


@pytest.fixture
def filesystem(files: Dict[str, str]) -> Iterator[None]:
    with Patcher() as patcher:
        for (filename, contents) in files.items():
            patcher.fs.create_file(filename, contents=contents)

        yield


@pytest.fixture
def danger(stdin, filesystem) -> Iterator[Danger]:
    Danger.dsl = None
    Danger.results = None
    yield Danger()
    Danger.dsl = None
    Danger.results = None
