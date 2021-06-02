from tkinter import *
import random
import math
import time
import json
settings = json.load(open("settings.json", "r"))


class Graph:
    def __init__(self):
        self.winShares = Tk()
        self.windowShares = Canvas(
            self.winShares,
            width=settings['window']['width'],
            height=settings['window']['height'],
            bg='black'
        )
        self.winMarket = Tk()
        self.windowMarket = Canvas(
            self.winMarket,
            width=settings['window']['width'],
            height=settings['window']['height'],
            bg='black'
        )
        self.companies = []
        self.xMax, self.yMax = 1, 300
        self.xMin, self.yMin = 0, 0
        self.windowShares.pack()
        self.windowMarket.pack()

    def findRange(self, smallest, largest, year):
        self.scalingRanges()
        for company in reversed(self.companies):
            company.newNode()
            for node in company.nodes:
                node.changePosition(self.xMax, self.yMax, self.yMax, company.shares)
            for line in reversed(company.lines):
                if line.moveCoord() is False:
                    company.nodes.pop(company.nodes.index(line.start))
                    company.lines.pop(company.lines.index(line))
                    self.windowShares.delete(line)
                    del line
            if company.marketCap <= 0 and company.operational:
                company.bankruptcy()
            if len(company.nodes) == 0:
                del company
        return

    def scalingRanges(self):
        for company in self.companies:
            if company.xMax > self.xMax:
                self.xMax = company.xMax
            if company.yMax > self.yMax:
                self.yMax = company.yMax
            if company.xMin < self.xMin:
                self.xMin = company.xMin
            if company.yMin > self.yMin:
                self.yMin = company.yMin


class Node:
    def __init__(self, window, x, y, year, value):
        self.window = window
        self.x, self.y = 2400, y
        self.marketValue = value
        self.corners = [self.x - 5, self.y - 5, self.x + 5, self.y + 5]
        self.year = year

    def changePosition(self, maxX, maxY, minY, shares):
        self.x -= math.ceil(settings['window']['width'] / settings['length'])
        self.y = (
                (settings['window']['height']) -
                math.ceil(((self.marketValue / shares) / maxY) * settings['window']['height'])
        )


class Lines:
    def __init__(self, window, start, end, color):
        self.window = window
        self.start = start
        self.end = end
        self.line = self.window.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color)

    def moveCoord(self):
        self.window.coords(self.line, self.start.x, self.start.y, self.end.x, self.end.y)
        if self.end.x <= 0:
            return False
        return True


class Company:

    pStates = {
        'incredible': 10,
        'excellent': 8,
        'good': 3,
        'normal': 0,
        'bad': -3,
        'horrible': -5,
        'horrendous': -8,
    }  # Possible States

    def __init__(self, window, market, shares, year, color):
        self.name = self.nameGeneration()
        self.operational = True
        self.window = window
        self.color = color
        self.marketCap = market
        self.currentValue = market/shares
        self.yearCreated = year
        self.yearCurrent = year
        self.shares = shares
        self.state = 'normal'
        self.nodes = [Node(self.window, 0, 10, year, market)]
        self.lines = []
        self.xMax, self.yMax = year, market / shares
        self.xMin, self.yMin = 0, 1000

    @staticmethod
    def nameGeneration():
        letters = list('abcdefghijklmnopqrstuvwxyz')
        name = ''
        for i in range(random.randrange(3, 6)):
            name += letters[random.randrange(len(letters))]
        return name

    def changeMarketCap(self, growth):
        self.marketCap += ((self.marketCap * growth) + 100)

    def scaleChange(self):
        if self.yMax < math.ceil(self.currentValue * 1.02):
            self.yMax = math.ceil(self.currentValue * 1.02)
        if self.currentValue - 25 < self.yMin:
            self.yMin = self.currentValue - 25
        self.xMax += 1

    def yearlyChange(self):
        chosen = random.randrange(100)
        temp_list = list(self.pStates)
        if chosen >= 90:
            if not (temp_list.index(self.state) == 0):
                self.state = temp_list[temp_list.index(self.state) - 1]
        elif chosen <= 9:
            if not (temp_list.index(self.state) == (len(temp_list) - 1)):
                self.state = temp_list[temp_list.index(self.state) + 1]
        chosen += self.pStates[self.state]
        change = ((chosen - 50) / settings['multiplier']) ** 2 / 100 ** 2
        if chosen < 25:
            change *= -1
        return change

    def newNode(self):
        self.yearCurrent += 1
        if self.operational:
            growth = self.yearlyChange()
            self.changeMarketCap(growth)
            self.stockSplit()
            self.currentValue = self.marketCap / self.shares  # Just for Human Understanding in Debugger
            node = Node(self.window, 0, 0, self.yearCurrent, self.marketCap)
            self.lines.append(Lines(self.window, self.nodes[-1], node, self.color))
            self.nodes.append(node)
        self.scaleChange()

    def stockSplit(self):
        if self.marketCap / self.shares >= 1000:
            self.shares *= 4
            self.yMax = math.ceil(self.yMax / 4)

    def bankruptcy(self):
        print(
            f"\nCompany existed from "
            f"{self.yearCreated} to "
            f"{self.yearCurrent} making it "
            f"{self.yearCurrent - self.yearCreated}")
        self.operational = False


def main():
    gph = Graph()
    for year in range(10000):
        print(f"Year: {year}")
        time.sleep(1/settings['speed'])
        gph.findRange(0, 1000000, year)
        gph.windowShares.update()
        if year % settings["newCompany"] == 0:
            colors = ['red', 'purple', 'green', 'white', 'blue', 'pink', 'orange', 'yellow', 'grey']
            gph.companies.append(Company(gph.windowShares, 10000, 10, year, random.choice(colors)))
    exit()
    mainloop()


if __name__ == '__main__':
    main()


"""
Problem 1: Once a company dies no Nodes are modified after that
"""