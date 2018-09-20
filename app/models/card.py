# coding=utf-8
import os
import re

import requests
import json
from termcolor import colored
from bs4 import BeautifulSoup


class Card:

    url = ''

    name = ''

    manacost = ''

    set = ''

    type = ''

    sub_types = []

    rules_text = ''

    flavor = ''

    artist = ''

    power = None

    toughness = None

    image_path = ''

    is_split = False

    def __init__(self, set, url, image_path):
        self.set = set
        self.url = url
        self.image_path = image_path

        with open('config.json') as file:
            config = json.load(file)

            if not config['silent']:
                print(colored('[GET][CARD] ' + url, 'green'))

            try:
                # Get card data from page
                page = BeautifulSoup(requests.get(config['domain'] + '/' + set + '/' + url).text, 'lxml')
                card = page\
                    .find('table', attrs={'valign': 'top', 'cellspacing': 0, 'cellpadding': 5, 'border': 0, 'align': 'center'})\
                    .findAll('td')
            except Exception as e:
                if not config['silent'] or config['debug']['is-enabled']:
                    print(colored('[ERROR] Could load card data at ' + url, 'red'))

                if config['debug']['is-enabled']:
                    print(colored(e, 'red'))

            try:
                # Create array for card types
                types = [c.strip() for c in card[2].text.strip().split('-')]

                # Create array for power and toughness
                pwr_thg = [pt.strip() for pt in card[7].find('font').text.strip().split('/')]

                # Set card attributes
                self.name = card[0].text.strip()
                self.manacost = card[1].text.strip()
                if len(types) > 1:
                    self.type = types[0]
                    self.sub_types = types[1].split(' ')
                self.rules_text = card[3].text.strip()
                self.flavor = card[4].text.strip()
                self.artist = card[6].find('font').text.strip()
                if len(pwr_thg) == 2:
                    self.power = pwr_thg[0]
                    self.toughness = pwr_thg[1]

            except Exception as e:
                if not config['silent']:
                    print(colored('[ERROR] Could parse card data at ' + url, 'red'))

                if config['debug']['is-enabled']:
                    print(colored(e, 'red'))

            # Get image
            if not self.has_image():
                open(self.image_path + self.get_image_filename() + '.jpg', 'wb') \
                    .write(requests.get(config['domain'] + '/' + set + '/cards/' + self.get_normalized_name() + '.jpg').content)

                if not config['silent']:
                    print (colored('[CACHED] ' + self.get_image_filename() + '.jpg', 'blue'))

    def get_name(self):
        return self.name

    def get_normalized_name(self):
        if self.name:
            return self.name.replace(' ', '').replace(',', '').lower()
        else:
            return self.url.replace('cards/', '').replace('.html', '') + '90'

    def get_manacost(self):
        return self.manacost

    def get_cmc(self):
        if bool(re.search(r'\d', self.manacost)):
            return int(self.manacost[0]) + (len(self.manacost) - 1)
        else:
            return len(self.manacost)

    def get_type(self):
        return self.type

    def is_creature(self):
        return self.type == 'Creature'

    def get_sub_types(self):
        return self.sub_types

    def get_sub_types_string(self):
        result = ''

        for sub_type in self.sub_types:
            result += sub_type + ' '

        return result

    def get_rules_text(self):
        return self.rules_text

    def get_flavor(self):
        return self.flavor

    def get_artist(self):
        return self.artist

    def get_power(self):
        return self.power

    def get_toughness(self):
        return self.toughness

    def get_image_filename(self):
        return self.set + '_' + self.get_normalized_name()

    def has_image(self):
        return os.path.isfile(self.image_path + self.get_image_filename() + '.jpg')
