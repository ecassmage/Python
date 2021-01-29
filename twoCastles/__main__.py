import pygame
import castleClass
from Mechanics import initializeTeams, Idk__name__
import time
import json
settings = json.load(open('settings.json', 'r'))
pygame.init()
list_of_buys = {}


def initialize_window():
    window = pygame.display.set_mode(
        (settings['window']['screen']['width'],
         settings['window']['screen']['height'])
    )
    pygame.display.set_caption("twoCastles.Error//Pleasequitandstartgameagain,anERRORhasoccurred")  # Program Title
    pygame.display.set_icon(pygame.image.load('Images/icon/icon.png'))  # Top left Icon
    bg_image = pygame.image.load('Images/background/bg_scenery.gif')
    bg_image = pygame.transform.scale(bg_image, (
        settings['window']['screen']['width'],
        settings['window']['screen']['height']
    )
                                      )
    window.fill('#000000')
    return window, bg_image


def moves(team, enemy):
    for soldat in team.soldiers:
        if soldat.type == 'projectile' or soldat.hold is False:
            soldat.movement()
        soldat.window.blit(soldat.image, soldat.xy)
        Idk__name__.proximity_check(team, soldat, enemy.soldiers)
    team.coins += 0.1


def sub_game_task(team_red, team_blue):
    moves(team_red, team_blue)
    moves(team_blue, team_red)
    Idk__name__.cash_flow(team_red)
    Idk__name__.cash_flow(team_blue)


def game_loop(window, bg_image):
    running = True
    team_red, team_blue = initializeTeams.make__Castle(window)  # using an import
    clock = pygame.time.Clock()
    event_timer = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill((0, 0, 0))
        window.blit(team_red.image, team_red.xy)
        window.blit(team_blue.image, team_blue.xy)
        sub_game_task(team_red, team_blue)
        pygame.display.update()
        clock.tick(settings['window']['fps'])
        if pygame.time.get_ticks()/1000 - event_timer >= 15:
            team_blue.coins += 250
            team_red.coins += 250
            event_timer = pygame.time.get_ticks()/1000



if __name__ == '__main__':
    win, bg_image_main = initialize_window()
    game_loop(win, bg_image_main)
