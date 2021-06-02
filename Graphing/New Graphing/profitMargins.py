# import random
import buyingGains
import configReader  # Just Reads my Json files so that all json files are easy to read and change at will
import competition
settings = configReader.settingsFileReader()


def smallerThan(x, y):  # Checks whether or not demand is smaller then Goods or vice versa
    if x < 0 or y < 0:
        return 0
    return y if x > y else x  # Returns smaller of the two values


def demandCalculation(company, productPrice, consumer=None):
    """
    Demand Calculator for determining demand for a product at its current price level
    """
    if consumer is None:
        consumer = company.totalConsumersFunc()
    # # print(consumerSize - (consumerSize * (productPrice/maximumPrice)))
    # return int(consumer-(consumer*(productPrice/company.industry.priceMax)))
    return competition.advancedDemand(company, price=productPrice, consumerSize=consumer, strength='extreme')


def revenueCalculation(productPrice, goods, demand, needGoods=True):
    # print('revenueCalculation', productPrice, goods, demand)
    soldGoods = int(smallerThan(goods, demand))
    if needGoods:
        return soldGoods * productPrice, soldGoods
    return soldGoods * productPrice


def costCalculation(company, goodsProduced, simplifiedFunc=False):
    """
    Currently Not finished,
        Employees, Fixed costs and Product costs have been mostly implemented but somethings like
        Debt costs have yet to be implemented as I am currently still working on programming their scripts
    """
    if simplifiedFunc is False:
        allFixedCosts = company.fixedCosts + company.advertisingCosts + company.factorFixedCost()
        employeeCosts = (company.employees * company.employeeWage) * 1500  # Light working they get long Lunches
        producedProducts = goodsProduced * company.productCost
        debtInterest = company.debtPayment
        allDebts = allFixedCosts + employeeCosts + producedProducts + debtInterest
        return allDebts * (1 + (company.totalFactorsOwned() / 100))
    return goodsProduced * company.productCost


# AntiCompetitive actions are not tolerated therefore everything needs minimum 5% markup/product
def makeSureCompanyIsProfitable(company):
    """No Uncompetitive actions like losing money to take your competition out of the market safety"""
    if company.productWorth <= company.productCost:
        company.productWorth = (company.productCost * 1.05)
    if company.productWorth >= company.industry.priceMax:
        company.productWorth -= 0.01


def IncreaseDecreaseCalculator(company, priceChange):
    expectedRevenueIncreaseNextYear = revenueCalculation(
        company.productWorth + priceChange,
        company.goodsProduced,
        demandCalculation(company, company.productWorth + priceChange),
        needGoods=False
    )
    expectedRevenueDecreaseNextYear = revenueCalculation(
        company.productWorth - priceChange,
        company.goodsProduced,
        demandCalculation(company, company.productWorth - priceChange),
        needGoods=False
    )
    return expectedRevenueIncreaseNextYear, expectedRevenueDecreaseNextYear


def testPossibleChangesToPrice(company, goods=None, consumerMax=None):
    try:

        if goods is None:
            goods = company.goodsProduced
        if consumerMax is None:
            consumerMax = company.totalConsumersFunc()

        return competition.bestPricePossible(maxPrice=company.industry.priceMax, strength=company.consumerDropOffLevel)

    except ZeroDivisionError:
        print("Broken", goods, consumerMax, -company.industry.priceMax, consumerMax, company.totalConsumersFunc())


def employeesNeeded(company):
    return company.factors[company.factorFocus] * (
            settings['capital'][company.factorFocus]['employed'] *
            settings['industries'][company.industryName]['employeeRatio'])


# Calculates employment levels in the Company whether too many are employed or too few
def hireMore(company, employee, hire=False):

    if hire is False:
        company.employees -= employee
        company.employeeCap = True
        return

    if company.employees - employee <= employeesNeeded(company):
        company.employees += employee
        return

    company.employees = employeesNeeded(company)
    company.employeeCap = True
    return


def decideOutcomeOfMarginChanges(company, bestScenario):
    company.productWorth = bestScenario['price']
    if bestScenario['goods'] > company.goodsProduced:
        # print(f"That is the Case for goods Increase: {bestScenario['goods']}")
        if company.employees + 10 < employeesNeeded(company):
            hireMore(company, 10, hire=True)
            return
        else:
            company.employeeCap = True
            buyingGains.expandingCompany(company)

    elif bestScenario['goods'] < company.goodsProduced:
        hireMore(company, 10, hire=False)

    if bestScenario['consumer'] > company.goodsProduced:
        company.isAdvertising = True

    elif bestScenario['consumer'] < company.goodsProduced:
        company.isAdvertising = False
        # doDespicableThingsFunction() Do something that will lose you popularity.
        print("How!?!?!? does this make more money losing customers. Something is wrong!!!")
    if company.profits > 0:
        buyingGains.expandingCompany(company)


def changeGoodsQuantityOrProductSellPrice(company):
    """
    Possible change for profitability. What is causing loss of potential products, too many goods or too expensive price
    Revenue = (-(consumerMax/priceMax)*(productPrice) + consumerMax) * productPrice
    Revenue = goods * productPrice
    goods(productPrice) = (-(consumerMax/priceMax)*(productPrice) + consumerMax)
    goods(productPrice) =  productPrice(-consumerMax/priceMax)productPrice + consumerMax)
    goods = -consumerMax/priceMax(productPrice) + consumerMax
    (goods - consumerMax) = -consumerMax/priceMax(productPrice)
    productPriceEquilibrium = (goods - consumerMax) * (priceMax/-consumerMax)
    """

    """ For Goods I am worried about the purchase of factories for the worse because it looks more profitable """
    checkChangesToSalesFigure(company)
    goods = settings['capital'][company.factorFocus]['product'] * 0.25
    consumer = company.totalConsumersFunc() * 0.2
    standardPrice = testPossibleChangesToPrice(company)
    goodsIncrease = testPossibleChangesToPrice(company, goods=company.goodsProduced+goods)
    goodsDecrease = testPossibleChangesToPrice(company, goods=company.goodsProduced-goods)
    consumerIncrease = testPossibleChangesToPrice(company, consumerMax=company.totalConsumersFunc()+consumer)
    consumerDecrease = testPossibleChangesToPrice(company, consumerMax=company.totalConsumersFunc()-consumer)
    lis = [
        [standardPrice, None, None],
        [goodsIncrease, company.goodsProduced+goods, None],
        [goodsDecrease, company.goodsProduced-goods, None],
        [consumerIncrease, None, company.totalConsumersFunc()+consumer],
        [consumerDecrease, None, company.totalConsumersFunc()-consumer],
    ]
    bestProfit = company.profits
    bestScenario = {
        'goods': company.goodsProduced, 'consumer': company.totalConsumersFunc(), 'price': standardPrice}
    for priceLoop, goodsLoop, consumerLoop in lis:

        if consumerLoop is None:
            consumerLoop = company.totalConsumersFunc()

        if goodsLoop is None:
            goodsLoop = company.goodsProduced

        revenueTemp = revenueCalculation(
            priceLoop, goodsLoop, demandCalculation(company, priceLoop, consumerLoop), needGoods=False)
        costTemp = costCalculation(company, goodsLoop, simplifiedFunc=True)

        if revenueTemp - costTemp > bestProfit:
            bestScenario = {'goods': goodsLoop, 'consumer': consumerLoop, 'price': priceLoop}
            bestProfit = revenueTemp - costTemp
        print(f"{revenueTemp - costTemp}", end=', ')
    print()
    decideOutcomeOfMarginChanges(company, bestScenario)
    company.productWorth = round(company.productWorth, 2)
    makeSureCompanyIsProfitable(company)


def hypotheticalSalesFigures(company, hypotheticalList, baseFigures):
    # print(hypotheticalList, '\n')
    print(baseFigures.items(), '\n')
    for i in hypotheticalList.items():
        print(i)
    print("\n")
    bestProfit = {'profit': baseFigures['profits'], 'price': baseFigures['price']}
    for name in hypotheticalList:

        if hypotheticalList[name]['profits'] > baseFigures['profits']:

            if hypotheticalList[name]['profits'] > bestProfit['profit']:
                bestProfit['profit'] = hypotheticalList[name]['profits']
                bestProfit['price'] = hypotheticalList[name]['price']

            if hypotheticalList[name]['revenue'] > baseFigures['revenue']:
                pass

            if hypotheticalList[name]['costs'] < baseFigures['costs']:
                pass

            if hypotheticalList[name]['goods'] != baseFigures['goods']:

                if hypotheticalList[name]['goods'] > baseFigures['goods']:

                    if company.employees + 10 < employeesNeeded(company):
                        hireMore(company, 10, hire=True)
                    else:
                        company.employeeCap = True
                        buyingGains.expandingCompany(company)

                else:
                    hireMore(company, 10, hire=False)

                if employeesNeeded(company) - company.employees < 10:
                    print(employeesNeeded(company), company.employees)

            if hypotheticalList[name]['consumers'] != baseFigures['consumers']:

                if hypotheticalList[name]['consumers'] > baseFigures['consumers']:
                    company.isAdvertising = True

                else:
                    company.isAdvertising = True
                    print("This is a bad decision making idea.")
    company.productWorth = bestProfit['price']
    return


def checkChangesToSalesFigure(company):

    goods = settings['capital'][company.factorFocus]['product'] * 0.2
    consumer = company.totalConsumersFunc() * 0.2

    """ I could but I don't want to """
    goodsIncrease = competition.priceForGoods(company=company, goods=company.goodsProduced + goods)
    goodsDecrease = competition.priceForGoods(company=company, goods=company.goodsProduced - goods)
    consumerIncrease = competition.priceForGoods(company=company, consumer=company.totalConsumersFunc() + consumer)
    consumerDecrease = competition.priceForGoods(company=company, consumer=company.totalConsumersFunc() - consumer)
    competitivePrice = competition.priceForGoods(company=company, consumer=competition.splitConsumers(company, True))
    standardPrice = competition.priceForGoods(company=company)

    listOfPossibilities = [

        [standardPrice, None, None, 0, 'standardPrice'],
        [goodsIncrease, company.goodsProduced + goods, None, 10000, 'goodsIncrease'],
        [goodsDecrease, company.goodsProduced - goods, None, -10000, 'goodsDecrease'],
        [consumerIncrease, None, company.totalConsumersFunc() + consumer, 10000, 'consumerIncrease'],
        [consumerDecrease, None, company.totalConsumersFunc() - consumer, -10000, 'consumerDecrease'],
        [competitivePrice, None, competition.splitConsumers(company, True), 0, 'competitivePrice']

    ]
    informationGenerated, baseInformation = {}, {}
    for i in listOfPossibilities:
        print(i)
    print("\n")
    """ I could but I don't want to """
    for price, goods, consumers, extraCosts, name in listOfPossibilities:
        goods = company.goodsProduced if goods is None else goods
        consumers = company.totalConsumersFunc() if consumers is None else consumers

        revenueAccrued = competition.advancedRevenue(company, price, goods, consumers, simpleFunc=True)
        costAccrued = costCalculation(company, goods) + extraCosts  # extraCosts is for minor ad costs + more employees
        profitsAccrued = revenueAccrued - costAccrued

        if name == 'standardPrice':
            baseInformation = {
                'revenue': revenueAccrued, 'costs': costAccrued, 'profits': profitsAccrued,
                'price': price, 'goods': goods, 'consumers': consumers
            }
        else:
            informationGenerated[name] = {
                'revenue': revenueAccrued, 'costs': costAccrued, 'profits': profitsAccrued,
                'price': price, 'goods': goods, 'consumers': consumers
            }
    hypotheticalSalesFigures(company, informationGenerated, baseInformation)
