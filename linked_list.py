from typing import Optional


class Node:
    """
    A node for a singly-linked list.
    """

    def __init__(self, value: object, next: Optional["Node"] = None) -> None:
        self.value: object = value
        self.next: Optional[Node] = next


class LinkedList:
    """
    A singly-linked list.
    """

    def __init__(self, value: object) -> None:
        """
        Parameters
        ----------
        value : object
            The value of the first node.
        """
        self.head: Node = Node(value)

    def insert(self, value: object) -> None:
        """
        Inserts a new value at the beginning of the list.

        Parameters
        ----------
        value : object
            The value of the new node.
        """
        new_head: Node = Node(value)
        new_head.next = self.head
        self.head = new_head

    def __str__(self) -> str:
        """
        Returns the list as "head.value->next.value->next.value" etc.
        """
        node: Optional[Node] = self.head
        as_str: str = ""
        while node:
            as_str += str(node.value) + "->"
            node = node.next
        return as_str[:-2]
