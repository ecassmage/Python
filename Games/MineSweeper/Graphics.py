import tkinter as tk
from Settings import JOpen
from win32api import GetSystemMetrics
import GameInformationObject as GIO  # This is to store Game Information
import math


class Graphics:
    def __init__(self):
        self.GraphicsSettings = JOpen.JOpen("GraphicsSettings.json")
        self.GameInfo = GIO.GameInformation()

        self.Resolution = {"Width": self.GraphicsSettings["Resolution"]["Width"], "Height": self.GraphicsSettings["Resolution"]["Height"]}
        self.__setDimensions()
        self.findRatio()
        # self.CellDimensions = {"Width": tempGraphicsSettings["Cells"]["Width"], "Height": tempGraphicsSettings["Cells"]["Height"]}

        self.tkArea = tk.Tk()
        self.tkArea.attributes('-fullscreen', True)
        self.Window = tk.Canvas(self.tkArea, width=self.Resolution["Width"], height=self.Resolution["Height"], bg=self.GraphicsSettings["Background Color"])

        self.lines = []

        self.__setGrid()
        self.__showScreen()

    def __showScreen(self):
        self.Window.pack()

    def __setDimensions(self):
        if self.Resolution["Width"] == 0 or self.Resolution["Width"] > GetSystemMetrics(0):  # To Fit the Screen
            self.Resolution["Width"] = GetSystemMetrics(0)
        if self.Resolution["Height"] == 0 or self.Resolution["Height"] > GetSystemMetrics(1):  # To Fit the Screen
            self.Resolution["Height"] = GetSystemMetrics(1)

    def findRatio(self):

        # If no ratio if found it will just end at the default resolution
        num1, num2 = 1, 1
        while num1 / num2 != self.Resolution["Width"] / self.Resolution["Height"]:
            if num1 / num2 < self.Resolution["Width"] / self.Resolution["Height"]:
                num1 += 1
            else:
                num2 += 1
        return [num1, num2]

    def largestNumberMakingMinimumSquares(self, Squares):
        num = 1
        iteration = 1
        while (self.Resolution["Width"] / iteration) * (self.Resolution["Height"] / iteration) > Squares:
            if self.Resolution["Width"] / iteration == int(self.Resolution["Width"] / iteration) and self.Resolution["Height"] / iteration == int(self.Resolution["Height"] / iteration):
                num = iteration
            iteration += 1
        pass

    def __setGrid(self):
        ratio = self.findRatio()
        cells = self.GameInfo.GameDifficulty["Number of Mines"] / (self.GameInfo.GameDifficulty["Ratio"] / 100)
        self.largestNumberMakingMinimumSquares(cells)
        newWidth = None
        num = math.sqrt((self.Resolution["Width"] * self.Resolution["Height"]) / cells)
        width = self.Resolution["Width"] / math.sqrt((self.Resolution["Width"] * self.Resolution["Height"]) / cells)
        height = self.Resolution["Height"] / math.sqrt((self.Resolution["Width"] * self.Resolution["Height"]) / cells)
        for x in range(0, self.Resolution["Width"]+1, self.GraphicsSettings["Cell Size"]):
            self.addLine((x, 0), (x, self.Resolution["Height"]))
        for y in range(0, self.Resolution["Width"]+1, self.GraphicsSettings["Cell Size"]):
            self.addLine((0, y), (self.Resolution["Width"], y))
        pass

    def addLine(self, xy1: tuple, xy2: tuple):
        self.lines.append(self.Window.create_line(xy1[0], xy1[1], xy2[0], xy2[1], fill=self.GraphicsSettings["Line Color"], width=self.GraphicsSettings["Line Width"]))
        pass


if __name__ == '__main__':
    G = Graphics()
    G.tkArea.mainloop()
