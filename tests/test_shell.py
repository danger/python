import subprocess
from unittest import mock

from danger_python.shell import resolve_danger_path
from tests.fixtures.shell import danger_js_path_fixture


def test_danger_path_can_be_resolved():
    """
    Test that danger-js path can be resolved.
    """
    with danger_js_path_fixture('/usr/bin/fake-danger-js \n \r'):
        resolved_path = resolve_danger_path()

    assert resolved_path == "/usr/bin/fake-danger-js"
