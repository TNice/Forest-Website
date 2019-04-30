import json
import random as r

data = {}
i = 1001


print("Starting...")
with open('USCounties.json') as jsonfile:
    data = json.load(jsonfile)

for cell in data['features']:
    properties = {
        "Id" : i,
        "Growth" : r.random(),
        "Fire" : r.random(),
        "Insect" : r.random()
    }

    cell['properties'] = properties
    i = i + 1

##for cell in data['features']:
##    cell['properties'] = {}
##    for i in range(1900,2100):
##        properties = {
##            "Id" : i,
##            "Growth" : r.random(),
##            "Fire" : r.random(),
##            "Insect" : r.random()
##        }
##        cell['properties'][str(i)] =  properties

if data != {}:
    with open('Test.json', "w") as file:
        json.dump(data, file)

print("DONE")
