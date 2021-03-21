import argparse

from sudoku.boardprinter import boardprinter
from sudoku.parser import parser
from sudoku.solver import solver

if __name__ == "__main__":

    args = argparse.ArgumentParser(description="Commandline Sudoku Solver")
    args.add_argument("file", help="Textfile containing sudoku data")
    args.add_argument("-v", "-visual",  help="Visual solver", action="store_true", default=False)
    args = args.parse_args()

    solved, iter = solver(parser(args.file), args.v)
    boardprinter(solved, iter=iter)
