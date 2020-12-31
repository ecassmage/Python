input_folder = 'input.txt'

mountain = []
limits = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
column = 0
part_2 = 1

with open('%s' % input_folder, "r") as file:
    for line in file.readlines():
        mountain.append(list(line.replace('\n', '')))

for gen in range(0, len(limits)):
    crash = 0
    column = 0
    for row in range(0, len(mountain), limits[gen][1]):
        if mountain[row][column] == '#':
            crash += 1
        column += limits[gen][0]
        if column >= len(mountain[row]):
            column -= len(mountain[row])
    part_2 *= crash

print('The Answer to Part 2 is: %d' % part_2)

