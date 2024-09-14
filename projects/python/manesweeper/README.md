# Minesweeper

This code is a simple Minesweeper game implemented in Python using the `tkinter` library for the graphical user interface (GUI). Here’s an easy-to-understand explanation of how it works, step by step:

## 1. Imports
- `import tkinter as tk`: Imports the `tkinter` library, which is used to create the graphical user interface.
- `import tkinter.messagebox as messagebox`: Imports a module from `tkinter` to show message boxes (like "Game Over" or "Congratulations" messages).
- `import random`: Imports the `random` library, which is used to randomly place mines on the board.

## 2. `MinesweeperGame` Class
This class handles the main logic of the game. It contains methods to create the board, place mines, reveal cells, and check if the player has won.

- **`__init__(self, rows, cols, num_mines)`**:
  - This is the constructor of the class. It initializes the board with a given number of rows (`rows`) and columns (`cols`), and specifies how many mines (`num_mines`) will be on the board.
  - It creates an empty board and a set to store the positions of the mines, as well as an `is_revealed` matrix to track which cells have been revealed.
  - It then calls methods to generate the board and place the mines.

- **`generate_board(self)`**:
  - Randomly places mines on the board.
  - Then, for each cell that is not a mine, it counts how many mines are in the surrounding cells and stores that number in the cell.

- **`place_mines(self)`**:
  - Ensures that mines are marked with `-1` on the board.

- **`reveal_cell(self, row, col)`**:
  - Reveals the cell at the position `(row, col)`. If it’s a mine, the game is over. If not, it reveals the number of surrounding mines.
  - If the cell is `0` (no surrounding mines), it automatically reveals the neighboring cells.

- **`check_win(self)`**:
  - Checks if the player has won the game. This happens if all non-mined cells have been revealed.

## 3. `create_ui(game)` Function
This function creates the game’s graphical interface using `tkinter`.

- **Main Window**:
  - Creates a window with the title "Minesweeper."

- **Grid Buttons**:
  - Creates buttons for each cell on the board. When a button is clicked, it calls `button_click` to reveal the corresponding cell.

- **`button_click(r, c)`**:
  - This function handles clicking on a cell on the board. It reveals the cell and updates the interface.
  - If the player wins, it shows a congratulations message and closes the window.

- **`update_ui()`**:
  - Updates the visual state of the buttons based on whether the cell has been revealed, if it’s a mine, or if it shows a number.

## 4. Main Code
- The block `if __name__ == "__main__":` runs when the file is executed directly.
- It sets up an 8x8 board with 10 mines and then creates a game instance. Finally, it calls `create_ui(game)` to display the game interface.

## Summary
This code implements a classic Minesweeper game where the player needs to uncover all the non-mined cells on an 8x8 board while avoiding the 10 hidden mines. The graphical interface allows the player to interact with the game, and the logic manages mine placement, cell revealing, and checking whether the player has won or lost.