from typing import Any


class HashMap:
    """
    A hashmap that uses open addressing to resolve collisions.
    """

    def __init__(self, size: int = 100) -> None:
        """
        Creates an empty hashmap.

        Parameters
        ----------
        size
            The size of the hashmap.
        """
        self.size: int = size
        self.map: list[Any] = [None] * size

    def add(self, key: str, value: Any) -> bool:
        """
        Adds a key-value pair to the hashmap or updates an existing pair.
        Uses open addressing to manage collisions.

        Parameters
        ----------
        key
            A key that can be used to later retrieve the value.
        value
            The value mapped to the key.

        Returns
        -------
        True if the value was added or updated.
        False if the hashmap was full.
        """
        num_collisions: int = 0
        while num_collisions < self.size:
            index: int = self._hash(key, num_collisions)
            key_and_value: Any = self.map[index]
            if not key_and_value:
                self.map[index] = [key, value]
                return True
            if key_and_value[0] == key:
                self.map[index][1] = value
                return True
            num_collisions += 1
        return False

    def get(self, key: str) -> Any:
        """
        Given a key, returns the associated value.

        Returns
        -------
        object
            The value mapped to the key.
        None
            If the key isn't found.
        """
        num_attempts: int = 0
        while num_attempts < self.size:
            index: int = self._hash(key, num_attempts)
            key_and_value: Any = self.map[index]
            if not key_and_value:
                return None
            if key_and_value[0] == key:
                return key_and_value[1]
            num_attempts += 1
        return None

    def keys(self) -> set[str]:
        """
        Returns a set of the hashmap's keys.
        """
        key_list: set[str] = set()
        for key_value in self.map:
            if key_value:
                key_list.add(key_value[0])
        return key_list

    def _hash(self, key: str, num_collisions: int = 0) -> int:
        return (sum(key.encode()) + num_collisions) % self.size
