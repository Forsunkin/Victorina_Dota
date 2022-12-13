import sqlite3


conn = sqlite3.connect('eto_baza.db')
cur = conn.cursor()


conn_arch = sqlite3.connect('archive.db')
cur_arch = conn_arch.cursor()


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


cur_arch.execute('''CREATE TABLE IF NOT EXISTS quests(
                    id INTEGER PRIMARY KEY,
                    match_id INTEGER,
                    hero_id INTEGER,
                    item_1 INTEGER,
                    item_2 INTEGER,
                    item_3 INTEGER,
                    item_4 INTEGER,
                    item_5 INTEGER,
                    item_6 INTEGER,
                    item_neutral INTEGER);''')