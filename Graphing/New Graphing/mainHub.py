import graphicalInterface
import yearlyBusinessDecisions
import competition
import time
import random
import Colors


def nodeNext(nodes, graph):
    for node in reversed(nodes):
        node.changePosition(graph)
    return


def lineNext(lines, company):
    for line in reversed(lines):
        line.changePosition(company)
    return


def newNodeAndLine(company):
    oldNode = company.nodesActive[-1]
    newNode = company.newNode()

    newLine = company.newLine(oldNode, newNode)

    company.nodesActive.append(newNode)
    company.linesActive.append(newLine)
    return


def changeBounds(graph):
    for company in graph.companiesActive:
        print('55 ', company.productWorth)
        if company.yUpper * 1.02 > graph.yUpperBound:
            graph.yUpperBound = round(company.yUpper * 1.02, 0)
        if company.yLower < graph.yLowerBound:
            graph.yLowerBound = company.yLower
    graph.yMiddleBound = (graph.yUpperBound + graph.yLowerBound) / 2


def backEnd(company):
    yearlyBusinessDecisions.centralManager(company)


def beginningOfYearCalculations(frontEnd):
    changeBounds(frontEnd)
    competition.countCompetitors(frontEnd, frontEnd.companiesActive)


def tasksEachCompanyNeedsToDo(company):
    print('1 ', company.productWorth)
    company.advertisingGains()
    competition.splitConsumers(company)
    company.totalConsumers = company.totalConsumersFunc()
    company.totalOwned = company.totalFactorsOwned()
    company.trendyCompany()
    print('2 ', company.productWorth)
    return


def nextCycleOfTheCorporateEnterprises(graph, year):

    beginningOfYearCalculations(graph)
    for company in graph.companiesActive:
        print('3 ', company.productWorth)
        tasksEachCompanyNeedsToDo(company)
        backEnd(company)
        company.yearPresent = year
        newNodeAndLine(company)
        nodeNext(company.nodesActive, graph)
        lineNext(company.linesActive, company)
        print('4 ', company.productWorth)
    graph.updateLabels()

    return


def newCompany(graph, year):
    if len(graph.companiesInactive) == 0:
        return None
    newCompanyTemplate = graph.companiesInactive[0]
    graph.companiesInactive.pop(0)
    tempIndustry = (random.choice(list(graph.Industry)))  # for choosing the new industry to enter
    newCompanyTemplate.newCompany(
        graph.bank,
        graph.stockMarket,
        graph.Industry['electronics'],
        'electronics',
        year,
        random.choice(Colors.COLORS)
    )
    newCompanyTemplate.nodesActive.append(newCompanyTemplate.newNode())
    print("\n New Company \n")
    return newCompanyTemplate


def main():
    gph = graphicalInterface.createGraph()
    gph.companiesActive.append(newCompany(gph, 0))
    year = 0
    while True:
        start = time.time()
        nextCycleOfTheCorporateEnterprises(gph, year)
        if gph.quitProgram:
            gph.tkFrame.quit()
            exit()
        time.sleep(1/20)
        gph.windowCanvas.update()
        # print(f"The Time Being: {time.time() - start}")
        if year % 50 == 0 and year > 100 and len(gph.companiesInactive) > 0:
            tempComp = newCompany(gph, 0)
            if tempComp is not None:
                gph.companiesActive.append(tempComp)

        year += 1


if __name__ == "__main__":
    main()
