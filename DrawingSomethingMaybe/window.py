import pygame


class Window:
    def __init__(self, dimensions: tuple, kwargs):
        self.window = pygame.display.set_mode(
            dimensions,
            False if 'fullscreen' not in kwargs else kwargs['fullscreen']
        )

        self.menuBar = None

    def addMenuItem(self, newItem: str):
        pass
