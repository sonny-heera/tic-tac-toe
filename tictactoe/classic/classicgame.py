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
    TOTAL_CELLS = ClassicBoard.DIMENSION * ClassicBoard.DIMENSION
    WIN_COORDS = [[Point(0, 0), Point(0, 1), Point(0, 2)], [Point(1, 0), Point(1, 1), Point(1, 2)],
                  [Point(2, 0), Point(2, 1), Point(2, 2)],
                  [Point(0, 0), Point(1, 0), Point(2, 0)], [Point(0, 1), Point(1, 1), Point(2, 1)],
                  [Point(0, 2), Point(1, 2), Point(2, 2)],
                  [Point(0, 0), Point(1, 1), Point(2, 2)], [Point(0, 2), Point(1, 1), Point(2, 0)]]

    def __init__(self, board: ClassicBoard, players: List[Player]):
        if len(players) > 2:
            raise ValueError("number of players should be 2")
        super().__init__(board, players)
        self.num_cells_used = 0

    def play(self):
        print("Starting new game")
        curr_player = self.players[0]
        while True:
            print(str(self.board) + "\n")
            self.execute_turn(curr_player)
            self.num_cells_used += 1

            if self.is_game_over(curr_player):
                print(str(self.board))
                break
            else:
                if curr_player is self.players[0]:
                    curr_player = self.players[1]
                else:
                    curr_player = self.players[0]

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
        if self.num_cells_used == ClassicGame.TOTAL_CELLS:
            print("game has ended in a tie")
            return True
        else:
            for coords in self.WIN_COORDS:
                if self.is_sequence_filled(player.symbol, coords):
                    print(f'Player {player.name} has won')
                    return True

        return False

    def is_sequence_filled(self, symbol: str, points: List[Point]) -> bool:
        for point in points:
            if self.board.get([point.row, point.col]) != symbol:
                return False

        return True


if __name__ == '__main__':
    player_1_name = str(input("Enter player 1 name: "))
    player_1 = Player(player_1_name, ClassicSymbol.O.value)

    player_2_name = str(input("Enter player 2 name: "))
    player_2 = Player(player_2_name, ClassicSymbol.X.value)

    game = ClassicGame(ClassicBoard(), [player_1, player_2])

    game.play()
