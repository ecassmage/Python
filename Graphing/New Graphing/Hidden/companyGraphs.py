import tkinter as tk
import time
from multiprocessing import Pool


class Graph:
    def __init__(self):
        self.win = tk.Tk()
        self.window = tk.Canvas(self.win, width=1000, height=1000, bg='grey')
        self.window.pack()
        self.nodes = [Node(0, 1000)]
        self.lines = []
        self.y = 1000

    def move(self, x):
        self.newNode(x)
        for node in self.nodes:
            node.move()
        for line in self.lines:
            line.move()

    def newNode(self, x):
        if x % 10 == 0:
            self.y -= 1

        if x > 1000:
            tempNode = self.nodes[0]
            tempLine = self.lines[0]
            self.lines.pop(0)
            self.nodes.pop(0)
            tempLine.start = self.nodes[-1]
            tempNode.x = x
            tempNode.y = self.y
            tempLine.end = tempNode
            self.lines.append(tempLine)
            self.nodes.append(tempNode)
        else:
            newNode = Node(x, self.y)
            self.lines.append(Line(self.window, self.nodes[-1], newNode))
            self.nodes.append(newNode)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x -= 5


class Line:
    def __init__(self, window, start, end):
        self.window = window
        self.start = start
        self.end = end
        self.line = self.window.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill='orange')

    def move(self):
        self.window.coords(self.line, self.start.x, self.start.y, self.end.x, self.end.y)


def loopFunc(null):
    startTrue = time.time()
    gph = Graph()
    for start in range(6000):
        # start = time.time()
        gph.move(start)
        gph.win.update()
        # print(f"Time: {time.time() - start}")
    # timeStore.append(time.time() - startTrue)
    timeStoreTemp = (time.time() - startTrue)
    gph.window.delete('all')
    del gph
    return timeStoreTemp


if __name__ == '__main__':
    timeStore = []
    # iterate = [0, 1, 2]
    # with Pool(processes=3) as p:
    #     timeStore = p.map(loopFunc, iterate)
    timeStore.append(loopFunc(0))
    print(timeStore)
    temp = 0
    for i in timeStore:
        temp += i
    # print(temp/len(iterate))
    print(temp/1)
