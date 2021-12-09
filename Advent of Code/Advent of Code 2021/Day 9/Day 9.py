def depthRevised(matrix, CurrentPosition, listOfCoordinates=None):
    if listOfCoordinates is None:
        listOfCoordinates = []

    number = matrix[CurrentPosition[0]][CurrentPosition[1]]
    if number == 9:
        return 0, listOfCoordinates
    if CurrentPosition[0] != 0:
        if matrix[CurrentPosition[0] - 1][CurrentPosition[1]] < number and [CurrentPosition[0] - 1, CurrentPosition[1]] not in listOfCoordinates:
            return 0, listOfCoordinates
    if CurrentPosition[0] != len(matrix) - 1:
        if matrix[CurrentPosition[0] + 1][CurrentPosition[1]] < number and [CurrentPosition[0] + 1, CurrentPosition[1]] not in listOfCoordinates:
            return 0, listOfCoordinates
    if CurrentPosition[1] != 0:
        if matrix[CurrentPosition[0]][CurrentPosition[1] - 1] < number and [CurrentPosition[0], CurrentPosition[1] - 1] not in listOfCoordinates:
            return 0, listOfCoordinates
    if CurrentPosition[1] != len(matrix[CurrentPosition[0]]) - 1:
        if matrix[CurrentPosition[0]][CurrentPosition[1] + 1] < number and [CurrentPosition[0], CurrentPosition[1] + 1] not in listOfCoordinates:
            return 0, listOfCoordinates
    listOfCoordinates.append(CurrentPosition)

    num1, num2, num3, num4 = 0, 0, 0, 0
    if CurrentPosition[0] != 0:  # Up
        if [CurrentPosition[0] - 1, CurrentPosition[1]] not in listOfCoordinates:
            num1, listOfCoordinates = depthRevised(matrix, [CurrentPosition[0] - 1, CurrentPosition[1]], listOfCoordinates)
    if CurrentPosition[0] != len(matrix) - 1:  # Down
        if [CurrentPosition[0] + 1, CurrentPosition[1]] not in listOfCoordinates:
            num2, listOfCoordinates = depthRevised(matrix, [CurrentPosition[0] + 1, CurrentPosition[1]], listOfCoordinates)
    if CurrentPosition[1] != 0:  # Left
        if [CurrentPosition[0], CurrentPosition[1] - 1] not in listOfCoordinates:
            num3, listOfCoordinates = depthRevised(matrix, [CurrentPosition[0], CurrentPosition[1] - 1], listOfCoordinates)
    if CurrentPosition[1] != len(matrix[CurrentPosition[0]]) - 1:  # Right
        if [CurrentPosition[0], CurrentPosition[1] + 1] not in listOfCoordinates:
            num4, listOfCoordinates = depthRevised(matrix, [CurrentPosition[0], CurrentPosition[1] + 1], listOfCoordinates)

    return sum([num1, num2, num3, num4]) + 1, listOfCoordinates


def main():
    matrix = []
    for line in open("input.txt"):
        lis = []
        for num in list(line.strip()):
            lis.append(int(num))
        matrix.append(lis)

    numArr = []
    for rNum in range(len(matrix)):
        for cNum, val, in enumerate(matrix[rNum]):
            lis = []
            num, lis = depthRevised(matrix, [rNum, cNum], lis)
            if num != 0:
                numArr.append([num, lis])
    numArr.sort(key=lambda x: x[0])
    pointsUsed = []
    summedNums = []
    for number, argument in reversed(numArr):
        for coordinate in argument:
            if coordinate in pointsUsed:
                break
        else:
            summedNums.append(number)
            if len(summedNums) == 3:
                break
    print(numArr[-1][0] * numArr[-2][0] * numArr[-3][0])


if __name__ == '__main__':
    main()
