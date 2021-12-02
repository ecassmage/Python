class Square:
    # Linked List Sort of System
    def __init__(self, SquareName, SquareNumber, alwaysActive):
        self.Name = str(SquareName)  # To Make Sure this is String
        self.Number = int(SquareNumber)  # To Make Sure this is integer
        self.Owner = None  # this Should be a Player
        self.next = None  # Next Square
        self.prev = None  # Previous Square, More for ease of working with stuff
        self.alwaysActive = alwaysActive

    def Bought(self, newOwner):     self.Owner = newOwner

    def setNext(self, SquareNext):  self.next = SquareNext

    def setPrev(self, SquarePrev):  self.prev = SquarePrev

    def isPurchasable(self):  # Acts Like an Abstract Method
        pass

    def OnSquare(self, Player):
        pass


if __name__ == "__main__":
    pass
