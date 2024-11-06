import json

with open('sampled_data.json') as f:
    data = json.load(f)

types = {}

for item in data:
    if item['type'] in types:
        types[item['type']] += 1
    else:
        types[item['type']] = 1

print(len(types.keys()))
print(types)