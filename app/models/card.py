# coding=utf-8
import os

import requests
import json
from termcolor import colored
from bs4 import BeautifulSoup


class Card:

    name = ''

    manacost = ''

    cmc = 0

    set = ''

    type = ''

    sub_types = []

    rules_text = ''

    flavor = ''

    artist = ''

    power = None

    toughness = None

    image_path = ''

    def __init__(self, set, url, image_path):
        with open('config.json') as file:
            config = json.load(file)

            # Get card data from page
            page = BeautifulSoup(requests.get(config['domain'] + '/' + set + '/' + url).text, 'lxml')
            card = page\
                .find('table', attrs={'valign': 'top', 'cellspacing': 0, 'cellpadding': 5, 'border': 0, 'align': 'center'})\
                .findAll('td')

            # Create array for card types
            types = [c.strip() for c in card[2].text.strip().split('-')]

            # Create array for power and toughness
            pwr_thg = [pt.strip() for pt in card[7].find('font').text.strip().split('/')]

            # Set card attributes
            self.name = card[0].text.strip()
            self.manacost = card[1].text.strip()
            self.cmc = int(self.manacost[0]) + (len(self.manacost) - 1)
            self.set = set
            self.type = types[0]
            self.sub_types = [types[1].split(' ')]
            self.rules_text = card[3].text.strip()
            self.flavor = card[4].text.strip()
            self.artist = card[6].find('font').text.strip()
            self.power = pwr_thg[0]
            self.toughness = pwr_thg[1]
            self.image_path = image_path

            # Get image
            if not self.has_image():
                open(self.image_path + self.get_image_filename() + '.jpg', 'wb') \
                    .write(requests.get(config['domain'] + '/' + set + '/cards/' + self.get_normalized_name() + '.jpg').content)

                if not config['silent']:
                    print (colored('[CACHED] ' + self.get_image_filename() + '.jpg', 'blue'))

            if not config['silent']:
                print(colored('[GET] ' + url, 'green'))

    def get_name(self):
        return self.name

    def get_normalized_name(self):
        return self.name.replace(' ', '').replace(',', '').lower()

    def get_manacost(self):
        return self.manacost

    def get_cmc(self):
        return self.cmc

    def get_type(self):
        return self.type

    def get_sub_types(self):
        return self.sub_types

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
