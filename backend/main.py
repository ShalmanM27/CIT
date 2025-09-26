from fastapi import FastAPI
from routes.health import router as health_router

app = FastAPI(title="AI Contract Assistant - Backend")

app.include_router(health_router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok", "message": "AI Contract Assistant backend is running"}
