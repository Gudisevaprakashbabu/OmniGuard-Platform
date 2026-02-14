from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

app = FastAPI(title="OmniGuard Ingestion Service")

Base.metadata.create_all(bind=engine)

app.include_router(router)
