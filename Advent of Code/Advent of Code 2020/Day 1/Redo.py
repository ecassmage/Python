def find3(dictionary):
    for key1 in dictionary.keys():
        for key2 in dictionary.keys():
            if 2020 - key1 - key2 in dictionary:
                return key1 * key2 * (2020 - key1 - key2)


def find2(dictionary):
    for key in dictionary.keys():
        if 2020 - key in dictionary:
            return key * (2020-key)


def main():
    dictionary = {}
    for line in open("input.txt"):
        dictionary.update({int(line): line})
    print(find2(dictionary))
    print(find3(dictionary))


if __name__ == '__main__':
    main()
