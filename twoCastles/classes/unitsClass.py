import pygame
import math
import json
settings = json.load(open('settings.json', 'r'))


class Soldier:
    def __init__(self, window, team, coord, image, soldat):
        self.can_move = False
        self.window = window
        self.x, self.y, self.xy = coord[0], coord[1], coord
        self.hp = settings['soldiers'][soldat]['hp']
        self.speed = settings['soldiers'][soldat]['speed'] / settings['fps']
        self.armor = settings['soldiers'][soldat]['armor']
        self.cost = settings['soldiers'][soldat]['cost']
        self.damage = settings['soldiers'][soldat]['damage']
        self.armor_pierce = settings['soldiers'][soldat]['armor_pierce']
        self.range = settings['soldiers'][soldat]['range']
        self.cooldown = settings['soldiers'][soldat]['cooldown']
        self.attacked_last = settings['soldiers'][soldat]['cooldown']
        self.team = team
        self.scale = settings['window']['unit_size']
        self.image = pygame.transform.scale(pygame.image.load(image), (self.scale, self.scale))
        if self.team == 'blue':
            self.image = pygame.transform.flip(self.image, True, False)
        self.rectangle = self.image.get_rect()

    def movement(self):
        if self.team == 'red':
            self.x += self.speed
        else:
            self.x -= self.speed
        self.rectangle = self.image.get_rect(x=self.x, y=self.y)
        self.xy = (self.x, self.y)
        return

    def rect_position(self):
        return self.image.get_rect(x=self.x, y=self.y)


class Footman(Soldier):
    def __init__(self, window, team, coord):
        if team == 'red':
            img = 'Images/units/knight_red.png'
        else:
            img = 'Images/units/knight_blue.png'
        super().__init__(window, team, coord, img, 'footman')
        self.type = 'footman'
        self.ranged = False
        self.y = self.y - self.scale
        self.xy = (self.x, self.y)


class Cheetah(Soldier):
    def __init__(self, window, team, coord):
        if team == 'red':
            img = 'Images/units/knight_red.png'
        else:
            img = 'Images/units/knight_blue.png'
        super().__init__(window, team, coord, img, 'cheetah')
        self.type = 'cheetah'
        self.ranged = False
        self.y = self.y - self.scale
        self.xy = (self.x, self.y)


class Tank(Soldier):
    def __init__(self, window, team, coord):
        if team == 'red':
            img = 'Images/units/knight_red.png'
        else:
            img = 'Images/units/knight_blue.png'
        super().__init__(window, team, coord, img, 'tank')
        self.type = 'tank'
        self.ranged = False
        self.y = self.y - self.scale
        self.xy = (self.x, self.y)


class Archer(Soldier):
    def __init__(self, window, team, coord):
        if team == 'red':
            img = 'Images/units/archer_red.png'
        else:
            img = 'Images/units/archer_blue.png'
        super().__init__(window, team, coord, img, 'archer')
        self.type = 'archer'
        self.projectile = 'Images/weapons/arrow.png'
        self.ranged = True
        self.y = self.y - self.scale
        self.xy = (self.x, self.y)


class Catapult(Soldier):
    def __init__(self, window, team, coord):
        if team == 'red':
            img = 'Images/units/catapult_red.png'
        else:
            img = 'Images/units/catapult_blue.png'
        super().__init__(window, team, coord, img, 'catapult')
        self.type = 'catapult'
        self.projectile = 'Images/weapons/arrow.png'
        self.ranged = True
        self.x_scale = 160
        self.y_scale = 103
        self.scale *= 2
        print(int(self.scale), self.scale * (self.y_scale/self.x_scale))
        self.image = pygame.transform.scale(
            pygame.image.load(img),
            (int(self.scale), math.floor(self.scale * (self.y_scale/self.x_scale)))
        )
        if self.team == 'blue':
            self.image = pygame.transform.flip(self.image, True, False)
        self.y -= math.floor(self.scale * (self.y_scale/self.x_scale))
        self.xy = (self.x, self.y)
