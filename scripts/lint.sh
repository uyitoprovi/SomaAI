#!/bin/bash

set -e

echo "Running linting..."
uv run ruff check src/
uv run ruff format --check src/
uv run mypy src/
