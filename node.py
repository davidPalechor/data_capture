class Node:
    def __init__(self, data: int, index: int):
        self.less = 0
        self.great = 0
        self.index = index
        self.data = data
        self.count = 1
