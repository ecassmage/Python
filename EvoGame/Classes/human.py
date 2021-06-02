import EvoLogging
import random


class Human:
    def __init__(self, canvas, coord, name):
        self.canvas = canvas
        self.age = 0
        self.name = name
        self.children = 0

        self.coord = coord
        self.moveTo = None
        self.chosenTarget = None
        self.ratioMovement = None

        self.speed = canvas.settings['human']['speed']
        self.holdOnToSpeedFloats = None
        self.movesRemaining = 0

        self.fertility = canvas.settings['human']['fertility']
        self.energy = self.energyPlentitude()
        self.size = canvas.settings['human']['size']
        self.vision = canvas.settings['human']['vision']

        self.sprite = self.canvas.canvas.create_rectangle(
            coord[0]-self.size, coord[1]-self.size, coord[0] + self.size, coord[1] + self.size,
            fill='orange'
        )

        self.eaten = False
        self.survive = False
        self.alive = True
        self.beingChased = [False, None]

        self.refreshRemainingMoves()
        self.determineSpeedFloat()

    def fullName(self):
        return self.name[0] + " " + self.name[1]

    def stringClass(self):
        return f"\tAge: {self.age}\n" \
               f"\tClass Information: {self}\n" \
               f"\tName: {self.fullName()}\n" \
               f"\tChildren: {self.children}\n" \
               f"\n" \
               f"\tCoordinate: {self.coord}\n" \
               f"\tMoveTo Coordinate: {self.moveTo}\n" \
               f"\tChosenTarget: {self.chosenTarget}\n" \
               f"\tRatioMovement: {self.ratioMovement}\n" \
               f"\n" \
               f"\tSpeed: {self.speed}\n" \
               f"\tFertility: {self.fertility}\n" \
               f"\tEnergy: {self.energy}\n" \
               f"\tSize: {self.size}\n" \
               f"\tVision: {self.vision}\n" \
               f"\tHoldOnToSpeedFloats: {self.holdOnToSpeedFloats}\n" \
               f"\tMovesRemaining: {self.movesRemaining}\n" \
               f"\tSprite ID: {self.sprite}\n" \
               f"\n" \
               f"\tEaten: {self.eaten}\n" \
               f"\tSurvived: {self.survive}\n" \
               f"\tAlive: {self.alive}\n" \
               f"\tBeingChased: {self.beingChased}\n"

    def resetHuman(self, coord, name):
        self.coord = coord
        self.moveTo = None
        self.chosenTarget = None
        self.ratioMovement = None
        self.age = 0
        self.children = 0
        self.name = name
        self.speed = self.canvas.settings['human']['speed']
        self.movesRemaining = round(self.speed)
        self.fertility = self.canvas.settings['human']['fertility']
        self.energy = self.energyPlentitude()
        self.size = self.canvas.settings['human']['size']
        self.vision = self.canvas.settings['human']['vision']
        self.eaten = False
        self.survive = False
        self.alive = True
        self.beingChased = [False, None]
        self.determineSpeedFloat()
        self.canvas.canvas.itemconfigure(self.sprite, state='normal')
        self.changeSize()  # Change Size back To Normal
        return self

    def changeSize(self):
        self.canvas.canvas.coords(
            self.sprite,
            self.coord[0] - self.size,
            self.coord[1] - self.size,
            self.coord[0] + self.size,
            self.coord[1] + self.size,
        )

    def newRoundHuman(self):
        self.eaten = False
        self.survive = False
        self.alive = True
        self.moveTo = None
        self.chosenTarget = None
        self.ratioMovement = None
        self.energy = self.energyPlentitude()
        self.refreshRemainingMoves()
        self.beingChased = [False, None]
        self.changeSize()

    def readjustDirection(self, coord):
        if coord is None:
            return
        self.moveTo = coord
        self.lineRatioManage()
        pass

    def determineSpeedFloat(self):
        """ This is to determine pixel float movement speed.
         Basically to catch lets say speed = 10.5, but pixels are Integer values so Human can only go 10 or 11, not
         10.5 so this determines that we have a whole number of 10 and a have 0.5 floating so after doing 1 / 0.5
         we have 2 so every 2 rounds of movement we will then move this human 11 pixels instead of just 10. """
        if abs((self.speed + self.size) - int(self.speed + self.size)) == 0:
            self.holdOnToSpeedFloats = None
            return None
        else:
            self.holdOnToSpeedFloats = [0, int(1 / abs((self.speed + self.size) - int(self.speed + self.size)))]

    def refreshRemainingMoves(self):
        """ This will store the total moves for this turn of movements, will add an extra tile of movement if the float
         has caught up. """
        self.movesRemaining = int(self.speed + self.size)
        if self.holdOnToSpeedFloats is None:
            return
        if self.holdOnToSpeedFloats[0] >= self.holdOnToSpeedFloats[1]:
            self.movesRemaining += 1
            self.holdOnToSpeedFloats[0] -= self.holdOnToSpeedFloats[1]
        else:
            self.holdOnToSpeedFloats[0] += 1

    def energyPlentitude(self):
        return ((self.canvas.settings['game']['width'] +
                 self.canvas.settings['game']['height']) / 2) * self.canvas.settings['human']['energy']

    def isFoodEaten(self):
        if isinstance(type(self.chosenTarget), Human) and self.chosenTarget.alive is False:
            self.chosenTarget = None
        if self.chosenTarget is not None and self.chosenTarget.eaten:
            self.chosenTarget = None

    def printCoord(self):
        print(self.coord)

    def randomMove(self):
        """ Might want to look into getting the same coordinate to see if that will cause a crash. """
        if self.moveTo is not None:
            return
        while self.moveTo == self.coord or self.moveTo is None:
            self.moveTo = (
                random.randrange(
                    round(self.canvas.settings['game']['distFromEdge']),
                    round(self.canvas.settings['game']['width'] - self.canvas.settings['game']['distFromEdge'])
                ),
                random.randrange(
                    round(self.canvas.settings['game']['distFromEdge']),
                    round(self.canvas.settings['game']['height'] - self.canvas.settings['game']['distFromEdge'])
                )
            )
        self.lineRatioManage()

    def chosenTargetChosen(self):
        if isinstance(self.chosenTarget, Human):
            self.moveTo = self.chosenTarget.coord
            self.lineRatioManage()
            # print("Catch")
            # self.canvas.settings['game']['fps'] = 1
            pass
        elif self.chosenTarget is None:
            return
        else:
            self.moveTo = self.chosenTarget.coord
            self.lineRatioManage()

    def findCoord(self):
        """ Check For Suicidal Squares Possibly Appearing after they get some food This might just be a rare occurrence
        but if it gets too serious, I will probably have to go and fix it. """

        if self.chosenTarget is not None and self.chosenTarget.eaten is False:
            """ Suicide Issues will be caused because of this section Probably """
            return

        self.chosenTarget, run = findCoord(self)

        if run:
            self.beingChased = [True, self.chosenTarget]
            self.chosenTarget = None
            self.readjustDirection(vectorDirection(self))
        else:
            self.chosenTargetChosen()
        if self.moveTo is None:
            self.randomMove()
        return

    def lineRatioManage(self):
        self.ratioMovement = [self.moveTo[0] - self.coord[0], self.moveTo[1] - self.coord[1], 0, 0, [0, 0]]
        if self.moveTo[0] - self.coord[0] == 0 or self.moveTo[1] - self.coord[1] == 0:
            self.ratioMovement[2] = 0
        else:
            self.ratioMovement[2] = abs(self.ratioMovement[1] / self.ratioMovement[0])

        if self.ratioMovement[0] > 0:
            self.ratioMovement[4][0] = 1
        elif self.ratioMovement[0] == 0:
            self.ratioMovement[4][0] = 0
        else:
            self.ratioMovement[4][0] = -1

        if self.ratioMovement[1] > 0:
            self.ratioMovement[4][1] = 1
        elif self.ratioMovement[1] == 0:
            self.ratioMovement[4][1] = 0
        else:
            self.ratioMovement[4][1] = -1

    def move(self):
        if self.moveTo is None:
            self.findCoord()
        if self.ratioMovement is None or self.movesRemaining <= 0:
            return
        if abs(self.ratioMovement[3]) >= 1:
            if self.coord[1] != self.moveTo[1]:
                self.ratioMovement[3] -= self.ratioMovement[4][1]
                self.coord[1] += self.ratioMovement[4][1]
                self.canvas.canvas.move(self.sprite, 0, self.ratioMovement[4][1])
            else:
                self.coord[0] += self.ratioMovement[4][0]
                self.canvas.canvas.move(self.sprite, self.ratioMovement[4][0], 0)
        else:
            if self.coord[0] != self.moveTo[0]:
                self.ratioMovement[3] += (self.ratioMovement[4][1] * self.ratioMovement[2])
                self.coord[0] += self.ratioMovement[4][0]
                self.canvas.canvas.move(self.sprite, self.ratioMovement[4][0], 0)
            else:
                self.coord[1] += self.ratioMovement[4][1]
                self.canvas.canvas.move(self.sprite, 0, self.ratioMovement[4][1])
        self.movesRemaining -= 1

    def distanceFromEdge(self):
        coordDist = [
            self.coord[0],
            self.coord[1],
            self.canvas.settings['game']['width'] - self.coord[0],
            self.canvas.settings['game']['height'] - self.coord[1]
        ]
        shortest = [0, coordDist[0]]
        for num in range(1, 4):
            if coordDist[num] < shortest[1]:
                shortest = [num, coordDist[num]]
        if shortest[0] == 0:
            self.moveTo = [self.size, self.coord[1]]
        elif shortest[0] == 1:
            self.moveTo = [self.coord[0], self.size]
        elif shortest[0] == 2:
            self.moveTo = [self.canvas.settings['game']['width'] - round(self.size) + 2, self.coord[1]]
        else:
            self.moveTo = [self.coord[0], self.canvas.settings['game']['height'] - round(self.size) + 2]
        self.lineRatioManage()
        pass

    def whatIsHumanChasing(self):
        self.isFoodEaten()
        if self.moveTo is None:
            self.findCoord()

        if self.chosenTarget is not None:

            if isinstance(self.chosenTarget, type(self)):
                huntingHumanPrey(self)  # Function Under Class Human, Not a Method of Human

            else:
                foragingForFood(self)  # Function Under Class Human, Not a Method of Human

        elif self.beingChased[0]:
            runForTheHillsOrPredatorWillEatYou(self)
            # vectorDirection(self)
            pass

        else:
            prowling(self)  # Function Under Class Human, Not a Method of Human

    def collideWithTargetCoordinate(self):
        prowling(self)
        # try:
        #     if self.survive:
        #         return
        #     if isinstance(type(self), type(self.chosenTarget)):
        #         huntingHumanPrey(self)
        #         return
        #     else:
        #         foragingForFood(self)
        # except TypeError:
        #     print("hello")
        #     raise TypeError

    def killHuman(self):
        self.canvas.canvas.coords(self.sprite, 0, 0, 0, 0)
        if self.alive is False:
            print("I am A dumb Retard Fuck Fucker")
            EvoLogging.logFailureToDeleteStorage(self.canvas, self)
        self.alive = False
        self.canvas.storedHumans.append(self.canvas.usedHumans.pop(self.canvas.usedHumans.index(self)))
        # self.canvas.usedHumansDict.pop(self.sprite)
        self.canvas.canvas.itemconfigure(self.sprite, state='hidden')

    def sizeDifference(self, human):
        if 100 * (1 - human.size / self.size) > self.canvas.settings['game_rules']['food']['prey_size_difference']:
            return 1
        elif 100 * (1 - self.size / human.size) > self.canvas.settings['game_rules']['food']['prey_size_difference']:
            return -1
        else:
            return 0


def stillInProximity(self, target):
    """ Difference between this function and proximityAlert is that this one checks if the target can still be seen """
    if (self.coord[0] - target.coord[0]) ** 2 + (self.coord[1] - target.coord[1]) ** 2 <= (self.vision + (self.vision/2)) ** 2:
        return True
    return False


def proximityAlert(coord1, coord2, adjacencyDist=1):
    """
    :param coord1:
    :param coord2:
    :param adjacencyDist: Distance from each other in Pixels
    :return:
    """
    return True if -1 * adjacencyDist <= coord2[0] - coord1[0] <= adjacencyDist and \
                   -1 * adjacencyDist <= coord2[1] - coord1[1] <= adjacencyDist else False


def vectorDirection(self):
    tempMoveTo = [2 * self.coord[0] - self.beingChased[1].coord[0], 2 * self.coord[1] - self.beingChased[1].coord[1]]
    # print(self.coord, tempMoveTo, self.beingChased[1].coord)
    if self.size > tempMoveTo[0] > self.canvas.settings['game']['width'] - self.size:
        tempMoveTo[0] = (tempMoveTo[0] + self.beingChased[1].coord[0]) / 2

    if self.size > tempMoveTo[1] > self.canvas.settings['game']['height'] - self.size:
        tempMoveTo[1] = (tempMoveTo[1] + self.beingChased[1].coord[1]) / 2

    if self.size > tempMoveTo[0] > self.canvas.settings['game']['width'] - self.size or \
            self.size > tempMoveTo[1] > self.canvas.settings['game']['height'] - self.size:
        self.randomMove()
        tempMoveTo = self.moveTo
        """ Just in case both the evasive maneuver and the back up maneuver go out of bounds """

    return tempMoveTo


def findCoord(self):
    return findClosestID(self, gatherIDSet(self))


def gatherIDSet(self):
    listOfIDSprites = self.canvas.canvas.find_enclosed(
        self.coord[0] - self.size - self.vision,
        self.coord[1] - self.size - self.vision,
        self.coord[0] + self.size + self.vision,
        self.coord[1] + self.size + self.vision,
    )
    validIDList = {}
    for ID in listOfIDSprites:
        if ID != self.sprite:
            if ID in self.canvas.usedHumansDict and self.canvas.usedHumansDict[ID].alive is False:
                continue
            coord = self.canvas.canvas.coords(ID)
            coordinate = [
                round(coord[0] + self.canvas.settings['food']['size']),
                round(coord[1] + self.canvas.settings['food']['size'])
            ]
            if (self.coord[0] - coordinate[0]) ** 2 + (self.coord[1] - coordinate[1]) ** 2 <= self.vision ** 2:
                validIDList.update({ID: coordinate})
    return validIDList


def findClosestID(self, validIDList):
    """ Don't Really know the point of most of what closestID does, might choose to change it later, since I made most
    of it useless. """
    # ID, Distance, Object Address
    closestID = [0, None]

    for ID in validIDList:
        closestTemp = [0, None]

        if validIDList[ID][0] in self.canvas.usedFood and validIDList[ID][1] in self.canvas.usedFood[validIDList[ID][0]]:
            closestTemp[0] = abs(validIDList[ID][0] - self.coord[0]) + abs(validIDList[ID][1] - self.coord[1])
            closestTemp[1] = self.canvas.usedFood[validIDList[ID][0]][validIDList[ID][1]]

        elif ID in self.canvas.usedHumansDict:

            sizeDifference = self.sizeDifference(self.canvas.usedHumansDict[ID])

            if sizeDifference == -1:
                return self.canvas.usedHumansDict[ID], True
            elif sizeDifference == 0:
                continue
            else:
                closestTemp[0] = abs(validIDList[ID][0] - self.coord[0]) + abs(validIDList[ID][1] - self.coord[1])
                closestTemp[1] = self.canvas.usedHumansDict[ID]

        else:
            EvoLogging.addNewLogCoord(self, closestID, ID, validIDList)

        if closestTemp[1] is not None and (closestID[1] is None or closestTemp[0] < closestID[0]):
            closestID = closestTemp

    return closestID[1], False


def huntingHumanPrey(self):
    self.readjustDirection(self.chosenTarget.coord)
    # self.moveTo = self.chosenTarget.coord
    if stillInProximity(self, self.chosenTarget) and self.chosenTarget.alive is False:
        if proximityAlert(self.coord, self.moveTo, 2):  # 2 because predators can pounce on the prey, or something like that
            # We got the kill now lets do something about it
            self.energy += round(self.chosenTarget.energy / 100)
            self.chosenTarget.killHuman()
            self.chosenTarget = None
            self.moveTo = None
            self.eaten = True
            self.distanceFromEdge()
            pass
    else:
        self.moveTo = None
        self.chosenTarget = None
        self.ratioMovement = None
        self.findCoord()


def prowling(self):

    if proximityAlert(self.coord, self.moveTo):

        if self.eaten:
            self.survive = True

        else:
            self.chosenTarget = None
            self.moveTo = None
            self.ratioMovement = None
            self.findCoord()


def runForTheHillsOrPredatorWillEatYou(self):
    if stillInProximity(self, self.beingChased[1]):
        self.readjustDirection(vectorDirection(self))
    else:
        self.beingChased = [False, None]
        self.moveTo = None
    pass


def foragingForFood(self):
    if proximityAlert(self.coord, self.moveTo):
        if self.chosenTarget.eaten:
            self.chosenTarget = None
            self.moveTo = None
            self.ratioMovement = None
            self.findCoord()
        else:
            self.energy += self.chosenTarget.energy
            self.chosenTarget.hideFood()
            self.chosenTarget = None
            self.eaten = True
            self.distanceFromEdge()


if __name__ == "__main__":
    from Classes import gui
    GUI = gui.GUI()
    humans = Human(GUI, (50, 100), ("Evan", "Morrison"))
    humans.findCoord()
    pass

# 202 is old length, current 322
