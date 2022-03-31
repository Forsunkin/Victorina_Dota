import sqlite3
import requests
import json

url_opendota = 'https://api.opendota.com/api/heroes'
heroes_data = requests.get(url_opendota).json()

test_values2 = ['Viper', ['Wraith Band', 'Hurricane Pike', 'Butterfly', 'Dust of Appearance', 'Power Treads', 'Iron Branch'], 'Bullwhip']
test_values = ['Viper', ['Wraith Band', 'Hurricane Pike', 'Butterfly'], 'Bullwhip']


conn = sqlite3.connect('eto_baza.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS heroes(
   id INT PRIMARY KEY,
   hero_id INT
   hero_name TEXT,
   item1 TEXT,
   item2 TEXT,
   item3 TEXT,
   item4 TEXT,
   item5 TEXT,
   item6 TEXT,
   neutral TEXT);
""")
conn.commit()

def sort_data(obj):
    hero_name = obj[0]
    try:
        print(f'Name: {obj[1][0]}')
        slot1 = obj[1][0]
        slot2 = obj[1][1]
        slot3 = obj[1][2]
        slot4 = obj[1][3]
        slot5 = obj[1][4]
        slot6 = obj[1][5]
        neutral = obj[2]
    except:
        UnboundLocalError


    print(hero_name, slot1, slot2, slot3, slot4, slot5, slot6, neutral)



sqlite_insert_query = """INSERT INTO heroes
                          VALUES (4, 'Alex', 'sale@gmail.com', '2020-11-20', 8600);"""

cur.execute(sqlite_insert_query)



#
# def post_hero_data(obj):
#     cur.execute("""CREATE TABLE IF NOT EXISTS heroes(
#        hero_id INT PRIMARY KEY,
#        hero_name TEXT,
#        hero_role TEXT,
#        item2 TEXT,
#        item3 TEXT,
#        item4 TEXT,
#        item5 TEXT,
#        item6 TEXT,
#        neutral TEXT);
#     """)
