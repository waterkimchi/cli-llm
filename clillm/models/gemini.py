import os
import typer
import time

from PIL import Image

from dotenv import load_dotenv
from rich import print
from google import genai
from typing import List, Optional
from pathlib import Path

load_dotenv()

app = typer.Typer()

assert os.getenv("GEMINI_KEY") != "", "API Key is not there"
client = genai.Client(api_key=f"{os.getenv('GEMINI_KEY')}")


@app.command("generate")
def generate_text(
    model: str = typer.Option(
        "gemini-2.0-flash",
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
    content = []
    generated_text = ""

    if prompt:
        content.append(prompt)

    if image_files:
        images = [image for image in image_files]
        for image in images:
            content.append(Image.open(image))

    if text_files:
        texts = [open(text_file, "r").read() for text_file in text_files]
        content.append(tx for tx in texts)

    try:
        response = client.models.generate_content_stream(model=model, contents=content)
        if prompt:
            print(f"Prompt: {prompt}")
        if image_files:
            print(f"Image: {image_files}")
        if text_files:
            print(f"Text File: {text_files}")
        print("=========================Reponse Begin=========================")
        for chunk in response:
            formatted_chunk = format_text(chunk.text)
            generated_text += formatted_chunk
            print(formatted_chunk, end="")
        print("\n=========================Reponse End=========================")
    except Exception as e:
        typer.echo(f"Unexpected Error: {e}")
        raise typer.Exit(1)

    if output_file:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file_path = f"{output_file}/response_{timestamp}.txt"
        with open(output_file_path, "w") as f:
            f.write(generated_text)
        typer.echo(f"Output written to {output_file_path}")


def format_text(text_chunk):
    # TODO: add formatting for color and bold
    return text_chunk
