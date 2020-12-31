import re
math = []
math_calculated = []
part_1 = 0
for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 18\\input.txt'):
    # print(eval(line.replace('\n', '')))
    math = re.findall(r'\d|\*|\+|\(|\)', line)
    # print(math)
    l_bracket_count, r_bracket_count, current_bracket, l_bracket_positions, r_bracket_positions = 0, 0, 0, [], []
    for i in range(0, len(math)):
        if math[i] == '(':
            l_bracket_count += 1
            l_bracket_positions.insert(0, i)
        elif math[i] == ')':
            r_bracket_count += 1
            r_bracket_positions.append(i)
    print("Bracket count: %d, %s, %s\n%s" % (l_bracket_count, l_bracket_positions, r_bracket_positions, math))
    for i in range(0, len(l_bracket_positions)):
        while True:
            # print(math[l_bracket_positions[i] + 2], math[l_bracket_positions[i] + 3])
            if math[l_bracket_positions[i] + 2] != ')' and math[l_bracket_positions[i] + 3] != ')':
                math[l_bracket_positions[i] + 1] = \
                    str(eval(math[l_bracket_positions[i] + 1] + math[l_bracket_positions[i] + 2] +
                             math[l_bracket_positions[i] + 3]))
                math.pop(l_bracket_positions[i] + 3)
                math.pop(l_bracket_positions[i] + 2)
                print(math)
            else:
                math.pop(l_bracket_positions[i] + 2)
                math.pop(l_bracket_positions[i])
                print("Break it: %s" % math)
                break
    while True:
        if len(math) >= 3:
            math[0] = str(eval(math[0] + math[1] + math[2]))
            math.pop(2)
            math.pop(1)
        else:
            print(math)
            part_1 += int(math[0])
            break
print("The Answer to Part 1 is: %d" % part_1)



    # for i in range(0, len(math)):
    #     if current_bracket == bracket_count
