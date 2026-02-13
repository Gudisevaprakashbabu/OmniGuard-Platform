from sqlalchemy.orm import Session
from . import db_models
from .models import TelemetryData


def create_telemetry_record(db: Session, data: TelemetryData):
    record = db_models.TelemetryRecord(
        system_id=data.system_id,
        hostname=data.hostname,
        os_version=data.os_version,
        agent_version=data.agent_version,
        cpu_usage=data.cpu_usage,
        memory_usage=data.memory_usage,
        disk_usage=data.disk_usage,
        network_usage=data.network_usage,
        temperature=data.temperature,
        process_count=data.process_count,
        timestamp=data.timestamp
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def get_all_telemetry(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.TelemetryRecord).offset(skip).limit(limit).all()


def get_telemetry_by_system(db: Session, system_id: str):
    return db.query(db_models.TelemetryRecord).filter(
        db_models.TelemetryRecord.system_id == system_id
    ).all()
