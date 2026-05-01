from fastapi import APIRouter
from services.playList_service import *

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
)

@router.get("/")
def get_playlists_api(
    playlists_offset: int = 0,
    playlist_userkey: int = -1):
    result = get_playlists(userkey=playlist_userkey, offset=playlists_offset)
    if not result:
        return {"state": "No playlists found", "playlists": []}
    return {"state": "Playlists found", "playlists": result}

@router.post("/create")
def create_playlist_api(
    playlist_userkey: int = -1, playlist_name: str = ""):
    result = create_playlist(userkey=playlist_userkey, playlistname=playlist_name)
    return {"result": result}

@router.delete("/delete")
def delete_playlist_api(
    playlist_userkey: int = -1, playlist_key: int = -1):
    result = delete_playlist(userkey=playlist_userkey, playlistkey=playlist_key)
    return {"result": result}