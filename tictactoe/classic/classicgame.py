from typing import List

from tictactoe.game import Game
from tictactoe.classic.classicboard import ClassicBoard, ClassicSymbol
from tictactoe.player import Player


class Point:
    """
    2-dimensional Cartesian coordinates.
    """

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


class ClassicGame(Game):
    """
    Classic tic-tac toe game with 2 players and a 3x3 grid.
    """
    MAX_TURNS = ClassicBoard.DIMENSION * ClassicBoard.DIMENSION
    VICTORY_COORDINATES = [[Point(0, 0), Point(0, 1), Point(0, 2)],  # horizontal
                           [Point(1, 0), Point(1, 1), Point(1, 2)],
                           [Point(2, 0), Point(2, 1), Point(2, 2)],
                           [Point(0, 0), Point(1, 0), Point(2, 0)],  # vertical
                           [Point(0, 1), Point(1, 1), Point(2, 1)],
                           [Point(0, 2), Point(1, 2), Point(2, 2)],
                           [Point(0, 0), Point(1, 1), Point(2, 2)],  # diagonal
                           [Point(0, 2), Point(1, 1), Point(2, 0)]]

    def __init__(self, board: ClassicBoard, players: List[Player]):
        if len(players) > 2:
            raise ValueError("number of players should be 2")
        super().__init__(board, players)

    def play(self):
        print("Starting new game")
        curr_player = self.players[0]
        turn = 0
        while turn < ClassicGame.MAX_TURNS:
            print(str(self.board) + "\n")
            self.execute_turn(curr_player)
            turn += 1

            if self.is_game_over(curr_player):
                print(str(self.board))
                break
            else:
                if curr_player is self.players[0]:
                    curr_player = self.players[1]
                else:
                    curr_player = self.players[0]

        if turn == ClassicGame.MAX_TURNS:
            print(str(self.board) + "\n")
            print("game has ended in a tie")

    def execute_turn(self, player: Player):
        try:
            print(f'It is {player.name}\'s turn')
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            self.board.set([row, col], player.symbol)
        except ValueError as e:
            print("Erroneous value provided: " + str(e))
            self.execute_turn(player)

    def is_game_over(self, player: Player) -> bool:
        for coordinates in self.VICTORY_COORDINATES:
            if self.is_sequence_filled(player.symbol, coordinates):
                print(f'Player {player.name} has won')
                return True

        return False

    def is_sequence_filled(self, symbol: str, points: List[Point]) -> bool:
        for point in points:
            if self.board.get([point.row, point.col]) != symbol:
                return False

        return True
