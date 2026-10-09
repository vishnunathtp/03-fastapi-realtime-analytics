from typing import Dict, List
from collections import defaultdict
from datetime import datetime

class AnalyticsEngine:
    def __init__(self):
        self._history: Dict[str, List[float]] = defaultdict(list)
        self._last_event: Dict[str, datetime] = {}

    def record_event(self, metric_name: str, value: float) -> dict:
        self._history[metric_name].append(value)
        self._last_event[metric_name] = datetime.utcnow()
        return self.get_summary(metric_name)

    def get_summary(self, metric_name: str) -> dict:
        values = self._history.get(metric_name, [])
        if not values:
            return {}
        return {
            "metric_name": metric_name,
            "count": len(values),
            "mean": round(sum(values) / len(values), 2),
            "min_value": min(values),
            "max_value": max(values),
            "last_updated": self._last_event.get(metric_name, datetime.utcnow()).isoformat()
        }

analytics_engine = AnalyticsEngine()
