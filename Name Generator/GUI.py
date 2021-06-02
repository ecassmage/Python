import tkinter as tk
from tkinter import font as tkFont


class GUI:
    def __init__(self):
        self.tk = tk.Tk()
        self.font = tkFont.Font(family="Time New Roman", size=9)
        self.length = self.font.measure("Evan Morrison")
        # self.tk = tk.Frame()
        self.canvas = tk.Canvas(self.tk, width=2600, height=1400, bg='white')
        self.canvas.pack()
        self.labels = []
        self.lines = []
        # self.tk.pack()

    def update(self):
        self.tk.update()

    def newLabel(self, parent, message):
        tempLabel = Labels(self, self.tk, self.font, message)
        tempLabel.parentLabel = parent
        if tempLabel.parentLabel is not None:
            tempLabel.parentLabel.childLabel.append(self)
        self.labels.append(tempLabel)
        return tempLabel


class Labels:
    def __init__(self, gui, canvas, font, Message):
        self.parentLabel = None
        self.childLabels = []
        self.text = Message
        self.canvas = canvas
        self.gui = gui
        self.coord = ()
        self.label = tk.Label(self.canvas, text=Message, font=font)
        self.lengthSize = gui.font.measure(self.text)
        self.label.update()
        # self.label.grid(column=0, row=0)
        self.label.pack()
        self.measureLabel()

    def measureLabel(self):
        self.canvas.update()
        self.coord = (self.label.winfo_width(), self.label.winfo_height(), self.label.winfo_x(), self.label.winfo_y())
        # print(self.label.winfo_height())
        # print(self.coord)
