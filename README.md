# Openapi Converter

A tool to convert an `openapi.json` into an `openapi.yaml` with camel cased operationIds.

## Pre-Requisites
1. Install [`python`](https://www.python.org/), any version higher than `3.8.1` will do.
2. Install [`poetry`](https://python-poetry.org/docs/#installation).
3. Run `poetry install`.

## Usage
`poetry run python converter.py path/to/openapi.json` will produce an output into stdout.

Hence, if you want to place it in a file, redirect it yourself:
```bash
poetry run python converter.py path/to/openapi.json > where/to/save/openapi.yaml
```
