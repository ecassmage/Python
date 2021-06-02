class Bank:
    def __init__(self):
        self.cash = 1000000000  # 1 Billion
        self.onLoan = 0  # Money currently loaned to other businesses
        self.interestRate = 7.8  # This banks standard interest rate (Compounded yearly)
        self.companies = []  # List of all companies who use this bank
        self.companiesOnLoan = []  # Just a list of debt driven companies
