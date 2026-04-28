"""
- get_all_artists()
- get_artist_by_id()
"""
from db import get_connection
from utils.db_utils import rows_to_dict, row_to_dict

def get_all_artists():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select * from artist;")
    artists = cur.fetchall()

    cur.close()
    conn.close()

    return rows_to_dict(artists)

def get_artist_by_id(artist_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from artist where a_artistkey = %s;", (artist_id,))
    artist = cur.fetchone()
    cur.close()
    conn.close()
    return row_to_dict(artist)

# print(get_all_artists())
# print(get_artist_by_id(7))
