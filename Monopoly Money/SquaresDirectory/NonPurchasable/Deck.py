from SquaresDirectory.NonPurchasableClass import NonPurchasable


class Deck(NonPurchasable):
    def __init__(self, SquareName, SquareNumber, DeckOfCards):
        super().__init__(SquareName, SquareNumber)
        self.DeckOfCards = DeckOfCards

    def OnSquare(self, Player):
        pass
        # I will want this to pick a card from this Deck of Cards, either through a stack or randomly
