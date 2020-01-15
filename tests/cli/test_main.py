from click.testing import CliRunner

from danger_python.cli.main import cli
from tests.fixtures.shell import (danger_js_missing_path_fixture,
                                  danger_js_path_fixture)


def test_runner_discovers_danger_path():
    """
    Test that the runner discovers danger path.
    """
    runner = CliRunner()

    with danger_js_path_fixture("/Users/danger/.nvm/versions/node/v10.6.0/bin/danger"):
        result = runner.invoke(cli, ["run"])

    assert result.exit_code == 0
    assert result.output == "/Users/danger/.nvm/versions/node/v10.6.0/bin/danger\n"

def test_runner_errors_out_when_danger_js_is_not_found():
    """
    Test that the runner discovers danger path.
    """
    runner = CliRunner()

    with danger_js_missing_path_fixture():
        result = runner.invoke(cli, ["run"])

    assert result.exit_code == 1
    assert result.output == "danger-js not found in PATH\n"

def test_pr_command_invokes_danger_js_passing_arguments():
    """
    Test that pr command invokes danger_js passing correct arguments.
    """
    runner = CliRunner()

    result = runner.invoke(cli, [
        "pr",
        "https://github.com/microsoft/TypeScript/pull/34806",
        "--use-github-checks"
    ])

    assert result.exit_code == 0
