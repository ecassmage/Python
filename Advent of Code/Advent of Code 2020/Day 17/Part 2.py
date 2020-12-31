from itertools import product
from copy import copy


def neighbour_buddies(neigh_coord, x1, y1, z1, w1):
    alive = 0
    for neighbour in product(range(x1 - 1, x1 + 2), range(y1 - 1, y1 + 2), range(z1 - 1, z1 + 2), range(w1 - 1, w1 + 2)):
        print(neighbour)
        exit()
        if neighbour in neigh_coord:
            alive += 1
    if (x1, y1, z1, w1) in neigh_coord:
        alive -= 1
    return alive


def size_of_cube(coord_size):
    l_x, l_y, l_z, l_w, cube_bound = 0, 0, 0, 0, []
    for x1, y1, z1, w1 in coord_size:
        if x1 > l_x:
            l_x = x1
        if y1 > l_y:
            l_y = y1
        if z1 > l_z:
            l_z = z1
        if w1 > l_w:
            l_w = w1
    cube_bound.append(l_x + 2), cube_bound.append(l_y + 2), cube_bound.append(l_z + 2), cube_bound.append(l_w + 2)
    for x1, y1, z1, w1 in coord_size:
        if x1 < l_x:
            l_x = x1
        if y1 < l_y:
            l_y = y1
        if z1 < l_z:
            l_z = z1
        if w1 < l_w:
            l_w = w1
    cube_bound.append(l_x - 1), cube_bound.append(l_y - 1), cube_bound.append(l_z - 1), cube_bound.append(l_w - 1)
    return cube_bound


def game_of_life(game_of_choice):
    new_list = []
    boundaries = size_of_cube(game_of_choice)
    middle_split = int(len(boundaries) / 2)
    # print("This is game of choice", game_of_choice)
    upper_bound = boundaries[:middle_split]
    lower_bound = boundaries[middle_split:]
    print(upper_bound, lower_bound)
    # print("This is the split", upper_bound, lower_bound)
    # print("The Bounds", lower_bound[0], upper_bound[0], lower_bound[1], upper_bound[1], lower_bound[2], upper_bound[2])
    for game_x in range(lower_bound[0], upper_bound[0]):
        for game_y in range(lower_bound[1], upper_bound[1]):
            for game_z in range(lower_bound[2], upper_bound[2]):
                for game_w in range(lower_bound[3], upper_bound[3]):
                    alive_count = neighbour_buddies(game_of_choice, game_x, game_y, game_z, game_w)
                    # print(alive_count)
                    # print((game_x, game_y, game_z))
                    if (game_x, game_y, game_z, game_w) in game_of_choice:
                        if alive_count == 2 or alive_count == 3:
                            # print("Alive")
                            new_list.append((game_x, game_y, game_z, game_w))
                    elif alive_count == 3:
                        # print("Dead")
                        new_list.append((game_x, game_y, game_z, game_w))
    # print("The New list is", new_list)
    return new_list


file = open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 17\\input.txt')
fin = []
for line in file.readlines():
    print(line.replace('\n', ''))
    fin.append(line)
grid = tuple(map(str.rstrip, fin))
coordinates = []
for x, row in enumerate(grid):
    for y, point in enumerate(row):
        if point == '#':
            coordinates.append((x, y, 0, 0))
# print(coordinates)
for count in range(0, 6):
    print("The Current Cycle: ", count + 1)
    coordinates = game_of_life(coordinates)
    part_1 = int(len(coordinates))
    print("The Answer to Part 1 is: %d" % part_1)
