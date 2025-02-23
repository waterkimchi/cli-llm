import typer

app = typer.Typer()


@app.command()
def name(name: str):
    print(f"Hello, {name}!")
