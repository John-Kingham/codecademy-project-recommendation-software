import unittest
from linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    def test_single_node_list(self) -> None:
        linky: LinkedList = LinkedList("eggs")
        self.assertEqual(linky.head.value, "eggs")

    def test_multi_node_list(self) -> None:
        items: list[str] = ["ham", "eggs", "green"]
        linky: LinkedList = LinkedList(items[0])
        linky.insert(items[1])
        linky.insert(items[2])
        temp_node: None | Node = linky.head
        for i in range(len(items) - 1, -1, -1):
            if temp_node:
                self.assertEqual(temp_node.value, items[i])
                temp_node = temp_node.next

    def test_str(self) -> None:
        linked_list = LinkedList("bar")
        linked_list.insert("foo")
        self.assertEqual(str(linked_list), "foo->bar")
