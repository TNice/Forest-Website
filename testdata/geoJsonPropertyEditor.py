import json
import random as r

data = {}

with open("us.json") as file:
    data = json.load(file)

    for cell in data['features']:
        properties = {
            "Growth" : r.random(),
            "Fire" : r.random(),
            "Insect" : r.random()
        }

        region['properties'] = properties

with open("us.json", "w") as file:
    json.dump(data)