from tkinter import *
import random
import math
import time
import json
import Stats
import numpy as np
import Colors
settings = json.load(open("settings.json", "r"))


class Graph:
    def __init__(self):
        # Shares Value Graphs GUI
        self.winShares = Tk()
        self.windowShares = Canvas(
            self.winShares,
            width=settings['window']['width'],
            height=settings['window']['height'],
            bg='black'
        )
        self.winShares.title("Share Price")
        self.companies = []
        self.companiesInactive = []
        self.xMaxS, self.yMaxS = 1, 0
        self.windowShares.pack()

        # Market Capital Graphs GUI
        self.winMarket = Tk()
        self.windowMarket = Canvas(
            self.winMarket,
            width=settings['window']['width'],
            height=settings['window']['height'],
            bg='black'
        )
        self.winMarket.title("Market Capital")
        self.yMaxMC = 0
        self.windowMarket.pack()
        self.statsCanada = Stats.main()

    def createCompanies(self):
        tempListCompanies = []
        for i in range(settings['maxCompanies']):
            tempListCompanies.append(
                Company(
                    self.windowShares, 0, 0, 0, 'red')
            )
        return tempListCompanies

    def findRange(self):
        self.scalingRanges()
        for company in reversed(self.companies):
            company.newNode()
            for node in company.nodes:
                node.changePosition(self, company)
            for line in reversed(company.lines):
                if line.moveCoord(company) is False:
                    self.cleanUp(line, company)
            if company.marketCap <= 0 and company.operational:
                company.bankruptcy()
            if len(company.lines) == 0:
                # company.windows[0].delete('all')
                for node in reversed(company.nodes):
                    del node
                self.companies.pop(self.companies.index(company))
                del company
        return

    def cleanUp(self, line, company):
        self.windowShares.delete(line)
        self.windowMarket.delete(line)
        # del company.nodes[company.nodes.index(line.start)]
        del line.start
        company.lines.pop(company.lines.index(line))
        del line

    def scalingRanges(self):
        for company in self.companies:
            if company.xMaxS > self.xMaxS:
                self.xMaxS = company.xMaxS
            if company.yMaxS > self.yMaxS:
                self.yMaxS = company.yMaxS
            if company.yMaxMC > self.yMaxMC:
                self.yMaxMC = company.yMaxMC


class Node:
    def __init__(self, year, value):
        self.active = True
        self.x = settings['window']['width']
        self.ySharePrice = 0
        self.yMarketCap = 0
        self.marketValue = value
        self.year = year

    def changePosition(self, graph, company):
        height = settings['window']['height']
        self.x -= math.ceil(settings['window']['width'] / settings['length'])
        self.ySharePrice = height - math.ceil(((self.marketValue / company.shares) / graph.yMaxS) * height)
        if self.ySharePrice > height:
            self.ySharePrice = height
        self.yMarketCap = height - math.ceil((self.marketValue / graph.yMaxMC) * height)
        if self.yMarketCap > height:
            self.yMarketCap = height


class Lines:
    def __init__(self, windows, start, end, color):
        self.active = True
        self.windowSharePrice = windows[0]
        self.windowMarketCap = windows[1]
        self.start = start
        self.end = end
        self.lineSharePrice = self.windowSharePrice.create_line(
            self.start.x, self.start.ySharePrice, self.end.x, self.end.ySharePrice, fill=color
        )
        self.lineMarketCap = self.windowMarketCap.create_line(
            self.start.x, self.start.yMarketCap, self.end.x, self.end.yMarketCap, fill=color
        )

    def moveCoord(self, parent):
        self.windowSharePrice.coords(
            self.lineSharePrice, self.start.x, self.start.ySharePrice, self.end.x, self.end.ySharePrice
        )
        # self.windowSharePrice.update()
        self.windowMarketCap.coords(
            self.lineMarketCap, self.start.x, self.start.yMarketCap, self.end.x, self.end.yMarketCap
        )
        # self.windowMarketCap.update()
        if self.end.x <= 0 and parent.operational is False:
            return False
        return True


class Company:
    pStates = settings['pStates']

    def __init__(self, windows, market, shares, year, color):
        self.name = self.nameGeneration()
        self.operational = True
        self.windows = windows
        self.color = color
        self.marketCap = market
        self.currentValue = market/shares
        self.yearCreated = year
        self.yearCurrent = year
        self.shares = shares
        self.state = 'good'
        self.nodes = [Node(year, market)]
        self.lines = []
        self.xMaxS, self.yMaxS = year, market / shares
        self.yMaxMC = market

    @staticmethod
    def nameGeneration():
        letters = list('abcdefghijklmnopqrstuvwxyz')
        name = ''
        for i in range(random.randrange(3, 6)):
            name += letters[random.randrange(len(letters))]
        return name

    def changeMarketCap(self, growth):
        self.marketCap += (self.marketCap * growth)
        if self.marketCap == 0:
            return
        fakeMarket = int(self.marketCap)
        randomLuck = \
            (((random.randrange(fakeMarket) - (fakeMarket / 2)) /
             (fakeMarket/(abs(abs(self.pStates[self.state])) + 1))) ** 5) * 10
        # A lot of the code above me is just fancy nonsense as it contradicts itself making changes static.
        if self.state == 'excellent' or self.state == 'incredible':
            randomLuck = abs(randomLuck)
        elif self.state == 'horrible' or self.state == 'horrendous':
            randomLuck = abs(randomLuck) * -1
        # print(randomLuck)
        self.marketCap += randomLuck

    def scaleChange(self):
        if self.yMaxS < math.ceil(self.currentValue * 1.02):
            self.yMaxS = math.ceil(self.currentValue * 1.02)
        if self.yMaxMC < math.ceil(self.marketCap * 1.01):
            self.yMaxMC = math.ceil(self.marketCap * 1.01)
        self.xMaxS += 1

    def yearlyChange(self):
        chosen = random.randrange(100)
        temp_list = list(self.pStates)
        if chosen >= 95:
            if not (temp_list.index(self.state) == 0):
                self.state = temp_list[temp_list.index(self.state) - 1]
        elif chosen <= 5:
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
            if self.yearCurrent - self.yearCreated > settings['length']:
                tempLine = self.lines[0]
                tempNode = self.nodes[0]
                self.lines.pop(0)
                self.nodes.pop(0)
                tempLine.start = self.nodes[-1]
                tempNode.year = self.yearCurrent
                tempNode.marketValue = self.marketCap
                tempNode.x = settings['window']['width']
                tempLine.end = tempNode
                self.lines.append(tempLine)
                self.nodes.append(tempNode)
            else:
                node = Node(self.yearCurrent, self.marketCap)
                self.lines.append(Lines(self.windows, self.nodes[-1], node, self.color))
                self.nodes.append(node)
        self.scaleChange()

    def stockSplit(self):
        if self.marketCap / self.shares >= settings['stockSplit']:
            self.shares = math.ceil(self.shares * random.randrange(2, 6))
            self.yMaxS = math.ceil(self.yMaxS / 4)
        # elif self.marketCap / self.shares <= 10:
        #     self.shares = math.ceil(self.shares / 2)

    def bankruptcy(self):
        print(
            f"\nCompany existed from "
            f"{self.yearCreated} to "
            f"{self.yearCurrent} making it "
            f"{self.yearCurrent - self.yearCreated}")
        self.operational = False


def updatingWindows(windows):
    for updateWindow in windows:
        updateWindow.update()


def printLine(currentMarket, year, start, gph):
    print(f"Current Market Size: {currentMarket:.2f}, "
          f"Year: {year}, "
          f"Time: {time.time() - start:.4f}, "
          f"Companies: {len(gph.companies)}")


def main():
    colors = Colors.COLORS
    gph = Graph()
    year = 0
    windows = [gph.windowShares, gph.windowMarket]
    while True:
        # time.sleep(1/settings['speed'])
        start = time.time()
        gph.findRange()
        if year % settings['window']['refresh'] == 0:
            updatingWindows(windows)
        if year % settings["newCompany"] == 0 and len(gph.companies) < settings['maxCompanies']:
            gph.companies.append(Company(windows, 50000, 50000, year, random.choice(colors)))
        currentMarket = 0
        for company in gph.companies:
            currentMarket += company.marketCap
        year += 1
        Stats.sort_values(gph.companies, gph.statsCanada)
        printLine(currentMarket, year, start, gph)


if __name__ == '__main__':
    main()
