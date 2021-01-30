import pygame
import random
import unitsClass
import json
settings = json.load(open('settings.json', 'r'))


def collect_taxes(castle):
    castle.coins += castle.coins_pot
    castle.coins_pot += 15


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


def attack_castle(attacker, attacked):
    if check_cooldown(attacker):
        damage_dealt = attacker.damage * (1 - attacked.armor/100)
        if damage_dealt < 1:
            damage_dealt = 1
        attacked.hp -= damage_dealt
        if check_if_dead(attacked):
            print("WINNER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            exit()


def release_attack(attacker, attacked, enemy_soldiers, team):
    if check_cooldown(attacker):
        damage_dealt = (attacker.damage * (1 - attacked.armor/100)) + attacker.armor_pierce
        if damage_dealt < 1:
            damage_dealt = 1
        attacked.hp -= damage_dealt
        check_health(attacked, enemy_soldiers, team)


def projectile_attack(attacker, attacked, enemy_soldiers, team):
    damage_dealt = (attacker.damage * (1 - attacked.armor/100)) + attacker.armor_pierce
    if damage_dealt < 1:
        damage_dealt = 1
    attacked.hp -= damage_dealt
    team.soldiers.pop(team.soldiers.index(attacker))
    check_health(attacked, enemy_soldiers, team)


def check_health(attacked, enemy_soldiers, team):
    if check_if_dead(attacked):
        more_money(team, attacked)
        enemy_soldiers.pop(enemy_soldiers.index(attacked))


def ranged_generation(sprite, team):
    if sprite.type == 'archer':
        team.soldiers.append(unitsClass.Arrow(sprite.window, sprite.xy, sprite.team))
    elif sprite.type == 'castle':
        team.soldiers.append(unitsClass.CastleMissile(sprite.window, sprite.spawn_coordinate, sprite.team))
    return
