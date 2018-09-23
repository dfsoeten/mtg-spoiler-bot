import unittest
from app.models.card import Card


class TestCard(unittest.TestCase):

    card = None

    def setUp(self):
        self.set = Card({
            'name': 'test-card-name',
            'manacost': None,
            'type': None,
            'sub_types': None,
            'set': None,
            'rules_text': None,
            'flavor': None,
            'artist': None,
            'power': None,
            'toughness': None,
            'url': None,
        })

    # def test_set_get_cards(self):
    #     # Arrange
    #     self.set.set_cards(['card1', 'card2'])
    #
    #     # Act
    #     result = self.set.get_cards()
    #
    #     # Assert
    #     self.assertEquals(result, ['card1', 'card2'])


