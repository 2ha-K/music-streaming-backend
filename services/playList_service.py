"""
- get_playlists()
- create_playlist()
- delete_playlist()
- add_track_to_playlist()
- remove_track_from_playlist()
"""
from db import get_connection
from utils.db_utils import rows_to_dict, row_to_dict

limit_num = 100

def get_playlists(userkey="", displaytrack=None, offset=0):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select " \
    "p.p_playlistkey, p.p_name " \
    "from playlist p where p.p_userkey = %s t order by p_playlist limit %s offset %s;", 
    (userkey, limit_num, offset,))
    playlists = cur.fetchall();

    cur.close();
    conn.close();

    return rows_to_dict(playlists);

def create_playlist():
    pass

def delete_playlist():
    pass

def add_track_to_playlist():
    pass

def remove_track_from_playlist():
    pass