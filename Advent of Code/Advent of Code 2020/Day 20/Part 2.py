from copy import copy
from operator import itemgetter
camera_map = {}
edges = {}
shot = []
ID = ''
edging, four_corners, unedited = {}, {}, {}
MONSTER_PATTERN = (
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
)


def edge(x):
    north, east, south, west, y = [], [], [], [], {}
    [north.append(x[0][i_north]) for i_north in range(0, len(x[0]))]
    y.update({'north': north})
    [east.append(x[i_east][9]) for i_east in range(0, len(x))]
    y.update({'east': east})
    [south.append(x[9][i_south]) for i_south in range(0, len(x[9]))]
    y.update({'south': south})
    [west.append(x[i_west][0]) for i_west in range(0, len(x))]
    y.update({'west': west})
    return y


def p2_edge(matrix, side):
    if side == 'n':
        return matrix[0]
    if side == 's':
        return matrix[-1]
    if side == 'e':
        return ''.join(map(itemgetter(-1), matrix))
    # 'w'
    return ''.join(map(itemgetter(0), matrix))


def strip_edges(x):
    print('EXXXX', x)
    return [row[1:-1] for row in x[1:-1]]


def comparison(x):
    border_directions = {}
    for reference_id in x:
        borders_add = {}
        r_north, r_east, r_south, r_west = [], [], [], []
        north = x[reference_id]['north']
        east = x[reference_id]['east']
        south = x[reference_id]['south']
        west = x[reference_id]['west']
        for i in reversed(x[reference_id]['north']):
            r_north.append(i)
        for i in reversed(x[reference_id]['east']):
            r_east.append(i)
        for i in reversed(x[reference_id]['south']):
            r_south.append(i)
        for i in reversed(x[reference_id]['west']):
            r_west.append(i)
        # print(north, r_north)
        for compare_id in x:
            if reference_id == compare_id:
                continue
            for coordinate_reference_id in x[compare_id]:
                if north == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'north': compare_id})
                    border_directions.update({reference_id: {'north': compare_id}})

                if r_north == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'r_north': compare_id})
                    border_directions.update({reference_id: {'r_north': compare_id}})

                if east == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'east': compare_id})
                    border_directions.update({reference_id: {'east': compare_id}})

                if r_east == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'r_east': compare_id})
                    border_directions.update({reference_id: {'r_east': compare_id}})

                if south == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'south': compare_id})
                    border_directions.update({reference_id: {'south': compare_id}})

                if r_south == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'r_south': compare_id})
                    border_directions.update({reference_id: {'r_south': compare_id}})

                if west == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'west': compare_id})
                    border_directions.update({reference_id: {'west': compare_id}})

                if r_west == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'r_west': compare_id})
                    border_directions.update({reference_id: {'r_west': compare_id}})

                border_directions.update({reference_id: borders_add})
    return border_directions


def all_coordinates(x):
    answer = 1
    # print("X OF X: %s" % x)
    for i in x:
        if ('north' not in x[i] and 'r_north' not in x[i]) and ('west' not in x[i] and 'r_west' not in x[i]):
            print("Top Left %s" % i, x[i])
            four_corners.update({'north_west': i})
            answer *= int(i)
        if ('north' not in x[i] and 'r_north' not in x[i]) and ('east' not in x[i] and 'r_east' not in x[i]):
            print("Top Right %s" % i, x[i])
            four_corners.update({'north_east': i})
            answer *= int(i)
        if ('south' not in x[i] and 'r_south' not in x[i]) and ('west' not in x[i] and 'r_west' not in x[i]):
            print("Bottom Left: %s" % i, x[i])
            four_corners.update({'south_west': i})
            answer *= int(i)
        if ('south' not in x[i] and 'r_south' not in x[i]) and ('east' not in x[i] and 'r_east' not in x[i]):
            print("Bottom Right: %s" % i, x[i])
            four_corners.update({'south_east': i})
            answer *= int(i)
    return answer, four_corners


def rotate_90(tiles):
    new = []
    for c in range(len(tiles[0])):
        new_row = ''.join(row[c] for row in tiles)[::-1]
        new.append(new_row)
    return new


def orientate_tiles(x):
    yield x
    for _ in range(3):
        x = rotate_90(x)
        yield x


def arrangements(x):
    yield from orientate_tiles(x)
    yield from orientate_tiles(x[::-1])


def matching_tiles(w, x, y, z):
    prev_side = p2_edge(w, y)
    for x_id, x_ in x.items():
        if w is x_:
            continue
        for whittler in arrangements(x_):
            if prev_side == p2_edge(whittler, z):
                x.pop(x_id)
                return whittler


def made_in_china(x, y, z):
    yield x
    for _ in range(z - 1):
        tile = matching_tiles(x, y, 'e', 'w')
        x = tile
        yield x


def building_image(x, y, z):
    first = x
    image = []
    while True:
        image_row = made_in_china(first, y, z)
        print(image_row)
        image_row = map(strip_edges, image_row)
        image.extend(map(''.join, zip(*image_row)))
        print(image)
        if len(y) == 0:
            break
        first = matching_tiles(first, y, 's', 'n')
    return image


for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 20\\sample.txt').readlines():
    line = line.replace('\n', '')
    if line == '':
        continue
    if 'Tile' in line:
        if ID != '':
            camera_map.update({ID: shot})
            unedited.update({ID: shot})
            edging.update({ID: edge(shot)})
        line = line.replace('Tile ', '')
        line = line.replace(':', '')
        camera_map.update({line: ''})
        ID = line
        shot = []
    else:
        shot.append(list(line))
camera_map.update({ID: shot})
unedited.update({ID: shot})
edging.update({ID: edge(shot)})
unedited_new = {}
for i in unedited:
    unedited2 = []
    for j in range(0, len(unedited[i])):
        unedited2.append(''.join(unedited[i][j]))
    unedited_new.update({int(i): unedited2})

return_sequence = comparison(edging)
answer, matching_sides = all_coordinates(comparison(edging))
print("The Answer to Part 1 is: %d" % answer)
print(matching_sides)
matching_sides_top_left, top_left_ID = matching_sides.popitem()
print('what', top_left_ID, matching_sides_top_left)
print(repr(int(top_left_ID)))
top_left = unedited_new[int(top_left_ID)]
for j, i in enumerate(top_left):
    top_left[j] = ''.join(i)
print("What", unedited)
# exit()
if matching_sides_top_left in 'north_east':
    top_left = rotate_90(top_left)
elif matching_sides_top_left in 'north_west':
    top_left = rotate_90(rotate_90(top_left))
elif matching_sides_top_left in 'south_west':
    top_left = rotate_90(rotate_90(rotate_90(top_left)))
print("We Free", top_left)
image_dimension = int(len(unedited_new) ** 0.5)
print(unedited_new)
print(unedited_new[int(top_left_ID)])
# exit()
unedited_new.pop(int(top_left_ID))
print(top_left, unedited_new, image_dimension)

print(unedited_new)
# exit()
image = building_image(top_left, unedited_new, image_dimension)


print('image', image)
print('\n\n')
for tile in return_sequence:
    print('return all', tile, return_sequence[tile])
print('unedited', unedited)
print("Edge lord", edging)
print(four_corners)
