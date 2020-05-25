import sys
from collections import deque
from copy import copy, deepcopy


N, M, C, P = map(int, sys.stdin.readline().rstrip().split(' '))

def main():
    graph = [[0 for i in range(N)] for i in range(N)]
    edges = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(M)]
    parent = [-1] * N
    paths = deque([int(sys.stdin.readline()) for _ in range(P)])

    if len(paths) < 3000:
        simple(graph, edges, paths)
    else:
        tester(graph, edges, paths, P/2)

    
def simple(graph, edges, paths):
    result = 0
    while len(paths) > 0:
        p = paths.popleft()
        edges[p][2] = 0
        for u,v,c in edges:
            graph[u][v] = c
            graph[v][u] = c

        flow, graph = max_flow(0, N-1, graph)
        if flow >= C:
            result = flow
        else: 
            break
    
    removed = P - (len(paths) + 1)
    print(str(removed) + " " + str(result))


def popmany(n, paths):
    result = []
    for _ in range(n):
        result.append(paths.popleft())

    return result, paths


def bfs(source, sink, graph):
    visited = [False] * N
    queue = deque()
    queue.append(source)
    visited[source] = True

    while len(queue) > 0:
        u = queue.popleft()

        for i, cap in enumerate(graph[u]):
            if not visited[i] and cap > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = u
    
    return visited[sink]

def max_flow(source, sink, graph):
    global parent
    parent = [-1] * N
    total_flow = 0
    while bfs(source, sink, graph):
        delta = 9223372036854775807
        s = sink
        while s != source:
            delta = min(delta, graph[parent[s]][s])
            s = parent[s]

        total_flow += delta 

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= delta
            graph[v][u] += delta
            v = parent[v]

    return total_flow, graph


def tester(graph, edges, paths, n):
    if n < 5:
        simple(graph, edges, paths)
    else:   
        result, graph, edges, paths = tryRemove(graph, edges, paths, n)
        if result:
            tester(graph, edges, paths, n)
        else:
            tester(graph, edges, paths, n//2)

def tryRemove(graph, edges, paths, n):
    old_graph = deepcopy(graph)
    old_edges = deepcopy(edges)
    old_paths = deepcopy(paths)

    toRemove, paths = popmany(n, paths)
    for e in toRemove:
        edges[e][2] = 0

    for u,v,c in edges:
            graph[u][v] = c
            graph[v][u] = c

    flow, graph = max_flow(0, N-1, graph)
    if flow >= C:
        return True, graph, edges, paths,
    else: 
        return False, old_graph, old_edges, old_paths


if __name__ == '__main__':
    main()