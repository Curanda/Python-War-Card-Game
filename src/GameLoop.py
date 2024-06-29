import random


class GameLoop:
    score = 0
    player1 = None
    player2 = None
    deck = {
        "heart": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "diamond": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "club": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "spade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    }
    stake = []

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def assignDeck(self):
        newDeck = []
        for suit, array in self.deck.items():
            for i in array:
                newDeck.append([suit, i])
        random.shuffle(newDeck)
        print("Shuffled deck: ", newDeck)
        print(self.player1.getName(), " has a following deck: ", newDeck[::2])
        print(self.player2.getName(), " has a following deck: ", newDeck[1::2])
        self.player1.setCurrentDeck(newDeck[::2])
        self.player2.setCurrentDeck(newDeck[1::2])

    def compare(self):
        one = self.player1.getCurrentDeck()[0][1]
        two = self.player2.getCurrentDeck()[0][1]
        print(self.player1.getCurrentDeck()[0], " versus ", self.player2.getCurrentDeck()[0])
        if one > two:
            print(self.player1.getName(), " takes ", self.player2.getCurrentDeck()[0])
            self.player1.addToDeck(self.player2.getCurrentDeck()[0])
            self.player2.removeFromDeck(self.player2.getCurrentDeck()[0])
            if len(self.stake) != 0:
                self.player1.extendDeck(self.stake)
                print(self.player1.getName(), " wins the war and takes", self.stake)
                self.stake = []
        elif one == two:
            self.stake.append(self.player1.getCurrentDeck()[0])
            self.stake.append(self.player2.getCurrentDeck()[0])
            self.player2.removeFromDeck(self.player2.getCurrentDeck()[0])
            self.player1.removeFromDeck(self.player1.getCurrentDeck()[0])
            print("war")
            self.compare()
        else:
            print(self.player2.getName(), " takes ", self.player1.getCurrentDeck()[0])
            self.player2.addToDeck(self.player1.getCurrentDeck()[0])
            self.player1.removeFromDeck(self.player1.getCurrentDeck()[0])
            if len(self.stake) != 0:
                self.player2.extendDeck(self.stake)
                print(self.player2.getName(), " wins the war and takes", self.stake)
                self.stake = []


    def run(self):
        self.assignDeck()
        while True:
            if len(self.player2.getCurrentDeck()) == 0:
                print(self.player1.getName(), " won this game taking those cards home: ", self.player1.getCurrentDeck())
                self.stake = []
                break
            if len(self.player1.getCurrentDeck()) == 0:
                print(self.player2.getName(), " won this game taking those cards home: ", self.player2.getCurrentDeck())
                self.stake = []
                break
            self.compare()


