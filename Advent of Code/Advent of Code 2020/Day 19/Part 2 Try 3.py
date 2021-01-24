import re
from copy import deepcopy


def annoying_building(w, x, y=0, z=0):
    if z >= len(x):
        return []
    y = w[y]
    if type(y) is str:
        if x[z] == y:
            return [z + 1]
        return []
    matches = []
    for i in y:
        better_matches = [z]
        for better_rule in i:
            new_match = []
            for index in better_matches:
                new_match += annoying_building(w, x, better_rule, index)
            better_matches = new_match
        matches += better_matches
    return matches


rules = {}
inputting = open('input.txt')
for line in map(str.rstrip, inputting):
    if line == '':
        break
    rule_id, options = line.split(': ')
    rule_id = int(rule_id)

    if '"' in options:
        rule = options[1:-1]
    else:
        rule = []
        for option in options.split('|'):
            rule.append(tuple(map(int, option.split())))

    rules[rule_id] = rule
rules2 = deepcopy(rules)
rules2[8] = [(42,), (42, 8)]
rules2[11] = [(42, 31), (42, 11, 31)]
print(rules)
valid = 0
for msg in map(str.rstrip, inputting):
    if len(msg) in annoying_building(rules2, msg):
        valid += 1
print(valid)