from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional


class TelemetryData(BaseModel):
    system_id: str
    hostname: Optional[str] = None
    os_version: Optional[str] = None
    agent_version: Optional[str] = None

    cpu_usage: float = Field(..., ge=0, le=100)
    memory_usage: float = Field(..., ge=0, le=100)
    disk_usage: float = Field(..., ge=0, le=100)

    network_usage: Optional[float] = None
    temperature: Optional[float] = None
    process_count: Optional[int] = None

    client_timezone: Optional[str] = "UTC"

    # Auto UTC timestamp if client does not send one
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
