from SquaresDirectory.PurchasableClass import Purchasable


class Property(Purchasable):  # Mostly Abstract Class
    def __init__(self, SquareName, SquareNumber, Color, Cost, HousingCost, Values, Mortgage):
        super().__init__(SquareName, SquareNumber, Color, Cost, Values, Mortgage)
        self.HousingCost = HousingCost  # Doubles for Hotel Costs As Well

    def OnSquare(self, Player):
        if self.isPurchasable():
            if Player.Money >= self.PropertyValue:
                self.Purchase(Player)
            pass  # Some Random Odds that this square is purchased, else auctioned or something else like nothing
        else:
            pass  # Pays Money to Owner of Property.

    def Purchase(self, Player):
        super().Purchase(Player)

    def rentOfProperty(self, basic=False) -> int:
        return self.RentPerLevel[self.HouseLevel]

    def CalculateValueOfProperty(self, ToPlayer=None):
        return super().CalculateValueOfProperty(ToPlayer)

    @staticmethod
    def CanUseHouses():  # Why ... Dunno
        return True

    def BuyHouse(self, Player):
        if self.HouseLevel < 4:
            if Player.GameBoard.Bank.numHousesInBank > 0:
                return True  # Houses Available to Purchase
            else:
                return False  # Houses not Available to Purchase
        elif self.HouseLevel == 4:
            if Player.GameBoard.Bank.numHotelsInBank > 0:
                return True  # Hotels Available to Purchase
            else:
                return False  # Hotels not Available to Purchase
