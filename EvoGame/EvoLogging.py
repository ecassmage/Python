import os


def reFormatAFolder(folderDirectory, fileName):
    if os.path.exists(os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory) and os.path.exists(os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory + "\\" + fileName + " 1.txt"):
        # Hillo = os.listdir(os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory)
        if len(os.listdir(os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory)) == 10:
            os.remove(os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory + "\\" + fileName + " 10.txt")
        # Hillo2 = os.listdir(os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory)
        for number, txtFile in enumerate(reversed(os.listdir(os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory))):
            newName = (txtFile.replace('.txt', '').split(' ')[0]) + " " + str(len(os.listdir(os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory)) - number + 1) + ".txt"
            os.rename(
                os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory + "\\" + txtFile,
                os.path.dirname(os.path.abspath(os.curdir)) + "\\" + folderDirectory + "\\" + newName
            )


def ReFormatLoggingCoordFolder():
    reFormatAFolder("EvoGame\\Logs\\CoordLogs", "findCoordLog")
    reFormatAFolder("EvoGame\\Logs\\FailureToDelete", "FailureToDeleteLog")


def addNewLogCoord(self, IDSet, ID, validIDList):
    if not os.path.exists(os.path.dirname(os.path.abspath(os.curdir)) + "\\EvoGame\\Logs\\CoordLogs"):
        os.makedirs(os.path.dirname(os.path.abspath(os.curdir)) + "\\EvoGame\\Logs\\CoordLogs")
    logFile = open("Logs\\CoordLogs\\findCoordLog 1.txt", 'a')
    if len(open("Logs\\CoordLogs\\findCoordLog 1.txt").readlines()) > 2:
        logFile.write("\n\n")
    logFile.write(
        f"Human Name: {self.fullName()}\n"
        f"\tSprite ID: {self.sprite}\n"
        f"\tClass Type: {type(self)}\n"
        f"\tCoord: {self.coord}\n"
        f"\tSquare Coord: {self.canvas.canvas.coords(self.sprite)}\n"
        f"\tMoveTo: {self.moveTo}\n"
        f"\tChildren: {self.children}\n"
        f"\tMutations: Speed -> {self.speed}, Vision -> {self.vision}, Size -> {self.size}, Fertility -> {self.fertility}, energy: {self.energy}\n"
        f"\tState: {self.alive}, Eaten: {self.eaten}, ChosenTarget: {self.chosenTarget}\n"
        f"\n"
        f"\tself Sprite ID: {self.sprite} -> "
        f"Conflict Sprite ID: {ID}\n"
        f"\tConflict ClosestID: {IDSet}\n"
        f"\tSquare Coord: {self.canvas.canvas.coords(ID)}\n"
        f"\tID List: {validIDList}\n"
    )
    if IDSet[1] is not None:
        logFile.write(f"\n\n {IDSet[1].stringClass()}\n\n" + self.stringClass())
        logFile.close()
        exit()
    logFile.close()
    print("Printed")


def logFailureToDeleteStorage(Screen, failedHuman):
    if not os.path.exists(os.path.dirname(os.path.abspath(os.curdir)) + "\\EvoGame\\Logs\\FailureToDelete"):
        os.makedirs(os.path.dirname(os.path.abspath(os.curdir)) + "\\EvoGame\\Logs\\FailureToDelete")
    logFile = open("Logs\\FailureToDelete\\FailureToDeleteLog 1.txt", 'w')
    logFileNewString = f"Failed Human Class Object\nName: {failedHuman.fullName()}\n{failedHuman.makeStringOfObject()}\n"
    logFileNewString += "\n\nScreen.usedHumans\n"
    for human in Screen.usedHumans:
        logFileNewString += f"Name: {human.fullName()}\n"
        logFileNewString += human.stringClass()
        logFileNewString += "\n"
    logFileNewString += "\n\nScreen.storedHumans\n"
    for human in Screen.storedHumans:
        logFileNewString += f"Name: {human.fullName()}\n"
        logFileNewString += human.stringClass()
        logFileNewString += "\n"
    logFileNewString += "\n\nScreen.usedFood\n"
    for x in Screen.usedFood:
        for y in Screen.usedFood[x]:
            logFileNewString += Screen.usedFood[x][y].stringClass()
            logFileNewString += "\n"
    logFileNewString += "\n\nScreen.storedFood\n"
    for food in Screen.storedFood:
        logFileNewString += food.stringClass()
        logFileNewString += "\n"
    logFile.write(logFileNewString)
    logFile.close()
    print("Hello World")
    pass
