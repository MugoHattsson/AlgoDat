from typing import Deque
from collections import deque
import sys


menList: Deque = deque([])
womenList: dict = {}
N: int = int(sys.stdin.readline())

def main():
    createLists()

    while len(menList) != 0:
        man = menList.popleft()
        woman = womenList[man.propose()]
        if woman.single:
            woman.setHusband(man)
        elif woman.changeHusband(man.identifier):
            menList.append(woman.setHusband(man))
        else:
            menList.append(man)

    for x in range(N):
        print(womenList[x+1])


class Man:
    def __init__(self, identifier, prefList):
        self.identifier: int = identifier
        self.prefList: Deque = prefList
    
    def __str__(self):
        return str(self.identifier)
    
    def propose(self):
        return int(self.prefList.popleft())


class Woman:
    marriedTo: Man
    single: bool

    def __init__(self, identifier, prefList):
        self.identifier: int = identifier
        self.prefList: Deque = prefList
        self.single = True
        self.marriedTo = None
    
    def __str__(self):
        return str(self.marriedTo.identifier)

    def setHusband(self, man):
        self.single = False
        oldHusband = self.marriedTo
        self.marriedTo = man
        return oldHusband

    def changeHusband(self, new):
        return self.prefList[new -1] < self.prefList[self.marriedTo.identifier-1]


def createLists():
    allLines = ' '.join([line.rstrip() for line in sys.stdin]).split(' ')

    for i in range(2*N):
        line = list(map(int, allLines[(i)*(N+1):(i+1)*(N+1)]))

        identifier = line[0]
        prefList = line[1:]

        if identifier in womenList:
            menList.append(Man(identifier, deque(prefList)))
        else:
            womenList[identifier] = Woman(identifier, deque(mapInverse(prefList)))


def mapInverse(list):
    resultList = [0] * N
    for i, v in enumerate(list):
        resultList[v-1] = i
    return resultList
    
if __name__ == '__main__':
    main()

