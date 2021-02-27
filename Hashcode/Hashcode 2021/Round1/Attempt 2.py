""" Well That red herring almost got me, seriously you don't even need the cars unless you want to max your points as
high as possible First step is to find which roads end at an intersection, then mark, best way is to use a list.
Then you go a start writing the submission file by first writing the length of nodes in the program then looping
through all the nodes by first writing the number of the intersection then writing the number of roads which end at
this intersection and finally looping through all the roads which end at this intersection writing their names down as
you go along. Each road is followed by a number between 1 and the max time in the simulation, but in this case it is
best to just write 1.
So the stuff should be written like this

100  -> This number states that there are 100 intersections that will be written in this file.
0  -> This number means that we will be talking about intersection 0 for now.
2  -> This number means that there are 2 roads which will be given at least 1 second of green light.
Road 1  -> This number means that the roads name is Road and that it will have a green light for 1 second before
            next road goes green
Roadeo 1  -> This number means that the roads name is Roadeo and that it will have a green light for 1 second
            before next road goes green
    // As a side note: if only 1 road is named it should be given 1 and this light will always be green.
1  -> This number means that we are on to the next intersection and the pattern will continue along.

This is the basic attempt, my next attempt involved removing all roads which didn't receive any cars from the system
alleviating some time to the roads which did receive cars overall making the whole system more efficient ever so
slightly. I tried setting better times for the roads based on how many cars used them but it never seemed to pan out
more the maybe a thousand points. Also any intersection which ended up with zero roads ending on it were deactivated
and ignored by the program.

This program has all the files sorted into 2 folders inputFiles folder and outputFiles folder, with the program sitting
outside of these 2 folders.
"""
# import os
import re
import math
from multiprocessing import Pool


class Node:
    def __init__(self, name):
        self.name = name
        self.incomingRoads = []
        self.outgoingRoads = []
        self.carsPassingThrough = 0
        self.active = True


class Roads:
    def __init__(self, name, start, end, length):
        self.nameOfRoad = name
        self.start = start
        self.end = end
        self.carsPassingThrough = 0
        self.timeDelay = 0
        self.lightActive = True
        self.roadLength = int(length)


class Car:
    def __init__(self):
        self.roadsToTravel = []


# def openPath():
#     for file in os.listdir(os.path.join(os.getcwd(), 'inputFiles')):
#         currentFile = open(os.path.join(os.getcwd(), 'inputFiles', file), 'r')
#         yield currentFile


def openSingleFile(inP):
    return open(inP, 'r')


def parseFile(file):
    """
    Parses the input files so that they are sorted for objectCreate
    :param file:
    :return:
    """
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


def timeStop(route, node, maxTime):
    """  This never really panned out as well as i'd hoped so meh not really happy about that. """
    num = route.carsPassingThrough / route.roadLength
    temp = math.floor((1 / (route.carsPassingThrough / node.carsPassingThrough)) / num)
    if temp == 0:
        temp = 1
    if len(node.incomingRoads) >= 3:
        route.timeDelay = 3
        return
    while temp >= maxTime or temp > 10:
        temp = math.ceil(temp / 2)
    route.timeDelay = temp

    return


def createObjects(numList, routes, carsList):
    """
    This creates the Objects that I will be using to link to the nodes or count appearances
    :param numList:  -> Holds the first input line.
    :param routes:  -> Holds all roads and their subsequent intersection connections
    :param carsList:  -> Holds all the car routes in them.
    :return:
    """
    roadObjects = {}
    carObjects = []
    nodes = {}
    for road in routes:
        roadObjects.update({road[2]: Roads(road[2], road[0], road[1], road[3])})
        if roadObjects[road[2]].end not in nodes:
            nodes.update({roadObjects[road[2]].end: Node(roadObjects[road[2]].end)})
        nodes[roadObjects[road[2]].end].incomingRoads.append(roadObjects[road[2]])
        if roadObjects[road[2]].start not in nodes:
            nodes.update({roadObjects[road[2]].start: Node(roadObjects[road[2]].start)})
        nodes[roadObjects[road[2]].start].outgoingRoads.append(roadObjects[road[2]])
    for carList in carsList:
        carObjects.append(Car())
        for road in carList[1:]:
            carObjects[-1].roadsToTravel.append(road)
            roadObjects[road].carsPassingThrough += 1
            nodes[roadObjects[road].end].carsPassingThrough += 1
        pass

    for node in reversed(nodes):
        for road in reversed(nodes[node].incomingRoads):
            if road.carsPassingThrough == 0:
                nodes[node].incomingRoads.pop(nodes[node].incomingRoads.index(road))
                road.lightActive = False
                del roadObjects[road.nameOfRoad]
        for road in reversed(nodes[node].outgoingRoads):
            if road.carsPassingThrough == 0:
                nodes[node].outgoingRoads.pop(nodes[node].outgoingRoads.index(road))
        if len(nodes[node].incomingRoads) <= 0:
            nodes[node].active = False

    for road in roadObjects:
        timeStop(roadObjects[road], nodes[roadObjects[road].end], int(numList[0]))
    return roadObjects, carObjects, nodes


def writeFile(nodes, filename):
    """
    This Function writes the files for submission
    :param nodes:  -> Nodes hold all the information for writing I just need to sift through to find it
    :param filename:  -> This is the file name so that the program doesn't overwrite all previously made files
    :return:
    """
    submissionFile = open(f"outputFiles/{filename}.txt", 'w')
    Count = 0
    for node in nodes:
        if nodes[node].active:
            Count += 1
    writeLine = f"{Count}\n"
    for node in nodes:
        if nodes[node].active:
            writeLine += f"{node}\n{len(nodes[node].incomingRoads)}\n"
            for road in nodes[node].incomingRoads:
                writeLine += f"{road.nameOfRoad} {road.timeDelay}\n"
    submissionFile.write(writeLine)
    submissionFile.close()


def main(inP):
    """
    This just manages the logic of each file mainly for switching between the main functions
    :param inP:  -> inP stands for inPut
    :return:
    """
    file = openSingleFile(f"inputFiles/{inP}.txt")
    numList, routes, carsList = parseFile(file)
    routeObjects, carObjects, nodes = createObjects(numList, routes, carsList)
    writeFile(nodes, f'submission{inP}')
    print(f"We done with {file} or as you could say Number: {inP}")
    return


if __name__ == '__main__':
    multi = True
    if multi:
        files = ['a', 'b', 'c', 'd', 'e', 'f']
        with Pool(processes=6) as p:
            p.map(main, files)
    else:
        main('a')
        exit()
