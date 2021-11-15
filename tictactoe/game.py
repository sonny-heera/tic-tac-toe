import abc
from typing import List
from tictactoe.board import Board
from tictactoe.player import Player


class Game(abc.ABC):
    """
    Tic-tac toe game.
    """

    def __init__(self, board: Board, players: List[Player]):
        self.board = board
        self.players = players

    @abc.abstractmethod
    def play(self):
        """
        Plays the game.
        """
        pass
