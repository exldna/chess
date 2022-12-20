from numpy import array, dtype

from bot.bot import Bot
from bot.massive import advantage_map, pieces_cost
from chess import Chess
from chess.board import BoardState

start_state = BoardState(array([
        [1, 0, 0, 0, 0, 0, 0, 11],
        [1, 0, 0, 0, 0, 0, 0, 11],
        [1, 0, 0, 0, 0, 0, 0, 11],
        [1, 0, 0, 0, 0, 0, 0, 11],
        [1, 0, 0, 0, 0, 0, 0, 11],
        [1, 0, 0, 0, 0, 0, 0, 11],
        [1, 0, 0, 0, 0, 0, 0, 11],
        [1, 0, 0, 0, 0, 0, 0, 11],
    ], dtype=dtype("i1")))


def main():
    bot1 = Bot(1, advantage_map, pieces_cost)
    bot2 = Bot(1, advantage_map, pieces_cost)
    Chess(bot1, bot2).play()


if __name__ == "__main__":
    main()
