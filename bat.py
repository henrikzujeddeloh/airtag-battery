import json
import os

FINDMY_FILES = '~/Library/Caches/com.apple.findmy.fmipcore/Items.data'

keys = 'batteryStatus'

airtags = {}

f = open(os.path.expanduser(FINDMY_FILES), 'r')
json_data = json.loads(f.read())
for item in json_data:
    airtags[item["name"]] = item["batteryStatus"]

for tag in airtags:
    print("Battery Status of " + tag + " is " + str(airtags[tag]))

