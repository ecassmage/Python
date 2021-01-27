from multiprocessing import Pool
from time import time
import make_objects
import json
from tkinter import *
from human import run_algorithm
main_win = Tk()
settings = json.load(open('../Settings'))


def initialize_humans(human_storage, human_nums, canvas_placed, name_to_give):
    human_storage, name_to_give = make_objects.create_human(human_storage, human_nums, canvas_placed, name_to_give)
    return human_storage, name_to_give


def initialize_food(food_storage, food_nums, canvas_placed):
    food_storage = make_objects.create_food(food_storage, food_nums, canvas_placed)
    return food_storage


def make_hums():
    canvas = Canvas(main_win, width=settings['window']['WIDTH'], height=settings['window']['HEIGHT'], bg='black')
    canvas.pack()
    humans, foods = [], {}
    name = 0
    humans, name = initialize_humans(humans, settings['starting']['humans'], canvas, name)
    foods = initialize_food(foods, settings['starting']['food'], canvas)
    # print(humans)
    return humans, foods


def fetch_info_pre_process(human_individual):
    # humans = values.human
    # foods = values.food
    human.run_algorithm(human_individual)
    # print(foods, humans[human_individual])
    return 1


def values(humans, foods):
    values.food = foods
    setattr(values, 'human', humans)
    # setattr(values, 'food', foods)


def multiprocess_allocation(humans, foods):
    # print("Hello")
    for hum in humans:
        hum.foods_dict = foods
    # print()
    if __name__ == "__main__":
        iterations = [i for i in range(len(humans))]
        with Pool(processes=7) as current:
            print(current.map(run_algorithm, humans))
        # current.join()
    """This Is Done"""
    print("Hello World")
    pass


human, food = make_hums()
multiprocess_allocation(human, food)
