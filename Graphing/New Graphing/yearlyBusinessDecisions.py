
"""
Name: Company Simulator
Developer: Evan Morrison
Version: 0.1.0.0
DateStarted: 2021/02/14
Date: 2021/02/17
"""

import configReader  # Just Reads my Json files so that all json files are easy to read and change at will
import Company
import buyingGains
from Institutions import StockMarket, Bank, Industries
import competition
import Taxes  # Always seems to be there like a constant of life
import profitMargins
import random
settings = configReader.settingsFileReader()


# Calculates the Items produced per capital factor ie Factories, MiningEquipment etc.
def capitalFactorOfProduction(employees, needed, Assets, Total, Location):
    if employees - needed > 0:
        employees -= needed
        Total += Location['product'] * Assets
        return Total, employees
    Total += (employees / needed) * Location['product'] * Assets
    return Total, 0


# Calculates the Production factor of company in that how much of whatever the company produces in items per year
def goodsProducedPerYear(company):
    company.previousYearEmployees = company.employees
    employeeRemaining = company.employees
    totalProduced = 0

    """ List of all the factors of Production you just need to be added similar to the others and it does the rest """
    """ Future probably go through here and make it more efficient since only 1 holds values factor['factor'] """
    meansToProduce = [
        (company.factors["factory"], settings['capital']['factory']),
        (company.factors["mining"], settings['capital']['mining']),
        (company.factors["farmable"], settings['capital']['farmable']),
        (company.factors["building"], settings['capital']['building'])
    ]
    # (meanOfProduction, Location) ▲
    # meanOfProduction is a factor of production
    # Location is the location in the settings dictionary the relevant information is found in.

    for meanOfProduction, Location in meansToProduce:

        maxCapacity = meanOfProduction * Location['employed']
        totalProduced, employeeRemaining = capitalFactorOfProduction(
            employeeRemaining, maxCapacity, meanOfProduction, totalProduced, Location)
        if employeeRemaining <= 0:

            # hireMore(company, hire=True)

            return totalProduced

    profitMargins.hireMore(company, employee=employeeRemaining)  # import

    return totalProduced


# Calculates revenue of the companies based on how much products they sold.
def soldGoods(company):
    """
    :param company: -> Company Object
    :return:
    """

    """ ▼ Storing for previous Years Statistics ▼ """
    company.previousYearRevenue = company.revenue
    company.previousYearCosts = company.costs
    company.profitsPreviousYear = company.profits
    company.previousYearProductsSold = company.goodsSold
    """ ▲ Storing for previous Years Statistics ▲ """

    """ ▼ Company Revenue Calculations ▼ """
    # demand = competition.advancedDemand(company, price=company.productWorth, strength='extreme')
    # company.revenue, company.goodsSold = profitMargins.revenueCalculation(company.productWorth, company.goods, demand)
    # bestPrice = competition.bestPricePossible(company=company)
    # bestDemand = competition.advancedDemand(company, price=bestPrice)
    print(company.productWorth)
    company.revenue = competition.advancedRevenue(company, simpleFunc=False)
    """ ▼ Company Costs Calculations ▼ """
    company.costs = profitMargins.costCalculation(company, company.goodsProduced)

    """ ▼ Company Change of Goods in Storage ▼ """
    # company.goods -= company.goodsSold

    """ ▼ Company Profits calculations ▼ """
    company.profits = (company.revenue - company.costs)
    company.cash += company.profits
    Taxes.taxes(company)
    profitMargins.checkChangesToSalesFigure(company)


def determineWorthOfCompany(company):
    if company.marketCap < 1000000:  # 1 Million is my definition of a small company
        pass
    return


def goodsAdded(company):
    company.goodsProduced = goodsProducedPerYear(company)
    company.goods += company.goodsProduced
    return


def checkAndBalances(company):
    if company.isExpanding():
        buyingGains.expandingCompany(company)
    return


def centralManager(companyObject):
    print(companyObject.productWorth)
    goodsAdded(companyObject)
    soldGoods(companyObject)
    StockMarket.marketCapitalizationCalculator(companyObject)
    print(companyObject.productWorth)


def main():

    electronics = Industries.Electronics()
    bankOfCanada = Bank.Bank()
    stockOfCanada = StockMarket.StockMarket()

    comp = Company.Company(bankOfCanada, stockOfCanada, electronics, 'electronics', 2021, 'blue')

    for i in range(500):
        centralManager(comp)
        print(f"{comp.revenue:.2f} - {comp.costs:.2f} = {comp.profits:.2f}\nTotal Cash: {comp.cash}\n")
        if i % 15 == 0 and i > 5:
            comp2 = Company.Company(bankOfCanada, stockOfCanada, electronics, 'electronics', 2021, 'red')
        if i % 100 == 0:
            print()
    print(comp.factors)

    # print(comp, '\n\n\n')
    # print(settings)
    # determineWorthOfCompany()


if __name__ == "__main__":
    main()
