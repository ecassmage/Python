"""
This is bodged to death. It don't work anymore as I attempted to fix it for part 2 and probably broke it.
"""


def mostCommon(bit, lis):
    arr = []
    for line in open("input.txt"):
        line = line.replace("\n", '')
        for char in line:
            arr.append([0, 0])
        break

    for number in lis:
        for char in number:
            if char == "0":
                arr[num][0] += 1
            else:
                arr[num][1] += 1
    return arr


if __name__ == "__main__":
    arr = []
    for line in open("input.txt"):
        line = line.replace("\n", '')
        for char in line:
            arr.append([0, 0])
        break

    listOfNums = []
    for line in open("input.txt").readlines():
        listOfNums.append(line.replace("\n", ""))

    for line in open("input.txt").readlines():
        line = line.replace("\n", '')
        for num, char in enumerate(line):
            if char == "0":
                arr[num][0] += 1
            else:
                arr[num][1] += 1
    gamma = ""
    epsilon = ""
    for zero, one in arr:
        if zero > one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print(arr)
    print(int(gamma, 2) * int(epsilon, 2))
    print(gamma + " " + epsilon)
