import requests
from bs4 import BeautifulSoup
import re

url = 'https://ru.dotabuff.com'
match_str = '/matches/'


# Функция сохроняет страницу в text для последующего распарсинга, при отладке
def save_text_page(obj=None):
    headers = {'User-agent': 'pc'}
    if obj is None:
        with open('matches.txt', 'w', encoding='utf-8') as file:
            re = requests.get(url + match_str, headers=headers)
            file.write(re.text)
            file.close()
    else:
        with open(f'{obj}.txt', 'w', encoding='utf-8') as file:
            re = requests.get(url + match_str + obj, headers=headers)
            file.write(re.text)
            file.close()


# Функция возвращает список с id матчей с параметрами Рейтинговый матч, режим AllPick
def get_match_id_from_page():
    with open('matches.txt', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
        items = soup.find_all('tr')
        rate = 'Рейтинговый подбор игр'
        mode = 'All Pick'
        post = []

        for item in items:
            if rate in str(item) and mode in str(item):
                try:
                    value = item.find('a').get('href')
                    if match_str in value:
                        match_id = value.split(match_str)[1]
                        if match_id not in post:
                            post.append(match_id)
                except:
                    AttributeError
                continue
        print(post)


def get_data_from_match_page():
    with open('6496190417.txt', 'r', encoding='utf-8') as file:
        dire_win_str = 'Победа сил Света'
        radiant_win_str = 'Победа сил Тьмы'
        soup = BeautifulSoup(file.read(), 'lxml')
        result_tag = soup.find(class_='match-result')
        if dire_win_str in str(result_tag):
            print(dire_win_str)
            dire_values = soup.find_all(class_='col-hints faction-dire player')
            print(dire_values, 'sa')
        elif radiant_win_str in str(result_tag):
            print(radiant_win_str)
            # col-hints faction-radiant player-1148208202


def testovoe(obj):
    dict = {'''
    'name':None,
    'hero_id':None,
    'item1':None,
    'item2': None
    'item3: '''}
    with open('6496190417.txt', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
        regex_radiant = re.compile('.*col-hints faction-radiant player-.*')
        regex_dire = re.compile('.*col-hints faction-dire player-.*')
        if obj == 'Победа сил Тьмы':
            regex_result = regex_dire
        elif obj == 'Победа сил Света':
            regex_result = regex_radiant

        for item in soup.find_all('tr', {"class": regex_result}):
            if item.find('th') is not None:  # исключение, отбор тегов не из таблиц
                continue
            elif item.find('th') is None:
                hero_name = (item.find('img').get('title'))  # hero_name
                hero_items = []
                inventory = item.find_all(class_='player-inventory-items')
                neutral_slot = item.find_all(class_='player-neutral-item')
                for x in inventory:
                    for one in x:
                        try:
                            hero_items.append(one.find('img').get('title'))
                        except:
                            AttributeError
                        continue
                    for z in neutral_slot:
                        try:
                            neutral_item = z.find('img').get('title')
                        except:
                            AttributeError
                        continue

                print([hero_name, hero_items, neutral_item])

            # {'name': 'Viper', item1:wb, neutral:bullshit}
            # print(item.find('img').get('title'))


testovoe(obj='Победа сил Света')
# get_data_from_match_page()
# save_text_page(obj='6496190417')
