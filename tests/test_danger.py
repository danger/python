import sys
from io import StringIO
from unittest import mock

import pytest

from danger_python.danger import (Danger, DangerResults, Violation, load_dsl,
                                  serialize_results, serialize_violation)
from tests.fixtures.danger import danger_input_file_fixture


def test_violation_is_correctly_serialized():
    """
    Test that Violation model is correctly serialized.
    """
    violation = Violation(message="Title", file_name="file.py", line=28)

    json = serialize_violation(violation)

    assert json == {"message": "Title", "file": "file.py", "line": 28}


def test_violation_is_correctly_serialized_with_optional_types():
    """
    Test that Violation model is correctly serialized with optional types.
    """
    violation = Violation(message="Message")

    json = serialize_violation(violation)

    assert json == {"message": "Message"}


def test_results_are_correctly_serialized():
    """
    Test that DangerResults model is correctly serialized.
    """
    results = DangerResults(
        fails=[Violation(message="Fail")],
        warnings=[Violation(message="Warning", file_name="warning.py", line=99)],
        messages=[Violation(message="Message")],
        markdowns=[Violation(message="Markdown")],
    )

    json = serialize_results(results)

    assert json == {
        "fails": [{"message": "Fail"},],
        "warnings": [{"message": "Warning", "file": "warning.py", "line": 99},],
        "messages": [{"message": "Message"},],
        "markdowns": [{"message": "Markdown"}],
    }


@pytest.mark.parametrize("modified_files", [["first_file.py", "module/second_file.py"]])
@pytest.mark.parametrize("created_files", [["new_file.py"]])
@pytest.mark.parametrize("deleted_files", [["file_to_delete.py"]])
def test_danger_parses_input(danger):
    """
    Test that Danger parses JSON file with the URL read from the standard input.
    """
    assert danger.git.modified_files == ["first_file.py", "module/second_file.py"]
    assert danger.git.created_files == ["new_file.py"]
    assert danger.git.deleted_files == ["file_to_delete.py"]


def test_load_dsl_method_works():
    """
    Test that loading DSL from file works.
    """
    fake_dsl = danger_input_file_fixture(
        modified_files=["a.py"], created_files=["b.py"], deleted_files=["c.py"]
    )
    stdin = sys.stdin
    sys.stdin = StringIO("danger://dsl//var/folders/zx/123/T/danger-dsl.json")
    expected_url = "/var/folders/zx/123/T/danger-dsl.json"

    with mock.patch("builtins.open", mock.mock_open(read_data=fake_dsl)) as mock_file:
        dsl = load_dsl()
        mock_file.assert_called_with(expected_url, "r")

    sys.stdin = stdin

    assert dsl
    assert dsl.git.modified_files == ["a.py"]
    assert dsl.git.created_files == ["b.py"]
    assert dsl.git.deleted_files == ["c.py"]
