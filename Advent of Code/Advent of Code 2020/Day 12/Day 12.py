import re
coordinate = [0, 0]
waypoint = [1, 10]
listy = []


def north(x):
    waypoint[0] = waypoint[0] + x
    return


def south(x):
    waypoint[0] = waypoint[0] - x
    return


def east(x):
    waypoint[1] = waypoint[1] + x
    return


def west(x):
    waypoint[1] = waypoint[1] - x
    return


def left(x):
    global waypoint
    x = int(x / 90)
    for left_turn in range(0, x):
        hold = -1 * waypoint[0]
        waypoint[0] = waypoint[1]
        waypoint[1] = hold
    return


def right(x):
    global waypoint
    x = int(x / 90)
    for left_turn in range(0, x):
        hold = waypoint[0]
        waypoint[0] = -1 * waypoint[1]
        waypoint[1] = hold
    return


def forward(x):
    global waypoint
    coordinate[0] = coordinate[0] + waypoint[0] * x
    coordinate[1] = coordinate[1] + waypoint[1] * x
    return


with open("E:\\Advent\\Day 12.txt", 'r') as Day12:
    days = Day12.readlines()
    for i in days:
        i = i.replace('\n', '')
        command = re.findall(r'[A-Z]', i)
        order = re.findall(r'\d{1,3}', i)
        # print(order)
        if command[0] == 'N':
            north(int(order[0]))
        elif command[0] == 'S':
            south(int(order[0]))
        elif command[0] == 'E':
            east(int(order[0]))
        elif command[0] == 'W':
            west(int(order[0]))
        elif command[0] == 'L':
            left(int(order[0]))
        elif command[0] == 'R':
            right(int(order[0]))
        elif command[0] == 'F':
            forward(int(order[0]))
        # print(coordinate)
        # print(waypoint)
# print('\n\n\n')
# print(coordinate)
# print(waypoint)
answer1 = abs(coordinate[0]) + abs(coordinate[1])
print("The Answer to Part 2 is: %d" % answer1)