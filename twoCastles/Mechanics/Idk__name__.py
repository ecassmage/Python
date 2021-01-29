import math
import pygame
import random
import unitsClass
import castleClass
import json
settings = json.load(open('settings.json', 'r'))


def end_of_round():
    pass


def proximity_check(team, sprite, opponents):
    if sprite.type != 'projectile':
        for so in opponents:  # so stands for sprite opponent
            if so.type != 'projectile':
                distance = math.sqrt((sprite.x - so.x)**2 + (sprite.y - so.y)**2)
                if distance <= sprite.range:
                    sprite.hold = True
                    if sprite.ranged is False:
                        if check_cooldown(sprite):
                            damage_dealt = sprite.damage - (sprite.damage * (so.armor/10)**2)
                            sprite.attacked_last = pygame.time.get_ticks() / 1000
                            if damage_dealt < 1:
                                damage_dealt = 1
                            so.hp -= damage_dealt
                            if check_if_dead(so):
                                opponents.pop(opponents.index(so))
                        return
                    else:
                        if check_cooldown(sprite):
                            team.soldiers.append(unitsClass.Arrow(sprite.window, sprite.team, sprite.xy))
                            sprite.attacked_last = pygame.time.get_ticks()/1000
                        return
        else:
            sprite.hold = False
            return
    else:
        projectile_proximity(team, sprite, opponents)


def projectile_proximity(team, sprite, opponents):
    for so in opponents:  # so stands for sprite opponent
        if so.type != 'projectile':
            distance = math.sqrt((sprite.x - so.x)**2 + (sprite.y - so.y)**2)
            if distance <= sprite.range:
                damage_dealt = sprite.damage - (sprite.damage * (so.armor / 10) ** 2)
                if damage_dealt < 1:
                    damage_dealt = 1
                so.hp -= damage_dealt
                try:
                    team.soldiers.pop(team.soldiers.index(sprite))
                    if check_if_dead(so):
                        team.coins += int(so.cost / 50)
                        team.score += int(so.cost / 10)
                        opponents.pop(opponents.index(so))

                        return
                    else:
                        return
                except ValueError:
                    print("ValueError: Reported")
    else:
        if sprite.distance_traveled >= settings['soldiers']['archer']['range']:
            team.soldiers.pop(team.soldiers.index(sprite))
            return


def check_cooldown(sprite):
    if (pygame.time.get_ticks()/1000) - sprite.attacked_last >= sprite.cooldown:
        return True
    else:
        return False


def choose_list(team):
    list_of_buys = {}
    for buyable in settings['soldiers']:
        list_of_buys.update({buyable: settings['soldiers'][buyable]['cost']})
    while len(team.queue) < 5:
        team.queue.append(random.choice(list(list_of_buys)))


def cash_flow(team):
    choose_list(team)
    if (pygame.time.get_ticks()/1000) - team.lay_over >= team.recruitment_delay:
        if team.coins >= settings['soldiers'][team.queue[0]]['cost']:
            team.coins -= settings['soldiers'][team.queue[0]]['cost']
            team.generate_new_soldier(team.queue[0])
            team.queue.pop(0)
            team.lay_over = (pygame.time.get_ticks()/1000)
    return


def check_if_dead(health):
    if health.hp <= 0:
        return True
    else:
        return False
