from tkinter import *
from copy import copy
import random
import time
import Evol_Module
# import tensorflow as tf
Hello = 100


'''___________________________________ Initial Variable Initialization Here _________________________________________'''
WIDTH, HEIGHT = 1000, 1000
Humans, Foods, Foods_sorted, New_Humans, historical = [], [], {}, [], {}
evolution_scoreboard = {'sense': {}, 'speed': {}}
color_energy = {'Red': 40, 'Blue': 50, 'Green': 75, 'Purple': 90}
initial_game_settings = {'humans': 50, 'foods': 750, 'energy': 250, 'max_energy': 400, 'speed': 10, 'sense': 10,
                         'fps': 0, 'size_human': 4}
global year, mass_extinction, oldest_human, name_of_human, history_humans, history_food, largest_children_count
global name_of_oldest, deaths
'''___________________________________ Initial Variable Initialization Here _________________________________________'''


'''___________________________________________________ Windows _____________________________________________________'''
main_tk, info_tk = Tk(), Tk()
main_win = Canvas(main_tk, width=WIDTH, height=HEIGHT, bg='black')
main_win.pack()
info_win = Canvas(info_tk, width=750, height=750, bg='orange')
info_win.pack()
'''___________________________________________________ Windows _____________________________________________________'''


"""
class Human is the amalgamation of all the inner workings of the Square AI bots and what they do.
The class only covers things that are involved with the the choices the AI needs to make in its day to day life.
"""


class Human:
    def __init__(self, window, x, y, name):
        self.name = f'Human {name}'
        self.win = window
        self.x, self.y, self.xy = x, y, (x, y)
        self.speed = initial_game_settings['speed']
        self.sense = initial_game_settings['sense']
        self.energy = initial_game_settings['energy']
        self.corners = [
            self.x-initial_game_settings['size_human'],
            self.y-initial_game_settings['size_human'],
            self.x+initial_game_settings['size_human'],
            self.y+initial_game_settings['size_human']]
        self.color = (0, 255, 0)
        self.color_hex = '#%02x%02x%02x' % self.color
        self.sprite = self.win.create_rectangle(
            self.x-initial_game_settings['size_human'],
            self.y-initial_game_settings['size_human'],
            self.x+initial_game_settings['size_human'],
            self.y+initial_game_settings['size_human'],
            fill='black', outline=self.color_hex, width=3)
        self.moves_remaining = self.speed
        self.survive_the_round = None
        self.survive_to_next_round = False
        self.food_in_range = None
        self.chosen_coordinate = None
        self.has_food = False
        self.age, self.kids = 0, 0

    def draw(self):
        if self.survive_to_next_round:
            return
        if self.energy <= 0:
            self.kill_human()
            return
        """This is to check if the human is against the wall after eating its fill"""
        if self.has_food:
            if self.x <= initial_game_settings['size_human'] or \
                    self.y <= initial_game_settings['size_human'] or \
                    self.x >= WIDTH - initial_game_settings['size_human'] or \
                    self.y >= HEIGHT - initial_game_settings['size_human']:
                self.survive_to_next_round = True
                return
            elif self.survive_the_round is None:
                self.survival()
        """This is to check if the human is against the wall after eating its fill"""
        """This for loop decides what move will be made whether to go for food, to search for food or to go home"""
        for i in range((self.moves_remaining + 1)):
            self.coordinate_control()  # Go to the coordinate_control method, just for organizational purposes
        self.win.update()
        """This for loop decides what move will be made whether to go for food, to search for food or to go home"""
        """Check how much energy will be taken after each move"""
        self.energy -= 5 + (self.speed/10) ** 2 + (self.sense / 10)
        """Check how much energy will be taken after each move"""
        return

    def coordinate_control(self):
        self.decision_coordinate()
        self.move_pixel()
        if self.food_in_range is not None:
            if self.corners[0] <= self.food_in_range.xy[0] <= self.corners[2] and \
                    self.corners[1] <= self.food_in_range.xy[1] <= self.corners[3]:
                self.eat_food()
        elif self.chosen_coordinate == (self.x, self.y):
            self.pick_coordinate()
        # self.re_draw_position()

    def decision_coordinate(self):
        if self.survive_the_round is None:
            if self.food_in_range is None:
                self.in_range()
            if self.food_in_range is None and self.chosen_coordinate is None:
                self.pick_coordinate()

    def kill_human(self):
        global deaths
        deaths += 1
        self.win.delete(self.sprite)
        Humans.pop(Humans.index(self))
        self.win.update()
        return

    def survival(self):
        if WIDTH - self.x < self.x:
            best_x = WIDTH - initial_game_settings['size_human']
            dif_x = WIDTH - self.x
        else:
            best_x = initial_game_settings['size_human']
            dif_x = self.x
        if HEIGHT - self.y < self.y:
            best_y = HEIGHT - initial_game_settings['size_human']
            dif_y = HEIGHT - self.y
        else:
            best_y = initial_game_settings['size_human']
            dif_y = self.y
        if dif_x <= dif_y:
            self.survive_the_round = (best_x, self.y)
        else:
            self.survive_the_round = (self.x, best_y)
        return

    def in_range(self):
        if self.moves_remaining > 0:
            for x in range(self.x - self.sense, self.x + self.sense + 1):
                if x in Foods_sorted:
                    list_of_food_in_x = Foods_sorted[x]
                else:
                    continue
                for food_in_range in list_of_food_in_x:
                    if (food_in_range.x - self.x)**2 + (food_in_range.y - self.y)**2 <= self.sense**2:
                        self.food_in_range = food_in_range
                        return
        return

    def pick_coordinate(self):
        rand_coordinate = (random.randrange(6, WIDTH-5), random.randrange(6, HEIGHT-5))
        self.chosen_coordinate = rand_coordinate
        # print(self.chosen_coordinate)

    def move_pixel(self):
        while True:
            if self.survive_the_round is not None:
                move_x, move_y = self.survive_the_round[0], self.survive_the_round[1]
                break
            elif self.food_in_range is None:
                move_x, move_y = self.chosen_coordinate[0], self.chosen_coordinate[1]
                break
            else:
                if self.food_in_range in Foods:
                    move_x, move_y = self.food_in_range.xy[0], self.food_in_range.xy[1]
                    break
                else:
                    self.food_in_range = None
                    self.decision_coordinate()

        move_x, move_y = move_x - self.x, move_y - self.y
        if abs(move_x) >= abs(move_y):
            movement = 'x_axis'
        else:
            movement = 'y_axis'
        if movement == 'x_axis':
            if move_x > 0:
                self.x += 1
                self.win.move(self.sprite, 1, 0)
            else:
                self.x -= 1
                self.win.move(self.sprite, -1, 0)
        else:
            if move_y > 0:
                self.y += 1
                self.win.move(self.sprite, 0, 1)
            else:
                self.y -= 1
                self.win.move(self.sprite, 0, -1)
        self.xy = (self.x, self.y)

    def re_draw_position(self):
        self.win.delete(self.sprite)
        self.corners = [self.x - 4, self.y - 4, self.x + 4, self.y + 4]
        self.sprite = self.win.create_rectangle(self.x - 4, self.y - 4, self.x + 4, self.y + 4,
                                                fill='black', outline=self.color_hex, width=3)
        # self.win.update()
        if initial_game_settings['fps'] == 0:
            time.sleep(0)
        else:
            time.sleep(1/initial_game_settings['fps'])

    def eat_food(self):
        self.energy += self.food_in_range.energy
        if self.energy > initial_game_settings['max_energy']:
            self.energy = initial_game_settings['max_energy']
        self.food_in_range.win.delete(self.food_in_range.sprite)
        if self.food_in_range in Foods:
            Foods.pop(Foods.index(self.food_in_range))
        if self.food_in_range in Foods_sorted[self.food_in_range.xy[0]]:
            foods_sorted_temp = Foods_sorted[self.food_in_range.xy[0]]
            foods_sorted_temp.pop(foods_sorted_temp.index(self.food_in_range))
        self.has_food = True
        self.food_in_range = None

    def recreate_self(self):
        # self.x, self.y = self.x, self.y
        self.xy = (self.x, self.y)
        self.survive_the_round = None
        self.survive_to_next_round = False
        self.food_in_range = None
        self.chosen_coordinate = None
        self.has_food = False
        self.age += 1
        self.energy = initial_game_settings['energy']
        self.sprite = self.win.create_rectangle(
            self.x - initial_game_settings['size_human'],
            self.y - initial_game_settings['size_human'],
            self.x + initial_game_settings['size_human'],
            self.y + initial_game_settings['size_human'],
            fill='black', outline=self.color_hex, width=3)
        New_Humans.append(self)

    @staticmethod
    def make_new_child():
        global name_of_human
        walls = {0: 0 + initial_game_settings['size_human'], 1: 0 + initial_game_settings['size_human'],
                 2: WIDTH - initial_game_settings['size_human'], 3: HEIGHT - initial_game_settings['size_human']}
        random_wall = random.randrange(4)
        if random_wall == 0 or random_wall == 2:
            y_human = random.randrange(6, HEIGHT - 5)
            human_new = Human(main_win, walls[random_wall], y_human, name_of_human)
        else:
            x_human = random.randrange(6, WIDTH - 5)
            human_new = Human(main_win, x_human, walls[random_wall], name_of_human)
        name_of_human += 1
        return human_new

    def evolution(self):
        global New_Humans, oldest_human, name_of_oldest
        self.recreate_self()
        if self.age > oldest_human:
            oldest_human = self.age
            name_of_oldest = self.name
        bonus_minus = initial_game_settings['max_energy'] - initial_game_settings['energy']
        bonus = int((self.energy - bonus_minus) / 7)
        if random.randrange(100 + bonus) > 50:
            self.kids += 1
            human_baby = self.make_new_child()
            human_baby.speed = self.speed
            human_baby.sense = self.sense

            seed_num = random.randrange(100 + bonus)
            if seed_num >= 75:
                if seed_num >= 95:
                    human_baby.sense += 1
                human_baby.sense += 1
            elif seed_num <= 25:
                if seed_num <= 5:
                    human_baby.sense -= 1
                human_baby.sense -= 1

            seed_num = random.randrange(100 + bonus)
            if seed_num >= 75:
                if seed_num >= 95:
                    human_baby.speed += 1
                human_baby.speed += 1
            elif seed_num <= 25:
                if seed_num <= 5:
                    human_baby.speed -= 1
                human_baby.speed -= 1

            human_baby.color = human_baby.color_scheme()
            human_baby.color_hex = '#%02x%02x%02x' % human_baby.color
            New_Humans.append(human_baby)
        return

    def color_scheme(self):
        if self.speed > self.sense:
            dif = 2 * (self.speed - self.sense)
            if dif <= 10:
                r = int(dif/10 * 255)
                return r, 255, 0
            elif 10 < dif < 20:
                r = int(255)
                g = int(255 - (dif/2)/10 * 255)
                return r, g, 0
            else:
                return 255, 0, 0

        elif self.speed < self.sense:
            dif = self.sense - self.speed
            if dif <= 10:
                b = int(dif / 10 * 255)
                return 0, 255, b
            elif 10 < dif < 20:
                b = int(255)
                g = int(255 - (dif / 2) / 10 * 255)
                return 0, g, b
            else:
                return 0, 0, 255
        else:
            return 0, 255, 0


"""
class Human is the amalgamation of all the inner workings of the Square AI bots and what they do.
The class only covers things that are involved with the the choices the AI needs to make in its day to day life.
"""

"""
class Food is involved with creating Food objects, basically just the circles location, color, nutrience of the food in 
energy and the objects physical form
"""


class Food:

    def __init__(self, canvas, x, y, color):
        self.win = canvas
        self.x, self.y, self.xy = x, y, (x, y)
        self.color = color
        self.energy = color_energy[color]
        self.sprite = self.win.create_oval(self.x - 3, self.y - 3, self.x + 3, self.y + 3, fill=self.color)


"""
class Food is involved with creating Food objects, basically just the circles location, color, nutrience of the food in 
energy and the objects physical form
"""

"""
Creates the Human Objects which are the stored in a list for ease of access and a centralized house of storage
"""


def human_create(num):
    global name_of_human
    walls = {0: 0 + initial_game_settings['size_human'], 1: 0 + initial_game_settings['size_human'],
             2: WIDTH - initial_game_settings['size_human'], 3: HEIGHT - initial_game_settings['size_human']}
    for human in range(num):
        random_wall = random.randrange(4)
        if random_wall == 0 or random_wall == 2:
            y_human = random.randrange(6, HEIGHT-5)
            Humans.append(Human(main_win, walls[random_wall], y_human, name_of_human))
        else:
            x_human = random.randrange(6, WIDTH-5)
            Humans.append(Human(main_win, x_human, walls[random_wall], name_of_human))

        name_of_human += 1


"""
Creates the Human Objects which are then stored in a list for ease of access and a centralized house of storage
"""

"""
Creates the Food Objects which are then stored in a list for ease of access and a centralized house of storage
There is also a call to another function which will store all the Food objects in a dictionary sorted based on their
x coordinate so that the Human doesn't have to check every single object of Food to determine whether or not it is close
enough to actually target it
"""


def food_create(num):
    global Foods_sorted
    remove_w, remove_h = int(WIDTH / 5), int(HEIGHT / 5)
    if remove_w > 100:
        remove_w = 100
    if remove_h > 100:
        remove_h = 100
    for food in range(num):
        x_food, y_food, color_food = \
            random.randrange(remove_w, WIDTH - remove_w), random.randrange(remove_h, HEIGHT - remove_h), \
            random.randrange(0, len(color_energy))
        food_object = Food(main_win, x_food, y_food, list(color_energy)[color_food])
        Foods.append(food_object)
        Foods_sorted = Evol_Module.sorted_dict(Foods_sorted, food_object)
    if len(Foods_sorted) < num < 100000:
        food_create(num - len(Foods_sorted))


"""
Creates the Food Objects which are then stored in a list for ease of access and a centralized house of storage
There is also a call to another function which will store all the Food objects in a dictionary sorted based on their
x coordinate so that the Human doesn't have to check every single object of Food to determine whether or not it is close
enough to actually target it
"""

"""
The GUI function which makes the majority of the GUI. The other parts are initialized at the top of the program
"""


def gui_window():
    global information_label, historical_records, evolution_trends
    info_gridframe = Frame(info_tk, bg='orange')
    historical_records = Listbox(info_gridframe, width=10, font=("Courier", 12))
    historical_records.grid(row=1, column=0)
    information_label = Label(info_gridframe, bg='#525252', width=10, height=10, font=("Courier", 12))
    information_label.grid(row=0, column=0)
    evolution_trends = Listbox(info_gridframe, bg='#525252', width=10, height=10, font=("Courier", 13))
    evolution_trends.grid(row=2, column=0)
    info_gridframe.place(x=65, y=65)
    info_win.update()
    pass


"""
The GUI function which makes the majority of the GUI. The other parts are initialized at the top of the program
"""

"""
The round_count function is called after all humans currently alive have been given a chance to make a move, It 
calculates some basic statistics to then push information to be attached to some Labels and be shown via the GUI
"""


def round_count():
    global history_humans, history_food, evolution_trends
    if len(Humans) > history_humans:
        history_humans = len(Humans)
    if len(Foods) > history_food:
        history_food = len(Foods)
    length_of_label = len(f"\nLongest Living Human is: {name_of_oldest} at the age of {oldest_human} years old")
    information_label['text'] = f"Total Amount of Humans Currently is: {len(Humans)}" \
                                f"\nTotal Food on Table is: {len(Foods)}"\
                                f"\nHistorical Highs for Humans include: {history_humans}" \
                                f"\nHistory for Food include: {history_food}" \
                                f"\nCurrent Year is: {year}AC" \
                                f"\nCurrent Mass Extinction Event: {mass_extinction}" \
                                f"\nLongest Living Human is: {name_of_oldest} at the age of {oldest_human} years old" \
                                f"\nLargest set of Children is: {largest_children_count}" \
                                f"\n Total deaths is: {deaths}"
    information_label['width'] = length_of_label
    historical_records['width'] = length_of_label
    evolution_trends['width'] = length_of_label


"""
The round_count function is called after all humans currently alive have been given a chance to make a move, It 
calculates some basic statistics to then push information to be attached to some Labels and be shown via the GUI
"""

"""
History record is similar to round_count but is called only after all moves for the entire round have been made and
records that need to be kept for longer periods of time are calculated here then stored into list boxes
"""


def history_record():
    global evolution_scoreboard
    sense_trends, total, speed_trends = 0, 0, 0
    for trends in evolution_scoreboard['sense']:
        sense_trends += evolution_scoreboard['sense'][trends] * trends
        total += evolution_scoreboard['sense'][trends]
    sense_trends /= total
    sense_trends = format(sense_trends, '.2f')
    total = 0
    for trends in evolution_scoreboard['speed']:
        speed_trends += evolution_scoreboard['speed'][trends] * trends
        total += evolution_scoreboard['speed'][trends]
    speed_trends /= total
    speed_trends = format(speed_trends, '.2f')
    historical_records.insert(0, f"Humans start year: {historical['Human_pop']}, "
                                 f"Humans end year: {historical['Human_remain']}")
    evolution_trends.insert(0, f"Trends of Sense: {sense_trends}, Trends of Speed: {speed_trends}")
    evolution_scoreboard = {'sense': {}, 'speed': {}}
    pass


"""
History record is similar to round_count but is called only after all moves for the entire round have been made and
records that need to be kept for longer periods of time are calculated here then stored into list boxes
"""

"""
All variables that are initialized as global from the get go are given a defined start value here as a centralized
area for better organization
"""


def define_all_globals():
    global year, mass_extinction, oldest_human, name_of_human, history_humans, history_food, largest_children_count
    global name_of_oldest, deaths
    year, mass_extinction, oldest_human, name_of_human, history_humans, history_food, largest_children_count, \
        name_of_oldest, deaths = 0, 0, 0, 0, 0, 0, 0, '', 0


global information_label, historical_records, evolution_trends
"""
All variables that are initialized as global from the get go are given a defined start value here as a centralized
area for better organization
"""

"""
Initializing the game dunno it did more but I moved some of its systems into other functions so it doesn't do quite
that much and is more of an intermediary
"""


def initialization_of_game():
    global Foods, Foods_sorted
    historical.update({'Food_remain': len(Foods)})
    # Foods, Foods_sorted = [], {}
    food_create(initial_game_settings['foods'])
    round_count()
    historical.update({'Food_pop': len(Foods)})
    return


"""
Initializing the game dunno it did more but I moved some of its systems into other functions so it doesn't do quite
that much and is more of an intermediary
"""

"""
Clean the board of all objects
"""


def clean_board():
    main_win.delete('all')


"""
Clean the board of all objects
"""

"""
Stores some information for the history_record here to be then moved to history_record after completion
"""


def tally():
    for human in Humans:
        human.re_draw_position()
        if human.sense not in evolution_scoreboard['sense']:
            evolution_scoreboard['sense'].update({human.sense: 1})
        else:
            evolution_scoreboard['sense'].update({human.sense: evolution_scoreboard['sense'][human.sense] + 1})
        if human.speed not in evolution_scoreboard['speed']:
            evolution_scoreboard['speed'].update({human.speed: 1})
        else:
            evolution_scoreboard['speed'].update({human.speed: evolution_scoreboard['speed'][human.speed] + 1})


"""
Stores some information for the history_record here to be then moved to history_record after completion
"""

"""
main_game function dunno its more of a secondary main function which acts like a centralized function for main 
program, it also has useless stuff in it currently as I had ideas but changed my mind and never got rid of any of it.
"""


def main_game():
    global Humans, New_Humans, year, Hello
    print(Hello)
    play_game, dead_up_to_now = True, 0
    gui_window()
    while play_game:
        # ___ Initialize Game ___
        initialization_of_game()
        human_create(initial_game_settings['humans'])
        # ___ Initialize Game ___
        while play_game:
            for human in Humans:
                human.draw()
                round_count()
            # main_win.update()
            for human in reversed(Humans):
                if len(Foods) == 0:
                    if human.has_food is True:
                        if human.survive_to_next_round is False:
                            break
                    else:
                        human.kill_human()
                elif human.survive_to_next_round is False:
                    break

            else:
                # final_check()
                # time.sleep(0.5)
                historical.update({'Human_remain': len(Humans)})
                New_Humans = []
                for human in Humans:
                    human.evolution()
                # clean_board()
                Humans = []
                Humans = copy(New_Humans)
                New_Humans = []
                initialization_of_game()
                main_win.update()
                historical.update({'Human_pop': len(Humans), 'year': year,
                                   'deaths_now': deaths, 'dead_this_year': dead_up_to_now})
                dead_up_to_now = deaths
                year += 1
                tally()
                history_record()
                # time.sleep(0.5)
            main_win.update()


"""
main_game function dunno its more of a secondary main function which acts like a centralized function for main 
program, it also has useless stuff in it currently as I had ideas but changed my mind and never got rid of any of it.
"""

"""
The other main function though it isn't a function
"""
if __name__ == "__main__":
    define_all_globals()
    main_game()
    main_tk.mainloop()
"""
The other main function though it isn't a function
"""
