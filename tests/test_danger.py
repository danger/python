from danger_python.danger import Violation, serialize_violation


def test_violation_is_correctly_serialized():
    """
    Test that Violation model is correctly serialized.
    """
    violation = Violation(message="Title", file_name="file.py", line=28)

    json = serialize_violation(violation)

    assert "message" in json
    assert "file" in json
    assert "line" in json
    assert json["message"] == "Title"
    assert json["file"] == "file.py"
    assert json["line"] == 28


def test_violation_is_correctly_serialized_with_optional_types():
    """
    Test that Violation model is correctly serialized with optional types.
    """
    violation = Violation(message="Message")

    json = serialize_violation(violation)

    assert "message" in json
    assert "file" not in json
    assert "line" not in json
    assert json["message"] == "Message"
