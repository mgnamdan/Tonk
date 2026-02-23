# Imports
from cards import Card
from decks import Deck
from players import CmpPlayer, HmnPlayer


# Main Definition
def main():
    playerOne = CmpPlayer()
    playerTwo = HmnPlayer("Joe")

    print(playerOne.score)
    print("")
    print(playerOne.hand)
    print("")
    print("")
    print(playerTwo.score)
    print("")
    print(playerTwo.hand)
    print("")
    print("")




# Main Call
if __name__ == "__main__":
    main()