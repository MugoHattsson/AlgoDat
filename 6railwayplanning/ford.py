import sys
from collections import deque


# N, M, C, P 
N, M, C, P = map(int, sys.stdin.readline().rstrip().split(' '))
print(N, M, C, P)

def main():

    nodes = [Node(i) for i in range(N)]
    edges = [map(int, sys.stdin.readline().rstrip().split(' ')) for _ in range(M)]

    print(nodes)

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

    print(nodes)

    print("Done")

def maxFlow(source, sink):
    global nodes
    path = bfs(source, sink)
    while not path: 
        minCap = 9223372036854775807
        for edge in path:
            if edge.cap < minCap:
                minCap = edge.cap

        for edge in path:
            edge.flow += minCap
            edge.opposite.cap = edge.flow
            


def bfs(source, sink):
    if source == sink:
        return []

    current_nodes = deque()
    current_nodes.append(source)
    path = [source]

    while len(current_nodes) != 0:
        current = current_nodes.popleft()
        for edge in current.edges():
            if not edge in path and not edge.opposite in path and edge.capacityLeft > 0: 
                path.append(edge)
                current_nodes.append(nodes[edge.v])
                if current == sink:
                    return path
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
        return str(self.u) + ", " + str(self.v) + ", " + str(self.flow) + "/" + str(self.cap)

    def __repr__(self):
        return str(self)

    def __eq__(self, obj):
        return isinstance(obj, Edge) and obj.u == self.u and obj.v == self.v

def readEdge():
    u,v,c = map(int, sys.stdin.readline().rstrip().split(' '))
    return Edge(u,v,c)
        
if __name__ == '__main__':
    main()