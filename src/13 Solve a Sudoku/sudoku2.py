def is_valid(board, row, col, num):
  """Checks if a number can be placed in a cell without violating Sudoku rules."""
  # Check row and column
  for i in range(9):
    if board[row][i] == num or board[i][col] == num:
      return False
  # Check 3x3 subgrid
  start_row = row - row % 3
  start_col = col - col % 3
  for i in range(3):
    for j in range(3):
      if board[start_row + i][start_col + j] == num:
        return False
  return True

def solve_sudoku(board):
  """Solves a Sudoku puzzle using backtracking."""
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        for num in range(1, 10):
          if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
              return True
            board[row][col] = 0  # Backtrack
        return False
  return True

def print_sudoku(board):
  """Prints a Sudoku puzzle in a grid format."""
  for i in range(9):
    for j in range(9):
      if j % 3 == 0 and j > 0:
        print("|", end=" ")
      print(board[i][j], end=" ")
    print()
    if (i + 1) % 3 == 0 and i < 8:
      print("-" * 27)


# Example usage
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if solve_sudoku(puzzle):
  print_sudoku(puzzle)
else:
  print("No solution found")