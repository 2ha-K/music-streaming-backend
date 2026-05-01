"""
- get_tracks_offset(offset=0)
- search_tracks()
- get_track_by_id()
"""
from db import get_connection
from utils.db_utils import rows_to_dict, row_to_dict

def get_tracks_offset(offset=0):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select * from track limit 100 offset %s;", (offset,))
    tracks = cur.fetchall();

    cur.close();
    conn.close();

    return rows_to_dict(tracks);

def search_tracks(title=None, artist=None, album=None, offset=0):
    conn = get_connection()
    cur = conn.cursor()

    clauses = []
    params = []

    if title:
        clauses.append("title ILIKE %s")
        params.append(f"{title}%")

    cur.close();
    conn.close();

    return rows_to_dict();

def get_track_by_id(trackKey):
    pass