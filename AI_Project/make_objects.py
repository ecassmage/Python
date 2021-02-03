"""
Developer: Evan Morrison
Program Name: AI_Project/make_objects
Version: 1.0.0
Date: 2021/01/27
"""
import json
import random

from classes import human, food

settings = json.load(open('Settings'))


def create_human(container, number, canvas, name):
    """
        A function to create new human objects.
        This function will choose a random wall to apply a x or y coordinate to then choose a
        random corresponding coordinate to finish the ensemble. will make a group at a time to keep
        code more centralized to its task function.

    :param container:
    :param number:
    :param canvas:
    :param name:
    :return:
    """
    walls = {0: settings['human']['size'],
             1: settings['human']['size'],
             2: settings['window']['WIDTH'] - settings['human']['size'],
             3: settings['window']['HEIGHT'] - settings['human']['size']}
    for _ in range(number):
        random_wall = random.randrange(4)
        if random_wall == 0 or random_wall == 2:
            y_human = random.randrange(settings['human']['size'],
                                       settings['window']['HEIGHT'] - settings['human']['size'])
            obj_human = human.Human(canvas, walls[random_wall], y_human, name)
        else:
            x_human = random.randrange(settings['human']['size'],
                                       settings['window']['WIDTH'] - settings['human']['size'])
            obj_human = human.Human(canvas, x_human, walls[random_wall], name)
        container.append(obj_human)
        name += 1
    return container, name


def generate_random_nums_food(remove_width, remove_height, creation_call=0):
    """
        This function doubles as both the coordinate generation function for new foods as well as
        a generator for humans when choosing a point on the board to go to if nothing is within
        range to see.

    :param remove_width:
    :param remove_height:
    :param creation_call:
    :return:
    """
    max_dif = 50
    if creation_call == 1:
        max_dif = 100
    if remove_width > max_dif:
        remove_width = max_dif
    if remove_height > max_dif:
        remove_height = max_dif
    x_coord = random.randrange(remove_width, settings['window']['WIDTH'] - remove_width)
    y_coord = random.randrange(remove_height, settings['window']['HEIGHT'] - remove_height)
    return x_coord, y_coord


def create_food(container, number, canvas):
    """
        This function creates food for the board and will call both the
        generate_random_nums_food function and sort_food function.

    :param container:
    :param number:
    :param canvas:
    :return:
    """
    try:
        remove_w, remove_h = int(settings['window']['WIDTH'] / 5), int(settings['window']['HEIGHT'] / 5)
        for _ in range(number):
            x_food, y_food = generate_random_nums_food(remove_w, remove_h, 1)
            color_food = random.choice(list(settings['food']['food_color']))
            obj_food = food.Food(canvas, x_food, y_food, color_food)
            container = sort_food(container, obj_food)
        if len(container) < number:
            container = create_food(container, number - len(container), canvas)
    except RecursionError:
        return container
    return container


def sort_food(food_dict, new_food):
    """
        Organizes food based on their x_axis coordinate.
        NOTE: This is mostly useless at this point since a new algorithm
         is now in use to find objects within visible range which doesn't
         need the objects to be sorted for efficiency.

    :param food_dict:
    :param new_food:
    :return:
    """
    if new_food.x not in food_dict:
        food_dict.update({new_food.x: {new_food.y: new_food}})
    else:
        x_level = food_dict[new_food.x]
        if new_food.y not in food_dict[new_food.x]:
            x_level.update({new_food.y: new_food})
    return food_dict
