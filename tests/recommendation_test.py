import unittest
from recommendation import Album, MusicDatabase


class TestCategorySearch(unittest.TestCase):

    def setUp(self) -> None:
        self.database: MusicDatabase = MusicDatabase("music_database.csv")

    def test_category_not_found(self) -> None:
        self.assertEqual(self.database.find_categories("xxx"), [])

    def test_one_category_found(self) -> None:
        self.assertEqual(self.database.find_categories("y"), ["Country"])

    def test_many_categories_found(self) -> None:
        self.assertEqual(sorted(self.database.find_categories("d")), sorted(["Indie", "World"]))


class TestGetAlbums(unittest.TestCase):

    def setUp(self) -> None:
        self.database: MusicDatabase = MusicDatabase("music_database.csv")

    def test_albums_not_found(self) -> None:
        self.assertEqual(self.database.get_albums("xxx"), [])

    def test_albums_found(self) -> None:
        album1: Album = Album("Test", "Testy Tunes", "The Testers", "2025-02-01")
        album2: Album = Album("Test", "Testy Again", "The Testers", "2024-01-03")
        test_list: list[Album] = [album1, album2]
        self.assertEqual(sorted(self.database.get_albums("Test")), sorted(test_list))
