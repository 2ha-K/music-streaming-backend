from fastapi import APIRouter
from pydantic import BaseModel
from services.history_service import get_history, log_history

router = APIRouter(
    prefix="/history",
    tags=["history"],
)

@router.get("/")
def get_history_api(userkey: int = -1):
    history = get_history(user_key=userkey)
    if not history:
        return {"state": "No history"}
    return {"history": history}

@router.post("/log")
def get_history_api(userkey: int = -1, trackkey: int = -1):
    result = log_history(user_key=userkey, track_key=trackkey)
    return {"result": result}