from chess.move import Move
from chess.board import Board, BoardNode


class Player:
    def get_move(self, board_node: BoardNode) -> Move:
        pass


class PlayerController:
    def __init__(self, board: Board, player: Player):
        self.board = board
        self.player = player

    def move(self):
        self.board.apply(self.player.get_move(self.board.current))
