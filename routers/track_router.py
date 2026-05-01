from fastapi import APIRouter
from services.track_service import get_tracks_offset, search_tracks, get_track_by_id

router = APIRouter(
    prefix="/track",
    tags=["track"],
)

@router.get("/")
def get_tracks_start():
    result = get_tracks_offset()
    if not result:
        return {"state": "No tracks found", "tracks": []}
    return {"state": "Tracks found", "tracks": result}