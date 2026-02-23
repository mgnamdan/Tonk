# Imports
from decks import Deck


# Main Definition
def main():
    testDeck = Deck()

    print(testDeck.drawPile)
    testDeck.resetDeck()
    print("\n\n")
    print(testDeck.drawPile)
    testDeck.resetDeck()
    print("\n\n")
    print(testDeck.drawPile)


# Main Call
if __name__ == "__main__":
    main()