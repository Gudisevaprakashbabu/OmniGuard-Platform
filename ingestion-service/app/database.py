from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# -----------------------------
# DATABASE CONNECTION STRING
# -----------------------------
# IMPORTANT:
# Use localhost because ingestion-service runs locally
DATABASE_URL = "postgresql://omniguard:omniguard123@localhost:5432/omniguard_db"

# -----------------------------
# CREATE ENGINE
# -----------------------------
engine = create_engine(DATABASE_URL)

# -----------------------------
# SESSION FACTORY
# -----------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# -----------------------------
# BASE CLASS FOR TABLE MODELS
# -----------------------------
Base = declarative_base()

# -----------------------------
# FASTAPI DB DEPENDENCY
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
