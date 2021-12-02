from SquaresDirectory import Square


class Purchasable(Square.Square):
    def __init__(self, SquareName, SquareNumber, Color, Cost, Values, Mortgage, alwaysActive=False):
        super().__init__(SquareName, SquareNumber, alwaysActive)
        self.isPurchased = False
        self.isMortgaged = False
        self.canBuildHouses = False
        self.HouseLevel = 0  # This Tells What Level Currently On
        self.PropertyValue = int(Cost)
        self.RentPerLevel = Values
        self.MortgageCost = int(Mortgage)
        self.Color = Color
        self.AIValue = int(Cost)  # This is Pointless, since every time it is accessed it has to be updated before returned and means many different things. Would probably be better as a local variable in the module it is modified from

    def isPurchasable(self):
        return not self.isPurchased

    def Purchase(self, Player):
        # Shared Tasks Between the Purchasable Child Classes
        Player.PropertiesOwned.append(self)
        self.isPurchased = True
        self.Owner = Player
        Player.Money -= self.PropertyValue
        Player.PropertiesOwnedNumbers[0] += 1

    def Mortgage(self):
        self.isMortgaged = True

    def PayMortgage(self):
        self.isMortgaged = False

    def OnSquare(self, Player):
        pass

    def rentOfProperty(self, basic=False) -> int:
        pass

    def CalculateValueOfProperty(self, ToPlayer=None):
        ToPlayer = self.Owner if ToPlayer is None else ToPlayer  # So That I can Check the value of a property to non owners
        OwnProperty = 0 if ToPlayer != self.Owner else 1
        self.AIValue = (self.PropertyValue * self.MortgageCost) ** (self.HouseLevel + 1)  # Initialize
        self.AIValue *= self.rentOfProperty(True) / ToPlayer.GameBoard.boardSize  # Multiple
        self.AIValue **= ToPlayer.OwnsSiblingProperty(self, Count=True) + OwnProperty  # Power
        self.AIValue *= 1.2 * ((self.PropertiesOwnedByCompetitor() + OwnProperty) / (len(ToPlayer.GameBoard.PropertiesMapped[self.Color])))  # Multiple
        return self.AIValue

    def BuyHouse(self, Player):
        return False

    def PropertiesOwnedByCompetitor(self, Player=None):
        Player = self.Owner if Player is None else Player  # will make input simpler but still give the complexity desired.
        number = 0
        for propriety in Player.GameBoard.PropertiesMapped[self.Color]:
            if propriety.Owner is not None or propriety.Owner != Player:
                number += 1
        return number

    def sellProperty(self, Seller, Buyer="Banker", Price=0):
        if self.canBuildHouses:
            for prop in Seller.GameBoard.PropertiesMapped[self.Color]:
                if prop.HouseLevel != 0:
                    return -1  # "Transaction Blocked as Development is still located on location or in surrounding territory"
        if Buyer == "Banker":
            # Seller.Money += self.
            pass
        else:
            pass

    def realValue(self):
        realVal = self.PropertyValue
        if self.isMortgaged:
            realVal -= self.MortgageCost * 0.5

        realVal += self.HouseLevel

    @staticmethod
    def CanUseHouses():
        return False


if __name__ == "__main__":
    N2 = Purchasable("hello", 1, "Blue", 100, [100], 100)
    print(N2.isPurchasable())
    print(N2.OnSquare(None))
