from numpy import ndarray, copy as np_copy
from chess.move import Position, Move, positions
from chess.pieces import pieces_types, PieceOnBoard


class BoardState:
    def __init__(self, state: ndarray):
        self.state = state

    def __getitem__(self, position: Position) -> int:
        return self.state[position.x][position.y]

    def __setitem__(self, position: Position, value):
        self.state[position.x][position.y] = value

    def copy(self):
        return BoardState(np_copy(self.state))


class BoardStateAccess:
    def __init__(self, board_state: BoardState):
        self.board_state = board_state
        self.possible_moves: list[Move] | None = None
        self.my_pieces: list[PieceOnBoard] | None = None

    def __setitem__(self, position: Position, value):
        pass

    def __getitem__(self, position: Position) -> int:
        pass

    def apply(self, move: Move):
        self[move.end] = self[move.begin]
        self[move.begin] = 0

    def get_possible_moves(self) -> list[Move]:
        if self.possible_moves is None:
            self.possible_moves = list()
            for piece_on_board in self.get_my_pieces():
                piece_possible_moves = piece_on_board.get_possible_moves(self)
                self.possible_moves += piece_possible_moves
        return self.possible_moves

    def get_my_pieces(self) -> list[PieceOnBoard]:
        if self.my_pieces is None:
            self.my_pieces = list()
            for position in positions:
                piece = self[position]
                if 0 < piece < 7:
                    self.my_pieces.append(PieceOnBoard(pieces_types[piece], position))
        return self.my_pieces


class WhiteBoardStateAccess(BoardStateAccess):
    def __init__(self, board_state: BoardState):
        super().__init__(board_state)

    def __setitem__(self, position: Position, value: int):
        self.board_state[position] = value

    def __getitem__(self, position: Position) -> int:
        return self.board_state[position]


class BlackBoardStateAccess(BoardStateAccess):
    pos_comp = Position(7, 7)

    def __init__(self, board_state: BoardState):
        super().__init__(board_state)

    def __setitem__(self, position: Position, value):
        real_pos = BlackBoardStateAccess.pos_comp - position
        if value == 0:
            self.board_state[real_pos] = 0
        else:
            self.board_state[real_pos] = value + 10

    def __getitem__(self, position: Position) -> int:
        value = self.board_state[BlackBoardStateAccess.pos_comp - position]
        if value == 0:
            return 0
        return value - 10


class Turn:
    def __init__(self, side: bool = True):
        self.side = side

    def create_access(self, board_state: BoardState) -> BoardStateAccess:
        if self.side:
            return WhiteBoardStateAccess(board_state)
        else:
            return BlackBoardStateAccess(board_state)

    def create_next_access(self, board_state: BoardState) -> BoardStateAccess:
        if self.side:
            return BlackBoardStateAccess(board_state)
        else:
            return WhiteBoardStateAccess(board_state)

    def produce(self):
        return Turn(not self.side)


class BoardNode:
    def __init__(self, state_access: BoardStateAccess, turn: Turn):
        self.turn = turn
        self.state_access = state_access
        self.possible_moves = dict.fromkeys(self.state_access.get_possible_moves())

    def apply(self, move: Move):
        if move is None or move not in self.possible_moves:
            print(*self.possible_moves)
            raise ValueError("impossible move - " + str(move))
        if self.possible_moves.get(move) is None:
            board_state_copy = self.state_access.board_state.copy()
            next_state_access = self.turn.create_access(board_state_copy)
            next_state_access.apply(move)
            self.possible_moves[move] = BoardNode(
                self.turn.create_next_access(board_state_copy), self.turn.produce())
        return self.possible_moves[move]


class Board:
    def __init__(self, board_state: BoardState):
        # white turn first
        self.root = BoardNode(WhiteBoardStateAccess(board_state), Turn())
        self.current = self.root

    def apply(self, move: Move):
        self.current = self.current.apply(move)
