import Files.FileOpener as FileOpener
import pygame

import Classes.Window
import Classes.Human

pygame.init()


def render(window):

    pass


def SetListData(window: Classes.Window.Window) -> (dict, list):
    humanList = list()
    humanDict = dict()

    for _ in range(window.settings['human']['start']['population']):
        newHuman = Classes.Human.Human()
        humanDict.update({newHuman.coord[0]: humanDict.get(newHuman.coord[0], []) + [newHuman]})
        humanList.append(newHuman)

    for i in range(window.settings['human']['start']['startingPopulationInfected']):
        humanList[i].infect(guarantee=True)

    return humanDict, humanList


def setIterableHumans(HumanList: list, HumanDict: dict, proximityCheck: list[4], newDay: bool):
    for human in HumanList:
        human.routine(HumanDict, True if proximityCheck[0] == proximityCheck[1] else False, newDay)
    proximityCheck[0] = proximityCheck[0] + 1 if proximityCheck[0] < proximityCheck[1] else 0


def main(window: Classes.Window.Window):
    clock = pygame.time.Clock()
    ShowWindow = True
    HumanDict, HumanList = SetListData(window)
    proximityLag = [0, window.settings['backEnd']['proximityLag']]
    dayNumber = 0
    newDay = False

    while ShowWindow:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ShowWindow = False

        if dayNumber >= window.settings['backEnd']['iterationRate']:
            dayNumber = 0
            newDay = True
        else:
            dayNumber += 1
            newDay = False

        setIterableHumans(HumanList, HumanDict, proximityLag, newDay)
        window.render(HumanList)
        clock.tick(window.fps)

    pass


if __name__ == '__main__':
    settingsMaster = FileOpener.openStg()
    windowMaster = Classes.Window.Window(settingsMaster)
    pygame.display.set_caption("Game Boy")
    # windowMaster = pygame.display.set_mode((1000, 1000))
    main(windowMaster)
    pass
