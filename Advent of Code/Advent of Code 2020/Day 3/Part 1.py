input_folder = 'input.txt'
mountain = []
column, part_1 = 0, 0

with open('%s' % input_folder, "r") as file:
    for line in file.readlines():
        mountain.append(list(line.replace('\n', '')))

for row in range(0, len(mountain)):
    if mountain[row][column] == '#':
        part_1 += 1
    column += 3
    if column >= len(mountain[row]):
        column -= len(mountain[row])

print('The Answer to Part 1 is: %d' % part_1)
