"""
The Plan for this is to have at the beginning of the program is too have it initialize however many companies is asked
of the program and place them into an inactive list.
    Why do this, it seems that tkinter which is what I am using to draw my GUI doesn't do too well with reusing
    objects and so even if I continuously delete objects upon not being useful anymore tkinter will continue to
    bloat its ID and other internal memory too the point where something running at the start of the program being
    updated 10 - 30 times per second will after give or take an hour maybe 0.5 - 1 time per second causing seriously
    large slow downs I don't want. An easy fix for this is to just create all objects at the beginning and just hide
    them when inactive while then calling them when needed. Once a company goes bankrupt the company Object will be
    cleared visually from the board without any of its' nodes or lines being deleted and then stored in an inactive
    list only ever accessed if a new company is needed or an active company has gone Bankrupt.

    Example:
        maxCompanies = 5

        self.companyActive = [Company0, Company1]
        self.companyInActive = [Company2, Company3, Company4]

        Company0 -> 'Goes Bankrupt'
        Company0 -> 'the nodes and lines are cleared of their information but not deleted either moved off screen '
                    'else I found some way to just not show the objects on screen and therefore not taking up '
                    'computation time.'

        self.companyActive = [Company1]
        self.companyInActive = [Company2, Company3, Company4, Company0]

        newCompanyFounded -> 'A new company is trying to appear which needs a company template'
        reconfigureCompanyForFreshStart ->  'some function/method which effectively factory resets company possibly '
                                            'by either calling __init__ from this function/method or having __init__ '
                                            'call this function/method and initializing everything here instead'

        self.companyActive = [Company1, Company2]
        self.companyInActive = [Company3, Company4, Company0]

The another Plan is to have a changeable GUI where buttons or a menu will exist where you can choose whichever form of
graph you want this will allow faster processing and higher versatility in graphing as the program only needs to render
a single graph but can be viewed a multitude of different ways. The information will be stored in the nodes as well as
the state at which the user wants the information to be stored as.

Example:
    If for instance the user is currently viewing the Market Cap, they can with the simple click of the mouse be able
    to switch to the shares page and a signal will be sent to all nodes with either a word or a number.
        (Haven't decided whether to use keywords like sharesGraph, marketCapGraph etc or to just use numbers.)
    This word/number will then once the node is meant to make its x, y changes dictate what information it will look at
    when making these changes.

I have decided to organize all the different possible graphs in a drop down menu so as to make them easier to fit on the
screen at a single time without taking too much space from the user. I am also adding some quality of life additions to
the menu as well including the ability to pause the program whenever you like as this will make it far easier to see
certain events on the graph if wanted. It also allows for the user to make guesses of the future should they desire too.


"""
import Company
from Institutions import StockMarket, Bank, Industries
import math
import time
import tkinter as tk
import configReader
rules = configReader.rulesFileReader()


class Graph:
    def __init__(self):

        self.yUpperBound = 2000000
        self.yLowerBound = 0
        self.yMiddleBound = (self.yUpperBound + self.yLowerBound) / 2
        self.pausedProgram = False
        self.quitProgram = False

        self.tkFrame = tk.Tk()
        self.windowFrame = tk.Frame(self.tkFrame)
        self.windowCanvas = tk.Canvas(
            self.windowFrame, width=rules['window']['width'], height=rules['window']['height'], bg='black')

        self.upperLabel = tk.Label(self.windowCanvas, text=f"{self.yUpperBound}", bg='black', fg='white')
        self.oneQuarterLabel = tk.Label(
            self.windowCanvas, text=f"{(self.yUpperBound + self.yMiddleBound) / 2}", bg='black', fg='white')
        self.middleLabel = tk.Label(self.windowCanvas, text=f"{self.yMiddleBound}", bg='black', fg='white')
        self.threeQuarterLabel = tk.Label(
            self.windowCanvas, text=f"{(self.yMiddleBound + self.yLowerBound) / 2}", bg='black', fg='white')
        self.lowerLabel = tk.Label(self.windowCanvas, text=f"{self.yLowerBound}", bg='black', fg='white')

        self.currentGraphType = 'marketCap'
        self.bank = Bank.Bank()
        self.stockMarket = StockMarket.StockMarket()
        self.basicIndustry = Industries.Electronics()
        self.Industry = {
            "electronics": Industries.Electronics(),
            "mining": Industries.Mining(),
            "fastFood": Industries.FastFood(),
            "retail": Industries.Retail(),
            "agriculture": Industries.Agriculture()
        }
        self.companiesInactive = self.createCompanies()
        self.companiesActive = []
        self.__menuGraphsType__()
        self.showScreen()

    def createCompanies(self):
        tempListCompanies = []
        for i in range(rules['companyConditions']['numberOfCompanies']):
            tempListCompanies.append(
                Company.Company(
                    self, self.windowCanvas, self.bank, self.stockMarket, self.basicIndustry, 'electronics', 0, 'red'
                )
            )
        return tempListCompanies

    def showScreen(self):
        self.windowFrame.pack()
        self.windowCanvas.pack()
        self.upperLabel.place(x=5, y=5)
        self.oneQuarterLabel.place(x=5, y=(rules['window']['height'] - 20) / 4)
        self.middleLabel.place(x=5, y=(rules['window']['height'] - 20) / 2)
        self.threeQuarterLabel.place(x=5, y=(rules['window']['height'] - 20) / (4 / 3))
        self.lowerLabel.place(x=5, y=rules['window']['height'] - 20)

    def updateLabels(self):
        self.upperLabel.config(text=f"{self.yUpperBound}")
        self.oneQuarterLabel.config(text=f"{(self.yUpperBound + self.yMiddleBound) / 2}")
        self.middleLabel.config(text=f"{self.yMiddleBound}")
        self.threeQuarterLabel.config(text=f"{(self.yMiddleBound + self.yLowerBound) / 2}")
        self.lowerLabel.config(text=f"{self.yLowerBound}")

    def __menuGraphsType__(self):
        self.font = ("Verdana", 10)
        self.mainMenu = tk.Menu(self.tkFrame)
        self.menuDropDown = tk.Menu()
        self.graphTypes = tk.Menu()
        """ Possibly another menu for isolating between industries or isolating between companies. """

        self.menuRegistry()
        self.graphTypeMenuRegistry()

        self.mainMenu.add_cascade(label='Menu', menu=self.menuDropDown)
        self.mainMenu.add_cascade(label='Graphs', menu=self.graphTypes)

        self.tkFrame.config(menu=self.mainMenu)

    def graphTypeMenuRegistry(self):
        """
        This Section manages the Graphs Drop Down Menu which can change what the graph will show on the next refresh
        NOTE: It will most likely take some time to actually update the graph this way as every single node has to be
        updated with new coordinates, then the lines have to be given these new coordinates and updated with
        tkinter.update() which can take a little time when dealing with more then 5000 objects albeit small objects.
        """
        self.graphTypes.add_command(
            label="Market Cap", font=self.font, command=lambda: self.changeGraph('marketCap'))
        self.graphTypes.add_command(
            label="Shares", font=self.font, command=lambda: self.changeGraph('shares'))
        self.graphTypes.add_command(
            label="Shares Price", font=self.font, command=lambda: self.changeGraph('sharePrice'))
        self.graphTypes.add_command(
            label="Age", font=self.font, command=lambda: self.changeGraph('year'))
        self.graphTypes.add_command(
            label="Revenue", font=self.font, command=lambda: self.changeGraph('revenue'))
        self.graphTypes.add_command(
            label="Cash", font=self.font, command=lambda: self.changeGraph('cash'))
        self.graphTypes.add_command(
            label="Costs", font=self.font, command=lambda: self.changeGraph('cost'))
        self.graphTypes.add_command(
            label="Profit", font=self.font, command=lambda: self.changeGraph('profit'))
        self.graphTypes.add_command(
            label="Debt", font=self.font, command=lambda: self.changeGraph('debt'))
        self.graphTypes.add_command(
            label="Outstanding Shares", font=self.font, command=lambda: self.changeGraph('outstanding'))
        self.graphTypes.add_command(
            label="Not Outstanding Shares", font=self.font, command=lambda: self.changeGraph('notOutstanding'))
        self.graphTypes.add_command(
            label="Goods in Stock", font=self.font, command=lambda: self.changeGraph('goods'))
        self.graphTypes.add_command(
            label="Goods sold this Year", font=self.font, command=lambda: self.changeGraph('goodsSoldThisYear'))
        self.graphTypes.add_command(
            label="Goods Produced this Year", font=self.font, command=lambda: self.changeGraph('goodsProducedThisYear'))
        self.graphTypes.add_command(
            label="Product Price", font=self.font, command=lambda: self.changeGraph('productPrice'))
        self.graphTypes.add_command(
            label="Employees", font=self.font, command=lambda: self.changeGraph('employees'))
        self.graphTypes.add_command(
            label="Assets Owned", font=self.font, command=lambda: self.changeGraph('factors'))
        self.graphTypes.add_command(
            label="Land Owned (Acres)", font=self.font, command=lambda: self.changeGraph('land'))
        self.graphTypes.add_command(
            label="Popularity", font=self.font, command=lambda: self.changeGraph('popularity'))

    def menuRegistry(self):
        self.menuDropDown.add_command(label='Pause', font=self.font, command=self.pauseGraphRunning)
        self.menuDropDown.add_command(label='Exit', font=self.font, command=self.quitApplication)

    def changeGraph(self, newGraphType):
        self.currentGraphType = newGraphType
        self.yUpperBound = 0
        try:
            self.yLowerBound = self.companiesActive[0].nodesActive[0].allNodeValues[self.currentGraphType]
        except IndexError:
            print("Hello\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return
        for company in self.companiesActive:
            company.yUpper = 0
            if len(company.nodesActive) >= 1:
                company.yLower = company.nodesActive[0].allNodeValues[self.currentGraphType]
            for node in company.nodesActive:
                if node.allNodeValues[self.currentGraphType] > self.yUpperBound:
                    self.yUpperBound = node.allNodeValues[self.currentGraphType]

                elif node.allNodeValues[self.currentGraphType] < self.yLowerBound:
                    self.yLowerBound = node.allNodeValues[self.currentGraphType]

                if node.allNodeValues[self.currentGraphType] > company.yUpper:
                    company.yUpper = node.allNodeValues[self.currentGraphType]

                elif node.allNodeValues[self.currentGraphType] < company.yLower:
                    company.yLower = node.allNodeValues[self.currentGraphType]
        self.yLowerBound -= abs(round(self.yLowerBound * 0.01, 0)) if (abs(round(self.yLowerBound * 0.01, 0)) >= 1) else 1
        self.yUpperBound += abs(round(self.yUpperBound * 0.01, 0)) if (abs(round(self.yLowerBound * 0.01, 0)) >= 1) else 1
        # print(self.yUpperBound, self.yLowerBound)

    def pauseGraphRunning(self):
        """
        This simply pauses and un pauses program based on a menu button press. Simple and easy to understand
        A press of the menu pause button a second time will un pause the program.
        """
        if self.pausedProgram:
            self.pausedProgram = False
        else:
            self.pausedProgram = True
        while self.pausedProgram:
            self.tkFrame.update()
            if self.quitProgram:
                self.tkFrame.quit()
                exit()

    def quitApplication(self): self.quitProgram = True


class Node:
    def __init__(self):
        self.x, self.y = rules['window']['width'], 0
        self.allNodeValues = {
            "marketCap": 0,
            "shares": 0,
            "sharePrice": 0,
            "year": 0,
            "revenue": 0,
            "cash": 0,
            "cost": 0,
            "profit": 0,
            "debt": 0,
            "outstanding": 0,
            "notOutstanding": 0,
            "goods": 0,
            "goodsSoldThisYear": 0,
            "goodsProducedThisYear": 0,
            "productPrice": 0,
            "employees": 0,
            "factors": 0,
            "land": 0,
            "popularity": 0
        }

    def changePosition(self, graph):
        height = rules['window']['height']
        self.x -= (rules["window"]["width"] / rules["companyConditions"]["lengthOfGraphs"])
        # print(graph.yUpperBound - graph.yLowerBound)
        self.y = math.ceil(height - (height * ((self.allNodeValues[graph.currentGraphType] - graph.yLowerBound) /
                                               round(graph.yUpperBound - graph.yLowerBound, 0))))
        return

    def initiateNode(self, company):
        self.allNodeValues = {
            "marketCap": company.marketCap,
            "shares": company.shares,
            "sharePrice": company.sharePrice,
            "year": (company.yearPresent - company.yearFounded),
            "revenue": company.revenue,
            "cash": company.cash,
            "cost": company.costs,
            "profit": company.profits,
            "debt": company.debt,
            "outstanding": company.shares * (company.percentOutstanding/100),
            "notOutstanding": company.shares * (company.percentNotOutstanding/100),
            "goods": company.goods,
            "goodsSoldThisYear": company.goodsSold,
            "goodsProducedThisYear": company.goodsProduced,
            "productPrice": company.productWorth,
            "employees": company.employees,
            "factors": company.totalFactorsOwned(),
            "land": company.land,
            "popularity": company.popularity
        }
        self.x = rules['window']['width']


class Line:

    def __newAttributes__(self, start, end, color):
        self.color = color
        self.start = start
        self.end = end

    def __activate__(self):
        self.line = self.window.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=self.color)
        self.activated = True

    def __init__(self, window):
        self.color = None
        self.start = None
        self.end = None
        self.window = window
        self.activated = False
        self.line = None

    def changePosition(self, company):
        self.window.coords(self.line, self.start.x, self.start.y, self.end.x, self.end.y)
        if self.end.x <= 0:
            self.hideLine()
            company.nodesInactive.append(self.start)
            company.nodesActive.pop(company.nodesActive.index(self.start))
            company.linesInactive.append(self)
            company.linesActive.pop(company.linesActive.index(self))

    def resetLine(self, start, end, color):
        self.__newAttributes__(start, end, color)
        if self.activated is False:
            self.__activate__()

    def hideLine(self):
        self.window.coords(-1, -1, -1, -1)


def createGraph():
    return Graph()


# a.windowFrame.update()
# bleep = a.windowCanvas.create_line(0, 0, 100, 100)
# for i in range(100):
#     if a.quitProgram:
#         a.tkFrame.quit()
#         exit()
#     # a.windowCanvas.coords(bleep, i, i, i + 100, i + 100)
#     a.windowFrame.update()
#     time.sleep(0.1)
# a.windowFrame.mainloop()

# print(a.companies)
