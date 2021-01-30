import pygame
import json
settings = json.load(open('settings.json', 'r'))


class Soldier:
    def __init__(self, window, team, coord, hp, speed, armor, cost, damage, image, arm_pier):
        self.hold = False
        self.window = window
        self.x, self.y, self.xy = coord[0], coord[1], coord
        self.hp = hp
        self.speed = speed
        self.armor = armor
        self.cost = cost
        self.damage = damage
        self.armor_pierce = arm_pier
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
        hp = settings['soldiers']['footman']['hp']
        speed = settings['soldiers']['footman']['speed']
        armor = settings['soldiers']['footman']['armor']
        cost = settings['soldiers']['footman']['cost']
        damage = settings['soldiers']['footman']['damage']
        pierce = damage = settings['soldiers']['footman']['armor_pierce']
        if team == 'red':
            img = 'Images/units/knight_red.png'
        else:
            img = 'Images/units/knight_blue.png'
        super().__init__(window, team, coord, hp, speed, armor, cost, damage, img, pierce)
        self.range = settings['soldiers']['footman']['range']
        self.cooldown = settings['soldiers']['footman']['cooldown']
        self.attacked_last = settings['soldiers']['footman']['cooldown']
        self.type = 'footman'
        self.ranged = False


class Tank(Soldier):
    def __init__(self, window, team, coord):
        hp = settings['soldiers']['tank']['hp']
        speed = settings['soldiers']['tank']['speed']
        armor = settings['soldiers']['tank']['armor']
        cost = settings['soldiers']['tank']['cost']
        damage = settings['soldiers']['tank']['damage']
        pierce = settings['soldiers']['tank']['armor_pierce']
        if team == 'red':
            img = 'Images/units/knight_red.png'
        else:
            img = 'Images/units/knight_blue.png'
        super().__init__(window, team, coord, hp, speed, armor, cost, damage, img, pierce)
        self.range = settings['soldiers']['tank']['range']
        self.cooldown = settings['soldiers']['tank']['cooldown']
        self.attacked_last = settings['soldiers']['tank']['cooldown']
        self.type = 'tank'
        self.ranged = False


class Archer(Soldier):
    def __init__(self, window, team, coord):
        hp = settings['soldiers']['archer']['hp']
        speed = settings['soldiers']['archer']['speed']
        armor = settings['soldiers']['archer']['armor']
        cost = settings['soldiers']['archer']['cost']
        damage = settings['soldiers']['archer']['damage']
        pierce = settings['soldiers']['archer']['armor_pierce']
        if team == 'red':
            img = 'Images/units/archer_red.png'
        else:
            img = 'Images/units/archer_blue.png'
        super().__init__(window, team, coord, hp, speed, armor, cost, damage, img, pierce)
        self.type = 'archer'
        self.projectile = 'Images/weapons/arrow.png'
        self.range = settings['soldiers']['archer']['range']
        self.cooldown = settings['soldiers']['archer']['cooldown']
        self.attacked_last = settings['soldiers']['archer']['cooldown']
        self.ranged = True


class Projectile:
    def __init__(self, window, coord, team, image):
        self.window = window
        self.x, self.y, self.xy = coord[0], coord[1] + 5, coord
        self.type = 'projectile'
        self.range = 5
        self.distance_traveled = 0
        self.team = team
        self.speed = 5
        self.image = image
        self.rectangle = self.image.get_rect(x=self.x, y=self.y)

    def movement(self):
        if self.team == 'red':
            self.x += self.speed
        else:
            self.x -= self.speed
        self.distance_traveled += self.speed
        self.xy = (self.x, self.y)
        # self.rectangle = self.image.get_rect(x=self.x, y=self.y)
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
        self.speed = 8
        if team == 'red':
            image = pygame.image.load('Images/weapons/arrow_red.png')
            image = pygame.transform.scale(image, (25, 25))
        else:
            image = pygame.image.load('Images/weapons/arrow_blue.png')
            image = pygame.transform.scale(image, (25, 25))
            image = pygame.transform.flip(image, True, False)
        super().__init__(window, coord, team, image)
