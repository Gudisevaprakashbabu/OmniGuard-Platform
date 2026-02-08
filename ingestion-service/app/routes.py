from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import TelemetryData
from .database import get_db
from . import crud
from datetime import timezone
import pytz

router = APIRouter()


@router.post("/telemetry")
async def receive_telemetry(
    data: TelemetryData,
    db: Session = Depends(get_db)
):

    # --------------------------
    # STORE DATA IN DATABASE
    # --------------------------
    saved_record = crud.create_telemetry_record(db, data)

    # --------------------------
    # TIME CONVERSIONS
    # --------------------------
    utc_time = data.timestamp.astimezone(timezone.utc)

    try:
        tz = pytz.timezone(data.client_timezone)
        client_time = utc_time.astimezone(tz)
    except Exception:
        client_time = utc_time

    # --------------------------
    # RESPONSE BACK TO CLIENT
    # --------------------------
    return {
        "status": "Telemetry stored successfully",
        "record_id": saved_record.id,
        "system_id": saved_record.system_id,
        "hostname": saved_record.hostname,
        "utc_timestamp": utc_time.isoformat(),
        "client_timestamp": client_time.isoformat(),
        "client_timezone": data.client_timezone
    }
