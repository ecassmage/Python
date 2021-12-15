class Linked:
    def __init__(self, letter):
        self.letter = letter
        self.next = None
        self.prev = None

    def setPrev(self, prev):
        self.prev = prev
        prev.next = self

    def setNext(self, nextNode):
        self.next = nextNode
        nextNode.prev = self.next
        pass

    def addAfter(self, node):
        nextTemp = self.next
        self.next = node
        node.next = nextTemp
        node.prev = self


def setupNodes(string):
    nodeStart = None
    nodeEnd = None
    for num, character in enumerate(list(string.strip())):
        node = Linked(character)
        if num == 0:
            nodeStart = node
            nodeEnd = node
        else:
            node.setPrev(nodeEnd)
            nodeEnd = node
    return nodeStart


def main(string):
    linkedList = None
    dictionary = {}
    for num, line in enumerate(open(string)):
        if num == 0:
            linkedList = setupNodes(line)
        elif num > 1:
            lis = line.strip().split(" -> ")
            dictionary.update({lis[0]: lis[1]})

    for _ in range(40):
        nodePtr = linkedList
        while nodePtr.next is not None and nodePtr is not None:
            letter1 = nodePtr.letter
            letter2 = nodePtr.next.letter
            if letter1 + letter2 in dictionary:
                newNode = Linked(dictionary[letter1 + letter2])
                nodePtr.addAfter(newNode)
                nodePtr = nodePtr.next
            nodePtr = nodePtr.next
        print(_)
    nodePtr = linkedList
    dictionChars = {}
    while nodePtr is not None:
        dictionChars[nodePtr.letter] = dictionChars.get(nodePtr.letter, 0) + 1
        nodePtr = nodePtr.next
    largest = 0
    smallest = 0
    for key in dictionChars:
        if smallest == 0:
            smallest = dictionChars[key]
        elif dictionChars[key] < smallest:
            smallest = dictionChars[key]
        if dictionChars[key] > largest:
            largest = dictionChars[key]
    return largest - smallest


if __name__ == "__main__":
    print(main("input.txt"))
