"""
Fetch all metadata from a single publication / conference year.
"""

import json
import requests


# Load config
cfg = json.load(open('config.json'))

# Load existing file
def load_existing_data(fname):
    try: 
        return json.load(open(fname))
    except FileNotFoundError:
        return {}

outfile_name = 'data/' + cfg['outfile']
data = load_existing_data(outfile_name)

# Request parameters
url = "http://ieeexploreapi.ieee.org/api/v1/search/articles"
params = {
    "publication_title": cfg['publication_title'],
    "apikey": cfg['apikey'],
    "max_record": "200"
}

# Request constraints
num_calls = 0,
max_calls = 175
sleep_duration = 0.15

# Make requests
while num_calls < max_calls:
    r = requests.get(url, params=params)
    data = r.json() # TODO append

# Save data
with open(outfile_name, 'w') as outfile:
    json.dump(data, outfile)