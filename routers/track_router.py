from fastapi import APIRouter
from services.track_service import get_tracks_offset, search_tracks, get_track_by_id

router = APIRouter(
    prefix="/track",
    tags=["track"],
)

@router.get("/")
def get_tracks_start_api():
    return get_tracks_offset(0)

@router.get("/offset={track_offset}")
def get_tracks_offset_api(track_offset: int):
    result = get_tracks_offset(offset=track_offset)
    if not result:
        return {"state": "No tracks found", "tracks": []}
    return {"state": "Tracks found", "tracks": result}