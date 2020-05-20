import sys

ALPHABET = list(filter(lambda x: x != ' ', sys.stdin.readline()))
ALPHA = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(len(ALPHABET)-1)]

def main():
    Q = int(sys.stdin.readline())
    queries = [query() for _ in range(Q)]

    for q in queries:
        w1, w2 = q
        align(w1, w2)

def query():
    s,t = sys.stdin.readline().rstrip().split(" ")
    return (s,t)

def align(s,t):
    delta = -4
    m = len(s)
    n = len(t)

    # Finds the optimal alignment score
    scoreTable = [[-100 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(0,m):
        scoreTable[i][0] = i*delta
    for j in range(0,n):
        scoreTable[0][j] = j*delta

    for i in range(1,m+1):
        for j in range(1,n+1):
            a = ALPHABET.index(s[i-1])
            b = ALPHABET.index(t[j-1])
            scoreTable[i][j] = max(
                ALPHA[a][b] + scoreTable[i-1][j-1],
                delta + scoreTable[i-1][j],
                delta + scoreTable[i][j-1]
            )


    # Traverses scoreTable to build the optimally aligned strings.
    alignmentA = ""
    alignmentB = ""
    i = len(s)
    j = len(t)

    while i > 0 and j > 0:
        score = scoreTable[i][j]
        scoreDiag = scoreTable[i-1][j-1]
        scoreUp = scoreTable[i][j-1]
        scoreLeft = scoreTable[i-1][j]
        a = ALPHABET.index(s[i-1])
        b = ALPHABET.index(t[j-1])
        if score == scoreDiag + ALPHA[a][b]:
            alignmentA = s[i-1] + alignmentA
            alignmentB = t[j-1] + alignmentB
            i -= 1
            j -= 1
        elif score == scoreLeft + delta:
            alignmentA = s[i-1] + alignmentA
            alignmentB = '*' + alignmentB
            i -= 1
        elif score == scoreUp + delta:
            alignmentA = '*' + alignmentA
            alignmentB = t[j-1] + alignmentB
            j -= 1
        
    while i > 0:
        alignmentA = s[i-1] + alignmentA
        alignmentB = '*' + alignmentB
        i -= 1
    while j > 0:
        alignmentA = '*' + alignmentA
        alignmentB = t[j-1] + alignmentB
        j -= 1
    
    print(alignmentA + " " + alignmentB)



if __name__ == '__main__':
    main()