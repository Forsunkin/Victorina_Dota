from keys import steam_api
import requests
import sqlite3
import json


url_items = f'https://api.steampowered.com/IEconDOTA2_570/GetGameItems/v1?key={steam_api}&language=english'
url_heroes = f'https://api.opendota.com/api/heroes'
