from clillm import __app_name__, __version__, cli
from typer.testing import CliRunner
from pathlib import Path
import os

runner = CliRunner()

TEST_IMAGE1 = "tests/res/test1.jpg"
TEST_IMAGE2 = "tests/res/test2.jpg"
TEST_TEXT1 = "tests/res/test_text1.txt"
TEST_TEXT2 = "tests/res/test_text2.txt"

with open(TEST_TEXT1, "w") as f:
    f.write('This is test text 1. Output ONLY "yes" if you can see this prompt.')
with open(TEST_TEXT2, "w") as f:
    f.write('This is test text 2. Output ONLY "yes" if you can see this prompt.')


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


def test_generate_all_inputs():
    prompt1 = "Test prompt 1"
    prompt2 = "Test prompt 2"

    result = runner.invoke(
        cli.app,
        [
            "llm",
            "generate",
            prompt1,
            prompt2,
            "-i",
            TEST_IMAGE1,
            "-i",
            TEST_IMAGE2,
            "-t",
            TEST_TEXT1,
            "-t",
            TEST_TEXT2,
        ],
    )

    assert result.exit_code == 0

    assert "yes" in result.stdout or "text1" in result.stdout


def test_generate_no_images_or_text():
    prompt1 = 'Test prompt 1. Output "yes" if you can see this text'
    prompt2 = 'Test prompt 2. Output "yes2" if you can see this text'

    result = runner.invoke(
        cli.app,
        [
            "llm",
            "generate",
            prompt1,
            prompt2,
        ],
    )

    assert result.exit_code == 0
    assert "yes" in result.stdout
    assert "yes2" in result.stdout
    # Add assertions to ensure no images or text processing occurred if relevant


def test_generate_single_image():
    prompt1 = 'Do you see the image? Answer "yes" or "no" only'

    result = runner.invoke(
        cli.app,
        [
            "llm",
            "generate",
            prompt1,
            "--image",
            TEST_IMAGE1,
        ],
    )
    assert result.exit_code == 0
    assert "yes" in result.stdout


def test_generate_single_text():
    prompt1 = "Test prompt 1"

    result = runner.invoke(
        cli.app,
        [
            "llm",
            "generate",
            prompt1,
            "--text",
            TEST_TEXT1,
        ],
    )
    print(result.stdout)
    assert result.exit_code == 0
    assert "yes" in result.stdout
