"""
Name: Question 2
Developer: Evan Morrison
Version: 1.0
Since: 1.0
"""


pi = 3.14  # Doesn't the math library have a pi variable? - pi
r = 6  # - radius
h = 19  # - height
surfaceArea = round(2 * pi * r * h)  # Calculates the surface Area of a cylinder using r as radius, pi for pi and h for height
print(f"the Surface Area of the Cylindrical tower height=>{h} and radius=>{r} rounded to nearest integer is {surfaceArea} metres ^ 2")  # prints the Information to terminal
lastTwo = int(str(surfaceArea)[-2:])  # splices the last two digits from the rest of the number
print(f"The Last two digits of the number are: {lastTwo}\n")  # prints the last two digits to the screen

