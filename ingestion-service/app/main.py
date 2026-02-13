from fastapi import FastAPI
from .routes import router
from .database import Base, engine
from . import db_models

app = FastAPI(title="OmniGuard Ingestion Service")

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(router)
