import time
import EvoLogging
from Classes import gui
import Logic
import RoundSurvivalScript
import PrintingConsoleInformation


def fpsTimer(start, frames, showFPS):

    DelayTime = time.time() - start

    if DelayTime < (1 / frames):
        time.sleep((1 / frames) - DelayTime)

        if DelayTime != 0 and showFPS:
            print(f"FPS: {frames}")

    elif showFPS:
        print(f"FPS: {round(1 / DelayTime)}")


def mainTasks(GUI):

    start = time.time()

    Logic.routineRoundChecks(GUI)

    fpsTimer(start, GUI.settings['game']['fps'], GUI.settings['dev']['fpsShow'])


def main(GUI):
    while True:

        mainTasks(GUI)

        for human in GUI.usedHumans:

            if human.survive is False:
                break

        else:
            if GUI.settings['dev']['statPrinting']:
                PrintingConsoleInformation.statCalculations(GUI, after=False)  # Library Import

            RoundSurvivalScript.endRoundChecks(GUI)

            if GUI.settings['dev']['statPrinting']:
                PrintingConsoleInformation.statCalculations(GUI)  # Library Import

            if len(GUI.usedHumans) == 0:
                break
    print("We Encountered an extinct Population")
    exit()


if __name__ == '__main__':

    EvoLogging.ReFormatLoggingCoordFolder()

    Canvas = gui.GUI()
    Canvas.tk.update()

    # Canvas.usedHumans[0].size = 5
    # Canvas.usedHumans[0].vision = 10
    # Canvas.usedHumans[1].vision = 10
    # Canvas.usedHumans[1].fertility = 30
    # Canvas.usedHumans[0].alive = False
    # Canvas.usedHumans[0].changeSize()

    PrintingConsoleInformation.statCalculations(Canvas)  # Library Import

    main(Canvas)

    Canvas.tk.mainloop()
