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
        uin = (item['id'], item['name'][5:], item['localized_name'])
        cur.execute(f'''INSERT or REPLACE INTO items VALUES (?,?,?)''', uin)
    conn.commit()


def post_data_heroes():
    conn = sqlite3.connect('eto_baza.db')
    cur = conn.cursor()
    heroes = re_heroes.json()

    for hero in heroes:
        roles_list = hero["roles"]
        roles = roles_list + ([None] * (4 - len(roles_list))) if len(roles_list) < 4 else roles_list
        uin = roles[:4]
        postal = hero["id"], hero["localized_name"], hero["name"][14:], uin[0], uin[1], uin[2], uin[3]
        cur.execute(f'''INSERT or REPLACE INTO heroes VALUES (?,?,?,?,?,?,?)''', postal)
    conn.commit()


post_data_items()
post_data_heroes()