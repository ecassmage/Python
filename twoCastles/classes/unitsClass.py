import time
import projectiles
import pygame
import json
settings = json.load(open('settings.json', 'r'))


class Soldier:
    def __init__(self, window, team, coord, hp, speed, armor, cost, damage, image):
        self.hold = False
        self.window = window
        self.x, self.y, self.xy = coord[0], coord[1], coord
        self.hp = hp
        self.speed = speed
        self.armor = armor
        self.cost = cost
        self.damage = damage
        self.team = team
        self.scale = settings['window']['unit_size']
        self.image = pygame.transform.scale(pygame.image.load(image), (self.scale, self.scale))
        if self.team == 'blue':
            self.image = pygame.transform.flip(self.image, True, False)

    def movement(self):
        if self.team == 'red':
            self.x += self.speed
        else:
            self.x -= self.speed

        self.xy = (self.x, self.y)
        return


class Footman(Soldier):
    def __init__(self, window, team, coord, hp, speed, armor, cost, damage):
        if team == 'red':
            img = 'Images/units/knight_red.png'
        else:
            img = 'Images/units/knight_blue.png'
        super().__init__(window, team, coord, hp, speed, armor, cost, damage, img)
        self.range = settings['soldiers']['footman']['range']
        self.cooldown = settings['soldiers']['footman']['cooldown']
        self.attacked_last = settings['soldiers']['footman']['cooldown']
        self.type = 'footman'
        self.ranged = False


class Archer(Soldier):
    def __init__(self, window, team, coord, hp, speed, armor, cost, damage):
        img = 'Images/units/knight.png'
        super().__init__(window, team, coord, hp, speed, armor, cost, damage, img)
        self.type = 'archer'
        self.projectile = 'Images/weapons/arrow.png'
        self.range = settings['soldiers']['archer']['range']
        self.cooldown = settings['soldiers']['archer']['cooldown']
        self.attacked_last = settings['soldiers']['archer']['cooldown']
        self.ranged = True


class Projectile:
    pass


class Arrow(Projectile):
    def __init__(self, window, team, coord):
        self.window = window
        self.x, self.y, self.xy = coord[0], coord[1], coord
        self.damage = settings['soldiers']['archer']['damage']
        self.type = 'projectile'
        self.speed = 5
        self.team = team
        self.range = 5
        self.distance_traveled = 0
        if team == 'red':
            self.image = pygame.image.load('Images/weapons/arrow_red.png')
            self.image = pygame.transform.scale(self.image, (15, 15))
        else:
            self.image = pygame.image.load('Images/weapons/arrow_blue.png')
            self.image = pygame.transform.scale(self.image, (15, 15))
            self.image = pygame.transform.flip(self.image, True, False)

    def movement(self):
        if self.team == 'red':
            self.x += self.speed
        else:
            self.x -= self.speed
        self.distance_traveled += self.speed
        self.xy = (self.x, self.y)
        return

