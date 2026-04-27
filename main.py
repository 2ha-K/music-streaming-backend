from fastapi import FastAPI
from routers.artist_router import router as artist_router
"""
Test: uvicorn main:app --reload
"""
app = FastAPI(
    title="Music API",
    version="1.0.0"
)

app.include_router(artist_router)


@app.get("/")
def root():
    return {"message": "API is running"}