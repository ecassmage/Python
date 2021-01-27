"""
Developer: Evan Morrison
Program Name: AI_Project/AI Evolution
Version: 1.0.0
Date: 2021/01/27
"""
import human
import food
import newRoundScript
from tkinter import *
import json
import make_objects
import time
settings = json.load(open("Settings", 'r'))


def initial_setup():
    main_win = Tk()
    canvas = Canvas(main_win, width=settings['window']['WIDTH'], height=settings['window']['HEIGHT'], bg='black')
    canvas.pack()
    return main_win, canvas


def initialize_humans(human_storage, human_nums, canvas_placed, name_to_give):
    human_storage, name_to_give = make_objects.create_human(human_storage, human_nums, canvas_placed, name_to_give)
    return human_storage, name_to_give


def initialize_food(food_storage, food_nums, canvas_placed):
    food_storage = make_objects.create_food(food_storage, food_nums, canvas_placed)
    return food_storage


def main_loop(human_list, food_dict):
    got_to_end = []
    while len(human_list) > 0:
        start = time.time()
        for human_person in reversed(human_list):
            true_false = human.run_algorithm(human_person, food_dict, human_list)
            ''' ▲ Pulling from the human class in the classes folder ▲ '''
            if true_false and human_person in human_list and human_person.back_at_base:
                got_to_end.append(human_person)
                human_list.pop(human_list.index(human_person))
        end = time.time() - start
        if end < 1/settings['window']['fps']:
            time.sleep(1/settings['window']['fps'] - end)
    return got_to_end, food_dict


def __main__(canvas):
    name = 0
    humans, foods = [], {}
    humans, name = initialize_humans(humans, settings['starting']['humans'], canvas, name)
    foods = initialize_food(foods, settings['starting']['food'], canvas)
    while True:
        print(f"The amount of humans starting alive is: {len(humans)}", end=' ')
        humans, foods = main_loop(humans, foods)
        print(f"The size of the humans pool that survived is: {len(humans)}")
        foods, humans, name, canvas = newRoundScript.clean_up(foods, humans, canvas, name)
        canvas.update()


if __name__ == "__main__":
    game_win, game_canvas = initial_setup()
    __main__(game_canvas)
