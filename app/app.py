from .models.spoiler import Spoiler
from .controllers.cache import Cache
from .views.prettyCard import PrettyCard
from termcolor import colored


class App:

    # Spoiler data
    spoiler = Spoiler()

    # Cache spoiler data
    cache = Cache(spoiler)

    def __init__(self):
        card = PrettyCard(self.spoiler.get_first_set().get_first_card())
        card.print_output()

        print(colored('{} new cards found'.format(len(self.spoiler.get_new_cards())), 'yellow'))

        for card in self.spoiler.get_new_cards():
            print(colored(card.get_name(), 'red'))

    def start(self):
        pass
