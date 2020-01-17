import functools
import subprocess
import sys
import traceback
from typing import List

import click

from click_default_group import DefaultGroup
from danger_python.decorators import danger_command
from danger_python.exceptions import DangerfileException, SystemConfigurationException
from danger_python.shell import execute_dangerfile, invoke_danger, resolve_danger_path


@click.group(cls=DefaultGroup, default="run", default_if_no_args=True)
def cli() -> None:
    pass


@cli.command()
def run() -> None:
    with open("dangerfile.py", "r") as dangerfile:
        try:
            execute_dangerfile(dangerfile.read())
        except DangerfileException as exc:
            click.echo(exc, err=True)
            sys.exit(-1)


@danger_command(cli, "pr")
def pr(arguments: List[str]) -> None:
    _execute_danger_js("pr", arguments)


@danger_command(cli, "local")
def local(arguments: List[str]) -> None:
    _execute_danger_js("local", arguments)


@danger_command(cli, "ci")
def ci(arguments: List[str]) -> None:
    _execute_danger_js("ci", arguments)


def _execute_danger_js(command_name: str, arguments: List[str]) -> None:
    command = [command_name]
    command.extend(arguments)

    process = invoke_danger(command)
    click.echo(process.stdout)
    sys.exit(process.returncode)
