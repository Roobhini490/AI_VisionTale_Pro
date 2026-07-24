import sqlite3

def connect():
    conn = sqlite3.connect("visiontale.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        age INTEGER,
        character TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_user(username, age, character, password):

    conn = sqlite3.connect("visiontale.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users(username, age, character, password)
            VALUES(?,?,?,?)
            """,
            (username, age, character, password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def login_user(username, password):

    conn = sqlite3.connect("visiontale.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user

connect()