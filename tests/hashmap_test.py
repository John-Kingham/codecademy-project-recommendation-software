import unittest
from hashmap import HashMap


class TestHashmap(unittest.TestCase):

    def test_add_one_value(self) -> None:
        hashmap: HashMap = HashMap(10)
        key: str = "eggs"
        test_value: list[int] = [1, 2, 3]
        hashmap.add(key, test_value)
        returned_value: object = hashmap.get(key)
        self.assertEqual(returned_value, test_value)

    def test_hashmap_full(self) ->None:
        pass
        # hashmap: HashMap = HashMap(1)
        # self.assertTrue(hashmap.add("key1", "test_value1"))
        # self.assertFalse(hashmap.add("key2", "test_value2"))
