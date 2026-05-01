from fastapi import FastAPI
from routers.artist_router import router as artist_router
from routers.auth_router import router as auth_router
from routers.track_router import router as track_router
from routers.favorite_router import router as favorite_router
from routers.playLists_router import router as playLists_router
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
app.include_router(favorite_router)
app.include_router(playLists_router)

@app.get("/")
def root():
    return {"message": "API is running"}