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

    def changeSize(self):
        self.canvas.canvas.coords(
            self.sprite,
            self.coord[0] - self.size,
            self.coord[1] - self.size,
            self.coord[0] + self.size,
            self.coord[1] + self.size,
        )

    def readjustDirection(self, coord):
        if coord is None:
            return
        self.moveTo = coord
        self.lineRatioManage()

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
