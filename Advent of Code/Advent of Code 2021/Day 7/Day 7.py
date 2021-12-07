import copy


def math(number):
    num = 0
    for i in range(1, number+1):
        num += i
    return num


def day7(array):
    # arraySort = sorted(array)
    # number = arraySort[len(arraySort)//2]
    # num = sum(array) // len(array)
    # print(num)
    best = 0
    number = 0
    for i in range(1000):
        number = 0
        for val in array:
            number += abs(math(val-i if val > i else i-val))
        if number == 0:
            pass
        elif best == 0:
            best = number
        elif number < best:
            best = number
        print(i)
    print(best)
    pass


def main():
    arr = []
    dictionary = {}
    for line in open("input.txt"):
        for element in line.strip().split(","):
            arr.append(int(element))
    print(arr)
    day7(arr)
    pass


if __name__ == "__main__":
    main()
    pass
