"""
- get_tracks_offset(offset=0)
- search_tracks()
- get_track_by_id()
"""
from db import get_connection
from utils.db_utils import rows_to_dict, row_to_dict

limit_num = 100

def get_tracks_offset(offset=0):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select " \
    "t.t_trackkey, t.t_title, a.a_name, t.t_album, t.t_duration, t.t_genre, t.t_description, t.t_uri " \
    "from track t join artist a on t.t_artistkey = a.a_artistkey order by t.t_trackkey limit %s offset %s;", 
    (limit_num, offset,))
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
        clauses.append("t.t_title ilike %s")
        params.append(f"{title}%")
    if artist:
        clauses.append("a.a_name ilike %s")
        params.append(f"{artist}%")
    if album:
        clauses.append("t.t_album ilike %s")
        params.append(f"{album}%")
    
    where_sql = ("where " + " and ".join(clauses)) if clauses else ""
    sql = f"""
    select t.t_trackkey, t.t_title, a.a_name, t.t_album, t.t_duration, t.t_genre, t.t_description, t.t_uri
    from track t join artist a on t.t_artistkey = a.a_artistkey {where_sql}
    order by t.t_trackkey limit %s offset %s
    """
    params.extend([limit_num, offset])

    cur.execute(sql, params)
    tracks = cur.fetchall()

    cur.close();
    conn.close();

    return rows_to_dict(tracks);

def get_track_by_id(trackKey):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select t.t_trackkey, t.t_title, a.a_name, t.t_album, t.t_duration, " \
    "t.t_genre, t.t_description, t.t_uri from track t join artist a on t.t_artistkey = a.a_artistkey " \
    "where t.t_trackkey = %s;", (trackKey,))
    tracks = cur.fetchone();

    cur.close();
    conn.close();

    return row_to_dict(tracks);