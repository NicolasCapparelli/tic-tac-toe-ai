from TTTAgent import TTTAgent
from tictactoe import TicTacToe, Marker


def play_tic_tac_toe():
    print("Select marker, x or o: ", end="")
    player_marker = Marker.x if input() == 'x' else Marker.o
    print()

    agent_marker = Marker.x if player_marker == Marker.o else Marker.o

    agent = TTTAgent("Tod", agent_marker)
    board = TicTacToe()
    while not board.finished:
        if board.turn == player_marker:
            next_move = get_user_input()
        else:
            avail_pos = board.get_all_available_positions()
            next_move = agent.find_best_move(board.board, avail_pos)

        x = next_move[0]
        y = next_move[1]
        board.place_marker(x, y)
        print(f"Move {board.moves}")
        board.print_board()
        print()

    print("Thanks for playing!")


def get_user_input():
    print("Coordinates: ", end='')
    position = input()
    print()

    position = position.split(",")
    return int(position[0])-1, int(position[1])-1


def main():
    play_tic_tac_toe()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
