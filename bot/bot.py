from chess.board import Board
from chess.player import Player
from chess.move import Move

from numpy import ndarray


class Bot(Player):
    def __init__(self, level, advantage_map: ndarray):
        self.level = level  # bot difficulty level(number of calculated moves)
        self.advantage_map = advantage_map

    def position_analysis(self, map: ndarray, advantage_map: ndarray,
                          pieces_cost: list) -> int:  # analys any board-position for bot
        return sum([advantage_map[map[i][j]][i][j] + pieces_cost[map[i][j]] for i in range(8) for j in range(8)])

    def one_move_analysis(self, board: Board, possible_moves: list, advantage_map: ndarray, pieces_cost: list):
        advantage = -100000
        for move in possible_moves:
            board.move(move) # TODO: write moves visitor
            advantage = max(advantage, self.position_analysis(board.map, advantage_map, pieces_cost))

    def move_analysis(self, map: ndarray) -> (list, int):  # analysis for level-moves bot+gamer
        x = self.level  # number of moves(s) = bot.level
        advantage = -100000
        # ...

    def move(self) -> Move:
        pass
