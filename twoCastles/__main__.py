import pygame
# from classes import castleClass
from Mechanics import initializeTeams, miscMechanics
from Mechanics import proximityMechanics, Graphics_UI
from Mechanics import castleMechanics
import time
import json
settings = json.load(open('settings.json', 'r'))
pygame.init()
list_of_buys = {}


def initialize_window():
    window = pygame.display.set_mode(
        (
            settings['window']['screen']['width'],
            settings['window']['screen']['height']
        )
    )
    pygame.display.set_caption("twoCastles")  # Program Title
    pygame.display.set_icon(pygame.image.load('Images/icon/icon.png'))  # Top left Icon
    bg_image = pygame.image.load('Images/background/bg_scenery.gif')
    bg_image = pygame.transform.scale(
        bg_image,
        (
            settings['window']['screen']['width'],
            settings['window']['screen']['height']
        )
    )
    window.fill('#000000')
    return window, bg_image


def moves(team, enemy):
    for soldat in team.soldiers:
        if soldat.type == 'projectile' or soldat.can_move:
            soldat.movement()
        proximityMechanics.proximity_check(team, soldat, enemy)  # Using an import
    team.next_round_coins += 0.1


def sub_game_tasks(team_red, team_blue):
    moves(team_red, team_blue)
    moves(team_blue, team_red)
    castleMechanics.cash_flow(team_red)  # Using an import
    castleMechanics.cash_flow(team_blue)  # Using an import
    castleMechanics.castle_moves(team_red, team_blue)  # Using an import
    castleMechanics.castle_moves(team_blue, team_red)  # Using an import


def re_draw_soldiers(team):
    for soldat in team.soldiers:
        soldat.window.blit(soldat.image, soldat.xy)
    return


def blit_renders(fonts):
    for font in fonts:
        fonts[font].window.blit(fonts[font].rendered, fonts[font].xy)


def draw_screen(window, team_red, team_blue, fonts_list, bgImage, game_time):
    """
    This all renders the images to the screen, best to keep it all in one place so as to keep stutters to a minimum
    in case of increased logic loads.
    :param window:
    :param team_red:
    :param team_blue:
    :param fonts_list:
    :param bgImage:
    :param game_time:
    :return:
    """
    window.fill((0, 0, 0))
    # window.blit(bg_image, (0, 0))  # this is a background doesn't fit currently so it is disabled
    window.blit(team_red.image, team_red.xy)
    window.blit(team_blue.image, team_blue.xy)
    re_draw_soldiers(team_blue)
    re_draw_soldiers(team_red)
    Graphics_UI.blit_renders(fonts_list)  # Using an import
    Graphics_UI.timer_font(window, game_time)  # Using an import
    pygame.display.update()


def make_text(team_red, team_blue):
    text = {}
    text = Graphics_UI.make_font(  # Using an import
        text, settings['window']['screen']['font_type'], settings['window']['screen']['font_size'], team_red)
    text = Graphics_UI.make_font(  # Using an import
        text, settings['window']['screen']['font_type'], settings['window']['screen']['font_size'], team_blue)
    return text


def updating_texts(text, team_red, team_blue):
    Graphics_UI.update_text(team_red, text)  # Using an import
    Graphics_UI.update_text(team_blue, text)  # Using an import


def cheat_mode(castle):
    for _ in range(25):
        castle.generate_new_soldier('archer')


def dev_spawn(team_red, team_blue):
    # Team Red
    team_red.generate_new_soldier('cheetah')
    # Team Blue
    team_blue.generate_new_soldier('footman')


def game_loop(window, bg_image):
    running = True
    team_red, team_blue = initializeTeams.make__Castle(window)  # using an import
    if settings['dev']['no spawn']:
        dev_spawn(team_red, team_blue)
    clock = pygame.time.Clock()
    fps = settings['fps']
    event_timer = 0
    texts = make_text(team_red, team_blue)
    if settings['dev']['cheat']:
        cheat_mode(team_red)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.time.get_ticks()/1000 - event_timer >= settings['game']['reinforcements_delay']:
            castleMechanics.collect_taxes(team_red)  # Using an import
            castleMechanics.collect_taxes(team_blue)  # Using an import
            event_timer = pygame.time.get_ticks()/1000
        updating_texts(texts, team_red, team_blue)
        Graphics_UI.renderScore(texts)  # Using an import
        """ ▼ centralized function designed for AI judgement calls"""
        sub_game_tasks(team_red, team_blue)
        """ ▼ does the drawing, best to keep them together for linear rendering so no large breaks appear"""
        draw_screen(window, team_red, team_blue, texts, bg_image,
                    settings['game']['reinforcements_delay'] - (pygame.time.get_ticks() / 1000 - event_timer))
        clock.tick(fps)


if __name__ == '__main__':
    win, bg_image_main = initialize_window()
    game_loop(win, bg_image_main)
