import sys
from typing import List

import click
from click_default_group import DefaultGroup

from danger_python.decorators import danger_command
from danger_python.exceptions import DangerfileException
from danger_python.shell import execute_dangerfile, invoke_danger


@click.group(cls=DefaultGroup, default="run", default_if_no_args=True)
def cli() -> None:
    pass


@cli.command()
def run() -> None:
    """Runs dangerfile.py as a danger process"""
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
    command = [command_name]
    command.extend(arguments)

    process = invoke_danger(command)
    click.echo(process.stdout)
    sys.exit(process.returncode)
