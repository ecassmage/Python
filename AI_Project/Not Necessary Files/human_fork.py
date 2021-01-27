import json
import random
import math
from multiprocessing import Pool
settings = json.load(open('Settings'))


class Human:
    """ ┼┼┼ This is the Human class which holds the program dealing with human objects and their properties ┼┼┼ """

    """ ▼ _______________ Initial set-up _______________ ▼ """

    def __init__(self, canvas, x, y, name):
        self.alive, self.back_at_base = True, False
        # self.window = canvas
        self.name = 'Human' + str(name)
        self.x, self.y, self.xy = x, y, (x, y)
        self.colorHex, self.colorRGB = '#ffffff', (0, 0, 0)
        self.speed = settings['human']['speed']
        self.sense = settings['human']['sense']
        self.size = settings['human']['size']
        self.energy = settings['human']['energy']
        self.sprite = canvas.create_rectangle(
            self.x - self.size,
            self.y - self.size,
            self.x + self.size,
            self.y + self.size,
            fill='black',
            outline=self.colorHex,
            width=settings['human']['size'] * 0.90
        )
        self.moves = []
        self.proximity = False
        self.Target = None
        self.direction = None
        self.eaten = False
        self.age, self.kids = 0, 0
        self.foods_dict = {}

    """ ▲ _______________ Initial set-up _______________ ▲ """

    """ ▼ ______________ Movement section ______________ ▼ """

    def radius_influence(self, food_coordinate_dict):
        for checking_the_x in range(self.x - self.sense, self.x + self.sense):
            if checking_the_x in food_coordinate_dict:
                y_range = math.ceil(math.sqrt(self.sense ** 2 - (checking_the_x - self.x) ** 2))
                if y_range * 2 > len(food_coordinate_dict[checking_the_x]):
                    for checking_the_y in food_coordinate_dict[checking_the_x]:
                        if (checking_the_x - self.x) ** 2 + (checking_the_y - self.y) ** 2 <= self.sense ** 2:
                            self.Target = food_coordinate_dict[checking_the_x][checking_the_y]
                            self.direction = self.Target.xy
                            return
                else:
                    for checking_the_y in range(self.y - y_range, self.y + y_range + 1):
                        if checking_the_y in food_coordinate_dict[checking_the_x] and\
                                (checking_the_x - self.x) ** 2 + (checking_the_y - self.y) ** 2 <= self.sense ** 2:
                            self.Target = food_coordinate_dict[checking_the_x][checking_the_y]
                            self.direction = self.Target.xy
                            return
        return

    def pick_a_random_pixel(self):
        self.direction = (
            random.randrange(6, settings['window']['WIDTH'] - 5),  # This is x
            random.randrange(6, settings['window']['HEIGHT'] - 5)  # This is y
        )

    def find_move(self, food_coordinate_dict):
        if self.eaten or self.proximity:
            return
        else:
            self.radius_influence(food_coordinate_dict)
            if self.direction is None:
                self.pick_a_random_pixel()
        return

    """ ▲ ______________ Movement section ______________ ▲ """

    """ ▼ _________________ Check Hits _________________ ▼ """

    def register_if_hit(self, food_dictionary):
        if self.eaten:
            if self.x <= settings['human']['size'] or \
                    self.x >= settings['window']['WIDTH'] - settings['human']['size'] or \
                    self.y <= settings['human']['size'] or \
                    self.y >= settings['window']['HEIGHT'] - settings['human']['size']:
                self.back_at_base = True
                return
        else:
            if self.Target is not None and self.Target == food_dictionary[self.Target.x][self.Target.y]:
                if abs(self.x - self.Target.x) <= self.Target.size and abs(self.y - self.Target.y) <= self.Target.size:
                    self.eaten = True
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
            else:
                self.x -= 1
        else:
            if difference_y > 0:
                self.y += 1
            else:
                self.y -= 1
        self.xy = (self.x, self.y)
        if self.xy == self.direction:
            self.direction = None
            self.register_if_hit(food_dictionary)
        return

    """ ▲ _________________ Check Hits _________________ ▲ """

    """ ▼ _________________ Draw Human _________________ ▼ """

    def re_draw_position(self, canvas):
        canvas.delete(self.sprite)
        self.sprite = \
            canvas.create_rectangle(
                self.x - self.size,
                self.y - self.size,
                self.x + self.size,
                self.y + self.size,
                fill='black',
                outline=self.colorHex,
                width=settings['human']['size'] * 0.90
            )

    """ ▲ _________________ Draw Human _________________ ▲ """


def run_algorithm(self):
    food_dictionary = self.foods_dict
    if self.energy <= 0:
        """Human is dead, something"""
    self.find_move(food_dictionary)
    self.moves = []
    # if settings['window']
    for _ in range(self.speed):
        if self.eaten is False:
            self.update_coordinates(food_dictionary)
    return self
