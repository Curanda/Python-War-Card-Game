from GameLoop import GameLoop
from Player import Player

class Main:
    def __init__(self):
        self.__name = "Main"

        player1 = Player("MMKK")
        player2 = Player("kkkMMMM")
        gameloop = GameLoop(player1, player2)
        gameloop.run()


if __name__ == "__main__":
    Main()


