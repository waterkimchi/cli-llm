import typer

from clillm import __app_name__, __version__
from typing import Optional

from .models import gemini
from .utilities import Utilities

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
    help: Optional[bool] = typer.Option(
        None,
        "--help",
        "--h",
        "-help",
        "-h",
        help="Show list of commands and flags with description.",
        is_eager=True,
    ),
):
    if version:
        util.print_menu(__app_name__, __version__)
    elif help:
        ctx.get_help()


app.add_typer(gemini.app, name="gemini")
