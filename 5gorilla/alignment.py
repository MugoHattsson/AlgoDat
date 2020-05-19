import sys

Alphabet = list(filter(lambda x: x != ' ', sys.stdin.readline()))
PairTable = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(len(Alphabet)-1)]
optMatrix = []
Scorespace = -4

def main():
    Q = int(sys.stdin.readline())
    queries = [query() for _ in range(Q)]

    for q in queries:
        align(q)


def query():
    s,t = sys.stdin.readline().rstrip().split(" ")
    return (s,t)


def charScore(a, b):
    if a == '*' or b == '*':
        return Scorespace
    else: 
        return PairTable[Alphabet.index(a)][Alphabet.index(b)]

def align(query):
    global optMatrix
    s,t = query
    i = len(s)-1
    j = len(t)-1
    optMatrix = [[(-100,"") for _ in range(len(t))] for _ in range(len(s))]
    # print(newOpt(i,j, (0,query)))
    print(optMatrix)


# def newOpt(i, j, a):
#     global optMatrix

#     optMatrix[i][j] = max(

#     )



if __name__ == '__main__':
    main()

class Alignment:
    
    def __init__(self, w1="", w2="", score=-100):
        self.w1 = w1
        self.w2 = w2
        self.score = score
    
    def __str__(self):
        return self.w1 + "  " + self.w2 + "   -   " + str(self.score)

    def add(self, a, b):
        self.w1 += a
        self.w2 += b
        self.score += charScore(a, b)

    def duplicateAdd(self, ali, a, b):
        return (Alignment(self.w1, self.w2, self.score)).add(a, b)

    def setAlignment(self, ali, a, b):
        self = ali
        self.add(a, b)
    
    def value(self):
        return self.score
    


def opt(i,j, queryScore):
    global optMatrix
    s,t = queryScore[1]

    if i == 0:
        return addChar(queryScore, i*'*', t[j], i*Scorespace)
    elif j == 0:
        return addChar(queryScore, s[i], j*'*', j*Scorespace)
    elif optMatrix[i][j][0] == -100:
        score = charScore(s[i],t[j])
        optMatrix[i][j] = max(
            (opt(i-1, j-1, addChar(queryScore, s[i], t[j], score)),
            opt(i, j-1, addChar(queryScore, "*", t[j], score)),
            opt(i-1, j, addChar(queryScore, s[i], "*", score))), key=lambda x: x[0]


            # charScore(s[i],t[j]) + opt(i-1,j-1, query),
            # Scorespace + opt(i,j-1, query),
            # Scorespace + opt(i-1,j, query)
        )
    return optMatrix[i][j]

def addChar(qs, a, b, score):
    newScore = qs[0] + score
    w1 = qs[1][0] + a
    w2 = qs[1][1] + b
    return (newScore, (w1, w2))

