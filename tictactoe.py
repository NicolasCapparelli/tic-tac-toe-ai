from enum import Enum
import random


class Marker(Enum):
    x = 'X'
    o = 'O'

    def __str__(self):
        return f'{self.value}'


class TicTacToe:
    board = None
    finished = False
    turn = None
    moves = 0

    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.turn = Marker.x if random.randint(0, 1) == 1 else Marker.o

    def place_marker(self, x, y):
        if not self.position_available(self.board, x, y):
            return False
        self.board[x][y] = self.turn
        self.moves += 1
        self.update_game_state()
        return True

    def update_game_state(self):
        winner = TicTacToe.check_win(self.board, self.moves)
        if winner is not None:
            self.finished = True
            print(f'{winner} is the winner!!')
            return

        self.turn = Marker.x if self.turn == Marker.o else Marker.o
        self.finished = True if self.moves == 9 else False

    def get_all_available_positions(self):
        positions = []
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] is None:
                    positions.append((x, y))
        return positions

    def print_board(self):
        for row in self.board:
            print('[', end='')
            for col in row:
                if col is None:
                    col = ' '
                print(f'|\t{col}\t|', end='')
            print(']')
        print()

    """ HELPER METHODS """
    @staticmethod
    def position_available(board, x, y):
        return board[x][y] is None

    @staticmethod
    def check_win(board, moves):
        for line in TicTacToe.lines(board):
            if len(set(line)) == 1 and line[0] is not None:
                return line[0].value

        return "tie" if moves == 9 else None

    @staticmethod
    def _lines(board):
        yield from board  # the rows
        yield [board[i][i] for i in range(len(board))]  # one of the diagonals

    @staticmethod
    def lines(board):
        yield from TicTacToe._lines(board)
        # rotate the board 90 degrees to get the columns and the other diagonal
        yield from TicTacToe._lines(list(zip(*reversed(board))))


