import time
import re
import os


def findMostFrequent(StringArr):
    dictionary = {}
    # print("Starting Now")  # it takes a while to parse a txt file when you aren't trying to be efficient
    timer = time.time()
    for word in StringArr:  # O(n)
        if word in dictionary:  # O(1)
            dictionary[word] = dictionary[word] + 1  # O(1)
        else:
            dictionary.update({word: 1})  # O(1)

    largest = ["", 0, 0.0]
    for word in dictionary:  # O(n)
        if dictionary[word] > largest[1]:
            largest[1] = dictionary[word]
            largest[0] = word
    largest[2] = float(time.time() - timer)
    return largest
    pass


def parseTxtFile(fileName):
    string = []
    for line in open(fileName, "r").readlines():
        stringList = re.findall("[a-zA-Z]+", line)
        for word in stringList:
            string.append(word.lower())
    return string


def allTxtFiles():
    path = "Folder"
    for txtFile in os.listdir(os.path.dirname(os.path.abspath(os.curdir)) + "\\Data Structures\\" + path):
        returned = findMostFrequent(parseTxtFile(path + "\\" + txtFile))
        print(f"For File: {txtFile}: The most frequent word is '{returned[0]}' with {returned[1]} occurrence", end='')
        print("s", end='') if returned[1] < 2 else print("", end='')  # for nice formatting where 1 occurrence isn't shown as 1 occurrences. though that doesn't happen so this is all pointless.
        print(f" taking {returned[2] * 1000} milliseconds")

    pass


if __name__ == '__main__':
    # stringArr = "there are two ways of constructing a software design one way is to make it so simple that there are obviously no deficiencies and the other way is to make it so complicated that there are no obvious deficiencies".lower().split(" ")

    # returned = findMostFrequent(parseTxtFile("text.txt"))
    # print(f"The most frequent word is '{returned[0]}' with {returned[1]} occurrence", end='')
    # print("s", end='') if returned[1] < 2 else print("", end='')
    # print(f" taking {returned[2] * 1000} milliseconds")
    allTxtFiles()

