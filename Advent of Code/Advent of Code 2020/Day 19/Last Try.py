import re
rules, search_terms, search_compiled = {}, [], []
zero, eight, eleven = ['8', '11'], ['42', '|', '42', '8'], ['42', '31', '|', '42', '11', '31']
build_up = {'0': ['8', '11'], '8': ['42', '|', '42', '8'], '11': ['42', '31', '|', '42', '11', '31']}
recursion_level = {}


def remove_nums(x):
    y = ''
    global tru_list
    for i, j in enumerate(x):
        if j.isdigit():
            pass
        else:
            y += j
    return y


def search_reformat(cheveux, cheveux_real):
    global search_compiled
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


def search_make_2(fromage, carry_on):
    for num, make_it_up in enumerate(carry_on):
        if isinstance(make_it_up, list):
            search_make_2(fromage, make_it_up)
        elif isinstance(make_it_up, int):
            carry_on[num] = fromage[make_it_up]
    return carry_on


def search_make(fromage):
    while True:
        bad_go = True
        for stat in fromage:
            cheese = fromage[stat]
            # print('cheese', cheese)
            for num, make_up in enumerate(cheese):
                # print(repr(make_up))
                if isinstance(make_up, list):
                    search_make_2(fromage, make_up)
                elif make_up.isdigit():
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


def building_search(x, y, z):
    for number, string in enumerate(x):
        if type(string) is list:
            building_search(string, y, z)
        elif type(string) is str:
            if string.isdigit():
                if int(string) == 8:
                    new_list.append(y)
                elif int(string) == 11:
                    new_list.append(z)
                else:
                    new_list.append(string)
            else:
                new_list.append(string)
    return new_list


def finish_product(x, y, z):
    for number, string in enumerate(x):
        if string.isdigit():
            if int(string) == 31:
                finished_product.append(y)
            elif int(string) == 42:
                finished_product.append(z)
        else:
            finished_product.append(string)
    return finished_product


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
oatmeal = search_make(rules)
recursion_level = {0: ['8', '11']}
print(repr(recursion_level))
thirty_one = ''.join(search_reformat(oatmeal['31'], oatmeal['31']))
forty_two = ''.join(search_reformat(oatmeal['42'], oatmeal['42']))
print('help', thirty_one)
print('me', forty_two)
for i in range(1, 15):
    new_list = []
    recursion_level.update({i: building_search(recursion_level[i - 1], eight, eleven)})
print(repr(recursion_level))
    # recursion_level.update({i: building_search(zero, eight, eleven)})
compiled = []
for i in recursion_level:
    search_compiled = []
    compiled.append(search_reformat(recursion_level[i], recursion_level[i]))
eight_compiled, eleven_compiled = '', ''
for i in eight:
    if i.isdigit():
        if int(i) == 31:
            eight_compiled += thirty_one
        elif int(i) == 42:
            eight_compiled += forty_two
    else:
        eight_compiled += i
for i in eleven:
    if i.isdigit():
        if int(i) == 31:
            eleven_compiled += thirty_one
        elif int(i) == 42:
            eleven_compiled += forty_two
    else:
        eight_compiled += i
matches = []
for j in search_terms:
    matches.append(re.findall(r'\b%s\b' % (eight_compiled + eleven_compiled), j))
print("These are mnatches", matches)
for i in compiled:
    finished_product = []
    built = ''.join(finish_product(i, thirty_one, forty_two))
    print('\n', built)
    for j in search_terms:
        matches.append(re.findall(r'\b%s\b' % built, j))
    matches = [x for x in matches if x != []]
    print('\n\n\n', matches, '\n', len(matches))
print('\n\n\n\n\n\n')
print(eight_compiled)
print(eleven_compiled)
print('\n\n\n\n\n\n')
print(compiled)

print(oatmeal)
print(oatmeal['31'])
print(oatmeal['42'])