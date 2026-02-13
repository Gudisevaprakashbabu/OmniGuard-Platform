from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base
from datetime import datetime, timezone


class TelemetryRecord(Base):
    __tablename__ = "telemetry_records"

    id = Column(Integer, primary_key=True, index=True)

    system_id = Column(String)
    hostname = Column(String)
    os_version = Column(String)
    agent_version = Column(String)

    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_usage = Column(Float)

    network_usage = Column(Float)
    temperature = Column(Float)
    process_count = Column(Integer)

    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
