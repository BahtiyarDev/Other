import sqlite3

with sqlite3.connect('data_base.db') as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex TEXT NOT NULL DEFAULT 'male',
                old INTEGER,
                score INTEGER)
""")

