from .models.spoiler import Spoiler
from .controllers.cache import Cache
from .views.prettyCard import PrettyCard


class App:

    # Spoiler data
    spoiler = Spoiler()

    # Cache spoiler data
    cache = Cache(spoiler)

    def __init__(self):
        card = PrettyCard(self.spoiler.get_first_set().get_first_card())
        card.print_output()

    def start(self):
        # When our program is done, cache everything
        # self.cache.all()
        pass
