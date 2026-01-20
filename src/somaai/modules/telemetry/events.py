"""Telemetry events."""

from typing import Any, Dict


class EventEmitter:
    """Event emitter."""

    def emit(self, event_name: str, data: Dict[str, Any]) -> None:
        """Emit an event."""
        pass
