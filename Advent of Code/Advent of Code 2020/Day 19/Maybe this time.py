import re
from copy import deepcopy
search_sect = False
dict_of_rules = {}
search_terms = []


def search_re_write(x, term_good=[]):
    term_good.append('(')
    for section in x:
        if isinstance(section, list):
            search_re_write(section)
        else:
            term_good.append(section)
    term_good.append(')')
    return term_good


def parse_recursive_proof(x_dict, string, current=None):
    pass


def parse(x_dict, current=None):
    if current is None:
        for part in x_dict:
            x_dict.update({part: parse(x_dict, x_dict[part])})
    else:
        for num, part in enumerate(current):
            if isinstance(part, list):
                parse(x_dict, part)
            if part == '|':
                continue
            elif part == 'a' or part == 'b':
                continue
            else:
                current[num] = x_dict[int(part)]
        return current
    return x_dict


for line in open("sample.txt"):
    if line == '\n':
        search_sect = True
        continue
    if search_sect:
        search_terms.append(re.findall(r'\w+', line))
    else:
        dict_temp = re.findall(r'(\d+): (.+)\n', line)
        pull_out = re.findall(r'\d+|\||\w', dict_temp[0][1])
        dict_of_rules.update({int(dict_temp[0][0]): pull_out})
made_list = parse(dict_of_rules)
made_list_2 = ''.join(search_re_write(made_list[0]))
matches = []
for i in search_terms:
    i = str(i)
    matches.append(re.findall(r'\b(%s)\b' % made_list_2, i))
matches = [x for x in matches if x != []]
print(len(matches))
original_list = deepcopy(made_list)
made_list[8] = ['42', '|', '42', '8']
made_list[11] = ['42', '31', '|', '42', '11', '31']
made_list[0] = ['8', '11']

proofed_plz = parse_recursive_proof(made_list, original_list)
print(made_list)
print(proofed_plz)
print(made_list[0])
print(proofed_plz[0])
# dict_of_rules[8] = '42 | 42 8'
# dict_of_rules[11] = '42 31 | 42 11 31'
