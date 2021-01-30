import pygame
import json
settings = json.load(open('settings.json', 'r'))
# triangle = pygame.draw.polygon(window, (210, 180, 140), [[x, y], [x - 10, y - 10], [x + 10, y - 10]], 5)

# , (10, 10)


class Fonts:
    def __init__(self, window, font_type, size, coord):
        self.font_score = pygame.font.Font(font_type, size)
        self.font_coins = pygame.font.Font(font_type, size)
        self.font_health = pygame.font.Font(font_type, size)
        self.font_pot = pygame.font.Font(font_type, size)
        self.font = font_type
        self.size = size + 5
        self.window = window
        self.score = 0
        self.coins = 0
        self.hp = 0
        self.pot = 0
        self.x, self.y, self.xy = coord[0], coord[1], coord
        self.rendered_score = None
        self.rendered_coins = None
        self.rendered_health = None
        self.rendered_pot = None

    def resize_font(self):
        if settings['window']['screen']['width'] - self.x <= self.font_score.size('txt')[0]*10:
            self.x -= (self.font_score.size('txt')[0]*10 - (settings['window']['screen']['width'] - self.x))
            self.xy = (self.x, self.y)


def make_font(font, font_type, size, team):
    font.update({team.team: Fonts(team.window, font_type, size, (team.x, 25))})
    return font


def update_text(team, font):
    font[team.team].score = int(team.score)
    font[team.team].coins = int(team.coins)
    font[team.team].hp = int(team.hp)
    font[team.team].pot = int(team.coins_pot)


def renderScore(fonts):
    for font in fonts:
        fonts[font].rendered_score = fonts[font].font_score.render(
            f"Team {font} score is: {fonts[font].score}", True, font
        )
        fonts[font].rendered_coins = fonts[font].font_coins.render(
            f"Team Coins is: {fonts[font].coins}", True, font
        )
        fonts[font].rendered_health = fonts[font].font_health.render(
            f"Team Health is: {fonts[font].hp}", True, font
        )
        if settings['dev']['dev_tools']:
            fonts[font].rendered_pot = fonts[font].font_pot.render(
                f"Team Pot is: {fonts[font].pot}", True, font
            )
        fonts[font].resize_font()


def blit_renders(fonts):
    for font in fonts:
        fonts[font].window.blit(fonts[font].rendered_score, fonts[font].xy)
        fonts[font].window.blit(fonts[font].rendered_coins, (fonts[font].x, fonts[font].y + fonts[font].size))
        fonts[font].window.blit(fonts[font].rendered_health, (fonts[font].x, fonts[font].y + fonts[font].size * 2))
        if settings['dev']['dev_tools']:
            fonts[font].window.blit(fonts[font].rendered_pot, (fonts[font].x, fonts[font].y + fonts[font].size * 3))
