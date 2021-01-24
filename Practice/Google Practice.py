from itertools import combinations
import copy
import math
teams = {}
pizzas = {}
list_temp_2 = []
list_temp = []
unique_ingredients = []


def pizza_delivery(pizza, ingredient, comb):
    group_ingredient_count = 0
    for individual_pizza in comb:
        for ind_ingredient in pizza[individual_pizza]:
            if ind_ingredient in ingredient:
                group_ingredient_count += 1
                ingredient.pop(ingredient.index(ind_ingredient))
    points = group_ingredient_count ** 2
    return points


for num, line in enumerate(open('a_example')):
    line = line.replace('\n', '')
    if num > 0:
        list_temp_2 = (line.split(' '))[1:]
        for ingredients in list_temp_2:
            if ingredients not in unique_ingredients:
                unique_ingredients.append(ingredients)
        pizzas.update({f'pizza {num - 1}': list_temp_2})
    else:
        list_temp = line.split(' ')
        teams.update({3: int(list_temp[3])})
        teams.update({2: int(list_temp[2])})
        teams.update({1: int(list_temp[1])})

# print(list_temp)
# print(list_temp_2)
# print(teams)
# print(pizzas)
# print(unique_ingredients)
largest_point_count = 0
best_pizza_combo = ()
ingredients_lost = 0
for i in reversed(range(2, 5)):
    if len(pizzas) < i:
        continue
    unique_fucks = copy.copy(unique_ingredients)
    largest_point_count = 0
    # pizza_list = list(pizzas)
    print(pizzas)
    combos = list(combinations(pizzas, i))
    for combo in combos:
        point = pizza_delivery(pizzas, unique_fucks, combo)
        if point > largest_point_count:
            largest_point_count = point
            ingredients_lost = math.sqrt(point)
            best_pizza_combo = combo
    print(largest_point_count)
    print(best_pizza_combo)
    print(ingredients_lost)
    print('\n')
    print(f"Done {i}")
    for pizza_del in reversed(best_pizza_combo):
        del pizzas[pizza_del]

