def doStuff(list1):
    zero = 0
    for _ in range(256):
        for j in range(0, 9):
            if j == 0:
                zero = list1[0]
            else:
                list1[j - 1] = list1[j]

        list1[8] = zero
        list1[6] += zero
    return fishy


if __name__ == "__main__":
    fishy = [0] * 9
    for line in open("input.txt"):
        for element in line.replace("\n", "").split(","):
            fishy[int(element)] += 1

    fishy = doStuff(fishy)
    print(sum(fishy))

