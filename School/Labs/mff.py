import random

lisOfRand = []
for i in range(1000000):
    lisOfRand.append([random.randrange(0, 2), random.randrange(0, 2), random.randrange(0, 2)])


numOfMFF = 0
numOfFF = 0
for i in lisOfRand:
    if i == [0, 1, 1]:
        numOfMFF += 1
    numOfF = 0
    for j in i:
        if j == 1:
            numOfF += 1
    if numOfF == 2:
        numOfFF += 1


print(f"Number of Male Female Female Are {numOfMFF} and Number of Female Females are {numOfFF}")

