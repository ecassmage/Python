from Settings import JOpen
import Player as Play
import Board
from AIPackage import Trading


class AI:
    def __init__(self):
        self.info = JOpen.AIOpen()
        self.TradingAI = Trading

    # To Buy A House
    def buyHouse(self, Player, Property):
        # this Should check if Player has enough to buy, the rules allow this player to buy, and that this property isn't Banned.
        if self.__CanPlayerBuy(Player, Property) and self.__AlwaysBuy(Player) and not self.__isPropertyOnList(Property):
            number = Player.RollDice(1, 100)  # Why not use random library here, well because I don't want to.
            if Player.OwnsSiblingProperty(Property):
                number += self.info["Chance Rules"]["Chain Purchasing %"]
            if number >= self.info["Chance Rules"]["Buy House %"]:
                Player.Purchase(Property)
        else:
            return False

    def __CanPlayerBuy(self, Player, Property):
        return Player.Money - self.__Savings(Player) >= Property.PropertyValue

    def __Savings(self, Player):
        return self.info["Players Beholden to Rules"]["Cash Minimum"] if Player.SpecialRules() else 0

    def __AlwaysBuy(self, Player):
        return Player.SpecialRules() == self.info["Players Beholden to Rules"]["Always Buy"] or not Player.SpecialRules()

    def __isPropertyOnList(self, Property):
        for propertyName in self.info["List AI Can not Purchase"]:
            if propertyName.Color == Property.Color:
                return True
        return False

    # Paying Rent
    def PayRent(self, Player, Property):
        if Property.rentOfProperty() > Player.Money:
            Property.Owner.Money += Player.Money
            Player.Money -= Property.rentOfProperty()
            ExtraMoney = self.__valueForDebt(Player, Property.rentOfProperty() - Player.Money)
            Property.Owner.Money += ExtraMoney[1]
            if ExtraMoney[0] < 0:
                for element in ExtraMoney[2]:  # ExtraMoney[2] is passed so that the Process will not have to sort these again.
                    Property.sellProperty(Player, Property.Owner)
                    pass
            else:
                Player.Money = ExtraMoney[0]
        else:
            Property.Owner.Money += Property.rentOfProperty()
            Player.Money -= Property.rentOfProperty()

    @staticmethod
    def __valueForDebt(Player, Debt):
        """ Calculates a relatively logical mortgaging and sell off to get back in the green
        :param Player: Desires a Player Object
        :param Debt: Desires the Amount of money needed.
        :return: if -1 then Bankrupt else this is the number of extra cash the player now has.
        """
        List = []
        Collected = 0
        for Property in Player.PropertiesOwned:
            if not Property.isMortgaged:
                List.append(Property)
        List.sort(key=CalculateValueOfProperty)
        for index in range(len(List)):
            if List[index].CanUseHouses():
                while List[index].HouseLevel > 0 and Debt - Collected > 0:
                    Collected += int(List[index].HousingCost / 2)  # Resale House Price Half Original Price
                    List[index].HouseLevel -= 1
            if Debt - Collected > 0:  # any Mortgaged properties would have been removed before getting here.
                Collected += List[index].MortgageCost
                List[index].Mortgage()
            if Debt - Collected <= 0:
                return [Collected - Debt, Debt]  # The Debt has been repayed.  [Money Mortgager Receives, Money Renter Receives]
        else:
            return Collected - Debt, Debt - (Debt - Collected), List  # We will Proceed to Selling Properties [Money Still Owed, Money Renter Receives, List Already Indexed]
        # Returns Profit From Selling and Mortgaging
        pass

    def publicValueDebt(self, Player, Debt):
        """ PRIVATE METHOD HERE GET RID OF THIS ACCESSOR """
        return self.__valueForDebt(Player, Debt)


def CalculateValueOfProperty(Property):
    return Property.CalculateValueOfProperty()


def externalAccess():
    AIObject = AI()
    B = Board.Board()
    B2 = Board.Board()
    B.splitProperties()
    B2.splitProperties()
    P = Play.Player(B, 200)
    PBuyer = Play.Player(B, 500)
    P2 = Play.Player(B2, 200)
    ptr = B.Go
    ptr2 = B2.Go
    for i in range(40):
        if ptr.isPurchasable():
            ptr.Purchase(P)
            ptr2.Purchase(P2)
        ptr = ptr.next
        ptr2 = ptr2.next
    Num = AIObject.publicValueDebt(P, 100000)  # Get rid of this method, Just for testing.
    Num2 = AIObject.publicValueDebt(P2, 5)  # Get rid of this method, Just for testing.
    AIObject.TradingAI.InitiateTrade(P, P.PropertiesOwned[0], PBuyer)
    AIObject.TradingAI.InitiateTrade(P, P.PropertiesOwned[1], PBuyer)
    pass


if __name__ == "__main__":
    externalAccess()
