import tkinter as tk
import tkinter.messagebox as messagebox
import random

class MinesweeperGame:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[0] * cols for _ in range(rows)]
        self.is_revealed = [[False] * cols for _ in range(rows)]
        self.mines = set()
        self.game_over = False

        self.generate_board()
        self.place_mines()

    def generate_board(self):
        for _ in range(self.num_mines):
            while True:
                row = random.randint(0, self.rows - 1)
                col = random.randint(0, self.cols - 1)
                if (row, col) not in self.mines:
                    self.mines.add((row, col))
                    self.board[row][col] = -1
                    break

        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != -1:
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.board[nr][nc] == -1:
                                count += 1
                    self.board[r][c] = count

    def place_mines(self):
        for r, c in self.mines:
            self.board[r][c] = -1

    def reveal_cell(self, row, col):
        if self.game_over or self.is_revealed[row][col]:
            return

        if (row, col) in self.mines:
            self.game_over = True
            messagebox.showinfo("Game Over", "Game Over! You clicked on a mine.")
        else:
            self.is_revealed[row][col] = True
            if self.board[row][col] == 0:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            self.reveal_cell(nr, nc)

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.is_revealed[r][c] and (r, c) not in self.mines:
                    return False
        return True

def create_ui(game):
    window = tk.Tk()
    window.title("Minesweeper")

    buttons = [[None] * game.cols for _ in range(game.rows)]

    def button_click(r, c):
        if not game.game_over:
            game.reveal_cell(r, c)
            update_ui()

            if game.check_win():
                messagebox.showinfo("Congratulations", "Congratulations! You've won the game.")
                window.destroy()

    def update_ui():
        for r in range(game.rows):
            for c in range(game.cols):
                if game.is_revealed[r][c]:
                    if (r, c) in game.mines:
                        buttons[r][c].config(text="*", state=tk.DISABLED, relief=tk.SUNKEN)
                    else:
                        buttons[r][c].config(text=str(game.board[r][c]), state=tk.DISABLED, relief=tk.SUNKEN)
                else:
                    buttons[r][c].config(text="", state=tk.NORMAL, relief=tk.RAISED)

    for r in range(game.rows):
        for c in range(game.cols):
            buttons[r][c] = tk.Button(window, width=3, height=1,
                                      command=lambda r=r, c=c: button_click(r, c))
            buttons[r][c].grid(row=r, column=c)

    window.mainloop()

if __name__ == "__main__":
    rows = 8
    cols = 8
    num_mines = 10
    game = MinesweeperGame(rows, cols, num_mines)
    create_ui(game)
