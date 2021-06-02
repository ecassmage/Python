from multiprocessing import Process
from threading import Thread
import random
import tkinter as tk


class Screen:
    def __init__(self):
        self.current = 0
        self.screen = tk.Tk()
        self.zero = tk.Canvas(self.screen, width=1000, height=1000, bg='orange')
        self.one = tk.Canvas(self.screen, width=1000, height=1000, bg='orange')
        self.two = tk.Canvas(self.screen, width=1000, height=1000, bg='orange')
        self.zero.pack()

    def update(self):
        # self.screen.update()
        # return
        if self.current == 0:
            self.zero.pack_forget()
            self.one.pack()
            self.current = 1
        elif self.current == 1:
            self.one.pack_forget()
            self.two.pack()
            self.current = 2
        elif self.current == 2:
            self.two.pack_forget()
            self.zero.pack()
            self.current = 0
        self.screen.update()

    def move(self, human):
        # self.zero.coords(human.sprite2, human.coord[0], human.coord[1], human.coord[0] + 5, human.coord[1] + 5)
        # return
        if self.current == 0:
            self.two.coords(human.sprite2, human.coord[0], human.coord[1], human.coord[0]+5, human.coord[1]+5)
        elif self.current == 1:
            self.zero.coords(human.sprite0, human.coord[0], human.coord[1], human.coord[0]+5, human.coord[1]+5)
        elif self.current == 2:
            self.one.coords(human.sprite1, human.coord[0], human.coord[1], human.coord[0]+5, human.coord[1]+5)


class Human:
    def __init__(self, screen, coord, goto):
        self.coord = coord
        self.goto = goto
        self.sprite0 = screen.zero.create_rectangle(self.coord[0], self.coord[1], self.coord[0]+5, self.coord[1]+5, fill='green')
        self.sprite1 = screen.one.create_rectangle(self.coord[0], self.coord[1], self.coord[0]+5, self.coord[1]+5, fill='green')
        self.sprite2 = screen.two.create_rectangle(self.coord[0], self.coord[1], self.coord[0]+5, self.coord[1]+5, fill='green')


def moveHuman(humans):
    for human in humans:
        if human.coord[0] - human.goto[0] == 0:
            human.coord[1] += (human.coord[1] - human.goto[1]) / abs(human.coord[1] - human.goto[1])
        elif human.coord[1] - human.goto[1] == 0:
            human.coord[0] += (human.coord[0] - human.goto[0]) / abs(human.coord[0] - human.goto[0])
        elif abs(human.coord[0] - human.goto[0]) < abs(human.coord[1] - human.goto[1]):
            human.coord[1] += ((human.coord[1] - human.goto[1]) / abs(human.coord[1] - human.goto[1]))
        else:
            human.coord[0] += ((human.coord[0] - human.goto[0]) / abs(human.coord[0] - human.goto[0]))


def makeNewFood(screen):
    listY = []
    while len(listY) != 1000:
        coords = [random.randrange(0, 1000), random.randrange(0, 1000)]
        goto = [random.randrange(0, 1000), random.randrange(0, 1000)]
        listY.append(Human(screen, coords, goto))
    return listY


def goo(screen, humans):
    for human in humans:
        screen.move(human)


def main():
    S = Screen()
    humans = makeNewFood(S)
    for i in range(100000):
        # process = Thread(target=moveHuman, args=(humans,))
        # process.start()
        moveHuman(humans)
        goo(S, humans)
        S.update()
        # process.join()

    S.screen.mainloop()
    pass


if __name__ == '__main__':
    main()
    pass
