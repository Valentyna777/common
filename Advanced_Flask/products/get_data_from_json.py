import json


def get_prod_data():
    with open("products/product_list.json") as file:
        return json.load(file)