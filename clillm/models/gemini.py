import os
import typer
import time
import json

from PIL import Image

from dotenv import load_dotenv
from rich import print
from google import genai
from typing import List, Optional, Dict
from pathlib import Path

load_dotenv()

app = typer.Typer()

assert os.getenv("GEMINI_KEY") != "", "API Key is not there"
client = genai.Client(api_key=f"{os.getenv('GEMINI_KEY')}")

CHAT_LOGS_DIR = Path("logs")
CHAT_LOGS_DIR.mkdir(exist_ok=True)


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


@app.command("create")
def create_chat(
    model: str = typer.Option(
        "gemini-2.0-flash",
        "--mode",
        "-m",
        help="The LLM model to use (currently only gemini-2.0-flash).",
    ),
    name: Optional[str] = typer.Option(None, help="Name of the chat (optional)."),
):
    print("Checking if chat exists...")
    if name is None:
        name = f"chat_{time.strftime('%Y%m%d_%H%M%S')}"
        if name(CHAT_LOGS_DIR / f"{name}.json").exists():
            typer.echo(f"Chat '{name}' already exists.")
            raise typer.Exit(1)
    print("Creating chat...")
    typer.echo(f"Chat '{name}' created.")
    join_chat(name)


@app.command("join")
def join_chat(name: str = typer.Argument(..., help="Name of the chat to join.")):
    if not (CHAT_LOGS_DIR / f"{name}.json").exists():
        typer.echo(f"Chat '{name}' does not exist.")
        print("Creating a new chat...")

    model = client.chats.create(model="gemini-2.0-flash")

    loaded_history = load_chat_from_file(name)
    print("Loading history...")
    model.send_message(f"This was the previous chat log: {loaded_history}")

    typer.echo(f"Joined chat '{name}'. Type 'exit' to leave.")
    while True:
        prompt = typer.prompt("You")
        if prompt.lower() == "exit":
            break
        try:
            response = model.send_message(prompt)
            print(response.text)
            save_chat_to_file(name, model._curated_history)

        except Exception as e:
            typer.echo(f"Error: {e}")
            break


@app.command("delete")
def delete_chat(name: str = typer.Argument(..., help="Name of the chat to delete.")):
    """Deletes an existing chat session."""
    file_path = CHAT_LOGS_DIR / f"{name}.json"
    if file_path.exists():
        os.remove(file_path)
        typer.echo(f"Chat '{name}' deleted.")
    else:
        typer.echo(f"Chat '{name}' does not exist.")


@app.command("list")
def list_chats():
    chat_files = [f.stem for f in CHAT_LOGS_DIR.glob("*.json")]
    if not chat_files:
        print("No chats found.")
    else:
        typer.echo("Available chats:")
        for chat_name in chat_files:
            print(f"- {chat_name}")


def format_text(text_chunk):
    # TODO: add formatting for color and bold
    return text_chunk


def save_chat_to_file(chat_name: str, chat_history: List[Dict[str, str]]):
    file_path = CHAT_LOGS_DIR / f"{chat_name}.json"
    serializable_history = []
    for message in chat_history:
        serializable_history.append(
            {"role": message.role, "parts": [part.text for part in message.parts]}
        )
    with open(file_path, "w") as f:
        json.dump(serializable_history, f, indent=4)


def load_chat_from_file(chat_name: str) -> List[Dict[str, str]]:
    file_path = CHAT_LOGS_DIR / f"{chat_name}.json"
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
