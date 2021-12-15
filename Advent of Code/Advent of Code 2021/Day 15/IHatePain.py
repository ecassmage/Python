def copyMatrixSet(matrix, copies):
    masterList = matrix

    for i in range(copies):
        newMatrix = []
        for row in matrix:
            newMatrixRow = []
            for node in row:
                newMatrixRow.append(node+1 - 9 if (node + 1) > 9 else node+1)
            newMatrix.append(newMatrixRow)
        masterList += newMatrix
        matrix = newMatrix
    return masterList


def copyRow(matrix, copies):
    matrixNew = []
    for row in matrix:
        matrixRow = []
        for i in range(copies):
            for node in row:
                matrixRow.append(node+i - 9 if (node + i) > 9 else node+i)
        matrixNew.append(matrixRow)
    return matrixNew


def main(basicMatrix, copyCountRow, copyCountCol):
    return copyMatrixSet(copyRow(basicMatrix, copyCountRow), copyCountCol-1)


if __name__ == '__main__':
    # main(0, 0, 0)
    pass
