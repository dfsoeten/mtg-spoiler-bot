import re
from .base import Base


class Card(Base):

    name = ''

    manacost = ''

    type = ''

    sub_types = []

    set = ''

    rules_text = ''

    flavor = ''

    artist = ''

    power = None

    toughness = None

    url = ''

    def __init__(self, c):
        Base.__init__(self)
        self.url = c['url']
        self.name = c['name']
        self.type = c['type']
        self.sub_types = c['sub_types']
        self.set = c['set']
        self.rules_text = c['rules_text']
        self.flavor = c['flavor']
        self.artist = c['artist']
        self.power = c['power']
        self.toughness = c['toughness']
        self.url = c['url']

    def get_name(self):
        return self.name

    def get_normalized_name(self):
        if self.name:
            return self.name.replace(' ', '').replace(',', '').lower()
        else:
            return self.url.replace(self.config['domain'] + '/' + self.set + '/cards/', '').replace('.html', '')

    def get_manacost(self):
        return self.manacost

    def get_cmc(self):
        if bool(re.search(r'\d', self.manacost)):
            return int(self.manacost[0]) + (len(self.manacost) - 1)
        else:
            return len(self.manacost)

    def get_type(self):
        return self.type

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


