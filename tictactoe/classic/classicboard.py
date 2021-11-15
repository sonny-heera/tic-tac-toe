from enum import Enum
from typing import List
from tictactoe.board import Board


class ClassicSymbol(Enum):
    """
    Valid symbols for a classic tic-tac toe game.
    """
    X = "X"
    O = "O"


class ClassicBoard(Board):
    """
    Classic 3x3 tic-tac toe board.
    """

    DIMENSION = 3

    def __init__(self):
        self.grid: List[List[str]] = [[None for i in range(ClassicBoard.DIMENSION)] for j in
                                     range(ClassicBoard.DIMENSION)]

    def get(self, position: List[int]) -> str:
        self.validate_position(position)

        return self.grid[position[0]][position[1]]

    def set(self, position: List[int], symbol: str):
        row = position[0]
        col = position[1]
        self.validate_position(position)

        if self.grid[row][col] is None:
            if symbol is not ClassicSymbol.X.value and symbol is not ClassicSymbol.O.value:
                raise ValueError("invalid symbol, must be X or O")
            else:
                self.grid[row][col] = symbol
        else:
            raise ValueError(f'position [{row}, {col}] is already occupied')

    def validate_position(self, position):
        if len(position) != 2:
            raise ValueError("position must be an integer list of size 2")

        row = position[0]
        col = position[1]

        if row > ClassicBoard.DIMENSION - 1 or row < 0:
            raise ValueError("row out of bounds")

        if col > ClassicBoard.DIMENSION - 1 or col < 0:
            raise ValueError("column out of bounds")

    def __str__(self):
        grid = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                symbol = self.grid[i][j]
                if symbol is None:
                    grid += " - "
                else:
                    grid += f' {symbol} '
            grid += "\n"
        return grid
