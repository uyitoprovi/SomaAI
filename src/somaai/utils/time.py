"""Time utilities."""

from datetime import datetime, timezone


def utc_now() -> datetime:
    """Get current UTC time."""
    return datetime.now(timezone.utc)


def format_timestamp(dt: datetime) -> str:
    """Format a datetime as ISO string."""
    return dt.isoformat()
