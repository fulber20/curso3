import tkinter as tk
import random

class juegoTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master=("Tic Tac Toe")
        self.reset_game()
        
    def reset_game(selft):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.player = "X"
        
if __name__ == "__main__":
    root = tk.Tk()
    game = juegoTicTacToe(root)
    root.mainloop()

