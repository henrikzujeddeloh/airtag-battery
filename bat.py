import json
import os
from tabulate import tabulate

FINDMY_FILES = '~/Library/Caches/com.apple.findmy.fmipcore/Items.data'

keys = 'batteryStatus'

airtags = {}

f = open(os.path.expanduser(FINDMY_FILES), 'r')
json_data = json.loads(f.read())
for item in json_data:
    airtags[item["name"]] = item["batteryStatus"]


headers = ["AirTag", "Battery Status"]

print(tabulate([k for k in airtags.items()], headers = headers, tablefmt='orgtbl'))
