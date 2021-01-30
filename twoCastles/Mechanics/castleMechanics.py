from Mechanics import proximityMechanics as pM
from Mechanics import miscMechanics as mM
import math
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
        attacked.coins += 4
        attacked.score -= 0.5
        attacked.coins_pot -= 0.1
        if mM.check_if_dead(attacked):
            print(f"Team {attacked.team} has died so: ", end='')
            print("WINNER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if settings['dec']['dev_tools']:
                attacked.hp = 775
            else:
                exit()


def castle_can_attack(castle, opponent):
    enemies = opponent.soldiers
    for soldier in enemies:  # ▼ mM & pM are pulling from imports ▼
        distance = math.sqrt((castle.spawn_coordinate[0] - soldier.x)**2 + (castle.spawn_coordinate[1] - soldier.y)**2)
        if distance <= castle.range:
            mM.ranged_generation(castle, castle)  # mM is pulling from imports
            return
    return


def healing_(castle):
    if castle.hp < 1000:
        castle.hp += castle.regeneration
        castle.coins -= castle.regeneration



