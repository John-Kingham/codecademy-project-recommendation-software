class HashMap:
    """
    A hashmap that uses open addressing to resolve collisions.
    """

    def __init__(self, size: int = 100) -> None:
        self.size: int = size
        self.map: list[list[object]] = [[]] * size

    def add(self, key: str, value: object) -> bool:
        """
        Adds a key-value pair to the hashmap or updates an existing pair.

        Returns
        -------
        True if the value was added or updated.
        False if the hashmap was full.
        """
        num_collisions: int = 0
        while num_collisions < self.size:
            index: int = self._hash(key, num_collisions)
            key_and_value: list[object] = self.map[index]
            if not key_and_value:
                self.map[index] = [key, value]
                return True
            if key_and_value[0] == key:
                self.map[index][1] = value
                return True
            num_collisions += 1
        return False

    def get(self, key: str) -> None | object:
        """
        Given a key, returns the associated value.

        Returns
        -------
        object
            The key's associated value.
        None
            If the key isn't found.
        """
        index: int = self._hash(key)
        key_and_value: list[object] = self.map[index]
        if key_and_value:
            return key_and_value[1]
        return None

    def _hash(self, key: str, num_collisions: int = 0) -> int:
        return (sum(key.encode()) + num_collisions) % self.size
