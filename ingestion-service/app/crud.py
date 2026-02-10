# Saves telemetry logic
from sqlalchemy.orm import Session
from . import db_models
from .models import TelemetryData


# -----------------------------
# GET ALL TELEMETRY
# -----------------------------
def get_all_telemetry(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.TelemetryRecord).offset(skip).limit(limit).all()


# -----------------------------
# GET TELEMETRY BY SYSTEM ID
# -----------------------------
def get_telemetry_by_system(db: Session, system_id: str):
    return (
        db.query(db_models.TelemetryRecord)
        .filter(db_models.TelemetryRecord.system_id == system_id)
        .all()
    )


def create_telemetry_record(db: Session, telemetry: TelemetryData):
    db_record = db_models.TelemetryRecord(
        system_id=telemetry.system_id,
        hostname=telemetry.hostname,
        os_version=telemetry.os_version,
        agent_version=telemetry.agent_version,
        cpu_usage=telemetry.cpu_usage,
        memory_usage=telemetry.memory_usage,
        disk_usage=telemetry.disk_usage,
        network_usage=telemetry.network_usage,
        temperature=telemetry.temperature,
        process_count=telemetry.process_count,
        timestamp=telemetry.timestamp
    )

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return db_record
