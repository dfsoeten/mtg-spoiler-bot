import requests
import json
import os.path
from termcolor import colored
from bs4 import BeautifulSoup


class Sets:

    # Set names
    sets = []

    # Set icon path
    set_icons_path = 'app/cache/set_icons/'

    # Get sets from source
    def __init__(self):
        with open('config.json') as file:
            config = json.load(file)
            soup = BeautifulSoup(requests.get(config['domain'] + config['new-sets-url']).text, 'lxml')

            for set in soup.find('tr', attrs={'align': 'center'}).findAll('td'):
                set_name = set.find('a')['href']

                if len(set_name) < 5:
                    # Map set names
                    self.sets.append(set_name)

                    # Save set icons to cache if it doesn't exist
                    if not os.path.isfile(self.set_icons_path + set_name + '.png'):
                        open(self.set_icons_path + set_name + '.png', 'wb')\
                            .write(requests.get(config['domain'] + '/' + set_name).content)

                        if config['output']:
                            print (colored('[CACHED] ' + set_name, 'yellow'))

    # Get sets
    def get_sets(self):
        return self.sets

    # Get sets length
    def get_sets_len(self):
        return len(self.sets)





