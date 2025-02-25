import os
import typer
import time

from PIL import Image

from dotenv import load_dotenv
from google import genai
from typing import List, Optional


load_dotenv()

assert os.getenv("GEMINI_KEY") != "", "API Key is not there"
client = genai.Client(api_key=f"{os.getenv('GEMINI_KEY')}")


def generate_text(
    prompt: Optional[str],
    images: Optional[List[str]],
    text: Optional[List[str]],
    output: Optional[str],
):
    content = []
    generated_text = ""

    if prompt:
        content.append(prompt)
    if images:
        for image in images:
            content.append(Image.open(image))
    if text:
        content.append(tx for tx in text)

    try:
        response = client.models.generate_content_stream(
            model="gemini-2.0-flash", contents=content
        )
        print("=========================Reponse Begin=========================")
        for chunk in response:
            formatted_chunk = format_text(chunk.text)
            generated_text += formatted_chunk
            print(formatted_chunk, end="")
        print("=========================Reponse End=========================")
    except Exception as e:
        typer.echo(f"Unexpected Error: {e}")
        raise typer.Exit(1)

    if output:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file_path = f"{output}/response_{timestamp}.txt"
        with open(output_file_path, "w") as f:
            f.write(generated_text)
        typer.echo(f"Output written to {output_file_path}")


def format_text(text_chunk):
    # TODO: add formatting for color and bold
    return text_chunk
