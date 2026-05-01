"""
- get_all_tracks()
- search_tracks()
- get_track_by_id()
"""
from db import get_connection
from utils.db_utils import rows_to_dict, row_to_dict

def get_all_tracks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select * from track;")
    tracks = cur.fetchall();

    cur.close();
    conn.close();

    return rows_to_dict(tracks);

def search_tracks(title=None, artist=None, album=None):
    pass

def get_track_by_id(trackKey):
    pass