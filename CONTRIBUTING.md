# Contributing to SomaAI

Thank you for your interest in contributing to SomaAI. This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Docker (optional, for containerized development)
- Redis (optional, for caching features)
- Qdrant (optional, for vector database)

### Local Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Rwanda-AI-Network/SomaAI.git
   cd SomaAI
   ```

2. Install dependencies:
   ```bash
   # Core dependencies
   make install
   
   # Or with uv directly
   uv sync
   
   # With caching support (Redis, GPTCache)
   uv sync --extra cache
   
   # With vector database support (Qdrant)
   uv sync --extra vectordb
   
   # All optional dependencies
   uv sync --extra all
   ```

3. Run the development server:
   ```bash
   make dev
   ```

4. (Optional) Run with Docker:
   ```bash
   make docker
   ```

## Development Workflow

### Branch Naming

Use descriptive branch names:
- `feature/add-quiz-generation` - New features
- `fix/retrieval-accuracy` - Bug fixes
- `docs/api-documentation` - Documentation updates

### Making Changes

1. Create a new branch from `main`
2. Make your changes
3. Run linting and tests:
   ```bash
   make lint
   make test
   ```
4. Commit your changes with a clear message
5. Push and open a Pull Request

### Code Style

We use [Ruff](https://github.com/astral-sh/ruff) for linting and formatting:

```bash
# Check linting
ruff check src/

# Auto-fix issues
ruff check src/ --fix

# Format code
ruff format src/
```

### Testing

Write tests for new functionality:

```bash
# Run all tests
make test

# Run specific test file
uv run pytest src/somaai/tests/test_specific.py -v
```

### Available Make Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make install` | Install dependencies with uv |
| `make dev` | Run development server |
| `make lint` | Run linting (ruff + mypy) |
| `make test` | Run tests |
| `make run` | Run the application |
| `make clean` | Clean up build artifacts |
| `make docker` | Run with Docker (app + redis + qdrant) |
| `make docker-stop` | Stop Docker containers |

## Pull Request Guidelines

Before submitting a PR:

- [ ] Code follows the project style guidelines
- [ ] All tests pass locally
- [ ] New functionality includes tests
- [ ] Documentation is updated if needed
- [ ] PR description clearly explains the changes

### Educational Content Guidelines

When contributing features that affect educational content:

- Ensure alignment with Rwanda Education Board (REB) curriculum standards
- Test with both English and Kinyarwanda content where applicable
- Consider accessibility for all students and teachers

## Reporting Issues

When reporting bugs, please include:

- Steps to reproduce the issue
- Expected vs actual behavior
- Environment details (OS, Python version)
- Relevant logs or error messages

## Questions?

For questions or discussions, please open an issue or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the Apache-2.0 license.
