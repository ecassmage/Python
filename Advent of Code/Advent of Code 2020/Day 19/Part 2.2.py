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
                search_reformat(section, cheveux)
            else:
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


def add_the_nums(w, eight_8, eleven_11):
    y = ''
    global tru_list
    for i, j in enumerate(w):
        if j.isdigit():
            if int(j) == 8:
                y += eight_8
            elif int(j) == 11:
                y += eleven_11
        else:
            y += j
    return y


tru_list, len_tru_list, fixed_list, tru_tru_list = [], [], [], []


def control_panel(w, x, y, z, long, short):
    for continuous in range(0, long - short):
        w2 = remove_nums(w)
        matches = []
        for i in x:
            matches.append(re.findall(r'\b(%s)\b' % w2, i))
        matches = [x for x in matches if x != []]
        for i in matches:
            tru_list.append(i)
        for i, k in enumerate(tru_list):
            for j, l in enumerate(tru_list[i]):
                tru_tru_list.append(''.join(tru_list[i][j]))
                for m, n in enumerate(tru_list[i][j]):

                    if tru_list[i][j][m] in x and tru_list[i][j][m] not in fixed_list:
                        fixed_list.append(tru_list[i][j][m])
        len_tru_list.append(len(fixed_list))
        w = add_the_nums(w, y, z)
        # print(w)
        k = 0
        try:
            for i, j in enumerate(reversed(len_tru_list)):
                if i == 0:
                    k = j
                    continue
                if j == k:
                    break
        except IndexError:
            print("bad")
            pass
    print('\n', len_tru_list, '\n', fixed_list, '\n', tru_tru_list)
    list_of_great = []
    print(len(tru_list))
    for i in tru_tru_list:
        for j in x:
            if re.findall(r'%s' % j, i):
                list_of_great.append(1)
                break
    print('hello2', list_of_great)
    print('hello', len(list_of_great))
    for i in list_of_great:
        pass


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
longest, shortest = 0, len(search_terms[0])
print(repr(rules))
# rules.update({'8': ['42 | 42 8']})
# rules.update({'11': ['42 31 | 42 11 31']})
for gg in search_terms:
    if len(gg) > longest:
        longest = len(gg)
    if len(gg) < shortest:
        shortest = len(gg)
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
# print('This is Oatmeal', oatmeal['0'])
search_compiled = []
# exit()
# missing_link = ''.join(search_reformat(oatmeal['0'], oatmeal['0']))
missing_link = ''.join(search_reformat(oatmeal['0'], oatmeal['0']))
# print(eight, eleven)
print(missing_link, '\n', search_terms, '\n', eight, '\n', eleven)
answer = control_panel(missing_link, search_terms, eight, eleven, longest, shortest)
exit()
# print(bad_nums)
# print(search_terms)
# print(rules)

