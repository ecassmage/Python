""" Well That red herring almost got me, seriously you don't even need the cars unless you want to max your points as
high as possible """

import os
import re
from multiprocessing import Pool


class Node:
    def __init__(self):
        self.incomingRoads = []
        self.outgoingRoads = []
        self.currentRoad = ''


class Roads:
    def __init__(self, name, start, end, time):
        self.nameOfRoad = name
        self.start = start
        self.end = end
        self.allCarsToTraverse = 0
        self.timeToTraverse = time
        self.lengthOfLight = 1
        self.carsOnRoad = []
        self.childrenNodes = []
        self.parentNodes = []
        self.siblingNodes = []
        self.needed = 0


class Car:
    def __init__(self, car, start, end):
        self.start = start
        self.end = end
        self.totalRoads = car[0]
        self.roadsToTraverse = []
        self.addRoads(car)

    def addRoads(self, car):
        for road in car[1:]:
            self.roadsToTraverse.append(road)


def openPath():
    for file in os.listdir(os.path.join(os.getcwd(), 'inputFiles')):
        currentFile = open(os.path.join(os.getcwd(), 'inputFiles', file), 'r')
        yield currentFile


def openSingleFile():
    return open('inputFiles/a.txt', 'r')


def parseFile(file):
    listOfRoutes = []
    listOfCars = []
    numLine = []
    for num, line in enumerate(file):
        if num == 0:
            line = line.replace('\n', '')
            numLine = line.split(' ')
        else:
            listOfRoutes.append(re.findall(r"\d+|\w[^\n ]+", line))
    num = int(numLine[3])
    for i in range(1, num + 1):
        listOfCars.append(listOfRoutes[len(listOfRoutes) - i])
    for n, i in enumerate(reversed(listOfRoutes)):
        if n >= num:
            break
        listOfRoutes.pop(-1)
    return numLine, listOfRoutes, listOfCars


def main():
    listOfPages = openPath()
    print(listOfPages)
    for i in listOfPages:
        print(i)
    for i in listOfPages:
        print(i)
    print(listOfPages)
    return


def createObjects(routes, carsList):
    routeObjects = {}
    carObjects = []
    for listing in routes:
        routeObjects.update({listing[2]: Roads(listing[2], int(listing[0]), int(listing[1]), listing[3])})
    for objectRoute in routeObjects:
        for secondaryObjectRoute in routeObjects:
            if routeObjects[secondaryObjectRoute] != routeObjects[objectRoute]:
                if routeObjects[secondaryObjectRoute].start == routeObjects[objectRoute].end:
                    routeObjects[objectRoute].childrenNodes.append(routeObjects[secondaryObjectRoute])
                if routeObjects[secondaryObjectRoute].end == routeObjects[objectRoute].start:
                    routeObjects[objectRoute].parentNodes.append(routeObjects[secondaryObjectRoute])
                if routeObjects[secondaryObjectRoute].end == routeObjects[objectRoute].end:
                    routeObjects[objectRoute].siblingNodes.append(routeObjects[secondaryObjectRoute])
    for listing in carsList:
        start = routeObjects[listing[1]]
        end = routeObjects[listing[-1]]
        carObjects.append(Car(listing, start, end))
        start.carsOnRoad.append(carObjects[-1])
    for car in carObjects:
        for road in car.roadsToTraverse:
            routeObjects[road].needed += 1
    nodes = {}
    for road in routeObjects:
        if routeObjects[road].start not in nodes:
            nodes.update({routeObjects[road].start: Node()})
        nodes[routeObjects[road].start].outgoingRoads.append(routeObjects[road])
        if routeObjects[road].end not in nodes:
            nodes.update({routeObjects[road].end: Node()})
        nodes[routeObjects[road].end].incomingRoads.append(routeObjects[road])
        pass
    return routeObjects, carObjects, nodes


def driveRoute(cars, routes, nums):
    for i in range(nums[0]):  # nums[0] holds how long the simulation last if it goes passed the it won't work
        for car in cars:
            pass
    pass


def writeFile(nodes, filename):
    submissionFile = open(f"outputFiles/{filename}.txt", 'w')
    submissionFile.write(f"{len(nodes)}\n")
    for node in nodes:
        submissionFile.write(f"{node}\n")
        submissionFile.write(f"{len(nodes[node].incomingRoads)}\n")
        for road in nodes[node].incomingRoads:
            submissionFile.write(f"{road} 1\n")
    submissionFile.close()


def main2():

    numList, routes, carsList = parseFile(file)
    routeObjects, carObjects, nodes = createObjects(routes, carsList)
    writeFile(nodes, f'submission{10}')
    print(f"We done with {file} or as you could say Number: {10}")
    # driveRoute(carObjects, routeObjects, numList)
    # print(numList)
    # print(routes)
    # print(carsList)
    return


if __name__ == '__main__':
    files = openPath()
    files2 = [open('inputFiles/b.txt', 'r'), open('inputFiles/f.txt', 'r')]
    with Pool(processes=2) as p:
        p.map(main2, files2)
    for num, file in enumerate(files):
        main2()
    # main()
