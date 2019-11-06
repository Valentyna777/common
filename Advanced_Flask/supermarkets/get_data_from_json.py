import json


def get_super_data():
    with open("supermarkets/supermarket_list.json") as file:
        return json.load(file)