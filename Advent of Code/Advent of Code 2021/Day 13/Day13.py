charMatch = "#"
charOther = "."


def matrixBuild(X, Y):
    matrix = []
    for _ in range(Y):
        matrixRow = []
        for _ in range(X):
            matrixRow.append(charOther)
        matrix.append(matrixRow)
    return matrix


def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()


def XFold(matrix, X):
    newMatrix = matrixBuild(X, len(matrix))
    for row in range(len(matrix)):
        for col, val in enumerate(matrix[row]):
            if col < X and val == charMatch:
                newMatrix[row][col] = val
            elif col == X:
                continue
            elif val == charMatch:
                try:
                    newMatrix[row][X - (col - X)] = val
                except IndexError:
                    continue
    return newMatrix


def YFold(matrix, Y):
    newMatrix = matrixBuild(len(matrix[0]), Y)
    for row in range(len(matrix)):
        if row < Y:
            for col, val in enumerate(matrix[row]):
                if val == charMatch:
                    newMatrix[row][col] = val
        elif row == Y:
            continue
        else:
            for col, val in enumerate(matrix[row]):
                if val == charMatch:
                    try:
                        newMatrix[Y - (row - Y)][col] = val
                    except IndexError:
                        continue

    # print(remove)
    return newMatrix


def daCount(matrix):
    num = 0
    for row in matrix:
        for cell in row:
            if cell == 1:
                num += 1
    return num


def main(string):
    largestX, largestY = 0, 0
    coordinates = []
    folds = []
    for line in open(string):
        if line.find("fold along x=") != -1:
            folds.append((int(line.strip().replace("fold along x=", "")), 0))
        elif line.find("fold along y=") != -1:
            folds.append((0, int(line.strip().replace("fold along y=", ""))))
        elif len(line.strip().split(",")) == 2:
            coord = line.strip().split(",")
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
            if coord[0] > largestX:
                largestX = coord[0]
            if coord[1] > largestY:
                largestY = coord[1]
            coordinates.append(coord)
    matrix = matrixBuild(largestX+1, largestY+1)
    for coordinateSet in coordinates:
        matrix[coordinateSet[1]][coordinateSet[0]] = charMatch
    # print(coordinates)
    # print(fold)
    # print(largestX)
    # print(largestY)
    # printMatrix(matrix)
    # matrix = YFold(matrix, 7)
    for fold in folds:
        if fold[0] == 0:
            matrix = YFold(matrix, fold[1])
        elif fold[1] == 0:
            matrix = XFold(matrix, fold[0])
    # printMatrix(matrix)
    # matrix = XFold(matrix, 5)
    printMatrix(matrix)
    print(daCount(matrix))


if __name__ == '__main__':
    main("input.txt")
