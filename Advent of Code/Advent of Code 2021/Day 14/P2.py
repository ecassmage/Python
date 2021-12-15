def dictionarySetup(String):
    dictionary = dict()
    count = dict()
    for num in range(len(String)-2):
        count[String[num]] = count.get(String[num], 0) + 1
        dictionary[String[num] + String[num+1]] = dictionary.get(String[num] + String[num+1], 0) + 1
    count[String[-2]] = count.get(String[-2], 0) + 1
    return dictionary, count


def iteration(dictionary, pairs, count):
    newDictionary = dict()
    for num, pair in enumerate(dictionary):
        if pair in pairs:
            newDictionary[pair[0] + pairs[pair]] = newDictionary.get(pair[0] + pairs[pair], 0) + dictionary[pair]
            newDictionary[pairs[pair] + pair[1]] = newDictionary.get(pairs[pair] + pair[1], 0) + dictionary[pair]
            # well this line was dumb of me. originally wrote above line like this: newDictionary[pairs[pair] + pair[0]] = newDictionary.get(pairs[pair] + pair[0], 0) + dictionary[pair]  notice what is wrong.
            count[pairs[pair]] = count.get(pairs[pair], 0) + dictionary[pair]
        else:
            newDictionary[pair] = newDictionary.get(pair, 0) + dictionary[pair]
    return newDictionary, count


def main(string):
    setDict = {}
    dictionary = {}
    count = dict()
    for num, line in enumerate(open(string)):
        if num == 0:
            setDict, count = dictionarySetup(line)
        elif num > 1:
            lis = line.strip().split(" -> ")
            dictionary.update({lis[0]: lis[1]})
    print(setDict)

    for _ in range(40):
        setDict, count = iteration(setDict, dictionary, count)
        print(count)
    print(setDict)

    largest = 0
    smallest = 0
    for key in count:
        if smallest == 0:
            smallest = count[key]
        elif count[key] < smallest:
            smallest = count[key]
        if count[key] > largest:
            largest = count[key]
    return largest - smallest


if __name__ == '__main__':
    print(main("input.txt"))
