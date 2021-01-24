import re


class Hierarchy:
    def __init__(self, bag, quantity):
        self.bag = bag
        self.children = []
        self.child_quantity = []
        self.bags_num = quantity
        self.bags_total = quantity + 1

    def add_children(self, value, num):
        self.children.append(value)
        self.child_quantity.append(num)
        # self.bags_total += value.bags_total * (num + 1)

    def count_total_bags(self, lis=[]):
        if self.children:
            for child in self.children:
                if child not in lis:
                    lis = child.count_total_bags()
                    self.bags_total += self.bags_total * self.child_quantity[self.children.index(child)]
        lis.append(self)
        return lis


def build_heir(bags):
    bag_name_to_obj, obj_list = {}, []
    for bag_parents in bags:
        quantity = 0
        for quantity_bags in bags[bag_parents]:
            quantity += bags[bag_parents][quantity_bags]
        obj = Hierarchy(bag_parents, quantity)
        obj_list.append(obj)
        bag_name_to_obj.update({bag_parents: obj})
    for bag_parents in bags:
        parent = bag_name_to_obj[bag_parents]
        for bag_children in bags[bag_parents]:
            child = bag_name_to_obj[bag_children]
            parent.add_children(child, bags[bag_parents][bag_children])
            # parent.count_total_bags()
    return obj_list, bag_name_to_obj


bags_dictionary = {}
for bag_hierarchy in open("../Advent of Code/Advent of Code 2020/Day 7/input.txt"):
    bag_hierarchy = bag_hierarchy.replace('.', '')
    freedom = re.findall('(.+) bags contain (.+)', bag_hierarchy)
    temp = freedom[0][1].split(', ')
    inside = {}
    for inside_bags in temp:
        if inside_bags == 'no other bags':
            bags_dictionary.update({freedom[0][0]: 0})
            continue
        temp_inside = inside_bags.split(' ', 1)
        temp_inside[1] = temp_inside[1].replace(' bags', '')
        temp_inside[1] = temp_inside[1].replace(' bag', '')
        inside.update({temp_inside[1]: int(temp_inside[0])})
    # temp = temp.split(' ', 1)
    bags_dictionary.update({freedom[0][0]: inside})
print(bags_dictionary)
list_obj, dict_obj = build_heir(bags_dictionary)
dict_obj['shiny gold'].count_total_bags()
shiny_gold = []
for i in list_obj:
    if i.bag == 'shiny gold':
        shiny_gold = i
        break
shiny_gold.count_total_bags()
print(list_obj)
