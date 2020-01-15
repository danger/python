from click.testing import CliRunner

from danger_python.cli.main import cli


def test_runner_discovers_danger_path():
    """
    Test that the runner discovers danger path.
    """
    runner = CliRunner()

    result = runner.invoke(cli, ["run"])

    assert result.exit_code == 0
    assert result.output == "/Users/kuba/.nvm/versions/node/v10.6.0/bin/danger\n"
