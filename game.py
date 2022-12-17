import sqlite3
from random_quests import get_random_list


conn = sqlite3.connect('db/archive.db')
cur = conn.cursor()

#rlist = get_random_list()

random_squest = 300


def get_data(obj):
    s = cur.execute(f'SELECT * FROM quests WHERE ID is {obj}')
    print(s.fetchone())                             # возвращает (300, 6916797701, 29, 1, 79, 73, 180, 108, 36, 838)


def get_ticket(obj):
    pass

get_data(random_squest)