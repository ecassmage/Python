from PIL import ImageTk, Image


class Cell:
    def __init__(self, canvas, mineStatus):
        self.Canvas = canvas
        self.img = Image.open("Images\\Mine.png") if mineStatus else None
        self.coordinates = []
        pass


if __name__ == "__main__":
    C = Cell(None, True)

