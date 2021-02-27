from itertools import permutations
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
            lis = re.findall(r'[^ 0-9\n]+', i)
            if len(lis) == 0:
                continue
            pizzas.update({f"{c}": lis})
            c += 1
    return pizzas, nums


def findCombinations(numberList, order):
    returnList = []
    orderNum = 0
    Deliveries = 0
    currentPizza = 0
    while orderNum < 3 and numberList[0] > 2:
        if numberList[order[orderNum]] <= 0 or numberList[0] < order[orderNum] + 2:
            orderNum += 1
            continue
        nextLine = f"{order[orderNum] + 2} "

        # print(numberList[order[orderNum]])
        if numberList[0] >= order[orderNum] + 2 and numberList[order[orderNum]] > 0:
            numberList[order[orderNum]] -= 1
            numberList[0] -= (order[orderNum] + 2)
            for thisPizza in range(currentPizza, currentPizza + order[orderNum] + 1):
                nextLine += f"{thisPizza} "
            currentPizza += order[orderNum] + 1
            nextLine += f"{currentPizza}"
            currentPizza += 1
            Deliveries += 1
        returnList.append(nextLine)
    print(currentPizza)
    return returnList, Deliveries


def findingCombos(numberList, order):
    returnList = []
    orderNum = 0
    Deliveries = 0
    currentPizza = 0
    while numberList[0] >= 2 and orderNum < 3:
        if numberList[0] < order[orderNum][1] or numberList[order[orderNum][0]] == 0:
            orderNum += 1
            continue
        else:
            nextLine = f"{order[orderNum][1]} "
            for thisPizza in range(currentPizza, currentPizza + order[orderNum][1] - 1):
                nextLine += f"{thisPizza} "
            currentPizza += order[orderNum][1] - 1
            nextLine += f"{currentPizza}"
            currentPizza += 1
            numberList[0] -= order[orderNum][1]
            numberList[order[orderNum][0]] -= 1
            Deliveries += 1
            returnList.append(nextLine)
    return returnList, Deliveries


def writeProgram(listToReturn, DeliveriesToReturn, fileName):
    response = open(fileName, "w")
    response.write(f"{DeliveriesToReturn}\n")
    for line in listToReturn:
        response.write(f"{''.join(line)}\n")
    response.close()


def writeProgramAdvanced(listOfReturns, listOfReturnIndexes, fileName, group):
    for i in listOfReturnIndexes:
        response = open(f"{fileName}", "w")
        for listLevel in listOfReturns[i]:
            """ [2, [Numbers]] """
            response.write(f"{listLevel[0]}\n")
            for level in listLevel[1]:
                response.write(f"{''.join(level)}\n")
    # response.write(f"{DeliveriesToReturn}\n")
    # for line in listToReturn:
    #
    #     response.write(f"{''.join(line)}\n")
    # response.close()


def countPoints(group, pizzas):
    totalPoints = 0
    for table in group[1]:
        uniqueIngredients = []

        for pizza in table[1:]:
            if pizza == ' ':
                continue
            for ingredient in pizzas[pizza]:
                if ingredient not in uniqueIngredients:
                    uniqueIngredients.append(ingredient)

        totalPoints += (len(uniqueIngredients) * len(uniqueIngredients))
    return totalPoints


def main():
    listOfFiles = [
        ["a_example", "aSubmission.txt"],
        ["b_little_bit_of_everything.in", "bSubmission.txt"],
        ["c_many_ingredients.in", "cSubmission.txt"],
        ["d_many_pizzas.in", "dSubmission.txt"],
        ["e_many_teams.in", "eSubmission.txt"]
    ]
    # listOfFiles = [["b_little_bit_of_everything.in", "bSubmission.txt"]]
    listOfOrders = list(permutations([[1, 2], [2, 3], [3, 4]]))
    # print(listOfOrders)
    tempGreatList = []
    pizzasList = []
    for order in listOfOrders:
        for inP, blank in listOfFiles:
            # outP = f"Submissions/{listOfOrders.index(order)}{outP}"
            pizzaDict, NumberList = openFile(inP)
            finishedList, Deliveries = findingCombos(NumberList, order)
            tempGreatList.append([Deliveries, finishedList])
            pizzasList.append(pizzaDict)
            # writeProgram(finishedList, Deliveries, outP)
            # print("Next")
    # print(tempGreatList)
    bestPerSub = [0] * len(listOfFiles)
    bestPerSubOrder = [0] * len(listOfFiles)
    for number in range(len(tempGreatList)):
        tempPoints = countPoints(tempGreatList[number], pizzasList[number])
        print(tempPoints, end=', ')
        # a = number % 5
        if tempPoints > bestPerSub[number % len(listOfFiles)]:
            bestPerSub[number % len(listOfFiles)] = tempPoints
            bestPerSubOrder[number % len(listOfFiles)] = number
    # writeProgramAdvanced(tempGreatList, bestPerSubOrder, 'Submissions/', listOfFiles)
    print()
    print(f"{bestPerSub}\n{bestPerSubOrder}")
    for num, ind in enumerate(bestPerSubOrder):
        writeProgram(tempGreatList[ind][1], tempGreatList[ind][0], f"Submissions/{listOfFiles[num][1]}")


if __name__ == "__main__":
    main()


"""
61, 18544, 871048911, 2295595, 10566870, 61, 18050, 871694523, 2327629, 10406831, 65, 19033, 890266578, 2338017, 9403148, 65, 17628, 900381483, 2404164, 9403148, 49, 18323, 892216467, 2366761, 8441080, 49, 17677, 903362762, 2428270, 8441080, 
[65, 19033, 903362762, 2428270, 10566870]
"""