import sys
from termcolor import colored

class Card:

    def __init__(self):
        pass

    def pretty_print(self, card):
        print(colored('\n[DEBUG] Card Information', 'red'))
        sys.stdout.write('+----------------------------------+\n')

        # Card Title
        sys.stdout.write('| ' + card.get_name())
        for i in range(1, (33 - len(card.get_name() + card.get_manacost()))):
            sys.stdout.write(' ')
        sys.stdout.write(card.get_manacost() + ' |\n')

        # Card Content
        for i in range(1, 10):
            sys.stdout.write('|                                  |\n')

        # Creature type
        sys.stdout.write('+----------------------------------+\n')
        sys.stdout.write('| ' + card.get_type() + ' - ')
        for sub_type in card.get_sub_types():
            sys.stdout.write(sub_type + ' ')

        # for i in range(1, ((len(debugCard.get_type()) + 3) + )):
        #     sys.stdout.write(' ')

        # print('+ ' + debugCard.get_name(), end='')

        # print(debugCard.get_name() + '          ' + debugCard.get_manacost())
        # print(debugCard.get_type())
        # print(debugCard.get_sub_types())
        # print(debugCard.get_rules_text())
        # print(debugCard.get_flavor())
        # print(debugCard.get_artist())
        # print(debugCard.get_power())
        # print(debugCard.get_toughness())
        #
        # print(debugCard.get_cmc())
        # print(debugCard.get_image_filename())