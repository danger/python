import subprocess
import sys
from io import StringIO
from unittest import mock

import pytest

from danger_python.exceptions import (DangerfileException,
                                      SystemConfigurationException)
from danger_python.shell import (build_danger_command, execute_dangerfile,
                                 resolve_danger_path)
from tests.fixtures.shell import (danger_js_missing_path_fixture,
                                  danger_js_path_fixture, subprocess_fixture)


def test_danger_path_can_be_resolved_if_present():
    """
    Test that danger-js path can be resolved.
    """
    with subprocess_fixture(danger_js_path_fixture("/usr/bin/fake-danger-js \n \r")):
        resolved_path = resolve_danger_path()

    assert resolved_path == "/usr/bin/fake-danger-js"


def test_danger_path_resolver_throws_an_error_if_not_present():
    """
    Test that danger-js path resolver throws an error if not present.
    """
    with subprocess_fixture(danger_js_missing_path_fixture()):
        with pytest.raises(SystemConfigurationException) as config_exc:
            resolve_danger_path()

    assert config_exc.match("danger-js not found in PATH")


def test_build_danger_command_works():
    """
    Test that building correct danger command works.
    """
    with subprocess_fixture(danger_js_path_fixture("/usr/bin/danger-js")):
        first_command = build_danger_command(["pr", "https://pr.url"])
        second_command = build_danger_command(["ci", "-i", "2020", "-t"])

    assert first_command == [
        "/usr/bin/danger-js",
        "pr",
        "https://pr.url",
        "-p",
        "danger-python",
        "-u",
    ]
    assert second_command == [
        "/usr/bin/danger-js",
        "ci",
        "-i",
        "2020",
        "-t",
        "-p",
        "danger-python",
        "-u",
    ]


def test_dangerfile_executor_formats_syntax_error_correctly(danger):
    """
    Test that dangerfile executor formats the SyntaxError correctly.
    """
    dangerfile = "a = 2\n" "b = 8\n" "This is not a valid Python syntax\n"

    with pytest.raises(DangerfileException) as danger_exc:
        execute_dangerfile(dangerfile)

    expected_message = (
        "There was an error when executing dangerfile.py:\n"
        "SyntaxError at line 3: invalid syntax\n\n"
        "Stacktrace:\n"
    )

    assert expected_message in str(danger_exc.value)


def test_dangerfile_executor_formats_name_error_correctly(danger):
    """
    Test that dangerfile executor formats the NameError correctly.
    """
    dangerfile = "a = 2\n" "c += 8\n" "b = 12\n"

    with pytest.raises(DangerfileException) as danger_exc:
        execute_dangerfile(dangerfile)

    expected_message = (
        "There was an error when executing dangerfile.py:\n"
        "NameError at line 2: name 'c' is not defined\n\n"
        "Stacktrace:\n"
    )

    assert str(danger_exc.value).startswith(expected_message)


def test_dangerfile_executor_formats_nester_error_correctly(danger):
    """
    Test that dangerfile executor formats the nested error correctly.
    """
    dangerfile = "import json\n" """json.loads('this is not a json')"""

    with pytest.raises(DangerfileException) as danger_exc:
        execute_dangerfile(dangerfile)

    expected_message = (
        "There was an error when executing dangerfile.py:\n"
        "JSONDecodeError at line 2: Expecting value: line 1 column 1 (char 0)\n\n"
        "Stacktrace:\n"
    )

    assert str(danger_exc.value).startswith(expected_message)
