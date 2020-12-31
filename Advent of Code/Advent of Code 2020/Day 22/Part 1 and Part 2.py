import copy
crepe_holder, player1, player2, play_2 = [], [], [], False


def play_cards(player_1, player_2, z):
    played_sets = {1: set(), 2: set()}
    while len(player_1) != 0 and len(player_2) != 0:
        if z == 1:
            if tuple(player_1) in played_sets[1] and tuple(player_2) in played_sets[2]:
                return 1, player_1
            else:
                played_sets[1].add(tuple(player_1))
                played_sets[2].add(tuple(player_2))
        x_first, y_first = player_1[0], player_2[0]
        player_1.pop(0), player_2.pop(0)
        if z == 1:
            if len(player_1) >= x_first and len(player_2) >= y_first:
                player_1_recurse, player_2_recurse = [], []
                [player_1_recurse.append(player_1[i]) for i in range(0, x_first)]
                [player_2_recurse.append(player_2[i]) for i in range(0, y_first)]
                winner, hand_won = play_cards(player_1_recurse, player_2_recurse, 1)
                if winner == 1:
                    player_1.append(x_first), player_1.append(y_first)
                else:
                    player_2.append(y_first), player_2.append(x_first)
                continue
        if x_first > y_first:
            player_1.append(x_first), player_1.append(y_first)
        else:
            player_2.append(y_first), player_2.append(x_first)
    if z == 0:
        if len(player_1) == 0:
            return 'Player 2', calculator(player_2)
        else:
            return 'Player 1', calculator(player_1)
    else:
        if len(player_1) == 0:
            return 2, player_2
        else:
            return 1, player_1


def calculator(x):
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
crepe_holder.append(copy.copy(player1))
crepe_holder.append(copy.copy(player2))
part_2 = []
part_1 = play_cards(player1, player2, 0)
print("%s Won Part 1\nThe Answer to Part 1 is: %d" % part_1)
player1, player2 = copy.copy(crepe_holder[0]), copy.copy(crepe_holder[1])
inter = play_cards(player1, player2, 1)
part_2.append(inter[0])
part_2.append(calculator(inter[1]))
print("Player %s Won Part 2\nThe Answer to Part 2 is: %d" % (part_2[0], part_2[1]))