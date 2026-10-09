from fastapi import FastAPI, BackgroundTasks
from schemas.analytics import MetricEvent
from services.engine import analytics_engine
from routers.websocket import router as ws_router, manager as ws_manager

app = FastAPI(title="Real-Time Analytics Gateway", version="1.0.0")

app.include_router(ws_router)

@app.get("/")
def root():
    return {"status": "online", "system": "realtime-analytics"}

@app.post("/api/events")
async def ingest_metric(event: MetricEvent, background_tasks: BackgroundTasks):
    summary = analytics_engine.record_event(event.metric_name, event.value)
    
    # Broadcast through WebSockets to dashboard listeners
    background_tasks.add_task(
        ws_manager.broadcast,
        {"event": event.model_dump(mode="json"), "summary": summary}
    )
    return {"status": "accepted", "event_id": event.event_id, "summary": summary}

@app.get("/api/metrics/{metric_name}")
def get_metrics(metric_name: str):
    return analytics_engine.get_summary(metric_name)
