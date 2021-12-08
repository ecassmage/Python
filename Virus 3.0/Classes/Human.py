import pygame
import random
import math
import Defines.Color

import Files.FileOpener as FileOpener
try:
    import Virus
except ModuleNotFoundError:
    import Classes.Virus as Virus


class Human:
    def __init__(self):
        self.stg = FileOpener.openStg()
        self.infected = False
        self.immune = False
        self.virus = None
        self.ageOfInfection = 0

        self.size = self.stg['human']['size'] // 2
        self.shape = self.stg['human']['start']['shape'].lower()
        self.speed = self.stg['human']['speed']

        self.coord = self.getCoordinateSet()
        self.pathing = [0, 0, [0, 0]]  # [Ratio, Current Point in Ratio, [unit vector x, unit vector y]]
        self.path = []  # a two-point x-y indicating the position this human will be traversing for the foreseeable future.

        self.color = Defines.Color.getColor(self.stg['human']['color'])  # red if infected
        self.Name = []  # To know who is dying on a personal level
        self.id = -1  # -1 means not set yet.  Might not be even needed as pygame has you draw a completely new object.

    def routine(self, HumanDict: dict, proximity: bool, newDay: bool):
        if newDay:
            self.increaseVirusAge()
        self.unInfectHuman()
        if not self.immune:
            self.choosePath(HumanDict)
            if proximity and self.infected:
                self.proximity(HumanDict)

    def drawSprite(self, window):
        match self.shape:
            case 'circle':
                self.id = pygame.draw.circle(window, self.color, self.coord, self.size)

    def setID(self, registerID):
        """
        Sets the ID to whatever is inputted. Probably not needed anymore, Might though in future so I am leaving it in
        :param registerID: Takes in an ID.
        """
        self.id = registerID

    def getCoordinateSet(self):
        """
        Will generate a random set of coordinates to give to the human as coordinates.
        Uses the size of the human and the width of the window to generate these coordinates to be within the bounds of the window.
        :return: Returns the set of coordinates as a list.
        """
        return [random.randrange(1 + self.size, self.stg['window']['width'] - self.size - 1), random.randrange(1 + self.size, self.stg['window']['height'] - self.size - 1)]

    def infect(self, virus=None, guarantee=False):
        if virus is None:
            virus = Virus.Virus()

        if virus.infectHuman() or guarantee:
            self.infected = True
            self.virus = virus
            self.color = Defines.Color.getColor(self.stg['virus']['color'])

    def increaseVirusAge(self):

        if self.infected:
            self.ageOfInfection += 1

    def unInfectHuman(self):
        def unInfect():
            self.infected = False
            self.color = Defines.Color.getColor(self.stg['virus']['colorRecovered'])
            self.ageOfInfection = 0
            self.immune = True
            self.update = False

        if self.ageOfInfection > self.stg['virus']['earliestRecovery']:
            if self.ageOfInfection > self.stg['virus']['latestRecovery']:
                unInfect()
            elif (100 * (1 / (1 + math.exp(-1 * ((self.ageOfInfection - (self.stg['virus']['latestRecovery'] - self.stg['virus']['earliestRecovery'])) / (self.stg['virus']['latestRecovery'] / 5)))))) / \
                    self.stg['backEnd']['iterationRate'] >= random.randrange(100):
                unInfect()

    # Define Movement of Object
    def checkProximity(self, other, proximityCheck):
        """
        checkProximity will check this human against another set of coordinates to see if it is withing proximityCheck
        it uses x^2 + y^2 == r^2 as a basis, though it will check instead if the left side is less then or equal to the right side.

        :param other: Takes the coordinate set that is being matched against.
        :param proximityCheck: Takes the proximity the other object needs to be in to trigger a response.
        :return: If the other set of coordinates fall within the collision boundary, this method will return True, else it will return False
        """
        coord_x = (other[0] - self.coord[0]) * (other[0] - self.coord[0])
        coord_y = (other[1] - self.coord[1]) * (other[1] - self.coord[1])
        coord_r = proximityCheck * proximityCheck

        return coord_x + coord_y <= coord_r

    def proximity(self, HumanDictionary):
        """
        Checks Proximity of of all humans to this specific human. Only for those who are infected though, non infected will not need to use this.
        Uses a dictionary to sort all the humans into their specific x coordinate cohorts
        :param HumanDictionary: Takes a dictionary of all humans keyed by their x coordinate.
        """
        for x in range(self.coord[0] - self.size - self.virus.proximity, self.coord[0] + self.size + self.virus.proximity):
            if x in HumanDictionary:
                for human in HumanDictionary[x]:
                    if human.immune or self == human:
                        continue
                    if self.checkProximity(human.coord, self.virus.proximity+self.size):
                        human.infect(self.virus)

    def choosePath(self, dictionary):
        """
        Chooses the Path that the human will be going. It will then move the character based on the unitVector it has.
        :param dictionary:
        :return:
        """
        if len(self.path) == 0 or self.checkProximity(self.path, 2 * self.speed):
            # x = random.randrange(1 + self.size, self.stg['window']['width'] - self.size - 1)
            # y = random.randrange(1 + self.size, self.stg['window']['height'] - self.size - 1)
            self.path = self.getCoordinateSet()
            self.calculatePath()
        self.move(dictionary)

    def calculatePath(self):
        """
        Will calculate the path needed using whatever this algorithm is called.
        It will first calculate the rise over the run and will follow this up by then calculating the unit vector for this specific rise over run.
        """
        try:
            self.pathing[0] = abs((self.path[1] - self.coord[1]) / (self.path[0] - self.coord[0]))
        except ZeroDivisionError:
            self.pathing[0] = 0

        self.pathing[2][0] = 1 * self.speed if self.path[0] - self.coord[0] > 0 else -1 * self.speed
        self.pathing[2][1] = 1 * self.speed if self.path[1] - self.coord[1] > 0 else -1 * self.speed

    def move(self, dictionary):
        """
        This will move the human along its line using the list of information generated by calculatePath(self).
        :param dictionary: Takes a dictionary of all the humans keyed by their x coordinate
        """
        def removeKey():
            """Removes self from the dictionary. Necessary as the x coordinate is about to change and be forgotten. Without this the dictionary would fill up to uncontrollable sizes."""
            if len(dictionary[self.coord[0]]) == 1:
                del [dictionary[self.coord[0]]]
            else:
                dictionary[self.coord[0]].pop(dictionary[self.coord[0]].index(self))

        def addKey():
            """Adds self back to the dictionary. Necessary as without it, the human would be lost to all others. It would still be able to move however as it can still be located in an iterable list."""
            if self.coord[0] in dictionary:
                dictionary[self.coord[0]].append(self)
            else:
                dictionary.update({self.coord[0]: [self]})

        def horizontalMovement():
            self.coord[0] += self.pathing[2][0]

        def verticalMovement():
            self.coord[1] += self.pathing[2][1]

        removeKey()

        if self.path[0] == self.coord[0]:
            verticalMovement()
        elif self.path[1] == self.coord[1]:
            horizontalMovement()
        else:
            if self.pathing[1] < self.speed:
                self.pathing[1] += self.pathing[0]
                horizontalMovement()
            else:
                self.pathing[1] -= self.speed
                verticalMovement()

        addKey()


if __name__ == '__main__':
    H = Human()
    H.coord = [102, 105]
    H.checkProximity([100, 100], 10)
    pass
