"""
- add_favorite()
- remove_favorite()
- get_favorites()
"""
from db import get_connection
import psycopg2
from utils.db_utils import rows_to_dict
def add_favorite(user_key, track_key):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO favorites (f_userkey, f_trackkey) VALUES (%s, %s)",
            (user_key, track_key)
        )

        conn.commit()
        return {"message": "Track added to favorites"}
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return {"error": f"Track({track_key}) is already in user({user_key})'s favorite list"}
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

def remove_favorite(user_key, track_key):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "DELETE FROM favorites WHERE f_userkey = %s AND f_trackkey = %s",
            (user_key, track_key)
        )
        conn.commit()
        if cur.rowcount == 0:
            return {"message": f"Track({track_key}) not found in favorites"}
        return {"message": f"Track({track_key}) removed from favorites"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_favorites(user_key):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM favorites WHERE f_userkey = %s",
        (user_key,)
    )
    favorite_tracks = cur.fetchall()
    cur.close()
    conn.close()
    return rows_to_dict(favorite_tracks)



