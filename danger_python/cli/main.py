import functools
import subprocess
import sys

import click

from danger_python.decorators import danger_command
from danger_python.exceptions import SystemConfigurationException
from danger_python.shell import invoke_danger, resolve_danger_path


@click.group()
def cli() -> None:
    pass

@cli.command()
def run() -> None:
    with open('dangerfile.py', 'r') as dangerfile:
        exec(dangerfile.read())

@danger_command(cli, 'pr')
def pr() -> None:
    pass

@danger_command(cli, 'local')
def local() -> None:
    pass

@danger_command(cli, 'ci')
def ci() -> None:
    pass
