from SquaresDirectory.PurchasableClass import Purchasable


class Railroad(Purchasable):
    def __init__(self, SquareName, SquareNumber, Cost, RentNumbers):
        super().__init__(SquareName, SquareNumber, "RailRoad", Cost, RentNumbers[0:len(RentNumbers) - 1], RentNumbers[len(RentNumbers) - 1])

    def OnSquare(self, Player):
        if self.isPurchasable():
            if Player.Money >= self.PropertyValue:
                self.Purchase(Player)
            pass  # Some Random Odds that this square is purchased, else auctioned or something else like nothing
        else:
            pass  # Pays Money to Owner of Property.

    def Purchase(self, Player):
        super().Purchase(Player)
        Player.PropertiesOwnedNumbers[1] += 1

    def rentOfProperty(self, basic=False) -> int:
        num = 0
        for Prop in self.Owner.PropertiesOwned:
            if Prop.Color == self.Color and not Prop.isMortgaged and Prop != self:
                num += 1
        return self.RentPerLevel[num]  # Should Capture The Correct Owed

    def CalculateValueOfProperty(self, ToPlayer=None):
        super().CalculateValueOfProperty(ToPlayer)
        self.AIValue *= (1 + self.Owner.OwnsSiblingProperty(self, Count=True))
        return self.AIValue
