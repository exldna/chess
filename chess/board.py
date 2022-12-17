from numpy import zeros, ndarray, dtype
from chess.move import Position, Move
from chess.pieces import Piece, Empty, Pawn, Bishop, Knight, Rook, Queen, King


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

    def at(self, position: Position):
        return self.pieces_types[self.map[position.x][position.y]]

    def move(self, move: Move) -> None | Piece:
        tmp = self.at(move.end)
        self.map[move.end.x][move.end.y] = self.map[move.begin.x][move.begin.y]
        self.map[move.begin.x][move.begin.y] = 0
        return tmp

    def is_terminated(self):
        return False
