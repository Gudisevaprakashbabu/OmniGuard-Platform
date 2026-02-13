from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import TelemetryData
from .database import get_db
from . import crud
from datetime import timezone
from .intelligence_client import analyze_telemetry
import pytz
from .logger import logger

router = APIRouter()


@router.get("/telemetry")
def fetch_all_telemetry(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_telemetry(db, skip, limit)


@router.get("/telemetry/{system_id}")
def fetch_system_telemetry(
    system_id: str,
    db: Session = Depends(get_db)
):
    return crud.get_telemetry_by_system(db, system_id)


@router.post("/telemetry")
async def receive_telemetry(
    data: TelemetryData,
    db: Session = Depends(get_db)
):

    logger.info(f"Telemetry received from {data.system_id}")

    # Store telemetry
    saved_record = crud.create_telemetry_record(db, data)

    # Time conversion
    utc_time = data.timestamp.astimezone(timezone.utc)

    try:
        tz = pytz.timezone(data.client_timezone)
        client_time = utc_time.astimezone(tz)
    except Exception:
        client_time = utc_time

    # Call intelligence engine safely
    try:
        analysis_result = await analyze_telemetry(saved_record.id)
    except Exception:
        analysis_result = {"status": "analysis unavailable"}

    return {
        "status": "Telemetry stored successfully",
        "record_id": saved_record.id,
        "system_id": data.system_id,
        "hostname": data.hostname,
        "analysis": analysis_result,
        "utc_timestamp": utc_time.isoformat(),
        "client_timestamp": client_time.isoformat(),
        "client_timezone": data.client_timezone
    }
