from danger_python.danger import (Danger, DangerResults, Violation,
                                  serialize_results, serialize_violation)
from tests.fixtures.danger import danger_input_fixture


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


def test_danger_parses_input_lazily():
    """
    Test that Danger parses JSON read from the standard input lazily.
    """
    input_json = {
        "danger": {
            "git": {
                "modified_files": ["first_file.py", "module/second_file.py"],
                "created_files": ["new_file.py",],
                "deleted_files": ["file_to_delete.py",],
            }
        }
    }

    with danger_input_fixture(input_json) as danger:
        input_json["danger"]["git"]["created_files"] = []

        assert danger.git.modified_files == ["first_file.py", "module/second_file.py"]
        assert danger.git.created_files == ["new_file.py"]
        assert danger.git.deleted_files == ["file_to_delete.py"]
        assert Danger().git.created_files == ["new_file.py"]
