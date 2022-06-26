from keys import steam_api
import requests

url_heroes = f'https://api.opendota.com/api/heroes'

re = requests.get(url_heroes)
re.json()[0]["id"], re.json()[0]["localized_name"]
roles = re.json()[0]["roles"]



c = ['Carry', 'Escape', 'Nuker']
r = c + ([None] * (4 - len(c))) if len(c) < 4 else c
print(r)

