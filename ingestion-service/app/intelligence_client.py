import httpx

INTELLIGENCE_ENGINE_URL = "http://127.0.0.1:8001/analysis"

async def analyze_telemetry(record_id: int):
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(f"{INTELLIGENCE_ENGINE_URL}/{record_id}")
        response.raise_for_status()
        return response.json()
