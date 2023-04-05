import json
import os
from tabulate import tabulate

FINDMY_FILES = '~/Library/Caches/com.apple.findmy.fmipcore/Items.data'

keys = 'batteryStatus'

airtags = {"AirTag" : [], "BatteryStatus" : [], "BatteryLevel" : []}

f = open(os.path.expanduser(FINDMY_FILES), 'r')
json_data = json.loads(f.read())
for item in json_data:
    airtags["AirTag"].append(item["name"])
    airtags["BatteryStatus"].append(item["batteryStatus"])


i=0
for tag in airtags["AirTag"]:
    bat_stat = airtags["BatteryStatus"][i]
    i+=1
    if bat_stat == 1:
        airtags["BatteryLevel"].append('#####')
    if bat_stat  == 2:
        airtags["BatteryLevel"].append('####')
    if bat_stat == 3:
        airtags["BatteryLevel"].append('###')
    if bat_stat == 4:
        airtags["BatteryLevel"].append('##')
    if bat_stat == 5:
        airtags["BatteryLevel"].append('#')


headers = ["AirTag", "Battery Status", "Battery Level"]
print(tabulate(airtags, headers = headers, tablefmt='outline'))
