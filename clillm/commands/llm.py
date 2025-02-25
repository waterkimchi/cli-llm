import typer

from ..models import gemini
from typing import List, Optional
from pathlib import Path

# from ..models import utils as model_utils

app = typer.Typer()


@app.command("generate")
def generate(
    model: str = typer.Option(
        "gemini",
        "--model",
        "-m",
        help="The LLM model to use (currently only gemini-2.0-flash).",
    ),
    prompt: List[str] = typer.Argument(..., help="The text prompt for input."),
    image_files: Optional[List[Path]] = typer.Option(
        None, "--image", "-i", help="Path to image files.", exists=True, dir_okay=False
    ),
    text_files: Optional[List[Path]] = typer.Option(
        None, "--text", "-t", help="Path to text files.", exists=True, dir_okay=False
    ),
    output_file: Optional[Path] = typer.Option(
        None, "--output", "-o", help="Path to output file.", dir_okay=True
    ),
):
    input_data = {}
    if image_files:
        input_data["images"] = [image for image in image_files]

    if text_files:
        input_data["text"] = [open(text_file, "r").read() for text_file in text_files]

    gemini.generate_text(
        prompt=prompt,
        images=input_data.get("images"),
        text=input_data.get("text"),
        output=output_file,
    )
