import GUI
import AI
import moveValidator
import math
import time
import configReader
settings = configReader.readSettings()


def getInt(message):
    while True:
        try:
            num = int(input(message))
        except ValueError:
            print("This is not a number")
            continue
        if type(num) != int:
            print("This is not a number")
        else:
            return num


def makeMove(gameMove):
    move = getInt("What number will you enter: ")
    if moveValidator.moveLegal(gameMove.board, move):
        moveValidator.placePieceOntoBoard(gameMove.board, 0, move, 'X')
        moveValidator.checkBoardVictoryStatus(gameMove.board, "X")
    for i in gameMove.board:
        print(i)
    return


def printBoard(board, boardObject=None, coord=None, printConsole=False, draw=False):
    if printConsole:
        for i in board:
            print(i)
        print()

    if draw:
        color = boardObject.teams[boardObject.currentTeam]['Color']
        team = boardObject.currentTeam
        boardObject.activatePiece(coord, color, team)


def playersMove(event, board):

    if board.teams[board.currentTeam]["AI"] or board.wonGame is not False:
        print("Wait Your Turn\n")
        return

    if board.pausedProgram:
        print("WE PAUSED")
        return

    quadrantSize = settings['window']['width'] / settings['board']['width']
    quadrant = math.floor(event.x / quadrantSize)
    if moveValidator.moveLegal(board.board, quadrant):
        row = moveValidator.placePieceOntoBoard(board.board, quadrant, board.teams[board.currentTeam]["Piece"])
        printBoard(board.board, board, (row, quadrant), draw=True)
        board.nextTurn = True
        if moveValidator.checkBoardVictoryStatus(board.board, board.teams[board.currentTeam]["Piece"]):
            board.wonGame = board.currentTeam
            return True
    return False
    # print(event.x)
    # print(board)


def aiMove(board, team):
    column = AI.AIBrain(board, board.board, team["Piece"], team['Difficulty'], team['Difficulty'])
    if settings['automatic']:
        for timing in range(int(60 * settings['time'])):
            time.sleep(1/60)
            board.tkwindow.update()
    if moveValidator.moveLegal(board.board, column):
        row = moveValidator.placePieceOntoBoard(board.board, column, team["Piece"])
        printBoard(board.board, board, (row, column), draw=True)
        board.nextTurn = True
        if moveValidator.checkBoardVictoryStatus(board.board, team["Piece"]):
            board.wonGame = board.currentTeam
            return True
        return False
    return False


def doYouWantAI(teams):
    yesResponse = ['yes', 'true', 1]
    for team in teams:
        response = input(f"Do you want {team} to be an AI: ")
        response = response.lower()
        if response in yesResponse:
            teams[team]["AI"] = True
        else:
            teams[team]["AI"] = False


def game(board):
    board.window.bind("<Button-1>", lambda event: playersMove(event, board))  # Maybe will need some Threading for this

    while board.wonGame is False:

        for team in board.teams:
            board.nextTurn = False
            board.currentTeam = team
            if moveValidator.isSpaceAvailable(board.board) is False:
                board.wonGame = "a Tie"
                return "a Tie"

            while board.nextTurn is False:

                if board.teams[team]["AI"]:
                    aiMove(board, board.teams[team])

                board.tkwindow.update()

                if board.quitProgram:
                    board.tkwindow.quit()
                    exit()

            if board.wonGame is not False:
                break

    return board.wonGame


def resetBoard(board):
    board.resetProgram()


# a.window.bind("<Button-1>", command=lambda: displayCoord(board))  # Maybe will need some Threading for this
def main():
    board = GUI.Canvas()
    doYouWantAI(board.teams)
    while True:
        winner = game(board)
        print(f"Winner is: {winner}")
        # resetBoard(board)
        while board.wonGame is not False:
            board.tkwindow.update()
            if settings['automatic']:
                printBoard(board.board, printConsole=True)
                resetBoard(board)
    # break


if __name__ == "__main__":
    main()
