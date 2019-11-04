import os
from shutil import copyfile

import requests
import json
from termcolor import colored
from .base import Base
from .scraper import Scraper
from app.models.set import Set
from app.models.card import Card


class Cache(Base):

    # Spoiler
    spoiler = None

    # Scraper
    scraper = None

    # Set image path
    set_icons_path = 'app/cache/set_images/'

    # Card image path
    cards_images_path = 'app/cache/card_images/'

    # Cache
    cache = {}

    def __init__(self, spoiler):
        Base.__init__(self)
        self.spoiler = spoiler
        self.scraper = Scraper()

        self.read_cache()
        self.start()
        self.write_cache()

    def start(self):
        # Cache set & card data
        for set_name in self.scraper.get_sets():

            # Instantiate set models
            set = Set(set_name)

            # Check if set exists, otherwise cache it
            if not self.has_set(set_name):
                self.cache['sets'][set_name] = {}
                self.cache_set_images(set)

            for card_url in self.scraper.get_card_urls(set.get_name()):
                card_name = self.scraper.get_card_name(card_url)
                new_card = True

                # Check if card exists, otherwise cache it
                if not self.has_card(set.get_name(), card_name):
                    self.cache['sets'][set.get_name()][self.scraper.get_card_name(card_url)] = self.scraper.get_card(set.get_name(), card_url)

                    if not self.config['silent']:
                        print(colored('[CACHED][CARD] ' + self.scraper.get_card_name(card_name), 'blue'))
                else:
                    new_card = False

                    if not self.config['silent']:
                        print(colored('[FROM CACHE][CARD] ' + self.scraper.get_card_name(card_name), 'yellow'))

                # Instantiate card model
                card = Card(self.cache['sets'][set.get_name()][card_name], new=new_card)
                set.append_card(card)
                self.cache_card_images(card)

            self.spoiler.append_set(set)

    # Check if the cache has set
    def has_set(self, set_name):
        return set_name in self.cache['sets']

    # Check if the cache has a card
    def has_card(self, set_name, card_name):
        return card_name in self.cache['sets'][set_name] if self.has_set(set_name) else False

    # Read cache
    def read_cache(self):
        if not os.path.isfile('app/cache/cache.json'):
            copyfile('app/cache/cache.default.json', 'app/cache/cache.json')

        with open('app/cache/cache.json') as file:
            self.cache = json.load(file)

    # Write cache
    def write_cache(self):
        with open('app/cache/cache.json', 'w+') as file:
            json.dump(self.cache, file, indent=2)

    # Cache set images
    def cache_set_images(self, set):
        # Check if set image exists, otherwise cache it
        if not os.path.isfile(self.set_icons_path + set.get_name() + '.png'):
            open(self.set_icons_path + set.get_name() + '.png', 'wb') \
                .write(requests.get(self.config['domain'] + '/' + set.get_name()).content)

            if not self.config['silent']:
                print(colored('[CACHED][IMAGE] ' + set.get_name() + '.png', 'blue'))

    # Cache card images
    def cache_card_images(self, card):
        # Check if card image exists, otherwise cache it
        if not os.path.isfile(self.cards_images_path + card.get_image_filename() + '.jpg') and card.get_image_filename() != '':
            open(self.cards_images_path + card.get_image_filename() + '.jpg', 'wb') \
                .write(requests.get(
                    self.config['domain'] + '/' + card.get_set() + '/cards/' + card.get_normalized_name() + '.jpg').content)

            if not self.config['silent']:
                print(colored('[CACHED][IMAGE] ' + card.get_image_filename() + '.jpg', 'blue'))

    # Return all new cards in the spoiler model
    def get_new_spoilers(self):
        return self.spoiler