import requests
import sqlite3


conn = sqlite3.connect('eto_baza.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS opendota(
            hero_id INTEGER PRIMARY KEY,
            name TEXT,
            role1 TEXT,
            role2 TEXT,
            role3 TEXT,
            role4 TEXT);''')