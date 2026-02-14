from pydantic import BaseModel
from datetime import datetime

class TelemetryCreate(BaseModel):
    system_id: str
    hostname: str
    os_version: str
    agent_version: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_usage: float
    temperature: float
    process_count: int
    timestamp: datetime
