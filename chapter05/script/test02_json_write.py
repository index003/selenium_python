import json

data1 = {
    "name": "字典名",
    "age": 38
}

with open("../data/w_json.json", "w", encoding="utf-8") as f:
    json.dump(data1, f, ensure_ascii=False)
