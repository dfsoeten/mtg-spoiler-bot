import sys
import json
from termcolor import colored


class PrettyCard:

    # Card object
    card = None

    card_width = 36

    title_space = 0

    output = ''

    def __init__(self, card):
        self.card = card

        # Set space between card title and mana cost
        self.title_space = (self.card_width - (4 + len(card.get_name() + card.get_manacost())))

    def get_output(self):

        # Start card title
        self.fill('+', '-')
        self.output += '| ' + self.card.get_name()
        self.fill_space(self.title_space)
        self.output += self.card.get_manacost() + ' |\n'
        self.fill('|', '-')
        # End Card title

        # Start card image
        for i in range(1, 8):
            self.fill('|', ' ')
        # End card image

        # Start card type
        self.fill('|', '-')
        self.fill_remaining('|', self.card.get_type() + ' - ' + self.card.get_sub_types_string())
        self.fill('|', '-')
        # End card type

        # Start card text
        for line in self.card.get_rules_text().splitlines():
            if len(line) > 0:
                self.fill_remaining('|', line)
                self.fill('|', ' ')

        return self.output

    def print_output(self):
        with open('config.json') as file:
            config = json.load(file)

            if not config['debug']['is-enabled']:
                print(colored('\n[DEBUG] Card Information', 'red'))

        print(self.get_output())

    def fill(self, border, content):
        self.output += border

        for i in range(1, self.card_width - 2):
            self.output += content

        self.output += border + '\n'

    def fill_space(self, amount):
        for i in range(1, amount):
            self.output += ' '

    def fill_remaining(self, border, content):
        self.output += border + ' '

        if len(content) < self.card_width - 4:
            self.output += content
            self.fill_space(self.card_width - (4 + len(content)))
            self.output += ' ' + border + '\n'

        else:
            self.output += content[:(self.card_width - 5)]
            self.output += ' ' + border + '\n'
            self.fill_remaining(border, content[(self.card_width - 5):])



