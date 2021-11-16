from tictactoe.classic.classicboard import ClassicSymbol, ClassicBoard
from tictactoe.classic.classicgame import ClassicGame
from tictactoe.player import Player

"""
Classic game runner.
"""


def main():
    p1_name = str(input("Enter player 1 name: "))
    p1 = Player(p1_name, ClassicSymbol.O.value)

    p2_name = str(input("Enter player 2 name: "))
    p2 = Player(p2_name, ClassicSymbol.X.value)

    game = ClassicGame(ClassicBoard(), [p1, p2])
    game.play()


if __name__ == '__main__':
    main()
