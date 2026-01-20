# SomaAI

An AI-enabled digital platform designed to improve teaching and learning across Rwanda. SomaAI provides students with practice materials and explanatory support based on official national resources, and provides teachers with rapid, practical assistance for preparing quizzes, tests, and clear explanations of complex topics.

## Features

- **AI-Powered Learning Assistant** - Contextual explanations with analogies and real-world examples
- **RAG-Based Retrieval** - Retrieval-Augmented Generation using official curriculum materials
- **Quiz & Test Generation** - Automated assessment creation for teachers
- **Multi-Language Support** - English content support (Kinyarwanda and French support in progress)

## Requirements

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- Docker (optional, for containerized deployment)
- Redis (optional, for caching)
- Qdrant (optional, for vector storage)

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Rwanda-AI-Network/SomaAI.git
cd SomaAI

# Install dependencies
uv sync

# Copy environment variables
cp .env.example .env
```

### Running Locally

```bash
# Run with Make
make dev

# Or directly with uv
uv run uvicorn somaai.main:app --reload --port 8000
```

### Running with Docker

```bash
# Build and run
./run.sh docker

# Or use docker-compose directly
docker-compose -f docker/docker-compose.yml up --build
```

## Development

```bash
# Install dependencies
make install

# Install with caching support
uv sync --extra cache

# Install with vector database support
uv sync --extra vectordb

# Install all optional dependencies
uv sync --extra all

# Run development server
make dev

# Run linting
make lint

# Run tests
make test

# Run the application
make run

# Clean build artifacts
make clean
```

## Available Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make install` | Install dependencies with uv |
| `make dev` | Run development server |
| `make lint` | Run linting (ruff + mypy) |
| `make test` | Run tests |
| `make run` | Run the application |
| `make clean` | Clean up build artifacts |
| `make docker` | Run with Docker |
| `make docker-stop` | Stop Docker containers |

## Project Structure

```
src/somaai/
├── api/           # FastAPI endpoints
├── cache/         # Caching (Redis, semantic)
├── modules/       # Core business logic
│   ├── chat/      # Chat handling
│   ├── ingest/    # Document ingestion
│   ├── rag/       # Retrieval & generation
│   ├── knowledge/ # Embeddings & vector storage
│   └── telemetry/ # Metrics & tracing
├── providers/     # External service integrations
└── database/      # Database models & migrations
```

## Documentation

- [API Documentation](docs/api.md)
- [Architecture Overview](docs/architecture.md)
- [Contributing Guide](CONTRIBUTING.md)

## License

Apache-2.0 license - see [LICENSE](LICENSE) for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.