import requests
from bs4 import BeautifulSoup
from termcolor import colored

from .base import Base


class Scraper(Base):

    def __init__(self):
        Base.__init__(self)

    def get_card_name(self, card_url):
        return card_url.replace('cards/', '').replace('.html', '')

    def get_sets(self):
        if not self.config['silent']:
            print(colored('[GET][SETS]', 'green'))

        soup = BeautifulSoup(requests.get(self.config['domain'] + self.config['new-sets-url']).text, 'lxml')
        sets = []

        for set in soup.find('tr', attrs={'align': 'center'}).findAll('td'):
            set_name = set.find('a')['href']

            if len(set_name) < 5:
                # Map set names
                sets.append(set_name)

        return sets

    def get_cards(self, set_name):
        if not self.config['silent']:
            print(colored('[GET][SET] ' + set_name, 'green'))

        soup = BeautifulSoup(requests.get(self.config['domain'] + '/' + set_name).text, 'lxml')
        cards = []

        for card in soup.findAll('a', 'card'):
            cards.append(card['href'])

        return cards

    def get_card(self, set_name, card_name):

        if not self.config['silent']:
            print(colored('[GET][CARD] ' + self.get_card_name(card_name), 'green'))

        # Get card data
        try:
            page = BeautifulSoup(requests.get(self.config['domain'] + '/' + set_name + '/' + card_name).text, 'lxml')
            card = page \
                .find('table',
                      attrs={'valign': 'top', 'cellspacing': 0, 'cellpadding': 5, 'border': 0, 'align': 'center'}) \
                .findAll('td')

        except Exception as e:
            if not self.config['silent']:
                print(colored('[ERROR] Could not get card data from ' + self.config['domain'] + '/' + set_name + '/' + card_name, 'red'))

            if self.config['debug']['is-enabled']:
                print(colored(e, 'red'))

        # Parse card data
        try:
            types = [c.strip() for c in card[2].text.strip().split('-')]
            pwr_thg = [pt.strip() for pt in card[7].find('font').text.strip().split('/')]

            return {
                'name': card[0].text.strip(),
                'manacost': card[1].text.strip(),
                'type': types[0] if len(types) >= 1 else None,
                'sub_types': types[1].split(' ') if len(types) == 2 else None,
                'set': set_name,
                'rules_text': card[3].text.strip(),
                'flavor': card[4].text.strip(),
                'artist': card[6].find('font').text.strip(),
                'power': int(pwr_thg[0]) if len(pwr_thg) == 2 else None,
                'toughness': int(pwr_thg[1]) if len(pwr_thg) == 2 else None,
                'url': self.config['domain'] + '/' + set_name + '/' + card_name
            }

        except Exception as e:
            if not self.config['silent']:
                print(colored('[ERROR] Could not parse card data from ' + self.config['domain'] + '/' + set_name + '/' + card_name, 'red'))

            if self.config['debug']['is-enabled']:
                print(colored(e, 'red'))

            return {}
