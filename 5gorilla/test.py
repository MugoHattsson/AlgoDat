import sys

Alphabet = list(filter(lambda x: x != ' ', sys.stdin.readline()))
PairTable = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(len(Alphabet)-1)]
#optMatrix = []
Scorespace = -4

def main():
    Q = int(sys.stdin.readline())
    queries = [query() for _ in range(Q)]

    for q in queries:
        w1, w2 = alignments(q)[1]
        print(w1 + " " + w2)


def query():
    s,t = sys.stdin.readline().rstrip().split(" ")
    return (s,t)


def alignments(query):
    # print(query)
    #global optMatrix
    s,t = query
    optMatrix = [[(-100,"") for _ in range(len(t))] for _ in range(len(s))]

    def opt(i,j):
        if (i,j) == (0,0):
            return (0,(s[0],t[0]))
        if j == 0:
            return updateEntry(Scorespace, s[i], '*', opt(i-1,0))
        elif i == 0:
            return updateEntry(Scorespace,'*', t[j], opt(0,j-1))
        elif optMatrix[i][j][0] == -100:
            result = max(
                updateEntry(charScore(s[i], t[j]), s[i], t[j], opt(i-1,j-1)),
                updateEntry(charScore('*', t[j]), '*', t[j], opt(i,j-1)),
                updateEntry(charScore(s[i], '*'), s[i], '*', opt(i-1,j)),
                key=lambda e: e[0]
            )
            optMatrix[i][j] = result
            # print(result)
            
        return optMatrix[i][j]

    return opt(len(s)-1,len(t)-1)

def charScore(x, y):
    if x == '*': return Scorespace 
    elif y == '*': return Scorespace
    else: 
        xInd = Alphabet.index(x)
        yInd = Alphabet.index(y)
        return PairTable[xInd][yInd]

def updateEntry(n, t1, t2, entry):
    score, (w1,w2) = entry
    return (score+n, (w1 + t1, w2 + t2))

if __name__ == '__main__':
    main()