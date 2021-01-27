"""
Developer: Evan Morrison
Program Name: AI_Project/classes/human
Version: 1.0.0
Date: 2021/01/27
"""

import json
import time
from make_objects import generate_random_nums_food as gen_nums
settings = json.load(open('Settings'))


class Human:
    """ ┼┼┼ This is the Human class which holds the program dealing with human objects and their properties ┼┼┼ """

    """ ▼ _______________ Initial set-up _______________ ▼ """

    def __init__(self, canvas, x, y, name):
        self.back_at_base = False
        self.window = canvas
        self.name = 'Human' + str(name)
        self.x, self.y, self.xy = x, y, (x, y)
        self.colorHex, self.colorRGB = '#ffffff', (0, 0, 0)
        self.speed = settings['human']['speed']
        self.sense = settings['human']['sense']
        self.size = settings['human']['size']
        self.energy = settings['human']['energy'] + \
            int((settings['window']['WIDTH'] * settings['window']['HEIGHT'])/5000)
        self.sprite = self.window.create_rectangle(
            self.x - self.size,
            self.y - self.size,
            self.x + self.size,
            self.y + self.size,
            fill='black',
            outline=self.colorHex,
            width=settings['human']['size'] * 0.90
        )
        self.proximity = False
        self.Target = None
        self.direction = None
        self.eaten = False
        self.age, self.kids = 0, 0
        self.foods_dict = {}

    """ ▲ _______________ Initial set-up _______________ ▲ """

    """ ▼ _______________ Small  Quality _______________ ▼ """

    def delete(self, human_dict):
        human_dict.pop(human_dict.index(self))
        self.window.delete(self.sprite)
        del self
        return human_dict

    """ ▲ _______________ Small  Quality _______________ ▲ """

    """ ▼ ______________ Movement section ______________ ▼ """

    def radius_influence(self, food_coordinate_dict):
        closest_object = self.window.find_closest(self.x, self.y, halo=self.sense)
        closest_object = closest_object[0]
        if closest_object != self.sprite:
            corners = self.window.coords(closest_object)
            _food_x = corners[0] + settings['food']['size']
            _food_y = corners[1] + settings['food']['size']
            if _food_x in food_coordinate_dict and _food_y in food_coordinate_dict[_food_x]:
                self.Target = food_coordinate_dict[_food_x][_food_y]
                self.direction = self.Target.xy
                return
            else:
                """This is very carnivore genes will come into play"""
                pass
        return

    def pick_a_random_pixel(self):
        self.direction = tuple(gen_nums(int(settings['window']['WIDTH'] / 4), int(settings['window']['HEIGHT'] / 4)))
        # This pulls a module from make_objects. The function it calls is generate_random_nums_food.

    def find_move(self, food_coordinate_dict):
        if self.eaten or self.proximity:
            return
        else:
            self.radius_influence(food_coordinate_dict)
            if self.direction is None:
                self.pick_a_random_pixel()
        return

    def move_to_safe_zone(self):
        if settings['window']['WIDTH'] - self.x < self.x:
            best_x = settings['window']['WIDTH'] - self.size
            dif_x = settings['window']['WIDTH'] - self.x
        else:
            best_x = self.size
            dif_x = self.x
        if settings['window']['HEIGHT'] - self.y < self.y:
            best_y = settings['window']['HEIGHT'] - self.size
            dif_y = settings['window']['HEIGHT'] - self.y
        else:
            best_y = self.size
            dif_y = self.y
        if dif_x <= dif_y:
            self.direction = (best_x, self.y)
        else:
            self.direction = (self.x, best_y)
        return

    """ ▲ ______________ Movement section ______________ ▲ """

    def accepting_herbivore(self, food_dictionary):
        self.energy += self.Target.energy
        self.Target.delete(food_dictionary)
        self.Target = None
        self.eaten = True
        self.move_to_safe_zone()

    """ ▼ _________________ Check Hits _________________ ▼ """

    def register_if_hit(self, food_dictionary):
        if self.eaten:
            if self.x <= settings['human']['size'] or \
                    self.x >= settings['window']['WIDTH'] - settings['human']['size'] or \
                    self.y <= settings['human']['size'] or \
                    self.y >= settings['window']['HEIGHT'] - settings['human']['size']:
                self.back_at_base = True
                return
        elif self.Target is not None and self.Target.y in food_dictionary[self.Target.x]:
            if abs(self.x - self.Target.x) <= self.Target.size and abs(self.y - self.Target.y) <= self.Target.size:
                self.accepting_herbivore(food_dictionary)  # Special stuff happens to those who are eaten
                """Eat and Delete the Food, Possibly move them to a new section """
            else:
                """Don't know if this is possible but if it does happen then this shouldn't matter"""
                """Scratch That this is for if you get to the food but it was already eaten"""
        else:
            self.find_move(food_dictionary)
        return

    def update_coordinates(self, food_dictionary):
        difference_x, difference_y = self.direction[0] - self.x, self.direction[1] - self.y
        if abs(difference_x) >= abs(difference_y):
            if difference_x > 0:
                self.x += 1
                self.window.move(self.sprite, 1, 0)
            else:
                self.x -= 1
                self.window.move(self.sprite, -1, 0)
        else:
            if difference_y > 0:
                self.y += 1
                self.window.move(self.sprite, 0, 1)
            else:
                self.y -= 1
                self.window.move(self.sprite, 0, -1)
        # self.window.update()
        self.xy = (self.x, self.y)
        if self.xy == self.direction:
            self.direction = None
            self.register_if_hit(food_dictionary)
        return

    """ ▲ _________________ Check Hits _________________ ▲ """

    """ ▼ _________________ Draw Human _________________ ▼ """

    def re_draw_position(self):
        self.sprite = \
            self.window.create_rectangle(
                self.x - self.size,
                self.y - self.size,
                self.x + self.size,
                self.y + self.size,
                fill='black',
                outline=self.colorHex,
                width=settings['human']['size'] * 0.90
            )

    """ ▲ _________________ Draw Human _________________ ▲ """


""" ▲ ________________ End of Class ________________ ▲ """

""" ▼ _______________ Main Operation _______________ ▼ """


def run_algorithm(self, food_dictionary, list_of_humans):
    if self.energy <= 0:
        self.delete(list_of_humans)
        time.sleep(1 / settings['window']['fps'])
        """Human is dead, something"""
    self.find_move(food_dictionary)
    for _ in range(self.speed):
        if self.back_at_base is False:
            self.update_coordinates(food_dictionary)
        else:
            self.window.update()
            return True
    self.energy -= (self.speed + self.sense/5)/10
    self.window.update()
    return False


""" ▲ _______________ Main Operation _______________ ▲ """
