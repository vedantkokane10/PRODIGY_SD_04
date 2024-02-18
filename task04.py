import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    # Check if the number is not present in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is not present in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find an empty cell in the Sudoku grid
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)

    # If there are no empty locations, the Sudoku is solved
    if not empty_location:
        return True

    row, col = empty_location

    # Try filling the empty location with a number from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Assign the number to the empty location
            board[row][col] = num

            # Update the GUI with the current state of the board
            update_board_gui()

            # Recursively try to solve the Sudoku
            if solve_sudoku(board):
                return True

            # If the current assignment does not lead to a solution, backtrack
            board[row][col] = 0

            # Update the GUI with the backtracked state of the board
            update_board_gui()

    # No number from 1 to 9 works at this location, backtrack
    return False

def update_board_gui():
    for i in range(9):
        for j in range(9):
            cell_value = sudoku_entries[i][j].get()
            sudoku_board[i][j] = int(cell_value) if cell_value else 0

def solve_button_click():
    update_board_gui()
    if solve_sudoku(sudoku_board):
        messagebox.showinfo("Sudoku Solved", "Sudoku puzzle has been solved!")
        update_board_gui()
    else:
        messagebox.showinfo("No Solution", "No solution exists for the current puzzle.")

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")

# Initialize the Sudoku board with empty values
sudoku_board = [[0] * 9 for _ in range(9)]

# Create an entry grid for the Sudoku board
sudoku_entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=3, justify="center")
        entry.grid(row=i, column=j)
        row_entries.append(entry)
    sudoku_entries.append(row_entries)

# Create a Solve button
solve_button = tk.Button(root, text="Solve", command=solve_button_click)
solve_button.grid(row=9, column=4, pady=10)

# Run the GUI
root.mainloop()
