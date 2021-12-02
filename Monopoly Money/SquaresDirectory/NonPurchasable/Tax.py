from SquaresDirectory.NonPurchasableClass import NonPurchasable


class Tax(NonPurchasable):
    def __init__(self, SquareName, SquareNumber, Cost):
        super().__init__(SquareName, SquareNumber)
        self.Cost = int(Cost)

    def OnSquare(self, Player):
        Player.Money -= self.Cost
        Player.GameBoard.FreeParking.Pot += self.Cost
