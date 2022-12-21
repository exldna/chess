from bot import Bot, advantage_map, pieces_cost
from chess import Chess


def main():
    bot1 = Bot(1, advantage_map, pieces_cost)
    bot2 = Bot(1, advantage_map, pieces_cost)
    Chess(bot1, bot2).play()


if __name__ == "__main__":
    main()
