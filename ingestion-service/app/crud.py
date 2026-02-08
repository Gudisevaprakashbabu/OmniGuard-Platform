# Saves telemetry logic
from sqlalchemy.orm import Session
from . import db_models
from .models import TelemetryData


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
