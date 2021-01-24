import re
import copy


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
THIS DOES NOT WORK ANYMORE DON'T KNOW WHY SO I MADE A NEW ONE CALLED 'Day 7 Part 1 and 2.py' WITH RECURSION, MUCH NICER
                                        LEAVING IT UP FOR SOME REASON DUNNO WHY?
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


bags = []
bags1 = []
bags2 = []
bags_remainder = []
bags_mini = []
bag_nums = []
bag_names = []
contains = []
num = 0
bag_mine = 'shiny gold'
count = 0
with open("input.txt", 'r') as Day7:
    Day7.readline()
    for i in Day7:
        l = i.split()
        for l1 in l:
            if l1 == "no":
                # print(i)
                break
        i = i.replace('\n', ' \n')
        i = i.replace(',', '')
        i = i.replace('bags', 'fuck')
        i = i.replace('bag', 'fuck')
        x = i.split(' fuck contain')
        name = x[0]
        bags.append(name)
        # print(x[1])
        parsed = x[1].split(' ')
        parsed.pop(0)
        word = ''
        for j in parsed:
            if j == '\n':
                bags.append(bags_mini)
                word = ''
                num = 0
                bags_mini = []
                break
            if j.isnumeric() is True:
                num = int(j)
            elif j == 'fuck':
                if num != 0 and word != '':
                    bags_mini.append(word)
                    bags_mini.append(num)
                    num = 0
                    word = ''
                    continue
            else:
                if word != '':
                    word = word + ' '
                word = word + j
print(bags)
# for i in range(1, len(bags), 2):
#     while True:
#         bag = False
#         # print(bags[i][0])
#         try:
#             for c in range(0, len(bags[i][0]), 2):
#                 bag_current = bags[i][c]
#                 for j in range(0, len(bags[bags.index(bags[i]) + 1]), 2):
#                     if bags[bags.index(bags[i][j])] == bag_mine:
#                         count = count + 1
#                         bag = True
#                         break
#                     else:
#                         print(bags[i])
#                         i = bags[bags.index(bags[i][j])]
#         except IndexError:
#             # print(bags[i - 1])
#             continue
#     if bag is True:
#         continue
c = 0
shiny = 0

pre_modify = copy.deepcopy(bags)
bags2 = copy.deepcopy(pre_modify)
while True:
    for i in range(1, len(bags), 2):
        current = 0
        for j in range(0, len(bags[i]), 2):
            try:
                current = j
                if bag_mine in bags[i]:
                    contains.append('shiny gold')
                    break
                if bags[i][j] in bags:
                    indexed = bags.index(bags[i][j])
                    for n in bags[indexed + 1]:
                        # y = str(n)
                        # if y.isnumeric() is True:
                        #     n = int(n) * int(bags[i][j + 1])
                        contains.append(n)
            except IndexError:
                pass
        # print(i)
        # print(contains)
        # if shiny == 1:
        #     exit()
        bags[i] = contains
        # print(bags[1])
        contains = []
    count = 0

    if shiny == 2:
        break
    shiny = shiny + 1

    # c = c + 1
    # if c == 4:
    #     break
for i in range(1, len(bags), 2):
    try:
        if bag_mine in bags[i]:
            count = count + 1
    except IndexError:
        pass
print("The Answer to Part 1 is: %d" % count)
count = 0
# for i in range(1, len(bags), 2):
#     bags2.append(bags[i - 1])
#     current = 0
#     for j in range(0, len(bags[i]), 2):
#         try:
#             current = j
#             if bag_mine in bags[i]:
#                 contains.append('shiny gold')
#                 break
#             if bags[i][j] in bags:
#                 indexed = bags.index(bags[i][j])
#                 for n in bags[indexed + 1]:
#                     # y = str(n)
#                     # if y.isnumeric() is True:
#                     #     n = int(n) * int(bags[i][j + 1])
#                     contains.append(n)
#         except IndexError:
#             pass
#     # print(i)
#     # print(contains)
#     # if shiny == 1:
#     #     exit()
#     bags2.append(contains)
#     # print(bags[1])
#     contains = []
# for i in range(1, len(bags2), 2):
#     if bag_mine in bags2[i]:
#         bags_remainder.append(bags2[i - 1])
#         bags_remainder.append(bags.index(bags2[i - 1]))
# count = 0
# for i in range(1, len(bags), 2):
#     for j in range(1, len(bags[i]), 2):
#         try:
#             if str(bags[i][j]).isnumeric() is True:
#                 count = count + int(bags[i][j])
#         except IndexError:
#             pass
# print(count)
# print(bags)
# print(bags2)
# print(bags_remainder)
# print(pre_modify)
# bags2 = pre_modify.copy()
bags3 = copy.deepcopy(pre_modify)
# for mine in range(1, len(pre_modify[pre_modify.index(bag_mine) + 1]), 2):
#     bag_nums.append(pre_modify[pre_modify.index(bag_mine) + 1][mine])
# print(bag_nums)
# for i in range(1, len(pre_modify), 2):
#     for j in range(1, len(pre_modify[i]), 2):
#         pre_modify[i][j] = pre_modify[i][j] + 1
for time in range(0, 7):
    bag_count = 0
    word1 = ''
    for i in range(0, len(pre_modify), 2):
        if pre_modify[i] == bag_mine:
            location = i
        try:
            for n in range(0, len(pre_modify), 2):
                num1 = pre_modify[i + 1][n + 1]
                word1 = pre_modify[i + 1][n]
                if word1 in pre_modify:
                    bag_count = 0
                    for m in range(1, len(pre_modify[pre_modify.index(word1) + 1]), 2):
                        # print("Hello World: %s" % bags2[bags2.index(word1) + 1][m])
                        # print("Goodbye World: %s" % bags3[bags2.index(word1) + 1][m])
                        # if time == 0:
                        #     bag_count = bag_count + bags2[bags2.index(word1) + 1][m]
                        # else:
                        #     if bags2[bags2.index(word1) + 1][m] != bags1[bags2.index(word1) + 1][m]:
                        #         bag_count = bag_count + bags2[bags2.index(word1) + 1][m]
                        bag_count = bag_count + bags2[bags2.index(word1) + 1][m]
                        # print(num1)
                        # print(bag_count)
                    bags3[i + 1][n + 1] = num1 * bag_count
                        # print(num1 * bag_count)
        except IndexError:
            pass
    # print(pre_modify)
    # print(bags1)
    # print(bags2)
    # print(bags3)
    for mine in range(1, len(bags2[bags2.index(bag_mine) + 1]), 2):
        bag_nums.append(bags2[bags2.index(bag_mine) + 1][mine])
    bags1 = copy.deepcopy(bags2)
    bags2 = copy.deepcopy(bags3)
# print(bags1)
# print(bags2)
# print(bags3)
# print(bag_nums)
# print(bag_nums)
sume = 0
for i in bag_nums:
    sume = sume + int(i)
print("The Answer to Part 2 is: %s" % sume)
# locate = []
# location = 0
# bags_in_bags = 1
# for i in range(0, len(pre_modify), 2):
#     if pre_modify[i] == bag_mine:
#         location = i
# locate.append(pre_modify[location])
# locate.append(pre_modify[location + 1])
# print(locate)