import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://omniguard:omniguard123@localhost:5432/omniguard_db"
)

INTELLIGENCE_ENGINE_URL = os.getenv(
    "INTELLIGENCE_ENGINE_URL",
    "http://localhost:8001"
)
