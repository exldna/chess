class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Move:
    def __init__(self, begin: Position, end: Position):
        self.begin = begin
        self.end = end
