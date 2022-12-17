from chess.board import Board
from chess.player import Player, WhiteController, BlackController


class Chess:
    def __init__(self, white: Player, black: Player):
        self.board = Board()

        self.white = WhiteController(self.board, white)
        self.white.player.set_controller(self.white)

        self.black = BlackController(self.board, black)
        self.black.player.set_controller(self.black)

    def play(self):
        while not self.board.is_terminated():
            self.white.move()
            self.black.move()
