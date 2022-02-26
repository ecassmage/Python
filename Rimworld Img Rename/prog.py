import os


def getNewest(directory, name: str, end: str):
    newestFile = ''
    removeFiles = []
    iteration = 0
    while True:
        iteration += 1
        schName = name + '-alt' + str(iteration) + end
        if os.path.exists(directory + '/' + schName):
            if newestFile != '':
                removeFiles.append(newestFile)
            newestFile = schName
        else:
            break
    return newestFile, removeFiles


def main():
    directory = 'F:/TimeLapse/Game2/tuque'
    # directory = 'Test'
    listOfFiles = [f for f in os.listdir(directory)]
    numberOfFilesRemoved = 0
    for file in listOfFiles:
        if 'alt' in file:
            coordName = file[0:file.rfind("alt")-1]
            endCode = file[file.rfind('.'):]
            newLine, remLines = getNewest(directory, coordName, endCode)
            if newLine != '':
                numberOfFilesRemoved += len(remLines)
                for fileToRemove in remLines:
                    os.remove(directory + "/" + fileToRemove)
                os.remove(directory + "/" + coordName + endCode)
                os.rename(directory + "/" + newLine, directory + "/" + coordName + endCode)

    print(f"{numberOfFilesRemoved} were removed")
    pass


if __name__ == "__main__":
    main()
    pass
