from CardDirectory import CardClasses
from SquaresDirectory import PurchasableClass
from SquaresDirectory.NonPurchasable import Deck, FreeParking, Go, Jail, Tax
from SquaresDirectory.Purchasable import Property, Railroad, Utility
import Bank


class Board:
    def __init__(self, CommunityChestName="Community Chest", ChanceName="Chance Name"):  # The Names Can Be Changed if Wanted
        self.Go = None
        self.CommunityChest = CardClasses.CardsSquare(CommunityChestName)
        self.Chance = CardClasses.CardsSquare(ChanceName)
        self.JailSquare = None
        self.FreeParking = None
        self.Bank = Bank.Bank()
        self.PropertiesMapped = {}
        self.boardSize = 0

        self.PlayerGroup = []

    def __splitPropertiesSpecial(self, lineSpecial):  # Private, No Lookie
        lineSpecial = lineSpecial.replace("None ", "")
        StringName = lineSpecial[lineSpecial.find("<") + 1:lineSpecial.find(">")]

        if StringName == "Community Chest":
            return Deck.Deck("Community Chest", lineSpecial[0: lineSpecial.find(" ")], self.CommunityChest)

        elif StringName == "Chance":
            return Deck.Deck("Chance", lineSpecial[0: lineSpecial.find(" ")], self.Chance)

        elif StringName == "RailRoad":
            lineSpecial = lineSpecial.replace("<RailRoad> ", "")
            LineRailRoad = open("PropertyTxt/RailRoad.txt", "r").readline().split(" ", 1)
            return Railroad.Railroad(lineSpecial[lineSpecial.find("<") + 1:lineSpecial.find(">")], lineSpecial[0:lineSpecial.find(" ")], int(LineRailRoad[0]), [int(i) for i in LineRailRoad[1].rsplit(" ")])

        elif StringName == "Utility":
            lineSpecial = lineSpecial.replace("<Utility> ", "")
            UtilityLine = open("PropertyTxt/Utility.txt", "r").readline().split(" ", 1)
            return Utility.Utility(lineSpecial[lineSpecial.find("<") + 1:lineSpecial.find(">")], lineSpecial[0:lineSpecial.find(" ")], int(UtilityLine[0]), [int(i) for i in UtilityLine[1].rsplit(" ")])

        elif StringName == "Luxury Tax":
            return Tax.Tax("Luxury Tax", lineSpecial[0: lineSpecial.find(" ")], lineSpecial[lineSpecial.rfind(" "):len(lineSpecial)])

        elif StringName == "Income Tax":
            return Tax.Tax("Income Tax", lineSpecial[0: lineSpecial.find(" ")], lineSpecial[lineSpecial.rfind(" "):len(lineSpecial)])

        elif StringName == "Go To Jail":
            lineSpecial = lineSpecial.replace("<Go To Jail> ", "", 1)
            return Jail.GoToJail(lineSpecial[lineSpecial.find("<") + 1:lineSpecial.find(">")], lineSpecial[0: lineSpecial.find(" ")])

        elif StringName == "Jail":
            lineSpecial = lineSpecial.replace("<Jail> ", "", 1)
            self.JailSquare = Jail.Jail(lineSpecial[lineSpecial.find("<") + 1:lineSpecial.find(">")], lineSpecial[0: lineSpecial.find(" ")])
            return self.JailSquare

        elif StringName == "Free":
            lineSpecial = lineSpecial.replace("<Free> ", "")
            self.FreeParking = FreeParking.FreeParking(lineSpecial[lineSpecial.find("<") + 1:lineSpecial.find(">")], lineSpecial[0: lineSpecial.find(" ")])
            return self.FreeParking

        print(f"ERROR: {lineSpecial}")
        return None

    def __addToMap(self, Key, Value):
        if Key in self.PropertiesMapped:
            self.PropertiesMapped[Key].append(Value)
        else:
            self.PropertiesMapped.update({Key: [Value]})

    def splitProperties(self):
        self.Go = Go.Go("Go", 0, 200)  # can double if landed on it
        tempLink = self.Go
        for line in open("PropertyTxt/Properties.txt", "r").readlines():
            lineSplit = line.replace("\n", "")
            if lineSplit[0:4] == "None":
                tempLink = self.setNextPrev(tempLink, self.__splitPropertiesSpecial(lineSplit))
            else:
                if lineSplit == "":
                    break
                name = lineSplit[lineSplit.find("<")+1:lineSplit.find(">")]
                lineSplit = lineSplit.replace("%s " % lineSplit[lineSplit.find("<"):lineSplit.find(">")+1], "")
                listOfStuff = lineSplit.split(" ")
                tempLink = self.setNextPrev(tempLink, Property.Property(name, listOfStuff[1], listOfStuff[0], listOfStuff[2], listOfStuff[3], [int(listOfStuff[i]) for i in range(4, len(listOfStuff) - 1)], listOfStuff[-1]))
            if isinstance(tempLink, PurchasableClass.Purchasable):
                self.__addToMap(tempLink.Color, tempLink)
            self.boardSize += 1  # Cause I don't believe I can actually measure a txt file number of lines another way.

        Board.setNextPrev(tempLink, self.Go)

    def initiateAuction(self, Property):
        pass

    @staticmethod
    def setNextPrev(self, newValNext):
        self.next = newValNext
        self.next.prev = self
        return self.next


if __name__ == "__main__":
    B = Board()
    B.splitProperties()
    pass
