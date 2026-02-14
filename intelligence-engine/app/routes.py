from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    risk_score = 0

    if data.get("cpu_usage", 0) > 85:
        risk_score += 30

    if data.get("memory_usage", 0) > 90:
        risk_score += 30

    if data.get("temperature", 0) > 80:
        risk_score += 40

    return {
        "risk_score": risk_score,
        "risk_level": (
            "HIGH" if risk_score >= 70 else
            "MEDIUM" if risk_score >= 40 else
            "LOW"
        )
    }
