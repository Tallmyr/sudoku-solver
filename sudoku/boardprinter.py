from itertools import chain

from blessings import Terminal

term = Terminal()

def boardprinter(board, row, col, iter):
    location = (row * 9) + col
    line = chain(*board)
    count, count2, countl = 0, 0, 0
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
