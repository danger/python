import subprocess

import click

from danger_python.shell import resolve_danger_path


@click.group()
def cli() -> None:
    pass

@cli.command()
def run() -> None:
    click.echo(resolve_danger_path())
