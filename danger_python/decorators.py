import click


def danger_command(cli, command_name: str):
    def wrapper(func):
        command_wrapper = cli.command(
            context_settings=dict(ignore_unknown_options=True), name=command_name,
        )
        argument_wrapper = click.argument("arguments", nargs=-1, type=click.UNPROCESSED)
        return command_wrapper(argument_wrapper(func))

    return wrapper
