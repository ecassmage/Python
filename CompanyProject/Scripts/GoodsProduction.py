import math
import Company


def Goods(company=None, goods=None, price=None, consumers=None, maxPrice=1000):
    print("Hello")
    if company is not None:
        goods = company.goods[0] if goods is None else goods
        price = company.price[0] if price is None else price
        consumers = company.consumers[0] if consumers is None else consumers
    else:
        if goods is None or price is None or consumers is None:
            raise Exception

    consumerReach = consumers - consumers * (math.log(price, maxPrice))
    print(consumerReach)


"""
    y = ((c * x)/2) * (cos((pi * p) / 2) + 1)
"""
if __name__ == '__main__':
    company = Company.Company()
    Goods(company=company, goods=1000, price=250, consumers=100000)
