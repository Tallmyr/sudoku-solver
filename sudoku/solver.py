from sudoku.boardprinter import boardprinter
from sudoku.check import check


def solver(board: list, vis: bool):
    """Solves a sudoku board using backtracking
    Parameters:
        board (list): Sudoku board to be solved
        vis (bool): Enable visual mode, where each iteration is printed

    Returns:
        board (list): Returns a solved board
        iter (int): Number of iterations required
    """
    # Define some needed vars
    solved, backtrack = False, False
    row, col, x, iter = 0, 0, 1, 0
    history = []

    # Main Loop
    while not solved:
        if board[row][col] == 0 or backtrack:  # Find next number to solve
            iter += 1

            # Loop through numbers 1-9, or from backtrack x
            for i in range(x, 10):
                valid = check(i, row, col, board)
                if valid is True:
                    board[row][col] = i
                    history.append([row, col, i])  # Add last location to stack
                    x = 1
                    backtrack = False
                    break

            # If nothing was found, backtrack one step on stack
            if valid is False:
                backtrack = True
                row, col, x = history[-1][0], history[-1][1], history[-1][2] + 1
                board[row][col] = 0
                history.pop()

        # if we are not backtracking, increment to next position
        if not backtrack:
            if row == 8 & col == 8:
                solved = True
            if col == 8:
                col = 0
                row += 1
            else:
                col += 1
        # Are we runing in visual mode?
        if vis:
            boardprinter(board, row, col, iter)
    return board, iter
