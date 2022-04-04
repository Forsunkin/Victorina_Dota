import requests
import sqlite3

url = 'https://api.opendota.com/api/heroes'

conn = sqlite3.connect('eto_baza.db')
cur = conn.cursor()



def get_data():
    r = requests.get(url)
    data = r.json()
    for item in data:
        name = item.get('localized_name')
        id = item.get('id')
        list_roles = item.get('roles')
        get_list_roles = get_roles(list_roles)
        list = [id, name]
        for item in get_list_roles:
            list.append(item)
        post_in_base(list)


def get_roles(obj):
    list = [None, None, None, None]
    for n, role in enumerate(obj):
        if n < 4:
            list[n] = role
        else:
            pass
    return list


def post_in_base(obj):
    cur.execute('INSERT INTO opendota VALUES(?, ?, ?, ?, ?, ?);', obj)
    conn.commit()


get_data()
