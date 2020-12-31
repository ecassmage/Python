import re
ingredients, allergens = [], []
index = {}
similar_ingredient_index, similarities = {}, {}
all_allergens = []
for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 21\\input.txt').readlines():
    # print("Fuck the retards: %s" % line)
    line = line.replace(')', '')
    line = line.replace('(', '')
    line = line.replace(',', '')
    line = line.replace('\n', '')
    ingredients_temp = line.split(' ')
    contain = False
    ingredient_make, allergen_temp = [], []
    for i in ingredients_temp:
        if contain:
            allergen_temp.append(i)
            continue
        if i == 'contains':
            contain = True
            continue
        else:
            ingredient_make.append(i)
    if contain:
        allergens.append(allergen_temp)
        ingredients.append(ingredient_make)
    else:
        pass
    # print(ingredients_temp)
summation = 0
# print(ingredients)
# print(allergens)
# for i in range(0, len(ingredients)):
#     summation += (len(ingredients[i]) - len(allergens[i]))
#     print(summation)

for i in range(0, len(allergens)):
    for j in range(0, len(allergens[i])):
        if allergens[i][j] not in all_allergens:
            all_allergens.append(allergens[i][j])
for i in all_allergens:
    concatenation = []
    for ingredient in range(0, len(allergens)):
        for ingredient_x in range(0, len(allergens[ingredient])):
            if i == allergens[ingredient][ingredient_x]:
                concatenation.append(ingredients[ingredient])
    similar_ingredient_index.update({i: concatenation})
c, d = 0, 0
# print(similar_ingredient_index)
list_of_bad, list_of_good = [], []
# for i in similar_ingredient_index:
#     for reference in range(0, len(similar_ingredient_index[i][0])):
#         in_all = True
#         for match_list in range(1, len(similar_ingredient_index[i])):
#             for match in range(1, len(similar_ingredient_index[i][match_list])):
#                 if similar_ingredient_index[i][0][reference] != similar_ingredient_index[i][match_list][match]:
#                     in_all = False
#                     # if similar_ingredient_index[i][match_list][match] not in list_of_bad:
#                     #     list_of_bad.append(similar_ingredient_index[i][match_list][match])
#                 else:
#                     in_all = True
#                     break
#                     # print(similar_ingredient_index[i][0][reference], similar_ingredient_index[i][match_list][match])
#             if in_all is False:
#                 pass
#                 # break
#             else:
#                 print(i, similar_ingredient_index[i][0][reference])
#                 if similar_ingredient_index[i][0][reference] not in list_of_good:
#                     list_of_good.append(similar_ingredient_index[i][0][reference])
#                 break
#         # if in_all:
#         #     break
list_of_good_index = {}
for i in similar_ingredient_index:
    list_of_good2 = []
    if len(similar_ingredient_index[i]) < 2:
        for quick in range(0, len(similar_ingredient_index[i][0])):
            # print("The World: %s" % similar_ingredient_index[i][0][quick])
            list_of_good.append(similar_ingredient_index[i][0][quick])
            list_of_good2.append(similar_ingredient_index[i][0][quick])
        list_of_good_index.update({i: list_of_good2})
        continue

    for reference in range(0, len(similar_ingredient_index[i][0])):
        good = True
        for match_list in range(1, len(similar_ingredient_index[i])):
            if similar_ingredient_index[i][0][reference] in similar_ingredient_index[i][match_list]:
                good = True
            else:
                good = False
                break
        if good:
            # print("WHY: %s, %s" % (i, similar_ingredient_index[i][0][reference]))
            list_of_good.append(similar_ingredient_index[i][0][reference])
            list_of_good2.append(similar_ingredient_index[i][0][reference])

    list_of_good_index.update({i: list_of_good2})


# print("FECK %s" % list_of_good)
for i in range(0, len(ingredients)):
    for j in range(0, len(ingredients[i])):
        for m in range(0, len(list_of_good)):
            if ingredients[i][j] not in list_of_good[m] and ingredients[i][j] not in list_of_bad:
                list_of_bad.append(ingredients[i][j])
# print(list_of_bad)
# print("WHAT THE FUCK: %s" % list_of_good)
# print(ingredients)
c = 0
list_of_bad = []
# for good in list_of_good:
#     for i in range(0, len(ingredients)):
#         for j in range(0, len(ingredients[i])):
#             # print(ingredients[i][j])
#             if good != ingredients[i][j] and ingredients[i][j] not in list_of_bad:
#                 list_of_bad.append(ingredients[i][j])
#                 c += 1
for good in ingredients:
    for goosh in good:
        if goosh not in list_of_good and goosh not in list_of_bad:
            list_of_bad.append(goosh)
# print(c)
c = 0
# print(list_of_good)
# print(list_of_bad)
for good in list_of_bad:
    for i in ingredients:
        for j in i:
            if good == j:
                c += 1
# print(c)
# print(list_of_good_index)
finally_list = {}
while True:
    g = 0
    try:
        for i in list_of_good_index:
            if len(list_of_good_index[i]) < 2:
                g = 1
                # print(i, list_of_good_index[i])
                remove = list_of_good_index[i][0]
                finally_list.update({i: remove})
                # print(remove)
                for j in list_of_good_index:
                    temp = list_of_good_index[j]
                    if remove in temp:
                        temp.pop(temp.index(remove))
                        list_of_good_index.update({j: temp})
                del list_of_good_index[i]
                break
    except IndexError:
        # print(list_of_good_index)
        exit()
    if g == 0:
        break
# print('\n\n\n\n')
part_2 = ''
d = 0
for key, value in sorted(finally_list.items()):
    part_2 += ('%s,' % value)
part_2 = part_2[:-1]
print("The Answer to Part 1 is: %d" % c)
print("The Answer to Part 2 is: %s" % part_2)
# print(finally_list)


# And this is after I removed a lot of the bad code
