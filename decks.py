from cards import Card

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