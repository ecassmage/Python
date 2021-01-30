import pygame
# from classes import castleClass
from Mechanics import initializeTeams, miscMechanics, proximityMechanics
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
        proximityMechanics.proximity_check(team, soldat, enemy)
    team.coins += 0.1


def sub_game_task(team_red, team_blue):
    moves(team_red, team_blue)
    moves(team_blue, team_red)
    miscMechanics.cash_flow(team_red)
    miscMechanics.cash_flow(team_blue)
    proximityMechanics.castle_can_attack(team_red, team_blue)
    proximityMechanics.castle_can_attack(team_blue, team_red)


def re_draw_soldiers(team):
    for soldat in team.soldiers:
        soldat.window.blit(soldat.image, soldat.xy)
    return


def draw_screen(window, team_red, team_blue):
    window.fill((0, 0, 0))
    # window.blit(bg_image, (0, 0))  # this is a background doesn't fit currently so it is disabled
    window.blit(team_red.image, team_red.xy)
    window.blit(team_blue.image, team_blue.xy)
    re_draw_soldiers(team_blue)
    re_draw_soldiers(team_red)
    pygame.display.update()


def cheat_mode(castle):
    for _ in range(50):
        castle.generate_new_soldier('archer')


def game_loop(window, bg_image):
    running = True
    team_red, team_blue = initializeTeams.make__Castle(window)  # using an import
    clock = pygame.time.Clock()
    fps = settings['window']['fps']
    event_timer = 0
    if settings['dev']['cheat']:
        cheat_mode(team_red)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        """ ▼ centralized function designed for judging whether able to attack"""
        sub_game_task(team_red, team_blue)
        """ ▼ does the drawing best, best to keep them together for immediate rendering"""
        draw_screen(window, team_red, team_blue)
        clock.tick(fps)
        if pygame.time.get_ticks()/1000 - event_timer >= 15:
            miscMechanics.collect_taxes(team_red)
            miscMechanics.collect_taxes(team_blue)
            event_timer = pygame.time.get_ticks()/1000


if __name__ == '__main__':
    win, bg_image_main = initialize_window()
    game_loop(win, bg_image_main)
