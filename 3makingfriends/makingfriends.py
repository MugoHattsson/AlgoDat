import sys
from collections import deque
from collections import defaultdict

LINE = sys.stdin.readline().split(' ')
N: int = int(LINE[0])
M: int = int(LINE[1])
parent = dict()

def main():
    for v in range(N):
        parent[v+1] = v+1
    edges = buildEdges()
    # print(edges)
    print(kruskal(edges))
    #print(parent)

def kruskal(edges):
    sum = 0
    # ((u,v),w) = edges.popleft()
    # parent[u] = v
    # parent[v] = 0
    
    # while(len(edges) != 0):
    #     ((u,v),w) = edges.popleft()
    #     parentU = find(u)
    #     parentV = find(v)

    #     # if (parentU, parentV) == (u, v):
    #     #     parent[v] = u
    #     #     parent[u] = 0
    #     #     sum += w
    #     # elif parentU != u and parentV == v:
    #     #     parent[v] = u
    #     #     sum += w
    #     # elif parentV != v and parentU == u:
    #     #     parent[u] = v
    #     #     sum += w
    #     # elif 

    #     if parentU != parentV:
    #         #parent[u] = parentV
    #         # if (parent[u], parent[v]) != (0,0):
    #         if parentV == v:
    #             parent[v] = 0
    #         parent[parentU] = parentV
    #         sum += w

    while(len(edges) != 0):
        ((u,v),w) = edges.popleft()
        parentU = find(u)
        parentV = find(v)

        if parentU != parentV:
            parent[parentU] = parentV
            sum += w

    return sum


def find(node):
    p = parent[node]
    if p == node:
        return node
    p = find(p)

def buildEdges():
    edges = []
    for _ in range(M):
        edges.append(createEdge())
    
    return deque(sorted(edges, key=lambda edge: edge[1]))

def createEdge():
    edgeTuple = lambda lst: ((lst[0], lst[1]), lst[2])
    return edgeTuple(list(map(int, sys.stdin.readline().split(' '))))

if __name__ == '__main__':
    main()