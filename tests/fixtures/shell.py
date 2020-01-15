import subprocess
from contextlib import contextmanager
from unittest import mock


@contextmanager
def danger_js_path_fixture(path: str):
    def fake_run(commands, capture_output):
        if commands == ['which', 'danger'] and capture_output:
            output = path.encode('utf-8')
            return subprocess.CompletedProcess(commands, 0, stdout=output)
        else:
            raise ValueError('Expected to receive `which danger` command')

    with mock.patch('subprocess.run') as mock_subprocess_run:
        mock_subprocess_run.side_effect = fake_run
        yield


@contextmanager
def danger_js_missing_path_fixture():
    def fake_run(commands, capture_output):
        output = 'danger not found'.encode('utf-8')
        return subprocess.CompletedProcess(commands, 1, stdout=output)

    with mock.patch('subprocess.run') as mock_subprocess_run:
        mock_subprocess_run.side_effect = fake_run
        yield
