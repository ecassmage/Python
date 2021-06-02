import random
import math
import GUI


class Person:
    def __init__(self, name, parent1, parent2):
        self.alive = True
        self.FirstName = name[0]
        self.LastName = name[1]
        self.age = 0
        self.parents = [parent1, parent2]
        self.LNamePreference = 0
        self.spouse = None
        self.Fertility = 0
        self.children = []

        self.familyLines = []
        self.gridSize = 0
        self.depth = 0
        self.tk = None
        self.label = None
        self.coord = ()

    def measureLabel(self):
        self.coord = (self.label.winfo_width(), self.label.winfo_height(), self.label.winfo_x(), self.label.winfo_y())
        print(self.coord)

    def newChild(self, FName):
        if self.LNamePreference == 0:
            child = Person((FName, self.LastName), self, self.spouse)
        else:
            child = Person((FName, self.spouse.LastName), self, self.spouse)
        self.children.append(child)
        child.Fertility = random.randint(-150, 50)
        return child

    def Marriage(self, name):
        self.spouse = Person((name[0], name[1]), None, None)
        self.LNamePreference = random.randint(0, 1)
        if random.randint(0, 1) == 1:
            if self.LNamePreference == 0:
                self.spouse.LastName = self.LastName
            else:
                self.LastName = self.spouse.LastName

    def name(self):
        return self.FirstName + " " + self.LastName


def ChooseRandomName(names, lName=False):
    if lName:
        return random.choice(names[0]), random.choice(names[1])
    return random.choice(names[0])


def writeNameList():
    firstNameList = []
    lastNameList = []
    for line in open("names.txt", 'r'):
        firstNameList.append(line.replace('\n', ''))
    for line in open("lastNames.txt", 'r'):
        lastNameList.append(line.replace('\n', '').lower().capitalize())
    return [firstNameList, lastNameList]


def Odds(check, human):
    """
    :param check:  what are we checking odds for
    :param human:  age of human
    :return:
    """
    def childOdds():
        odds = math.ceil((400 * math.cos(math.radians(18 * (human.age - 25) / 7))) / 2) - 1.8 ** len(2 * human.children) + human.Fertility  # 3.6
        return odds if odds > 10 else 10

    if check == 'child':
        return 0 if human.age > 60 else childOdds()
    elif check == 'death':
        return math.ceil((human.age/60) ** 6)
    else:
        return 0


def YearEvents(names, humans):
    for human in reversed(humans):
        if human.age >= 18 and human.spouse is None and random.randrange(0, 5) == 1:
            human.Marriage(ChooseRandomName(names, True))
        if 55 > human.age >= 18 and human.spouse is not None:
            if len(human.children) < 2:
                oddsOfChild = Odds("child", human)
                if random.randrange(0, 1000) <= oddsOfChild:
                    humans.append(human.newChild((ChooseRandomName(names))))
                    if random.randrange(0, 100) <= 5:
                        humans.append(human.newChild((ChooseRandomName(names))))
        if random.randrange(0, 100) > 100 - Odds('death', human):
            human.alive = False
            humans.pop(humans.index(human))
        else:
            human.age += 1
    return humans


def printFamilyTree(Node, level, TruthList):
    def addTab(number):
        for truth in range(level - number):
            print("║    ", end='') if TruthList[truth] else print("     ", end='')

    addTab(2)
    if level != 1:
        print("╠══ ", end='') if TruthList[level-2] else print("╚══ ", end='')
    print(Node.name())
    for num, child in enumerate(Node.children):
        if num + 1 != len(Node.children):
            TruthList.append(True)
        else:
            TruthList.append(False)
        printFamilyTree(child, level+1, TruthList)
    if level != 1:
        if len(Node.children) > 0 and Node.parents[0].children.index(Node) + 1 < len(Node.parents[0].children):
            addTab(1)
            print()
        TruthList.pop(-1)


def ImmediatePrintFamily(Node):
    print(len(Node.name()))
    longestName = 0
    for child in Node.children:
        if len(child.name()) > longestName:
            longestName = len(child.name())
            print(child.name())
    print(longestName)
    pass


def findGridSizes(node, depth):
    node.label = a.newLabel(None, node.name())
    node.depth = depth
    if len(node.children) == 0:
        node.gridSize = node.label.lengthSize + 5
        return node.gridSize
    else:
        num = 0
        for child in node.children:
            num += findGridSizes(child, depth+1)
        if node.label.coord[0] < num:
            node.gridSize = num + 5
        else:
            node.gridSize = node.label.lengthSize + 5
        return node.label.coord[0] + num


def printFamilyCanvas(node, x=0):

    if node.parents[0] is None:
        x = 2500-node.label.coord[0]
        node.label.label.place(x=x, y=3 * node.label.coord[1] * node.depth)
        node.label.measureLabel()
        x -= node.gridSize / 2
    else:
        node.label.label.place(x=math.floor((2 * x + node.gridSize)/2), y=3 * node.label.label.winfo_height() * node.depth)
        node.label.measureLabel()
        node.familyLines.append(node.label.gui.canvas.create_line(
                (2 * node.parents[0].label.label.winfo_x() + node.parents[0].label.label.winfo_width()) / 2,
                node.parents[0].label.label.winfo_y() + node.parents[0].label.coord[1],
                (2 * node.label.label.winfo_x() + node.label.label.winfo_width()) / 2,
                node.label.label.winfo_y()
            )
        )
        node.label.gui.lines.append(node.familyLines[-1])
    x = math.floor((2 * x + node.gridSize)/2) - node.gridSize/2
    # print(node.name(), x)
    for child in node.children:
        printFamilyCanvas(child, x)
        x += child.gridSize


def printFamily(node):
    findGridSizes(node, 0)
    printFamilyCanvas(node)
    # printFamilyCanvas(node)
    # for child in node.children:
    #     printFamily(child)


def firstParent(names):
    Parent = Person(("Evan", "Morrison"), None, None)
    Parent.age = 18
    Parent.Marriage(ChooseRandomName(names, True))
    Parent.LNamePreference = 0
    Parent.LastName = "Morrison"
    Parent.Fertility = 50
    return Parent


def main():
    names = writeNameList()
    # print(ChooseRandomName(names, True))
    Origin = firstParent(names)
    Humans = [Origin]
    Humans = YearEvents(names, Humans)
    for i in range(150):
        # print("Year %d" % i)
        Humans = YearEvents(names, Humans)
    # print(Humans[0].FirstName, Humans[0].LastName, Humans[0].spouse, Humans[0].LNamePreference, Humans[0].age)
    print("The Tree")
    printFamilyTree(Origin, 1, [])
    print("\n")
    # printFamilyTree(Origin.children[0].children[0].children[0].children[0], 1, [])
    # ImmediatePrintFamily(Origin)
    printFamily(Origin)
    # a.tk.mainloop()
    print("Done")
    # exit()


def goLeft(gui):
    for label in gui.labels:
        label.label.place(
            x=label.label.winfo_x() - 250,
            y=label.label.winfo_y()
        )
    for line in gui.lines:
        coords = gui.canvas.coords(line)
        gui.canvas.coords(line, coords[0] - 250, coords[1], coords[2] - 250, coords[3])


def goRight(gui):
    for label in gui.labels:
        # print(label.label.winfo_x(), 10, label.label.winfo_y())
        label.label.place(
            x=label.label.winfo_x() + 250,
            y=label.label.winfo_y()
        )
    for line in gui.lines:
        coords = gui.canvas.coords(line)
        gui.canvas.coords(line, coords[0] + 250, coords[1], coords[2] + 250, coords[3])


if __name__ == '__main__':
    a = GUI.GUI()
    main()
    a.update()
    # a.newLabel(None, "Evan Morrison")
    # print("hello")
    while True:
        a.tk.bind("<a>", lambda x: goRight(a))
        a.tk.bind("<d>", lambda x: goLeft(a))
        a.update()
