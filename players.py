class CmpPlayer:
    
    def __init__(self, name="Bob"):
        self.name = name
        self.playerSetup()


    def playerSetup(self):
        self.score = 0
        self.hand = []


    def __repr__(self):
        return f"{self.name}"
    

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        if self.name != other.name:
            return False
        if self.score != other.score:
            return False
        if len(self.hand) != len(other.hand):
            return False
        for idx in range(len(self.hand)):
            if self.hand[idx] != other.hand[idx]:
                return False
        return True



class HmnPlayer(CmpPlayer):
    
    def __init__(self, name):
        super().__init__(name)