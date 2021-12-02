def read(string):
    return open(string, "r").readlines()


def idk():
    listCurrent, summed, prev, filled, numberOfIncreases = [0, 0, 0], 0, 0, 0, 0
    for number in [int(val) for val in open("input.txt").readlines()]:

        if filled == 3:
            if summed + number - listCurrent[0] > summed:
                numberOfIncreases += 1
        else:
            filled += 1

        summed += number
        summed -= listCurrent[0]
        listCurrent = [listCurrent[1], listCurrent[2], number]
    return numberOfIncreases


if __name__ == '__main__':
    num = 0
    prev = 0
    previous = 0
    lis = []
    for line in read("input.txt"):
        lis.append(int(line))
    for i in range(len(lis)):
        try:
            prev = lis[i] + lis[i+1] + lis[i+2]
            if i == 0:
                pass
            elif prev > previous:
                num += 1
            previous = prev
        except IndexError:
            print(num)
            break

    print(idk())

