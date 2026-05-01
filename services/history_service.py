"""
- get_history()
- log_history()
"""

from db import get_connection
import psycopg2
from utils.db_utils import rows_to_dict

def get_history(user_key=-1):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM listeninghistory WHERE i_userkey = %s order by i_playeddate",
        (user_key,)
    )

    history = cur.fetchall()

    cur.close()
    conn.close()

    return rows_to_dict(history)

def log_history(user_key=-1, track_key=-1):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO listeninghistory (i_userkey, i_trackkey) VALUES (%s, %s)",
            (user_key, track_key)
        )

        conn.commit()
        return {"message": "Track added to history"}
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