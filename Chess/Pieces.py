# import tkinter as tk


class Piece:
    def __init__(self, window, color, x, y):
        """(x, y)"""
        self.window = window
        self.x, self.y = x, y
        self.color = color


class King(Piece):
    def __init__(self, *args):
        Piece.__init__(self, *args)
        self.points = 500
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.repetition = False


class Queen(Piece):
    def __init__(self, *args):
        Piece.__init__(self, *args)
        self.points = 100
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.repetition = True


class Bishop(Piece):
    def __init__(self, *args):
        Piece.__init__(self, *args)
        self.points = 45
        self.moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.repetition = True


class Knight(Piece):
    def __init__(self, *args):
        Piece.__init__(self, *args)
        self.points = 65
        self.moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        self.repetition = False


class Rook(Piece):
    def __init__(self, *args):
        Piece.__init__(self, *args)
        self.points = 40
        self.moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        self.repetition = True


class Pawn(Piece):
    def __init__(self, *args):
        Piece.__init__(self, *args)
        self.points = 10
        self.moves = [(1, 0)]
        self.special = [(1, 0), (2, 0)]
        self.attack = [(1, -1), (1, 1)]
        self.repetition = False
        self.hasMoved = False
