from fastapi import APIRouter
from services.track_service import get_all_tracks, search_tracks, get_track_by_id

router = APIRouter(
    prefix="/track",
    tags=["track"],
)

@router.get("/")
def get_all_tracks_api():
    result = get_all_tracks()
    if not result:
        return {"state": "No tracks found", "tracks": []}
    return {"state": "Tracks found", "tracks": result}