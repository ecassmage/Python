import math
import random


class Human:
    def __init__(self, yearBorn, desire):
        self.Name = [self.makeName(True), self.makeName()]
        self.Children = []
        self.Spouse = None
        self.desire = 0
        self.Desire(desire)

        self.yearBorn = yearBorn
        self.Gender = random.randint(0, 1)
        self.age = 0

    @staticmethod
    def makeName(first=False):
        return ""

    def chanceOfChild(self):
        if self.age < 14 or self.age > 59:
            return False
        k = 100 / (3 * 2418.137)
        yesNo = random.randrange(0, 100000)
        # print(f"Number Here: {17.5 * math.sin((self.age/(3 * math.pi)) - (math.pi / 2)) + 17.5}")
        if yesNo/1000 < (17.5 * math.sin((self.age/(3 * math.pi)) - (math.pi / 2)) + 17.5) * (1 / (self.development() * len(self.Children) + 1 + self.desire)):
            self.Children.append("T")
        return yesNo/1000 < (17.5 * math.sin((self.age/(3 * math.pi)) - (math.pi / 2)) + 17.5) * (1 / (self.development() * len(self.Children) + 1 + self.desire))

    def ageUp(self):
        self.age += 1

    def development(self):
        num = (1/1000000) * self.yearBorn * 4
        return num if num <= 4 else 4

    def Desire(self, num):
        if num > 6:
            num = 6
        self.desire = 6 - num


if __name__ == '__main__':
    human = Human(0, 6)
    numOfChildren = []
    average = 0
    for i in range(1000000):
        if human.age >= 60:
            numOfChildren.append(len(human.Children))
            average += len(human.Children)
            human.age = 0
            human.Children = []
            human.yearBorn = i
            human.Desire(random.randint(0, 6))
            print("\n --- Switch --- \n")
        print(f"age: {human.age} had Child: {human.chanceOfChild()}")
        human.chanceOfChild()
        human.ageUp()
    numOfChildren.append(0)
    print(f"{numOfChildren}")
    jumbo = 0
    for i in range(4):
        average2 = 0
        for j in range(int(len(numOfChildren) / 4)):
            if numOfChildren[i*int(len(numOfChildren) / 4) + j] == 0:
                jumbo += 1
            average2 += numOfChildren[i*int(len(numOfChildren) / 4) + j]
        print(f"numbers {i*int(len(numOfChildren) / 4)} - {i*int(len(numOfChildren) / 4) + int(len(numOfChildren) / 4)} have an Average of: {average2 / int(len(numOfChildren) / 4)}")
    print(f"\n{average / len(numOfChildren)} with {jumbo} 0's")
