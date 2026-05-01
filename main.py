from fastapi import FastAPI
from routers.artist_router import router as artist_router
from routers.auth_router import router as auth_router
from routers.track_router import router as track_router
"""
Test: uvicorn main:app --reload
"""
app = FastAPI(
    title="Music API",
    version="1.0.0"
)

app.include_router(artist_router)
app.include_router(auth_router)
app.include_router(track_router)

@app.get("/")
def root():
    return {"message": "API is running"}