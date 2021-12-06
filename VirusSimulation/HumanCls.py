import random
import FileOpener
import Virus


class Human:
    def __init__(self):
        self.stg = FileOpener.openStg()

        self.infected = False
        self.virus = None
        self.ageOfInfection = 0

        self.size = self.stg['human']['size'] // 2
        self.speed = self.stg['human']['speed']

        self.coord = getBoundaryPosition([self.stg['window']['width'], self.stg['window']['height']], self.size)
        self.pathing = [0, 0, [0, 0]]  # [Ratio, Current Point in Ratio, [unit vector x, unit vector y]]
        self.path = []  # a two-point x-y indicating the position this human will be traversing for the foreseeable future.

        self.color = "green"  # red if infected
        self.Name = []  # To know who is dying on a personal level
        self.id = -1  # -1 means not set yet.
        pass

    def routine(self, HumanList, proximity=True):
        self.choosePath()
        if proximity:
            self.proximity(HumanList)

    def setID(self, newID):
        self.id = newID

    def drawSprite(self, tkinterWindow):
        return tkinterWindow.create_oval(self.coord[0] - self.size, self.coord[1] - self.size, self.coord[0] + self.size, self.coord[1] + self.size, fill=self.color)

    def infect(self, virus=None):
        if virus is None:  # No virus was given so this will just assume that the default virus was the strain.
            virus = Virus.Virus()
        self.infected = True
        self.virus = virus
        self.color = 'red'

    def setName(self):
        pass

    def increaseVirusAge(self):
        if self.infected:
            self.ageOfInfection += 1

    def proximityCheck(self, humanCmp=None, proximityVar=None):
        if proximityVar is None:
            proximityVar = self.virus.proximity + self.size

        coordCenter2 = self.path if humanCmp is None else humanCmp.coord
        coordCenter = self.coord

        return (coordCenter2[0] - coordCenter[0]) ** 2 + (coordCenter2[1] - coordCenter[1]) ** 2 < proximityVar**2

    def proximity(self, listOfOtherHumans):
        if not self.infected:
            return
        for human in listOfOtherHumans:
            if human.infected or human == self:
                continue
            if self.proximityCheck(human) and self.virus.infectHuman():
                human.infect(self.virus)

    def choosePath(self):
        if self.path == [] or self.proximityCheck(proximityVar=(2*self.speed)):
            x = random.randrange(25, self.stg['window']['width'] - 25)
            y = random.randrange(25, self.stg['window']['height'] - 25)
            self.path = [x, y]
            self.calculatePath()
        self.move()

    def calculatePath(self):
        try:
            self.pathing[0] = abs((self.path[1] - self.coord[1]) / (self.path[0] - self.coord[0]))
        except ZeroDivisionError:
            self.pathing[0] = 0

        self.pathing[2][0] = 1 * self.speed if self.path[0] - self.coord[0] > 0 else -1 * self.speed
        self.pathing[2][1] = 1 * self.speed if self.path[1] - self.coord[1] > 0 else -1 * self.speed

    def move(self):
        def horizontalMovement():
            self.coord[0] += self.pathing[2][0]

        def verticalMovement():
            self.coord[1] += self.pathing[2][1]

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


def getBoundaryPosition(Boundary, size):
    return [random.randrange(size, Boundary[0] - size), random.choice([size, Boundary[1] - size])] if random.randint(0, 1) == 1 \
        else [random.choice([size, Boundary[0] - size]), random.randrange(size, Boundary[1] - size)]


if __name__ == '__main__':

    # human1 = Human(0)
    # human2 = Human(0)
    # human3 = Human(0)
    #
    # human1.virus = Virus.Virus()
    #
    # human1.coord = [100, 78]
    # human2.coord = [93, 76]
    # human3.coord = [98, 77]
    #
    # print(human1.proximity([human1, human2]))  # should return False if proximity is 10 and True if proximity is 100
    # print(human1.proximity([human1, human3]))  # should return True if proximity is 10 and True if proximity is 100
    #
    # human1.choosePath()
    # print(f"{human1.coord} {human1.path} {human1.pathing}")
    # for i in range(10000):
    #     human1.choosePath()
    #     if human1.proximityCheck(proximityVar=5):
    #         print(f"{human1.coord} {human1.path} {human1.pathing}")
    #
    # print("HumanCls.py Test Run")
    pass
