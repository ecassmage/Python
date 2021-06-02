import copy
import random
import moveValidator
import configReader
settings = configReader.readSettings()


def AIBrain(updateWindow, board, piece, recursionBasicState, recursionDepth):
    updateWindow.tkwindow.update()
    totalPointsPerMove = []
    for move in range(len(board[0])):
        pointsThisMove = 0
        copyBoard = copy.deepcopy(board)

        if moveValidator.moveLegal(copyBoard, move):
            row = moveValidator.placePieceOntoBoard(copyBoard, move, piece)
            pointsThisMove += 5
        else:
            totalPointsPerMove.append(-1000)
            continue
        tempCoord = (row, move)
        truth, points = moveValidator.checkBoardVictoryStatus(copyBoard, piece, True, tempCoord)
        if truth:
            pointsThisMove += 100

        pointsThisMove += 3 ** points

        if recursionDepth > 0:

            if piece == 'X':
                newPiece = 'O'
            else:
                newPiece = 'X'
            worstMove = AIBrain(updateWindow, copyBoard, newPiece, recursionBasicState, recursionDepth - 1)
            pointsThisMove -= (worstMove / (1 + recursionBasicState - recursionDepth))

        totalPointsPerMove.append(pointsThisMove)
    largestPointNum = totalPointsPerMove[0]
    for number, points in enumerate(totalPointsPerMove):
        if points > largestPointNum:
            largestPointNum = points

    if recursionDepth == recursionBasicState:
        listOfAcceptableMoves = []
        for number, move in enumerate(totalPointsPerMove):
            if move == largestPointNum:
                listOfAcceptableMoves.append(number)
        return random.choice(listOfAcceptableMoves)
    else:
        return largestPointNum


def main():
    boardList = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    cpyList = copy.deepcopy(boardList)
    listOfWins = [0, 0, 0]
    for loop in range(1000):
        X = 2
        for i in range(20):
            column = AIBrain(boardList, "X", 0, 0)
            if moveValidator.moveLegal(boardList, column):
                moveValidator.placePieceOntoBoard(boardList, column, "X")
            # for j in boardList:
            #     print(j)
            # print()
            if moveValidator.checkBoardVictoryStatus(boardList, "X"):
                X = 1
                print("X Wins:", moveValidator.checkBoardVictoryStatus(boardList, "X"))
                break
            column = AIBrain(boardList, "O", 3, 3)
            if moveValidator.moveLegal(boardList, column):
                moveValidator.placePieceOntoBoard(boardList, column, "O")
            # for j in boardList:
            #     print(j)
            # print()
            if moveValidator.checkBoardVictoryStatus(boardList, "O"):
                X = 0
                print("O Wins:", moveValidator.checkBoardVictoryStatus(boardList, "O"))
                break

        if X == 1:
            listOfWins[0] += 1
        elif X == 0:
            listOfWins[1] += 1
        else:
            listOfWins[2] += 1

        boardList = copy.deepcopy(cpyList)
    print(f"\n"
          f"X Wins: {listOfWins[0]} games\n"
          f"O Wins: {listOfWins[1]} games\n"
          f"There were {listOfWins[2]} Ties"
          f"\n")
    return


if __name__ == "__main__":
    main()
