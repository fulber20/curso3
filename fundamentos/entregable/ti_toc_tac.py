import tkinter as tk
import random

class juegoTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master=("Tic Tac Toe")
        self.reset_game()
        
if__name__=="__main__":
    root = tk.Tk()
    game =  juegoTicTacToe(root)
    root.mainloop()