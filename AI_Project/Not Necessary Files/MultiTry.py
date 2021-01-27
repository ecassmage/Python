from multiprocessing import Process
import os
from time import time
import random
import json
settings = json.load(open('../Settings'))


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


if __name__ == '__main__':
    num_cpu = os.cpu_count()
    dict_made = create_food({}, 1000)
    print(dict_made)
    process = []
    for i in range(50):
        p = Process(target=sort_func, args=(dict_made, (500, 500)))
        process.append(p)
    for i in process:
        i.start()
    for i in process:
        i.join()
    print(process)