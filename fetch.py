"""
Fetch all metadata from a single publication / conference year.
"""

import time
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
max_record = 25
params = {
    "publication_title": cfg['publication_title'],
    "apikey": cfg['apikey'],
    "max_record": str(max_record)
}

# Request constraints
num_calls = 0
max_calls = 175
start_record = 1 # TODO parametrize
total_records = None
sleep_duration = 0.5

# Call API in loop
def should_terminate(num_calls, max_calls, start_record, total_records):
    return num_calls > max_calls or \
        (total_records is not None and start_record > total_records)

while not should_terminate(num_calls, max_calls, start_record, total_records):
    # Make request
    params["start_record"] = start_record
    print("Requesting...")
    print(params)
    r = requests.get(url, params=params)
    req_json = r.json()

    # Append to existing data
    print("Appending data...")
    if data == {}:
        data = req_json
    else:
        data["articles"].append(req_json["articles"])

    # Update loop variables
    num_calls += 1
    start_record += max_record
    total_records = req_json["total_records"]
    print("num_calls: " + str(num_calls))
    print("start_record: " + str(start_record))
    time.sleep(sleep_duration)

# Save data
with open(outfile_name, 'w') as outfile:
    json.dump(data, outfile)