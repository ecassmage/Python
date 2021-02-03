from tkinter import *
import time
import math
tk = Tk()
window = Canvas(tk, width=1000, height=1000)
window.pack()


class Ball:
    def __init__(self, x, y, size):
        self.window = window
        self.x, self.y, self.xy = x, y, (x, y)
        self.image = self.window.create_oval(x - size/2, y - size/2, x + size/2, y + size/2, fill='red')
        self.radius = 50


def move_ball(obj):
    change_x = 10 * (math.cos(math.pi/12))
    print(change_x)
    print(obj.x**2)
    if obj.radius**2 - (obj.x - obj.radius)**2 > 0:
        y_change = math.sqrt(obj.radius ** 2 - (obj.x - obj.radius) ** 2)
    else:
        y_change = -math.sqrt(abs(obj.radius ** 2 - (obj.x - obj.radius) ** 2))
    print("THis", obj.radius**2 - (obj.x - obj.radius)**2)
    print(y_change)
    if obj.y < 750 or obj.x < 200:
        obj.window.move(obj.image, 15, -y_change)
        obj.x += 15
    else:
        obj.window.move(obj.image, 0, 0)
    return


def main():
    ball = Ball(50, 975, 50)
    window.update()
    while True:
        time.sleep(1/10)
        move_ball(ball)
        window.update()


if __name__ == '__main__':
    main()
    tk.mainloop()
