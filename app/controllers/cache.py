import os
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

        # Cache set & card data
        for set in self.scraper.get_sets():

            # Check if set exists, otherwise cache it
            if not self.has_set(set):
                self.cache['sets'][set] = {}

            # Populate set models
            self.spoiler.append_sets(Set(set))

            set = self.spoiler.find_set(set)

            # Check if set image exists, otherwise cache it
            if not os.path.isfile(self.set_icons_path + set.get_name() + '.png'):
                self.cache_set_images(set)

            for card in self.scraper.get_cards(set.get_name()):
                # Check if card exists, otherwise cache it
                if not self.has_card(set.get_name(), self.scraper.get_card_name(card)):
                    self.cache['sets'][set.get_name()][self.scraper.get_card_name(card)] = self.scraper.get_card(set.get_name(), card)

                    if not self.config['silent']:
                        print(colored('[CACHED][CARD] ' + self.scraper.get_card_name(card), 'blue'))

                card = Card(self.cache['sets'][set.get_name()][self.scraper.get_card_name(card)])
                self.spoiler.find_set(set.get_name()).append_card(card)

                # Check if card image exists, otherwise cache it
                if not os.path.isfile(self.cards_images_path + card.get_image_filename() + '.jpg'):
                    self.cache_card_images(card)

                break
            break

        self.write_cache()

    def has_new_set(self):
        if self.cache['sets'] == self.scraper.get_sets():
            return False
        else:
            return True

    def has_set(self, set_name):
        return set_name in self.cache['sets']

    def has_card(self, set_name, card_name):
        return card_name in self.cache['sets'][set_name]

    # Read cache
    def read_cache(self):
        with open('app/cache/cache.json') as file:
            self.cache = json.load(file)

    # Write cache
    def write_cache(self):
        with open('app/cache/cache.json', 'w+') as file:
            json.dump(self.cache, file, indent=2)

    # Cache set images
    def cache_set_images(self, set):
        # Save set icons to cache if it doesn't exist
        open(self.set_icons_path + set.get_name() + '.png', 'wb') \
            .write(requests.get(self.config['domain'] + '/' + set.get_name()).content)

        if not self.config['silent']:
            print(colored('[CACHED][IMAGE] ' + set.get_name(), 'blue'))

    # Cache card images
    def cache_card_images(self, card):
        open(self.cards_images_path + card.get_image_filename() + '.jpg', 'wb') \
            .write(requests.get(
                self.config['domain'] + '/' + card.get_set() + '/cards/' + card.get_normalized_name() + '.jpg').content)

        if not self.config['silent']:
            print(colored('[CACHED][IMAGE] ' + card.get_image_filename() + '.jpg', 'blue'))




