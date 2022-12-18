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


class Bishop(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        possible_moves: list = []
        diags = [[Position(position.x - i, position.y + i) for i in range(1, min(position.x, 7 - position.y) + 1)],
                 [Position(position.x - i, position.y - i) for i in range(1, min(position.x, position.y) + 1)],
                 [Position(position.x + i, position.y - i) for i in range(1, min(7 - position.x, position.y) + 1)],
                 [Position(position.x + i, position.y + i) for i in range(1, min(7 - position.x, 7 - position.y) + 1)]]
        for diag in diags:
            for coord in diag:
                possible_moves.append(Move(position, coord))
                if board_access[coord] != 0:
                    break
        return possible_moves


class Knight(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
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
            possible_moves.append(Move(position, position + Position(-1, 2)))
        if position.y + 2 < 8 and position.x - 1 >= 0:
            possible_moves.append(Move(position, position + Position(1, -2)))
        if position.y + 2 < 8 and position.x + 1 < 8:
            possible_moves.append(Move(position, position + Position(1, 2)))
        return possible_moves


class Rook(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        possible_moves: list = []
        diags = [[Position(position.x - i, position.y) for i in range(1, position.x + 1)],
                 [Position(position.x, position.y - i) for i in range(1, position.y + 1)],
                 [Position(position.x + i, position.y) for i in range(1, 7 - position.x + 1)],
                 [Position(position.x, position.y + i) for i in range(1, 7 - position.y + 1)]]
        for diag in diags:
            for coord in diag:
                possible_moves.append(Move(position, coord))
                if board_access[coord] != 0:
                    break
        return possible_moves


class Queen(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
        possible_moves: list = []
        diags = [[Position(position.x - i, position.y) for i in range(1, position.x + 1)],
                 [Position(position.x, position.y - i) for i in range(1, position.y + 1)],
                 [Position(position.x + i, position.y) for i in range(1, 7 - position.x + 1)],
                 [Position(position.x, position.y + i) for i in range(1, 7 - position.y + 1)],
                 [Position(position.x - i, position.y + i) for i in range(1, min(position.x, 7 - position.y) + 1)],
                 [Position(position.x - i, position.y - i) for i in range(1, min(position.x, position.y) + 1)],
                 [Position(position.x + i, position.y - i) for i in range(1, min(7 - position.x, position.y) + 1)],
                 [Position(position.x + i, position.y + i) for i in range(1, min(7 - position.x, 7 - position.y) + 1)]]
        for diag in diags:
            for coord in diag:
                possible_moves.append(Move(position, coord))
                if board_access[coord] != 0:
                    break
        return possible_moves


class King(Piece):
    def get_moves(self, board_access: BoardAccess, position: Position) -> list[Move]:
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
