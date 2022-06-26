import sqlite3


conn = sqlite3.connect('eto_baza.db')
cur = conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS items(
                id INTEGER PRIMARY KEY,
                name TEXT);''')

cur.execute('''CREATE TABLE IF NOT EXISTS heroes(
               id INTEGER PRIMARY KEY,
               name TEXT,
               role_1 TEXT,
               role_2 TEXT,
               role_3 TEXT,
               role_4 TEXT);''')

