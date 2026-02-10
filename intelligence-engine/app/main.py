from fastapi import FastAPI
from .routes import router

app = FastAPI(title="OmniGuard Intelligence Engine")

app.include_router(router)
