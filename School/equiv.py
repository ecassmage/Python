def getSizeOfInt(integer):
    string = str(integer)
    sumTemp = 0
    for char in string:
        sumTemp += int(char)
    return sumTemp


def classEquiv(lowerRange=0, upperRange=25):
    classNums = []
    equalityNum = 5
    for i in range(upperRange):
        string = str(i)
        sumTemp = 0
        for num in string:
            sumTemp += int(num)
        if sumTemp == equalityNum:
            classNums.append(i)
    return classNums


def equiv(lowerRange=0, upperRange=25):
    classNums = []
    equalityNum = 5
    for i in range(lowerRange, upperRange):
        iNum = getSizeOfInt(i)
        for j in range(lowerRange, upperRange):
            if iNum == getSizeOfInt(j):
                classNums.append([i, j])
    return classNums


def equivStatic(array):
    classNums = []
    equalityNum = 5
    for i in array:
        iNum = getSizeOfInt(i)
        for j in array:
            if iNum == getSizeOfInt(j):
                classNums.append([i, j])
    return classNums


if __name__ == "__main__":
    # print(classEquiv(25))
    # print(equiv(0, 12))
    print(equivStatic([0, 1, 2, 3, 10, 11, 12]))
