# CLI LLM
<div align="center">
  <img src="https://github.com/user-attachments/assets/bcbdd4b2-5eed-4671-8e08-6a94883f4daa" width="40%" alt="DeepSeek-R1" />
</div>
<hr>
<div align="center" style="line-height: 1;">
    <a href="https://github.com/waterkimchi/cli-llm/"><img src="https://img.shields.io/github/stars/waterkimchi/cli-llm" alt="Stars Badge"/></a>
<a href="https://github.com/waterkimchi/cli-llm"><img src="https://img.shields.io/github/forks/waterkimchi/cli-llm" alt="Forks Badge"/></a>
<a href="https://github.com/waterkimchi/cli-llm"><img src="https://img.shields.io/github/issues-pr/waterkimchi/cli-llm" alt="Pull Requests Badge"/></a>
<a href="https://github.com/waterkimchi/cli-llm"><img src="https://img.shields.io/github/issues/waterkimchi/cli-llm" alt="Issues Badge"/></a>
<a href="https://github.com/waterkimchi/cli-llm"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/waterkimchi/cli-llm?color=2b9348"></a>
<a href="https://github.com/waterkimchi/cli-llm/blob/master/LICENSE"><img src="https://img.shields.io/github/license/waterkimchi/cli-llm?color=2b9348" alt="License Badge"/></a>
</div>
<br>

A CLI application that leverages LLMs to generate text(currently only Gemini-2.0-flash support) in the command line. Foundationally uses [typer](https://typer.tiangolo.com) library for CLI support and various LLM APIs for the actual service. CLI-LLM achieves to make LLMs more accessbile and customized through its unique command-line UI and to further extend the capabilities.

## Features

* **Streaming Output:** Displays generated text as it's produced by the LLM API, providing a more interactive experience.
* **Various Inputs:**  Can include prompts, image paths, and existing text as context for the models.
* **Error Handling:** Includes basic error handling to catch and display issues with the API or other parts of the application.

### TODO:
* **Formatted Output:** Uses ANSI escape codes to add colors and symbols to the output, making it easier to read and understand.
* **Other LLMs:** OpenAI, Claude, Grok, etc.
* **Status:** Listing service status for the models.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/waterkimchi/cli-llm.git
   cd cli-llm
2. **Install Script**
   ```bash
   sh install.vm.sh
3. **Set up API Keys**
   ```bash
   cp .env.example .env
   ```
   Add your LLM API keys for each service provided.

## Usage
### Virtual Environment
If you followed the above installation proccess, you would have a venv/ directory in the root of the project. Simply run:
```bash
source venv/bin/activate
```
to enter the vm and run:
```bash
clillm -h
```


