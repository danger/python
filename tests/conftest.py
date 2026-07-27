import sys
from collections.abc import Iterator
from io import StringIO
from unittest import mock

import pytest
from pyfakefs.fake_filesystem_unittest import Patcher
from testfixtures.popen import MockPopen

from danger_python.danger import Danger
from tests.fixtures.danger import danger_input_file_fixture
from tests.fixtures.shell import SubprocessFixture


@pytest.fixture
def modified_files() -> list[str]:
    return []


@pytest.fixture
def created_files() -> list[str]:
    return []


@pytest.fixture
def deleted_files() -> list[str]:
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
def danger_js_path() -> str | None:
    return None


@pytest.fixture
def danger_js_output() -> str:
    return ""


@pytest.fixture
def danger_js_arguments() -> str:
    return ""


@pytest.fixture
def subprocesses(
    danger_js_path: str | None, danger_js_output: str, danger_js_arguments: str
) -> list[SubprocessFixture]:
    which_danger_subprocess = SubprocessFixture(
        command="which danger",
        exit_code=0 if danger_js_path else 1,
        output=danger_js_path if danger_js_path else "danger not found",
    )

    danger_subprocess: SubprocessFixture | None = None

    if danger_js_path:
        danger_subprocess = SubprocessFixture(
            command=danger_js_path + " " + danger_js_arguments,
            exit_code=0,
            output=danger_js_output,
        )

    return list(filter(None, (which_danger_subprocess, danger_subprocess)))


@pytest.fixture
def run_subprocess(subprocesses: list[SubprocessFixture]) -> Iterator[None]:
    with mock.patch("subprocess.Popen", new_callable=MockPopen) as mock_popen:
        for process in subprocesses:
            mock_popen.set_command(
                process.command,
                returncode=process.exit_code,
                stdout=process.output.encode("utf-8") if process.output else b"",
            )

        yield


@pytest.fixture
def files(
    modified_files: list[str],
    created_files: list[str],
    deleted_files: list[str],
    dangerfile: str,
) -> dict[str, str]:
    return {
        "/var/path/to/file.json": danger_input_file_fixture(
            modified_files=modified_files,
            created_files=created_files,
            deleted_files=deleted_files,
        ),
        "dangerfile.py": dangerfile,
    }


@pytest.fixture
def filesystem(files: dict[str, str]) -> Iterator[None]:
    with Patcher() as patcher:
        assert patcher.fs is not None
        for filename, contents in files.items():
            patcher.fs.create_file(filename, contents=contents)

        yield


@pytest.fixture
def danger(stdin, filesystem) -> Iterator[Danger]:
    Danger.dsl = None
    Danger.results = None
    yield Danger()
    Danger.dsl = None
    Danger.results = None
