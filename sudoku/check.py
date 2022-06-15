def check(i, r, c, board):
    # sourcery skip: invert-any-all, use-any, use-itertools-product
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
