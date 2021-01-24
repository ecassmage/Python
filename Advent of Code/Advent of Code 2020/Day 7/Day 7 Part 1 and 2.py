import re


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

                            THIS DOES WORK PROPERLY AND IS THE CORRECT ONE TO LOOK AT!!!
                            
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def main_function(x_dict, current):
    total_sum = 0
    if current == 0:
        return 0
    for sub_bag in current:
        total_sum += (main_function(x_dict, x_dict[sub_bag]) + 1) * current[sub_bag]
    return total_sum


def part_1_function(x_dict, current=None):
    total = 0
    if current is not None:
        if x_dict[current] == 0:
            return 0
        if 'shiny gold' in x_dict[current]:
            return 1
        for bag in x_dict[current]:
            total += part_1_function(x_dict, bag)
            if total == 1:
                return 1
        return total
    else:
        for bag in x_dict:
            total += part_1_function(x_dict, bag)
            pass
    return total


bags_dictionary = {}
for bag_hierarchy in open("input.txt"):
    bag_hierarchy = bag_hierarchy.replace('.', '')
    freedom = re.findall('(.+) bags contain (.+)', bag_hierarchy)
    temp = freedom[0][1].split(', ')
    inside = {}
    for inside_bags in temp:
        if inside_bags == 'no other bags':
            bags_dictionary.update({freedom[0][0]: 0})
            break
        temp_inside = inside_bags.split(' ', 1)
        temp_inside[1] = temp_inside[1].replace(' bags', '')
        temp_inside[1] = temp_inside[1].replace(' bag', '')
        inside.update({temp_inside[1]: int(temp_inside[0])})
    else:
        bags_dictionary.update({freedom[0][0]: inside})
print(f"The answer to Part 1 is: {part_1_function(bags_dictionary)}")
print(f"The answer to Part 2 is: {main_function(bags_dictionary, bags_dictionary['shiny gold'])}")
