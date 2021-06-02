class Human:

    def stringOfClass(self):
        return f"\tAge: {self.age}\n\tClass Information: {self}\n\tName: {self.fullName()}\n\tChildren: {self.children}\n" \
               f"\n" \
               f"\tCoordinate: {self.coord}\n\tMovement: {self.movement}\n\tRatioMovement: {self.ratioMovement}\n" \
               f"\n" \
               f"\tSpeed: {self.speed}\n\tFertility: {self.fertility}\n\tEnergy: {self.energy}\n\tSize: {self.size}\n\tVision: {self.vision}\n\tHoldOnToSpeedFloats: {self.holdOnToSpeedFloats}\n" \
               f"\tMovesRemaining: {self.movesRemaining}\n\tSprite ID: {self.sprite}\n" \
               f"\n" \
               f"\tRulesVariables: {self.ruleVariables}\n"

    def __init__(self, canvas, coord, name):
        self.speed = canvas.settings['human']['speed']
        self.holdOnToSpeedFloats = None
        self.movesRemaining = 0
        self.fertility = canvas.settings['human']['fertility']
        self.energy = self.energyPlentitude()
        self.size = canvas.settings['human']['size']
        self.vision = canvas.settings['human']['vision']

        self.age = 0
        self.name = name
        self.children = 0

        self.coord = coord
        self.movement = [None, None]  # [Object, Coordinates]
        self.ratioMovement = None

        self.canvas = canvas
        self.sprite = self.canvas.canvas.create_rectangle(
            coord[0]-self.size, coord[1]-self.size, coord[0] + self.size, coord[1] + self.size,
            fill='orange'
        )
        self.ruleVariables = {"eaten": False, "survive": False, "alive": True, "chased": False}

    def fullName(self):
        return self.name[0] + " " + self.name[1]

    def energyPlentitude(self):
        return ((self.canvas.settings['game']['width'] + self.canvas.settings['game']['height']) / 2) * self.canvas.settings['human']['energy']

    def SetDirection(self, coord):
        if coord is None:
            return
        self.movement[1] = coord
        self.lineRatioManage()
        pass

    def isBeingChased(self):
        return True if self.ruleVariables['chased'] else False

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

    def lineRatioManage(self):
        self.ratioMovement = [self.movement[1][0] - self.coord[0], self.movement[1][1] - self.coord[1], 0, 0, [0, 0]]
        self.ratioMovement[2] = 0 if self.movement[1][0] - self.coord[0] == 0 or self.movement[1][1] - self.coord[1] == 0 else abs(self.ratioMovement[1] / self.ratioMovement[0])
        self.ratioMovement[4][0] = ratioChange(self.ratioMovement[0])
        self.ratioMovement[4][1] = ratioChange(self.ratioMovement[1])

    def findCoord(self):
        pass

    def move(self):
        if self.movement[1] is None:
            self.findCoord()

        if self.ratioMovement is None or self.movesRemaining <= 0:
            return

        if abs(self.ratioMovement[3]) >= 1:
            if self.coord[1] != self.movement[1][1]:
                self.ratioMovement[3] -= self.ratioMovement[4][1]
                self.coord[1] += self.ratioMovement[4][1]
                self.canvas.canvas.move(self.sprite, 0, self.ratioMovement[4][1])
            else:
                self.coord[0] += self.ratioMovement[4][0]
                self.canvas.canvas.move(self.sprite, self.ratioMovement[4][0], 0)
        else:
            if self.coord[0] != self.movement[1][0]:
                self.ratioMovement[3] += (self.ratioMovement[4][1] * self.ratioMovement[2])
                self.coord[0] += self.ratioMovement[4][0]
                self.canvas.canvas.move(self.sprite, self.ratioMovement[4][0], 0)
            else:
                self.coord[1] += self.ratioMovement[4][1]
                self.canvas.canvas.move(self.sprite, 0, self.ratioMovement[4][1])
        self.movesRemaining -= 1


def ratioChange(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1


if __name__ == '__main__':
    import tkinter as tk
    from Classes import gui
    C = tk.Tk()
    G = gui.GUI()
    H = Human(G, )
