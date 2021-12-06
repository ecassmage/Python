import HumanCls
import GUI
import time
import tkinter as tk
import signal


def collectTimeGUI(startTime, endTime, hz, invisible=None):
    timeCalculate = (1 / hz) - (endTime - startTime)
    if invisible is not None:
        print(f"{timeCalculate}: {invisible} of {1/hz}")
        pass
    return timeCalculate if timeCalculate > 0 else 0


def guiSetup(queueMAIN, queueGUI, gui):
    while True:
        obj = queueMAIN.get()
        if obj == "Done":
            break
        queueGUI.put(obj.drawSprite(gui.win))


def getMostRecent(queue):
    obj = None
    while not queue.empty():
        obj = queue.get()
    return obj


def guiSignals(procedure, sig, frame):
    exit()
    # match procedure:
    #     case "QUIT CODE: SIGINT":
    #         print("GUI QUITTING")
    #         exit()


def guiFunction(main_gui, gui_main):
    signal.signal(signal.SIGINT, lambda sig, frm: guiSignals("QUIT CODE: SIGINT", sig, frm))
    gui = GUI.GUI(gui_main)
    guiSetup(main_gui, gui_main, gui)

    timeStart = -1 * (1 / gui.stg['window']['hz']) - 1
    while True:
        try:
            gui.checkCoordinates(getMostRecent(main_gui))
            timeEnd = time.time()
            time.sleep(collectTimeGUI(timeStart, timeEnd, gui.stg['window']['hz'], "gui"))
            timeStart = time.time()
            gui.update()

        except tk.TclError:
            gui_main.put("ProgramClose-001")
            time.sleep(0.2)
            exit()

        except KeyboardInterrupt:
            gui_main.close()
            main_gui.close()
            exit()
