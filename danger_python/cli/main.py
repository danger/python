import functools
import subprocess
import sys
import traceback

import click

from click_default_group import DefaultGroup
from danger_python.decorators import danger_command
from danger_python.exceptions import (DangerfileException,
                                      SystemConfigurationException)
from danger_python.shell import (execute_dangerfile, invoke_danger,
                                 resolve_danger_path)


@click.group(cls=DefaultGroup, default='run', default_if_no_args=True)
def cli() -> None:
    pass

@cli.command()
def run() -> None:
    with open('dangerfile.py', 'r') as dangerfile:
        try:
            execute_dangerfile(dangerfile.read())
        except DangerfileException as exc:
            click.echo(exc, err=True)
            sys.exit(-1)

@danger_command(cli, 'pr')
def pr() -> None:
    pass

@danger_command(cli, 'local')
def local() -> None:
    pass

@danger_command(cli, 'ci')
def ci() -> None:
    pass
