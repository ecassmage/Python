def nextDict(setOfSegments, segOutputs):
    segKnown = [''] * 4
    for part in setOfSegments.split(" "):
        match len(part):
            case 2:
                segKnown[0] = part
            case 3:
                segKnown[1] = part
            case 4:
                segKnown[2] = part
            case 7:
                segKnown[3] = part

    numberCount = 0
    for part in segOutputs.split(" "):
        numberCount *= 10
        match len(part):
            case 2:
                numberCount += 1
            case 3:
                numberCount += 7
            case 4:
                numberCount += 4
            case 5:
                two = {1: [1, 0], 4: [2, 0], 7: [2, 0]}
                three = {1: [2, 0], 4: [3, 0], 7: [3, 0]}
                five = {1: [1, 0], 4: [3, 0], 7: [2, 0]}

                for char in part:
                    if char in segKnown[0]:
                        two[1][1] += 1
                        three[1][1] += 1
                        five[1][1] += 1
                    if char in segKnown[1]:
                        two[7][1] += 1
                        three[7][1] += 1
                        five[7][1] += 1
                    if char in segKnown[2]:
                        two[4][1] += 1
                        three[4][1] += 1
                        five[4][1] += 1
                numberPos = []
                for numberGamesSuck, dic in enumerate([two, three, five]):
                    for Key in dic:
                        if dic[Key][0] != dic[Key][1]:
                            break
                    else:
                        match numberGamesSuck:
                            case 0:
                                numberPos.append(2)
                                numberCount += 2
                            case 1:
                                numberPos.append(3)
                                numberCount += 3
                            case 2:
                                numberPos.append(5)
                                numberCount += 5
                            case _:
                                print("you succk")
                if len(numberPos) > 1:
                    print(numberPos)

            case 6:
                zero = {1: [2, 0], 4: [3, 0], 7: [3, 0]}
                six = {1: [1, 0], 4: [3, 0], 7: [2, 0]}
                nine = {1: [2, 0], 4: [4, 0], 7: [3, 0]}

                for char in part:
                    if char in segKnown[0]:
                        zero[1][1] += 1
                        six[1][1] += 1
                        nine[1][1] += 1
                    if char in segKnown[1]:
                        zero[7][1] += 1
                        six[7][1] += 1
                        nine[7][1] += 1
                    if char in segKnown[2]:
                        zero[4][1] += 1
                        six[4][1] += 1
                        nine[4][1] += 1
                numberPos = []
                for numberGamesSuck, dic in enumerate([zero, six, nine]):
                    for Key in dic:
                        if dic[Key][0] != dic[Key][1]:
                            break
                    else:
                        match numberGamesSuck:
                            case 0:
                                numberPos.append(0)
                                numberCount += 0
                            case 1:
                                numberPos.append(6)
                                numberCount += 6
                            case 2:
                                numberPos.append(9)
                                numberCount += 9
                            case _:
                                print("you succk")
                if len(numberPos) > 1:
                    print(numberPos)
            case 7:
                numberCount += 8
    return numberCount


if __name__ == "__main__":
    arr = []
    for line in open("input.txt"):
        arr.append(line.replace("\n", "").split(" | "))
    total = 0
    for beatRoot in arr:
        total += nextDict(beatRoot[0], beatRoot[1])

    print(total)
