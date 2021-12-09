class Node:
    def __init__(self, number):
        self.up = None
        self.down = None
        self.left = None
        self.right = None

        self.number = number
        self.Basin = None

    def isBasin(self):
        if self.Basin is None:
            self.Basin = all([self.checkDirection(self.up, Basin=True), self.checkDirection(self.down, Basin=True), self.checkDirection(self.left, Basin=True), self.checkDirection(self.right, Basin=True)])
        return self.Basin

    def checkDirection(self, direction, Basin=False):
        if Basin:
            return direction is None or direction.number > self.number
        return direction is None or direction.number >= self.number

    def isSloped(self, listOfChecked=None):
        if listOfChecked is None:
            listOfChecked = []
        if self.up not in listOfChecked and not self.checkDirection(self.up):
            return False
        if self.down not in listOfChecked and not self.checkDirection(self.down):
            return False
        if self.left not in listOfChecked and not self.checkDirection(self.left):
            return False
        if self.right not in listOfChecked and not self.checkDirection(self.right):
            return False
        return True


class HeightMap:

    def __init__(self, matrix, peak=9):
        self.matrix = []
        self.peak = peak
        self.__setUpMatrix__(matrix)
        pass  # This will be pointless to have, but I want to complete it none the less.

    def __setUpMatrix__(self, matrix):

        for rowNumber in range(len(matrix)):
            matrixRow = []
            for colNumber, col in enumerate(matrix[rowNumber]):
                node = Node(col)

                if rowNumber != 0:
                    try:
                        node.up = self.matrix[rowNumber - 1][colNumber]
                        self.matrix[rowNumber - 1][colNumber].down = node
                    except IndexError:
                        pass

                if colNumber != 0:
                    try:
                        node.left = matrixRow[-1]
                        matrixRow[-1].right = node
                    except IndexError:
                        pass

                matrixRow.append(node)

            self.matrix.append(matrixRow)
