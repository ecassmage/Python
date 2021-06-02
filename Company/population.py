import Company


class World:

    def __companyInformation__(self):
        """
        self.companyStatistics: {
            CompanyName: {
                "productPrice": price,
                "productQuantity": products
            }
        }
        """

    def __init__(self):
        self.population = 7000000000
        self.consumerRatio = 0.1
        self.maxPrice = 2000
        self.businessDesire = 100
        self.companies = []
        self.companyStatistics = {}
        self.mostExpensive, self.leastExpensive, self.averagePrice = 0, 0, 0

    def findStatsAboutCompetition(self):
        mostExpensive, leastExpensive, averagePrice = self.companies[0].price, self.companies[0].price, 0
        for comp in self.companies:
            if comp.price > mostExpensive:
                mostExpensive = comp.price
            elif comp.price < leastExpensive:
                leastExpensive = comp.price
            averagePrice += comp.price
        averagePrice /= len(self.companies)
        return mostExpensive, leastExpensive, averagePrice

    def consumersAvailable(self):
        return self.population * self.consumerRatio

    def splitConsumption(self):
        """
        priceToSellAllGoods = maxPrice ** ((consumer - goods) / consumer)
        maxProfitForInfiniteGoods = maxPrice ** (1 - (1 / math.log(maxPrice)))
        DemandCurve = consumerSize - consumerSize * (math.log(price, priceMax))
        """
        self.mostExpensive, self.leastExpensive, self.averagePrice = self.findStatsAboutCompetition()
        listOfCheapestCompanies, listOfMostExpensiveCompanies = [], []
        listOfBelowAverageCompanies, listOfAboveAverageCompanies = [], []
        for company in self.companies:
            company.ambientConsumers = 0
            if company.price == self.leastExpensive:
                listOfCheapestCompanies.append(company)
            elif company.price == self.mostExpensive:
                listOfMostExpensiveCompanies.append(company)
            if company.price <= self.averagePrice:
                listOfBelowAverageCompanies.append(company)
            else:
                listOfAboveAverageCompanies.append(company)

        for company in listOfCheapestCompanies:
            company.ambientConsumers += (self.consumersAvailable() * (0.25 / len(listOfCheapestCompanies)))
        for company in listOfBelowAverageCompanies:
            company.ambientConsumers += self.consumersAvailable() * (0.35 / len(listOfBelowAverageCompanies))
        for company in self.companies:
            company.ambientConsumers += self.consumersAvailable() * (0.40 / len(self.companies))
        pop = 0
        for i in self.companies:
            pop += i.ambientConsumers
        print(self.population)
        print(pop)

    def populationIncrease(self):
        self.population = round(self.population * 1.00075, 0)


def main():
    world = World()
    for newCompany in range(10):
        Company.Company(world)
    world.splitConsumption()
    pass


if __name__ == '__main__':
    main()
