import json
def load_data():
    with open('one.json', 'r') as file:
        data = json.load(file)
    return data

load_data()