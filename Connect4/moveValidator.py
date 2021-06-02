def moveLegal(board, column):
    if 0 <= column < len(board[0]) and board[0][column] == " ":
        return True
    return False


def isSpaceAvailable(board):
    if " " in board[0]:
        return True
    return False


def findRow(board, column, row=0):
    if board[row][column] == " ":
        return findRow(board, column, row + 1)
    return row


def placePieceOntoBoard(board, column, piece, row=0):
    if row+1 >= len(board) or board[row+1][column] != " ":
        board[row][column] = piece
        return row
    else:
        return placePieceOntoBoard(board, column, piece, row+1)


def coordInBounds(board, coord):
    if 0 <= coord[0] < len(board) and 0 <= coord[1] < len(board[0]):
        return True
    return False


def checkAdjacencies(board, piece, startPoint, direction, move):
    newCoord = (startPoint[0] + direction[0], startPoint[1] + direction[1])
    if coordInBounds(board, newCoord) and board[newCoord[0]][newCoord[1]] == piece and move < 3:
        return checkAdjacencies(board, piece, newCoord, direction, move + 1)
    return move


def bestPoint(directionPoints, largest=False):
    largestPoint = 0
    for points in range(0, 8, 2):
        if 1 + directionPoints[points] + directionPoints[points + 1] > largestPoint:
            largestPoint = 1 + directionPoints[points] + directionPoints[points + 1]
        if 1 + directionPoints[points] + directionPoints[points + 1] >= 4:
            return True
    if largest:
        return largestPoint
    return False


def checkBoardVictoryStatus(board, victoryPiece, ai=False, aiCoord=None):
    directions = [(-1, -1), (1, 1), (-1, 0), (1, 0), (-1, 1), (1, -1), (0, -1), (0, 1)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == victoryPiece:
                directionPoints = [0] * 8
                for pickle, slimyPickle in enumerate(directions):
                    directionPoints[pickle] = checkAdjacencies(board, victoryPiece, (i, j), slimyPickle, 0)
                if bestPoint(directionPoints):
                    if ai:
                        return True, 4
                    return True

    if ai:
        directionPoints = [0] * 8
        for num, direction in enumerate(directions):
            directionPoints[num] = checkAdjacencies(board, victoryPiece, aiCoord, direction, 0)
        points = bestPoint(directionPoints, largest=True)
        return False, points
    return False
