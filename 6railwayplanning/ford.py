import sys
from collections import deque


# N, M, C, P 
N, M, C, P = map(int, sys.stdin.readline().rstrip().split(' '))
nodes = []
edges = [map(int, sys.stdin.readline().rstrip().split(' ')) for _ in range(M)]


def main():
    global nodes

    nodes = [Node(i) for i in range(N)]
    

    # Building graph.
    for u,v,c in edges:
        forwardEdge = Edge(u,v,c)
        reverseEdge = Edge(v,u,c)
        sourceNode = nodes[u]
        sinkNode = nodes[v]

        forwardEdge.opposite = reverseEdge
        reverseEdge.opposite = forwardEdge
        sourceNode.addEdge(forwardEdge)
        sinkNode.addEdge(reverseEdge)

    print(nodes[0],nodes[-1])
    result = maxFlow(nodes[0], nodes[-1])


    print("Done")

def maxFlow(source, sink):
    path = bfs(source, sink)
    print("MF", path)
    while len(path) > 0: 
        minCap = 9223372036854775807
        for edge in path:
            if edge.capacityLeft() < minCap:
                minCap = edge.capacityLeft()

        for edge in path:
            edge.flow += minCap
            edge.opposite.flow += minCap

        path = bfs(source, sink)

    return sum(e.flow for e in source.edges)



def bfs(source, sink):
    if source == sink:
        print("Basfall")
        return []
    print("Sink:",sink)

    current_nodes = deque()
    current_nodes.append(source)
    path = []

    while len(current_nodes) != 0:
        current = current_nodes.popleft()
        for edge in current.edges:
            if not edge in path and not edge.opposite in path and edge.capacityLeft > 0: 
                # print(edge)
                path.append(edge)
                # print(path)
                current_nodes.append(nodes[edge.v])
                print("CS: ", current, edge, sink)
                if current == sink:
                    print("hej")
                    return path
    
    print(path)
    return []

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __str__(self):
        return str(self.name) + ": " + str(self.edges)

    def __repr__(self):
        return str(self)

    def __eq__(self, obj):
        return isinstance(obj, Node) and obj.name == self.name

    def addEdge(self, edge):
        self.edges.append(edge)

class Edge:
    def __init__(self, u, v, cap):
        self.u = u
        self.v = v
        self.cap = cap
        self.flow = 0
        self.opposite = None

    def capacityLeft(self):
        return self.cap - self.flow

    def setFlow(self, u, v, flw):
        self.flow += flw

    def __str__(self):
        return "E: (" + str(self.u) + ", " + str(self.v) + "), " + str(self.flow) + "/" + str(self.cap)

    def __repr__(self):
        return str(self)

    def __eq__(self, obj):
        return isinstance(obj, Edge) and obj.u == self.u and obj.v == self.v

def readEdge():
    u,v,c = map(int, sys.stdin.readline().rstrip().split(' '))
    return Edge(u,v,c)
        
if __name__ == '__main__':
    main()