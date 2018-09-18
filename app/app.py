from models.sets import Sets
from models.cards import Cards


class App:

    def __init__(self):
        sets = Sets()
        cards = Cards(sets.get_sets()[0])

    def start(self):
        pass
