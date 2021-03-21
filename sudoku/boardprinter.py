from itertools import chain

from blessings import Terminal

term = Terminal()


def boardprinter(board: list, row=10, col=9, iter=0):
    """Print out pretty looking board

    Parameters:
        board (list): List containing Sudoku Board
        row (int): Row number for current iteration (Optional)
        col (int): Col number for current iteration (Optional)
        iter (int): Iteration running through to print progress (Optional)
    """

    # Find current location, and build string
    location = (row * 9) + col
    line = chain(*board)

    # Is this running visual, or is this final print?
    if row < 10:
        with term.location(0, term.height - 14):
            printing(line, location, iter)
    else:
        printing(line, location, iter)


def printing(line, location, iter):
    """Build the Blessings Print String

    Parameters:
        line (chain): Chain from sudoku list
        location (int): Location for current Iter
        iter (int): Current iter for status
    """

    # Set initial countters
    c_count, b_count, l_count = 0, 0, 0

    # Print status
    print(term.normal + "Iterations: " + term.red + str(iter))

    # Main Loop
    for y, x in enumerate(line):

        # If we are at end of line, new line and reset counters
        if b_count == 9:
            print()
            b_count = c_count = 0
            l_count += 1

        # Add horisontal seperator on row *3, reset counter
        if l_count == 3:
            print(term.normal + "------ ------- ------")
            l_count = 0

        # Add Vertical seperator on col *3, reset counter
        if c_count == 3:
            print(term.normal + "|", end=" ")
            c_count = 0

        # Decide on colors of numbers
        if y < location:
            print(term.green + str(x), end=" ")
        elif y == location:
            print(term.blue + str(x), end=" ")
        else:
            if x == 0:
                print(" ", end=" ")
            else:
                print(term.normal + str(x), end=" ")

        # Increment counters
        c_count += 1
        b_count += 1
