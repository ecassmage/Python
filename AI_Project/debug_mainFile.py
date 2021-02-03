"""
Developer: Evan Morrison
Program Name: AI_Project/AI Evolution
Version: 1.0.0
Date: 2021/01/27
"""
from classes import human, food
import newRoundScript
from tkinter import *
import json
import make_objects
import time
settings = json.load(open("Settings", 'r'))


def debug_testing(dev_win, dev_canvas):
    print("This is for Debugging")
    food_dictionary_dev = {1234: {1234: food.Food(dev_canvas, 1234, 1234, 'Purple')}}
    food_dictionary_dev[1234][1234].delete(food_dictionary_dev)
    return


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
        if len(food_dict) == 0:
            for human_food_shortage in human_list:
                if human_food_shortage.eaten is False:
                    human_food_shortage.delete(human_list)
        end = time.time() - start
        if end < 1/settings['window']['fps']:
            time.sleep(1/settings['window']['fps'] - end)
    return got_to_end, food_dict


def __main__(dev_win, dev_canvas):
    name = 0
    humans, foods = [], {}
    humans, name = initialize_humans(humans, settings['starting']['humans'], dev_canvas, name)
    foods = initialize_food(foods, settings['starting']['food'], dev_canvas)
    while True:
        print(f"The Food this round starts at: {len(foods)}")
        print(f"The amount of humans starting alive is: {len(humans)}", end=' ')
        humans, foods = main_loop(humans, foods)
        print(f"The size of the humans pool that survived is: {len(humans)}")
        foods, humans, name, dev_canvas = newRoundScript.clean_up(foods, humans, dev_canvas, name)
        dev_canvas.update()
