import json
import os
import tabulate

# Location of FindMy cache file for AirTags
FINDMY_FILES = '~/Library/Caches/com.apple.findmy.fmipcore/Items.data'

# dict with AirTag names, and battery status
airtags = {"AirTag" : [], "BatteryStatus" : [], "BatteryLevel" : []}

# opens file and reads as json
f = open(os.path.expanduser(FINDMY_FILES), 'r')
json_data = json.loads(f.read())
for item in json_data:
    airtags["AirTag"].append(item["name"])
    airtags["BatteryStatus"].append(item["batteryStatus"])

# Loop to translate battery status to battery level
i=0
for tag in airtags["AirTag"]:
    bat_stat = airtags["BatteryStatus"][i]
    i+=1
    if bat_stat == 1:
        airtags["BatteryLevel"].append(u'\u2588'+u'\u2588'+u'\u2588'+u'\u2588'+u'\u2588')
    if bat_stat  == 2:
        airtags["BatteryLevel"].append(u'\u2588'+u'\u2588'+u'\u2588'+u'\u2588'+u'\u2591')
    if bat_stat == 3:
        airtags["BatteryLevel"].append(u'\u2588'+u'\u2588'+u'\u2588'+u'\u2591'+u'\u2591')
    if bat_stat == 4:
        airtags["BatteryLevel"].append(u'\u2588'+u'\u2588'+u'\u2591'+u'\u2591'+u'\u2591')
    if bat_stat == 5:
        airtags["BatteryLevel"].append(u'\u2588'+u'\u2591'+u'\u2591'+u'\u2591'+u'\u2591')


# creates final table to output
headers = ["AirTag", "Battery Status", "Battery Level"]
print(tabulate.tabulate(airtags, headers = headers, tablefmt='outline'))
