import random
import configReader
settings = configReader.settingsFileReader()


def checkLand(company):
    requiredLand = settings['capital'][company.factorFocus]['land']
    neededPurchase = (requiredLand - company.landRemaining) if (company.landRemaining < requiredLand) else 0
    company.cash -= neededPurchase * settings['land']['acre']['cost']

    company.land += neededPurchase
    company.landRemaining += neededPurchase

    return


def buyingNewFactor(company):
    if company.profits > 0 and company.yearlyTrend >= 2 and company.employeeCap:
        checkLand(company)
        company.factors.update({company.factorFocus: company.factors[company.factorFocus] + 1})  # plus 1 factor
        company.cash -= settings['capital'][company.factorFocus]['cost']
        company.landRemaining -= settings['capital'][company.factorFocus]['land']
        company.employeeCap = False
        # print("\nBought Factory\n")
    return


# Is the company attempting too expand or stagnant
def expandingCompany(company):
    buyingNewFactor(company)

    if company.goods == 0:

        randNumber = random.randrange(100)
        if company.expanding and randNumber >= 95:
            buyingNewFactor(company)

        elif randNumber >= 90:
            company.expanding = True
        elif randNumber <= 20:
            company.expanding = False


def isAdvertisingGoodIdea():
    pass


def payingBackDebt(company):
    company.debtPayment = company.debt * (company.interestRate/100)
    company.registeredBank.cash += company.debtPayment


def passedBankruptcyLine(graph, company):
    """ Will first attempt to sell off assets in an attempt to bring themselves off the ground. """
    company.factors[company.factorFocus] -= 1
    return


def sellShares():
    """This is to determine whether to sell a portion of insider shares or not max sell able at a time is 5%"""
    return


def companyInDebt(graph, company):
    if company.bankruptcyTimer == 0:
        passedBankruptcyLine(graph, company)
    if company.cash >= 0:
        company.bankruptcyTimer = 5
        return
    debt = abs(company.cash)
    if company.registeredBank.cash >= debt:

        company.registeredBank.cash -= debt
        company.debt += debt
        company.registeredBank.onLoan += debt
        company.companyInDebt = True

        company.cash = 0
        company.interestRate = company.registeredBank.interestRate
