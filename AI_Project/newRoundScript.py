"""
Developer: Evan Morrison
Program Name: AI_Project/newRoundScript
Version: 1.0.0
Date: 2021/01/27

This Script is meant to run the operations once a round is over and the fates of all the 'humans'
has been decided.
"""

import make_objects as mo
import json
import random
from copy import copy
settings = json.load(open('Settings'))


def clean_up(food_dict, humans_list, canvas, names):
    """
    Deals with the clean up after a round is over as a controller.
    This is also technically the main function of the script.
    """
    clean_up_food(food_dict)
    humans_list = fix_up_humans(humans_list)
    humans_list, names, canvas = initialize_new_humans(humans_list, names, canvas)
    food_dict = initialize_food({}, canvas)
    return food_dict, humans_list, names, canvas


def clean_up_food(food_dict):
    """Deletes all the food on the board"""
    for x in food_dict:
        for y in food_dict[x]:
            food_dict[x][y].clean_board()


def fix_up_humans(humans):
    """Resets certain attributes of the humans to set them back to a new season of survival"""
    for self in humans:
        self.back_at_base = False
        self.Target = None
        self.proximity = False
        self.direction = None
        self.eaten = False
        self.energy += settings['human']['energy']
        self.age += 1
    return humans


def initialize_food(food_storage, canvas_placed):
    """creates new food via the make_objects modulus"""
    food_storage = mo.create_food(food_storage, settings['starting']['food'], canvas_placed)
    return food_storage


def initialize_new_humans(humans_list, name, canvas):
    """Creates baby humans who will inherit and possible mutate better
    or worse skills for a trade off of more energy consumption"""
    humans_copy = copy(humans_list)
    for human_parent in humans_list:
        temp_empty = []
        if random.randrange(100) > 50:
            i, name = mo.create_human(temp_empty, 1, canvas, name)
            i = i[0]
            i.speed = human_parent.speed
            i.sense = human_parent.sense
            sense_rand = random.randrange(100)
            speed_rand = random.randrange(100)
            if sense_rand > 75:
                i.sense += 1
            elif sense_rand < 25:
                i.sense -= 1
            if speed_rand > 75:
                i.speed += 1
            elif speed_rand < 25:
                i.speed -= 1
            humans_copy.append(i)
    return humans_copy, name, canvas
