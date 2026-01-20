# SomaAI Architecture

## Overview

SomaAI is built using a modular architecture designed for scalability and maintainability.

## Components

### API Layer
- FastAPI-based REST API
- Versioned endpoints (v1)
- Request/Response validation with Pydantic

### Modules
- **Chat**: Conversation handling
- **Ingest**: Document ingestion pipeline
- **RAG**: Retrieval-Augmented Generation
- **Knowledge**: Vector storage and embeddings
- **Users**: User management
- **Telemetry**: Metrics and tracing

### Providers
- **LLM**: Language model integrations
- **Speech**: Speech processing (future)
- **Storage**: File storage handling

### Database
- Session management
- Models and migrations
