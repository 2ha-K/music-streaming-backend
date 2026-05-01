"""
- register()
- login()
"""
from db import get_connection
import psycopg2
from utils.auth import verify_password, hash_password

def register(email, password, username, display_name, role="audience"):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (u_email, u_userpassword_hash, u_username, u_displayname, u_role) VALUES (%s, %s, %s, %s, %s) RETURNING u_userkey",
            (email, hash_password(password), username, display_name, role)
        )

        if role == "artist":
            user_id = cur.fetchone()["u_userkey"]
            cur.execute(
                "INSERT INTO artist (a_name, a_userkey) VALUES (%s, %s)",
                (username, user_id)
            )
        conn.commit()
        return {"success": True}
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return {"error" : "Email or Username or ArtistName already exists"}
    except psycopg2.errors.NotNullViolation:
        conn.rollback()
        return {"error": "Missing required field"}
    except psycopg2.Error as e:
        conn.rollback()
        return {"error": e}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def login(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select u_userpassword_hash from users where u_email = %s", (email,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return {"success": False, "error": "Email does not exist"}
    hashed_password = row["u_userpassword_hash"]
    if verify_password(password, hashed_password):
        return {"success": True}
    else:
        return {"success": False, "error": "Incorrect password"}

