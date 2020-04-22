import sys
from collections import deque

nodes: dict = {}
LINE = sys.stdin.readline().split(' ')
N: int = int(LINE[0])
Q: int = int(LINE[1])

def main():
    create_graph()

    for _ in range(Q):
        line = sys.stdin.readline().rstrip().split(' ')
        start: str = line[0]
        end: str = line[1]

        bfs(start, end)

def contains(word, other):
    tail = word[1:]
    for char in tail:
        if tail.count(char) > other.count(char):
            return False
    return True

def find_connected(word):
    for node in nodes.keys():
        if node != word and contains(word, node):
            nodes[word].append(node)

def bfs(start: str, end: str):
    if start == end:
        print(0)
        return

    current_nodes = deque()
    current_nodes.append(start)
    visited: set = {start}
    pred: dict = {start : ""}

    def path_length(node, length=0):
        if pred[node] == "":
            return length
        return path_length(pred[node], length + 1)

    while len(current_nodes) != 0:
        current = current_nodes.popleft()
        for neighbour in nodes[current]:
            if not neighbour in visited:
                visited.add(neighbour)
                current_nodes.append(neighbour)
                pred[neighbour] = current
                if neighbour == end:
                    print(path_length(neighbour))
                    return
    print("Impossible")



def create_graph():
    for _ in range(N):
        word = sys.stdin.readline().rstrip()
        nodes[word] = []

    for node in nodes.keys():
        find_connected(node)


if __name__ == '__main__':
    main()
