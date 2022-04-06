import requests
from bs4 import BeautifulSoup
import re
import sqlite3


url = 'https://ru.dotabuff.com'
match_str = '/matches/'
headers = {'User-agent': 'pc'}
test_match_id = ['6508700610', '6508713704', '6508737615', '6508724898', '6508730306', '6508697127', '6508724773', '6508730149', '6508739078', '6508725515', '6508721160', '6508737234', '6508743735', '6508733695', '6508737885', '6508721767', '6508710789', '6508720651', '6508722675', '6508725087', '6508721033']
test_post_v_bazu = ['Queen of Pain', 'Platemail', 'Null Talisman', "Linken's Sphere", 'Null Talisman', 'Power Treads', 'Orchid Malevolence', 'Elven Tunic']



# Функция возвращает список с id матчей с параметрами Рейтинговый матч, режим AllPick
# Далее отправляет список с id в функцию, которая циклом получает данные со страницы каждого матча
# def get_match_id_from_page():
#         response = requests.get(url+match_str, headers=headers)
#         soup = BeautifulSoup(response.text, 'lxml')
#         items = soup.find_all('tr')
#         rate = 'Рейтинговый подбор игр'
#         mode = 'All Pick'
#         post = []
#
#         for item in items:
#             if rate in str(item) and mode in str(item):
#                 try:
#                     value = item.find('a').get('href')
#                     if match_str in value:
#                         match_id = value.split(match_str)[1]
#                         if match_id not in post:
#                             post.append(match_id)
#                 except:
#                     AttributeError
#                 continue
#         return post


# для отоадки поиска по страницы, для избежания 409 прибегаю к парсингу текстового файла.
def opros(obj):
    for item in obj:
        response = requests.get(url+match_str+item, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')



def testovoe(obj):
    with open('6496190417.txt', 'r', encoding='utf-8') as file:
        regex_radiant = re.compile('.*col-hints faction-radiant player-.*')
        regex_dire = re.compile('.*col-hints faction-dire player-.*')
        soup = BeautifulSoup(file.read(), 'lxml')
        match_result = soup.find(class_='match-result').text
        if match_result == 'Победа сил Тьмы':
            regex_result = regex_dire
        elif obj == 'Победа сил Света':
            regex_result = regex_radiant

        for item in soup.find_all('tr', {"class": regex_result}):
            if item.find('th') is not None:  # исключение, отбор тегов не из таблиц
                continue
            elif item.find('th') is None:
                hero_name = (item.find('img').get('title'))  # hero_name
                list = [hero_name]
                inventory = item.find_all(class_='player-inventory-items')
                neutral_slot = item.find_all(class_='player-neutral-item')
                for slot in inventory:
                    for tag_slot in slot:
                        try:
                            list.append(tag_slot.find('img').get('title'))
                        except:
                            AttributeError
                        continue
                    for tag_neutral in neutral_slot:
                        try:
                            list.append(tag_neutral.find('img').get('title'))
                        except:
                            AttributeError
                        continue

                print(list)
# Требуемые данные: [id_героя, слот1, слот2, 3, 4, 5, 6, нейтральныйшмот]


def getid_from_baza(obj):
    conn = sqlite3.connect('eto_baza.db')
    cur = conn.cursor()
    rrr = cur.execute(f"SELECT hero_id FROM opendota WHERE name == '{obj}'")
    rrr = cur.fetchone()
    id_of_hero = rrr[0]
    print(id_of_hero)

getid_from_baza(test_post_v_bazu[0])
#Написать функицию которая собирает строку со всеми данными используя полученное id
