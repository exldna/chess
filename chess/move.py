class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Move:
    def __init__(self, begin: Position = None, end: Position = None):
        self.begin = begin
        self.end = end

    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end

    def __str__(self):
        return f"{{{self.begin}; {self.end}}}"

    def __hash__(self):
        return hash((self.begin.x, self.begin.y, self.end.x, self.end.y))
