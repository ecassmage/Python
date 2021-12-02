from SquaresDirectory.NonPurchasable.Deck import Deck


class CardsSquare:
    def __init__(self, SquareName):
        self.Name = SquareName
        self.Cards = []

    def addSquare(self, SquareNumber):
        pass

    def addCards(self):
        # self.Cards.append("Added")
        pass


class Card:
    def __init__(self, Description, WhatEverThisWillBe):
        self.Description = Description
        self.WhatEverThisWillBe = WhatEverThisWillBe


if __name__ == "__main__":
    N2 = CardsSquare("hello")
    N = Deck(N2, "hello", 1)
    N2.addCards()
    print(N.DeckOfCards.Cards)
    print(N2.Cards)
    N2.addCards()
    print(N.DeckOfCards.Cards)
    print(N2.Cards)
