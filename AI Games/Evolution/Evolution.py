from tkinter import Tk, Canvas, Listbox, Label, Button, Entry, Frame, StringVar
from itertools import product
import random
from math import floor, ceil
import time
random.seed(a=None, version=2)
tk = Tk()
tk_stats = Tk()
width = 2000
height = 1300
width2 = 2500
canvas = Canvas(tk, width=width2, height=height, bg='white')
stats_canvas = Canvas(tk_stats, width=1000, height=1000, bg='#378AA6')
canvas.pack()
stats_canvas.pack()
global list_highscores, Labels_Humans, Button_Humans, Humans, Foods, Foods_coord
global entry_of_starter_food


class Human:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.speed = initializing_settings['speed']
        self.sense = initializing_settings['sense']
        self.energy = initializing_settings['energy']
        self.coord = (x, y)
        self.sprite = 0
        self.corners = []
        self.R = 255
        self.G = 255
        self.position()
        self.found = None
        self.found_foods = None
        self.age, self.kids = 0, 0

    def move(self, x, y):
        self.coord = (self.coord[0] + (x * 10), self.coord[1] + (y * 10))

    def movement(self):
        # print('\n\n')
        # try:
        x, y = self.coord[0], self.coord[1]
        good_moves, food_found = [], None
        # print(repr(good_moves))
        if self.found is not None:
            # print('1', repr(good_moves))
            if self.found_foods not in Foods:
                self.found = None
                self.found_foods = None
                # print('2', repr(good_moves))
            else:
                temp_x, temp_y = self.found[0] - x, self.found[1] - y
                # print('3', repr(good_moves))
                if abs(temp_x) + abs(temp_y) >= 15:
                    good_moves = [(x + floor(temp_x * (15 / (abs(temp_x) + abs(temp_y)))),
                                  y + floor(temp_y * (15 / (abs(temp_x) + abs(temp_y)))))]
                    t_x, t_y = good_moves[0]
                    if t_x < 0:
                        t_x = x - self.corners[0]
                    if t_y < 0:
                        t_y = y - self.corners[1]
                    good_moves = [(t_x, t_y)]
                    # print('4', repr(good_moves))

                else:
                    good_moves = [(temp_x, temp_y)]
                    # print('5', repr(good_moves))
        if self.found is None:
            good_moves, food_found = self.pathmaker()
            # print('6', repr(good_moves))
            if len(good_moves) == 0:
                good_moves, food_found = self.pathfinder()
                # print('11', repr(good_moves))
        # print('7', repr(good_moves))
        if len(good_moves) == 1:
            # print('8', repr(good_moves))
            self.found = good_moves[0]
            self.found_foods = food_found
            temp_x, temp_y = good_moves[0][0] - x, good_moves[0][1] - y
            if abs(temp_x) + abs(temp_y) >= 15:
                # print('9', repr(good_moves))
                t_x, t_y = x + floor(temp_x * (15 / (abs(temp_x) + abs(temp_y)))), \
                           y + floor(temp_y * (15 / (abs(temp_x) + abs(temp_y))))
                # = good_moves[0]
                if t_x < 0:
                    t_x = x - self.corners[0]
                if t_y < 0:
                    t_y = y - self.corners[1]
                good_moves = [(t_x, t_y)]
            self.coord = good_moves[0]
        else:
            # print('10', repr(good_moves), food_found)
            move = random.randrange(0, len(good_moves))

            self.coord = good_moves[move]
        self.position()
        return
        # except:
        #     exit()

    def pathfinder(self):
        x, y, good_moves = self.coord[0], self.coord[1], []
        for x_temp, y_temp in product(range(x - floor(10 * self.sense), x + ceil(11 * self.sense)),
                                      range(y - floor(10 * self.sense), y + ceil(11 * self.sense))):
            xxxx = ((x - self.corners[0]), width - (self.corners[2] - x),
                    (y - self.corners[1]), height - (self.corners[3] - y))
            if (x_temp, y_temp) != (x, y) and (x - self.corners[0]) <= x_temp <= width - (self.corners[2] - x) and\
                    (y - self.corners[1]) <= y_temp <= height - (self.corners[3] - y):
                if abs(x - x_temp) + abs(y - y_temp) < 15 * self.speed:
                    good_moves.append((x_temp, y_temp))
                if x_temp in Foods_coord:
                    for foods in Foods_coord[x_temp]:
                        if (x_temp, y_temp) == foods.center:
                            # print("Primo")
                            return [(x_temp, y_temp)], foods
        return good_moves, None

    def pathmaker(self):
        x, y, good_moves = self.coord[0], self.coord[1], []
        radius = 10 * self.sense
        if (ceil(radius) - radius) > (radius - floor(radius)):
            radius = ceil(radius)
        else:
            radius = floor(radius)
        good_squares = []
        list_temp = []
        for foods_c in range(x-10, x+11):
            if foods_c in Foods_coord:
                for foods_objects in Foods_coord[foods_c]:
                    x_food, y_food = foods_objects.center
                    if (x - x_food)**2 + (y - y_food)**2 <= radius**2 and \
                            (x - self.corners[0]) <= x_food <= width - (self.corners[2] - x) and \
                            (y - self.corners[1]) <= y_food <= height - (self.corners[3] - y):
                        return [(x_food, y_food)], foods_objects
        for x_squared in range(-radius, radius+1):
            for y_squared in range(-radius, radius+1):
                list_temp.append((x_squared, y_squared))
                if ((x_squared**2) + (y_squared**2)) <= radius**2:
                    if (x - self.corners[0]) <= 10 * x_squared + x <= width - (self.corners[2] - x) and \
                            (y - self.corners[1]) <= 10 * y_squared + y <= height - (self.corners[3] - y):
                        good_squares.append((10 * x_squared + x, 10 * y_squared + y))
        # for x_temp, y_temp in product(range(x - floor(20 * self.sense), x + ceil(21 * self.sense)),
        #                               range(y - floor(20 * self.sense), y + ceil(21 * self.sense))):
        #     if (x_temp, y_temp) != (x, y) and 25 <= x_temp <= width - 40 and 25 <= y_temp <= height - 40:
        #         good_moves.append((x_temp, y_temp))
        return good_squares, None

    def position(self):
        Hello = Foods_coord
        canvas.delete(self.sprite)
        color = '#%02x%02x%02x' % (floor(self.R - self.speed*25), floor(self.G - self.sense*25), 0)
        self.corners = [self.coord[0] - 5, self.coord[1] - 5, self.coord[0] + 5, self.coord[1] + 5]
        self.sprite = canvas.create_rectangle(
            self.corners[0], self.corners[1],
            self.corners[2], self.corners[3],
            fill=color)

    def draw(self):
        global Foods_coord
        self.movement()
        canvas.update()
        if self.energy <= 0:
            Humans.pop(Humans.index(self))
            canvas.delete(self.sprite)
            return
        if self.energy > 125:
            if random.randrange(100) > 95:
                self.baby()
                self.energy -= 65
        self.energy -= (((self.speed/4) ** 2) + self.sense)
        # for humans in Humans:
        human_coord = self.corners
        for foods in Foods:
            food_coord = foods.coord
            if human_coord[0] <= foods.center[0] <= human_coord[2] and \
                    human_coord[1] <= foods.center[1] <= human_coord[3]:
                self.eat_food(foods)
        self.age += 1
        if len(Foods) < 500:
            if random.randrange(1000) > 750:
                # try:
                x_f, y_f, color_f = random.randrange(25, width - 40), random.randrange(25, height - 40), \
                                    random.randrange(len(colors))
                foods_obj = Food(canvas, x_f, y_f, colors[color_f])
                Foods.append(foods_obj)
                Foods_coord = sorted_dict(Foods_coord, foods_obj)
                # except KeyError:
                #     print('Words')
                #     raise KeyError
        self.largest_check()

    def eat_food(self, obj):
        try:
            self.energy = self.energy + obj.energy
            if self.energy > 200:
                self.energy = 200
            temp_dict = Foods_coord[obj.center[0]]
            temp_dict.pop(temp_dict.index(obj))
            canvas.delete(obj.sprite)
            Foods.pop(Foods.index(obj))
        except KeyError:
            print('Words')
            raise KeyError

    def baby(self):
        little_baby = 0
        if self.coord[0] < 10 and self.coord[1] < 10:
            little_baby = Human(canvas, self.coord[0] + 10, self.coord[1] + 10)
        elif self.coord[0] < 10 <= self.coord[1]:
            little_baby = Human(canvas, self.coord[0] + 10, self.coord[1] - 10)
        elif self.coord[0] >= 10 > self.coord[1]:
            little_baby = Human(canvas, self.coord[0] - 10, self.coord[1] + 10)
        else:
            little_baby = Human(canvas, self.coord[0] - 10, self.coord[1] - 10)
        Humans.append(little_baby)
        num = random.randrange(0, 100)
        little_baby.sense = self.sense
        little_baby.speed = self.speed
        if num > 85:
            little_baby.speed += 0.1
        elif num < 15:
            little_baby.speed -= 0.1
        if little_baby.speed > 10:
            little_baby.speed = 10
        elif little_baby.speed < 0:
            little_baby.speed = 0
        num = random.randrange(0, 100)
        if num > 85:
            little_baby.sense += 0.1
        elif num < 15:
            little_baby.sense -= 0.1
        if little_baby.sense > 10:
            little_baby.sense = 10
        elif little_baby.sense < 0:
            little_baby.sense = 0
        self.kids += 1

    def largest_check(self):
        global longest_living, largest_children_count
        if self.age > longest_living:
            longest_living = self.age
        if self.kids > largest_children_count:
            largest_children_count = self.kids


class Food:

    all_foods = {}

    def __init__(self, canvas, x, y, color):
        color_energy = {'Red': 40, 'Blue': 50, 'Green': 75, 'Purple': 90}
        self.canvas = canvas
        self.color = color
        self.energy = color_energy[color]
        self.center = (x, y)
        self.coord = [x - 3, y - 3, x + 3, y + 3]
        self.all_foods.update({(x, y): self})
        self.sprite = canvas.create_oval(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=color)


def sorted_dict(x_dict, t_f):
    if t_f.center[0] not in x_dict:
        x_dict.update({t_f.center[0]: [t_f]})
    else:
        temps = x_dict[t_f.center[0]]
        temps.append(t_f)
    return x_dict


def make_list(x):
    global list_highscores, Labels_Humans
    list_highscores.delete(0, 'end')
    for human_kind in x:
        list_highscores.insert("end", f"{human_kind} + {human_kind.age} + {human_kind.kids}")
    return list_highscores


def pause_sim():
    global pause
    if pause == 1:
        pause = 0
    else:
        pause = 1


def reset_program():
    global reset_all
    print(initializing_settings)
    entered_of_starter_food.set("")
    reset_all = 1


def how_much_food():
    global Foods_coord, entered_of_starter_food, reset_all
    initializing_settings.update({'food': int(entry_of_starter_food.get())})


def starting_human_count():
    pass


def initialize_gui():
    global list_highscores, Labels_Humans, Button_Humans
    global entry_of_starter_food
    # ************************ Widget
    # list_highscores = Listbox(tk, bg='grey', width=50, height=10)
    # list_highscores.place(x=2000, y=0)
    # Labels_Humans = Label(tk, bg='grey', width=50, height=10, font=("Courier", 12))
    # Labels_Humans.place(x=2000, y=500)
    # Button_Humans = Button(tk, bg='black', width=10, height=1, text='Press Me',
    #                        font=("Courier", 20), fg='white', command=lambda: pause_sim())
    # Button_Humans.place(anchor='se', x=2500, y=1300)
    # ************************ Widget
    canvas.create_rectangle(width, 0, width2, height, fill='orange')
    gridframe = Frame(tk, bg='orange')

    list_highscores = Listbox(gridframe, bg='grey', width=50, height=10)
    list_highscores.grid(row=2, column=0)
    pause_button = Button(gridframe, bg='black', width=10, height=1, text='Pause',
                          font=("Courier", 20), fg='white', command=lambda: pause_sim())
    pause_button.grid(row=3, column=0)
    reset_button = Button(gridframe, bg='black', width=10, height=1, text='Stop',
                          font=("Courier", 20), fg='white', command=lambda: reset_program())
    reset_button.grid(row=4, column=0)

    gridframe_entry = Frame(tk, bg='orange')
    label_entry = Label(gridframe, text='This is the Entry Section', font=("Courier", int((width2-width)/22)))
    label_entry.grid(row=5, column=0)

    entry_of_starter_food_label = Label(gridframe_entry, bg='orange', text='New Food Amount',
                                        font=("Courier", int((width2-width) / 35)))
    entry_of_starter_food_label.grid(row=2, column=1)
    entry_of_starter_food = Entry(gridframe_entry,
                                  textvariable=entered_of_starter_food)
    entry_of_starter_food.grid(row=2, column=2)
    entry_of_starter_food.bind("<Return>", how_much_food)

    entry_of_starter_food_label = Label(gridframe_entry, bg='orange', text='New Human Amount',
                                        font=("Courier", int((width2 - width) / 35)))
    entry_of_starter_food_label.grid(row=3, column=1)
    entry_of_starter_food = Entry(gridframe_entry, textvariable=entered_of_starter_food)
    entry_of_starter_food.grid(row=3, column=2)
    entry_of_starter_food.bind("<Return>", how_much_food)

    gridframe.place(x=width+15, y=25)
    gridframe_entry.place(x=width+20, y=height/2)
    canvas.create_rectangle(0, 0, width, height, fill='black', outline='purple', width=15)
    second_gui_nums()


def second_gui_nums():
    global Labels_Humans, Current_settings, Labels_Humans2
    grid_settings = Frame(tk_stats, bg='#378AA6')
    Labels_Humans = Label(grid_settings, bg='#378AA6', width=45, height=10, font=("Courier", 13))
    Labels_Humans.grid(row=0, column=0)
    Current_settings = Label(grid_settings, bg='#378AA6', width=45, height=10, font=("Courier", 13))
    Current_settings.grid(row=0, column=1)
    grid_settings.place(x=5, y=30)


def initialize_stuff():
    global list_highscores, Button_Humans, Humans, Foods, Foods_coord
    Foods, Humans, Foods_coord = [], [], {}
    for i in range(initializing_settings['food']):
        x_f, y_f, color_f = random.randrange(25, width - 40), random.randrange(25, height - 40), random.randrange(
            len(colors))
        temp_food = Food(canvas, x_f, y_f, colors[color_f])
        Foods.append(temp_food)
        Foods_coord = sorted_dict(Foods_coord, temp_food)
    # Foods_coord = sorted(Foods_coord)
    # print(Foods_coord)
    for i in range(initializing_settings['humans']):
        x_f, y_f = random.randrange(25, width - 40), random.randrange(25, height - 40)
        Humans.append(Human(canvas, x_f, y_f))
    hell = canvas.find_all()
    Current_settings['text'] = f"Starting Humans is set to : {initializing_settings['humans']}" \
                               f"\nStarting Food is set to : {initializing_settings['food']}" \
                               f"\nBeginning Sense set to : {initializing_settings['sense']}" \
                               f"\nBeginning Speed set to : {initializing_settings['speed']}" \
                               f"\nBeginning Energy set to : {initializing_settings['energy']}\n"


def top_check():
    if len(top_10) == 0:
        top_10.append(human)
    else:
        for indexed in range(len(top_10)):
            if human.age + human.kids > (top_10[indexed].age + top_10[indexed].kids):
                top_10.insert(indexed, human)
                break
            elif len(top_10) < 10:
                top_10.append(human)
                break
    while len(top_10) > 10:
        top_10.pop(-1)


def change_text():
    global History_Humans, History_Food
    if len(Humans) > History_Humans:
        History_Humans = len(Humans)
    if len(Foods) > History_Food:
        History_Food = len(Foods)
    Labels_Humans['text'] = f"\nTotal Amount of Humans Currently is: {len(Humans)}" \
                            f"\nTotal Food on Table is: {len(Foods)}"\
                            f"\nHistorical Highs for Humans include: {History_Humans}" \
                            f"\nHistory for Food include: {History_Food}" \
                            f"\nCurrent Year is: {Year}AC" \
                            f"\nCurrent Mass Extinction Event: {Mass_extinction}" \
                            f"\nLongest Living Human is: {longest_living} years old" \
                            f"\nLargest set of Children is: {largest_children_count}"


initializing_settings = {'food': 500, 'humans': 1, 'sense': 5, 'speed': 2, 'energy': 100}
colors, pause = ['Red', 'Blue', 'Green', 'Purple'], 0
length_time = 0.1
History_Humans, History_Food, longest_living, largest_children_count = 0, 0, 0, 0
Year = 0
entered_of_starter_food = StringVar()
Mass_extinction = 0
while True:
    reset_all = 0
    initialize_gui()
    initialize_stuff()
    while True:
        start = time.time()
        top_10 = []
        for human in Humans:
            human.draw()
            top_check()
            canvas.update()
        if len(Humans) == 0:
            for i in range(1):
                x_f, y_f = random.randrange(25, width - 40), random.randrange(25, height - 40)
                Humans.append(Human(canvas, x_f, y_f))
                Mass_extinction += 1
        change_text()
        make_list(top_10)
        end = time.time()
        if (end - start) < length_time:
            time.sleep(length_time - (end - start))
        Year += 1
        if pause == 1:
            if reset_all == 1:
                break
            while True:
                canvas.update()
                if pause == 0:
                    break
                elif reset_all == 1:
                    break
        if reset_all == 1:
            break
    canvas.delete('all')
# tk.mainloop()
pass
