import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import sqlite3


url = 'https://ru.dotabuff.com'
match_str = '/matches/'
headers = {'User-agent': 'pc'}
test_match_id = ['6508700610', '6508713704', '6508737615', '6508724898', '6508730306', '6508697127', '6508724773', '6508730149', '6508739078', '6508725515', '6508721160', '6508737234', '6508743735', '6508733695', '6508737885', '6508721767', '6508710789', '6508720651', '6508722675', '6508725087', '6508721033']
test_post_v_bazu = ['Queen of Pain', 'Platemail', 'Null Talisman', "Linken's Sphere", 'Null Talisman', 'Power Treads', 'Orchid Malevolence', 'Elven Tunic']



def parse_pages(match_id=None):
        with open('6496190417.txt', 'r') as response:
                regex_radiant = re.compile('.*col-hints faction-radiant player-.*')
                regex_dire = re.compile('.*col-hints faction-dire player-.*')
                soup = BeautifulSoup(response.read(), 'lxml')

                match_result = soup.find(class_='match-result').text
                if match_result == 'Победа сил Тьмы':
                    regex_result = regex_dire
                elif match_result == 'Победа сил Света':
                    regex_result = regex_radiant

                for item in soup.find_all('tr', {"class": regex_result}):
                    if item.find('th') is not None:                         # исключение, отбор тегов не из таблиц
                        continue
                    elif item.find('th') is None:
                        match_id = None                                     # match_id
                        hero_name = (item.find('img').get('title'))         # hero_name
                        hero_id = getid_from_baza(hero_name)                # hero_id
                        inventory = item.find_all(class_='player-inventory-items')
                        neutral_slot = item.find_all(class_='player-neutral-item')
                        dict = {'match_id': match_id, 'hero_id': hero_id, 'hero_name': hero_name}
                        for n, slot in enumerate(inventory):
                            for tag_slot in slot:
                                try:
                                #пепеписать логику добавления слотов
                                    dict[f'slot{n}'] = tag_slot.find('img').get('title')
                                except:
                                    AttributeError
                                continue
                            for tag_neutral in neutral_slot:
                                try:
                                    dict.update(**{f'neutralslot':tag_neutral.find('img').get('title')})
                                except:
                                    AttributeError
                                continue

                        print(dict)





def getid_from_baza(obj):
    conn = sqlite3.connect('eto_baza.db')
    cur = conn.cursor()
    rrr = cur.execute(f"SELECT hero_id FROM opendota WHERE name == '{obj}'")
    rrr = cur.fetchone()
    id_of_hero = rrr[0]
    return id_of_hero

parse_pages()