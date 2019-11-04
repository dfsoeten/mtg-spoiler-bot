import json
from termcolor import colored


class PrettyCard:
    # Card object
    card = None

    # Card width
    card_width = 37

    # Output result
    output = ''

    def __init__(self, card):
        self.card = card

    def get_output(self):

        # Start card title
        self.fill('+', '-')
        if len(self.card.get_name() + self.card.get_manacost()) + 6 > self.card_width:
            self.fill_justify('|',
                              [self.card.get_name()[:(self.card_width - (len(self.card.get_manacost()) + 8))] + '..',
                               self.card.get_manacost()])
        else:
            self.fill_justify('|', [self.card.get_name(), self.card.get_manacost()])
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
        self.fill('|', '-')
        # End card text

        # Start card footer
        if 'Creature' in self.card.get_type():
            pwr_tgh = str(self.card.get_power()) + '/' + str(self.card.get_toughness())

            if len(self.card.get_artist() + pwr_tgh) + 2 > self.card_width:
                self.fill_justify('|',
                                  [self.card.get_artist()[:(self.card_width - (len(pwr_tgh) + 8))] + '..', pwr_tgh])
            else:
                self.fill_justify('|', [self.card.get_artist(), pwr_tgh])
        else:
            self.fill_remaining('|', self.card.get_artist())

        self.fill('+', '-')
        # End Card footer

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
            self.output += " "

    def fill_justify(self, border, content):
        self.output += border + ' ' + content[0]
        self.fill_space((self.card_width - (4 + len(content[0] + content[1]))))
        self.output += content[1] + ' ' + border + '\n'

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
