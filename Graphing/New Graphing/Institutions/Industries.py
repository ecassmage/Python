import configReader
settings = configReader.settingsFileReader()


class Economy:
    def __init__(self):
        self.consumerPop = 100000000  # 100 million
        self.stability = 'stable'  # State of the overall Economy


class Industry:
    def __init__(self, sett, rangeOfPrice, bias):
        self.priceMax = sett['productCost'] * rangeOfPrice  # range of prices in industry
        self.marketCap = 0  # marketCap of All companies in this industry
        self.shares = 0  # shares of all companies in this industry
        self.priceAverage = 0  # average price all companies in this industry sell their products at
        self.companiesUnderAverage = 0
        self.consumerBias = bias  # % who like it cheap
        self.consumerSize = sett['startSize']  # size of the basic consumer market
        self.companiesInIndustry = []  # companies in industry


class Electronics(Industry):
    def __init__(self):
        Industry.__init__(self, settings['industries']['electronics'], 20, 50)


class Mining(Industry):
    def __init__(self):
        Industry.__init__(self, settings['industries']['mining'], 10, 25)


class FastFood(Industry):
    def __init__(self):
        Industry.__init__(self, settings['industries']['fastFood'], 8, 20)


class Retail(Industry):
    def __init__(self):
        Industry.__init__(self, settings['industries']['retail'], 10, 28)


class Agriculture(Industry):
    def __init__(self):
        Industry.__init__(self, settings['industries']['agriculture'], 15, 15)

