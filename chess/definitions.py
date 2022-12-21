from chess.pieces import Empty, Pawn, Bishop, Knight, Rook, Queen, King
from chess.move import Position

pieces_types = [
    Empty(),
    Pawn(),
    Bishop(),
    Knight(),
    Rook(),
    Queen(),
    King()
]

positions = [Position(x, y) for x in range(8) for y in range(8)]
