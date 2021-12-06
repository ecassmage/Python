from multiprocessing import Process, Queue
import HumanCls
import guiLogic
import FileOpener
import time
import signal
# Sadly No process/thread sharing is possible with windows.


def setupListOfHumans(jsonFile):
    listOfHumans = []
    for _ in range(jsonFile['human']['population']):
        listOfHumans.append(HumanCls.Human())
    return listOfHumans


class MainContainer:
    def __init__(self, main_gui, gui_main, Humans):
        self.main_gui = main_gui
        self.gui_main = gui_main
        self.Humans = Humans


def collectTime(startTime, endTime, hz, invisible=None):
    timeCalculate = (1 / hz) - (endTime - startTime)
    if invisible is not None:
        print(f"{timeCalculate}: {invisible} of {1/hz}")
        pass
    return timeCalculate if timeCalculate > 0 else 0


def nextIteration(HumanList, proximity=True):
    for human in HumanList:
        human.routine(HumanList, proximity)
        pass


def setupInitialGame(queueMAIN, queueGUI, file):
    listOfHumans = setupListOfHumans(file)
    for human in listOfHumans:
        queueMAIN.put(human)
        human.setID(queueGUI.get())
    queueMAIN.put("Done")
    return listOfHumans


def quitP(sig, sig2):
    exit()


def mainSwitchBoard(switch, container, sig=None, frame=None):
    # This is separated in case I want to add more signals.
    if switch == "ProgramClose-001":
        print("Closing Program")
        while not container.main_gui.empty():
            container.main_gui.get()
        while not container.gui_main.empty():
            container.gui_main.get()
        container.main_gui.close()
        container.gui_main.close()
        exit()
    elif switch == "QUIT":
        print("Closing Program")
        container.main_gui.close()
        container.gui_main.close()
        exit()


def main():
    fileInfo = FileOpener.openStg()

    main_gui = Queue()
    gui_main = Queue()

    process = Process(target=guiLogic.guiFunction, args=(main_gui, gui_main,))
    process.start()

    HumanList = setupInitialGame(main_gui, gui_main, fileInfo)
    mainContainer = MainContainer(main_gui, gui_main, HumanList)
    timeStart = -1 * (1 / fileInfo['window']['hz']) - 1
    HumanList[0].infect()
    truthFlipFlop = False
    signal.signal(signal.SIGINT, lambda sig, frm: mainSwitchBoard("QUIT", mainContainer, sig, frm))
    while True:
        timeEnd = time.time()
        truthFlipFlop += 1
        if not gui_main.empty():
            objGet = gui_main.get(block=False, timeout=collectTime(timeStart, timeEnd, fileInfo['window']['hz']))
            mainSwitchBoard(objGet, mainContainer)
        else:
            time.sleep(collectTime(timeStart, timeEnd, fileInfo['window']['hz'], "main"))
            timeStart = time.time()
            nextIteration(HumanList, truthFlipFlop)
            main_gui.put(HumanList)



    pass


if __name__ == '__main__':
    main()
    pass
