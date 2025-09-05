# 4-minute-python

This repo contains code from my series of 4 minute videos on python.

## Prerequisites

- [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
- [python 3.13>](https://www.python.org/downloads/)

## How to run

1. Fork the repo
1. Clone your fork

    ```sh
    git clone https://github.com/username/4-minute-python.git
    ```

1. Create a virtual environment

    ```sh
    uv venv
    ```

1. Activate the virtual environment

    ```sh
    source uv/bin/activate
    ```

1. Install dependencies

    ```sh
    uv sync
    ```

1. Run any snippet you'd like by moving into its directory and running:

    ```sh
    uv run file_name.py
    ```

## Available Snippets

| Video  | Path                 | Files                                                         | Description |
|--------|----------------------|---------------------------------------------------------------|-------------|
| video1 | `snippets/video1/`   | `for_loop.py`, `list_comp.py`, `README.md`, `words.txt`       | Compares a basic for-loop versus a list comprehension using the same word list. |
| video2 | `snippets/video2/`   | `gen_exps.py`, `README.md`, `words.txt`                       | Demonstrates generator expressions and their memory/iteration behavior. |
| video3 | `snippets/video3/`   | (empty for now)                                               | Placeholder for upcoming snippet(s). |

