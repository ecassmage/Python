import copy


class Node:
    def __init__(self, number):
        self.adjacent = []
        self.number = number
        self.pathWalked = 0
        self.pathLeft = 0
        pass

    def addAdjacent(self, new):
        if isinstance(new, list):
            for newElement in new:
                self.adjacent.append(newElement)
                newElement.adjacent.append(self)
        else:
            self.adjacent.append(new)
            new.adjacent.append(self)


class Matrix:
    def __init__(self, sizeRow, sizeCol):
        self.TopLeft = None
        self.matrix = []
        for _ in range(sizeRow):
            matrix = []
            for _ in range(sizeCol):
                matrix.append(None)
            self.matrix.append(matrix)
        self.lowestRisk = -1

    def addNode(self, node, x, y):
        try:
            if self.matrix[x][y] is None:
                raise IndexError  # why?

            node.addAdjacent(self.matrix[x][y])
        except IndexError:
            pass

    def add(self, node, x, y, topLeft=False):
        if topLeft:
            self.TopLeft = node
        self.matrix[x][y] = node
        self.addNode(node, x - 1, y)
        self.addNode(node, x + 1, y)
        self.addNode(node, x, y - 1)
        self.addNode(node, x, y + 1)


def lowest(lis):
    # small = [-1, None]
    # for num in lis:
    #     if small[0] == -1 or num[0] < small[0]:
    #         small = lis
    # return small
    small = -1
    for num in lis:
        if small == -1 or num < small:
            small = lis
    return small


def iteration(matrix, currentNode=None, listOfPassed=None):
    if currentNode is None:
        currentNode = matrix.TopLeft

    if listOfPassed is None:
        listOfPassed = []
    listOfPassed.append(currentNode)
    listOfNums = []
    for node in currentNode.adjacent:
        listOfNums.append(iteration(matrix, node, copy.copy(listOfPassed)))
    return lowest(listOfNums)


def main(string):
    matrixL = []
    for numR, line in enumerate(open(string)):
        MR = []
        for numC, num in enumerate(list(line.strip())):
            MR.append([numR, numC, num])
        matrixL.append(MR)
    matrix = Matrix(len(matrixL[0]), len(matrixL))
    for row in matrixL:
        for col in row:
            if col[0] == 0 and col[1] == 0:
                matrix.add(Node(col[2]), col[0], col[1], True)
            else:
                matrix.add(Node(col[2]), col[0], col[1])
    print(matrixL)


if __name__ == '__main__':
    main('test.txt')
    pass
