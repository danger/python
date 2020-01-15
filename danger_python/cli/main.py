import subprocess

import click


@click.group()
def cli() -> None:
    pass

@cli.command()
def run() -> None:
    process = subprocess.run(['which', 'danger'], capture_output=True)
    if not process.returncode:
        click.echo(process.stdout.strip())
