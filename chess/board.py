from numpy import zeros, ndarray, dtype
from chess.position import Position
from chess.pieces import *


class Board:
    def __init__(self):
        self.map: ndarray = zeros((8, 8), dtype=dtype('i1'))
        self.pieces_types = [
            Empty(),
            Pawn(),
            Bishop(),
            Knight(),
            Rook(),
            Queen(),
            King()
        ]

    def at(self, pos: Position):
        return self.pieces_types[self.map[pos.x][pos.y]]

    def do_move(self, start: Position, end: Position):
        self.map[end.x][end.y] = self.map[start.x][start.y]
        self.map[start.x][start.y] = 0

    def move(self, start: Position, end: Position) -> None | Piece:
        # TODO: validate
        tmp = self.at(end)
        self.do_move(start, end)
        return tmp

    def is_terminated(self):
        return False
