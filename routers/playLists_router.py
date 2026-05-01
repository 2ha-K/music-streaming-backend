from fastapi import APIRouter
from services.playList_service import *

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
)

@router.get("/")
def get_playlists_api(playlists_offset: int = 0):
    result = get_playlists(offset=playlists_offset)
    if not result:
        return {"state": "No tracks found", "tracks": []}
    return {"state": "Tracks found", "tracks": result}