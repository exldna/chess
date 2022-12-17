import numpy as np
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

    def at(self, position: Position) -> Piece:
        return self.pieces_types[self.map[position.x][position.y]]

    def move(self, move: Move) -> None | Piece:
        # TODO: validate
        eat = self.at(move.end)
        self.apply(self.map, move)
        return eat

    def moved(self, move: Move) -> ndarray:
        return self.apply(np.copy(self.map), move)

    @staticmethod
    def apply(m: ndarray, move: Move) -> ndarray:
        m[move.end.x][move.end.y] = m[move.begin.x][move.begin.y]
        m[move.begin.x][move.begin.y] = 0
        return m

    def is_terminated(self):
        return False
