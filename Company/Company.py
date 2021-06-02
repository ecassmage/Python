import random


class Company:

    def __CompanyInformation__(self, world):
        self.name = ''
        self.yearFounded = 0
        self.age = 0
        self.world = world

    def __shares__(self):
        """ Shares of the company """
        self.shares = 0
        self.outstandingShares = 0
        self.notOutstandingShares = 0
        self.shareMaxPrice = 400

    def __RevenueAndCosts__(self):
        """ Revenue and Costs """

        """ Revenue """
        self.dailyRevenue = 0
        self.weeklyRevenue = 0
        self.monthlyRevenue = 0
        self.yearlyRevenue = 0

        """ Costs """
        self.dailyCosts = 0
        self.weeklyCosts = 0
        self.monthlyCosts = 0
        self.yearlyCosts = 0

        """ Cash """
        self.cash = 0

    def __Profits__(self):
        self.dailyProfits = 0
        self.weeklyProfits = 0
        self.monthlyProfits = 0
        self.yearlyProfits = 0

    def __ProductionCapabilities__(self):
        """
        FactoryTemplate:
        self.CapitalProducers = {
            FactoryName: {
                "gpd": number,  # gpd -> Goods Per Day
                "nw": number,  # nw -> Needed Workers (per Day)
                "upkeep": number  # upkeep -> Monthly Upkeep
            }
        }
        """
        self.CapitalProducers = {}
        return

    def __goods__(self):
        def generateRandomPrice():
            return random.randrange(0, 2000)
        """ Goods and pricing indexes """

        """ Goods """
        self.dailyGoods = 0
        self.weeklyGoods = 0
        self.monthlyGoods = 0
        self.yearlyGoods = 0
        self.dailyGoodsProduced = 0
        self.weeklyGoodsProduced = 0
        self.monthlyGoodsProduced = 0
        self.yearlyGoodsProduced = 0
        self.dailyGoodsSold = 0
        self.weeklyGoodsSold = 0
        self.monthlyGoodsSold = 0
        self.yearlyGoodsSold = 0
        self.goodsQuality = 'average'

        """ Prices """
        self.price = generateRandomPrice()
        self.productCost = 0

    def __ConsumerAvailability__(self):
        self.popularity = 0
        self.ambientConsumers = 0
        self.seasonalPopularity = {
            "Q1": 2000,
            "Q2": 1000,
            "Q3": 2500,
            "Q4": 10000,
        }

    def __init__(self, world):
        self.__CompanyInformation__(world)
        self.__shares__()
        self.__RevenueAndCosts__()
        self.__Profits__()
        self.__ProductionCapabilities__()
        self.__goods__()
        self.modifiers = {
            "EfficientCompany": False,
            "NewCompany": True,
            "minorScandal": False,
            "mediumScandal": False,
            "majorScandal": False,
            "catastrophicScandal": False,
        }
        self.setStuffUp()

    def setStuffUp(self):
        self.worldAddCompany()

    def worldAddCompany(self):
        self.world.companies.append(self)

    def addMoreCapital(self, number=1):
        for _ in range(number):
            self.CapitalProducers.update({
                f"Factory {len(self.CapitalProducers)}": {
                    "gpd": 100,
                    "nw": 20,
                    "upkeep": 10000
                }
            })
