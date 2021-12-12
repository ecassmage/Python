import copy
globalList = []


class Node:
    def __init__(self, Letter):
        self.Connected = []
        self.letter = Letter
        self.smallCave = False
        self.Checked = False
        self.PathsTaken = []

        if not 'A' <= self.letter <= 'Z':
            self.smallCave = True

    def connectTo(self, node):
        self.Connected.append(node)

    def isEnd(self):
        return self.letter == "end"

    def hasBeen(self, listOfGoneToo=None):
        return self.letter == 'start' or self.Checked if listOfGoneToo is None else self.letter == 'start' or (self in listOfGoneToo and self.smallCave)


def iterate(node, listOfGoneToo=None, doubled=False):
    if listOfGoneToo is None:
        listOfGoneToo = []

    nums = 0
    if node.isEnd():
        return 1
    if node.hasBeen(listOfGoneToo):
        if not doubled and node.letter != "start":
            doubled = True
        else:
            return 0

    if node not in listOfGoneToo:
        listOfGoneToo.append(node)
    for path in node.Connected:
        nums += iterate(path, copy.copy(listOfGoneToo), doubled)

    return nums


def start(startNode):
    nums = 0
    for path in startNode.Connected:
        nums += iterate(path, [startNode])
    return nums


def main(file):
    array = []
    dictionary = {}
    for line in open(file):
        array.append(line.strip().split("-"))
    for line in array:
        Node1 = dictionary.get(line[0], Node(line[0]))
        Node2 = dictionary.get(line[1], Node(line[1]))
        Node1.connectTo(Node2)
        Node2.connectTo(Node1)
        dictionary.update({line[0]: Node1, line[1]: Node2})

    print(array)
    print(dictionary)
    print(start(dictionary['start']))


if __name__ == '__main__':
    main("input.txt")
