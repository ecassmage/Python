class Food:
    def __init__(self, canvas, coord):
        self.canvas = canvas
        self.energy = round(canvas.settings['food']['energy'])
        self.coord = coord
        self.size = self.canvas.settings['food']['size']
        self.eaten = False
        self.sprite = self.canvas.canvas.create_oval(
            self.coord[0] - self.size, self.coord[1] - self.size, self.coord[0] + self.size, self.coord[1] + self.size,
            fill='white'
        )

    def resetFood(self, coord):
        self.coord = coord
        self.size = self.canvas.settings['food']['size']
        self.eaten = False
        self.canvas.canvas.coords(
            self.sprite,
            self.coord[0] - self.size,
            self.coord[1] - self.size,
            self.coord[0] + self.size,
            self.coord[1] + self.size
        )
        return self

    def hideFood(self, removeDict=True):
        self.canvas.canvas.coords(self.sprite, 0, 0, 0, 0)
        self.eaten = True
        self.canvas.storedFood.append(self.canvas.usedFood[self.coord[0]].pop(self.coord[1]))
        if len(self.canvas.usedFood[self.coord[0]]) == 0 and removeDict:
            self.canvas.usedFood.pop(self.coord[0])

    def stringClass(self):
        return f"Class Information: {self}\n" \
               f"\tEnergy: {self.energy}\n" \
               f"\tCoordinates: {self.coord}\n" \
               f"\tSize: {self.size}\n" \
               f"\tEaten: {self.eaten}\n" \
               f"\tSprite ID: {self.sprite}\n"
