from SquaresDirectory.NonPurchasableClass import NonPurchasable


class GoToJail(NonPurchasable):
    def __init__(self, SquareName, SquareNumber):
        super().__init__(SquareName, SquareNumber)

    def OnSquare(self, Player):
        Player.isInJail = True
        Player.PositionOnBoard = Player.GameBoard.Go


class Jail(NonPurchasable):
    def __init__(self, SquareName, SquareNumber):
        super().__init__(SquareName, SquareNumber)

    def OnSquare(self, Player):
        pass
