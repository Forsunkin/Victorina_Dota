import requests

url_public = 'https://api.opendota.com/api/publicMatches'


re = requests.get(url_public)
print(re.json()[0])


'match_id',