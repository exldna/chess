from chess.board import Board, BoardBehaviour, BoardAccess, WhiteBoardAccess, BlackBoardAccess
from chess.move import Move, Position


class PlayerBehaviour:
    @staticmethod
    def get_possible_moves(board_access: BoardAccess) -> list[Move]:
        possible_moves = list()
        for x in range(8):
            for y in range(8):
                curr_position = Position(x, y)
                if 0 < board_access[curr_position] < 7:
                    piece = BoardBehaviour.at(board_access, curr_position)
                    possible_moves += piece.get_moves(board_access, curr_position)
        return possible_moves


class Player:
    def get_move(self, controller) -> Move:
        pass


class PlayerController:
    def __init__(self, board_access: BoardAccess, player: Player):
        self.board_access = board_access
        self.player = player

    def move(self):
        BoardBehaviour.move(self.board_access, self.player.get_move(self))


class WhitePlayerController(PlayerController):
    def __init__(self, board: Board, player: Player):
        super().__init__(WhiteBoardAccess(board), player)


class BlackPlayerController(PlayerController):
    def __init__(self, board: Board, player: Player):
        super().__init__(BlackBoardAccess(board), player)
