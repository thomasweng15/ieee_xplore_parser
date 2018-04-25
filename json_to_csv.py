"""
Convert json to csv file.
"""

import os
import json
import csv

dirs = ["HRI", "ICRA", "IROS", "RO-MAN"]
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

data = []
for d in dirs:
    dir_path = os.path.join(path, d)
    fns = os.listdir(dir_path)
    for fn in fns: 
        j = json.load(open(dir_path + "/" + fn))
        
        for a in j["articles"]:
            if "title" not in a.keys() or "abstract" not in a.keys():
                continue

            data.append([a["title"], a["abstract"]])

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for d in data:
        writer.writerow(d)
