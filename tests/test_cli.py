import json
from typing import List
from unittest import mock

import pytest
from click.testing import CliRunner

from danger_python.cli import cli

DANGER_PR_ARGUMENTS = [
    "pr",
    "https://github.com/microsoft/TypeScript/pull/34806",
    "--use-github-checks",
    "-p",
    "danger-python",
    "-u",
]


@pytest.mark.parametrize("danger_js_path", ["/usr/bin/danger-js"])
@pytest.mark.parametrize("danger_js_output", ["danger-js output"])
@pytest.mark.parametrize("danger_js_arguments", [DANGER_PR_ARGUMENTS])
@pytest.mark.usefixtures("run_subprocess")
def test_pr_command_invokes_danger_js_passing_arguments():
    """
    Test that pr command invokes danger_js passing correct arguments.
    """
    runner = CliRunner()
    arguments = [
        "pr",
        "https://github.com/microsoft/TypeScript/pull/34806",
        "--use-github-checks",
    ]
    result = runner.invoke(cli, arguments)

    assert result.exit_code == 0
    assert result.output == "danger-js output\n"


DANGER_LOCAL_ARGUMENTS = [
    "local",
    "-i",
    "fake_danger_id",
    "-t",
    "-p",
    "danger-python",
    "-u",
]


@pytest.mark.parametrize("danger_js_path", ["/usr/bin/js-danger"])
@pytest.mark.parametrize("danger_js_output", ["parsed local output"])
@pytest.mark.parametrize("danger_js_arguments", [DANGER_LOCAL_ARGUMENTS])
@pytest.mark.usefixtures("run_subprocess")
def test_local_command_invokes_danger_js_passing_arguments():
    """
    Test that local command invokes danger_js passing correct arguments.
    """
    runner = CliRunner()
    arguments = ["local", "-i", "fake_danger_id", "-t"]
    result = runner.invoke(cli, arguments)

    assert result.exit_code == 0
    assert result.output == "parsed local output\n"


DANGER_CI_ARGUMENTS = ["ci", "-v", "--no-publish-check", "-p", "danger-python", "-u"]


@pytest.mark.parametrize("danger_js_path", ["/usr/bin/very-danger"])
@pytest.mark.parametrize("danger_js_arguments", [DANGER_CI_ARGUMENTS])
@pytest.mark.parametrize("danger_js_output", ["The output!"])
@pytest.mark.usefixtures("run_subprocess")
def test_ci_command_invokes_danger_js_passing_arguments():
    """
    Test that ci command invokes danger_js passing correct arguments.
    """
    runner = CliRunner()
    arguments = ["ci", "-v", "--no-publish-check"]
    result = runner.invoke(cli, arguments)

    assert result.exit_code == 0
    assert result.output == "The output!\n"


@pytest.mark.parametrize(
    "dangerfile", ['print("Hello world")\n' 'print("Goodbye world")']
)
@pytest.mark.usefixtures("danger")
def test_run_command_invokes_dangerfile():
    """
    Test that run command invokes dangerfile.py contents.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["run"])

    assert result.exit_code == 0
    assert result.output.startswith("Hello world\nGoodbye world\n")


@pytest.mark.parametrize("dangerfile", ["This is not a valid syntax of Python"])
@pytest.mark.usefixtures("danger")
def test_run_command_shows_traceback_when_dangerfile_fails():
    """
    Test that run command shows traceback when dangerfile.py fails.
    """
    runner = CliRunner(mix_stderr=False)
    result = runner.invoke(cli, ["run"])

    expected_error = (
        "There was an error when executing dangerfile.py:\n"
        "SyntaxError at line 1: invalid syntax\n\n"
        "Stacktrace:\n"
    )

    assert result.exit_code == -1
    assert result.stderr.startswith(expected_error)


@pytest.mark.parametrize("dangerfile", ['print("Default command")'])
@pytest.mark.usefixtures("danger")
def test_default_command_invokes_dangerfile():
    """
    Test that default command invokes dangerfily.py contents.
    """
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert result.output.startswith("Default command\n")


@pytest.mark.parametrize("modified_files", [["a.py", "b.py"]])
@pytest.mark.parametrize("dangerfile", ["print(danger.git.modified_files)"])
@pytest.mark.usefixtures("danger")
def test_executing_dangerfile_passes_danger_instance_to_the_script():
    """
    Test that executing run command passes danger instance with parsed input
    to the Dangerfile locals.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["run"])

    assert result.exit_code == 0
    assert result.output.startswith("['a.py', 'b.py']\n")


@pytest.mark.parametrize(
    "dangerfile",
    [
        'warn("This is the final warning")\n'
        'fail("You are going to fail")\n'
        'message("Hello world")\n'
        'markdown("Test markdown")\n'
    ],
)
@pytest.mark.usefixtures("danger")
def test_executing_dangerfile_prints_results_to_stdout():
    """
    Test that executing run command reports results back to output.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["run"])

    expected_json = {
        "fails": [{"message": "You are going to fail"}],
        "warnings": [{"message": "This is the final warning"}],
        "messages": [{"message": "Hello world"}],
        "markdowns": [{"message": "Test markdown"}],
    }

    assert result.exit_code == 0
    assert result.output == json.dumps(expected_json) + "\n"
