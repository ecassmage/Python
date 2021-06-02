from txtLists import settings
import random
import tkinter as tk
import time
settings = settings.settingsOpen()


def tempFunc(current, goTo, infoList, Canvas, obj):
    if abs(infoList[3]) >= 1:
        if current[1] != goTo[1]:
            infoList[3] -= infoList[4][1]
            current[1] += infoList[4][1]
            Canvas.move(obj, 0, infoList[4][1])
        else:
            current[0] += infoList[4][0]
            Canvas.move(obj, infoList[4][0], 0)
    else:
        if current[0] != goTo[0]:
            infoList[3] += (infoList[4][1] * infoList[2])
            current[0] += infoList[4][0]
            Canvas.move(obj, infoList[4][0], 0)
        else:
            current[1] += infoList[4][1]
            Canvas.move(obj, 0, infoList[4][1])
    return current, infoList


if __name__ == "__main__":
    tkCanvas = tk.Tk()
    canvas = tk.Canvas(tkCanvas, width=1000, height=1000)

    canvas.pack()
    currentPosition = [500, 500]
    square = canvas.create_rectangle(currentPosition[0], currentPosition[1], currentPosition[0]+10, currentPosition[1]+10)
    end = [
        random.randrange(
            round(settings['game']['distFromEdge']),
            round(settings['game']['width'] - settings['game']['distFromEdge'])
        ),
        random.randrange(
            round(settings['game']['distFromEdge']),
            round(settings['game']['height'] - settings['game']['distFromEdge'])
        )
    ]
    # end = [352, 787]
    info = [end[0] - currentPosition[0], end[1] - currentPosition[1], 0, 0, [0, 0]]
    info[2] = abs(info[1] / info[0])

    if info[0] > 0:
        info[4][0] = 1
    elif info[0] == 0:
        info[4][0] = 0
    else:
        info[4][0] = -1

    if info[1] > 0:
        info[4][1] = 1
    elif info[1] == 0:
        info[4][1] = 0
    else:
        info[4][1] = -1

    for i in range(1000):
        currentPosition, info = tempFunc(currentPosition, end, info, canvas, square)
        print(f"currentPosition: {currentPosition}, end: {end}, info: {info}")
        if currentPosition[0] - end[0] == 0 and currentPosition[1] - end[1] == 0:
            print("We Done")
            break
        tkCanvas.update()
        time.sleep(1/60)
    tkCanvas.mainloop()
