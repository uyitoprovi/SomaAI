"""Telemetry tracing."""


class Tracer:
    """Request tracer."""

    def start_span(self, name: str) -> None:
        """Start a trace span."""
        pass

    def end_span(self) -> None:
        """End the current span."""
        pass
