import json
import httpx

from fastapi.encoders import jsonable_encoder

async def analyze_telemetry(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://intelligence-engine:8001/analyze",
            json=jsonable_encoder(data)
        )
        return response.json()
