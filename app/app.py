from models.spoiler import Spoiler
from views.card import Card


class App:

    def __init__(self):
        spoiler = Spoiler()
        card = Card()

        print(spoiler.get_first_set().get_name())
        print(spoiler.get_first_set().get_first_card().get_name())
        # card.pretty_print(spoiler.get_first_set().get_first_card())

    def start(self):
        pass
