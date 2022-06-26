from keys import steam_api
import requests
import sqlite3
import json


url_items = f'https://api.steampowered.com/IEconDOTA2_570/GetGameItems/v1?key={steam_api}&language=english'
url_heroes = f'https://api.opendota.com/api/heroes'

re_items = requests.get(url_items)
re_heroes = requests.get(url_heroes)


def post_data_items():
    conn = sqlite3.connect('eto_baza.db')
    cur = conn.cursor()
    items = re_items.json()['result']['items']


    for item in items:
        uin = (item['id'], item['localized_name'])
        cur.execute(f'''INSERT INTO items VALUES (?,?)''', uin)
    conn.commit()

def post_data_heroes():

