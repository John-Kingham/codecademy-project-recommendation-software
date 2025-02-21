import unittest
from hashmap import HashMap


class TestHashmap(unittest.TestCase):

    def test_add_value(self) -> None:
        hashmap: HashMap = HashMap()
        hashmap.add("eggs", "ham")
        self.assertEqual(hashmap.get("eggs"), "ham")

    def test_update_value(self) -> None:
        hashmap: HashMap = HashMap()
        hashmap.add("eggs", "ham")
        hashmap.add("eggs", "spam")
        self.assertEqual(hashmap.get("eggs"), "spam")

    def test_hashmap_full(self) -> None:
        hashmap: HashMap = HashMap(1)
        self.assertTrue(hashmap.add("key1", "value1"))
        self.assertFalse(hashmap.add("key2", "value2"))
        self.assertEqual(hashmap.get("key1"), "value1")
        self.assertIsNone(hashmap.get("key2"))

    def test_keys(self) -> None:
        hashmap: HashMap = HashMap()
        hashmap.add("eggs", "on toast")
        hashmap.add("ham", "sandwich")
        self.assertEqual(hashmap.keys(), set(["eggs", "ham"]))
        