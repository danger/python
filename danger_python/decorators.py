import functools
from typing import List

import click

from danger_python.shell import invoke_danger


def danger_command(cli, command_name: str):
    def wrapper(func):
        @cli.command(
            context_settings=dict(ignore_unknown_options=True),
            name=command_name,
        )
        @click.argument('arguments', nargs=-1, type=click.UNPROCESSED)
        def execute_command(arguments: List[str]) -> None:
            command = [command_name]
            command.extend(arguments)

            process = invoke_danger(command)
            click.echo(process.stdout)
            func(process.returncode)

    return wrapper
