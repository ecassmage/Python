import math
from Mechanics import miscMechanics
from classes import unitsClass
import pygame
import json
settings = json.load(open('settings.json', 'r'))


def proximity_check(team, sprite, enemy_castle):
    opponents = enemy_castle.soldiers
    if sprite.type != 'projectile':
        for so in opponents:  # 'so' stands for sprite opponent
            if so.type != 'projectile':
                if proximity(sprite, so):
                    sprite.hold = True
                    if sprite.ranged is False:
                        miscMechanics.release_attack(sprite, so, opponents, team)
                    elif miscMechanics.check_cooldown(sprite):
                        miscMechanics.ranged_generation(sprite, team)
                    return
        else:
            if proximity(sprite, enemy_castle):
                sprite.hold = True
                if sprite.ranged:
                    miscMechanics.ranged_generation(sprite, team)
                else:
                    miscMechanics.attack_castle(sprite, enemy_castle)
                return
            else:
                sprite.hold = False
            return
    else:
        projectile_proximity(team, sprite, opponents, enemy_castle)


def projectile_proximity(team, sprite, opponents, enemy_castle):
    for so in opponents:  # so stands for sprite opponent
        if so.type != 'projectile':
            if proximity(sprite, so):
                miscMechanics.release_attack(sprite, so, opponents, team)
                team.soldiers.pop(team.soldiers.index(sprite))
                return
    else:
        if proximity(sprite, enemy_castle):
            miscMechanics.attack_castle(sprite, enemy_castle)
            team.soldiers.pop(team.soldiers.index(sprite))
            return
        if sprite.distance_traveled > sprite.max_range:
            team.soldiers.pop(team.soldiers.index(sprite))
            return


def castle_can_attack(castle, opponent):
    enemies = opponent.soldiers
    for soldier in enemies:
        if distance(castle, soldier) <= castle.range and miscMechanics.check_cooldown(castle):
            miscMechanics.ranged_generation(castle, castle)
    return


def proximity(sprite, target):
    if sprite.rect_position().colliderect(target.rect_position()) or distance(sprite, target) <= sprite.range:
        return True
    else:
        return False


def distance(sprite, target):
    return math.sqrt((target.x - sprite.x) ** 2 + (target.y - sprite.y) ** 2)
