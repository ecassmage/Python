from SquaresDirectory.PurchasableClass import Purchasable


class Utility(Purchasable):
    def __init__(self, SquareName, SquareNumber, Cost, RentNumbers):
        super().__init__(SquareName, SquareNumber, "Utility", Cost, RentNumbers[0:len(RentNumbers) - 1], RentNumbers[len(RentNumbers)-1])

    def OnSquare(self, Player):
        if self.isPurchasable():
            if Player.Money >= self.PropertyValue:
                self.Purchase(Player)
            else:
                pass
        else:
            pass  # Pays Money to Owner of Property.

    def Purchase(self, Player):
        super().Purchase(Player)
        Player.PropertiesOwnedNumbers[2] += 1

    def rentOfProperty(self, basic=False) -> int:
        num = 0
        for Prop in self.Owner.PropertiesOwned:
            if Prop.Color == "Utility" and not Prop.isMortgaged and Prop != self:
                num += 1
        if basic:
            return 7 * self.RentPerLevel[num]
        return self.Owner.RollDice(2) * self.RentPerLevel[num]  # Should Capture The Correct Owed

    def CalculateValueOfProperty(self, ToPlayer=None):
        super().CalculateValueOfProperty(ToPlayer)
        self.AIValue *= (1 + self.Owner.OwnsSiblingProperty(self, Count=True))
        return self.AIValue
