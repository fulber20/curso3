import tkinter as tk
from tkinter import messagebox
import random

class JuegoTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.reset_game()

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.player = "X"
        self.game_over = False

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.master, text=" ", font=('Arial', 60), width=5, height=2,
                                   command=lambda r=row, c=col: self.player_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def player_move(self, row, col):
        if self.board[row][col] == " " and not self.game_over:
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)
            if self.check_winner(self.player):
                self.end_game(f"Jugador {self.player} gana!")
            elif self.is_draw():
                self.end_game("Es un empate!")
            else:
                self.player = "O"
                self.ai_move()

    def ai_move(self):
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
        if available_moves and not self.game_over:
            row, col = random.choice(available_moves)
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)
            if self.check_winner(self.player):
                self.end_game(f"Jugador {self.player} gana!")
            elif self.is_draw():
                self.end_game("Es un empate!")
            else:
                self.player = "X"

    def check_winner(self, player):
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != " " for row in range(3) for col in range(3))

    def end_game(self, message):
        self.game_over = True
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state="disabled")
        response = messagebox.askyesno("Juego Terminado", message + "\n¿Quieres reiniciar el juego?")
        if response:
            self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = JuegoTicTacToe(root)
    root.mainloop()
