camera_map = {}
edges = {}
shot = []
ID = ''
edging, four_corners = {}, {}


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
    # print('  '.join(north) + '   ' + '  '.join(x[0]))
    # for i in range(1, len(east) - 1):
    #     print('%s%27s' % (west[i], east[i]) + '   ' + '  '.join(x[i]))
    # print('  '.join(south) + '   ' + '  '.join(x[-1]) + '\n')
    return y


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
        for compare_id in x:
            if reference_id == compare_id:
                continue
            for coordinate_reference_id in x[compare_id]:
                if north == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'north': compare_id})
                    # print("This is the north: %s, %s, %s, %s: %s" % (reference_id, north, compare_id,
                    #                                                  coordinate_reference_id,
                    #                                                  x[compare_id][coordinate_reference_id]))
                if r_north == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'r_north': compare_id})
                    border_directions.update({reference_id: {'r_north': compare_id}})
                    # print("This is the north: %s, %s, %s, %s: %s" % (reference_id, north, compare_id,
                    #                                                  coordinate_reference_id,
                    #                                                  x[compare_id][coordinate_reference_id]))
                if east == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'east': compare_id})
                    border_directions.update({reference_id: {'east': compare_id}})
                    # print("This is the east: %s, %s, %s, %s: %s" % (reference_id, north, compare_id,
                    #                                                 coordinate_reference_id,
                    #                                                 x[compare_id][coordinate_reference_id]))
                if r_east == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'r_east': compare_id})
                    border_directions.update({reference_id: {'r_east': compare_id}})
                    # print("This is the east: %s, %s, %s, %s: %s" % (reference_id, north, compare_id,
                    #                                                 coordinate_reference_id,
                    #                                                 x[compare_id][coordinate_reference_id]))
                if south == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'south': compare_id})
                    border_directions.update({reference_id: {'south': compare_id}})
                    # print("This is the south: %s, %s, %s, %s: %s" % (reference_id, north, compare_id,
                    #                                                  coordinate_reference_id,
                    #                                                  x[compare_id][coordinate_reference_id]))
                if r_south == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'r_south': compare_id})
                    border_directions.update({reference_id: {'r_south': compare_id}})
                    # print("This is the south: %s, %s, %s, %s: %s" % (reference_id, north, compare_id,
                    #                                                  coordinate_reference_id,
                    #                                                  x[compare_id][coordinate_reference_id]))
                if west == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'west': compare_id})
                    border_directions.update({reference_id: {'west': compare_id}})
                    # print("This is the west: %s, %s, %s, %s: %s" % (reference_id, north, compare_id,
                    #                                                  coordinate_reference_id,
                    #                                                  x[compare_id][coordinate_reference_id]))
                if r_west == x[compare_id][coordinate_reference_id]:
                    borders_add.update({'r_west': compare_id})
                    border_directions.update({reference_id: {'r_west': compare_id}})
                    # print("This is the west: %s, %s, %s, %s: %s" % (reference_id, north, compare_id,
                    #                                                 coordinate_reference_id,
                    #                                                 x[compare_id][coordinate_reference_id]))
                border_directions.update({reference_id: borders_add})
        # print('This is it the Final Night')
    return border_directions


def all_coordinates(x):
    answer = 1
    print("X OF X: %s" % x)
    for i in x:
        if 'north' not in x[i] and 'r_north' not in x[i] and 'west' not in x[i] and 'r_west' not in x[i]:
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
    return answer


for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 20\\sample.txt').readlines():
    line = line.replace('\n', '')
    if line == '':
        continue
    if 'Tile' in line:
        if ID != '':
            camera_map.update({ID: shot})
            edging.update({ID: edge(shot)})
        line = line.replace('Tile ', '')
        line = line.replace(':', '')
        camera_map.update({line: ''})
        ID = line
        shot = []
    else:
        shot.append(list(line))
camera_map.update({ID: shot})
edging.update({ID: edge(shot)})
print("The Answer to Part 1 is: %d" % all_coordinates(comparison(edging)))
print(edging)
print(four_corners)
