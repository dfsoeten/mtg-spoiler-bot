import json


class Base:

    config = []

    def __init__(self):
        with open('config.json') as file:
            self.config = json.load(file)
