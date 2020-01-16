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


@contextmanager
def subprocess_fixture(*fixtures: List[SubprocessFixture]):
    def match_fixture(fixture: SubprocessFixture, commands: List[str], **kwargs):
        kwarg_match = lambda kv: kwargs.get(kv[0], None) == kv[1]
        kwargs_match = all(map(kwarg_match, fixture.kwargs.items()))
        return fixture.commands == commands and kwargs_match

    def fake_run(commands, **kwargs):
        try:
            matcher = lambda f: match_fixture(f, commands, **kwargs)
            return __completed_process(next(filter(matcher, fixtures)))
        except StopIteration:
            msg = f"Could not find fixture for call with {commands} and {kwargs}"
            raise ValueError(msg)

    with mock.patch("subprocess.run") as mock_subprocess_run:
        mock_subprocess_run.side_effect = fake_run
        yield


def __completed_process(fixture: SubprocessFixture) -> subprocess.CompletedProcess:
    return subprocess.CompletedProcess(
        fixture.commands, fixture.exit_code, stdout=fixture.output.encode("utf-8")
    )


def danger_js_path_fixture(path: str) -> SubprocessFixture:
    return SubprocessFixture(
        commands=["which", "danger"],
        kwargs={"capture_output": True},
        exit_code=0,
        output=path,
    )


def danger_js_missing_path_fixture():
    return SubprocessFixture(
        commands=["which", "danger"],
        kwargs={"capture_output": True},
        exit_code=1,
        output="danger not found",
    )


def danger_success_fixture(
    danger_path: str, output: Optional[str], arguments: List[str]
) -> SubprocessFixture:
    return SubprocessFixture(
        commands=[danger_path] + arguments,
        kwargs={"capture_output": True},
        exit_code=0,
        output=output,
    )
