from fastapi import APIRouter
from services.track_service import get_tracks_offset, search_tracks, get_track_by_id

router = APIRouter(
    prefix="/tracks",
    tags=["tracks"],
)

@router.get("/get_tracks")
def get_tracks_api(track_offset: int = 0):
    result = get_tracks_offset(offset=track_offset)
    if not result:
        return {"state": "No tracks found", "tracks": []}
    return {"state": "Tracks found", "tracks": result}

@router.get("/search")
def search_tracks_api(
    track_title: str = "",
    track_artist: str = "",
    track_album: str = "",
    track_offset: int = 0
):
    if track_title or track_artist or track_album:
        result = search_tracks(
            title=track_title, artist=track_artist, album=track_album, offset=track_offset
            )
    else:
        result = search_tracks(offset=track_offset)

    if not result:
        return {"state": "No tracks found", "tracks": []}
    return {"state": "Tracks found", "tracks": result}

@router.get("/{id}")
def get_track_by_id_api(id: int = -1):
    result = get_track_by_id(trackKey = id)
    if not result:
        return {"state": "No tracks found", "tracks": []}
    return {"state": "Tracks found", "tracks": result}