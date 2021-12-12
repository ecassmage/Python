import copy


class Node:
    def __init__(self, number):
        self.number = int(number)
        self.flashed = False

    def addNum(self, num=1):
        self.number += num

    def iterate(self, flash=True):
        self.addNum()
        if flash:
            self.flashed = True

    def canFlash(self):
        return self.number > 9 and not self.flash()

    def flash(self):
        if self.flashed:
            return False
        return True

    def isZero(self):
        if self.number > 9:
            self.number = 0

    def reset(self):
        self.flashed = False


def adjacent(matrix, coordinate, listOfFinished=None):
    if listOfFinished is None:
        listOfFinished = []

    if not matrix[coordinate[0]][coordinate[1]].canFlash():
        return
    directions = [(-1, -1), (1, 1), (-1, 0), (1, 0), (-1, 1), (1, -1), (0, -1), (0, 1)]
    for x, y in directions:
        if 0 <= coordinate[0] + x < len(matrix) and 0 <= coordinate[1] + y < len(matrix[0]):
            matrix[coordinate[0] + x][coordinate[1] + y].iterate(False)
            listOfFinished.append([coordinate[0], coordinate[1]])
            if matrix[coordinate[0] + x][coordinate[1] + y].number == 10:
                adjacent(matrix, [coordinate[0] + x, coordinate[1] + y], listOfFinished)


def getNums(row):
    return [node.number for node in row]


def setTo0(matrix):
    num = 0
    for RN in range(len(matrix)):
        for CN in range(len(matrix[RN])):
            if matrix[RN][CN].number > 9:
                num += 1
                matrix[RN][CN].number = 0
            matrix[RN][CN].reset()
    return num


def part2(matrix):
    num = 0
    while True:
        num += 1
        for RN in range(len(matrix)):
            for CN in range(len(matrix[RN])):
                matrix[RN][CN].iterate()
                if matrix[RN][CN].canFlash():
                    adjacent(matrix, [RN, CN])
        numero = setTo0(matrix)
        if numero == len(matrix) * len(matrix[0]):
            return num
    pass


def iteration(matrix, number):
    num = 0
    if number == -1:
        return part2(matrix)

    for _ in range(number):
        # for line in matrix:
        #     print(getNums(line))
        for RN in range(len(matrix)):
            for CN in range(len(matrix[RN])):
                matrix[RN][CN].iterate()
                if matrix[RN][CN].canFlash():
                    adjacent(matrix, [RN, CN])
        numero = setTo0(matrix)
        # print(numero)
        # print()
        num += numero
    return num
    pass


def main():
    matrix = []
    for row in open("input.txt"):
        rowM = []
        for number in list(row.strip()):
            rowM.append(Node(number))
        matrix.append(rowM)

    matrixCopy = copy.deepcopy(matrix)
    print(iteration(matrix, 100))
    print(iteration(matrixCopy, -1))


if __name__ == '__main__':
    main()
    pass
