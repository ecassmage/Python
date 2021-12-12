class Node:
    def __init__(self, this, prev):
        self.this = this
        self.next = prev  # kinda confusing


class Stack:
    def __init__(self):
        self.last = None


def parentheses(par):  # ()
    match par:
        case ")":
            return True
        case _:
            return False


def angledGreats(par):  # <>
    match par:
        case ">":
            return True
        case _:
            return False


def CurleyThings(par):  # {}
    match par:
        case "}":
            return True
        case _:
            return False


def Brockets(par):  # []
    match par:
        case "]":
            return True
        case _:
            return False


def part1Func():
    Part1 = 0
    dictionaryOfStuff = {'(': parentheses, '<': angledGreats, '{': CurleyThings, '[': Brockets}
    Openers = list("([{<")
    dictionaryOfPoints = {')': 3, ']': 57, '}': 1197, '>': 25137}

    for line in open("input.txt"):
        stack = Stack()
        for pracket in list(line.strip()):
            if pracket in Openers:
                stack.last = Node(pracket, stack.last)
            elif stack.last is not None:
                if dictionaryOfStuff[stack.last.this](pracket):
                    stack.last = stack.last.next
                else:
                    # print(f"Corrupt: {line.strip()}")
                    Part1 += dictionaryOfPoints[pracket]
                    break
            else:
                print(f"This Failed at: {pracket}")
                exit()
    return Part1


def part2Func():
    Part2 = []
    dictionaryOfStuff = {'(': parentheses, '<': angledGreats, '{': CurleyThings, '[': Brockets}
    Openers = list("([{<")

    for line in open("input.txt"):
        stack = Stack()
        for pracket in list(line.strip()):
            if pracket in Openers:
                stack.last = Node(pracket, stack.last)
            elif stack.last is not None:
                if dictionaryOfStuff[stack.last.this](pracket):  # idk, just wanted to do it this way since I think it is cool.
                    stack.last = stack.last.next
                else:
                    break
            else:
                print(f"This Failed at: {pracket}")
                exit()
        else:
            NumberInHere = 0
            while stack.last is not None:

                match stack.last.this:
                    case "(":
                        NumberInHere = (NumberInHere * 5) + 1
                    case "[":
                        NumberInHere = (NumberInHere * 5) + 2
                    case "{":
                        NumberInHere = (NumberInHere * 5) + 3
                    case "<":
                        NumberInHere = (NumberInHere * 5) + 4
                stack.last = stack.last.next
            Part2.append(NumberInHere)
    return sorted(Part2)[len(Part2) // 2]


if __name__ == '__main__':
    part1, part2 = part1Func(), part2Func()
    print(f"Part 1: {part1}\nPart 2: {part2}")
    pass
