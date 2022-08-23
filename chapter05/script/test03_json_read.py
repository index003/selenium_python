import json

with open("../data/w_json.json", encoding="utf-8") as f:
    data = json.load(f)
    print(data)