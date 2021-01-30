import pygame
import unitsClass
import json
settings = json.load(open('settings.json', 'r'))


class Castle:
    def __init__(self, image, window, coord, team, bounds):
        self.window = window
        self.image = pygame.transform.scale(image, (75, 75))
        self.x, self.y, self.xy = coord[0], coord[1], coord
        self.spawn_coordinate = (self.x + 22.5, self.y + 45)
        self.team, self.type = team, 'castle'
        self.hp = settings['castle']['hp']
        self.armor = settings['castle']['armor']
        self.range = settings['castle']['range']
        self.cooldown = settings['castle']['cooldown']
        self.attacked_last = settings['castle']['cooldown']
        self.bounds = bounds
        self.coins = 500
        self.coins_pot = 200
        self.score = 200
        self.recruitment_delay = settings['castle']['delay_recruit']
        self.lay_over = settings['castle']['delay_recruit']
        self.soldiers = []
        self.queue = []
        self.rectangle = self.image.get_rect(x=self.x, y=self.y)

    def generate_new_soldier(self, type_soldier):
        temp_obj = None
        if type_soldier == 'footman':
            temp_obj = unitsClass.Footman(self.window,
                                          self.team,
                                          self.spawn_coordinate,
                                          )
        elif type_soldier == 'archer':
            temp_obj = unitsClass.Archer(self.window,
                                         self.team,
                                         self.spawn_coordinate,
                                         )
        elif type_soldier == 'tank':
            temp_obj = unitsClass.Tank(self.window,
                                         self.team,
                                         self.spawn_coordinate,
                                         )

        self.soldiers.append(temp_obj)
        return

    def rect_position(self):
        return self.image.get_rect(x=self.x, y=self.y)
