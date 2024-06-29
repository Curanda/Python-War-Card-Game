class Player:
    name = ""
    currentDeck = []

    def __init__(self, name):
        self.name = name

    def getCurrentDeck(self):
        return self.currentDeck

    def setCurrentDeck(self, currentDeck):
        self.currentDeck = currentDeck

    def getName(self):
        return self.name

    def addToDeck(self, card):
        self.currentDeck.append(card)

    def removeFromDeck(self, card):
        self.currentDeck.remove(card)

    def extendDeck(self, cards):
        self.currentDeck.extend(cards)



