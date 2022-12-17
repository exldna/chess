from chess.board import Board
from chess.player import Player, PlayerController
from chess.move import Move

from numpy import ndarray, copy


class Bot(Player):
    def __init__(self, level, advantage_map: ndarray, pieces_cost: list):
        super().__init__()
        self.level = level  # bot difficulty level(number of calculated moves)
        self.advantage_map = advantage_map
        self.pieces_cost = pieces_cost

    def position_analysis(self, board_map: ndarray) -> int:  # analys any board-position for bot
        return sum([self.advantage_map[board_map[i][j]][i][j] + self.pieces_cost[board_map[i][j]]
                    for i in range(8) for j in range(8)])

    def move_analysis(self, x: int, board_map: ndarray) -> int:
        if x == 0:
            return self.position_analysis(board_map)
        bot_advantage = -10000
        player_advantage = 10000
        for move in self.controller.get_possible_moves(board_map):
            advantage = self.move_analysis(x - 1, Board.apply(copy(board_map), move))
            if bot_advantage < advantage:
                bot_advantage = advantage
            if player_advantage > bot_advantage:
                player_advantage = bot_advantage
        return player_advantage

    def get_move(self) -> Move:
        possible_moves = self.controller.get_possible_moves(self.controller.board.map)
        best_move = possible_moves[0]
        best_advantage = self.move_analysis(self.level, self.controller.board.moved(best_move))
        for move in possible_moves[1:]:
            advantage = self.move_analysis(self.level, self.controller.board.moved(move))
            if advantage > best_advantage:
                best_move = move
                best_advantage = advantage
        return best_move
