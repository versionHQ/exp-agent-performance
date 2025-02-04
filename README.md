# Overview

![MIT license](https://img.shields.io/badge/License-MIT-green)
![python ver](https://img.shields.io/badge/Python-3.11/3.12-orange)


Experiment on AI agent performance using `versionhq` and `pydantic`.


**Visit:**

- [PyPI](https://pypi.org/project/versionhq/)
- [Github](https://github.com/versionHQ/multi-agent-system)
- [Documentation](https://chief-oxygen-8a2.notion.site/Documentation-17e923685cf98001a5fad5c4b2acd79b?pvs=4) *under review
- [Process](https://medium.com/@kuriko-iwai/48d42fc57b71)

<hr />

## Key Features

Generate multi-agent systems based on the task complexity, execute tasks, and evaluate output based on the given criteria. 

Agents are model-agnostic, and can handle and share RAG tools, knowledge, memory, and callbacks among other agents.


<hr />

## Quick Start

1. Install `uv` package manager:

   For MacOS:

   ```
   brew install uv
   ```

   For Ubuntu/Debian:

   ```
   sudo apt-get install uv
   ```

2. Install dependencies:
   ```
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

* In case of AssertionError/module mismatch, run Python version control using `.pyenv`
   ```
   pyenv install 3.12.8
   pyenv global 3.12.8  (optional: `pyenv global system` to get back to the system default ver.)
   uv python pin 3.12.8
   echo 3.12.8 > .python-version
   ```

3. Set up environment variables:
   Create `.env` file in the project root and add the following:
   ```
   OPENAI_API_KEY=your-openai-api-key
   GEMINI_API_KEY=your-gemini-api-key
   OPENROUTER_API_KEY=your-openrouter-api-key
   ```

4. Run:
   ```
   uv run main.py
   ```

<hr />

## Customizing

- To add or refine an agent, use `src/agents.py`.

- To add or refine a task, use `src/tasks.py`.


<hr />

## Results

<img src="https://res.cloudinary.com/dfeirxlea/image/upload/v1738634968/pj_m_test/ulzp0wi0rptq61vkirkq.png">

(Feb 3, 2025)

<hr />

## Trouble Shooting

Common issues and solutions:
- API key errors: Ensure all API keys in the `.env` file are correct and up to date. Make sure to add `load_dotenv()` on the top of the python file to apply the latest environment values.
- Database connection issues: Check if the Chroma DB is properly initialized and accessible.
- Memory errors: If processing large contracts, you may need to increase the available memory for the Python process.
- Issues related to the Python version: Use Python 3.12.x as default by running `uv venv --python 3.12.8` and `uv python pin 3.12.8`.
- Issues related to dependencies: `uv cache clean`, `uv venv`, and run `uv pip install -r requirements.txt -v`.
- `reportMissingImports` error from pyright after installing the package: This might occur when installing new libraries while VSCode is running. Open the command pallete (ctrl + shift + p) and run the Python: Restart language server task.
