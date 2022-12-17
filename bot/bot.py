from chess.board import Board
from chess.player import Player, PlayerController
from chess.move import Move

from numpy import ndarray


class Bot(Player):
    def __init__(self, level, advantage_map: ndarray, pieces_cost: list):
        super().__init__()
        self.level = level  # bot difficulty level(number of calculated moves)
        self.advantage_map = advantage_map
        self.pieces_cost = pieces_cost

    def position_analysis(self, board_map: ndarray) -> int:  # analys any board-position for bot
        return sum([self.advantage_map[board_map[i][j]][i][j] + self.pieces_cost[board_map[i][j]]
                    for i in range(8) for j in range(8)])

    def move_analysis(self, controller: PlayerController, x: int, board_map: ndarray) -> int:
        if x == 0:
            return self.position_analysis(board_map)
        bot_advantage = -10000
        player_advantage = 10000
        for move1 in controller.get_possible_moves(board_map):
            for move2 in controller.get_possible_moves(controller.board.moved(move1)):
                advantage = self.move_analysis(controller, x - 1,
                                               Board.apply(controller.board.moved(move1), move2))
                if bot_advantage < advantage:
                    bot_advantage = advantage
            if player_advantage > bot_advantage:
                player_advantage = bot_advantage
        return player_advantage

    def get_move(self, controller: PlayerController) -> Move:
        best_move = Move()
        best_advantage = -10000
        for move in controller.get_possible_moves(controller.board.map):
            advantage = self.move_analysis(controller, self.level, controller.board.moved(move))
            if advantage > best_advantage:
                best_move = move
                best_advantage = advantage
        return best_move
