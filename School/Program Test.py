from multiprocessing import Process, Queue
import tkinter as tk
import time


class GUI:
    def __init__(self, coord):
        self.tk = tk.Tk()
        self.canvas = tk.Canvas(self.tk, width=2000, height=1200, bg='orange')
        self.obj = self.canvas.create_rectangle(coord[0], coord[1], coord[2], coord[3], fill='red')

    def pack(self):
        self.canvas.pack()

    def update(self):
        self.tk.update()

    def newCoord(self, coord):
        self.canvas.coords(self.obj, coord[0], coord[1], coord[2], coord[3])


def GUIUpdateFunction(queue, coord):
    Graphics = GUI(coord)
    Graphics.pack()
    while True:
        if not queue.empty():
            obj = queue.get(block=False, timeout=1/60)
            if obj == 'break':
                break
            else:
                Graphics.newCoord(obj)
        Graphics.update()
        time.sleep(1/60)


if __name__ == '__main__':
    pObj = [0, 0, 10, 10]
    queue = Queue()
    P = Process(target=GUIUpdateFunction, args=(queue, pObj,))
    P.start()

    while True:
        if pObj[2] > 1000:
            break
        else:
            pObj = [pObj[0]+1, pObj[1]+1, pObj[2]+1, pObj[3]+1]
            queue.put(pObj)
        time.sleep(1/60)
    queue.put("break")
