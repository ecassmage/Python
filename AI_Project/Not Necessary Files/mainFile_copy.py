from human_fork import run_algorithm
from multiprocessing import Pool
from tkinter import *
import json
import make_objects

settings = json.load(open("../Settings"))


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


def foods_hold_dict():
    pass


def multiprocess_allocation(humans, foods, window):
    # print("Hello")
    for hum in humans:
        hum.foods_dict = foods
    # print()
    for humankind in humans:
        humankind.re_draw_position(window)
    if __name__ == "__main__":
        with Pool(processes=4) as current:
            humans = current.map(run_algorithm, humans)
        window.update()
        current.join()
    # """This Is Done"""
    # print("Hello World")

    return humans


def main_loop(human_list, food_dict, window):
    c = 0
    while True:
        human_list = multiprocess_allocation(human_list, food_dict, window)
        # c += 1
        # # start = time.time()
        # for human_person in reversed(human_list):
        #     human.run_algorithm(human_person, food_dict, window)  # Pulling from the human class in the classes folder
        # window.update()
        # # print(f"Logic Time: {time.time() - start}")
        # # start = time.time()
        #
        # # print(f"Rendering Time: {time.time() - start}")
        # # time.sleep(1/60)
        # # break
        # if c > 150:
        #     pass
        # for humans in human_list:
        #     humans.re_draw_position(window)
        # window.update()
    return


def __main__(main_win, canvas):
    name = 0
    humans, foods = [], {}
    humans, name = initialize_humans(humans, settings['starting']['humans'], canvas, name)
    foods = initialize_food(foods, settings['starting']['food'], canvas)
    main_loop(humans, foods, canvas)
    main_win.mainloop()


if __name__ == "__main__":
    game_win, game_canvas = initial_setup()
    __main__(game_win, game_canvas)
