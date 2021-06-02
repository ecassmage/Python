import math
import random
import graphicalInterface
import configReader  # Just Reads my Json files so that all json files are easy to read and change at will
settings = configReader.settingsFileReader()
rules = configReader.rulesFileReader()


class Company:

    def __institutionsRegistered__(self, industry, bank, stockMarket):
        self.industry = industry  # The industry this company is a part of
        self.bank = bank  # The bank that this company is a part of. Only 1 bank
        self.stockMarket = stockMarket  # The Stock market that this company is currently a part of. Only 1 Stock market

    def __companyInfo__(self, industryName, year, color):
        self.name = nameGenerate()  # Name of Company. Random Letters Inc. chooses the names
        self.yearFounded = year  # The founding year of the company
        self.yearPresent = year  # The current Year.
        self.industryName = industryName  # The Name of the industry this company is a part of. Just The Name.
        self.addCompanyToInstitutions()  # Just a command to add this company to certain lists
        self.color = color  # The color the lines on the graph will show up as.

    def __graphicalStorage__(self):
        self.yUpper, self.yLower = 0, 0  # Upper and Lower bounds for graphing to fit info on screen.
        self.nodesInactive = self.createNodes()  # Holds the Inactive Nodes for company on graph
        self.linesInactive = self.createLines()  # Holds the Inactive Lines for company on graph
        self.nodesActive = []  # Holds the Active Nodes for company on graph
        self.linesActive = []  # Holds the Active Lines for company on graph

    def __economicStats__(self):
        self.marketCap = 1000000  # Market Capitalization
        self.cash = 1000000  # Cash Available
        self.yearlyTrend = 0  # profit Trends. Are the good + or are they bad -
        self.debt = 1000  # The current debt held buy company
        self.interestRate = 0  # Interest Rate for debt
        self.bankruptcyTimer = 5  # x number of years before bankruptcy

    def __stocks__(self):
        self.shares = 10000  # Shares the company is split into.
        self.percentOutstanding = 15  # Shares currently on the market
        self.percentNotOutstanding = 85  # Shares owned by the company
        self.sharePrice = 0
        # self.Volume = 0  # Blanked For Now since this would be incredibly difficult to make realistic
        self.approval = 50
        self.dividends = 1.5  # percent given back to investors each year per share

    def __companyState__(self):
        self.state = 'average'  # Current Economical State
        self.innovative = True  # Are they developing top of the line Products
        self.expanding = True  # Is Company Expanding
        self.corrupt = False  # Corruption
        self.companyInDebt = False  # Company in Debt
        self.employeeCap = False  # No Jobs available for more employees
        self.soldAllGoods = False  # All goods were sold bonuses ahead
        self.demandMatched = False  # We matched equilibrium demand and supply
        self.overProduction = False  # We are producing more then we can sell
        self.dividendGiven = False  # We give Share Holders dividends. ▲ in Volume Trading Probably ▼ in Volatility.

    def __revenue__(self):
        self.productWorth = 1000  # The Price the Company has chosen to sell the product at
        self.productionValue = settings['industries'][self.industryName]['productionValue']  # Difficulty to Produce
        self.revenue = 0  # Revenue Per Year

    def __costs__(self):
        self.costs = 0  # Costs for the Year
        self.employees = math.ceil(100 * settings['industries'][self.industryName]['employeeRatio'])  # Employee Count
        self.employeeWage = settings['industries'][self.industryName]['wage']  # Employee Wages
        self.fixedCosts = settings['industries'][self.industryName]['fixedCosts']  # Fixed Costs which don't move
        self.productCost = settings['industries'][self.industryName]['productCost']  # Cost to produce Item
        self.debtPayment = 0  # The Amount of interest accrued by the company from its outstanding debt

    def __profits__(self):
        self.profits = 0  # Yearly Profits
        self.profitsPreviousYear = 0  # Record of Profits from the previous year.
        self.previousYearRevenue = 0  # Record of Revenue from the previous year.
        self.previousYearCosts = 0  # Record of Costs from the previous year.
        self.previousYearEmployees = 0  # Record of Employees from the previous year.
        self.previousYearProductsSold = 0  # Record of Products Sold from the previous year.

    def __goodsProduction__(self, industryName):
        self.factors = {
            "factory": 0,
            "mining": 0,
            "building": 0,
            "farmable": 0
        }  # ▲ new types of Factors added here
        self.factorFocus = settings['industries'][industryName]['factor']
        self.factors.update({self.factorFocus: 1})
        self.totalOwned = self.totalFactorsOwned()

        """ Goods Information """
        self.goods = 0  # Amount of Currently in Stock
        self.goodsSold = 0  # Goods the Company Managed to sell this year
        self.goodsProduced = 0  # Amount Produced This Year

        """ Land """
        self.landRemaining = 0
        self.land = settings['capital'][self.factorFocus]['land'] * self.factors[self.factorFocus]

        """ Sales """
        self.previousYearGoodsDeficit = 0  # holds quantity of goods not sold previous year.

    def __consumers__(self):
        """ self.excessCosts """
        self.isAdvertising = False
        self.advertisingCosts = 0  # if Advertising is True -> 10% profit goes to advertise if needed.

        """ Consumers """
        self.popularity = 0  # Fans of company, Demand other corps can't steal away but is still affected by prices..
        self.ambientConsumers = 0
        self.totalConsumers = self.totalConsumersFunc()
        self.consumerDropOffLevel = 'strong'

    def __TAXES__(self):
        """ Taxes and Tax Breaks """
        self.amountGivenToCharity = 0
        self.isClean = False
        self.isEqual = False  # Determined to be fair in employment

    def __randomModifiers__(self):
        """ These are just modifiers.json to spice up the companies a little and make more fluctuations in graphs """
        self.caughtInMinorScandal = False  # Embezzlement Related
        self.caughtInMediumScandal = False  # Something Sexual Assault and the likes Related
        self.caughtInLargeScandal = False  # Something Assassination Related
        self.caughtInCatastrophicScandal = False  # Something Treason Related
        self.randomGoodPublicity = False
        self.newStartUp = True
        self.smallEfficiencyImprovement = False  # Employee discovers efficiency improvement
        self.toxicWorkEnvironment = False  # Environment hard to work in from Sexism, Racism or Bad Manager.
        self.badProductRelease = False  # Competing product released same Time, or just bad Product
        self.goodCompany = False  # Recognised as a good company like CD Projekt Red before Cyberpunk 2077
        self.minorAccidentHappened = False
        self.majorAccidentHappened = False
        self.stateOfTheArtLogisticsNetwork = False  # Really good Logistics network
        self.overPriced = False  # Like Apple, bad connotation with overpriced Greed
        self.photogenicCompany = False  # You can get fans from just appearing in a camera. (Elon Musk type Thing)

    def __init__(self, parent, window, bank, stockMarket, industry, industryName, year, color):
        """ This is set up like this calling other functions to initialize but this is better then double writing this
        out like I would have to to get a new active company, this way I just have to call all the initialing functions
        again via a make new company function and presto, a reconfigured function here """

        self.window = window
        self.parent = parent
        self.__institutionsRegistered__(industry, bank, stockMarket)
        self.__companyInfo__(industryName, year, color)
        self.__graphicalStorage__()
        self.__economicStats__()
        self.__stocks__()
        self.__companyState__()
        self.__revenue__()
        self.__costs__()
        self.__profits__()
        self.__goodsProduction__(industryName)
        self.__consumers__()
        self.__TAXES__()
        self.__randomModifiers__()

    @staticmethod
    def createNodes():
        tempListNodes = []
        for i in range(rules['companyConditions']['lengthOfGraphs'] + 10):
            tempListNodes.append(graphicalInterface.Node())
        return tempListNodes

    def createLines(self):
        tempListLines = []
        for i in range(rules['companyConditions']['lengthOfGraphs'] + 10):
            tempListLines.append(graphicalInterface.Line(self.window))
        return tempListLines

    def newCompany(self, bank, stockMarket, industry, industryName, year, color):
        self.__institutionsRegistered__(industry, bank, stockMarket)
        self.__companyInfo__(industryName, year, color)
        self.__economicStats__()
        self.__stocks__()
        self.__companyState__()
        self.__revenue__()
        self.__costs__()
        self.__profits__()
        self.__goodsProduction__(industryName)
        self.__consumers__()
        self.__TAXES__()
        self.__randomModifiers__()

    def newNode(self):
        newNodeTemp = self.nodesInactive[0]
        self.nodesInactive.pop(0)
        newNodeTemp.initiateNode(self)
        self.checkBounds(newNodeTemp)

        return newNodeTemp

    def newLine(self, start, end):
        newLineTemp = self.linesInactive[0]
        self.linesInactive.pop(0)
        newLineTemp.resetLine(start, end, self.color)
        return newLineTemp

    def cleanCompany(self):
        for active in reversed(self.linesActive):
            active.window.itemconfigure(active.line, state='hidden')
            self.linesInactive.append(active)
            self.linesActive.pop(-1)
        for active in reversed(self.nodesActive):
            self.nodesInactive.append(active)
            self.nodesActive.pop(-1)

    def pickPriceOfProduct(self):
        return random.randrange(0, self.industry.priceMax)

    def addCompanyToInstitutions(self):
        self.industry.companiesInIndustry.append(self)
        self.bank.companies.append(self)
        self.stockMarket.companies.append(self)

    def totalConsumersFunc(self):
        return self.ambientConsumers + self.popularity

    def totalFactorsOwned(self):
        totalFactors = 0
        for factor in self.factors:
            totalFactors += self.factors[factor]
        return totalFactors

    def advertisingGains(self):
        temp = round(self.popularity * 0.005, 0)
        if self.isAdvertising and self.profits > \
                rules['rules']['advertising']['perFan'] / (rules['rules']['advertising']['percent']/100):
            self.advertisingCosts = self.profits * (rules['rules']['advertising']['percent'] / 100)
            self.popularity += round(self.advertisingCosts / (rules['rules']['advertising']['perFan']), 0)
        else:
            self.advertisingCosts = 0
        self.popularity -= temp
        self.industry.consumerSize += temp

    def factorFixedCost(self):
        totalFactorCost = 0
        for factor in self.factors:
            totalFactorCost += self.factors[factor] * settings['capital'][factor]['upkeep']
        return totalFactorCost

    def trendyCompany(self):

        if self.yearlyTrend >= 0 <= self.profits:
            self.yearlyTrend += 1

        elif self.yearlyTrend < 0 <= self.profits:
            self.yearlyTrend = 1

        elif self.yearlyTrend > 0 > self.profits:
            self.yearlyTrend = -1

        elif self.yearlyTrend < 0 > self.profits:
            self.yearlyTrend += -1

        else:
            self.yearlyTrend = 0

        return

    def checkBounds(self, node):
        if node.allNodeValues[self.parent.currentGraphType] > self.yUpper:
            self.yUpper = node.allNodeValues[self.parent.currentGraphType]
        if node.allNodeValues[self.parent.currentGraphType] < self.yLower:
            self.yLower = node.allNodeValues[self.parent.currentGraphType]


def nameGenerate():
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    name = ''
    for i in range(random.randrange(2, 7)):
        name += letters[random.randrange(len(letters))]
    return name
