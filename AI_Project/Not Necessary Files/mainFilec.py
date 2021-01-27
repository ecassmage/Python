import human
import food
from tkinter import *
from multiprocessing import Process
import json
import make_objects
import time
import copy
settings = json.load(open("../Settings"))


class Board:

    board = 0

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=settings['window']['WIDTH'],
                             height=settings['window']['HEIGHT'], bg='black')
        self.board = self

    @staticmethod
    def return_board():
        return board


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


def refresh():
    canvas = Board.return_board()
    print(canvas)
    exit()
    canvas.update()


def main_loop(human_list, food_dict, window):
    c = 0
    while True:
        c += 1
        # start = time.time()
        Process(target=refresh).start()
        exit()
        for human_person in reversed(human_list):
            human.run_algorithm(human_person, food_dict, window)  # Pulling from the human class in the classes folder
        # window.update()
        # p.join()
        # print(f"Logic Time: {time.time() - start}")
        # start = time.time()
        # print(f"Rendering Time: {time.time() - start}")
        # time.sleep(1/60)
        # break
        if c > 50:
            pass
    return


def __main__(main_win, canvas):
    name = 0
    humans, foods = [], {}
    humans, name = initialize_humans(humans, settings['starting']['humans'], canvas, name)
    foods = initialize_food(foods, settings['starting']['food'], canvas)
    main_loop(humans, foods, canvas)
    main_win.mainloop()


if __name__ == "__main__":
    board = Board()
    board.canvas.pack()
    # print("this", Board.return_board())
    # game_win, game_canvas = initial_setup()
    __main__(board.window, board.canvas)
    # print(board.board)
    # print(Board.board)
    # print(Board.return_board())
    mainloop()
