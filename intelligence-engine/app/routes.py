from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/analysis/{record_id}")
def analyze_record(record_id: int):

    risk_score = random.randint(1, 100)

    status = "Healthy" if risk_score < 50 else "Risk Detected"

    return {
        "system_id": record_id,
        "risk_score": risk_score,
        "status": status,
        "message": "Mock analysis result"
    }
