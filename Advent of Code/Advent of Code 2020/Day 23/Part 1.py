# from collections import deque
from copy import copy
cup = {}
cup_order_start = []


def cup_change_game(x):
    cup_current = 0
    z = len(x)
    for repetitions in range(0, 100):
        if cup_current >= z:
            cup_current = 0
        print(repetitions + 1, ": The Start of X", x)
        print("The current", cup_current)
        three_cups = []
        chosen_number = x[cup_current]

        for three_cups_conundrum in range(cup_current + 1, cup_current + 4):
            if three_cups_conundrum >= z:
                three_cups_conundrum -= z
            # print(three_cups)
            # print(x)
            # print("THree cuppies", cup_current)
            three_cups.append(x[three_cups_conundrum])
            x[three_cups_conundrum] = -1
            # print(three_cups)
            # print(x)
        true_prime = chosen_number
        true_prime_index = x.index(chosen_number)
        for i in reversed(x):
            if i == -1:
                x.pop(x.index(i))
        # print("This is x", x)
        cup_current += 1
        true_list = copy(x)
        print("The Three Cups: ", three_cups)
        while True:
            chosen_number -= 1
            if chosen_number <= 0:
                chosen_number += z
            if chosen_number in x:
                for i in reversed(three_cups):
                    x.insert(x.index(chosen_number) + 1, i)
                break

        while True:
            if true_prime_index != x.index(true_prime):
                x.append(x[0])
                x.pop(0)
            else:
                break
    return x


def cup_counting(x):
    y = ''
    while True:
        if x[0] == 1:
            x.pop(0)
            break
        else:
            x.append(x[0])
            x.pop(0)
    while True:
        if len(x) == 0:
            return y
        y += str(x[0])
        x.pop(0)


for line in open('input.txt').readlines():
    cup_order_start = [int(i) for i in list(line)]
returned = cup_counting(cup_change_game(increase(cup_order_start)))
print("The Answer to Part 1 is: %s" % returned)