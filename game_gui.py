from TTTAgent import TTTAgent
from tictactoe import TicTacToe, Marker
import math
from tkinter import *


class GameGui(Tk):
    button_array = []
    game = None
    agent = None
    player_marker = None
    agent_marker = None

    def __init__(self, game):
        super().__init__()

        self.game = game
        self.title("Tic Tac Toe Agent")

        for x in range(0, 3):
            for y in range(0, 3):
                square = Button(self,
                                command=lambda r=x, c=y: self.advance_game(r, c),
                                font=('normal', 30, 'normal'),
                                text="  ",
                                width=5,
                                height=3)
                square.grid(row=x, column=y)
                square['state'] = 'disabled'
                self.button_array.append(square)

        self.info_label = Label(self)
        self.prompt_label = Label(self)

        self.marker_option_x = Button(self, width=2, height=2)
        self.marker_option_o = Button(self, width=2, height=2)

        self.reset_button = Button(self, text="Play Again", command=self.reset)
        self.game_setup()

        self.mainloop()

    def reset(self):
        self.game = TicTacToe()
        self.update_game_board()
        for button in self.button_array:
            button['state'] = 'disabled'
        self.prompt_label.grid_forget()
        self.prompt_label.grid_forget()
        self.reset_button.grid_forget()
        self.game_setup()

    def game_setup(self):
        self.info_label.config(text="Choose a marker: ")
        self.marker_option_x.config(command=lambda marker='x': self.start_game(marker),
                                    font=('normal', 10, 'normal'),
                                    text=" X ")

        self.marker_option_o = Button(command=lambda marker='o': self.start_game(marker),
                                      font=('normal', 10, 'normal'),
                                      text=" O ")

        self.info_label.grid(row=4, column=0)
        self.marker_option_x.grid(row=4, column=1)
        self.marker_option_o.grid(row=4, column=2)

    def start_game(self, user_marker_choice):
        for button in self.button_array:
            button['state'] = 'normal'

        self.player_marker = Marker.x if user_marker_choice == 'x' else Marker.o
        self.agent_marker = Marker.o if self.player_marker == Marker.x else Marker.x
        self.agent = TTTAgent("Tod", self.agent_marker)

        self.marker_option_x.grid_remove()
        self.marker_option_o.grid_remove()

        if self.game.turn == self.player_marker:
            self.info_label.config(text=f"You move first!")
        else:
            self.run_agent_turn()
            self.update_game_board()

    def advance_game(self, r, c):
        self.game.place_marker(r, c)
        self.update_game_board()

        if not self.game.finished:
            self.run_agent_turn()
            self.update_game_board()
            self.info_label.config(text="Your turn!")

        if self.game.finished:
            self.end_game()

    def update_game_board(self):
        for i, button in enumerate(self.button_array):
            marker = self.game.board[i // 3][(i % 3)]
            button.config(text=f"{marker.value if marker is not None else ''}")

    def end_game(self):
        self.info_label.grid(row=4, column=1)
        if self.game.winner != "tie":
            self.info_label.config(text=f"{self.game.winner} wins!")
        else:
            self.info_label.config(text=f"It's a tie!")

        self.reset_button.config(width=10, height=2)
        self.reset_button.grid(row=6, column=1)

    def run_agent_turn(self):
        r, c = self.agent.find_best_move(self.game.board, self.game.get_all_available_positions())
        self.game.place_marker(r, c)
