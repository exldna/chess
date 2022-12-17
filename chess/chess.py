from chess.board import Board
from chess.player import Player, WhitePlayerController, BlackPlayerController


class Chess:
    def __init__(self, white: Player, black: Player):
        self.board = Board()
        self.white_player_controller = WhitePlayerController(self.board, white)
        self.black_player_controller = BlackPlayerController(self.board, black)

    def play(self):
        while not self.board.is_terminated():
            self.white_player_controller.move()
            self.black_player_controller.move()
