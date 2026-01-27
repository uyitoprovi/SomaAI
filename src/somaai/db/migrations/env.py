"""Alembic migrations environment."""

from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, pool
import sys, os

# Add src to path so 'somaai' can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), "../../..", "src"))

import somaai.db.models  # noqa: F401 - imports all models so metadata is populated
from somaai.db.base import Base
from somaai.settings import settings

# Alembic Config object, provides access to .ini file values
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for autogenerate
target_metadata = Base.metadata


def get_url() -> str:
    url = settings.database_url
    if url.startswith("sqlite+aiosqlite"):
        return url.replace("sqlite+aiosqlite", "sqlite")
    if "+asyncpg" in url:
        return url.replace("+asyncpg", "")
    return url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(get_url(), poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
