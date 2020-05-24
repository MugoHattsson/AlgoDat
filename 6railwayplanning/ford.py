import sys


# N, M, C, P 
N, M, C, P = map(int, sys.stdin.readline().rstrip().split(' '))
print(N, M, C, P)

def main():

    edges = [map(int, sys.stdin.readline().rstrip().split(' ')) for _ in range(M)]
    # for e in edges: print(str(e))

    graph = {}

    for _ in range(M):
        u,v,c = map(int, sys.stdin.readline().rstrip().split(' '))
        graph[(u,v)] = ((0,0), c)

    print(graph)

    print("Done")

class edge:

    def __init__(self, n1, n2, cap):
        self.n1 = n1
        self.n2 = n2
        self.cap = cap

        self.flow = 0
        self.flowReverse = 0
    

    def capacityLeft(self):
        return self.cap - (self.flow + self.flowReverse)

    def setFlow(self, n1, n2, flw):
        self.flow += flw

    def __str__(self):
        return str(self.n1) + ", " + str(self.n2) + ", " + str(self.flow) + "/" + str(self.cap)

def readEdge():
    u,v,c = map(int, sys.stdin.readline().rstrip().split(' '))
    return edge(u,v,c)
        
if __name__ == '__main__':
    main()