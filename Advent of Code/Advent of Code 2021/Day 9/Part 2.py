import HeightMap


def recursiveCall(node, listOfAlreadyVisited=None):
    Counts = [0] * 5
    if listOfAlreadyVisited is None:
        listOfAlreadyVisited = []
    if node.number < 9 and node.isSloped(listOfAlreadyVisited):
        Counts[0] = 1
        listOfAlreadyVisited.append(node)
        if node.up is not None and node.up not in listOfAlreadyVisited:
            Counts[1], listOfAlreadyVisited = recursiveCall(node.up, listOfAlreadyVisited)
        if node.down is not None and node.down not in listOfAlreadyVisited:
            Counts[2], listOfAlreadyVisited = recursiveCall(node.down, listOfAlreadyVisited)
        if node.left is not None and node.left not in listOfAlreadyVisited:
            Counts[3], listOfAlreadyVisited = recursiveCall(node.left, listOfAlreadyVisited)
        if node.right is not None and node.right not in listOfAlreadyVisited:
            Counts[4], listOfAlreadyVisited = recursiveCall(node.right, listOfAlreadyVisited)
    return sum(Counts), listOfAlreadyVisited


def part2(heightMap: HeightMap.HeightMap):
    listOfStuff = []
    for rowNodes in heightMap.matrix:
        for node in rowNodes:
            if node.isBasin():
                val = recursiveCall(node)
                listOfStuff.append(val[0])
    finalThree = (sorted(listOfStuff, reverse=True)[0:3])
    return finalThree[0] * finalThree[1] * finalThree[2]


def buildMatrix():
    file = open("test.txt")
    matrixArray = []
    for line in file:
        lis = []
        for num in list(line.strip()):
            lis.append(int(num))
        matrixArray.append(lis)
    file.close()
    return matrixArray


def main():
    matrix = buildMatrix()
    HMap = HeightMap.HeightMap(matrix)
    print(part2(HMap))


if __name__ == "__main__":
    main()
