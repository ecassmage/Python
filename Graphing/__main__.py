from tkinter import *
import random
import math
import time


class Node:
    def __init__(self, window, x, y, position, value):
        self.window = window
        self.x, self.y = x, y
        self.value = value
        self.corners = [self.x - 5, self.y - 5, self.x + 5, self.y + 5]
        # self.image = self.window.create_oval(self.corners, fill='white')
        self.position = position

    def changePosition(self, maxX, maxY):
        self.x = math.ceil((self.position / maxX) * 1000)
        self.y = math.ceil(1000 - (self.value / maxY) * 1000)


class Lines:
    def __init__(self, window, start, end):
        self.window = window
        self.start = start
        self.end = end
        self.line = self.window.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill='red')

    def moveCoord(self):
        self.window.coords(self.line, self.start.x, self.start.y, self.end.x, self.end.y)


class Graph:
    def __init__(self, start):
        self.currentX, self.currentY = 0, 1000
        self.win = Tk()
        self.window = Canvas(self.win, width=1000, height=1000, bg='black')
        self.window.pack()
        self.nodes = []
        self.lines = []
        self.xMin, self.yMin = 0, 0
        self.xMax, self.yMax = 0, math.ceil(start*1.02)
        self.prev = 'up'

    def randomNode(self):
        switchCase = {'up': [-1, 'down'], 'down': [1, 'up']}
        chosen = random.randrange(100)
        if self.prev == 'up':
            chosen += 5  # Global Improvement Bias
        if chosen >= 99:
            y = 7
        elif chosen >= 98:
            y = 6
        elif chosen >= 90:
            y = 5
        elif chosen >= 75:
            y = 4
        elif chosen >= 65:
            y = 3
        elif chosen >= 40:
            y = 2
        elif chosen >= 20:
            y = 1
        else:
            self.prev = switchCase[self.prev][1]
            y = random.randrange(1, 4)
        y *= switchCase[self.prev][0]
        return y

    def changeScale(self, displace):
        if self.yMax < math.ceil(displace * 1.02):
            self.yMax = math.ceil(displace * 1.02)
        if displace - 25 < self.yMin:
            self.yMin = displace - 25
        self.xMax += 1

    def newNode(self):
        displacement = self.randomNode()
        oldNewNode = self.nodes[-1]
        position = len(self.nodes) + 1
        self.changeScale(oldNewNode.value - displacement)
        # self, window, x, y, position, value

        newNode = Node(self.window, 0, 0, position, oldNewNode.value - displacement)
        self.nodes.append(newNode)
        self.lines.append(Lines(self.window, oldNewNode, newNode))


def main():
    graph = Graph(1000)
    # a = Node(graph.window, 100, 100)
    graph.nodes.append(Node(graph.window, graph.currentX, graph.currentY, 1, 100))
    graph.window.update()
    # a.window.coords(a.image, 750, 750, 775, 775)
    for i in range(1, 1000000):
        graph.newNode()
        for node in graph.nodes:
            node.changePosition(graph.xMax, graph.yMax)
        for line in graph.lines:
            line.moveCoord()
        graph.window.update()
        # time.sleep(1/30)
    graph.window.mainloop()
    return


if __name__ == '__main__':
    main()
