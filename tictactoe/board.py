import abc
from typing import List


class Board(abc.ABC):
    """
    Board in a tic-tac toe game.
    """

    @abc.abstractmethod
    def get(self, position: List[int]) -> str:
        """
        Returns the symbol at the position on the board.

        :param position: list of integers representing the position
        :return: symbol at the provided position
        """
        pass

    @abc.abstractmethod
    def set(self, position: List[int], symbol: str):
        """
        Sets the position on the board to the provided symbol.

        :param position: list of integers representing the position
        :param symbol: string representing the symbol to set
        """
        pass
