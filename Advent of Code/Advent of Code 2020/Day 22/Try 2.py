player1, player2 = [], []
current, limbo = [], []
play_2 = False
base_game = [0, 0, [], []]
played_sets = {1: [], 2: []}


def recursive(x, y):
    # print(repr(x))
    global current
    # print('This is killing me', repr(x), repr(y))
    x_first, y_first = x[0], y[0]
    limbo[-2], limbo[-1] = x[0], y[0]
    x.pop(0), y.pop(0)
    # print(x, x_first, y, y_first)
    # base_game[0], base_game[1], base_game[2], base_game[3] = x_first, y_first, x, y
    if len(x) >= x_first and len(y) >= y_first:
        # print("Let us Start a new game")
        recurse_x, recurse_y = [], []
        for i in range(0, x_first):
            recurse_x.append(x[i])
        for i in range(0, y_first):
            recurse_y.append(y[i])
        # print(recurse_x, recurse_y)
        # print(x, x_first, y, y_first)
        # current.append(recurse_x[0]), current.append((recurse_y[0]))
        # recurse_x.pop(0), recurse_y.pop(0)
        current.append(recurse_x), current.append(recurse_y)
        # print(current)
        limbo.append(recurse_x[0]), limbo.append(recurse_y[0])
        feet, current = true_recursion(current)
        # print('Hellllllllo')
        # print("Recursion done")
        # print(current)
        # [current.pop(-1) for num in range(0, 4)]
        # print("This is Base: %s" % base_game)
        # x_first, y_first, x, y = current[-4], current[-3], current[-2], current[-1]
        # print("x: %s (%s)\ny: %s (%s)" % (x, x_first, y, y_first))
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


def true_recursion(packed_list):
    global played_sets
    played_sets = {1: set(), 2: set()}
    while True:
        # print("List of packs", packed_list)
        player_1, player_2 = packed_list[-2], packed_list[-1]
        while True:
            if player_1 not in played_sets[1] and player_2 not in played_sets[2]:
                played_sets[1].add(player_1)
                played_sets[2].add(player_2)
            else:
                return 1
            print('Jello', packed_list, limbo)
            # print("We got numbers all right", repr(player_1), player_2)
            player_1, player_2 = recursive(player_1, player_2)
            # print("We got numbers all right", player_1, len(player_1), player_2, len(player_2))
            if len(player_1) != 0 and len(player_2) != 0:
                if len(player_1) <= 0:
                    pass
                elif len(player_2) <= 0:
                    pass
            else:
                break
        print("WE Got limbo: %s" % limbo)
        x_send, y_send = limbo[-2], limbo[-1]
        print('Jello', packed_list, limbo)
        [(limbo.pop(-1), packed_list.pop(-1)) for i in range(0, 2)]
        if len(player_1) <= 0:
            player_2.append(y_send), player_2.append(x_send)
        else:
            player_2.append(x_send), player_2.append(y_send)
        print('Jello', packed_list, limbo)

        if len(packed_list) == 0:
            # print("HELLLO", len(player_1), len(player_2))
            if len(player_1) == 0:
                print('high')
                return 1
            elif len(player_2) == 0:
                print('bye')
                return 0


# def recursive():
#     global current
#     print("next Game")
#     print(current)
#     # x, y, x_first, y_first = current[-2], current[-1], current[-4], current[-3]
#     x, y = current[-2], current[-1]
#     print("This is x: %s\nThis is y: %s" % (x, y))
#     while True:
#         print("We Good")
#         print("THE X: %s\nTHE Y: %s" % (x, y))
#         x_first, y_first = x[0], y[0]
#         print("WHY IS NOthing: %s, %s" % (x_first, y_first))
#         print("We Goodier")
#         x.pop(0), y.pop(0)
#         print(x, x_first, y, y_first)
#         if len(x) >= x_first and len(y) >= y_first:
#             print("Let us Start a new game recursive")
#             # print(x, y, x_first, y_first)
#             recurse_x, recurse_y = [], []
#             for i in range(0, x_first):
#                 recurse_x.append(x[i])
#             for i in range(0, y_first):
#                 recurse_y.append(y[i])
#             # current.append(x_first), current.append(y_first), current.append(x), current.append(y)
#             current[-4], current[-3], current[-2], current[-1] = x_first, y_first, x, y
#             # print(current)
#             current.append(recurse_x[0]), current.append(recurse_y[0])
#             current.append(recurse_x), current.append(recurse_y)
#             feet = recursive()
#             # print("The current chapter of life: %s" % current)
#             # print("x: %s (%s)\ny: %s (%s)" % (x, x_first, y, y_first))
#             # for i in range(0, 4):
#             #     current.pop(-1)
#             # print(current)
#             # print("x: %s (%s)\ny: %s (%s)" % (current[-2], current[-4], current[-1], current[-3]))
#             x_first, y_first, x, y = current[-4], current[-3], current[-2], current[-1]
#             # print("THIS IS CURRENT: %s" % current)
#             # try:
#             if feet == 1:
#                 y.append(y_first), y.append(x_first)
#             elif feet == 0:
#                 x.append(x_first), x.append(y_first)
#             continue
#             # except UnboundLocalError:
#             #     pass
#         if x_first > y_first:
#             x.append(x_first), x.append(y_first)
#         else:
#             y.append(y_first), y.append(x_first)
#         print("2\nTHE X: %s\nTHE Y: %s" % (x, y))
#         if len(x) <= 0:
#             print("Well That was Fun")
#             for i in range(0, 4):
#                 current.pop(-1)
#             return 1
#         elif len(y) <= 0:
#             print("Well That was Fun")
#             for i in range(0, 4):
#                 current.pop(-1)
#             return 0
#         # print("%s \n %s" % (x, y))
#         # print(current)
#         # print("x: %s (%s)\ny: %s (%s)" % (current[-2], current[-4], current[-1], current[-3]))
#
#
def card_turn(x, y):
    global current
    x_first, y_first = x[0], y[0]
    x.pop(0), y.pop(0)
    print(x, x_first, y, y_first)
    base_game[0], base_game[1], base_game[2], base_game[3] = x_first, y_first, x, y
    # if len(x) >= x_first and len(y) >= y_first:
    #     print("Let us Start a new game")
    #     recurse_x, recurse_y = [], []
    #     for i in range(0, x_first):
    #         recurse_x.append(x[i])
    #     for i in range(0, y_first):
    #         recurse_y.append(y[i])
    #     print(recurse_x, recurse_y)
    #     # print(x, x_first, y, y_first)
    #     # current.append(recurse_x[0]), current.append((recurse_y[0]))
    #     # recurse_x.pop(0), recurse_y.pop(0)
    #     limbo.append(recurse_x[0]), limbo.append(recurse_y[0])
    #     current.append(recurse_x), current.append(recurse_y)
    #     print(current)
    #     feet = true_recursion(current)
    #     print("Recursion done")
    #     # [current.pop(-1) for num in range(0, 4)]
    #     print("This is Base: %s" % base_game)
    #     x_first, y_first, x, y = base_game[0], base_game[1], base_game[2], base_game[3]
    #     print("x: %s (%s)\ny: %s (%s)" % (x, x_first, y, y_first))
    #     if feet == 1:
    #         y.append(y_first), y.append(x_first)
    #     elif feet == 0:
    #         x.append(x_first), x.append(y_first)
    #     return x, y
    #     # print(x, x_first, y, y_first)
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


for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 22\\input.txt').readlines():
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
c = 1
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
print("%d:%s, %s" % (c, player1, player2))