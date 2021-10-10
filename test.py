import json

with open('test.json') as f:
    data = json.load(f)
    print(data['resourceSets'][0]['resources'][0]['travelDistance']))