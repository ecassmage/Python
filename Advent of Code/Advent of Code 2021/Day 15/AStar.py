class Node:
    def __init__(self, weight, coordinate):
        self.weight = weight
        self.Parent = None
        self.TargetNode = None

        self.gCost = -1
        self.hCost = -1
        self.fCostVal = -1

        self.Visited = False
        self.adjacentNodes = []
        self.coordinate = tuple(coordinate)

    def setHCost(self):
        self.hCost = self.getDistance(self.TargetNode)

    def getH(self):
        return self.hCost

    def setDistanceFromStart(self):
        pass

    def updateChildren(self):
        for child in self.adjacentNodes:
            if child.Visited:
                continue
            value = self.gCost + self.getDistance(child) + child.weight
            if child.gCost == -1 or value < child.gCost:
                child.gCost = value
                child.hCost = child.getDistance(child.TargetNode)
                child.closestParent = self

    def getDistance(self, child):
        return 10 * (child.coordinate[0] - self.coordinate[0]) + 10 * (child.coordinate[1] - self.coordinate[1])

    def fCost(self):
        self.fCostVal = self.hCost + self.gCost
        return self.fCostVal

    def addAdjacent(self, new):
        if isinstance(new, list):
            for newElement in new:
                self.adjacentNodes.append(newElement)
                newElement.adjacent.append(self)
        else:
            self.adjacentNodes.append(new)
            new.adjacentNodes.append(self)
