import random
from txtLists import settings
settings = settings.settingsOpen()


def endRoundChecks(GUI):
    GUI.tk.update()
    for human in reversed(GUI.usedHumans):
        human.age += 1
        human.newRoundHuman()
        babyMaker(GUI, human, birthRate(human))
    newFoodGrowth(GUI)


def babyMaker(GUI, parent, num):
    for i in range(num):
        GUI.newHumanParents(parent)
        parent.children += 1


def birthRate(human):
    if random.randint(1, 100) < (5 + ((4 * human.fertility) / 5)) * human.canvas.settings['game_rules']['birth_rate_multiplier']:
        numOfBabies = ceil((human.fertility ** 3) / (1000000 / human.canvas.settings['game_rules']['number_of_babies']))
        if numOfBabies == 0:
            return 1
        return numOfBabies
    return 0


def ceil(num):
    newNum = int(num)
    if num - newNum <= 0:
        return newNum
    else:
        return newNum + 1


def newFoodGrowth(Screen):
    # currentAmountOfFood = len(Screen.usedFood)
    foodToMatch = len(Screen.usedFood) + random.randrange(
        -1 * abs(Screen.settings["game_rules"]["food"]['food_range']),
        abs(Screen.settings["game_rules"]["food"]['food_range'])
    )
    if foodToMatch < Screen.settings["game_rules"]["food"]['minimum_food']:
        foodToMatch = Screen.settings["game_rules"]["food"]['minimum_food']
    elif foodToMatch > Screen.settings["game_rules"]["food"]['maximum_food']:
        foodToMatch = Screen.settings["game_rules"]["food"]['maximum_food']
    listOfCoordinates = list(Screen.usedFood)
    # print(listOfCoordinates)
    for coordX in listOfCoordinates:
        listOfY = list(Screen.usedFood[coordX])
        # print(listOfY)
        for coordY in listOfY:
            Screen.usedFood[coordX][coordY].hideFood()
    Screen.addFood(foodToMatch)
