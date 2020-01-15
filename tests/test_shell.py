import subprocess
from unittest import mock

from danger_python.shell import resolve_danger_path


@mock.patch('subprocess.run')
def test_danger_path_can_be_resolved(mock_subprocess_run):
    """
    Test that danger-js path can be resolved.
    """
    def fake_run(commands, capture_output):
        if commands == ['which', 'danger'] and capture_output:
            output = '/usr/bin/fake-danger-js \n \r'.encode('utf-8')
            return subprocess.CompletedProcess(commands, 0, stdout=output)
        else:
            raise ValueError('Expected run to receive `which danger` command')

    mock_subprocess_run.side_effect = fake_run
    resolved_path = resolve_danger_path()

    assert resolved_path == "/usr/bin/fake-danger-js"
