import click

from .cmd import client


class Plant:
    def __init__(self, debug=False):
        self.debug = debug


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def cli(ctx, debug):
    """Root command for the Plantd command line utility."""
    ctx.obj = Plant(debug)


cli.add_command(client)
