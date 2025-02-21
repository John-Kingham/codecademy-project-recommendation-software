import unittest
from linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    def test_single_node_list(self) -> None:
        value: str = "eggs"
        linked_list: LinkedList = LinkedList(value)
        self.assertEqual(linked_list.head.value, value)

    def test_multi_node_list(self) -> None:
        value1: str = "eggs"
        value2: str = "ham"
        value3: str = "green"
        values: list[str] = [value1, value2, value3]
        linked_list: LinkedList = LinkedList(value3)
        linked_list.insert(value2)
        linked_list.insert(value1)
        temp_node: Node = linked_list.head
        for i in range(len(values)):
            if temp_node:
                self.assertEqual(temp_node.value, values[i])
                temp_node = temp_node.next
