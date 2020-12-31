import re
flipped_tile = []


def north_east(x, y):  # (0, 1)
    return x, (y + 1)


def north_west(x, y):  # (-1, 1)
    return x - 1, y + 1


def south_east(x, y):  # (1, -1)
    return x + 1, y - 1


def south_west(x, y):  # (0, -1)
    return x, y - 1


def east(x, y):  # (1, 0)
    return x + 1, y


def west(x, y):  # (-1, 0)
    return x - 1, y


def neighbour_buds(happy_neighbours, x1, y1):
    smiles = 0
    # print(happy_neighbours, x1, y1)
    changes = [(0, 1), (-1, 1), (1, -1), (0, -1), (1, 0), (-1, 0)]
    for adjacency_bonus_x, adjacency_bonus_y in changes:
        validation = tuple((adjacency_bonus_x + x1, adjacency_bonus_y + y1))
        # print(validation)
        if validation in happy_neighbours:
            smiles += 1
    # if (x1, y1) in happy_neighbours:
    #     smiles -= 1
    # print(smiles)
    # exit()
    return smiles


def size_of_ego(coord_size):
    l_x, l_y, art_museum = 0, 0, []
    for x1, y1 in coord_size:
        if x1 > l_x:
            l_x = x1
        if y1 > l_y:
            l_y = y1
    art_museum.append(l_x + 2), art_museum.append(l_y + 2)
    # print("Coord_Size", coord_size)
    for x1, y1 in coord_size:
        if x1 < l_x:
            l_x = x1
        if y1 < l_y:
            l_y = y1
    art_museum.append(l_x - 1), art_museum.append(l_y - 1)
    return art_museum


def art_is_weird(lifestyle_points):
    # print(lifestyle_points)
    all_new_list = set()
    boundaries = size_of_ego(lifestyle_points)
    # print(boundaries)
    middle_split = int(len(boundaries) / 2)
    upper_bound = boundaries[:middle_split]
    lower_bound = boundaries[middle_split:]
    # print(upper_bound, lower_bound)
    for x2 in range(lower_bound[0], upper_bound[0]):
        for y2 in range(lower_bound[1], upper_bound[1]):
            points = neighbour_buds(lifestyle_points, x2, y2)
            if points == 2 or ((x2, y2) in lifestyle_points and points == 1):
                all_new_list.add((x2, y2))
    # print(all_new_list)
    return all_new_list


def coord_is_good(bag_of_goodies, candidate):
    if candidate not in bag_of_goodies:
        bag_of_goodies.append(coordinate)
    else:
        bag_of_goodies.pop(bag_of_goodies.index(candidate))
    return bag_of_goodies


def walks_of_life(tile_instruction):
    x, y = 0, 0
    for i, tile_change in enumerate(tile_instruction):
        # print(i)
        # print(tile_change)
        if tile_change == 'ne':
            x, y = north_east(x, y)
        if tile_change == 'nw':
            x, y = north_west(x, y)
        if tile_change == 'se':
            x, y = south_east(x, y)
        if tile_change == 'sw':
            x, y = south_west(x, y)
        if tile_change == 'e':
            x, y = east(x, y)
        if tile_change == 'w':
            x, y = west(x, y)
    return x, y


true_list = set()

for line in open("E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 24\\input.txt").readlines():

    tiles = (re.findall(r'ne|nw|se|sw|e|w', line.replace('\n', '')))
    # print(tiles)
    x_coord, y_coord = (walks_of_life(tiles))
    # flipped_tile.append((x_coord, y_coord))
    coordinate = (x_coord, y_coord)
    flipped_tile = coord_is_good(flipped_tile, coordinate)
true_list = set(flipped_tile)
for sad in range(0, 100):
    true_list = art_is_weird(true_list)
    # print("Current Loop is: %d" % (sad + 1))
    # print("Current list length is: %s" % len(flipped_tile))
print("The Answer to Part 1 is: %d" % len(flipped_tile))
print("The Answer tp Part 2 is: %d" % len(true_list))