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

        # Get card data
        for set in self.scraper.get_sets():
            if not self.has_set(set):
                self.cache['sets'][set] = {}

            self.spoiler.append_sets(Set(set))

            for card in self.scraper.get_cards(set):
                if not self.has_card(set, self.scraper.get_card_name(card)):
                    self.cache['sets'][set][self.scraper.get_card_name(card)] = self.scraper.get_card(set, card)

                    if not self.config['silent']:
                        print(colored('[CACHED] ' + self.scraper.get_card_name(card), 'blue'))

                self.spoiler.find_set(set).append_card(Card(self.cache['sets'][set][self.scraper.get_card_name(card)]))

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

    # Cache everything in memory
    def all(self):
        self.sets()
        self.cards()

    # Cache sets
    def sets(self):
        for set in self.spoiler.get_sets():

            # Save set icons to cache if it doesn't exist
            if not os.path.isfile(self.set_icons_path + set.get_name() + '.png'):
                open(self.set_icons_path + set.get_name() + '.png', 'wb') \
                    .write(requests.get(self.config['domain'] + '/' + set.get_name()).content)

                if not self.config['silent']:
                    print(colored('[CACHED] ' + set.get_name(), 'blue'))

            # Save set data

    # Cache cards
    def cards(self):

        for set in self.spoiler.get_sets():
            for card in set.get_cards():
                # Save card images to cache if it doesn't exist
                if not os.path.isfile(self.cards_images_path + card.get_image_filename() + '.jpg'):
                    open(self.cards_images_path + card.get_image_filename() + '.jpg', 'wb') \
                        .write(requests.get(
                            self.config['domain'] + '/' + set + '/cards/' + card.get_normalized_name() + '.jpg').content)

                    if not self.config['silent']:
                        print(colored('[CACHED] ' + card.get_image_filename() + '.jpg', 'blue'))

            # Save card data




