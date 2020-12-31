import re
import copy
math = []
math_calculated = []
part_1 = 0


def multiplication(x):
    p = 1
    while True:
        if p >= len(x) - 1:
            break
        if x[p-1].isnumeric() and x[p] == '*' and x[p+1].isnumeric():
            x[p - 1] = str(eval(x[p - 1] + x[p] + x[p + 1]))
            x.pop(p + 1)
            x.pop(p)
        else:
            p += 1
    return x


def addition(x):
    p = 1
    while True:
        if p >= len(x) - 1:
            break
        if x[p - 1].isnumeric() and x[p] == '+' and x[p + 1].isnumeric():
            x[p - 1] = str(eval(x[p - 1] + x[p] + x[p + 1]))
            x.pop(p + 1)
            x.pop(p)
        else:
            p += 1
    return x


def brackets(x):
    l_bracket_count, r_bracket_count, current_bracket, l_bracket_positions, r_bracket_positions = 0, 0, 0, [], []
    for i in range(0, len(x)):
        if x[i] == '(':
            l_bracket_count += 1
            l_bracket_positions.insert(0, i)
        elif x[i] == ')':
            r_bracket_count += 1
            r_bracket_positions.append(i)
    for i in range(0, len(l_bracket_positions)):
        y = []
        while True:
            if math[l_bracket_positions[i] + 1] != ')':
                y.append(math[l_bracket_positions[i] + 1])
                x.pop(l_bracket_positions[i] + 1)
            else:
                break
        y = copy.copy(addition(y))
        y = copy.copy(multiplication(y))
        x.insert(l_bracket_positions[i] + 1, y[0])
        x.pop(l_bracket_positions[i] + 2)
        x.pop(l_bracket_positions[i])
    return x


part_2 = 0
for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 18\\input.txt'):
    math = re.findall(r'\d|\*|\+|\(|\)', line)
    if '(' in math:
        math = copy.copy(brackets(math))
    if '+' in math:
        math = copy.copy(addition(math))
    if '*' in math:
        math = copy.copy(multiplication(math))
    if '+' in math:
        math = copy.copy(addition(math))
    if '*' in math:
        math = copy.copy(multiplication(math))
    part_2 += int(math[0])
    print(math)
print("The Answer to Part 2 is: %d" % part_2)
