from chess.board import BoardAccess, BoardBehaviour
from chess.move import Position, Move


class Piece:
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        pass


class Empty(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        return []


class Pawn(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        if position.y >= 8:
            return []
        next_position = position + Position(0, 1)
        if board_access[next_position] != 0:
            return []
        return [Move(position, next_position)]


class Bishop(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        pass


class Knight(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        pass


class Rook(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        pass


class Queen(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        pass


class King(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        pass
