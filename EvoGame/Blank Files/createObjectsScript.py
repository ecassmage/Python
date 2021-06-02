from Classes import human, food
import os
import random
from txtLists import settings
import Logic
settings = settings.settingsOpen()


def outerRimOfGame():
    if random.randrange(2) == 1:
        x = random.randrange(settings['human']['size'], settings['game']['width'] - round(settings['human']['size']))
        if random.randrange(2) == 1:
            y = settings['game']['height'] - round(settings['human']['size'])
        else:
            y = settings['human']['size']
    else:
        if random.randrange(2) == 1:
            x = settings['game']['width'] - round(settings['human']['size'])
        else:
            x = settings['human']['size']
        y = random.randrange(settings['human']['size'], settings['game']['height'] - round(settings['human']['size']))
    """
    if x >= settings['game']['width'] - round(settings['human']['size']) or y >= settings['game']['height'] -\
            round(settings['human']['size']):
        print(f"x={x}, y={y} -> {settings['game']['width']}, {settings['game']['height']}")
    """
    return x, y


def createHumans(canvas, num, listOfHumans=None):
    listOfHumans = [] if listOfHumans is None else listOfHumans
    fNameDirectory = os.path.abspath(os.curdir) + '\\txtLists\\firstNames.txt'
    lNameDirectory = os.path.abspath(os.curdir) + '\\txtLists\\lastNames.txt'
    fNames = [name.replace('\n', '') for name in open(fNameDirectory, 'r')]
    lNames = [name.replace('\n', '').lower().capitalize() for name in open(lNameDirectory, 'r')]

    while len(listOfHumans) < num:
        newHuman = human.Human(canvas, tuple(outerRimOfGame()), (random.choice(fNames), random.choice(lNames)))
        listOfHumans.append(newHuman)

    del fNames
    del lNames
    return listOfHumans


def createFood(canvas, num, foodDict=None):
    foodDict = {} if foodDict is None else foodDict

    def sizeOfDict():
        numOfKeys = 0
        for yLevel in foodDict:
            numOfKeys += len(yLevel)
        return numOfKeys

    def sortFood():
        if newFood.coord[0] not in foodDict:
            foodDict.update({newFood.coord[0]: {newFood.coord[1]: newFood}})
        elif newFood.coord[1] not in foodDict[newFood.coord[0]]:
            foodDict[newFood.coord[0]].update({newFood.coord[1]: newFood})
        else:
            return False
        return True

    def lookThroughDict(xCoord, yCoord):
        if xCoord in foodDict and yCoord in foodDict[xCoord]:
            return False
        return True

    number = sizeOfDict()
    while number < num and number < ((settings['game']['width'] * settings['game']['height']) / 10):
        """ Prevents too much food to the point that nothing more 
        can be placed a lot of room so as to keep performance up. """
        x = random.randrange(
            round(settings['game']['distFromEdge']), round(settings['game']['width'] - settings['game']['distFromEdge']))
        y = random.randrange(
            round(settings['game']['distFromEdge']), round(settings['game']['height'] - settings['game']['distFromEdge']))
        if lookThroughDict(x, y):
            newFood = food.Food(canvas, (x, y))
            sortFood()
            number += 1
        else:
            continue

    return foodDict


if __name__ == "__main__":
    humans = createHumans(None, settings['pop']['human'])
    food = createFood(None, settings['pop']['food'])
    Logic.checkMoves(humans[0], food)
    for human in humans:
        human.printCoord()
    pass
