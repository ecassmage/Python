def InitiateTrade(Seller, Property, Buyer):
    """
    This Will Calculate the Difference between want. A player will not want a property very much if it will not gain them anything.
    ie if there are 2 properties in the group and they currently have neither, receiving 1 as a trade is not really worth very much to them.
    :param Seller:
    :param Property:
    :param Buyer:
    :return:
    """
    ValSeller = Property.CalculateValueOfProperty(Seller)   # Value before sale
    ValBuyer = Property.CalculateValueOfProperty(Buyer)     # Value before sale
    Property.Owner = Buyer
    ValSellerAfter = Property.CalculateValueOfProperty(Seller)  # Value after sale
    ValBuyerAfter = Property.CalculateValueOfProperty(Buyer)    # Value after sale
    #Property.Owner = Seller

    pass


def TradeAccepted(Seller, Property, Buyer):
    pass

def BuyersOffer(ValSeller, ValSellerAfter, ValBuyer, ValBuyerAfter):
    pass


def SellersOffer(ValSeller, ValSellerAfter, ValBuyer, ValBuyerAfter):
    pass


if __name__ == "__main__":  # this modules testing will be covered inside of AI.py
    pass
