"""Database session management."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from somaai.settings import settings

# Database URL from settings
DATABASE_URL = getattr(settings, "database_url", "sqlite:///./somaai.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    """Get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
