from SquaresDirectory.NonPurchasableClass import NonPurchasable


class FreeParking(NonPurchasable):
    def __init__(self, SquareName, SquareNumber):
        super().__init__(SquareName, SquareNumber)
        self.Pot = 0

    def OnSquare(self, Player):
        Player.Money += self.Pot
        self.Pot = 0