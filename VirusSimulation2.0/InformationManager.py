import tkinter as tk
import time
import mainShared


class InfoGUI:
    def __init__(self):
        self.tk = tk.Tk()
        self.width = 1000
        self.height = 1000
        self.graph = tk.Canvas(self.tk, width=self.width, height=self.height, bg='green')
        self.rectangles = []

        self.graph.pack()
        pass

    def newRectangle(self, removed: int, susceptible: int, infected: int):
        y = [self.height * (removed / sum([removed, susceptible, infected])), self.height * (susceptible / sum([removed, susceptible, infected])), self.height * (infected / sum([removed, susceptible, infected]))]
        xLengthPerRectangle = self.width / (len(self.rectangles) + 1)
        # self.graph.coords(lis[0], self.width - xLengthPerRectangle, 0, self.width, y[0])
        # self.graph.coords(lis[1], self.width - xLengthPerRectangle, y[0], self.width, y[0] + y[1])
        # self.graph.coords(lis[2], self.width - xLengthPerRectangle, y[0] + y[1], self.width, y[0] + y[1] + y[2])
        newRectangle1 = self.graph.create_rectangle(self.width-xLengthPerRectangle, 0, self.width, y[0], fill='grey', width=0)      # Removed
        newRectangle2 = self.graph.create_rectangle(self.width-xLengthPerRectangle, y[0], self.width, y[0] + y[1], fill='green', width=0)       # Susceptible
        newRectangle3 = self.graph.create_rectangle(self.width-xLengthPerRectangle, y[0] + y[1], self.width, y[0] + y[1] + y[2], fill='red', width=0)     # Infected

        for number, node in enumerate(self.rectangles):
            for rectangle in node:
                coord = self.graph.coords(rectangle)
                self.graph.coords(rectangle, xLengthPerRectangle * number, coord[1], (xLengthPerRectangle+1) * number, coord[3])

        self.rectangles.append([newRectangle1, newRectangle2, newRectangle3])

        self.tk.update()


class InfoMgr:
    def __init__(self):
        self.Susceptible = []
        self.Infected = []
        self.Removed = []
        self.Graph = InfoGUI()

    def newSet(self, newNode):  # -> [susceptible, infected, removed]
        # self.Susceptible.append(newNode[0])
        # self.Infected.append(newNode[1])
        # self.Removed.append(newNode[2])
        self.Graph.newRectangle(newNode[2], newNode[0], newNode[1])

    def countUpHumans(self, humanList: list):
        newNodeListCount = [0, 0, 0]
        for human in humanList:
            if human.infected:
                newNodeListCount[1] += 1
            elif human.immune:
                newNodeListCount[2] += 1
            else:
                newNodeListCount[0] += 1
        self.newSet(newNodeListCount)


def flipQueue(queue):
    temp = queue[0]
    queue[0] = queue[1]
    queue[1] = temp


def main(queue):
    Info = InfoMgr()
    flipQueue(queue)
    while True:
        startTimer = time.time()
        if not queue[1].empty():
            lis = queue[1].get()
            if lis == "QUIT":
                queue[0].put("Received")
                exit()
            Info.countUpHumans(lis)
        endTimer = time.time()
        time.sleep(mainShared.collectTime(startTimer, endTimer, 4, "INFORMATION", True))
