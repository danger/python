from unittest import mock

from click.testing import CliRunner

from danger_python.cli.main import cli
from tests.fixtures.shell import (danger_js_missing_path_fixture,
                                  danger_js_path_fixture,
                                  danger_success_fixture, subprocess_fixture)


def test_pr_command_invokes_danger_js_passing_arguments():
    """
    Test that pr command invokes danger_js passing correct arguments.
    """
    runner = CliRunner()
    arguments = [
        "pr",
        "https://github.com/microsoft/TypeScript/pull/34806",
        "--use-github-checks"
    ]
    danger_path = '/usr/bin/danger-js'
    expected_arguments = [
        "pr",
        "https://github.com/microsoft/TypeScript/pull/34806",
        "--use-github-checks",
        "-p",
        "danger-python"
    ]
    danger_fixture = danger_success_fixture(
        danger_path=danger_path,
        output='danger-js output',
        arguments=expected_arguments
    )

    with subprocess_fixture(danger_js_path_fixture(danger_path), danger_fixture):
        result = runner.invoke(cli, arguments)

    assert result.exit_code == 0
    assert result.output == "danger-js output\n"


def test_local_command_invokes_danger_js_passing_arguments():
    """
    Test that local command invokes danger_js passing correct arguments.
    """
    runner = CliRunner()
    arguments = [
        "local",
        "-i",
        "fake_danger_id",
        "-t",
    ]
    danger_path = '/usr/bin/js-danger'
    expected_arguments = [
        "local",
        "-i",
        "fake_danger_id",
        "-t",
        "-p",
        "danger-python"
    ]
    danger_fixture = danger_success_fixture(
        danger_path=danger_path,
        output='parsed local output',
        arguments=expected_arguments
    )

    with subprocess_fixture(danger_js_path_fixture(danger_path), danger_fixture):
        result = runner.invoke(cli, arguments)

    assert result.exit_code == 0
    assert result.output == "parsed local output\n"


def test_ci_command_invokes_danger_js_passing_arguments():
    """
    Test that ci command invokes danger_js passing correct arguments.
    """
    runner = CliRunner()
    arguments = [
        "ci",
        "-v",
        "--no-publish-check",
    ]
    danger_path = '/usr/bin/very-danger'
    expected_arguments = [
        "ci",
        "-v",
        "--no-publish-check",
        "-p",
        "danger-python"
    ]
    danger_fixture = danger_success_fixture(
        danger_path=danger_path,
        output='The output!',
        arguments=expected_arguments
    )

    with subprocess_fixture(danger_js_path_fixture(danger_path), danger_fixture):
        result = runner.invoke(cli, arguments)

    assert result.exit_code == 0
    assert result.output == "The output!\n"


def test_run_command_invokes_dangerfile():
    """
    Test that run command invokes dangerfile.py contents.
    """
    runner = CliRunner()
    dangerfile = "print(\"Hello world\")\n" \
        "print(\"Goodbye world\")"

    with mock.patch("builtins.open", mock.mock_open(read_data=dangerfile)) as mock_file:
        result = runner.invoke(cli, ["run"])
        mock_file.assert_called_with("dangerfile.py", "r")

    assert result.exit_code == 0
    assert result.output == "Hello world\nGoodbye world\n"


def test_default_command_invokes_dangerfile():
    """
    Test that default command invokes dangerfily.py contents.
    """
    runner = CliRunner()
    dangerfile = "print(\"Default command\")"

    with mock.patch("builtins.open", mock.mock_open(read_data=dangerfile)) as mock_file:
        result = runner.invoke(cli)
        mock_file.assert_called_with("dangerfile.py", "r")

    assert result.exit_code == 0
    assert result.output == "Default command\n"
