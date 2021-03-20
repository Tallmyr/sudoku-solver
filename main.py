from itertools import chain
from time import sleep

from blessings import Terminal

board = [
    [0, 7, 1, 6, 8, 4, 0, 0, 0],
    [0, 4, 9, 7, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 5, 0, 4],
    [0, 0, 0, 3, 0, 7, 0, 0, 0],
    [2, 0, 3, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 3, 7, 2, 0],
    [0, 0, 0, 4, 9, 8, 6, 1, 0],
]
term = Terminal()


def boardprinter(board, row, col, iter):
    location = (row * 9) + col
    line = chain(*board)
    count = 0
    count2 = 0
    countl = 0
    with term.location(0, term.height - 14):
        print(term.normal + "Iterations: " + term.red + str(iter))
        for y, x in enumerate(line):
            if count2 == 9:
                print()
                count2 = 0
                count = 0
                countl += 1
            if countl == 3:
                print(term.normal + "------ ------- ------")
                countl = 0
            if count == 3:
                print(term.normal + "|", end=" ")
                count = 0
            if y < location:
                print(term.green + str(x), end=" ")
            elif y == location:
                print(term.blue + str(x), end=" ")
            else:
                if x == 0:
                    print(term.red + " ", end=" ")
                else:
                    print(term.normal + str(x), end=" ")
            count += 1
            count2 += 1


def check(i, r, c, board):
    # Check Row
    for col in range(9):
        if board[r][col] == i:
            return False

    # Check Col
    for row in range(9):
        if board[row][c] == i:
            return False

    # Check Boxes
    boxw = r - r % 3
    boxh = c - c % 3

    for w in range(boxw, boxw + 3):
        for h in range(boxh, boxh + 3):
            if board[w][h] == i:
                return False

    return True


def solver(board):
    solved = False
    row = 0
    col = 0
    x = 1
    backtrack = False
    history = []
    iter = 0
    while not solved:
        if board[row][col] == 0 or backtrack:
            iter += 1
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
        boardprinter(board, row, col, iter)
    return board


print(solver(board))
