import json
import random as r

data = {}
i = 1001


print("Starting...")
with open('USCounties.json') as jsonfile:
    data = json.load(jsonfile)

##for cell in data['features']:
##    properties = {
##        "Id" : i,
##        "Growth" : r.random(),
##        "Fire" : r.random(),
##        "Insect" : r.random()
##    }
##
##    cell['properties'] = properties
##    i = i + 1

for cell in data['features']:
    properties = {
        'Id' : i
    }
    for j in range(1,5):
        properties[str(j)] = r.random()
        
    i = i + 1

    cell['properties'] = properties

if data != {}:
    with open('InsectTestData.json', "w") as file:
        json.dump(data, file)

print("DONE")
