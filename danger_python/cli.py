import sys
from typing import List

import click
from click_default_group import DefaultGroup

from danger_python.decorators import danger_command
from danger_python.exceptions import DangerfileException
from danger_python.shell import execute_dangerfile, invoke_danger


@click.group(cls=DefaultGroup)
def cli() -> None:
    pass


@danger_command(cli, "runner")
def run(arguments: List[str]) -> None:
    print(arguments)
    """Runs dangerfile.py as a danger process"""
    runner()


@danger_command(cli, "runner")
def runner(arguments: List[str]) -> None:
    """Runs dangerfile.py as a danger process, ignoring unknown options"""
    with open("dangerfile.py", "r") as dangerfile:
        try:
            execute_dangerfile(dangerfile.read())
        except DangerfileException as exc:
            click.echo(exc, err=True)
            sys.exit(-1)


@danger_command(cli, "pr")
def pr(arguments: List[str]) -> None:
    """Runs your local Dangerfile against an existing GitHub PR.
       Will not post on the PR"""
    _execute_danger_js("pr", arguments)


@danger_command(cli, "local")
def local(arguments: List[str]) -> None:
    """Runs danger standalone on a repo, useful for git hooks"""
    _execute_danger_js("local", arguments)


@danger_command(cli, "ci")
def ci(arguments: List[str]) -> None:
    """Runs Danger on CI"""
    _execute_danger_js("ci", arguments)


def _execute_danger_js(command_name: str, arguments: List[str]) -> None:
    process = invoke_danger(command_name, arguments)
    click.echo(process.stdout)
    if process:
        click.echo(process.stderr, err=True)
    sys.exit(process.returncode)
