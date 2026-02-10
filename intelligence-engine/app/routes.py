from fastapi import APIRouter
from .services import analyze_system

router = APIRouter()

@router.get("/analysis/{system_id}")
def get_analysis(system_id: str):
    return analyze_system(system_id)
