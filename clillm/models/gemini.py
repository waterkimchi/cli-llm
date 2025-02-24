import os
import typer

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
):
    content = []

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
        for chunk in response:
            formatted_chunk = format_text(chunk.text)  # Format the chunk
            print(formatted_chunk, end="")
    except Exception as e:
        typer.echo(f"Unexpected Error: {e}")
        raise typer.Exit(1)


def format_text(text_chunk):
    # TODO: add formatting for color and bold
    return text_chunk
