def file():
    arr = []
    for line in open("input.txt"):
        arr.append(line.replace(" -> ", ",").replace("\n", "").split(","))
    return arr


def getBoys(lis):
    newList = []
    largestX = 0
    largestY = 0
    for element in lis:
        newList.append([int(element[0]), int(element[1]), int(element[2]), int(element[3])])
        if int(element[0]) > largestX:
            largestX = int(element[0])
        if int(element[1]) > largestY:
            largestY = int(element[1])
        if int(element[2]) > largestX:
            largestX = int(element[2])
        if int(element[3]) > largestY:
            largestY = int(element[3])
    return newList, largestX, largestY


def goInDirection(coordL, coordinate):
    if coordinate[0] == coordinate[2]:
        if coordinate[1] > coordinate[3]:
            for Y in range(coordinate[3], coordinate[1]+1):
                coordL[Y][coordinate[0]] += 1
        else:
            for Y in range(coordinate[1], coordinate[3]+1):
                coordL[Y][coordinate[0]] += 1

    elif coordinate[1] == coordinate[3]:
        if coordinate[0] > coordinate[2]:
            for X in range(coordinate[2], coordinate[0]+1):
                coordL[coordinate[1]][X] += 1
        else:
            for X in range(coordinate[0], coordinate[2]+1):
                coordL[coordinate[1]][X] += 1
    else:
        coordVec = [1 if coordinate[0] < coordinate[2] else -1, 1 if coordinate[1] < coordinate[3] else -1]
        coordinateCurrent = [coordinate[0], coordinate[1]]
        smallestLargest = [coordinate[0] if coordinate[0] < coordinate[2] else coordinate[2], coordinate[0] if coordinate[0] > coordinate[2] else coordinate[2]]
        for _ in range(smallestLargest[0], smallestLargest[1]+1):
            coordL[coordinateCurrent[1]][coordinateCurrent[0]] += 1
            coordinateCurrent = [coordinateCurrent[0] + coordVec[0], coordinateCurrent[1] + coordVec[1]]
            pass
    return coordL


if __name__ == "__main__":
    arr = file()
    array, largeX, largeY = getBoys(arr)
    coordList = []
    for i in range(1000):
        coordBoy = []
        for j in range(1000):
            coordBoy.append(0)
        coordList.append(coordBoy)
    for element in array:
        coordList = goInDirection(coordList, element)
    for i in coordList:
        print(i)
    num = 0
    for row in coordList:
        for point in row:
            if point >= 2:
                num += 1

    print(num)

