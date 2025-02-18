import unittest
from music_database import categories
from recommendation import autocomplete


class TestAutocomplete(unittest.TestCase):

    def test_not_found(self) -> None:
        self.assertEqual(autocomplete("X"), [])

    def test_one_found(self) -> None:
        self.assertEqual(autocomplete("y"), ["Country"])

    def test_many_found(self) -> None:
        self.assertEqual(autocomplete("d"), ["Indie", "World"])
