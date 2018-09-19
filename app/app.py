from models.sets import Sets
from models.cards import Cards


class App:

    def __init__(self):
        sets = Sets()
        cards = Cards(sets.get_sets()[0])

        # print(cards.get_cards()[0].get_name())
        # print(cards.get_cards()[0].get_manacost())
        # print(cards.get_cards()[0].get_cmc())
        # print(cards.get_cards()[0].get_type())
        # print(cards.get_cards()[0].get_sub_types())
        # print(cards.get_cards()[0].get_rules_text())
        # print(cards.get_cards()[0].get_flavor())
        # print(cards.get_cards()[0].get_artist())
        # print(cards.get_cards()[0].get_power())
        # print(cards.get_cards()[0].get_toughness())
        #
        # print(cards.get_cards()[0].get_image_filename())

    def start(self):
        pass
