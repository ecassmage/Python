from Mechanics import miscMechanics as mM
import math
import pygame
import random
import json
settings = json.load(open('settings.json', 'r'))


def castle_moves(castle, opponent):
    castle_can_attack(castle, opponent)
    healing_(castle)


def attack_castle(attacker, attacked):
    if mM.check_cooldown(attacker):
        damage_dealt = attacker.damage * (1 - attacked.armor/100)
        if damage_dealt < 1:
            damage_dealt = 1
        attacked.hp -= damage_dealt
        attacked.next_round_coins += 4
        attacked.score -= 0.5
        attacked.coins_pot -= 0.1
        if mM.check_if_dead(attacked):
            print(f"Team {attacked.team} has died so: ", end='')
            print("WINNER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if settings['dev']['dev_tools']:
                attacked.hp = 775
            else:
                exit()


def castle_can_attack(castle, opponent):
    enemies = opponent.soldiers
    for soldier in enemies:  # ▼ mM & pM are pulling from imports ▼
        if soldier.type != 'projectile':
            distance = math.sqrt((castle.spawn_coordinate[0] - soldier.x)**2 + (castle.spawn_coordinate[1] - soldier.y)**2)
            if distance <= castle.range:
                mM.ranged_generation(castle, castle, soldier)  # mM is pulling from imports
                return
    return


def healing_(castle):
    if castle.hp < 1000:
        castle.hp += castle.regeneration
        castle.next_round_coins -= castle.regeneration


def choose_list(team):
    list_of_buys = {}
    for buyable in settings['soldiers']:
        list_of_buys.update({buyable: settings['soldiers'][buyable]['cost']})
    while len(team.queue) < 5:
        team.queue.append(random.choice(list(list_of_buys)))


def cash_flow(team):
    if settings['dev']['no spawn'] is False:
        choose_list(team)
        if (pygame.time.get_ticks()/1000) - team.lay_over >= team.recruitment_delay and \
                team.total_soldiers < settings['window']['per_turn_soldiers'] * 3 and \
                team.per_time_soldiers > 0:
            if team.coins >= settings['soldiers'][team.queue[0]]['cost']:
                team.coins -= settings['soldiers'][team.queue[0]]['cost']
                team.generate_new_soldier(team.queue[0])
                team.queue.pop(0)
                team.lay_over = (pygame.time.get_ticks()/1000)
                team.total_soldiers += 1
                team.per_time_soldiers -= 1
    return


def reset_quota(castle):
    castle.per_time_soldiers = settings['window']['per_turn_soldiers']


def collect_taxes(castle):
    if castle.coins_pot < 0:
        castle.coins_pot = 0
    castle.coins += (castle.coins_pot + castle.next_round_coins)
    castle.coins_pot += (castle.next_round_coins/100)
    castle.next_round_coins = 0
    reset_quota(castle)

