import re
import copy
rules, search_terms = {}, []
starting_terms = {}
zero_term = []
sections = []


# def recursion(x):
#     for m in rules:
#         for n in range(0, len(rules[m])):
#             x.update({x[m]: 'hello'})
#     print(x)
#     return
#
#     pass
c = 0

term_good = []
all_possibilities = []


def defeck(x):
    term_good.append('(')
    for section in x:
        if isinstance(section, list):
            defeck(section)
        else:
            term_good.append(section)
    term_good.append(')')
    return term_good


def parsing(x):
    global long_boi, c
    c = 0
    # print(x)
    try:
        c += 1
        for loop in x:

            if c > 500:
                return long_boi
            if len(loop) == 1:
                long_boi += j
                # print(long_boi)
            else:
                parsing(x)

    except RecursionError:
        return long_boi

    return long_boi


def group_parsing(x):
    y, z = [], []
    for i in x:
        if i == '/':
            z.append(y)
            y = []
        else:
            y.append(i)
    return z


def final_thoughts(x):
    y = 0
    right_side = False
    for i in x:
        if i[0] != '|':
            if right_side:
                y -= 1
                right_side = False
            else:
                y += 1
        else:
            if y == 0:
                right_side = True
            continue


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
    # print(line)
# print(rules)
for i in rules:
    # print(repr(i))
    for j in range(0, len(rules[i])):
        # print(repr(rules[i][j]))
        if re.findall(r'a|b', rules[i][j]):
            starting_terms.update({i: rules[i][j]})
# recursion(rules)
for i in rules:
    fiddle = rules[i]
    # print(len(fiddle))
    if len(fiddle) == 1 and fiddle[0].isnumeric():
        # print(fiddle)
        rules.update({i: rules[fiddle[0]]})
# print("Filament", rules)
for i in rules:
    fiddle = rules[i]
    if '|' not in fiddle and fiddle[0].isnumeric():
        # print(fiddle)
        for j in range(0, len(fiddle)):
            fiddle[j] = rules[fiddle[j]]
            rules.update({i: fiddle})
        # print(rules)
# print("2", rules)
for starts in starting_terms:
    # print(repr(starts))
    for i in rules:
        fiddle = rules[i]
        for j in range(0, len(fiddle)):
            if fiddle[j] == '%s' % starts:
                fiddle[j] = starting_terms[starts]
                rules.update({i: fiddle})
                # print(rules)
# print('3', rules)
for i in rules:
    fickle = rules[i]
    # print(fickle)
    for j in range(0, len(fickle)):
        # print(repr(fickle[j]))
        try:
            if fickle[j].isnumeric():
                fickle[j] = rules[fickle[j]]
        except AttributeError:
            pass
# print('4', rules)
# for i in rules:
#     print('hello')
#     fickle = rules[i]
#     # print(fickle)
#     for j in range(0, len(fickle)):
#         print(repr(fickle[j]))
#         try:
#             if fickle[j].isnumeric():
#                 print('hello', fickle[j], i)
#                 if fickle[j] == i:
#                     print(fickle[j])
#                     del fickle[j]
#         except AttributeError:
#             pass
# print('5', rules)
# exit()
long_boi = ''
print(rules['42'])
# print("HELLO BOIsss", defeck(rules['0']))
c = 1
hello = defeck(rules['0'])
# hello.insert(0, '\b')
# hello.append('\b')
# print("HELLO BOIsss", hello)
the_search = ''.join(hello)
print(the_search)
# print(repr(the_search))
# print(repr(search_terms))
matches = []
# print("hello is here", the_search)
print(''.join(defeck(rules['42'])))
print(''.join(defeck(rules['31'])))
for i in search_terms:
    # print(i)
    matches.append(re.findall(r'\b(%s)\b' % the_search, i))
matches = [x for x in matches if x != []]
# print('matches', matches)
term_good = []
temp_list_1000 = defeck([[[[['b'], [['a'], [['b'], ['b'], '|', ['a'], ['b']], '|', ['b'], [[['a'], '|', ['b']], [['a'], '|', ['b']]]], '|', ['a'], [['b'], [['b'], ['b']], '|', ['a'], [['b'], ['b'], '|', ['a'], [['a'], '|', ['b']]]]], ['b'], '|', [[[['a'], ['a'], '|', ['a'], ['b']], ['a'], '|', [['b'], ['b']], ['b']], ['b'], '|', [[[['a'], '|', ['b']], ['a'], '|', ['b'], ['b']], ['a']], ['a']], ['a']]], [[[['b'], [['a'], [['b'], ['b'], '|', ['a'], ['b']], '|', ['b'], [[['a'], '|', ['b']], [['a'], '|', ['b']]]], '|', ['a'], [['b'], [['b'], ['b']], '|', ['a'], [['b'], ['b'], '|', ['a'], [['a'], '|', ['b']]]]], ['b'], '|', [[[['a'], ['a'], '|', ['a'], ['b']], ['a'], '|', [['b'], ['b']], ['b']], ['b'], '|', [[[['a'], '|', ['b']], ['a'], '|', ['b'], ['b']], ['a']], ['a']], ['a']], [['b'], [['b'], [['a'], [['b'], ['a']], '|', ['b'], [['a'], ['a']]], '|', ['a'], [['b'], [['a'], ['b'], '|', [['a'], '|', ['b']], ['a']], '|', ['a'], [['b'], ['a'], '|', ['a'], ['b']]]], '|', ['a'], [['b'], [[['a'], ['b'], '|', [['a'], '|', ['b']], ['a']], ['b'], '|', [[['a'], '|', ['b']], ['a'], '|', ['b'], ['b']], ['a']], '|', ['a'], [[['b'], ['a']], ['b'], '|', [['b'], ['a'], '|', ['b'], ['b']], ['a']]]]]]
)
send_over = ''.join(temp_list_1000)
print(send_over)
matches = []
for i in search_terms:
    # print(i)
    matches.append(re.findall(r'\b(%s)\b' % send_over, i))
matches = [x for x in matches if x != []]
# kippy = group_parsing(hello)
# kippy = [x for x in kippy if x != []]
# kippy = final_thoughts(kippy)
# print(kippy)
# print("HELLO BOI", rules['0'])
# print(long_boi)
print("The Answer to Part 1 is: %d" % len(matches))

