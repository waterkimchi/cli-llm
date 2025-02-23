from typing import Optional

import typer

from clillm import __app_name__, __version__
from .callbacks.utilities import Utilities

app = typer.Typer(
    help="Access various LLM models in your command-line.",
    invoke_without_command=True,
    no_args_is_help=True,
)

util = Utilities()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        is_eager=True,
    ),
):
    util.print_menu()


@app.command("help")
def help(
    ctx: typer.Context,
):
    print(ctx.parent.get_help())
