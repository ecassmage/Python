""" I need a better way to determine what the demand a company can receive is since the way currently just involves
 splitting the consumers in pieces between the companies and so all this causes is each company getting in the
 was of each other instead of out competing each other """
import math


def smallerThan(x, y):
    return x if y > x else y


class Consumers:
    def __init__(self):
        self.electronicConsumers = 1000000
        self.electronicCompetitors = 0
        self.electronicAveragePrice = 0
        self.electronicBias = 40
        self.miningConsumers = 100000000
        self.miningCompetitors = 0
        self.fastFoodConsumers = 10000000
        self.fastFoodCompetitors = 0
        self.retailConsumers = 10000000
        self.retailCompetitors = 0
        self.agricultureConsumers = 100000000
        self.agricultureCompetitors = 0


def countCompetitors(graph, companies):

    for industry in graph.Industry:
        graph.Industry[industry].priceAverage = 0
        graph.Industry[industry].companiesUnderAverage = 0
    counts = 0
    for company in companies:
        if company.marketCap > 0:
            company.industry.priceAverage += company.productWorth
            counts += 1

    for industry in graph.Industry:
        if counts != 0:
            graph.Industry[industry].priceAverage /= counts

    for company in companies:
        if company.productWorth <= company.industry.priceAverage:
            company.industry.companiesUnderAverage += 1

    return


def bestPricePossible(company=None, maxPrice=None, strength=None):
    """ Finds the absolute best price for revenue if goods for sale were infinite. Good for finding absolute revenue """
    if company is not None:
        maxPrice = company.industry.priceMax
        strength = company.consumerDropOffLevel

    if strength == 'weak':
        return maxPrice / 2

    if strength == 'strong':
        return (((2 * maxPrice) / 3) ** 2) / maxPrice

    if strength == 'extreme':
        return maxPrice ** (1 - (1 / math.log(maxPrice)))


def priceForGoods(company=None, consumer=None, maxPrice=None, goods=None):
    """ Catches good and accurate price values for selling. """
    if company is not None:
        consumer = company.totalConsumersFunc() if consumer is None else consumer
        maxPrice = company.industry.priceMax if maxPrice is None else maxPrice
        goods = company.goodsProduced if goods is None else goods

    if company.consumerDropOffLevel == 'weak':
        return (goods - consumer) * (-maxPrice / consumer)

    if company.consumerDropOffLevel == 'strong':
        return maxPrice * ((consumer - goods) / consumer) ** 2

    if company.consumerDropOffLevel == 'extreme':
        return maxPrice ** ((consumer - goods) / consumer)


def advancedRevenue(company, goodPrice=None, goodsProduced=None, consumers=None, simpleFunc=False):
    print(goodPrice)

    def changeCompanyStats():
        # company.productWorth = bestPrice
        company.goodsSold = goodsSold
        company.goods -= goodsSold

    goodPrice = company.productWorth if goodPrice is None else goodPrice
    goodsProduced = company.goodsProduced if goodsProduced is None else goodsProduced
    consumers = company.totalConsumersFunc() if consumers is None else consumers

    if simpleFunc is False:

        maxPrice, goods, strength = company.industry.priceMax, company.goods, company.consumerDropOffLevel

        bestPrice = bestPricePossible(maxPrice=maxPrice, strength=strength)
        neededDemandForBestPrice = advancedDemand(
            price=bestPrice, consumerSize=consumers, priceMax=maxPrice, strength=strength)

        if goods >= neededDemandForBestPrice and goods >= 10 * goodsProduced:
            print("hello2")
            goodsSold = neededDemandForBestPrice

        elif neededDemandForBestPrice > goods > goodsProduced and goods >= 10 * goodsProduced:
            print("hello")
            bestPrice = priceForGoods(company, consumers, maxPrice, goods)
            goodsSold = goods

        else:
            bestPrice = priceForGoods(company, goods=goodsProduced)
            goodsSold = advancedDemand(company, price=bestPrice)

        maxRevenueFromProduced = bestPrice * goodsSold
        changeCompanyStats()
        # print(maxRevenueFromProduced)
        return maxRevenueFromProduced  # for more complex and exact calculations
    # print(goodPrice * goodsProduced)
    print(goodPrice, company.productWorth)
    expectedDemand = advancedDemand(company, price=goodPrice, consumerSize=consumers)
    return goodPrice * smallerThan(goodsProduced, expectedDemand)  # just a simple call to this function


def advancedDemand(company=None, price=None, consumerSize=None, priceMax=None, strength=None) -> int:
    """
    I am using a better formula here to calculate demand
    Example:
        Demand = consumerSize - consumerSize * (price / priceMax) -> Weak
        OR
        Demand = consumerSize - consumerSize * sqrt(price / priceMax) -> Strong
        OR
        Demand = consumerSize - consumerSize * (log_priceMax(price)) -> Extreme
    """
    price = company.productWorth if price is None else price
    consumerSize = company.totalConsumersFunc() if consumerSize is None else consumerSize
    priceMax = company.industry.priceMax if priceMax is None else priceMax
    strength = company.consumerDropOffLevel if strength is None else strength
    print(price, consumerSize, priceMax, strength)
    if strength == 'weak':
        tempDemand = consumerSize - consumerSize * (price / priceMax)  # -> Weak
    elif strength == 'strong':
        tempDemand = consumerSize - consumerSize * math.sqrt(price / priceMax)  # -> Strong
    else:
        tempDemand = consumerSize - consumerSize * (math.log(price, priceMax))  # -> Extreme

    # print("advancedDemand", price, consumerSize, priceMax, tempDemand)
    return math.floor(tempDemand)


def splitConsumers(company, override=False):

    if override is False:

        company.ambientConsumers = company.industry.consumerSize * (1 - (company.industry.consumerBias / 100))
        company.ambientConsumers /= len(company.industry.companiesInIndustry)

        if company.productWorth <= company.industry.priceAverage:
            """ This checks if your price is a cheap price """
            totalTemp = company.industry.consumerSize * (company.industry.consumerBias / 100)
            company.ambientConsumers += round(totalTemp / company.industry.companiesUnderAverage, 0)
            company.ambientConsumers = math.floor(company.ambientConsumers)
        return

    """ This is to easily check if competing price is more optimal over expensive prices. 
    Generally good for those who don't control a large market Share """
    totalTemp1 = company.industry.consumerSize * (1 - (company.industry.consumerBias / 100))
    totalTemp1 /= len(company.industry.companiesInIndustry)
    totalTemp2 = company.industry.consumerSize * (company.industry.consumerBias / 100)
    totalTemp2 /= (company.industry.companiesUnderAverage + 1)
    return round(totalTemp1 + totalTemp2, 0)


def main():
    print(advancedDemand(price=1900, consumerSize=10000000, priceMax=2000, strength='weak'))
    print(advancedDemand(price=1900, consumerSize=10000000, priceMax=2000, strength='strong'))
    print(advancedDemand(price=1900, consumerSize=10000000, priceMax=2000, strength='extreme'))
    print(f"bestPricePossible: {bestPricePossible(maxPrice=2000, strength='extreme')}")


if __name__ == "__main__":
    main()
