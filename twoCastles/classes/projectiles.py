import pygame


class Arrow:
    def __init__(self, team, x, y, damage):
        self.x, self.y, self.xy = x, y, (x, y)
        self.speed = 45
        self.damage = damage
        if team == 'red':
            self.direction = 'right'
        else:
            self.direction = 'left'
        self.image = pygame.image.load('Images/weapons/arrow.png')

    def _move(self):
        if self.direction == 'right':
            self.x -= self.speed
        else:
            self.x += self.speed
