player1, player2 = [], []
play_2 = False


def recursive(x, y):
    print("next Game")
    while True:

        x_first, y_first = x[0], y[0]
        x.pop(0), y.pop(0)
        print(x, x_first, y, y_first)
        if len(x) >= x_first and len(y) >= y_first:
            print("Let us Start a new game")
            # print(x, y, x_first, y_first)
            recurse_x, recurse_y = [], []
            for i in range(0, x_first):
                recurse_x.append(x[i])
            for i in range(0, y_first):
                recurse_y.append(y[i])
            feet = recursive(recurse_x, recurse_y)
            try:
                if feet == 1:
                    y.append(y_first), y.append(x_first)
                elif feet == 0:
                    x.append(x_first), x.append(y_first)
                continue
            except UnboundLocalError:
                pass
        if x_first > y_first:
            x.append(x_first), x.append(y_first)
        else:
            y.append(y_first), y.append(x_first)

        if len(x) <= 0:
            print("Well That was Fun")
            return 1
        if len(y) <= 0:
            print("Well That was Fun")
            return 0
        # print("%s \n %s" % (x, y))


def card_turn(x, y):
    x_first, y_first = x[0], y[0]
    x.pop(0), y.pop(0)
    print(x, x_first, y, y_first)
    if len(x) >= x_first and len(y) >= y_first:
        print("Let us Start a new game")
        recurse_x, recurse_y = [], []
        for i in range(0, x_first):
            recurse_x.append(x[i])
        for i in range(0, y_first):
            recurse_y.append(y[i])
        print(recurse_x, recurse_y)
        # print(x, x_first, y, y_first)
        feet = recursive(recurse_x, recurse_y)
        # print(x, x_first, y, y_first)
        if feet == 1:
            y.append(y_first), y.append(x_first)
        elif feet == 0:
            x.append(x_first), x.append(y_first)
        return x, y
        # print(x, x_first, y, y_first)
    if x_first > y_first:
        x.append(x_first), x.append(y_first)
    else:
        y.append(y_first), y.append(x_first)
    # print("%s \n %s" % (x, y))
    return x, y


def part_1(x):
    y = 0
    z = len(x)
    for i in x:
        y += i * z
        z -= 1
    return y


for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 22\\sample.txt').readlines():
    if line == '\n' or line == 'Player 1:\n':
        continue
    line = line.replace('\n', '')
    if line == 'Player 2:':
        play_2 = True
        continue
    if play_2:
        player2.append(int(line))
    else:
        player1.append(int(line))

#     print(line)
# print(player1, player2)
c = 0
while True:
    player1, player2 = card_turn(player1, player2)
    if len(player1) < 1 or len(player2) < 1:
        break
    c += 1
    if c > 30:
        break
if len(player1) < 1:
    answer = part_1(player2)
else:
    answer = part_1(player1)
print('The Answer to Part 1 is: %d' % answer)
print("%d:\n%s\n%s" % (c, player1, player2))