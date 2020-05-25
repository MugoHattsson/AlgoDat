import sys
from collections import deque
from copy import deepcopy


N, M, C, P = map(int, sys.stdin.readline().rstrip().split(' '))

def main():
    

    graph = [[0 for i in range(N)] for i in range(N)]
    edges = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(M)]
    parent = [-1] * N
    paths = deque([int(sys.stdin.readline()) for _ in range(P)])

    # toRemove, paths = popmany(1830, paths)
    # for e in toRemove:
    #    edges[e][2] = 0
    # simple(graph, edges, paths)

    if len(paths) < 3000:
        # print("simple")
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
        # print(flow)
        if flow >= C:
            result = flow
        else: 
            break
    
    # print(len(paths))
    removed = P - (len(paths) + 1)
    print(str(removed) + " " + str(result))

def advanced(graph, edges, paths):
    result = 0 

    while len(paths) > 0:
        path_len = len(paths)
        if path_len < 40:
            simple(graph, edges, paths)
        else:
            edges_old = deepcopy(edges) # list(edges)
            paths_old = deepcopy(paths) # deque(paths)
            graph_old = deepcopy(graph) # [list(l) for l in graph]
            toRemove, paths = popmany(path_len // 20, paths)
            # print(len(toRemove), path_len)
            for e in toRemove:
                edges[e][2] = 0
            for u,v,c in edges:
                graph[u][v] = c
                graph[v][u] = c

            flow, graph = max_flow(0, N-1, graph)
            if flow >= C:
                result = flow
            else: 
                #print(len(paths))
                #edges = list(edges_old)
                #paths = deque(paths_old) 
                simple(graph_old, edges_old, paths_old)
                break
                


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
    old_paths = deepcopy(paths)
    old_edges = deepcopy(edges)

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