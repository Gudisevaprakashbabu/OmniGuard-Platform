from sqlalchemy.orm import Session
from app import db_models
from app.models import TelemetryCreate

def create_telemetry(db: Session, telemetry: TelemetryCreate):
    db_obj = db_models.Telemetry(**telemetry.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all_telemetry(db: Session):
    return db.query(db_models.Telemetry).all()
