from itertools import permutations
from multiprocessing import Pool
import re
import random


def openFile(fileLocation):
    pizzas = {}
    nums = []
    c = 0
    for n, i in enumerate(open(fileLocation)):
        if n == 0:
            nums = re.findall(r'\d+', i)
            for num, val in enumerate(nums):
                nums[num] = int(val)
            continue
        if i == '\n':
            continue
        else:
            num = re.findall(r"\d+", i)
            lis = re.findall(r'[^ 0-9\n]+', i)
            if len(lis) == 0:
                continue
            pizzas.update({f"{c}": [int(num[0]), lis]})
            c += 1
    return pizzas, nums


def sortPizzas(pizzaList, shuffleList):
    sortedList = sorted(pizzaList, key=lambda k: (pizzaList[k][0]))
    returnList = []
    # print(sortedList)
    if shuffleList == 0:
        for i in reversed(sortedList):
            returnList.append(i)
        return returnList
    else:
        random.shuffle(sortedList)
        return sortedList
    # print(sortedList)
    # return returnList


def findingCombos(numberList, pizzaList, order):
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
                nextLine += f"{pizzaList[thisPizza]} "
            currentPizza += order[orderNum][1] - 1
            nextLine += f"{pizzaList[currentPizza]}"
            currentPizza += 1
            numberList[0] -= order[orderNum][1]
            numberList[order[orderNum][0]] -= 1
            Deliveries += 1
            returnList.append(nextLine)
    return returnList, Deliveries


def countPoints(group, pizzas):
    totalPoints = 0
    for table in group[1]:
        uniqueIngredients = []
        for pizza in table[1:]:
            if pizza == ' ':
                continue
            for ingredient in pizzas[pizza][1]:

                if ingredient not in uniqueIngredients:
                    uniqueIngredients.append(ingredient)
            # print(f'{pizzas[pizza]}', end=', ')
        # print(f"\n{uniqueIngredients}")
        totalPoints += len(uniqueIngredients) ** 2
    return totalPoints


def writeProgram(listToReturn, DeliveriesToReturn, fileName):
    response = open(fileName, "w")
    response.write(f"{DeliveriesToReturn}\n")
    for line in listToReturn:
        response.write(f"{''.join(line)}\n")
    response.close()


def bestTXT(best):
    bestestList = []
    for i in range(5):
        bestestList.append([0, 0, 0])
    """
    bestest = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    """
    # print(best)
    for secondBestList in best:
        # print(secondBestList)
        for gg, bestPerSub, bestPerSubOrder in secondBestList:
            # print(gg, bestPerSub, bestPerSubOrder)
            r1, r2, r3, r4, r5 = bestPerSub
            c1, c2, c3, c4, c5 = bestPerSubOrder
            print(r1, r2, r3, r4, r5)
            print(c1, c2, c3, c4, c5)
            print()
            if r1 > bestestList[0][1]:
                bestestList[0][0] = gg
                bestestList[0][1] = r1
                bestestList[0][2] = c1
            if r2 > bestestList[1][1]:
                bestestList[1][0] = gg
                bestestList[1][1] = r2
                bestestList[1][2] = c2
            if r3 > bestestList[2][1]:
                bestestList[2][0] = gg
                bestestList[2][1] = r3
                bestestList[2][2] = c3
            if r4 > bestestList[3][1]:
                bestestList[3][0] = gg
                bestestList[3][1] = r4
                bestestList[3][2] = c4
            if r5 > bestestList[4][1]:
                bestestList[4][0] = gg
                bestestList[4][1] = r5
                bestestList[4][2] = c5
    return bestestList


def main(gg):
    listOfFiles = [
        ["a_example", "aSubmission.txt"],
        ["b_little_bit_of_everything.in", "bSubmission.txt"],
        ["c_many_ingredients.in", "cSubmission.txt"],
        ["d_many_pizzas.in", "dSubmission.txt"],
        ["e_many_teams.in", "eSubmission.txt"]
    ]
    # listOfFiles = [["b_little_bit_of_everything.in", "bSubmission.txt"]]
    # print(listOfOrders)
    bestOfBest = []
    # for gg in range(4):
    listOfOrders = list(permutations([[1, 2], [2, 3], [3, 4]]))
    tempGreatList = []
    pizzasList = []
    print(f"Starting: {gg}")
    for order in listOfOrders:
        for inP, blank in listOfFiles:
            pizzaDict, NumberList = openFile(inP)
            sortedList = sortPizzas(pizzaDict, gg)
            finishedList, Deliveries = findingCombos(NumberList, sortedList, order)
            tempGreatList.append([Deliveries, finishedList])
            pizzasList.append(pizzaDict)
    bestPerSub = [0] * len(listOfFiles)
    bestPerSubOrder = [0] * len(listOfFiles)
    for number in range(len(tempGreatList)):
        tempPoints = countPoints(tempGreatList[number], pizzasList[number])
        # print(tempPoints, end=', ')
        if tempPoints > bestPerSub[number % len(listOfFiles)]:
            bestPerSub[number % len(listOfFiles)] = tempPoints
            bestPerSubOrder[number % len(listOfFiles)] = number
    # print()
    # print(f"{bestPerSub}\n{bestPerSubOrder}")
    bestOfBest.append((gg, bestPerSub, bestPerSubOrder))
    for num, ind in enumerate(bestPerSubOrder):
        writeProgram(tempGreatList[ind][1], tempGreatList[ind][0], f"Submissions/{gg}{listOfFiles[num][1]}")
    # bestTXT(bestOfBest)
    # print(bestOfBest)
    return bestOfBest


if __name__ == "__main__":
    lis = [0, 1, 2, 3]
    with Pool(processes=4) as p:
        bestList = p.map(main, lis)
    # print(bestList)
    print(bestTXT(bestList))


