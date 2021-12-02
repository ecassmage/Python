class Graph:
    def __init__(self, ID):
        self.id = ID
        self.Done = False
        self.nodes = []

    def addNode(self, graph):
        self.nodes.append(graph)

    def printGraphs(self):
        if self.Done:
            return
        print(self.id)
        self.Done = True
        for node in self.nodes:
            node.printGraphs()


if __name__ == "__main__":
    GraphList = [
        Graph(1),
        Graph(2),
        Graph(3),
        Graph(4),
        Graph(5)
    ]
    GraphList[0].addNode(GraphList[1])
    GraphList[0].addNode(GraphList[2])
    GraphList[0].addNode(GraphList[3])
    GraphList[0].addNode(GraphList[4])

    GraphList[1].addNode(GraphList[0])
    GraphList[1].addNode(GraphList[2])
    GraphList[1].addNode(GraphList[3])

    GraphList[2].addNode(GraphList[0])
    GraphList[2].addNode(GraphList[1])
    GraphList[2].addNode(GraphList[4])

    GraphList[3].addNode(GraphList[0])
    GraphList[3].addNode(GraphList[1])

    GraphList[4].addNode(GraphList[0])
    GraphList[4].addNode(GraphList[2])

    GraphList[0].printGraphs()

