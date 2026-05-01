"""
- get_playlists()
- create_playlist()
- delete_playlist()
- add_track_to_playlist()
- remove_track_from_playlist()
"""
from db import get_connection
import psycopg2
from utils.db_utils import rows_to_dict, row_to_dict

limit_num = 100

def get_playlists(userkey=-1, displaytrack=None, offset=0):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select " \
    "p.p_playlistkey, p.p_name " \
    "from playlist p where p.p_userkey = %s order by p.p_playlistkey limit %s offset %s;", 
    (userkey, limit_num, offset,))
    playlists = cur.fetchall();

    cur.close();
    conn.close();

    return rows_to_dict(playlists);

def create_playlist(userkey=-1, playlistname=""):
    conn = get_connection()
    cur = conn.cursor()

    if (userkey==-1):
        return {"error": "No userkey"}

    try:
        cur.execute(
            "INSERT INTO playlist (p_userkey, p_name) VALUES (%s, %s)",
            (userkey, playlistname)
        )

        conn.commit()
        return {"message": f"Playlist {playlistname} created"}
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return {"error": f"Playlist{playlistname}) is a playlist for user({userkey})"}
    except psycopg2.errors.NotNullViolation:
        conn.rollback()
        return {"error": "Missing required field"}
    except psycopg2.Error as e:
        conn.rollback()
        return {"error": str(e)}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_playlist(userkey=-1, playlistkey=-1):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "DELETE FROM playlist WHERE p_userkey = %s AND p_playlistkey = %s",
            (userkey, playlistkey)
        )
        conn.commit()
        if cur.rowcount == 0:
            return {"message": f"Playlist {playlistkey} not found in user {userkey} playlist"}
        return {"message": f"Playlist {playlistkey} removed from user {userkey} playlist"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def add_track_to_playlist(playlistkey=-1, trackkey=-1):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO playlisttrack (pt_playlistkey, pt_trackkey) VALUES (%s, %s)",
            (playlistkey, trackkey)
        )

        conn.commit()
        return {"message": f"Playlist({playlistkey}) added track({trackkey})"}
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return {"error": f"Playlist{playlistkey}) already contains track({trackkey})"}
    except psycopg2.errors.NotNullViolation:
        conn.rollback()
        return {"error": "Missing required field"}
    except psycopg2.Error as e:
        conn.rollback()
        return {"error": str(e)}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def remove_track_from_playlist():
    pass