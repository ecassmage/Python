import re


def openFile(fileLocation):
    pizzas = {}
    nums = []
    c = 0
    for n, i in enumerate(open(fileLocation)):
        if n == 0:
            nums = re.findall(r'\d+', i)
            for num, val in enumerate(nums):
                nums[num] = int(val)
        if i == '\n':
            continue
        else:
            lis = re.findall(r'[a-z,A-Z]+', i)
            if len(lis) == 0:
                continue
            pizzas.update({f"{c}": lis})
            c += 1
    return pizzas, nums


def countPoints(group, pizzas):
    totalPoints = 0
    for table in group:
        uniqueIngredients = []
        # print(repr(table))
        # exit()
        for pizza in table[0][1:]:
            if pizza == ' ':
                continue
            for ingredient in pizzas[pizza]:
                if ingredient not in uniqueIngredients:
                    uniqueIngredients.append(ingredient)
        a = table[0]
        # print(uniqueIngredients, len(uniqueIngredients))

        totalPoints += len(uniqueIngredients) ** 2
        # print(totalPoints)

    return totalPoints


def GenerateMakes(pizzas, nums):
    c = 0
    D = 0
    madeList = []
    for i in range(len(pizzas)):
        if nums[0] >= 4 and nums[3] > 0:
            nums[0] -= 4
            nums[3] -= 1
            madeList.append([f'4 {c} {c+1} {c+2} {c+3}'])
            c += 4
            D += 1
        elif nums[0] >= 3 and nums[2] > 0:
            nums[0] -= 3
            nums[2] -= 1
            madeList.append([f'3 {c} {c + 1} {c + 2}'])
            c += 3
            D += 1
        elif nums[0] >= 2 and nums[1] > 0:
            nums[0] -= 2
            nums[1] -= 1
            madeList.append([f'2 {c} {c + 1}'])
            c += 2
            D += 1
        else:
            break
    print(nums)
    return madeList, D


def writeProgram(listToReturn, DeliveriesToReturn, fileName):
    response = open(fileName, "w")
    response.write(f"{DeliveriesToReturn}\n")
    for line in listToReturn:

        response.write(f"{''.join(line)}\n")
    response.close()


if __name__ == "__main__":
    listOfFiles = [
        ["a_example", "aSubmission.txt"],
        ["b_little_bit_of_everything.in", "bSubmission.txt"],
        ["c_many_ingredients.in", "cSubmission.txt"],
        ["d_many_pizzas.in", "dSubmission.txt"],
        ["e_many_teams.in", "eSubmission.txt"]
    ]

    for inP, outP in listOfFiles:
        pizzaDict, NumberList = openFile(inP)
        finishedList, Deliveries = GenerateMakes(pizzaDict, NumberList)
        print(finishedList)
        print(f"{countPoints(finishedList, pizzaDict)}, ")
        writeProgram(finishedList, Deliveries, outP)
