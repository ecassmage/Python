"""
Developer: Evan Morrison
Program Name: AI_Project/classes/food
Version: 1.0.0
Date: 2021/01/27
"""

import json
settings = json.load(open('Settings'))


class Food:

    def __init__(self, canvas, x, y, color):
        self.alive = True
        self.window = canvas
        self.x, self.y, self.xy = x, y, (x, y)
        self.color = color
        self.size = settings['food']['size']
        self.energy = settings['food']['food_color'][color]
        self.sprite = self.window.create_oval(
            self.x - self.size,
            self.y - self.size,
            self.x + self.size,
            self.y + self.size,
            fill=self.color
        )

    def delete(self, food_dict):
        self.window.delete(self.sprite)
        del food_dict[self.x][self.y]
        if len(food_dict[self.x]) == 0:
            del food_dict[self.x]
        del self
        return food_dict

    def clean_board(self):
        self.window.delete(self.sprite)
        del self
