from AStar import Node
import IHatePain as IHateLaPain


class Matrix:
    def __init__(self, rows, columns):
        self.notNeededNodes = {}
        self.nodesToCheck = []
        self.visitedNodes = []
        self.matrix = []
        for _ in range(rows):
            matrix = []
            for _ in range(columns):
                matrix.append(None)
            self.matrix.append(matrix)

    def addNode(self, node, x, y):
        try:
            if self.matrix[x][y] is None:
                raise IndexError  # why?

            node.addAdjacent(self.matrix[x][y])
        except IndexError:
            pass

    def add(self, node):
        self.notNeededNodes.update({node: node.weight})
        self.matrix[node.coordinate[0]][node.coordinate[1]] = node
        self.addNode(node, node.coordinate[0] - 1, node.coordinate[1])
        self.addNode(node, node.coordinate[0] + 1, node.coordinate[1])
        self.addNode(node, node.coordinate[0], node.coordinate[1] - 1)
        self.addNode(node, node.coordinate[0], node.coordinate[1] + 1)

    def visited(self, node):
        self.nodesToCheck.pop(self.nodesToCheck.index(node))
        self.visitedNodes.append(node)
        for child in node.adjacentNodes:
            self.check(child)

    def check(self, node):
        if node in self.notNeededNodes:
            del(self.notNeededNodes[node])
            self.nodesToCheck.append(node)


def getGCost(self):
    return self.gCost


def getHCost(self):
    return self.hCost


def getweight(self):
    return self.weight


def getval(self):
    return self.fCostVal


def printMatrix(matrix, arrayOfHits, attribute=getweight):
    for coords in matrix.matrix:
        print("[", end='')
        for number, node in enumerate(coords):
            if number != 0:
                if attribute == getweight:
                    print(", ", end='')
                else:
                    print(", \t", end='')
            if node.coordinate not in arrayOfHits:
                print(attribute(node), end='')
            else:
                print(attribute(node) if attribute is not getweight else 0, end='')
        if attribute != getweight:
            print("\t", end='')
        print("]")


def iterate(matrix, TopLeft, BottomRight):
    currentNode = TopLeft
    currentNode.Visited = True
    TopLeft.distanceFromStart = 0
    TopLeft.setHCost()
    currentNode.updateChildren()
    matrix.check(currentNode)  # point of this being that I am too lazy to set up a system to account for the first node. However I am not too lazy to write this entire section which would have taken a similar amount of time probably.
    matrix.visited(currentNode)

    while currentNode != BottomRight:
        shortestChild = None
        collisions = []
        for child in matrix.nodesToCheck:
            if shortestChild is None or child.fCost() < shortestChild.fCost():
                shortestChild = child
                collisions = []
            elif child.fCost() == shortestChild.fCost():
                collisions.append(child)

        if len(collisions) != 0:
            for collision in collisions:
                if collision.hCost < shortestChild.hCost:
                    shortestChild = collision
        # print(f"{shortestChild}: weight: {shortestChild.weight}, coord: {shortestChild.coordinate},\t value: {shortestChild.fCostVal}")
        shortestChild.Visited = True
        shortestChild.updateChildren()
        matrix.visited(shortestChild)
        currentNode = shortestChild

    summed = 0
    arrayOfHit = []
    while currentNode != TopLeft:
        summed += currentNode.weight
        arrayOfHit.append(currentNode.coordinate)
        currentNode = currentNode.closestParent
    arrayOfHit.append((0, 0))

    # printMatrix(matrix, arrayOfHit)
    # print()
    # printMatrix(matrix, arrayOfHit, getGCost)
    # print()
    # printMatrix(matrix, arrayOfHit, getHCost)
    # print()
    # printMatrix(matrix, arrayOfHit, getval)
    return summed


def part1(string):
    topLeft = None
    bottomRight = None
    openedFile = open(string)
    lines = list(openedFile.readlines())
    openedFile.close()

    matrixTemp = []
    for row in lines:
        matrixRow = []
        for node in list(row.strip()):
            matrixRow.append(int(node))
        matrixTemp.append(matrixRow)
    # matrixTemp = IHateLaPain.main(matrixTemp, 5, 5)
    matrix = Matrix(len(matrixTemp), len(matrixTemp[0]))
    for numR, line in enumerate(matrixTemp):
        for numC, num in enumerate(line):
            node = Node(int(num), (numR, numC))
            if numR == 0 and numC == 0:
                topLeft = node
            bottomRight = node
            matrix.add(node)

    for line in matrix.matrix:
        for node in line:
            node.TargetNode = bottomRight
    return iterate(matrix, topLeft, bottomRight)


def part2(string):
    topLeft = None
    bottomRight = None
    openedFile = open(string)
    lines = list(openedFile.readlines())
    openedFile.close()

    matrixTemp = []
    for row in lines:
        matrixRow = []
        for node in list(row.strip()):
            matrixRow.append(int(node))
        matrixTemp.append(matrixRow)
    matrixTemp = IHateLaPain.main(matrixTemp, 5, 5)
    matrix = Matrix(len(matrixTemp), len(matrixTemp[0]))
    for numR, line in enumerate(matrixTemp):
        for numC, num in enumerate(line):
            node = Node(int(num), (numR, numC))
            if numR == 0 and numC == 0:
                topLeft = node
            bottomRight = node
            matrix.add(node)

    for line in matrix.matrix:
        for node in line:
            node.TargetNode = bottomRight
    return iterate(matrix, topLeft, bottomRight)


if __name__ == '__main__':
    print(f"Part1: {part1('input.txt')}")
    print(f"Part2: {part2('input.txt')}")
    pass

# 656
