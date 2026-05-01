"""
- get_history()
- log_history()
"""

from db import get_connection
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

def log_history():
    pass