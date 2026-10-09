# 03-fastapi-realtime-analytics

High-throughput real-time streaming analytics engine powered by FastAPI, Pydantic v2, and WebSockets.

## Features
- Fast asynchronous ingestion endpoint for telemetry events
- In-memory aggregation engine computing running averages and min/max stats
- WebSocket event broadcaster notifying active client subscribers

## Running the Application
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
