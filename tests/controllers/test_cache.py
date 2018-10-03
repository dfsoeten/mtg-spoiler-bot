import unittest
from app.controllers.cache import Cache
from app.models.spoiler import Spoiler


class TestCache(unittest.TestCase):

    cache = None

    def setUp(self):
        self.cache = Cache(Spoiler())
        self.cache.start()

    def test_has_new_set(self):
        # Act
        result = self.cache.has_new_set()

        # Assert
        self.assertTrue(result)



