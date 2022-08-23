import json


def read_json(filename):

    file_path = "../data/" + filename
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
