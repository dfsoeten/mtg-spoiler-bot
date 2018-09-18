import requests
import json
from termcolor import colored
from bs4 import BeautifulSoup


class Cards:

    # Card urls
    card_urls = []

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

                # Store all card urls
                for card in soup.findAll('a', 'card'):
                    self.card_urls.append(card['href'])

            else:
                if not config['silent']:
                    print(colored('[ERROR] Could not get cards from ' + set, 'red'))

    # Get card urls
    def get_card_urls(self):
        return self.card_urls

    # Get card urls length
    def get_cards_length(self):
        return len(self.card_urls)

