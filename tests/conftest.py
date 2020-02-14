import sys
from io import StringIO
from typing import Dict, Iterator, List, Optional
from unittest import mock

import pytest
from pyfakefs.fake_filesystem_unittest import Patcher
from testfixtures.popen import MockPopen

from danger_python.danger import Danger
from tests.fixtures.danger import danger_input_file_fixture
from tests.fixtures.shell import SubprocessFixture


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
def danger_js_path() -> Optional[str]:
    return None


@pytest.fixture
def danger_js_output() -> str:
    return ""


@pytest.fixture
def danger_js_arguments() -> str:
    return ""


@pytest.fixture
def subprocesses(
    danger_js_path: Optional[str], danger_js_output: str, danger_js_arguments: str
) -> List[SubprocessFixture]:
    which_danger_subprocess = SubprocessFixture(
        command="which danger",
        exit_code=0 if danger_js_path else 1,
        output=danger_js_path if danger_js_path else "danger not found",
    )

    danger_subprocess: Optional[SubprocessFixture] = None

    if danger_js_path:
        danger_subprocess = SubprocessFixture(
            command=danger_js_path + " " + danger_js_arguments,
            exit_code=0,
            output=danger_js_output,
        )

    return list(filter(None, (which_danger_subprocess, danger_subprocess)))


@pytest.fixture
def run_subprocess(subprocesses: List[SubprocessFixture]) -> Iterator[None]:
    with mock.patch("subprocess.Popen", new_callable=MockPopen) as mock_popen:
        for process in subprocesses:
            mock_popen.set_command(
                process.command,
                returncode=process.exit_code,
                stdout=process.output.encode("utf-8") if process.output else None,
            )

        yield


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
