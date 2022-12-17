from numpy import ndarray

from chess.board import Board
from chess.move import Move


class Player:
    def __init__(self):
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def get_move(self) -> Move:
        pass


class PlayerController:
    def __init__(self, board: Board, player: Player):
        self.board = board
        self.player = player

    def get_possible_moves(self, board_map: ndarray) -> list[Move]:
        pass # TODO: write this

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
