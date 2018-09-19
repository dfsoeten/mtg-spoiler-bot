import requests
import json
import os.path
from set import Set
from termcolor import colored
from bs4 import BeautifulSoup


class Spoiler:

    # Set urls
    set_urls = []

    # Sets
    sets = []

    # Set icon path
    set_icons_path = 'app/cache/set_images/'

    # Get sets from source
    def __init__(self):
        with open('config.json') as file:
            config = json.load(file)
            soup = BeautifulSoup(requests.get(config['domain'] + config['new-sets-url']).text, 'lxml')

            for set in soup.find('tr', attrs={'align': 'center'}).findAll('td'):
                set_name = set.find('a')['href']

                if len(set_name) < 5:
                    # Map set names
                    self.set_urls.append(set_name)

                    # Save set icons to cache if it doesn't exist
                    if not os.path.isfile(self.set_icons_path + set_name + '.png'):
                        open(self.set_icons_path + set_name + '.png', 'wb')\
                            .write(requests.get(config['domain'] + '/' + set_name).content)

                        if not config['silent']:
                            print (colored('[CACHED] ' + set_name, 'blue'))

    # Get sets
    def get_sets(self):
        if len(self.sets) != len(self.set_urls):
            for i in range(len(self.sets), len(self.set_urls), 1):
                self.sets.append(Set(self.set_urls[i]))

    # Get sets length
    def get_sets_len(self):
        return len(self.sets)

    # Get the latest set
    def get_first_set(self):
        if not self.sets:
            self.sets.append(Set(self.set_urls[0]))

        return self.sets[0]





