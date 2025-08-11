"""Console script for tg_notifier."""

import typer
from rich.console import Console

from tg_notifier import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for tg_notifier."""
    console.print("Replace this message by putting your code into "
               "tg_notifier.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
