from chess.move import Position, Move


class PieceType:
    def get_possible_moves(self, board_access, position: Position) -> list[Move]:
        pass


class Empty(PieceType):
    def get_possible_moves(self, board_access, position: Position) -> list[Move]:
        return []


class Pawn(PieceType):
    def get_possible_moves(self, board_access, position: Position) -> list[Move]:
        if position.y >= 7:
            return []
        possible_moves: list = []
        next_position = position + Position(0, 1)
        if board_access[next_position] == 0:
            possible_moves.append(Move(position, next_position))
        if position.x != 7:
            next_position_1 = position + Position(1, 1)
            if board_access[next_position_1] != 0:
                possible_moves.append(Move(position, next_position_1))
        if position.x != 0:
            next_position_2 = position + Position(-1, 1)
            if board_access[next_position_2] != 0:
                possible_moves.append(Move(position, next_position_2))
        return possible_moves


class Bishop(PieceType):
    def get_possible_moves(self, board_access, position: Position) -> list[Move]:
        diagonals = [
            [Position(position.x - i, position.y + i) for i in range(1, min(position.x, 7 - position.y) + 1)],
            [Position(position.x - i, position.y - i) for i in range(1, min(position.x, position.y) + 1)],
            [Position(position.x + i, position.y - i) for i in range(1, min(7 - position.x, position.y) + 1)],
            [Position(position.x + i, position.y + i) for i in range(1, min(7 - position.x, 7 - position.y) + 1)]
        ]
        possible_moves: list = []
        for diagonal in diagonals:
            for coord in diagonal:
                possible_moves.append(Move(position, coord))
                if board_access[coord] != 0:
                    break
        return possible_moves


class Knight(PieceType):
    def get_possible_moves(self, board_access, position: Position) -> list[Move]:
        possible_moves: list = []
        if position.x - 2 >= 0 and position.y - 1 >= 0:
            possible_moves.append(Move(position, position + Position(-2, -1)))
        if position.x - 2 >= 0 and position.y + 1 < 8:
            possible_moves.append(Move(position, position + Position(-2, 1)))
        if position.x + 2 < 8 and position.y - 1 >= 0:
            possible_moves.append(Move(position, position + Position(2, -1)))
        if position.x + 2 < 8 and position.y + 1 < 8:
            possible_moves.append(Move(position, position + Position(2, 1)))
        if position.y - 2 >= 0 and position.x - 1 >= 0:
            possible_moves.append(Move(position, position + Position(-1, -2)))
        if position.y - 2 >= 0 and position.x + 1 < 8:
            possible_moves.append(Move(position, position + Position(1, -2)))
        if position.y + 2 < 8 and position.x - 1 >= 0:
            possible_moves.append(Move(position, position + Position(-1, 2)))
        if position.y + 2 < 8 and position.x + 1 < 8:
            possible_moves.append(Move(position, position + Position(1, 2)))
        return possible_moves


class Rook(PieceType):
    def get_possible_moves(self, board_access, position: Position) -> list[Move]:
        directions = [
            [Position(position.x - i, position.y) for i in range(1, position.x + 1)],
            [Position(position.x, position.y - i) for i in range(1, position.y + 1)],
            [Position(position.x + i, position.y) for i in range(1, 7 - position.x + 1)],
            [Position(position.x, position.y + i) for i in range(1, 7 - position.y + 1)]
        ]
        possible_moves: list = []
        for direction in directions:
            for coord in direction:
                possible_moves.append(Move(position, coord))
                if board_access[coord] != 0:
                    break
        return possible_moves


class Queen(PieceType):
    def get_possible_moves(self, board_access, position: Position) -> list[Move]:
        directions = [
            [Position(position.x - i, position.y) for i in range(1, position.x + 1)],
            [Position(position.x, position.y - i) for i in range(1, position.y + 1)],
            [Position(position.x + i, position.y) for i in range(1, 7 - position.x + 1)],
            [Position(position.x, position.y + i) for i in range(1, 7 - position.y + 1)],
            [Position(position.x - i, position.y + i) for i in range(1, min(position.x, 7 - position.y) + 1)],
            [Position(position.x - i, position.y - i) for i in range(1, min(position.x, position.y) + 1)],
            [Position(position.x + i, position.y - i) for i in range(1, min(7 - position.x, position.y) + 1)],
            [Position(position.x + i, position.y + i) for i in range(1, min(7 - position.x, 7 - position.y) + 1)]
        ]
        possible_moves: list = []
        for direction in directions:
            for coord in direction:
                possible_moves.append(Move(position, coord))
                if board_access[coord] != 0:
                    break
        return possible_moves


class King(PieceType):
    def get_possible_moves(self, board_access, position: Position) -> list[Move]:
        possible_moves: list = []
        if position.x - 1 >= 0 and position.y - 1 >= 0:
            possible_moves.append(Move(position, position + Position(-1, -1)))
        if position.x - 1 >= 0 and position.y + 1 < 8:
            possible_moves.append(Move(position, position + Position(-1, 1)))
        if position.x + 1 < 8 and position.y - 1 >= 0:
            possible_moves.append(Move(position, position + Position(1, -1)))
        if position.x + 1 < 8 and position.y + 1 < 8:
            possible_moves.append(Move(position, position + Position(1, 1)))
        if position.y - 1 >= 0:
            possible_moves.append(Move(position, position + Position(0, -1)))
        if position.y + 1 < 8:
            possible_moves.append(Move(position, position + Position(0, 1)))
        if position.x - 1 >= 0:
            possible_moves.append(Move(position, position + Position(-1, 0)))
        if position.x + 1 < 8:
            possible_moves.append(Move(position, position + Position(1, 0)))
        return possible_moves


class PieceOnBoard:
    def __init__(self, piece: PieceType, position: Position):
        self.piece = piece
        self.position = position

    def get_possible_moves(self, board_access):
        return self.piece.get_possible_moves(board_access, self.position)
