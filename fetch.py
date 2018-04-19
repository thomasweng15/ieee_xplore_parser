import json
import requests

cfg = json.load(open('config.json'))
url = "http://ieeexploreapi.ieee.org/api/v1/search/articles"
params = {
    "publication_title": cfg['publication_title'],
    "key": cfg['apikey']
}

r = requests.get(url, params=params)
print(r)