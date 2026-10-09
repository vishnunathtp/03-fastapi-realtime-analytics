from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any

class MetricEvent(BaseModel):
    event_id: str = Field(..., description="Unique event identifier")
    source: str = Field(..., description="Service or system producing the metric")
    metric_name: str = Field(..., description="Name of the tracked metric")
    value: float = Field(..., description="Numeric telemetry value")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Optional[Dict[str, Any]] = None

class AggregatedMetrics(BaseModel):
    metric_name: str
    count: int
    mean: float
    min_value: float
    max_value: float
    last_updated: datetime
