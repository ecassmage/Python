import re
import copy
import itertools
constraints, constraint_word, your_ticket, nearby_ticket, valid_ticket, invalid_ticket = [], [], [], [], [], []
valid_rows, proper_order, used = [], [], []
your_ticket_truth, both_ticket_truth = False, False
invalid_ticket_count = 0
ticket_keys = {}

with open("E:\\Advent\\Day 16.txt", 'r') as Day16:
    for line in Day16.readlines():
        if line == '\n':
            continue
        line = line.replace('\n', '')
        if line == 'your ticket:':
            your_ticket_truth = True
            continue
        elif line == 'nearby tickets:':
            both_ticket_truth = True
            continue
        if your_ticket_truth is False:
            cuts = re.findall(r'(\d{1,4}-\d{1,4})', line)
            constraint_word.append(re.findall('([a-z]{3,26} [a-z]{3,26}|[a-z]{3,26})', line))
            for i in range(len(cuts)):
                constraints.append(cuts[i].split('-'))
                constraint_word.append(cuts[i].split('-'))
        elif your_ticket_truth is True and both_ticket_truth is False:
            your_ticket.append(re.findall(r'\d{1,4}', line))
        else:
            nearby_ticket.append(re.findall(r'\d{1,4}', line))

for current_ticket in range(0, len(nearby_ticket)):
    # currently_valid = True
    for current_number in range(0, len(nearby_ticket[current_ticket])):
        existence = False
        for constraint in range(0, len(constraints)):
            if int(constraints[constraint][1]) >= \
                int(nearby_ticket[current_ticket][current_number]) >= \
                    int(constraints[constraint][0]):
                # print("Hello: %s" % nearby_ticket[current_ticket][current_number])
                existence = True
                continue
        if existence is False:
            invalid_ticket.append(int(nearby_ticket[current_ticket][current_number]))
            # currently_valid = False
    # if currently_valid:
    #     valid_ticket.append(nearby_ticket[current_ticket])
for count in range(len(invalid_ticket)):
    invalid_ticket_count += invalid_ticket[count]
# print(constraint_word)
# print(invalid_ticket)
# print("The sum of invalid numbers are: %d" % invalid_ticket_count)
# print(constraints)
# print(your_ticket)
# print(nearby_ticket)
# print(len(constraints))
c, d, e, f, g = 0, 0, 0, 0, 0
for i in range(0, len(nearby_ticket)):
    good_bad_chart = []
    for j in range(0, len(nearby_ticket[i])):
        good_num = False
        for m in range(0, len(constraints)):
            if int(constraints[m][1]) >= \
                int(nearby_ticket[i][j]) >= \
                    int(constraints[m][0]):
                good_num = True
                break
        if good_num:
            good_bad_chart.append(1)
        else:
            good_bad_chart.append(0)
    if 0 not in good_bad_chart:
        valid_ticket.append(nearby_ticket[i])
# print(len(valid_ticket))
# print(len(valid_ticket[0]))
# print(valid_ticket)
row_index = []
valids = []
for current_column in range(0, len(valid_ticket[0])):
    f = 0
    valid_rows2 = []
    for constraint in range(0, len(constraints), 2):
        f += 1
        good_constraint = True
        e = 0
        for current_row in range(0, len(valid_ticket)):
            for cc in range(0, 2):
                # print("%s, %s" % (constraints[constraint + cc][0], constraints[constraint + cc][1]))
                if int(constraints[constraint + cc][1]) >= \
                        int(valid_ticket[current_row][current_column]) >= \
                        int(constraints[constraint + cc][0]):
                    good_constraint = True
                    e += 1
                    break
                else:
                    good_constraint = False
            if good_constraint is False:
                # print("FFF %d: %s Failed: %s, %s" % (g, valid_ticket[current_row][current_column], constraints[constraint], constraints[constraint + 1]))
                break
            else:
                # print("SSS %d: %s Success: %s, %s" % (g, valid_ticket[current_row][current_column], constraints[constraint], constraints[constraint + 1]))
                pass
        # print(e)
        if good_constraint:
            # print("Good E: %d" % e)
            # print("Constraint: %d" % f)
            c += 1
            valid_rows.append(constraints[constraint])
            valid_rows.append(constraints[constraint + 1])
            valid_rows2.append(constraints[constraint])
            valid_rows2.append(constraints[constraint + 1])
            if constraints[constraint + 1] == constraint_word[constraint_word.index(constraints[constraint]) + 1]:
                if re.findall(r'departure', str(constraint_word[constraint_word.index(constraints[constraint]) - 1])):
                    row_index.append(g)
            # constraints.pop(constraints.index(constraints[constraint + 1]))
            # constraints.pop(constraints.index(constraints[constraint]))
    valids.append(valid_rows2)

    # print("Bad Boy")
    d += 1
    # print("Constraints: %d" % f)
    g += 1
# print(d)
# print(c)
# print(constraints)
# print("\n\n\n\n")
# print(constraint_word)
# print(valid_rows)
# print("\n\n\n\n")
# print(proper_order)
# print(your_ticket)
Part_2_answer = 1
# for i in row_index:
#     Part_2_answer *= int(your_ticket[0][i])
# print("Hello rows: %s" % row_index)
# print("The Answer to Day 16 Part 1 is: %d" % invalid_ticket_count)
# print("The Answer to Day 16 Part 2 is: %d" % Part_2_answer)
# print(valid_rows)
# print(len(valid_rows))
# print(valids)
# print(len(valids))
formalized_list = []
# print(constraint_word)
for i in range(0, len(valids)):
    un_formalized_list = []
    for j in range(0, len(valids[i]), 2):
        if valids[i][j + 1] == constraint_word[constraint_word.index(valids[i][j]) + 1]:
            word1 = str(constraint_word[constraint_word.index(valids[i][j]) - 1]).replace("['", '')
            word1 = word1.replace("']", '')
            un_formalized_list.append(word1)
            # print(un_formalized_list)
    formalized_list.append(un_formalized_list)
while True:
    none = True
    for i in range(0, len(formalized_list)):
        if len(formalized_list[i]) == 1:
            ticket_keys.update({i: formalized_list[i][0]})
            used.append(formalized_list[i][0])
            none = False
    # print(ticket_keys)
    for i in range(0, len(formalized_list)):
        for j in range(0, len(formalized_list[i])):
            try:
                if formalized_list[i][j] in used:
                    formalized_list[i].pop((formalized_list[i].index(formalized_list[i][j])))
            except IndexError:
                break
    if none is True:
        break
#     else:
#         print(formalized_list)
#         print(ticket_keys)
#         print(used)
# print(ticket_keys)
# print(formalized_list)
# print("Hello:")
all_the_lists = itertools.product(*formalized_list)
c = 0
# print("Hello: %d" % len(list(all_the_lists)))
for i in all_the_lists:
    c += 1
    pass
Part_2_answer = 1
for i in ticket_keys:
    if re.findall(r'departure', ticket_keys[i]):
        Part_2_answer *= int(your_ticket[0][i])
# print(all_the_lists)
print("The Answer to Day 16 Part 1 is: %d" % invalid_ticket_count)
print("The Answer to Day 16 Part 2 is: %d" % Part_2_answer)