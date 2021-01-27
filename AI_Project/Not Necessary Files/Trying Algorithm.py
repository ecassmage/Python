import make_objects
from time import time
from tkinter import *
import math
import os
from contextlib import contextmanager
import random
import json
settings = json.load(open('../Settings'))
tk = Tk()
canvas = Canvas(tk)
times1 = []
times2 = []
processes = []
num_p = os.cpu_count()
temp_list = []


def sort_find2(x, coord_position):
    for checking_the_x in range(coord_position[0] - 10, coord_position[0] + 11):
        if checking_the_x in x:
            y_range = math.ceil(math.sqrt(10 ** 2 - (checking_the_x - coord_position[0]) ** 2))
            if y_range * 2 > len(x[checking_the_x]):
                for checking_the_y in x[checking_the_x]:
                    if (checking_the_y-500)**2 + (checking_the_x-500)**2 <= 10**2:
                        return tuple((checking_the_x, checking_the_y))
            else:
                for checking_the_y in range(coord_position[1] - y_range, coord_position[1] + y_range + 1):
                    if checking_the_y in x[checking_the_x]:
                        if (checking_the_y-500)**2 + (checking_the_x-500)**2 <= 10**2:
                            return tuple(x[checking_the_x][checking_the_y].xy)
    return None


def sort_find_pro(x, y, z):
    for x_columns in range(y - 10, y + 11):
        if x_columns in x:
            for y_rows in range(z - 10, z + 11):
                if y_rows in x[x_columns] and\
                        (x_columns - 500)**2 + (y_rows - 500)**2 <= 100:
                    # temp_list.append((x_columns, y_rows))
                    return tuple((x_columns, y_rows))
    return None


def main():

    return


def sort_list_dict(container, x, y):
    if x not in container:
        container.update({x: [y]})
    else:
        x_level = container[x]
        x_level.append(y)
    return container


def create_food(container_2, number):
    try:
        remove_w, remove_h = int(settings['window']['WIDTH'] / 5), int(settings['window']['HEIGHT'] / 5)
        if remove_w > 100:
            remove_w = 100
        if remove_h > 100:
            remove_h = 100
        for _ in range(number):
            x_food = random.randrange(remove_w, settings['window']['WIDTH'] - remove_w)
            y_food = random.randrange(remove_h, settings['window']['HEIGHT'] - remove_h)
            container_2 = sort_list_dict(container_2, x_food, y_food)
        if len(container_2) < number:
            container_2 = create_food(container_2, number - len(container_2))
    except RecursionError:
        return container_2
    return container_2


def sort_func(x, coord_position):
    for x_columns in range(coord_position[0], coord_position[0] + 11):
        if x_columns in x:
            for y_rows in range(coord_position[1] - 10, coord_position[1] + 11):
                if y_rows in x[x_columns] and\
                        (x_columns - 500)**2 + (y_rows - 500)**2 <= 100:
                    return tuple((x_columns, y_rows))
    return None


main()
