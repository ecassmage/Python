import random
import Board


class Player:
    def __init__(self, GameBoard, StartingMoney, specialRules=False):
        self.GameBoard = GameBoard
        self.Money = StartingMoney
        self.PropertiesOwned = []
        self.PositionOnBoard = GameBoard.Go
        self.NumOfGetOutOfJailFreeCards = 0
        self.isInJail = [False, 0]
        self.PropertiesOwnedNumbers = [0, 0, 0]  # Properties, RailRoads, Utilities
        self.Mortgages = []
        self.__specialRules = specialRules

    def PlayTurn(self):
        if self.isInJail[0]:
            if self.isInJail[1] > 3:
                self.isInJail = [False, 0]
            if self.NumOfGetOutOfJailFreeCards > 0:
                self.NumOfGetOutOfJailFreeCards -= 1
                self.isInJail = [False, 0]
            elif self.RollDice(1) == self.RollDice(1):
                self.isInJail = [False, 0]
            else:
                self.isInJail[1] += 1
                return
        num = self.RollDice(2)
        self.Move(num)
        if self.Money < 0:
            self.deptRepayment()
        return num

    def Move(self, Number):
        for i in range(Number):
            self.PositionOnBoard = self.PositionOnBoard.next
            if self.PositionOnBoard.alwaysActive:
                self.PositionOnBoard.OnSquare(self)
        self.PositionOnBoard.OnSquare(self)  # Not Done Yet For All

    def deptRepayment(self):
        pass

    def SpecialRules(self):
        return self.__specialRules

    def OwnsSiblingProperty(self, Property, Count=False):
        num = 0
        for PropertyOwned in self.GameBoard.PropertiesMapped[Property.Color]:
            if PropertyOwned.Owner == self and PropertyOwned is not Property:
                if Count:
                    num += 1
                else:
                    return True
        return num if Count else False

    @staticmethod
    def RollDice(NumOfDice, Sides=6):
        num = 0
        for i in range(NumOfDice):
            num += random.randrange(1, Sides+1)
        return num


if __name__ == '__main__':
    B = Board.Board()
    B.splitProperties()
    P = Player(B, 500)
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    P.PlayTurn()
    pass
