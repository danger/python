from click.testing import CliRunner

from danger_python.cli.main import cli
from tests.fixtures.shell import danger_js_path_fixture


def test_runner_discovers_danger_path():
    """
    Test that the runner discovers danger path.
    """
    runner = CliRunner()

    with danger_js_path_fixture("/Users/danger/.nvm/versions/node/v10.6.0/bin/danger"):
        result = runner.invoke(cli, ["run"])

    assert result.exit_code == 0
    assert result.output == "/Users/danger/.nvm/versions/node/v10.6.0/bin/danger\n"
