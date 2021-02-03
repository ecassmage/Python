import pygame
import math
from Mechanics import TrajectoryScript
import json
settings = json.load(open('settings.json', 'r'))


class Projectile:
    def __init__(self, window, coord, team, image):
        self.window = window
        self.x, self.y, self.xy = coord[0], coord[1] + 5, coord
        self.type, self.fire_type = 'projectile', 'line'
        self.range = 5
        self.distance_traveled = 0
        self.team = team
        self.speed = 7
        self.image = image
        self.rectangle = self.image.get_rect(x=self.x, y=self.y)

    def movement(self):
        if self.team == 'red':
            self.x += self.speed
        else:
            self.x -= self.speed
        self.distance_traveled += self.speed
        self.xy = (self.x, self.y)
        return

    def rect_position(self):
        return self.image.get_rect(x=self.x, y=self.y)


class Arrow(Projectile):
    def __init__(self, window, coord, team):
        self.damage = settings['soldiers']['archer']['damage']
        self.armor_pierce = settings['soldiers']['archer']['armor_pierce']
        self.max_range = settings['soldiers']['archer']['range']
        if team == 'red':
            image = pygame.image.load('Images/weapons/arrow_red.png')
            image = pygame.transform.scale(image, (15, 15))
        else:
            image = pygame.image.load('Images/weapons/arrow_blue.png')
            image = pygame.transform.scale(image, (15, 15))
            image = pygame.transform.flip(image, True, False)
        super().__init__(window, coord, team, image)


class CastleMissile(Projectile):
    def __init__(self, window, coord, team):
        self.damage = settings['castle']['damage']
        self.armor_pierce = settings['castle']['armor_pierce']
        self.max_range = settings['castle']['range']
        self.speed = 10
        self.scale = 25

        if team == 'red':
            image = pygame.image.load('Images/weapons/arrow_red.png')
            image = pygame.transform.scale(image, (self.scale, self.scale))
        else:
            image = pygame.image.load('Images/weapons/arrow_blue.png')
            image = pygame.transform.scale(image, (self.scale, self.scale))
            image = pygame.transform.flip(image, True, False)
        super().__init__(window, coord, team, image)
        self.y -= self.scale
        self.xy = (self.x, self.y)


class CatapultBall:
    def __init__(self, window, speed, team, x, y, dst):
        self.team, self.type = team, 'projectile'
        self.primed = False
        self.fire_type = 'arc'  # How it is fired as a trajectory. So here is an arc but it could be straight
        self.damage = 50  # Just Temporary
        self.armor_pierce = 10
        self.speed = speed
        self.range = 15
        self.distance_traveled = 0
        self.distance = dst
        # self.max_speed, self.max_distance = 80, 600  # Temp values as not implemented yet, For max_values
        self.window = window
        self.x_arc = (speed * math.cos(math.pi/6))/settings['fps']
        self.y_arc = (speed * math.sin(math.pi/6))
        self.x_start, self.y_start = x, y + (103 / 160) * (settings['window']['unit_size'] * 2)
        self.xy_arc = (self.x_arc, self.y_arc)
        self.x, self.y, self.xy = x, y, (x, y)
        self.gravity = settings['game']['gravity']/settings['fps']
        self.image = pygame.image.load('Images/weapons/rock.png')
        self.image = pygame.transform.scale(self.image, (7, 7))

    def movement(self):
        if self.team == 'red':
            self.x += self.x_arc
        else:
            self.x -= self.x_arc
        self.y -= (self.y_arc / settings['fps'])
        self.y_arc -= self.gravity
        self.distance_traveled += self.x_arc
        self.xy = (self.x, self.y)
        self.xy_arc = (self.x_arc, self.y_arc)
        if -5 <= self.y - self.y_start <= 5 and self.distance_traveled > self.distance:
            self.primed = True
        # TrajectoryScript.arc_movement(self)

    def rect_position(self):
        return self.image.get_rect(x=self.x, y=self.y)
