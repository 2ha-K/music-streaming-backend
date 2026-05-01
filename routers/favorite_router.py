from fastapi import APIRouter
from pydantic import BaseModel
from services.favorite_service import add_favorite, remove_favorite, get_favorites

router = APIRouter(
    prefix="/favorite",
    tags=["favorite"],
)

class Add(BaseModel):
    user_key: int
    track_key: int

@router.post("/add")
def add_favorite_api(payload: Add):
    user_key = payload.user_key
    track_key = payload.track_key
    result = add_favorite(user_key, track_key)
    return {"result": result}


class Delete(BaseModel):
    user_key: int
    track_key: int

@router.delete("/remove")
def remove_favorite_api(payload: Delete):
    user_key = payload.user_key
    track_key = payload.track_key
    result = remove_favorite(user_key, track_key)
    return {"result": result}

@router.get("/favorites/{user_key}")
def get_favorites_api(user_key: int):
    favorites = get_favorites(user_key=user_key)
    if not favorites:
        return {"state": "No favorites"}
    return {"favorites": favorites}
