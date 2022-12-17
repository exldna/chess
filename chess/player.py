from chess.board import Board
from chess.move import Move


class Player:
    def get_move(self) -> Move:
        pass


class PlayerController:
    def __init__(self, board: Board, player: Player):
        self.board = board
        self.player = player

    def move(self):
        pass


class WhiteController(PlayerController):
    def __init__(self, board: Board, player: Player):
        super().__init__(board, player)

    def move(self):
        self.board.move(self.player.get_move())


class BlackController(PlayerController):
    def __init__(self, board: Board, player: Player):
        super().__init__(board, player)

    def move(self):
        self.board.move(self.player.get_move())
