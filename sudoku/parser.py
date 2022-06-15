import pathlib
import re


def parser(file: str):
    """Parser to take .txt file and turn into Sudoku list.
    Parameters:
        file (str): Path to .txt file

    Returns:
        (list): Nested list containing Sudoku


    Input Sample:

        Input needs to be text file containing 81 numbers in order. Everything except numbers will be stripped out.

        9 0 7 5 0 1 8 2 0
        0 3 5 0 2 0 0 1 0
        0 1 8 0 0 6 0 0 3
        0 0 0 0 0 0 2 0 9
        0 9 0 6 5 2 0 0 1
        1 0 2 0 4 9 5 0 0
        3 8 6 4 0 0 0 0 0
        7 5 0 2 1 0 6 0 0
        4 0 0 0 0 0 0 8 0

    """
    text = pathlib.Path(file).read_text()
    text = re.sub("\D", "", text) # noqa W605
    numbers = list(map(int, text))
    if len(numbers) != 81:
        raise ValueError(f"Incorrect input format for textfile {file}")
    return [numbers[i : i + 9] for i in range(0, len(numbers), 9)]
