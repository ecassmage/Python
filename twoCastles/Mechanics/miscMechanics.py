import pygame
from classes import unitsClass, projectiles
from Mechanics import TrajectoryScript
import json
settings = json.load(open('settings.json', 'r'))


def more_money(team, opponent):
    team.coins_pot += int(opponent.cost / 50)
    team.score += int(opponent.cost / 10)


def check_cooldown(sprite):
    if hasattr(sprite, 'attacked_last') and hasattr(sprite, 'cooldown'):
        if (pygame.time.get_ticks()/1000) - sprite.attacked_last >= sprite.cooldown:
            sprite.attacked_last = pygame.time.get_ticks() / 1000
            return True
        else:
            return False
    else:
        return True


def check_if_dead(health):
    if health.hp <= 0:
        return True
    else:
        return False


def release_attack(attacker, attacked, enemy, team):
    if check_cooldown(attacker):
        damage_dealt = (attacker.damage * (1 - attacked.armor/100)) + attacker.armor_pierce
        if damage_dealt < 1:
            damage_dealt = 1
        attacked.hp -= damage_dealt
        check_health(attacked, enemy, team)


def projectile_attack(attacker, attacked, enemy_soldiers, team):
    damage_dealt = (attacker.damage * (1 - attacked.armor/100)) + attacker.armor_pierce
    if damage_dealt < 1:
        damage_dealt = 1
    attacked.hp -= damage_dealt
    team.soldiers.pop(team.soldiers.index(attacker))
    check_health(attacked, enemy_soldiers, team)


def check_health(attacked, enemy, team):
    if check_if_dead(attacked):
        more_money(team, attacked)
        enemy.soldiers.pop(enemy.soldiers.index(attacked))
        enemy.total_soldiers -= 1


def ranged_generation(sprite, team, target, dst=0):
    if check_cooldown(sprite):
        if sprite.type == 'archer':
            team.soldiers.append(projectiles.Arrow(sprite.window, sprite.xy, sprite.team))
        elif sprite.type == 'castle':
            team.soldiers.append(projectiles.CastleMissile(sprite.window, sprite.spawn_coordinate, sprite.team))
        elif sprite.type == 'catapult':
            team.soldiers.append(TrajectoryScript.make_new_rock(sprite, dst, target))
    return
