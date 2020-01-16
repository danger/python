import subprocess
import sys

import click

from danger_python.exceptions import SystemConfigurationException
from danger_python.shell import invoke_danger, resolve_danger_path


@click.group()
def cli() -> None:
    pass

@cli.command()
def run() -> None:
    try:
        click.echo(resolve_danger_path())
    except SystemConfigurationException as config_exc:
        click.echo(config_exc, err=True)
        raise config_exc


@cli.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('pr_arguments', nargs=-1, type=click.UNPROCESSED)
def pr(pr_arguments) -> None:
    commands = ['pr']
    commands.extend(pr_arguments)

    process = invoke_danger(commands)
    click.echo(process.stdout)
    sys.exit(process.returncode)
