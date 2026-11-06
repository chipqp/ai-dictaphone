from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.transcription import router as transcription_router


app = FastAPI(title="Ai dictaphone")

app.include_router(health_router)
app.include_router(transcription_router)
