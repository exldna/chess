from chess import Chess
from chess.player import Player


def main():
    player1 = Player()
    player2 = Player()
    chess_instance = Chess(player1, player2)
    chess_instance.play()


if __name__ == "__main__":
    main()
