from chess.board import Board
from chess.player import Player
from chess.move import Position
from massive import *

class Bot(Player):
    def __init__(self, level, advantage_map: ndarray):
        self.level = level # bot difficulty level(number of calculated moves)

    def position_analysis(self, map: ndarray, advantage_map : ndarray, pieces_cost : list) -> int: #analys any board-position for bot
        x = 0 #advantage
        for i in range (8):
            for j in range (8):#checking all cells
                x+=advantage_map[map[i][j]][i][j] + pieces_cost[map[i][j]]
        return x

    def one_move_analysis(self, map : ndarray, possible_moves : list, advantage_map : ndarray, pieces_cost : list):
        advantage = -100000
        map_copy = map
        for move in possible_moves:
            if self.position_analysis(Board.move(possible_moves[1], map_copy), advantage_map, pieces_cost) > advantage:
                advantage = self.position_analysis(Board.move(possible_moves[1], map_copy), advantage_map, pieces_cost)

    def move_analysis(self, map: ndarray) -> (list, int): #analysis for level-moves bot+gamer
        x = self.level# number of moves(s) = bot.level
        advantage = -100000
        if self.team == 1:#if the bot is playing for white
            if x != 0:
                pass
            else:
                pass
        else:#if the bot is playing for black
            pass
    def move(self) -> tuple[Position]:
        pass