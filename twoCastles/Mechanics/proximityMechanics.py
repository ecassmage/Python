import math
from Mechanics import miscMechanics, castleMechanics
import json
settings = json.load(open('settings.json', 'r'))


def proximity_check(team, sprite, enemy_castle):
    if sprite.type != 'projectile':
        for so in enemy_castle.soldiers:  # 'so' stands for sprite opponent
            if so.type != 'projectile':
                if proximity(sprite, so):
                    sprite.can_move = False
                    if sprite.ranged is False:
                        miscMechanics.release_attack(sprite, so, enemy_castle, team)
                    else:
                        miscMechanics.ranged_generation(sprite, team, so, dst=distance(sprite, so))
                    return
        else:
            if proximity(sprite, enemy_castle):
                sprite.can_move = False
                if sprite.ranged:
                    miscMechanics.ranged_generation(sprite, team, enemy_castle, dst=distance(sprite, enemy_castle))
                else:
                    castleMechanics.attack_castle(sprite, enemy_castle)
                return
            else:
                sprite.can_move = True
            return
    else:
        projectile_proximity(team, sprite, enemy_castle)


def projectile_proximity(team, sprite, enemy_castle):
    if sprite.fire_type == 'line':
        for so in enemy_castle.soldiers:  # so stands for sprite opponent
            if so.type != 'projectile':
                if proximity(sprite, so):
                    miscMechanics.release_attack(sprite, so, enemy_castle, team)
                    team.soldiers.pop(team.soldiers.index(sprite))
                    return
        else:
            if proximity(sprite, enemy_castle):
                castleMechanics.attack_castle(sprite, enemy_castle)
                team.soldiers.pop(team.soldiers.index(sprite))
                return
            if sprite.distance_traveled > sprite.max_range:
                team.soldiers.pop(team.soldiers.index(sprite))
                return
    elif sprite.fire_type == 'arc':
        for so in enemy_castle.soldiers:  # so stands for sprite opponent
            if so.type != 'projectile' and proximity(sprite, so):
                miscMechanics.release_attack(sprite, so, enemy_castle, team)
                sprite.primed = True
        if proximity(sprite, enemy_castle):
            castleMechanics.attack_castle(sprite, enemy_castle)
            sprite.primed = True
        if sprite.primed:
            team.soldiers.pop(team.soldiers.index(sprite))


def proximity(sprite, target):
    if sprite.rect_position().colliderect(target.rect_position()) or distance(sprite, target) <= sprite.range:
        return True
    else:
        return False


def distance(sprite, target):
    return math.sqrt((target.x - sprite.x) ** 2 + (target.y - sprite.y) ** 2)
