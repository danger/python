import subprocess
from unittest import mock

from danger_python.shell import resolve_danger_path


def test_danger_path_can_be_resolved():
    """
    Test that danger-js path can be resolved.
    """
    def fake_run(commands, capture_output):
        if commands == ['which', 'danger'] and capture_output:
            return subprocess.CompletedProcess(0, stdout='/usr/bin/fake-danger-js\n\n')

    resolved_path = resolve_danger_path()

    assert resolved_path == "/Users/kuba/.nvm/versions/node/v10.6.0/bin/danger"
