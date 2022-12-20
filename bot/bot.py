from chess.player import Player
from chess.move import Move, positions
from chess.board import BoardStateAccess, BoardNode

from numpy import ndarray


class Bot(Player):
    def __init__(self, level, advantage_map: ndarray, pieces_cost: list):
        super().__init__()
        self.level = level  # bot difficulty level(number of calculated moves)
        self.advantage_map = advantage_map
        self.pieces_cost = pieces_cost

    def position_analysis(self, board_access: BoardStateAccess) -> int:
        advantage = 0
        for position in positions:
            piece = board_access[position]
            if piece == 0:
                continue
            if 0 < piece < 7:
                advantage -= self.advantage_map[piece][position.x][position.y]
                advantage -= self.pieces_cost[piece]
            else:
                if piece < 0:
                    piece += 10
                elif piece > 7:
                    piece -= 10
                advantage += self.advantage_map[piece][position.x][position.y]
                advantage += self.pieces_cost[piece]
        return advantage

    def move_analysis(self, x: int, board_node: BoardNode) -> int:
        if x == 0:
            return self.position_analysis(board_node.state_access)
        bot_advantage = -1000000
        player_advantage = 1000000
        for move1 in board_node.possible_moves:
            moved_board_1: BoardNode = board_node.apply(move1)
            for move2 in moved_board_1.possible_moves:
                moved_board_2 = moved_board_1.apply(move2)
                advantage = self.move_analysis(x - 1, moved_board_2)
                if bot_advantage < advantage:
                    bot_advantage = advantage
            if player_advantage > bot_advantage:
                player_advantage = bot_advantage
        return player_advantage

    def get_move(self, board_node: BoardNode) -> Move:
        best_move = None
        best_advantage = -10000
        # print(board_node.turn.side, len(board_node.possible_moves), '\n',
        #       *map(lambda x: str(x) + '\n', board_node.possible_moves))
        for move in board_node.possible_moves:
            moved_board = board_node.apply(move)
            advantage = self.move_analysis(self.level, moved_board)
            if advantage > best_advantage:
                best_move = move
                best_advantage = advantage
        return best_move
