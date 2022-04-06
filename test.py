import requests
from bs4 import BeautifulSoup

url = 'https://ru.dotabuff.com'
match_str = '/matches/'
headers = {'User-agent': 'pc'}


def get_match_id_from_page():
        response = requests.get(url+match_str, headers=headers)
        soup = BeautifulSoup(response, 'lxml')
        items = soup.find_all('tr')
        print(soup)
        print(items)


get_match_id_from_page()