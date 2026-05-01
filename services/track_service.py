"""
- get_tracks_offset(offset=0, limit=100)
- search_tracks()
- get_track_by_id()
"""
from db import get_connection
from utils.db_utils import rows_to_dict, row_to_dict

def get_tracks_offset(offset=0, limit=100):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select * from track limit %s offset %s;", (limit, offset,))
    tracks = cur.fetchall();

    cur.close();
    conn.close();

    return rows_to_dict(tracks);

def search_tracks(title=None, artist=None, album=None):
    pass

def get_track_by_id(trackKey):
    pass