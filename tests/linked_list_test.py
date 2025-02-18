import unittest
from linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):

    def test_single_node_list(self) -> None:
        linky: LinkedList = LinkedList("eggs")
        self.assertEqual(linky.head.value, "eggs")

    def test_multi_node_list(self) ->None:
        linky: LinkedList = LinkedList("eggs")
        linky.insert("ham")
        linky.insert("green")
        self.assertEqual(linky.head.value, "green")
        self.assertEqual(linky.head.next.value, "ham") # type: ignore
        self.assertEqual(linky.head.next.next.value, "eggs") # type: ignore
    
    