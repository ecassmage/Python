"""Why have this here, Well because it is ugly code that I don't really want to have to look at ever"""
from Mechanics import boundsMechanics
from classes import castleClass
import pygame
import json
settings = json.load(open('settings.json', 'r'))


def make__Castle(window):
    red_team_bounds = boundsMechanics.Bounds((0,
                                              0,
                                              200,
                                              settings['window']['screen']['height'])
                                             )

    blue_team_bounds = boundsMechanics.Bounds((settings['window']['screen']['width'] - 200,
                                               0,
                                               settings['window']['screen']['width'],
                                               settings['window']['screen']['height'])
                                              )
    castles = {'red': castleClass.Castle(pygame.image.load('Images/castles/red_castle.png'),
                                         window,
                                         (
                                             10,
                                             (settings['window']['screen']['height']/2) - 75
                                         ),
                                         'red',
                                         red_team_bounds
                                         ),
               'blue': castleClass.Castle(pygame.image.load('Images/castles/blue_castle.png'),
                                          window,
                                          (
                                              settings['window']['screen']['width'] - 85,
                                              (settings['window']['screen']['height']/2) - 75
                                          ),
                                          'blue',
                                          blue_team_bounds
                                          )
               }
    del red_team_bounds, blue_team_bounds
    return castles['red'], castles['blue']


