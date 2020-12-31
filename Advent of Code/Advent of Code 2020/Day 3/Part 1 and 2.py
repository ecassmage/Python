import copy
input_folder = 'input.txt'

mountain = []
limits = [[3, 1], [1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
column = 0
part_1 = 0
part_2 = 1

with open('%s' % input_folder, "r") as file:
    for line in file.readlines():
        mountain.append(list(line.replace('\n', '')))
saved_mountain = copy.deepcopy(mountain)

for gen in range(0, len(limits)):
    crash = 0
    column = 0
    mountain = copy.deepcopy(saved_mountain)
    for row in range(0, len(mountain), limits[gen][1]):
        if mountain[row][column] == '.':
            mountain[row][column] = 'O'
            mountain[row][column] = '.'
        elif mountain[row][column] == '#':
            crash += 1
            mountain[row][column] = 'X'
            mountain[row][column] = '#'
        column += limits[gen][0]
        if column >= len(mountain[row]):
            column -= len(mountain[row])
        # print(column, len(mountain[column]))
        # print(mountain[row])
    if gen == 0:
        part_1 = crash
        continue
    part_2 *= crash

print('The Answer to Part 1 is: %d' % part_1)
print('The Answer to Part 2 is: %d' % part_2)