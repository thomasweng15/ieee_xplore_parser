"""
Convert json to csv file.
"""

import os
import json
import csv

dirs = ["HRI", "ICRA", "IROS", "RO-MAN"]
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

for d in dirs:
    dir_path = os.path.join(path, d)
    fns = os.listdir(dir_path)
    for fn in fns: 
        data = json.load(open(dir_path + "/" + fn))
        
        print(data)
