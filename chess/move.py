class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


class Move:
    def __init__(self, begin: Position = (0, 0), end: Position = (0, 0)):
        self.begin = begin
        self.end = end
