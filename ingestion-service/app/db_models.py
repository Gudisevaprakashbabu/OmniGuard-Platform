# Database table structure
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone

from .database import Base


class TelemetryRecord(Base):
    __tablename__ = "telemetry_records"

    id = Column(Integer, primary_key=True, index=True)

    # System Information
    system_id = Column(String, index=True)
    hostname = Column(String)
    os_version = Column(String)
    agent_version = Column(String)

    # Resource Metrics
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_usage = Column(Float)
    network_usage = Column(Float)
    temperature = Column(Float)
    process_count = Column(Integer)

    # Timestamp
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
