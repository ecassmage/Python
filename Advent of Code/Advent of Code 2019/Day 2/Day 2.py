import copy


def Part1(array, noun=12, verb=2):
    array[1] = noun
    array[2] = verb
    end = len(array)
    ptr = 0
    while ptr < end+1:
        match array[ptr]:
            case 1:
                array[array[ptr + 3]] = array[array[ptr + 1]] + array[array[ptr + 2]]
            case 2:
                array[array[ptr + 3]] = array[array[ptr + 1]] * array[array[ptr + 2]]
            case _, 99:
                print(f"ERROR -> {noun}, {verb}")
                break
        ptr += 4
    return array[0]


def Part2(array):
    for i in range(100):
        for j in range(100):
            if Part1(copy.copy(array), i, j) == 19690720:
                return 100 * i + j
    return 0


if __name__ == '__main__':
    arr = []
    for line in open("input.txt"):
        arr = line.strip().split(",")
    for num in range(len(arr)):
        arr[num] = int(arr[num])

    print(Part1(copy.copy(arr)))
    print(Part2(arr))
