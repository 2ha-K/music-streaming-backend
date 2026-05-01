from fastapi import APIRouter
from services.artist_service import get_all_artists, get_artist_by_id

router = APIRouter(
    prefix="/artist",
    tags=["artist"],
)

@router.get("/artists")
def get_all_artists_api():
    result = get_all_artists()
    if not result:
        return {"state": "No artists found", "artists": []}
    return {"state": "Artists found", "artists": result}

@router.get("/artist/{artist_id}")
def get_artist_by_id_api(artist_id: int):
    result = get_artist_by_id(artist_id)
    if not result:
        return {"state": "Artist not found", "artist": None}
    return {"state": "Artist found", "artist": result}