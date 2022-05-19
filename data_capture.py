from stats import Stats


class DataCapture:
    def __init__(self):
        self.nodes = []

    def add(self, data: int):
        """Adds a node into de DataCapture internal node structure

        :param data: data to be included
        """
        self.nodes.append(data)

    def build_stats(self) -> Stats:
        """Returns a Stats instance for using the statistic methods

        :return: Stats instance
        """
        self.nodes.sort()
        stats = Stats(self.nodes)
        stats.build_stats()

        return stats
