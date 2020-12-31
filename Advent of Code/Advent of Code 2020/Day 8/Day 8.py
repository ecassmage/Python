import copy
commands = []
commands_basic = []
accumulator = 0
position = 0
look = 'nop'
change = 'jmp'
with open("E:\\Advent\\Day 8.txt", 'r') as Day8:
    Day8.readline()
    for i in Day8:
        i = i.split(' ')
        i[1] = i[1].replace('\n', '')
        commands.append(i[0])
        commands.append(i[1])
    print(commands)
    commands_basic = copy.deepcopy(commands)
c = 0
while True:
    commands = copy.deepcopy(commands_basic)
    while True:
        commands = copy.deepcopy(commands_basic)
        try:
            if commands[c] == look:
                commands[c] = change
                c = c + 1
                # if c < 10:
                #     print(commands)
                break
            c = c + 1
        except IndexError:
            look = 'jmp'
            change = 'nop'
            # print('Failure')
            c = 0
            accumulator = 0
    accumulator = 0
    position = 0
    while True:
        try:
            # print(commands[position])
            if commands[position] == 'nop':
                commands[position] = 'Used'
                position = position + 2
                continue
            elif commands[position] == 'acc':
                commands[position] = 'Used'
                accumulator = accumulator + int(commands[position + 1])
                position = position + 2
            elif commands[position] == 'jmp':
                commands[position] = 'Used'
                position = position + (2 * (int(commands[position + 1])))
            elif commands[position] == 'Used':
                # print("Bad Go")
                # print('list')
                # print("Finally: %s" % accumulator)
                break
            else:
                position = position + 2
            if position > len(commands):
                # print('Success')
                print(accumulator)
                exit()
        except IndexError:
            if position >= len(commands):
                # print('Success')
                print(accumulator)
                exit()
