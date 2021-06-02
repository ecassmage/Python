import tkinter as tk
from Classes import human, food
import os
import random
from txtLists import settings


class GUI:
    def __init__(self):
        fNameDirectory = os.path.abspath(os.curdir) + '\\txtLists\\firstNames.txt'
        lNameDirectory = os.path.abspath(os.curdir) + '\\txtLists\\lastNames.txt'
        self.fNames = [name.replace('\n', '') for name in open(fNameDirectory, 'r')]
        self.lNames = [name.replace('\n', '').lower().capitalize() for name in open(lNameDirectory, 'r')]
        self.settings = settings.settingsOpen()
        self.humanPopulation = 0
        self.foodPopulation = 0
        self.tk = tk.Tk()
        self.geometry = f"{self.settings['game']['width']}x{self.settings['game']['height']}+10+10"
        self.tk.geometry(self.geometry)
        self.canvas = tk.Canvas(self.tk, width=self.settings['game']['width'], height=self.settings['game']['height'], bg='black')
        self.canvas.place(x=0, y=0, relx=0.001, rely=0.001)
        self.fps = self.settings['game']['fps']
        self.storedHumans = []
        self.storedFood = []
        self.usedHumans = []
        self.usedHumansDict = {}
        self.usedFood = {}
        self.addHuman(self.settings['pop']['StartingHumans'])
        self.addFood(self.settings['pop']['StartingFood'])
        self.refreshSpeed = self.settings['game']['refreshRate']
        self.megaFast = 0

    def storeHuman(self, newHuman):
        self.usedHumansDict.update({newHuman.sprite: newHuman})

    def addHuman(self, num, returnHuman=False):

        tempLength = len(self.usedHumans)

        while len(self.usedHumans) < num + tempLength:

            if len(self.storedHumans) > 0:
                newHuman = self.storedHumans.pop().resetHuman(list(outerRimOfGame(self.settings)), (random.choice(self.fNames), random.choice(self.lNames)))
            else:
                newHuman = human.Human(self, list(outerRimOfGame(self.settings)), (random.choice(self.fNames), random.choice(self.lNames)))
                self.storeHuman(newHuman)

            self.usedHumans.append(newHuman)
            self.storeHuman(newHuman)
            if returnHuman:
                return newHuman

    def newHumanParents(self, parent):
        if random.randrange(10) < 8:
            newName = (random.choice(self.fNames), parent.name[1])
        else:
            newName = (random.choice(self.fNames), random.choice(self.lNames))

        if len(self.storedHumans) > 0:
            newHuman = self.storedHumans.pop().resetHuman(list(outerRimOfGame(self.settings)), newName)

        else:
            newHuman = human.Human(self, list(outerRimOfGame(self.settings)), newName)
            self.storeHuman(newHuman)
        self.mutations(parent, newHuman)
        self.usedHumans.append(newHuman)

        newHuman.changeSize()

    def mutations(self, parent, newHuman):
        generalChance = self.settings['game_rules']['mutations']['chance_of_general_mutation']
        speedChance = self.settings['game_rules']['mutations']['chance_of_speed_mutation']
        visionChance = self.settings['game_rules']['mutations']['chance_of_vision_mutation']
        fertilityChance = self.settings['game_rules']['mutations']['chance_of_fertility_mutation']
        sizeChance = self.settings['game_rules']['mutations']['chance_of_size_mutation']
        newHuman.speed = parent.speed
        newHuman.vision = parent.vision
        newHuman.fertility = parent.fertility
        newHuman.size = parent.size

        if random.randrange(100) < generalChance + speedChance:
            if random.randint(0, 1) == 1:
                newHuman.speed += 0.2 * self.settings['game_rules']['mutations']['mutation_range']["speed_range"]
            else:
                newHuman.speed -= 0.2 * self.settings['game_rules']['mutations']['mutation_range']["speed_range"]

        if random.randrange(100) < generalChance + visionChance:
            if random.randint(0, 1) == 1:
                newHuman.vision += 0.2 * self.settings['game_rules']['mutations']['mutation_range']["vision_range"]
            else:
                newHuman.vision -= 0.2 * self.settings['game_rules']['mutations']['mutation_range']["vision_range"]

        if random.randrange(100) < generalChance + fertilityChance:
            if random.randint(0, 1) == 1:
                newHuman.fertility += 0.25 * self.settings['game_rules']['mutations']['mutation_range']["fertility_range"]
            else:
                newHuman.fertility -= 0.25 * self.settings['game_rules']['mutations']['mutation_range']["fertility_range"]

        if random.randrange(100) < generalChance + sizeChance:
            if random.randint(0, 1) == 1:
                newHuman.size += 0.1 * self.settings['game_rules']['mutations']['mutation_range']["size_range"]
            else:
                newHuman.size -= 0.1 * self.settings['game_rules']['mutations']['mutation_range']["size_range"]

    def sortFood(self, newFood):
        if newFood.coord[0] not in self.usedFood:
            self.usedFood.update({newFood.coord[0]: {newFood.coord[1]: newFood}})
        elif newFood.coord[1] not in self.usedFood[newFood.coord[0]]:
            self.usedFood[newFood.coord[0]].update({newFood.coord[1]: newFood})
        else:
            return False
        return True

    def sizeOfDict(self):
        numOfKeys = 0
        for yLevel in self.usedFood:
            numOfKeys += len(self.usedFood[yLevel])
        return numOfKeys

    def lookThroughDict(self, xCoord, yCoord):
        if xCoord in self.usedFood and yCoord in self.usedFood[xCoord]:
            return False
        return True

    def reDrawFood(self, Food):
        self.canvas.coords(Food.sprite, Food.coord[0], Food.coord[1], Food.coord[0]+Food.size, Food.coord[1]+Food.size)

    def addFood(self, num):
        number = self.sizeOfDict()
        tempLength = number
        while number < num + tempLength and number < ((self.settings['game']['width'] * self.settings['game']['height']) / 10):
            """ Prevents too much food to the point that nothing more 
            can be placed a lot of room so as to keep performance up. """
            x = random.randrange(
                round(self.settings['game']['distFromEdge']),
                round(self.settings['game']['width'] - self.settings['game']['distFromEdge'])
            )
            y = random.randrange(
                round(self.settings['game']['distFromEdge']),
                round(self.settings['game']['height'] - self.settings['game']['distFromEdge'])
            )
            if self.lookThroughDict(x, y):
                if len(self.storedFood) > 0:
                    self.sortFood(self.storedFood.pop().resetFood([x, y]))

                else:
                    self.sortFood(food.Food(self, [x, y]))

                number += 1
            else:
                continue
        pass


def outerRimOfGame(Settings):
    if random.randrange(2) == 1:
        x = random.randrange(Settings['human']['size'], Settings['game']['width'] - round(Settings['human']['size'] + 1))
        if random.randrange(2) == 1:
            y = Settings['game']['height'] - round(Settings['human']['size']) + 2
        else:
            y = Settings['human']['size']
    else:
        if random.randrange(2) == 1:
            x = Settings['game']['width'] - round(Settings['human']['size']) + 2
        else:
            x = Settings['human']['size']
        y = random.randrange(Settings['human']['size'], Settings['game']['height'] - round(Settings['human']['size'] + 1))
    """
    if x >= settings['game']['width'] - round(settings['human']['size']) or y >= settings['game']['height'] -\
            round(settings['human']['size']):
        print(f"x={x}, y={y} -> {settings['game']['width']}, {settings['game']['height']}")
    """
    return x, y
