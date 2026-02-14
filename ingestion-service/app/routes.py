from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, models
from app.intelligence_client import analyze_telemetry

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/telemetry")
async def receive_telemetry(
    telemetry: models.TelemetryCreate,
    db: Session = Depends(get_db)
):
    saved = crud.create_telemetry(db, telemetry)
    intelligence = await analyze_telemetry(telemetry.model_dump())
    return {
        "saved": saved.id,
        "intelligence": intelligence
    }

@router.get("/telemetry")
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_telemetry(db)
