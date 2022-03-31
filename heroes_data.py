import requests
import json

url = 'https://api.opendota.com/api/heroes'

# В среднем 4 роли

print requests.get(url)