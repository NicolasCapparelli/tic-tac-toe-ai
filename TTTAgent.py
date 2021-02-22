from tictactoe import TicTacToe, Marker

MAX_MOVES = 9  # Total number of possible moves in a tic tac toe game


class TTTAgent:
    name = ""
    marker_type = None
    opponent_marker_type = None

    def __init__(self, name, marker_type):
        self.name = name
        self.marker_type = marker_type
        self.opponent_marker_type = Marker.x if self.marker_type == Marker.o else Marker.o

    def find_best_move(self, board, available_positions):
        """ For a given game state (board), return the best move by calling minimax on all available positions  """

        # When available_positions is 9, the agent starts. Best opening move is going to a corner.
        if len(available_positions) == 9:
            return available_positions[0]

        best_move = None
        best_move_score = float('-inf')
        for pos in available_positions:
            x = pos[0]
            y = pos[1]
            board[x][y] = self.marker_type
            move_score = self.minimax(board, False, MAX_MOVES - len(available_positions) + 1)
            board[x][y] = None  # Undo the move to prevent messing with the actual game board
            if move_score > best_move_score:
                best_move_score = move_score
                best_move = pos
        return best_move

    def minimax(self, board, is_maximizing_player, moves):
        """
            Given a game state, play out all possible scenarios, assigns them a score,
            and return the highest score of all the scenarios
        """
        winner = TicTacToe.check_win(board, moves)
        if winner is not None:
            return self.get_score(winner)

        return self.traverse_for_best_score(board, is_maximizing_player, moves)

    def traverse_for_best_score(self, board, is_maximizing_player, moves):
        best_score = float('-inf') if is_maximizing_player else float('inf')
        for x in range(0, 3):
            for y in range(0, 3):
                if board[x][y] is None:
                    board[x][y] = self.marker_type if is_maximizing_player else self.opponent_marker_type
                    move_score = self.minimax(board, not is_maximizing_player, moves + 1)
                    board[x][y] = None
                    best_score = max(move_score, best_score) if is_maximizing_player else min(move_score, best_score)
        return best_score

    def get_score(self, winner):
        """ Maps a winner string [ 'x' | 'o' | 'tie'] to a score value based on the agent's marker_type """
        if winner == self.marker_type.value:
            return 1
        elif winner == "tie":
            return 0
        else:
            return -1
