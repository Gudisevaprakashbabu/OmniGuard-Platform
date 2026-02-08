from fastapi import FastAPI
from .routes import router
from .database import engine, Base
from . import db_models

app = FastAPI(title="OmniGuard Ingestion Service")

# Create tables automatically
Base.metadata.create_all(bind=engine)

app.include_router(router)
