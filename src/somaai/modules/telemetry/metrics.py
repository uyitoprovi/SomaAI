"""Telemetry metrics."""


class MetricsCollector:
    """Metrics collector."""

    def record(self, metric_name: str, value: float) -> None:
        """Record a metric."""
        pass

    def get_metrics(self) -> dict:
        """Get all metrics."""
        return {}
