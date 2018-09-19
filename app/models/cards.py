import requests
import json
from card import Card
from termcolor import colored
from bs4 import BeautifulSoup


class Cards:

    # Card urls
    cards = []

    # Set icon path
    cards_images_path = 'app/cache/card_images/'

    # Get sets from source
    def __init__(self, set):
        with open('config.json') as file:
            config = json.load(file)

            if requests.get(config['domain'] + '/' + set).status_code == 200:
                if not config['silent']:
                    print(colored('[GET] ' + set, 'green'))

                soup = BeautifulSoup(requests.get(config['domain'] + '/' + set).text, 'lxml')

                if config['debug']:
                    card = soup.find('a', 'card')
                    self.cards.append(Card(set, card['href'], self.cards_images_path))

                else:
                    # Store all card urls
                    for card in soup.findAll('a', 'card'):
                        self.cards.append(Card(set, card['href'], self.cards_images_path))

            else:
                if not config['silent']:
                    print(colored('[ERROR] Could not get cards from ' + set, 'red'))

    # Get card urls
    def get_cards(self):
        return self.cards

    # Get card urls length
    def get_cards_length(self):
        return len(self.cards)

