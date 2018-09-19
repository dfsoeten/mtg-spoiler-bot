from models.spoiler import Spoiler
from views.prettyCard import PrettyCard


class App:

    def __init__(self):
        spoiler = Spoiler()
        card = PrettyCard(spoiler.get_first_set().get_first_card())
        card.print_output()

    def start(self):
        pass
