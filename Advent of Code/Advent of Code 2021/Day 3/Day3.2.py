def findCommon(lis):
    arr = []
    for _ in range(len(lis[0])):
        arr.append([0, 0])
    for number in lis:
        for num, char in enumerate(number):
            if char == "0":
                arr[num][0] += 1
            else:
                arr[num][1] += 1
    return arr


def largest(arr):
    for bit in range(len(arr[0])):
        array = findCommon(arr)
        searchBit = '0' if array[bit][0] > array[bit][1] else '1'
        newArr = []
        for i in range(len(arr)):
            if arr[i][bit] == str(searchBit):
                newArr.append(arr[i])
        arr = newArr
    return arr


def smallest(arr):
    for bit in range(len(arr[0])):
        if len(arr) == 1:
            break
        array = findCommon(arr)
        searchBit = '1' if array[bit][0] > array[bit][1] else '0'
        newArr = []
        for i in range(len(arr)):
            if arr[i][bit] == searchBit:
                newArr.append(arr[i])
        arr = newArr
    return arr


def main():
    arr = []
    for line in open("input.txt").readlines():
        arr.append(line.replace("\n", ""))
    First = arr

    O2 = largest(arr)

    arr = First
    CO2 = smallest(arr)
    print(int(CO2[0], 2) * int(O2[0], 2))
    print(CO2, O2)


main()

