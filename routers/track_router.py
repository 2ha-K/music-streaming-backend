from fastapi import APIRouter
from services.track_service import get_tracks_offset, search_tracks, get_track_by_id

router = APIRouter(
    prefix="/track",
    tags=["track"],
)

@router.get("/")
def get_tracks_api(track_offset: int = 0):
    result = get_tracks_offset(offset=track_offset)
    if not result:
        return {"state": "No tracks found", "tracks": []}
    return {"state": "Tracks found", "tracks": result}