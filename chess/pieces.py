from chess.position import Position


class Piece:
    def get_moves(self) -> list[Position]:
        pass


class Empty(Piece):
    def get_moves(self) -> list[Position]:
        return list()


class Pawn(Piece):
    def get_moves(self) -> list[Position]:
        return [Position(0, 1)]


class Bishop(Piece):
    def get_moves(self) -> list[Position]:
        return [Position(0, 1)]


class Knight(Piece):
    pass


class Rook(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass
