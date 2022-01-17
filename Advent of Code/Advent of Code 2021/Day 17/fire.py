dictionary = {}


def addFactorial(start=0, end=0):
    if abs(start-end) in dictionary:
        return dictionary[abs(start-end)]
    minimum = min([start, end])
    maximum = max([start, end])
    dictionary[abs(start-end)] = sum(range(minimum, minimum + maximum + 1))
    return dictionary[abs(start-end)]


def getFactTop(start, end, startSpeed=0):
    while start > end:
        startSpeed += 1
        start -= startSpeed
    return start


def checkX(xVel: int, targetX: list):
    x = 0
    iterations = 0
    while not (targetX[0] <= x <= targetX[1]):
        x += xVel
        if xVel < 0:
            xVel += 1
            if x < targetX[0] or targetX[0] > 0:
                return False
        elif xVel > 0:
            xVel -= 1
            if x > targetX[1] or targetX[1] < 0:
                return False
        else:
            return False
        if x > targetX[1]:
            return False
        iterations += 1
    return True


def checkY(yVel: int, targetY: list):
    y = 0
    iterations = 0
    while not (targetY[0] <= y <= targetY[1]):
        y += yVel
        yVel -= 1
        if y < targetY[0]:
            return False
        iterations += 1
    return iterations


def rangeMeasure(x, y, target):

    pass


def test():
    x, y = checkX(20, [20, 30]), checkY(2, [-10, -5])
    print(x, y)
    x, y = checkX(6, [20, 30]), checkY(3, [-10, -5])
    print(x, y)
    pass


def findSmallestX(target):
    x = 0
    while True:
        if checkX(x, target):
            break
        x += 1
    print(x)
    return x


def findLargestX(target):
    return max(target)


def findSmallestY(target):
    return min(target)


def findLargestY(target):
    return abs(min(target))


def updateVel(x, y):
    y -= 1
    if x < 0:
        x += 1
    elif x > 0:
        x -= 1
    return x, y


def part1TrickedMe(target):
    bounds = [findSmallestX(target[0]), findLargestX(target[0]), findSmallestY(target[1]), findLargestY(target[1])]
    good = []
    print(bounds)
    for x in range(bounds[0], bounds[1]+1):
        for y in range(bounds[2], bounds[3]):
            coord = [0, 0]
            xVel = x
            yVel = y
            valid = True
            if x == 7 and y == 2:
                pass
            while not (target[0][0] <= coord[0] <= target[0][1] and target[1][0] <= coord[1] <= target[1][1]):
                coord = [coord[0] + xVel, coord[1] + yVel]
                xVel, yVel = updateVel(xVel, yVel)
                if coord[0] > target[0][1] or coord[1] < target[1][0]:
                    valid = False
                    break
            if valid:
                good.append([x, y])
    print(good)
    print(len(good))


def main(inp):
    line = open(inp).read().strip().replace("target area: x=", '').replace(', y=', ' ').replace('..', ' ').split()
    listOfStuff = [[int(line[0]), int(line[1])], [int(line[2]), int(line[3])]]
    print(listOfStuff)
    part1TrickedMe(listOfStuff)
    # findLargestY(listOfStuff, x)
    pass


if __name__ == '__main__':
    main('input.txt')
    print(addFactorial(0, 197))
    pass
