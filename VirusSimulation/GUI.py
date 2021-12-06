import tkinter as tk
import FileOpener


class GUI:
    def __init__(self, queue):

        self.stg = FileOpener.openStg()

        self.queue = queue
        self.tk = tk.Tk()
        self.win = tk.Canvas(self.tk, width=self.stg['window']['width'], height=self.stg['window']['height'])

        self.__initializeGraphics__()

    def __initializeGraphics__(self):
        self.win.pack()

    def checkCoordinates(self, Humans):
        if Humans is None:
            return

        for human in Humans:
            self.win.coords(human.id, human.coord[0]-human.size, human.coord[1]-human.size, human.coord[0]+human.size, human.coord[1]+human.size)
            self.win.itemconfig(human.id, fill=human.color)

    def update(self):
        self.tk.update()

    def mainloop(self):
        self.tk.mainloop()


if __name__ == '__main__':
    gui = GUI(0)
    gui.tk.mainloop()
    pass
