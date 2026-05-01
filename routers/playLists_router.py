from fastapi import APIRouter
from services.playList_service import *

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
)

@router.get("/")
def get_playlists_api(
    playlist_offset: int = 0,
    playlist_userkey: int = -1,
    playlist_view_key: int = -1):
    result = get_playlists(userkey=playlist_userkey, offset=playlist_offset, displaytrack=playlist_view_key)
    if "userplaylists" in result:
        value = result.get("userplaylists")
        if (not value):
            return {"state": "No playlists found", "playlists": []}
        else:
            return {"state": "Playlists found", "playlists": value}
    else:
        value = result.get("playlist")
        if (not value):
            return {"state": "No playlist tracks found", "playlisttracks": []}
        else:
            return {"state": "Playlists tracks found", "playlisttracks": value}

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

@router.post("/add-to-playlist")
def add_track_to_playlist_api(
    playlist_key: int = -1, track_key: int = -1):
    result = add_track_to_playlist(playlistkey=playlist_key, trackkey=track_key)
    return {"result": result}