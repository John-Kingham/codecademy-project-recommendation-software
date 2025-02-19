class HashMap:
    """
    A hashmap that uses open addressing to resolve collisions.
    """

    def __init__(self, size: int = 100) -> None:
        self.size: int = size
        self.map: list[None | list[object]] = [None] * size

    def add(self, key: str, value: object) -> bool:
        """
        Adds a key-value pair to the hashmap or updates an existing pair.

        Returns
        -------
        True if the value was added or updated.
        False if the hashmap was full.
        """

        # try to add or update the key-value pair

        key_index: int = 0
        value_index: int = 1
        index: int = self._hash(key)
        key_value_pair: None | list[object] = self.map[index]
        if key_value_pair is None:
            self.map[index] = [key, value]
            return True
        if key_value_pair[key_index] == key: # type: ignore
            self.map[index][value_index] = value # type: ignore
            return True

        # if there was a collision, repeatedly try another index

        num_collisions: int = 1
        # TODO: I DON'T THINK THE WHILE TRUTH VALUE IS RIGHT. 
        # WE'RE LEAVING THE LOOP WHEN WE SUCCEED, SO CAN'T WE JUST SAY WHILE TRUE?
        while key_value_pair[key_index] != key: # type: ignore
            index = self._hash(key, num_collisions)
            key_value_pair = self.map[index]
            if key_value_pair is None:
                self.map[index] = [key, value]
                return True
            if key_value_pair[key_index] == key:
                key_value_pair[value_index] = value
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
        if self.map[index]:
            return self.map[index][1]  # type: ignore
        return None

    def _hash(self, key: str, num_collisions: int = 0) -> int:
        return (sum(key.encode()) + num_collisions) % self.size
