import sys
import time
from collections import deque
from collections import defaultdict
import multiprocessing as mp

nodes = defaultdict(list)
LINE = sys.stdin.readline().split(' ')
N: int = int(LINE[0])
Q: int = int(LINE[1])

def main():
    create_graph()

    # print("Printing")
    # for node in nodes.keys():
    #     print(node, ": ", nodes[node])

    for _ in range(Q):
        line = sys.stdin.readline().rstrip().split(' ')
        start: str = line[0]
        end: str = line[1]

        bfs(start, end)

    # for node in nodes:
    #     print(node, ": ", nodes[node])

def contains(word, other):
    tail = word[1:]
    for char in tail:
        if tail.count(char) > other.count(char):
            return False
    return True

# def find_connected(word, words):
#     global nodes
#     #print("fc: ", word)
#     for other in words:
#         #print("Iter: ", other)
#         if other != word and contains(word, other):
#             #print("Appending: ", other)
#             nodes[word].append(other)

def find_connected(word, words, return_dict):
    result = []
    for other in words:
        if other != word and contains(word, other):
            result.append(other)
    return_dict[word] = result
            

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
    #pool = mp.Pool(mp.cpu_count())
    global nodes

    keys = []
    processes = []
    return_dict = mp.Manager().dict()

    for _ in range(N):
        word = sys.stdin.readline().rstrip()
        keys.append(word)

    for word in keys:
        p = mp.Process(target=find_connected, args=(word,keys, return_dict))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    nodes = return_dict

    #nodes = dict([pool.apply(find_connected, args=(node, keys)) for node in keys])

    #pool.close()


if __name__ == '__main__':
    main()
