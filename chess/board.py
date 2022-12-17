from numpy import zeros, ndarray, dtype
from chess.move import Position, Move
from chess.pieces import Empty, Pawn, Bishop, Knight, Rook, Queen, King


class Board:
    def __init__(self):
        self.map: ndarray = zeros((8, 8), dtype=dtype('i1'))

    def is_terminated(self):
        return False


class BoardAccess:
    def __init__(self, board: Board):
        self.m = board.map

    def __setitem__(self, position: Position, value):
        pass

    def __getitem__(self, position: Position) -> int:
        pass


class WhiteBoardAccess(BoardAccess):
    def __init__(self, board: Board):
        super().__init__(board)

    def __setitem__(self, position: Position, value):
        self.m[position.x][position.y] = value

    def __getitem__(self, position: Position) -> int:
        return self.m[position.x][position.y]


class BlackBoardAccess(BoardAccess):
    def __init__(self, board: Board):
        super().__init__(board)

    def __setitem__(self, position: Position, value):
        self.m[position.x][7 - position.y] = value

    def __getitem__(self, position: Position) -> int:
        return self.m[position.x][7 - position.y]


class BoardBehaviour:
    pieces_types = [
        Empty(),
        Pawn(),
        Bishop(),
        Knight(),
        Rook(),
        Queen(),
        King()
    ]

    @staticmethod
    def at(access: BoardAccess, position: Position):
        return BoardBehaviour.pieces_types[access[position]]

    @staticmethod
    def move(access: BoardAccess, move: Move):
        # TODO: validate
        eat = BoardBehaviour.at(access, move.end)
        BoardBehaviour.apply(access, move)
        return eat

    @staticmethod
    def apply(access: BoardAccess, move: Move) -> ndarray:
        access[move.end] = access[move.begin]
        access[move.begin] = 0
        return access.m
