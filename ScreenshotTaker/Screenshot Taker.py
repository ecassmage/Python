import pyautogui
import time


def printScreenDrag(num):
    pyautogui.press("printscreen")
    time.sleep(1)
    pyautogui.moveTo(10, 10)
    pyautogui.dragTo(2550, 1430, duration=0.3, button='left')
    # goToClipBoard(num)
    goToActionClip(num)


def justSteamScreenshot():
    pyautogui.press("f12")


def goToClipBoard(num):
    time.sleep(3)
    pyautogui.click(2350, 1290)
    saveToFolder(num)


def goToActionClip(num):
    time.sleep(1)
    pyautogui.press("winleft")
    time.sleep(1)
    pyautogui.click(2510, 1410)
    time.sleep(1)
    pyautogui.click(2300, 230)
    saveToFolder(num)


def saveToFolder(num):
    time.sleep(1.5)
    pyautogui.keyDown("CTRL")
    pyautogui.press("s")
    pyautogui.keyUp("CTRL")
    time.sleep(3)
    pyautogui.typewrite(f"Stellaris Game - Screenshot {num}")
    pyautogui.press("ENTER")
    time.sleep(1)
    pyautogui.click(2536, 13)
    time.sleep(1.5)


def positionOnScreen():
    print(pyautogui.position())
    exit()


def pauseGame(state):
    pyautogui.click(2475, 10)
    pyautogui.moveTo(1275, 725)
    if state == "pause":
        time.sleep(3)


def subRoutine(num, state):
    if simple:
        justSteamScreenshot()
    else:
        if inGame:
            pauseGame('pause')
        printScreenDrag(num)
        if state:
            pauseGame('play')


if __name__ == '__main__':

    print(pyautogui.size())
    # positionOnScreen()

    ScreenShotDelay = 1
    timeScale = 1
    PicturesTaken, CurrentScreenshot = 0, 0
    inGame = True
    simple = True
    time.sleep(4)

    subRoutine(CurrentScreenshot + PicturesTaken, inGame)
    if inGame:
        pauseGame('play')
    PicturesTaken += 1
    start = time.time()

    while True:
        if ScreenShotDelay * timeScale <= time.time() - start:

            subRoutine(CurrentScreenshot + PicturesTaken, inGame)
            PicturesTaken += 1
            print(f"We just Saved ScreenShot {PicturesTaken}")
            start = time.time()


