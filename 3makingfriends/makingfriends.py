import sys
from collections import deque
from collections import defaultdict

LINE = sys.stdin.readline().split(' ')
N: int = int(LINE[0])
M: int = int(LINE[1])
parent = [i for i in range(0,N+1)]
# rank = [0]*(N+1)

def main():
    edges = buildEdges()
    #print(edges)
    print(kruskal(edges))


def kruskal(edges):
    sum = 0

    while(len(edges) != 0):
        u,v,w = edges.popleft()
        parentU = find(u)
        parentV = find(v)
        # rankU = rank[u]
        # rankV = rank[v]

        if parentU != parentV:
            # if rankU > rankV:
            #     parent[parentV] = parentU
            # elif rankU < rankV:
            #     parent[parentU] = parentV
            # else:
            #     parent[parentV] = parentU
            #     rank[u] += 1
            parent[parentV] = parentU
            sum += w

    return sum

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def buildEdges():
    edges = []
    for _ in range(M):
        edges.append(createEdge())
    
    return deque(sorted(edges, key=lambda edge: edge[2]))

def createEdge():
    #edgeTuple = lambda lst: ((lst[0], lst[1]), lst[2]) # [x,y,z] -> ((x,y),z)
    return list(map(int, sys.stdin.readline().split(' ')))

if __name__ == '__main__':
    main()