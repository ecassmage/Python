from SquaresDirectory.NonPurchasableClass import NonPurchasable


class Go(NonPurchasable):
    def __init__(self, SquareName, SquareNumber, Value):
        super().__init__(SquareName, SquareNumber, alwaysActive=True)
        self.Receive = Value

    def OnSquare(self, Player):
        Player.Money += self.Receive
