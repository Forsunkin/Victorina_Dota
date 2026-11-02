# получить количество номров в базе
# запустить рандомайзер без повторов

import sqlite3
import requests
import random

conn = sqlite3.connect('db/archive.db')
cur = conn.cursor()
#SELECT COUNT(*) FROM имя таблицы WHERE * условие


def get_random_list():
    count = cur.execute('''SELECT COUNT(*) FROM quests''')
    c = count.fetchone()[0]
    l = list(range(1, c))
    random.shuffle(l)
    return l




def get_picture(obj):
    url = f'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/{obj}.png'
    print(url)


get_random_list()