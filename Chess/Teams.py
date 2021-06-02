import tkinter as tk
import Pieces
import json
settings = json.load(open("settings.json", 'r'))


class Board:
    def __init__(self):
        self.tkWindow = tk.Tk()
        self.window = tk.Canvas(
            self.tkWindow, width=settings['window']['width'], height=settings['window']['height'], bg='peach puff')
        self.window.pack()
        self.team1 = makeTeam(self.window, settings['teams']['team1']['color'], 'top')
        self.team2 = makeTeam(self.window, settings['teams']['team2']['color'], 'bottom')
        self.turn = 'team1'
        self.coordBoard = computerBoard()


class ChessTeam:
    def __init__(self, window, color):
        self.window = window
        self.color = color
        self.pieces = []


def computerBoard():
    board = []
    for y in range(8):
        row = []
        for x in range(8):
            row.append((x, y))
        board.append(row)
    return board


def makeTeam(window, color, side):
    if side == 'top':

        team = ChessTeam(window, color)

        team.pieces.append(Pieces.Rook(window, color, 0, 0))
        team.pieces.append(Pieces.Knight(window, color, 1, 0))
        team.pieces.append(Pieces.Bishop(window, color, 2, 0))
        team.pieces.append(Pieces.King(window, color, 3, 0))
        team.pieces.append(Pieces.Queen(window, color, 4, 0))
        team.pieces.append(Pieces.Bishop(window, color, 5, 0))
        team.pieces.append(Pieces.Knight(window, color, 6, 0))
        team.pieces.append(Pieces.Rook(window, color, 6, 0))

        for x in range(8):
            team.pieces.append(Pieces.Pawn(window, color, x, 1))

        return team

    elif side == 'bottom':

        team = ChessTeam(window, color)

        team.pieces.append(Pieces.Rook(window, color, 0, 7))
        team.pieces.append(Pieces.Knight(window, color, 1, 7))
        team.pieces.append(Pieces.Bishop(window, color, 2, 7))
        team.pieces.append(Pieces.Queen(window, color, 3, 7))
        team.pieces.append(Pieces.King(window, color, 4, 7))
        team.pieces.append(Pieces.Bishop(window, color, 5, 7))
        team.pieces.append(Pieces.Knight(window, color, 6, 7))
        team.pieces.append(Pieces.Rook(window, color, 6, 7))

        for x in range(8):
            team.pieces.append(Pieces.Pawn(window, color, x, 6))

        return team


if __name__ == "__main__":
    a = Board()
    a.tkWindow.mainloop()
    pass
