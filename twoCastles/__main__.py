import pygame
# from classes import castleClass
from Mechanics import initializeTeams, miscMechanics
from Mechanics import proximityMechanics, scoreSystem
from Mechanics import castleMechanics
import json
settings = json.load(open('settings.json', 'r'))
pygame.init()
list_of_buys = {}


def initialize_window():
    window = pygame.display.set_mode(
        (settings['window']['screen']['width'],
         settings['window']['screen']['height'])
    )
    pygame.display.set_caption("twoCastles")  # Program Title
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
    castleMechanics.castle_moves(team_red, team_blue)
    castleMechanics.castle_moves(team_blue, team_red)


def re_draw_soldiers(team):
    for soldat in team.soldiers:
        soldat.window.blit(soldat.image, soldat.xy)
    return


def blit_renders(fonts):
    for font in fonts:
        fonts[font].window.blit(fonts[font].rendered, fonts[font].xy)


def draw_screen(window, team_red, team_blue, fonts_list):
    """
    This all renders the images to the screen, best to keep it all in one place so as to keep stutters to a minimum
    in case of increased logic loads.
    :param window:
    :param team_red:
    :param team_blue:
    :param fonts_list:
    :return:
    """
    window.fill((0, 0, 0))
    # window.blit(bg_image, (0, 0))  # this is a background doesn't fit currently so it is disabled
    window.blit(team_red.image, team_red.xy)
    window.blit(team_blue.image, team_blue.xy)
    re_draw_soldiers(team_blue)
    re_draw_soldiers(team_red)
    scoreSystem.blit_renders(fonts_list)
    pygame.display.update()


def make_text(team_red, team_blue):
    text = {}
    text = scoreSystem.make_font(
        text, settings['window']['screen']['font_type'], settings['window']['screen']['font_size'], team_red)
    text = scoreSystem.make_font(
        text, settings['window']['screen']['font_type'], settings['window']['screen']['font_size'], team_blue)
    return text


def updating_texts(text, team_red, team_blue):
    scoreSystem.update_text(team_red, text)
    scoreSystem.update_text(team_blue, text)


def cheat_mode(castle):
    for _ in range(25):
        castle.generate_new_soldier('archer')


def game_loop(window, bg_image):
    running = True
    team_red, team_blue = initializeTeams.make__Castle(window)  # using an import
    clock = pygame.time.Clock()
    fps = settings['window']['fps']
    event_timer = 0
    texts = make_text(team_red, team_blue)
    if settings['dev']['cheat']:
        cheat_mode(team_red)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.time.get_ticks()/1000 - event_timer >= 15:
            miscMechanics.collect_taxes(team_red)
            miscMechanics.collect_taxes(team_blue)
            event_timer = pygame.time.get_ticks()/1000
        updating_texts(texts, team_red, team_blue)
        scoreSystem.renderScore(texts)
        """ ▼ centralized function designed for judging whether able to attack"""
        sub_game_task(team_red, team_blue)
        """ ▼ does the drawing best, best to keep them together for immediate rendering"""
        draw_screen(window, team_red, team_blue, texts)
        clock.tick(fps)


if __name__ == '__main__':
    win, bg_image_main = initialize_window()
    game_loop(win, bg_image_main)
