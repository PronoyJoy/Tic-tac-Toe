import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", width=10, height=3, command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)
        
        self.board[1][1] = "X"
        self.buttons[1][1].config(text="X", state=tk.DISABLED)
        
    def make_move(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = "O"
            self.buttons[i][j].config(text="O", state=tk.DISABLED)
            if self.check_win(self.board):
                messagebox.showinfo("Result", "You win!")
                self.reset_game()
                return
            if self.check_tie(self.board):
                messagebox.showinfo("Result", "It's a tie!")
                self.reset_game()
                return
            self.computer_move()
            if self.check_win(self.board):
                messagebox.showinfo("Result", "Computer wins!")
                self.reset_game()
                return
            if self.check_tie(self.board):
                messagebox.showinfo("Result", "It's a tie!")
                self.reset_game()
                return

    def computer_move(self):
        while True:
            i, j = random.randint(0, 2), random.randint(0, 2)
            if self.board[i][j] == " ":
                self.board[i][j] = "X"
                self.buttons[i][j].config(text="X", state=tk.DISABLED)
                break

    def check_win(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return True
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return True
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        return False

    def check_tie(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ", state=tk.NORMAL)
        self.board[1][1] = "X"
        self.buttons[1][1].config(text="X", state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
