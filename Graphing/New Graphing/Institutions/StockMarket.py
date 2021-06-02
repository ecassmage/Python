import configReader
settings = configReader.settingsFileReader()


class StockMarket:
    def __init__(self):
        self.name = "STK-MKT"
        self.marketValue = 0
        self.sharesTotal = 0
        self.companies = []


def stockSplit(company):
    return


def factorValue(company):
    return (company.factors[company.factorFocus] * settings['capital'][company.factorFocus]['cost']) * 0.75


def landValue(company):
    return (company.land * settings['land']['acre']['cost']) * 0.9


def consumerValue(company):
    """ This is to simulate the value from having lots of consumers willing to buy from you """
    return ((company.totalConsumers - company.popularity) * 0.1) + (company.popularity * 0.25)


def valueAddedFromOtherSources(company, valueAdded):
    valueStart = valueAdded
    if valueAdded <= 0:  # Don't want valueAdded to a dead company
        return 0
    if company.innovative:
        valueAdded *= 1.025  # innovation breeds more money so raises investor confidence
    if company.expanding:
        valueAdded *= 1.03  # Means the future is looking more bright raises investor confidence
    if company.companyInDebt:
        valueAdded *= 0.9875  # Not very good to be in debt. Not the worst thing though
    if company.soldAllGoods:
        valueAdded *= 1.005  # We sold all goods meaning out of the money we spent on goods we wasted none of it.
    if company.overProduction:
        valueAdded *= 0.99  # This means the company wasted money causing a loss of confidence
    if 0 < company.profits > company.profitsPreviousYear:
        valueAdded *= 1.05  # Shows a good year for Company Raising share Price
        if company.costs < company.previousYearCosts:
            # inside if because this means profits went up and costs went down even better
            # then if both profits and costs went up
            valueAdded *= 1.01
    if company.yearlyTrend > 10:
        valueAdded += (valueAdded * 0.1)
    elif company.yearlyTrend < -10:
        valueAdded -= (valueAdded * 0.1)
    else:
        valueAdded += (valueAdded * (company.yearlyTrend/100))  # whether good or bad trends speak wonders for the future
    if valueAdded < valueStart:
        return valueStart  # Just because you look bad doesn't mean cold hard cash is worth less
    return valueAdded


def marketCapitalizationCalculator(company):

    valueAdded = company.cash + landValue(company) + factorValue(company)
    valueAdded = valueAddedFromOtherSources(company, valueAdded)

    valueLost = company.debt
    company.marketCap = valueAdded - valueLost
    company.sharePrice = company.marketCap / company.shares
    # return valueAdded - valueLost
