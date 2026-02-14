from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    system_id = Column(String, index=True)
    hostname = Column(String)
    os_version = Column(String)
    agent_version = Column(String)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_usage = Column(Float)
    network_usage = Column(Float)
    temperature = Column(Float)
    process_count = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
