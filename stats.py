from node import Node


class Stats:
    def __init__(self, data: list):
        self.data = data
        self.hash_table = {}
        self.root = None

    def create_node(self, data: int, max_length: int, index: int):
        """Creates a node with particular info

        :param data: Data that will be contained in the log
        :param max_length: Max number of items added to the DataCapture instance so far
        :param index: Index that will identify the node
        """
        if data in self.hash_table:
            node = self.hash_table[data]
            node.count += 1
            index = node.index
        else:
            node = Node(data, index)
            self.hash_table[data] = node

        if index == 0:
            node.great = max_length - 1
            return node

        node.less = index
        node.great = max_length - node.count - index
        return node

    def build_stats(self):
        """Creates a map of nodes with its own information
        """
        for index in range(len(self.data)):
            self.create_node(self.data[index], len(self.data), index)

    def greater(self, key: int) -> int:
        """Returns how many numbers are greater than the key

        :param key: Key to be compared
        :return: The number of items that are greater than the key. 0 if the key does not exist.
        """
        node = self.hash_table.get(key)
        if not node:
            return 0
        return node.great

    def less(self, key: int) -> int:
        """Returns how many numbers are less than the key

        :param key: Key to be compared
        :return: The number of items that are lower than the key. 0 if the key does not exist.
        """
        node = self.hash_table.get(key)
        if not node:
            return 0
        return node.less

    def between(self, start: int, end: int) -> int:
        """Returns how many numbers there are between the start key and the end key (inclusive).

        :param start: Start key from which the range will be built
        :param end: End key that closes the range
        :return: The number of items existing between the start and the end key. 0 if either does not exist.
        """
        node_start = self.hash_table.get(start)
        node_end = self.hash_table.get(end)
        if not node_start or not node_end:
            return 0
        return node_start.count + (node_start.great - node_end.great)
