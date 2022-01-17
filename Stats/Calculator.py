import math


def factorial(number: int):
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return fact


def BinCoefficient(x: int, n: int):
    return factorial(x) / (factorial(n) * factorial(x - n))


def nBin(x: int, r: int, p: float):
    return (BinCoefficient(x - 1, r - 1)) * (p ** r) * ((1 - p) ** (x - r))


def Bin(s: int, n: int, p: float):
    """ Binomial Distribution

    :param s: successes
    :param n: number of trials
    :param p: probability of success
    :return:
    """
    return (BinCoefficient(n, s)) * ((p**s) * (1 - p)**(n-s))


def Geo(x: int, p: float):
    return p * ((1 - p)**(x - 1))


def mean(p: float):
    temp = 1 / p
    return int(temp) if temp == int(temp) else temp


def VarGeo(p: float):
    return (1 - p) / p**2


def CumulativeGeo(s: int, p: float):
    return 1 - (1 - p)**s


def HyperGeo(x=0, n=0, N=0, M=0, MEAN=False, VAR=False):
    if MEAN:
        return (n * M) / N

    if VAR:
        return (n * M * (N - M) * (N - n)) / (N**2 * (N - 1))

    return (BinCoefficient(M, x) * BinCoefficient(N - M, n - x)) / BinCoefficient(N, n)


def poisson(x, Lambda, less=False):
    if less:
        num = 0
        for i in range(x+1):
            num += ((Lambda ** i) * (math.e ** (-1 * Lambda))) / factorial(i)
        return num
    return ((Lambda ** x) * (math.e ** (-1 * Lambda))) / factorial(x)


def main():
    pass


if __name__ == "__main__":
    # print(f"0: {factorial(0)}")
    # print(f"1: {factorial(1)}")
    # print(f"2: {factorial(2)}")
    # print(f"3: {factorial(3)}")
    # print(f"4: {factorial(4)}")
    # print(f"5: {factorial(5)}")
    # print(f"6: {factorial(6)}")
    # print(Bin(5, 12, 1 / 2))
    # print(Bin(7, 12, 1 / 2))
    # print(nBin(10, 3, 0.4))
    # print(mean(0.2))
    # print(mean(0.3))
    # print(VarGeo(0.3))
    # print(CumulativeGeo(3, 0.3))
    # print(HyperGeo(0, 6, 24, 4))
    # print(HyperGeo(2, 5, 120, 80))
    # print(Bin(2, 5, 80 / 120))
    # print(poisson(3, 2.3 * 2))
    # print(poisson(1, (1 - 0.1) * (1 / 3)))
    # print(poisson(0, 0.1 * 3))
    main()
