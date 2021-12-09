import HeightMap


def part1(heightMap: HeightMap.HeightMap):
    num = 0
    for rowNodes in heightMap.matrix:
        for node in rowNodes:
            if node.isBasin():
                num += node.number + 1
    return num


def buildMatrix():
    file = open("input.txt")
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
    print(part1(HMap))
    pass


if __name__ == "__main__":
    main()
