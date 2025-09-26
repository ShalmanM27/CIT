from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from routes.health import router as health_router

app = FastAPI(
    title="AI Contract Assistant API", 
    version="1.0.0",
    description="API for AI Contract Assistant -CIT Hackathon"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

app.include_router(health_router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok", "message": "AI Contract Assistant backend is running"}


if __name__ == "__main__":
    import uvicorn
    # Bind to 0.0.0.0 so emulators and other devices can reach the server
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)