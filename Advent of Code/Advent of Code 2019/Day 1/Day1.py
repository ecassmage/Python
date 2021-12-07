def Day1(array):
    summed = 0
    for number in array:
        summed += number // 3 - 2

    return summed


def Day2Recurse(number):
    newNumber = number // 3 - 2
    if newNumber <= 0:
        return 0
    return newNumber + Day2Recurse(newNumber)


def Day2(array):
    summed = 0
    for number in array:
        summed += Day2Recurse(number)
    return summed


if __name__ == '__main__':
    arr = []
    with open("input.txt") as file:
        for line in file:
            arr.append(int(line.strip()))
    print(Day1(arr))
    print(Day2(arr))
    pass
