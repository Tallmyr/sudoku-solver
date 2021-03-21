from sudoku.parser import parser
from sudoku.solver import solver

if __name__ == "__main__":
    
    print(solver(parser("samples/s15c.txt"), True))
