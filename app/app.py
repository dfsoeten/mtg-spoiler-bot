from .models.spoiler import Spoiler
from .controllers.cache import Cache
from .views.prettyCard import PrettyCard
from termcolor import colored
import telegram
import os


class App:

    # Spoiler data
    spoiler = Spoiler()

    # Cache spoiler data
    cache = Cache(spoiler)

    # Telegram Bot
    bot = telegram.Bot(token=os.getenv('API_TOKEN'))

    def __init__(self):
        print(colored('{} new cards found'.format(len(self.spoiler.get_new_cards())), 'yellow'))

    def start(self):
        print(self.bot.get_me())


