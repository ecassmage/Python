from multiprocessing import Process, Queue
from threading import Thread
import tkinter as tk
import time


class GUI:
    def __init__(self):
        self.tk = tk.Tk()
        self.Canvas = tk.Canvas(self.tk, width=1000, height=1000)
        self.Canvas.pack()


def update(gui):
    gui.tk.update()
    time.sleep(1/60)


def func(queue):
    C = GUI()
    x = 0
    while True:
        if not queue.empty():
            obj = queue.get(block=False, timeout=1/60)
        else:
            obj = ""
        if obj == "done":
            break
        elif obj == 'coord':
            obj = queue.get()
            print(obj)
            a = C.Canvas.create_rectangle(obj[0], obj[1], obj[2], obj[3], fill='red')
        x += 1
        update(C)

        print(x)


if __name__ == "__main__":
    qu = Queue()
    P = Process(target=func, args=(qu,))
    P.start()

    for i in range(10):
        if i == 5:
            qu.put('coord')
            qu.put([1, 2, 100, 250])
        else:
            qu.put("Good")
        time.sleep(1)
    qu.put("done")
    P.join()
