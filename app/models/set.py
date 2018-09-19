import requests
import json
from card import Card
from termcolor import colored
from bs4 import BeautifulSoup


class Set:

    # Name
    name = ''

    # Card urls
    card_urls = []

    # Card
    cards = []

    # Set icon path
    cards_images_path = 'app/cache/card_images/'

    # Get sets from source
    def __init__(self, set_name):
        self.name = set_name

        with open('config.json') as file:
            config = json.load(file)

            if requests.get(config['domain'] + '/' + self.name).status_code == 200:
                if not config['silent']:
                    print(colored('[GET][SET] ' + self.name, 'green'))

                soup = BeautifulSoup(requests.get(config['domain'] + '/' + self.name).text, 'lxml')
                cards = soup.findAll('a', 'card')

                # Debug Mode
                if config['debug']['is-enabled']:
                    if len(cards) > config['debug']['card-index']:
                        self.card_urls.append(cards[config['debug']['card-index']]['href'])
                    elif not config['silent']:
                        print(colored('[ERROR] There is no card with index ' + str(config['debug']['card-index']) + ' for set ' + self.name, 'red'))

                # Non Debug Mode
                else:
                    # Store all card urls
                    for card in cards:
                        self.card_urls.append(card['href'])

            else:
                if not config['silent']:
                    print(colored('[ERROR] Could not get cards from ' + self.name, 'red'))

    # Get name
    def get_name(self):
        return self.name

    # Get cards
    def get_cards(self):
        if len(self.cards) != len(self.card_urls):
            for i in range(len(self.cards), len(self.card_urls), 1):
                self.cards.append(Card(self.name, self.card_urls[i], self.cards_images_path))

        return self.cards

    # Get card urls length
    def get_cards_length(self):
        return len(self.cards)

    # Get first card
    def get_first_card(self):
        if not self.cards:
            self.cards.append(Card(self.name, self.card_urls[0], self.cards_images_path))

        return self.cards[0]
