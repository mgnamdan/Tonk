from cards import Card
from random import shuffle

class Deck:

    RANKS = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Clubs', 'Hearts', 'Spades', 'Diamonds']

    def __init__(self):
        self.resetDeck()


    def resetDeck(self):
        self.drawPile = []
        self.discardPile = []
        self.outPile = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                newCard = Card(rank, suit)
                self.drawPile.append(newCard)


    def __repr__(self):
        return "\n".join(str(card) for card in self.drawPile)
    

    def __eq__(self, other):
        if not isinstance(other, Deck):
            return False
        meCheck = self.drawPile + self.discardPile + self.outPile
        youCheck = other.drawPile + other.discardPile + other.outPile
        if len(meCheck) != len(youCheck):
            return False
        for idx in range(len(meCheck)):
            if meCheck[idx] != youCheck[idx]:
                return False
        return True
    

    def randShuffle(self):
        shuffle(self.drawPile)


    def parShuffle(self):
        midIdx = len(self.drawPile) // 2
        firstHalf = self.drawPile[:midIdx]
        secondHalf = self.drawPile[midIdx:]
        self.drawPile = []
        for idx in range(len(firstHalf)):
            self.drawPile.append(firstHalf[idx])
            self.drawPile.append(secondHalf[idx])


    def drawCard(self):
        self.outPile.append(self.drawPile.pop(0))
        return self.outPile[0]
    

    def discardCard(self, card):
        if card in self.outPile:
            self.outPile.remove(card)
            self.discardPile.append(card)
