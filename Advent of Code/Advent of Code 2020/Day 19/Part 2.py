import re
from copy import deepcopy
import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(1000)
rules, search_terms, search_compiled, len_matches, already_done = {}, [], [], [], []


def loop_nums(loops):
    bad_list = []
    for stat in loops:
        for make_up in loops[stat]:
            if make_up.isnumeric():
                if make_up == stat:
                    bad_list.append(make_up)
    return bad_list


def search_make_2(fromage, carry_on, bad_fromage):
    for num, make_it_up in enumerate(carry_on):
        if isinstance(make_it_up, list):
            search_make_2(fromage, make_it_up, bad_fromage)
        elif isinstance(make_it_up, int):
            if make_it_up not in bad_fromage:
                carry_on[num] = fromage[make_it_up]
    return carry_on


def search_make(fromage, bad_fromage):
    while True:
        bad_go = True
        for stat in fromage:
            cheese = fromage[stat]
            # print('cheese', cheese)
            for num, make_up in enumerate(cheese):
                # print(repr(make_up))
                if isinstance(make_up, list):
                    search_make_2(fromage, make_up, bad_fromage)
                elif make_up.isdigit():
                    if make_up not in bad_fromage:
                        # print('Hello', make_up)
                        cheese[num] = fromage[make_up]
                        bad_go = False
                    # else:
                    #     if stat == make_up:
                    #         cheese.pop(num)
            fromage.update({stat: cheese})
        if bad_go:
            break
    return fromage


def add_missing(mapping, control):
    # global already_done
    # print(control)
    # copied = deepcopy(control)
    for num, spot in enumerate(control):
        # print(num, spot)
        # print(repr(spot))
        if isinstance(spot, list):
            add_missing(mapping, spot)
        elif spot in already_done:
            continue
        elif spot.isdigit():
            control[num] = mapping[spot]
            already_done.append(spot)
        else:
            continue
    # print(already_done)
    return control


def search_reformat(cheveux, cheveux_real):

    global bad_nums, search_compiled
    search_compiled.append('(')
    try:
        for section in cheveux:
            if isinstance(section, list):
                # print("Fuck All cunts including you")
                search_reformat(section, cheveux)
            # elif section in bad_nums:
            #     # print("Fuck All cunts including you")
            #     continue
            else:
                # print(search_compiled)
                search_compiled.append(section)
    except RecursionError:
        print("Weird", cheveux_real)
        print("Recursion Broke it")
        exit()
    search_compiled.append(')')
    # print(search_compiled)
    return search_compiled


def remove_nums(x):
    y = ''
    global tru_list
    for i, j in enumerate(x):
        if j.isdigit():
            pass
        else:
            y += j
    return y


def control_panel(control_1, control_2, control_3, control_4):
    while True:
        matches = []
        new_control_1 = ''
        # print(control_1)
        better_control = remove_nums(control_1)
        # print(control_2)
        # print(control_3)
        # print(control_4)
        for i in control_2:
            matches.append(re.findall(r'\b%s\b' % better_control, i))
        matches = [x for x in matches if x != []]
        # print(matches)
        for i in matches:
            if i not in tru_list:
                tru_list.append(i)
        if len(tru_list) not in len_tru_list:
            len_tru_list.append(len(tru_list))
        else:
            return len_tru_list
        for i, j in enumerate(control_1):
            # print(control_1[i])
            if j.isdigit():
                if int(j) == 8:
                    new_control_1 += control_3
                elif int(j) == 11:
                    new_control_1 += control_4
            else:
                new_control_1 += j
        control_1 = deepcopy(new_control_1)
        print(len_tru_list)


tru_list, len_tru_list = [], []
for line in open('sample.txt').readlines():
    line = line.replace('\n', '')
    line = line.replace('"', '')
    terms = []
    if re.findall(r'\d', line):
        term = re.findall(r'(\d{1,5}):', line)
        if term[0] == '0':
            zero_terms = line.replace('%s: ' % term[0], '').split(' ')
        terms = line.replace('%s: ' % term[0], '').split(' ')
        rules.update({term[0]: terms})
    elif line == '':
        continue
    else:
        search_terms.append(line)
bad_nums = loop_nums(rules)
# print(rules)
oatmeal = search_make(rules, bad_nums)
# print("Oatmeal", oatmeal)
# exit()
# print('This is Oatmeal', oatmeal)
eight = ''.join(search_reformat(oatmeal['8'], oatmeal['8']))
search_compiled = []
eleven = ''.join(search_reformat(oatmeal['11'], oatmeal['11']))
missing_link = add_missing(oatmeal, oatmeal['0'])
print('This is Oatmeal', oatmeal['0'])
search_compiled = []
# exit()
# missing_link = ''.join(search_reformat(oatmeal['0'], oatmeal['0']))
missing_link = ''.join(search_reformat(oatmeal['0'], oatmeal['0']))
# print(eight, eleven)
print(missing_link, '\n', search_terms, '\n', eight, '\n', eleven)

# exit()
answers = control_panel(missing_link, search_terms, eight, eleven)
print("The Answers are:", answers)
print("The Answer is:", answers[-1])
# print(bad_nums)
# print(search_terms)
# print(rules)

