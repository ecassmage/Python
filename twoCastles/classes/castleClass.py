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
        self.team = team
        self.health = 1000
        self.bounds = bounds
        self.coins = 500
        self.score = 200
        self.recruitment_delay = settings['castle']['delay_recruit']
        self.lay_over = settings['castle']['delay_recruit']
        self.soldiers = []
        self.queue = []

    def generate_new_soldier(self, type_soldier):
        temp_obj = None
        if type_soldier == 'footman':
            temp_obj = unitsClass.Footman(self.window,
                                          self.team,
                                          self.spawn_coordinate,
                                          settings['soldiers']['footman']['hp'],
                                          settings['soldiers']['footman']['speed'],
                                          settings['soldiers']['footman']['armor'],
                                          settings['soldiers']['footman']['cost'],
                                          settings['soldiers']['footman']['damage'],
                                          )
        elif type_soldier == 'archer':
            temp_obj = unitsClass.Archer(self.window,
                                         self.team,
                                         self.spawn_coordinate,
                                         settings['soldiers']['archer']['hp'],
                                         settings['soldiers']['archer']['speed'],
                                         settings['soldiers']['archer']['armor'],
                                         settings['soldiers']['archer']['cost'],
                                         settings['soldiers']['archer']['damage'],
                                         )

        self.soldiers.append(temp_obj)
        return
