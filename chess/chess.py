from chess.board import Board
from chess.player import Player


class Chess:
    def __init__(self, white: Player, black: Player):
        self.white: Player = white
        self.black: Player = black

        self.board = Board()

    def play(self):
        while not self.board.is_terminated():
            while self.board.move(*self.white.move()) is None:
                pass
            while self.board.move(*self.black.move()) is None:
                pass
