import re


def getFile():
    listReturn = []
    for lineHere in open("input.txt"):
        listReturn.append(re.findall("[0-9]+", lineHere))
    return listReturn


def bingo(boardPlay):
    for row in boardPlay:
        for letter in row:
            if letter[0] != "_":
                break
        else:
            return True
    for i in range(len(boardPlay[0])):
        for j in range(len(boardPlay)):
            if boardPlay[j][i][0] != "_":
                break
        else:
            return True
    return False


def switchMatches(newBoards, num):
    for newBoard in newBoards:
        for row in newBoard:
            for i in range(len(row)):
                if row[i] == num:
                    row[i] = "_" + row[i]


if __name__ == "__main__":
    arr = getFile()
    lineNums = arr[0]
    boards = []
    board = []
    winner = []
    for line in range(1, len(arr)):
        match arr[line]:
            case []:
                if len(board) == 0:
                    continue
                boards.append(board)
                board = []
            case _:
                board.append(arr[line])
                pass
    winningNum = 0
    latestToWin = None
    for number in lineNums:
        switchMatches(boards, number)
        for thisBoardNum in reversed(range(len(boards))):
            if bingo(boards[thisBoardNum]):
                winner = boards[thisBoardNum]
                winningNum = int(number)
                latestToWin = boards.pop(boards.index(winner))
        else:
            continue

    print(latestToWin)
    sumOf = 0
    for rowW in range(len(latestToWin)):
        for colW in range(len(latestToWin[rowW])):
            if latestToWin[rowW][colW][0] != "_":
                sumOf += int(winner[rowW][colW])
            # winner[rowW][colW] = winner[rowW][colW].replace("_", "")
    print(sumOf * winningNum)
    pass
