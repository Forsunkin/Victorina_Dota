import sqlite3
import requests
import json

url_opendota = 'https://api.opendota.com/api/heroes'
heroes_data = requests.get(url_opendota).json()

test_values = ['Viper', ['Wraith Band', 'Hurricane Pike', 'Butterfly', 'Dust of Appearance', 'Power Treads', 'Iron Branch'], 'Bullwhip']

conn = sqlite3.connect('eto_baza.db')
cur = conn.cursor()

def post(obj):
    items = {'item1': None, 'item2': None, 'item3': None, 'item4': None, 'item5': None, 'item6': None}
    for n, item in enumerate(obj[1]):
        items.update(f'item{n}'=item)
        print(item)
    #можно попробывать обновить значение в словаре и вызывать его по переменной

    sqlite_post = f"""INSERT INTO heroes (hero_id, hero_name, item1, item2, item3, item4, item5, item6, neutral)
                              VALUES (3, 'item1', 'item2', 'item3',
                                                                  'item4', 'item5', 'item6',
                                                                  'neu
                                                                  ;"""

    sqlite_post = f"""INSERT INTO table (item1, item2, item3, item4, item5, item6)
                              VALUES ({item1}, '{item2}', '{item4}', '{item5}', '{item6});"""
#list=(l,i,s,t)
#VALUES(? ? ? ? ?), list


    print(sqlite_post)
    # cur.execute(sqlite_post)
    # conn.commit()
    # cur.close()
post(test_values)



cur.execute("""CREATE TABLE IF NOT EXISTS heroes(
   id INT PRIMARY KEY,
   hero_id INT,
   hero_name TEXT,
   item1 TEXT,
   item2 TEXT,
   item3 TEXT,
   item4 TEXT,
   item5 TEXT,
   item6 TEXT,
   neutral TEXT);
""")
