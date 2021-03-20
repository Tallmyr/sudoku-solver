board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

def check(i, r, c, board):
    # Check Row
    for col in range(9):
        if board[r][col] == i:
            return False

        # Check Col
        for row in range(9):
            if board[row][c] == i:
                return False

    return True


def solver(board):
    solved = False
    history = []
    row = 0
    col = 0
    x = 1
    backtrack = False
    while not solved:
        if board[row][col] == 0 or backtrack:
            for i in range(x, 10):
                valid = check(i, row, col, board)
                if valid == True:
                    board[row][col] = i
                    history.append([row, col, i])
                    x = 1
                    backtrack = False
                    break
            if valid == False:
                backtrack = True
                row = history[-1][0]
                col = history[-1][1]
                x = history[-1][2] + 1
                board[row][col] = 0
                history.pop()
        if not backtrack:
            if row == 8 & col == 8:
                solved = True
            if col == 8:
                col = 0
                row += 1
            else:
                col += 1
    return board


print(solver(board))
