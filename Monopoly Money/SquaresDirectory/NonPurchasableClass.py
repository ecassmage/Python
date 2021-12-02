from SquaresDirectory import Square


class NonPurchasable(Square.Square):
    def __init__(self, SquareName, SquareNumber, alwaysActive=False):
        super().__init__(SquareName, SquareNumber, alwaysActive)
        self.Owner = "Bank"

    def isPurchasable(self):
        return False

    def OnSquare(self, Player):
        pass


if __name__ == "__main__":
    N = NonPurchasable("hello", 1)
    print(N.isPurchasable())
    print(N.OnSquare(None))
