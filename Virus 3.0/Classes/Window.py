import pygame
import Defines.Color


class Window:
    def __init__(self, settings):
        self.settings = settings
        if settings['window']['fullscreen']:
            self.window = pygame.display.set_mode((settings['window']['width'], settings['window']['height']), pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode((settings['window']['width'], settings['window']['height']))
        self.color = Defines.Color.getColor(settings['window']['bg'])
        self.window.fill(self.color)
        self.render([])
        self.fps = settings['window']['hz']

    def render(self, humans):
        self.window.fill(self.color)

        for human in humans:
            human.drawSprite(self.window)

        pygame.display.update()
