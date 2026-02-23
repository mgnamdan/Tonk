# Imports
from cards import Card
from decks import Deck


# Main Definition
def main():
    testDeck = Deck()

    drawnCard = testDeck.drawCard()
    print(testDeck.outPile)
    print("")
    print(testDeck.discardPile)
    print("")
    testDeck.discardCard(drawnCard)
    print(testDeck.outPile)
    print("")
    print(testDeck.discardPile)

    testDeck.resetDeck()
    print(testDeck.outPile)
    print("")
    print(testDeck.discardPile)




# Main Call
if __name__ == "__main__":
    main()