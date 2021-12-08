from PyQt5.QtWidgets import QApplication, QMainWindow
import time
import pygame
import random
pygame.init()


def render(window, listOfRectangles, rex):
    window.fill((0, 54, 124))
    listOfRectangles = createList(len(listOfRectangles), window)
    rr = rex.center
    rex = pygame.draw.circle(window, (255, 0, 0), rex.center, abs((rex.left - rex.right) / 2))
    pygame.display.update()


def r(upper):
    return random.randrange(upper)


def createList(number, surface):
    lis = []
    for i in range(number):
        middle = (r(2560), r(1440))
        lis.append(pygame.draw.rect(surface, (255, 200, 0), pygame.Rect(middle[0], middle[1], 2, 2)))
    return lis


def pickleQ(gy):
    pass


def main(window):
    showScreen = True
    clock = pygame.time.Clock()
    fps = 60
    listOfRect = createList(5000, window)
    numberOfFrames = 0
    start = time.time()
    rex = pygame.draw.circle(window, (255, 0, 0), (100, 100), 15)
    while showScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showScreen = False
        render(window, listOfRect, rex)
        rex.move_ip(1, 1)
        clock.tick(fps)
        numberOfFrames += 1
        if time.time() - start > 1:
            print(f"fps: {numberOfFrames}")
            numberOfFrames = 0
            start = time.time()


if __name__ == '__main__':
    canvas = pygame.display.set_mode((2500, 1400))
    canvas.fill('#000000')
    # canvas.fill(pygame.RED())
    pygame.display.set_caption("Practice Test")  # Program Title
    main(canvas)
