from numpy import dtype, array

from chess.player import Player, PlayerController
from chess.board import Board, BoardState


class Chess:
    def __init__(self, white: Player, black: Player, start_state: BoardState = None):
        if start_state is None:
            start_state = BoardState(array([
                [4, 1, 0, 0, 0, 0, 11, 14],
                [3, 1, 0, 0, 0, 0, 11, 13],
                [2, 1, 0, 0, 0, 0, 11, 12],
                [5, 1, 0, 0, 0, 0, 11, 15],
                [6, 1, 0, 0, 0, 0, 11, 16],
                [2, 1, 0, 0, 0, 0, 11, 12],
                [3, 1, 0, 0, 0, 0, 11, 13],
                [4, 1, 0, 0, 0, 0, 11, 14],
            ], dtype=dtype("i1")))
        self.board = Board(start_state)
        self.white_player = PlayerController(self.board, white)
        self.black_player = PlayerController(self.board, black)

    def play(self):
        print(self.board.current.state_access.board_state.state, '\n')
        while True:
            self.white_player.move()
            print(self.board.current.state_access.board_state.state, '\n')
            self.black_player.move()
            print(self.board.current.state_access.board_state.state, '\n')
