from models.spoiler import Spoiler
from views.prettyCard import PrettyCard


class App:

    def __init__(self):
        spoiler = Spoiler()
        spoiler.get_first_set().get_cards()

    def start(self):
        pass
