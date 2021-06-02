class Company:

    def __init__(self):
        self.name = self.writeNames()
        self.revenue = [0, 0, 0, 0, 0]
        self.costs = [0, 0, 0, 0, 0]
        self.profits = [0, 0, 0, 0, 0]
        self.goods = [0, 0, 0, 0, 0]
        self.price = 0
        self.maxPrice = 1000
        self.DTDCosts = {}
        self.productionValue = 0
        self.employees = 0
        self.maxEmployees = 0
        self.producedGoods = 0
        self.consumerInterest = [100000]
        self.modifiers = {}

    @staticmethod
    def writeNames():
        names = []
        for line in open("CompanyNames.txt", 'r'):
            names.append(line.replace(' \t', '').replace('\n', ''))
        return names
