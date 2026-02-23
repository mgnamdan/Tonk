class Card:

    def __init__(self, rank="Two", suit="Clubs"):
        self.rank = rank
        self.suit = suit


    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    

    # def __eq__(self, other):
    #     if isinstance(other, Card):
    #         print(type(other))
    #         print("Catch 1")
    #         return False
    #     if self.rank != other.rank:
    #         print("Catch 2")
    #         return False
    #     if self.suit != other.suit:
    #         print("Catch 3")
    #         return False
    #     return True
    