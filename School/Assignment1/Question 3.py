"""
Name: Question 3
Developer: Evan Morrison
Version: 1.0
Since: 1.0
"""


time = 23  # minutes
distance = 2.4  # kilometres

print(f"The Time to walk 4 kilometres at a pace of {distance}km / {time}m is {round((4 / distance) * time, 2)} minutes")
# this will calculate the time inside of the print statement using (distanceGoing / distance) * time or (4/2.4)*23

print(f"The Student can walk {int(30 / ((0.2 / distance) * time))} 200-metre laps in 30 minutes")
# this will calculate the number of Labs inside of the print statement using (30 / ((0.2 / distance) * time or (30m / ((0.2km / 2.4km) * 23m)) then floored with int
