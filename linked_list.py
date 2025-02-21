from typing import Any


class Node:
    """
    A node that stores a value in a singly-linked list.
    """

    def __init__(self, value: object, next: Any = None) -> None:
        self.value: object = value
        self.next: Any = next


class LinkedList:
    """
    A singly-linked list.
    """

    def __init__(self, value: object) -> None:
        """
        Creates a new list with an initial value.
        """
        self.head: Node = Node(value)

    def insert(self, value: object) -> None:
        """
        Inserts a new value at the beginning of the list.
        """
        new_head: Node = Node(value)
        new_head.next = self.head
        self.head = new_head
