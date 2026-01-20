#!/bin/bash

set -e

echo "Starting development server..."
uv run uvicorn somaai.main:app --reload --host 0.0.0.0 --port 8000
