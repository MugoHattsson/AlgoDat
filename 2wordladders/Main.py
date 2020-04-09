import sys
import collections

nodes: dict = {}
LINE = sys.stdin.readline().split(' ')
N: int = int(LINE[0])
Q: int = int(LINE[1])

def main():
    createGraph()

    for _ in range(Q):
        line = sys.stdin.readline().rstrip().split(' ')
        start: Node = nodes[line[0]]
        end: Node = nodes[line[1]]

        resetNodes()

        bfs(start, end)

class Node:
    def __init__(self, word):
        self.word = word
        self.connected: list = []
        self.visited = False
        self.pred: Node = None

    def __eq__(self, obj):
        return isinstance(obj, Node) and obj.word == self.word

    def findConnected(self):
        for currentNode in nodes.values():
            if currentNode != self and self.contains(currentNode.word):
                self.connected.append(currentNode)

    def contains(self, otherWord):
        tail = self.word[1:]
        for char in tail:
            if tail.count(char) > otherWord.count(char):
                return False
        return True

def resetNodes():
    for node in nodes.values():
        node.visited = False


def bfs(start, end):
    if start == end:
        print(0)
        return
    currentNodes = collections.deque()
    currentNodes.append(start)
    start.visited = True
    start.pred = None

    while len(currentNodes) != 0:
        current = currentNodes.popleft()
        for neighbour in current.connected:
            if not neighbour.visited:
                neighbour.visited = True
                currentNodes.append(neighbour)
                neighbour.pred = current
                if neighbour == end:
                    print(pathLength(neighbour))
                    return
    print("Impossible")

def pathLength(node, length=0):
    if node.pred is None:
        return length
    return pathLength(node.pred, length + 1)

def createGraph():
    for _ in range(N):
        word = sys.stdin.readline().rstrip()
        nodes[word] = Node(word)

    for node in nodes.values():
        node.findConnected()


if __name__ == '__main__':
    main()
